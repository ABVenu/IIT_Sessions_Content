# Objective Assignment: LLM Internals for Designers

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

Ananya's startup ships a **GreenCart** support bot on Groq. Finance asks why the monthly API bill jumped after they started sending longer prompts with more retrieved FAQ chunks.

What does the provider primarily bill for?

A. **Input tokens** and **output tokens** processed per API call  
B. The number of English **words** visible in the chat UI only  
C. The number of PDF **pages** uploaded to cloud storage  
D. A flat fee per calendar day regardless of prompt size

**Correct Answer:** A

**Answer Explanation:**  
A is correct — cloud LLM APIs charge by tokens sent (input) and generated (output), not by words or page count.

B is incorrect because billing uses tokenisation, which often differs from word count. C is incorrect because storage billing is separate from per-call token metering. D is incorrect because usage-based APIs scale with token volume.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A designer runs the same RAG prompt through `tiktoken` and sees **36 words** but **64 tokens**.

What is the **best** explanation?

A. **Tokenisation** splits text into subword pieces — tokens are not always one-to-one with words  
B. `tiktoken` always doubles the word count for Groq models  
C. Tokens count only punctuation, not letters  
D. Word count and token count must always match in English

**Correct Answer:** A

**Answer Explanation:**  
A is correct — URLs, punctuation, delimiters, and subword splits can raise token count above word count.

B is incorrect because there is no fixed doubling rule. C is incorrect because tokens include letters and subwords, not punctuation alone. D is incorrect because the lab deliberately shows divergence.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A product spec says the model has an **8,000-token context window**.

What does that limit refer to?

A. The **maximum tokens** the model can process in **one forward pass** — including system text, RAG chunks, chat history, tool results, and the reply slot  
B. The maximum number of characters in the user's latest message only  
C. The total size of `chat_history.json` saved on disk  
D. The maximum number of ReAct tool calls allowed per day

**Correct Answer:** A

**Answer Explanation:**  
A is correct — input and output share one window budget per request.

B is incorrect because the whole prompt stack counts, not just the last user line. C is incorrect because disk persistence can exceed what is sent each call. D is incorrect because iteration limits (`max_iterations`) are a separate control.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

**GreenCart** saves **every** chat turn to `chat_history.json`, but the backend sends only the **last 4 messages** to the model when the window is tight.

Which statement is **most accurate**?

A. The full history may exist on disk, but the model only **"sees"** what your code attaches to **this** API request  
B. Saving to JSON automatically loads all 200 turns into every API call  
C. Truncation permanently deletes older messages from the JSON file  
D. Context limits apply only to **output** tokens, never to input

**Correct Answer:** A

**Answer Explanation:**  
A is correct — short-term memory is what you pack into the request; disk storage is separate.

B is incorrect because developers choose how much history to reload. C is incorrect because windowing drops messages from the **prompt**, not necessarily from disk. D is incorrect because input and output share the same window.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

**GreenCart** launches a **refund-policy Q&A** feature grounded on legal FAQ chunks. Customers must get **consistent, policy-aligned** answers every time.

Which **`temperature`** setting is the **safest default**?

A. **`0`** — minimise random token choices for stable, factual replies  
B. **`1.2`** — maximise creative paraphrase  
C. **`0.9`** — encourage varied refund interpretations  
D. **Above `1.0`** — brainstorm alternate policies per user

**Correct Answer:** A

**Answer Explanation:**  
A is correct — low temperature keeps compliance-style answers stable; high temperature risks conflicting refund wording.

B, C, and D increase variance and are inappropriate for policy bots where inconsistent answers can cause legal and UX harm.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A RAG assembler uses `MAX_CONTEXT_TOKENS = 600` for the retrieval block only. The vector DB returns **six** chunks, but `build_context_block` includes only **four** before stopping.

What **most likely** happened?

A. Adding the **fifth** chunk would push the retrieval section **over the 600-token budget**, so remaining chunks were **dropped**  
B. The vector database can never return more than four rows  
C. **`temperature=0`** automatically limits retrieval to four chunks  
D. The system prompt was removed to make room

**Correct Answer:** A

**Answer Explanation:**  
A is correct — the loop stops when the next piece would exceed the designer-set cap, mimicking tight-window RAG design.

B is incorrect because retrieval can return more hits than fit in the budget. C is incorrect because temperature affects sampling, not chunk packing. D is incorrect because omitting the system prompt is discouraged, not the default packing behaviour.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A single **GreenCart** agent request packs **RAG**, **chat history**, and a **tool observation** into one Groq call.

Which items **compete for the same context window** in that request?

A. **System instructions** and grounding rules  
B. **Retrieved FAQ chunks** injected into the prompt  
C. **Chat turns** your code includes this round  
D. The **`GROQ_API_KEY`** string stored in your `.env` file  
E. **Tool observation** text passed back into the model

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are all prompt payload that consumes input tokens in one forward pass.

D is incorrect because environment secrets are not sent as prompt text unless you mistakenly paste them into the message.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A product has three surfaces: **refund-policy RAG**, an **`lookup_order` tool planner**, and a **festive SMS banner generator**.

Which configuration choices align with **sound design**?

A. **Refund policy Q&A:** `temperature=0`  
B. **Festive SMS generator:** higher temperature (for example `0.7`–`0.9`) for creative copy  
C. **`lookup_order` tool planning:** low/moderate temperature (for example `~0.3`) for reliable tool routing  
D. **Refund policy Q&A:** `temperature=0.9` so every customer gets a unique refund rule  
E. Use a fixed **`seed`** in automated tests when the API supports it for reproducible QA runs

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the consistency-vs-creativity trade-off for policy, tools, and creative surfaces.

D is incorrect because high temperature on refund policy can produce conflicting legal answers turn to turn.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

After **20 turns**, **GreenCart** users report: *"The bot stopped following 'answer only from the policy document.'"* The app windowed history to the last **N** messages.

Which diagnoses and responses are **valid**?

A. **Silent truncation** may have **dropped** the earliest user message that stated the grounding rule  
B. **Windowed history** sends only the tail — constraints from turn 1 may no longer reach the model  
C. Setting **`temperature=1.2`** automatically erases older rows from `chat_history.json` on disk  
D. **Re-inject grounding rules** in the system prompt or use **summary memory** for long sessions  
E. Each **multi-turn agent lap** adds tokens (scratchpad + observations), accelerating pressure on the window

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A, B, D, and E describe truncation, windowing, fixes, and token growth in agent loops.

C is incorrect — temperature affects sampling randomness, not disk deletion of chat logs.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A designer reviews a **RAG + memory + agent** feature approaching the context ceiling before launch.

Which actions follow the **designer playbook** taught for production?

A. **Trim chat history or RAG chunks** before **omitting the system prompt** that holds grounding rules  
B. **Never omit the system prompt** when cutting tokens on customer-facing flows  
C. **Summarise tool observations** when a single observation exceeds roughly **500 tokens** before re-prompting  
D. Paste a **full 40-page PDF** into one prompt to avoid building a retrieval pipeline  
E. Reserve roughly **10–15%** of the window below the hard max as a **safety margin** for longer answers

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are trimming priorities, observation caps, and safety-margin habits from the playbook.

D is incorrect — pasting full PDFs wastes tokens, raises cost/latency, and can overflow the window instead of using chunking + retrieval.
