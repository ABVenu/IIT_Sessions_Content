# Objective Assignment — Short-Term vs Long-Term Memory in AI Agents

**Total Questions:** 10 | **MCQs:** 6 (4 Easy, 2 Moderate) | **MSQs:** 4 (2 Moderate, 2 Hard)

---

## Q1 — Multiple Choice (Single Correct) | Easy

Riya is using an AI writing assistant to draft a business proposal. She starts the chat by saying "I'm writing a proposal for a healthcare startup." Two messages later, she asks "Can you add a section about our target audience?" and the agent correctly builds on the earlier context. However, when she closes the browser and reopens the chat the next day, the agent has no memory of the healthcare startup or the proposal.

Which type of memory was the agent relying on during that original session?

- A) Long-Term Memory
- B) Short-Term Memory
- C) Procedural Memory
- D) Semantic Memory

**Correct Answer:** B

**Answer Explanation:**
Short-Term Memory (STM) lives only within the current session — it is stored in the context window and disappears once the session ends. The agent could refer to the healthcare startup *within* the session because the earlier message was still in the context window. But when the browser was closed, the session ended and no information was persisted, which is why the agent had no recollection on the next day. Long-Term Memory would have survived across sessions. Procedural Memory stores workflows. Semantic Memory stores factual world knowledge.

---

## Q2 — Multiple Choice (Single Correct) | Easy

Arjun is debugging an AI customer support bot. He notices that when a conversation runs past 50 messages, the bot starts forgetting details mentioned at the very beginning. His tech lead explains: *"The model can only act on what's currently on its desk — everything else is invisible to it."*

Which concept is the tech lead describing?

- A) Vector Database
- B) Episodic Memory
- C) Context Window
- D) Summary Memory

**Correct Answer:** C

**Answer Explanation:**
The context window is the maximum amount of text (measured in tokens) that an LLM can read and process in a single call. Everything the model "sees" — user questions, its own past answers, and system instructions — must fit within this window. The "desk" analogy maps directly to the context window: only what is placed on the desk is visible to the model. A Vector Database is an external storage system. Episodic Memory is a type of long-term memory. Summary Memory is a strategy for managing conversation history.

---

## Q3 — Multiple Choice (Single Correct) | Easy

A team building a legal document analysis agent decides to send the entire conversation history to the LLM with every new request — no deletions, no compressions, no filtering of any kind. The product manager explains: *"We cannot afford to lose even a single word from the discussion."*

Which short-term memory strategy is this team using?

- A) Window Memory
- B) Summary Memory
- C) Episodic Memory
- D) Buffer Memory

**Correct Answer:** D

**Answer Explanation:**
Buffer Memory stores and passes the *complete, unmodified* conversation history to the model on every request. Nothing is ever deleted, summarised, or filtered — the full message list is passed as-is. It is the right choice when every word of prior context matters, such as in legal discussions where precision is paramount. Window Memory keeps only the last N messages. Summary Memory compresses older messages into a brief. Episodic Memory is a type of long-term memory, not a short-term strategy.

---

## Q4 — Multiple Choice (Single Correct) | Easy

A health AI assistant is asked: *"What are the side effects of Metformin?"* It answers correctly without any prior conversation about the topic — the knowledge was loaded into the system long before the question was asked. The answer came from a knowledge base containing medical facts, drug information, and clinical guidelines.

Which type of long-term memory does this represent?

- A) Episodic Memory
- B) Procedural Memory
- C) Semantic Memory
- D) Buffer Memory

**Correct Answer:** C

**Answer Explanation:**
Semantic Memory stores factual knowledge about the world — facts, concepts, definitions, and domain expertise that are not tied to any specific past event or conversation. A medical knowledge base containing drug information and clinical guidelines is a classic example of semantic memory. Episodic Memory stores specific past interactions (e.g., "Last Tuesday, user Ravi asked about restaurants"). Procedural Memory stores step-by-step workflows. Buffer Memory is a short-term memory management strategy, not a type of long-term memory.

---

## Q5 — Multiple Choice (Single Correct) | Moderate

An AI fitness coach starts a session by gathering key context: *"I see you're 28 years old, training for a 5K run, and have a right knee injury — I'll keep that in mind."* The conversation runs for 45 turns. At turn 46, the user says: *"Suggest a warm-up routine for today."* The agent recommends high-impact jumping jacks. The user is frustrated — the agent has completely forgotten the knee injury.

The system uses **Window Memory with a window size of 10**. What is the most likely cause of this failure?

- A) The model's context window was too small for the current session
- B) The agent did not have a Long-Term Memory system — session data was never persisted
- C) The knee injury information, mentioned at the very start, has been dropped outside the 10-message window
- D) The summarisation step failed to compress the early messages correctly

**Correct Answer:** C

**Answer Explanation:**
Window Memory keeps only the last N messages and discards everything older. With a window size of 10, any message from more than 10 turns ago is invisible to the model. The knee injury was mentioned at turn 1 and is now far outside the sliding window — the model genuinely cannot see it. This is the classic trade-off of Window Memory: important early context can be permanently dropped. The context window is not the issue (the architecture is working exactly as designed). There is no summarisation step in Window Memory — that is a different strategy.

---

## Q6 — Multiple Choice (Single Correct) | Moderate

A junior developer is reviewing the following snippet from a Window Memory implementation:

```python
WINDOW_SIZE = 6
full_history = []  # Currently has 20 messages stored

recent_history = full_history[-WINDOW_SIZE:]
response = call_llm(messages=recent_history)
```

The junior developer asks: *"How many messages does the LLM actually receive when `call_llm` is invoked?"*

- A) 20
- B) 14
- C) 8
- D) 6

**Correct Answer:** D

**Answer Explanation:**
`full_history[-WINDOW_SIZE:]` uses Python list slicing to retrieve the **last `WINDOW_SIZE` elements** of the list. With `WINDOW_SIZE = 6` and `full_history` containing 20 messages, the expression `full_history[-6:]` returns the 6 most recent messages. These are the only messages passed to `call_llm`. The remaining 14 earlier messages remain stored in `full_history` for record-keeping purposes but are not sent to the model — this is precisely how Window Memory bounds the context size.

---

## Q7 — Multiple Select (Multiple Correct) | Moderate

DataFlow AI is building a B2B analytics assistant that helps business analysts during hour-long sessions with 50+ message exchanges. The engineering team plans to use **Buffer Memory** to ensure the agent never loses any conversation context.

Which of the following are genuine risks or limitations of this decision? *(Select all that apply)*

- A) The model will be unable to understand any question asked after the first 10 turns
- B) API call costs will increase with every new message sent, since the full history is resent each time
- C) The conversation history may eventually exceed the model's maximum context window size
- D) As the context grows very large, the model may pay less attention to important messages mentioned early in the session
- E) The agent will lose its system prompt instructions permanently after turn 5

**Correct Answers:** B, C, D

**Answer Explanation:**
- **B ✓** — In Buffer Memory, the full conversation history is sent with every API call. Since pricing is typically per token, longer conversations mean higher costs per call — and this cost grows linearly with every new turn.
- **C ✓** — Every model has a maximum context window size. As the buffer grows indefinitely across 50+ message sessions, it will eventually hit this ceiling, forcing older messages to be dropped.
- **D ✓** — Performance degradation is a documented limitation — models can lose effective "attention" to messages buried deep in a very long context, making important early information less influential.
- **A ✗** — The model can understand questions at any turn; Buffer Memory passes all history, so the model sees the full conversation. This option confuses the behaviour of Window Memory with Buffer Memory.
- **E ✗** — The system prompt is part of the context and is not dropped in Buffer Memory; it stays at the top of the message list on every call.

---

## Q8 — Multiple Select (Multiple Correct) | Moderate

Meera is evaluating memory strategies for her AI-powered journaling assistant. She wants a strategy that keeps conversations manageable in length while still retaining the key themes and preferences mentioned earlier in the session. She reads about **Summary Memory**.

Which of the following statements accurately describe the Summary Memory strategy? *(Select all that apply)*

- A) It passes the complete, unmodified history to the LLM on every call
- B) Older messages are compressed into a running summary to keep the context compact
- C) The summarisation process requires an additional LLM call, adding a small processing overhead
- D) Once messages are compressed into a summary, their verbatim content may be lost
- E) Summary Memory produces identical token costs to Window Memory

**Correct Answers:** B, C, D

**Answer Explanation:**
- **B ✓** — Summary Memory replaces older raw messages with a compressed summary rather than keeping every message in full. Only the summary and the most recent messages are passed to the model.
- **C ✓** — Summarisation is achieved by making a separate LLM call (e.g., `call_llm(messages=[{"role": "user", "content": summary_prompt}])`), which adds a small but real processing and cost overhead.
- **D ✓** — Summarisation is inherently lossy — exact phrasing, nuance, and specific wording from old messages are not preserved; only the key facts and themes survive.
- **A ✗** — This describes Buffer Memory, not Summary Memory. Summary Memory explicitly compresses and replaces old messages.
- **E ✗** — Summary Memory incurs additional token cost from the summarisation call itself, making its cost profile different from — and in some cases higher than — Window Memory.

---

## Q9 — Multiple Select (Multiple Correct) | Hard

A hospital has deployed an AI clinical assistant called MedAI. It stores the following items between sessions:

| Item | Stored Information |
|---|---|
| **Item 1** | "Patient Arun Sharma, age 42, has Type 2 diabetes. He prefers bullet-point summaries and his last consultation was on April 15th." |
| **Item 2** | "Metformin is a biguanide-class drug used as first-line treatment for Type 2 diabetes. It works by reducing hepatic glucose production." |
| **Item 3** | "When a patient reports chest pain, always follow this protocol: Step 1 — confirm duration and radiation of pain; Step 2 — ask about breathlessness; Step 3 — escalate to emergency if two or more red flags are present." |
| **Item 4** | "In the session on April 15th, Arun reported mild fatigue after starting Metformin. The doctor suggested monitoring for two weeks." |

Which of the following correctly classify these items by long-term memory type? *(Select all that apply)*

- A) Item 1 is Episodic Memory — it records a specific patient's personal details and past consultation date
- B) Item 1 is Semantic Memory — it contains factual information about the patient
- C) Item 2 is Semantic Memory — it stores factual, domain-specific pharmacological knowledge
- D) Item 3 is Procedural Memory — it defines a step-by-step clinical escalation workflow
- E) Item 4 is Episodic Memory — it records a specific past interaction with context, time, and event details
- F) Item 4 is Procedural Memory — it stores how the agent should respond to Metformin queries

**Correct Answers:** A, C, D, E

**Answer Explanation:**
- **A ✓** — Item 1 contains a specific patient's profile, preferences, and last consultation date — this is Episodic Memory (memory of a specific person and their history), not general world knowledge.
- **C ✓** — Item 2 is factual pharmacological knowledge about a drug — not tied to any specific event or person. This is Semantic Memory (facts and domain knowledge about the world).
- **D ✓** — Item 3 defines a step-by-step protocol the agent must follow when a condition is met. This is Procedural Memory — stored how-tos and workflows.
- **E ✓** — Item 4 records *what happened* in a specific past session on a specific date for a specific patient. This is Episodic Memory — a diary entry of a past event.
- **B ✗** — Item 1 is not Semantic Memory. Semantic Memory stores general world knowledge (e.g., "Type 2 diabetes is a metabolic condition"). Patient-specific profile data and consultation dates are Episodic.
- **F ✗** — Item 4 is not Procedural Memory. Procedural Memory stores action workflows (like Item 3). Item 4 is a record of something that already happened — that is Episodic.

---

## Q10 — Multiple Select (Multiple Correct) | Hard

A team is designing an AI-powered personal tutor for a university platform serving **50,000 students**. Each student has sessions of 40–60 messages, and the tutor must remember each student's learning goals and struggles from previous weeks to provide continuity.

The engineering team has the following proposals on the table. Which of the following design decisions are well-reasoned for this system? *(Select all that apply)*

- A) Use Buffer Memory for all sessions to ensure no context is ever lost within a session
- B) Use Window Memory with a carefully tuned window size to keep per-session token costs predictable and bounded
- C) Store each student's learning goals and known struggles in a vector database for retrieval in future sessions
- D) Use a single shared JSON file on the server to store all 50,000 student profiles
- E) Use LLM-driven extraction at the end of each session to identify and persist key information about the student to long-term memory
- F) Use Summary Memory for within-session management when sessions run longer than 40 messages

**Correct Answers:** B, C, E, F

**Answer Explanation:**
- **B ✓** — Window Memory bounds per-session token usage to a fixed, predictable size. This is essential at scale — 50,000 users × 50-message sessions would make Buffer Memory astronomically expensive.
- **C ✓** — A vector database provides durable, semantically-searchable long-term storage for student profiles — the right tool for episodic/semantic memory in production.
- **E ✓** — LLM-driven extraction at session end intelligently identifies what is worth preserving (goals, struggles, progress), ensuring meaningful data is saved to long-term memory without manual rules.
- **F ✓** — Summary Memory compresses older turns within a long session, keeping the context manageable while retaining key facts — well-suited for 40–60 message sessions.
- **A ✗** — Buffer Memory in 40–60 message sessions at 50,000 users would cause rapidly escalating token costs and risk hitting context window limits. It is not scalable here.
- **D ✗** — A single shared JSON file for 50,000 users is not a scalable architecture. It creates read/write bottlenecks, is not searchable by meaning, and is unsuitable for production-grade retrieval.
