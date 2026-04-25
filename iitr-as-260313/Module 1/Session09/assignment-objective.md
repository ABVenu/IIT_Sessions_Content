# Assignment — Objective (Prompt Engineering, Business Use Cases & Framework Overview)

**Instructions:** Answer all questions. For multiple-select questions (MSQ), select **all** options that apply.

**Scope:** This quiz covers prompt engineering fundamentals: **system prompts**; **role prompting**; the **C-I-F-C formula** (Context, Instruction, Format, Constraints); **output format control**; **prompt variations** (zero-shot, one-shot, few-shot); **real-world use cases**; **agent behavior mapping**; and the three major frameworks — **LangChain**, **CrewAI**, and **AutoGen** — including when to use each.

---

## Section A — Multiple Choice, Single Correct (MCQ)

### Q1 (Easy)

A student types *"Summarise this paragraph"* into ChatGPT and gets a vague, unhelpful answer. She rewrites it as: *"You are a study mentor. Summarise this paragraph for a Class 10 student in exactly 3 bullet points, using simple language."* The second version works perfectly. What skill did she apply to improve her result?

- A) Retrieval-Augmented Generation (RAG)
- B) Multi-agent coordination
- C) Prompt Engineering
- D) Output tokenisation

**Answer Explanation (for Assess):**
**Correct answer: C.** **Prompt Engineering** is the practice of designing and refining instructions given to an LLM to get accurate, useful outputs. The student made her prompt clearer, more specific, and better structured — that is exactly what prompt engineering means.
**A** is wrong: RAG involves connecting an LLM to external documents; no documents are involved here. **B** is wrong: multi-agent coordination is about multiple AI agents working together. **D** is wrong: tokenisation is how text is split internally; it is not something a user applies.

---

### Q2 (Easy)

Before a company's banking chatbot goes live, its developers add a hidden block of instructions saying: *"You are FinBot, an HDFC Bank assistant. Always reply in formal English. Never share account numbers or OTPs. Only answer questions about savings accounts and personal loans."* What is this hidden block of instructions called?

- A) A few-shot prompt
- B) A system prompt
- C) A user prompt
- D) A role-variation prompt

**Answer Explanation (for Assess):**
**Correct answer: B.** A **system prompt** is a set of initial instructions given to the LLM — before any user interaction — that defines its identity, tone, boundaries, and knowledge scope. It is hidden from the end-user and governs the whole conversation.
**A** is wrong: a few-shot prompt includes 2–3 examples to guide style; it is not an identity-defining instruction set. **C** is wrong: a user prompt is what the customer types. **D** is a made-up term.

---

### Q3 (Easy)

Ravi is learning to write better prompts. His instructor tells him to always include four ingredients in every prompt: who he is and what the situation is, the exact task the AI must do, how the answer should look, and any limits like word count or things to avoid. What is the name of this four-part recipe?

- A) The STAR formula
- B) The RICE framework
- C) The C-I-F-C formula
- D) The 4P method

**Answer Explanation (for Assess):**
**Correct answer: C.** The **C-I-F-C formula** stands for **Context** (who you are / the situation), **Instruction** (what to do), **Format** (how the output should look), and **Constraints** (limits, things to avoid). It is the standard recipe taught for writing effective LLM prompts.
**A** (Situation, Task, Action, Result) is used in interview storytelling. **B** is a product prioritisation method. **D** is not a standard prompting framework.

---

### Q4 (Easy)

Priya asks ChatGPT: *"Explain compound interest."* She gets a textbook-style definition. She then tries: *"You are a friendly bank relationship manager. Explain compound interest to a 45-year-old shopkeeper using his shop savings as a real example."* The second answer is far more practical and relatable. Which specific prompting technique produced this improvement?

- A) Few-shot prompting
- B) Output format control
- C) Role prompting
- D) Prompt chaining

**Answer Explanation (for Assess):**
**Correct answer: C.** **Role prompting** is the technique of explicitly assigning a persona or profession to the LLM so its answer matches the expected expertise and style of that role. By saying *"you are a friendly bank relationship manager,"* Priya made the model draw on a specific communication style.
**A** is wrong: few-shot prompting gives examples, not roles. **B** is wrong: output format control specifies structure like bullets or tables. **D** (prompt chaining) is linking multiple LLM calls in sequence.

---

### Q5 (Moderate)

A fintech company wants an AI system where a **Researcher agent** first collects the latest RBI policy updates, a **Writer agent** then drafts a compliance report from that research, and finally an **Editor agent** polishes and finalises the document — all happening in sequence. Which framework is **best suited** for this multi-role pipeline?

- A) LangChain — because it connects a single agent to tools and data sources
- B) AutoGen — because it supports human-in-the-loop conversations
- C) CrewAI — because it orchestrates a team of agents with defined roles working together
- D) No existing framework supports sequential agent pipelines

**Answer Explanation (for Assess):**
**Correct answer: C.** **CrewAI** is built specifically for orchestrating multiple agents with separate, defined roles (Researcher, Writer, Editor) that hand off work to each other in a structured sequence — exactly this use case.
**A** is wrong for *this* question: LangChain is strong for tool use and RAG, and can support multi-step flows, but **CrewAI** is the option that best matches a **named-role crew** with a clear sequential handoff between specialists. **B** is wrong: AutoGen suits back-and-forth conversational or code-heavy multi-agent scenarios; human-in-the-loop is its strength, not this style of specialist pipeline. **D** is incorrect.

---

### Q6 (Moderate)

A developer asks ChatGPT to generate a formal customer complaint email. **Version 1** gives the task with no examples. **Version 2** first shows two sample complaint emails (one from a retail context, one from a telecom context), and then asks for a new one — the output closely matches the desired tone and structure. What prompting technique explains why Version 2 performs so much better?

- A) Role prompting
- B) Zero-shot prompting
- C) Few-shot prompting
- D) Output format control

**Answer Explanation (for Assess):**
**Correct answer: C.** **Few-shot prompting** means giving 2–3 examples *inside the prompt* before asking for the output. The model learns the expected style and structure from those examples, so the result is more accurate and on-brand.
**A** is wrong: role prompting assigns a persona, not examples. **B** is wrong: zero-shot means no examples in the prompt — that describes Version 1, not why Version 2 improved. **D** is wrong: format control specifies structure (tables, bullets), not style-via-examples.

---

## Section B — Multiple Select, Multiple Correct (MSQ)

*Select all correct options.*

### Q7 (Moderate — MSQ)

A data analyst is using an LLM to extract structured information from 500 customer feedback forms and wants the output to be **directly usable in other tools** without manual cleanup. Which of the following output formats should the analyst request?

- A) **JSON** — for feeding output directly into code or applications
- B) **Markdown Table** — for readable comparisons in documentation or reports
- C) **Free-form paragraph** — the most flexible format for downstream tool processing
- D) **CSV** — for loading directly into Excel or a database
- E) **Numbered steps** — ideal for process documentation

**Answer Explanation (for Assess):**
**Correct answers: A, B, D.** **JSON** is ideal when output feeds into software. **Markdown tables** are useful for documentation and human-readable reports. **CSV** loads cleanly into Excel or databases.
**C** is wrong: free-form paragraphs are for humans to read, not for machines to process downstream. **E** is wrong: numbered steps are for tutorials and process guides, not for extracting and storing structured data.

---

### Q8 (Moderate — MSQ)

A product manager is designing a system prompt for a healthcare chatbot called *"SehatMitra"* targeted at Indian users. Which of the following can a **system prompt effectively control**?

- A) The **identity** of the bot — e.g., "You are SehatMitra, a wellness assistant for Indian users"
- B) The **tone** — e.g., "Use simple Hindi-English mix, always sound warm and caring"
- C) The **boundaries** — e.g., "Never give medicine dosages; always ask the user to consult a doctor"
- D) The **context window size** of the underlying LLM model
- E) The **format** of replies — e.g., "Always respond in under 4 sentences"

**Answer Explanation (for Assess):**
**Correct answers: A, B, C, E.** A system prompt controls the bot's **identity**, **tone**, **safety boundaries**, and **output format** — all four are standard system prompt components demonstrated in the session.
**D** is wrong: context window size is a hard technical limit set by the model architecture and provider; it cannot be changed by a system prompt. A system prompt tells the model *how* to behave, not *how much* it can process.

---

### Q9 (Hard — MSQ)

A startup is building a "Career Advisor Agent" that takes a user's skill list, searches live job portals for demand data, and returns a table of 3 matching careers with average salaries and top companies. Which of the following statements about **designing this agent correctly** are true?

- A) The System Prompt should assign the agent's role and tone *before* any user query is processed
- B) The LLM's first action after reading the user query should always be to immediately call the job portal search tool
- C) The ability to call external tools (like a job portal API) is what separates an agent from a plain chatbot
- D) The output format instruction — e.g., "return results as a table with columns: Career, Avg Salary, Top Companies" — should be part of the prompt
- E) The correct agent loop is: User Prompt → LLM reasoning → Tool call → LLM again with tool output → Final answer

**Answer Explanation (for Assess):**
**Correct answers: A, C, D, E.**
**A** is correct: the system prompt sets the agent's personality and scope before any user message arrives.
**C** is correct: tool access (APIs, search, databases) is the defining feature that makes an LLM-based system an *agent* rather than a chatbot.
**D** is correct: output format control is part of the prompt and makes the final result directly usable.
**E** is correct: this is the standard agent flow — the LLM first reasons, then decides a tool is needed, calls it, gets results, and generates the final formatted answer.
**B** is wrong: the LLM does not jump straight to a tool. It first *reasons* about the query, decides *if* a tool is needed, and only then calls it. Skipping reasoning leads to poor, brittle agents.

---

### Q10 (Hard — MSQ)

A developer has three new projects:
- **Project X:** A chatbot for a law firm that must answer only from the firm's internal case documents and policy PDFs — not from general web knowledge.
- **Project Y:** A content factory where one agent researches a topic, a second agent writes an article, and a third agent edits it before publishing.
- **Project Z:** A code-debugging assistant where two AI agents debate the root cause of a bug, one rewrites the code, and the other executes and verifies it — with the developer able to jump in at any point.

Which of the following **framework-to-project mappings** are correct?

- A) **LangChain for Project X** — best for one smart agent grounded in private documents via RAG
- B) **CrewAI for Project Y** — best for a pipeline of role-based agents handing off work in sequence
- C) **AutoGen for Project Z** — best for conversational multi-agent collaboration with code execution and human-in-the-loop
- D) **AutoGen for Project X** — because it is the most mature framework with the largest community
- E) **LangChain for Project Z** — because it supports the most integrations

**Answer Explanation (for Assess):**
**Correct answers: A, B, C.**
**A** is correct: LangChain is the go-to for a single, powerful agent that needs to retrieve and reason over private documents (RAG use case).
**B** is correct: CrewAI is purpose-built for multi-role agent teams in a structured sequential workflow.
**C** is correct: AutoGen is designed for conversational agents that debate, write code, execute it, and keep a human in the loop — Project Z is its textbook use case.
**D** is wrong: AutoGen is conversational and code-focused; it is not the right fit for a document-grounded single-agent chatbot. LangChain has the largest community, not AutoGen.
**E** is wrong: while LangChain has broad integrations, it does not natively support multi-agent conversation-style debugging with code execution as a first-class feature the way AutoGen does.

---

*End of objective assignment.*
