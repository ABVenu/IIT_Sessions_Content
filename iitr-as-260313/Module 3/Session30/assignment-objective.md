# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy -> Moderate -> Hard

Question Types:
- 6 MCQ (Single Correct): Q1-Q6
- 4 MSQ (Multiple Correct): Q7-Q10

---

## Q1 (MCQ, Easy)
Riya uses a plain LLM API wrapper with no history passed between calls. In turn 1 she says: *"My order ID is ORD102."* In turn 2 she asks: *"What is the refund status of it?"* What is the most likely behavior?

A. The model automatically remembers ORD102 from turn 1  
B. Turn 2 behaves like a fresh request unless prior messages are sent again  
C. The API stores all chats permanently in the model weights  
D. Turn 2 always calls the correct tool without any context wiring

**Correct Answer:** B

**Answer Explanation:**  
Default LLM API calls are stateless. Without explicitly attaching prior messages (or a memory layer), turn 2 cannot rely on turn 1 facts.

**Why other options are wrong:**  
- A: Stateless calls do not retain prior turns by default.  
- C: Model weights are not updated per user chat at inference time.  
- D: Tool use still needs context; it will not magically recall ORD102.

---

## Q2 (MCQ, Easy)
In a `ChatPromptTemplate`, you add:

```python
MessagesPlaceholder(variable_name="chat_history", optional=True)
```

What does `MessagesPlaceholder` do by itself?

A. Automatically saves every user and AI message into a database  
B. Reserves a slot in the prompt where a message list can be injected at runtime  
C. Replaces the need for `AgentExecutor`  
D. Stores tool intermediate steps across different user sessions

**Correct Answer:** B

**Answer Explanation:**  
`MessagesPlaceholder` only defines where history will appear in the prompt. Your application (or `RunnableWithMessageHistory`) must supply and update the actual messages.

**Why other options are wrong:**  
- A: No automatic persistence is provided by the placeholder alone.  
- C: Executor is still required to run the agent loop.  
- D: Cross-session tool storage is not the placeholder's role; scratchpad handles current-run tool steps.

---

## Q3 (MCQ, Easy)
Why is `optional=True` commonly set on the `chat_history` placeholder?

A. To disable tool calling on the first turn  
B. To allow the first turn to run when history is still empty  
C. To force the model to invent fake prior messages  
D. To merge all users into one shared conversation

**Correct Answer:** B

**Answer Explanation:**  
On the first message, `chat_history` is often `[]`. `optional=True` prevents errors when that list is empty.

**Why other options are wrong:**  
- A: Tool calling is unrelated to this flag.  
- C: It does not fabricate history.  
- D: Session isolation is a separate design concern.

---

## Q4 (MCQ, Easy)
In a tool-calling agent prompt, what is the primary role of `MessagesPlaceholder(variable_name="agent_scratchpad")`?

A. Store all customer chats from the last 30 days  
B. Hold intermediate tool-call steps for the current agent run  
C. Replace `chat_history` for follow-up questions like *"track it"*  
D. Persist order IDs in a SQL database

**Correct Answer:** B

**Answer Explanation:**  
`agent_scratchpad` is working memory for the active invocation (tool chosen, inputs, observations), not long-term dialogue memory.

**Why other options are wrong:**  
- A/C: Long-term / cross-turn recall is handled by `chat_history`, not scratchpad.  
- D: Database persistence is an application-level choice, not scratchpad's default job.

---

## Q5 (MCQ, Moderate)
Arjun's agent has `MessagesPlaceholder("chat_history")`, passes `chat_history=[]` on every `invoke`, and never appends messages after responses. Turn 1 shares an order ID; turn 2 asks *"What is the status of it?"* The app runs without errors but fails to recall the ID. What is the most likely root cause?

A. `max_iterations` is too high  
B. History slot exists in the prompt, but the list is never updated after each turn  
C. `agent_scratchpad` is missing, so tools cannot run  
D. `optional=True` prevents any memory from ever working

**Correct Answer:** B

**Answer Explanation:**  
This is the classic wiring bug: the placeholder reserves space, but without post-invoke `append` of `HumanMessage` and `AIMessage`, later turns still see empty history.

**Why other options are wrong:**  
- A: Iteration limits do not cause ID amnesia across turns.  
- C: Tools can still run; context for follow-ups is missing.  
- D: `optional=True` allows empty first turn; it does not block updates you add manually.

---

## Q6 (MCQ, Moderate)
A food-delivery bot receives:  
Turn 1 — *"Deliver to Flat 12B, Green Park."*  
Turn 2 — *"How far is the rider from here?"*  

Which design choice most directly enables correct turn 2 behavior?

A. Pass rolling `chat_history` (prior human/AI turns) into each new `invoke`  
B. Increase model temperature to 1.0  
C. Remove `agent_scratchpad` to save tokens  
D. Call `invoke` with only turn 2 text and `chat_history=[]` every time

**Correct Answer:** A

**Answer Explanation:**  
Follow-ups with pronouns (*here*, *it*) need prior turns in `chat_history` so the model can resolve references.

**Why other options are wrong:**  
- B: Temperature affects randomness, not memory.  
- C: Scratchpad helps tool loops within a turn; removing it does not add dialogue memory.  
- D: Stateless invocation repeats the turn 2 failure pattern.

---

## Q7 (MSQ, Moderate)
You are building a manual-memory tool-calling agent (no `RunnableWithMessageHistory` yet). Which practices are correct?

A. Use the same variable name in the placeholder and in `invoke` (e.g., `chat_history`)  
B. After each `invoke`, append `HumanMessage` then `AIMessage` to the same list  
C. Append only `AIMessage` and skip the user line to save tokens  
D. Set `optional=True` on the `chat_history` placeholder when the first turn may be empty

**Correct Answers:** A, B, D

**Answer Explanation:**  
Correct manual wiring requires key/name alignment, post-turn append in conversational order, and optional empty history on turn one.

**Why option C is wrong:**  
Skipping the human line breaks turn pairing and confuses the model about what the user actually asked.

---

## Q8 (MSQ, Moderate)
A startup runs a support bot for 500 concurrent users. Which statements about session-scoped memory are correct?

A. Each user/conversation should map to its own history bucket (e.g., `session_id`)  
B. One global `chat_history` list shared by all users is a serious design mistake  
C. `config={"configurable": {"session_id": "..."}}` helps select the right bucket in auto-memory setups  
D. `InMemoryChatMessageHistory` automatically writes to PostgreSQL on every message

**Correct Answers:** A, B, C

**Answer Explanation:**  
Per-session stores prevent cross-user leakage. Configurable `session_id` routes requests in `RunnableWithMessageHistory` patterns. In-memory stores live in RAM unless you add persistence.

**Why option D is wrong:**  
In-memory history does not imply database persistence by default.

---

## Q9 (MSQ, Hard)
Regarding `chat_history` versus `agent_scratchpad` in LangChain tool-calling agents, which statements are correct?

A. `chat_history` carries prior user/assistant turns across separate invocations  
B. `agent_scratchpad` supports tool-step continuity within the current run  
C. `agent_scratchpad` alone is enough for turn 2 to resolve *"status of it"* without `chat_history`  
D. Agents that handle follow-up questions after tool use typically need both placeholders

**Correct Answers:** A, B, D

**Answer Explanation:**  
Dialogue memory and per-run tool traces solve different problems; follow-up pronouns need `chat_history`, while multi-step tool chains need scratchpad.

**Why option C is wrong:**  
Scratchpad resets per invocation and does not store prior user turns for pronoun resolution.

---

## Q10 (MSQ, Hard)
Your team is comparing stateless and memory-enabled agent designs before production rollout. Which statements are correct?

A. The same `AgentExecutor` can demonstrate both patterns by changing only how `chat_history` is passed  
B. Turn 2 follow-ups with pronouns typically fail when `chat_history` is always passed as an empty list  
C. In-memory session history survives application restart without any external database  
D. `input_messages_key` in `RunnableWithMessageHistory` must match the user-input key used in the prompt template

**Correct Answers:** A, B, D

**Answer Explanation:**  
Stateless vs memory-enabled behavior is mainly a wiring difference in history passing. Empty history on every call reproduces stateless failure on follow-ups. Auto-memory wrappers require aligned input keys between config and prompt.

**Why option C is wrong:**  
In-memory stores are ephemeral; restart clears RAM unless history is persisted externally (for example, in a database).
