# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

An ed-tech company runs a **standalone LangChain RAG chain** for course policies. Every student question triggers retrieval, even when the student only asks: *"What is the status of ticket TKT-51001?"*

What is the **main limitation** of this design compared to an **integrated tool-calling agent**?

A. The chain cannot search policy documents at all  
B. The chain always retrieves documents and cannot autonomously choose a ticket-lookup tool instead  
C. The chain automatically refuses all out-of-domain questions without any prompt rules  
D. The chain stores chat history in Chroma by default

**Correct Answer:** B

**Answer Explanation:**  
A standalone RAG chain follows a fixed retrieve-then-answer path. An integrated agent can **arbitrate** between a retriever-backed tool and auxiliary tools such as ticket lookup.

**Why other options are wrong:**  
- A: RAG chains are built for document search; that is not the limitation here.  
- C: Refusal behaviour depends on prompts, not on chain vs agent architecture alone.  
- D: Chat history is a separate memory concern, not a default Chroma feature.

---

## Q2 (MCQ, Easy)

A developer wraps an existing Chroma retriever using:

```python
course_policy_tool = create_retriever_tool(
    retriever=retriever,
    name="course_policy_tool",
    description="Search official course policy documents for refund and attendance rules.",
)
```

What is the **primary purpose** of `create_retriever_tool`?

A. Fine-tune the LLM on every policy PDF  
B. Expose the retriever as a callable tool the agent can select like any other `@tool`  
C. Delete the vector database after each query  
D. Replace `AgentExecutor` with an LCEL chain

**Correct Answer:** B

**Answer Explanation:**  
`create_retriever_tool` turns a retriever into a **tool contract** (name + description) so a tool-calling agent can invoke policy search when appropriate.

**Why other options are wrong:**  
- A: No fine-tuning happens in this wrapper.  
- C: Chroma data remains unless you delete it explicitly.  
- D: Agents and LCEL chains solve different orchestration patterns.

---

## Q3 (MCQ, Easy)

A course support agent has two tools:

- **`course_policy_tool`** — searches policy documents  
- **`get_ticket_status`** — looks up a ticket ID in a support database  

A student asks: *"What is the status of ticket TKT-1002?"*

Which tool should the agent call **first**?

A. `course_policy_tool`  
B. `get_ticket_status`  
C. Both tools in every case  
D. Neither — the LLM should answer from general world knowledge

**Correct Answer:** B

**Answer Explanation:**  
Ticket status is **live operational data** tied to a ticket ID, not a paragraph inside the policy corpus. That is a **tool-first** routing case.

**Why other options are wrong:**  
- A: Policy search does not return ticket workflow status.  
- C: Both tools are needed only when the user asks for policy **and** ticket facts together.  
- D: Production support bots should use registered tools, not open-ended trivia.

---

## Q4 (MCQ, Easy)

In a tool-calling agent prompt you define:

```python
MessagesPlaceholder(variable_name="chat_history", optional=True),
("human", "{input}"),
MessagesPlaceholder(variable_name="agent_scratchpad"),
```

Turn 1: *"My ticket is TKT-51001."*  
Turn 2: *"What is the status of it?"*

Which placeholder helps the agent resolve *"it"* as **TKT-51001**?

A. `agent_scratchpad` only  
B. `chat_history` only  
C. Both placeholders store the same past user-assistant turns  
D. Neither — the LLM always remembers prior turns without placeholders

**Correct Answer:** B

**Answer Explanation:**  
**`chat_history`** holds prior **user ↔ assistant** messages across invocations. **`agent_scratchpad`** holds tool steps for the **current** run only.

**Why other options are wrong:**  
- A: Scratchpad tracks tool calls inside one execution, not multi-turn dialogue memory.  
- C: They serve different roles and are filled differently.  
- D: You must pass and maintain history explicitly (or use a history helper).

---

## Q5 (MCQ, Moderate)

After shipping a course support agent, the team notices: refund questions sometimes call **`get_ticket_status`** instead of **`course_policy_tool`**, even though the code runs without errors.

What is the **most practical first fix**?

A. Increase `max_iterations` to 100  
B. Rewrite tool descriptions and system prompt routing rules so each tool's *when to use* is explicit  
C. Delete Chroma and stop using retrieval entirely  
D. Switch from `gpt-4o-mini` to a smaller embedding model

**Correct Answer:** B

**Answer Explanation:**  
This is a **wrong tool** failure signature. Clear tool **contracts** (name + description + prompt rules) are the first arbitration fix before tuning retrieval knobs.

**Why other options are wrong:**  
- A: More iterations do not fix incorrect tool choice.  
- C: Removing retrieval breaks policy questions.  
- D: Embedding model changes address weak retrieval, not tool routing.

---

## Q6 (MCQ, Moderate)

A developer wires `MessagesPlaceholder("chat_history")` and passes `chat_history=[]` on every `invoke`, but **never appends** `HumanMessage` / `AIMessage` after each reply.

What symptom appears on turn 2?

A. The agent cannot call any tools on turn 1  
B. Turn 2 behaves like turn 1 with **no memory** of earlier messages  
C. Chroma automatically stores chat history  
D. `agent_scratchpad` replaces the need to append messages

**Correct Answer:** B

**Answer Explanation:**  
The placeholder reserves space; **you** must append messages after each `invoke`. Without append, the list stays empty — classic **missing memory** behaviour.

**Why other options are wrong:**  
- A: Turn 1 can still work; the bug shows on follow-ups.  
- C: Chroma stores document vectors, not dialogue turns.  
- D: Scratchpad does not persist cross-turn user facts.

---

## Q7 (MSQ, Moderate)

Which components are **required** to run a LangChain **tool-calling agent with conversational memory** like the course support demo?

A. `create_tool_calling_agent` bound to an LLM, tools, and prompt  
B. `AgentExecutor` with the same `tools` list and parameters such as `max_iterations`  
C. `MessagesPlaceholder` for `agent_scratchpad` in the prompt  
D. `RunnablePassthrough` as a substitute for `chat_history`

**Correct Answers:** A, B, C

**Answer Explanation:**  
The agent graph, executor loop, scratchpad placeholder, and manual or automatic **`chat_history`** maintenance form the integrated pattern taught in the lab.

**Why other options are wrong:**  
- D: `RunnablePassthrough` forwards inputs in LCEL chains; it does not replace conversational memory in agent prompts.

---

## Q8 (MSQ, Moderate)

An **EvalPack** row for the course support agent includes:

```python
{
    "name": "refund_policy",
    "input": "What is the refund policy within the first week?",
    "expected_tool": "course_policy_tool",
    "expected_keywords": ["7 days", "refund", "30 days"],
    "failure_type": "weak_retriever_or_missing_retrieval",
}
```

Which statements about this EvalPack design are **correct**?

A. `expected_tool` helps verify **tool arbitration** for in-domain policy questions  
B. `expected_keywords` supports checking grounded answer content after a run  
C. `failure_type` suggests what to fix if the case fails (retrieval vs routing)  
D. EvalPack rows must always set `expected_tool` to `get_ticket_status`

**Correct Answers:** A, B, C

**Answer Explanation:**  
Compact eval cases combine **routing expectations**, **answer checks**, and **failure hints** for regression testing.

**Why other options are wrong:**  
- D: Each case sets the tool that **should** fire for that scenario; ticket cases use `get_ticket_status`, policy cases use `course_policy_tool`.

---

## Q9 (MSQ, Hard)

A team debugs a course support agent and records these **failure signatures**. Which **first-fix** statements are **correct**?

A. **Wrong tool** (policy question calls `get_ticket_status`) → improve tool descriptions and routing rules in the system prompt  
B. **Weak retrieval** (right tool, irrelevant policy chunk) → tune `chunk_size`, `chunk_overlap`, or retriever `k`  
C. **Over-refusal** (agent refuses when policy exists in corpus) → review overly strict refusal wording in the system prompt  
D. **Wrong tool** failures → fix first by setting LLM `temperature=1.0` so the model explores more random tools

**Correct Answers:** A, B, C

**Answer Explanation:**  
Wrong-tool, weak-retrieval, and over-refusal fixes map to **contracts**, **retrieval tuning**, and **prompt strictness** respectively — the debugging order taught for integrated agents.

**Why other options are wrong:**  
- D: Higher temperature increases randomness; it does not repair tool arbitration. Routing fixes start with descriptions and prompt rules, not temperature tricks.

---

## Q10 (MSQ, Hard)

A course support agent exposes **`course_policy_tool`** and **`get_ticket_status`**. The system prompt says the bot only helps with **course policies and support tickets**.

For each user message, which routing outcomes are **correct**?

A. *"What is the refund policy?"* → call `course_policy_tool`  
B. *"Status of ticket TKT-51001?"* → call `get_ticket_status`  
C. *"Who won IPL 2025?"* → refuse politely; do not invent an answer from tools  
D. *"What is the refund policy?"* → always call `get_ticket_status` first, then never retrieve

**Correct Answers:** A, B, C

**Answer Explanation:**  
In-domain policy → retriever tool. Ticket ID → auxiliary tool. Out-of-domain sports trivia → guarded refusal without tool misuse.

**Why other options are wrong:**  
- D: Refund policy lives in documents; forcing ticket lookup first is incorrect arbitration.
