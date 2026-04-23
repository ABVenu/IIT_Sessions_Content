# Assignment — Objective (Session 28: Introduction to RAG)

**Instructions for learners:** This assignment tests your conceptual understanding of how plain LLMs work, their limitations, what RAG is, and why retrieval quality decides the final answer quality. Read each scenario carefully before choosing your answer.

- Total Questions: 10 (6 MCQs + 4 MSQs)
- Submission: Via the Assess platform
- Ordering: Easy → Moderate → Hard

---

## Section A — Multiple Choice (Single Correct)

### Q1. (Easy — MCQ)

Simran is demoing ChatGPT to her manager. She asks, *"What is Java?"* and gets a near-perfect answer. Excited, she then asks, *"What is the leave encashment policy at my company, Infynitec, that was updated last week?"* The model confidently gives a wrong answer.

What is the most accurate reason the second answer failed?

- A. LLMs stop working for questions longer than 10 words.
- B. A plain LLM was not trained on Infynitec's internal documents, and by default it cannot read live company files.
- C. LLMs always invent numbers, regardless of the question.
- D. LLMs only understand English; Simran should have asked in Hindi.

**Answer:** B

**Explanation:**

- **B is correct.** This hits two core limitations from the session: (i) **lack of domain-specific context** — the LLM never saw Infynitec's HR policy in training, and (ii) **no built-in access to external/real-time data** — it cannot open the company's HR portal on its own. Without RAG, the model answers from generic memory and produces a confident but wrong response.
- **A is wrong.** LLMs handle long queries routinely; query length is not the cause.
- **C is wrong.** LLMs do not *always* invent numbers — they answer well on widely known public facts (like "What is Java?"). The failure mode here is specific to *private / recently changed* information.
- **D is wrong.** The question was already in English; language is not the issue.

---

### Q2. (Easy — MCQ)

A bank deploys a plain LLM chatbot with no retrieval system. A customer asks, *"What is today's fixed deposit interest rate at your bank?"* The chatbot confidently invents a rate like "6.75% p.a." — which turns out to be wrong.

This behaviour of the LLM generating fabricated information while sounding fluent and confident is called:

- A. Grounding
- B. Hallucination
- C. Retrieval
- D. Fine-tuning

**Answer:** B

**Explanation:**

- **B is correct.** As defined in the session, **hallucination** is when an LLM generates information that is incorrect, fabricated, or unsupported while presenting it as a confident factual answer. A "fake interest rate" is a textbook hallucination.
- **A is wrong.** Grounding is the *opposite* — anchoring the answer to real retrieved evidence.
- **C is wrong.** Retrieval is the step of *fetching* relevant chunks from a knowledge base, not generating fake content.
- **D is wrong.** Fine-tuning is a training technique to adapt a model to specific data; it is unrelated to the act of fabrication.

---

### Q3. (Easy — MCQ)

Rahul is building an "Ask HR" assistant for his 200-person startup. He wants the assistant to answer questions like *"How many casual leaves do I get?"* using the company's actual HR policy PDF — not from generic internet knowledge.

Which approach fits his requirement best?

- A. Use a plain LLM with no external data.
- B. Use only a keyword search on the PDF and return raw paragraphs to the user.
- C. Use a Retrieval-Augmented Generation (RAG) pipeline that first retrieves from the HR policy and then asks the LLM to answer using that content.
- D. Train a new LLM from scratch on his laptop.

**Answer:** C

**Explanation:**

- **C is correct.** The scenario is the exact fit for RAG: the answer *must* come from a specific trusted document (HR policy). RAG retrieves the right chunk first, then the LLM generates a grounded, natural-language answer.
- **A is wrong.** A plain LLM will answer from generic memory and may get *this* company's rules wrong (hallucination risk).
- **B is wrong.** Keyword search alone returns raw paragraphs and does not handle phrasing differences (e.g., "WFH" vs "remote work"). It also gives no natural-language answer.
- **D is wrong.** Training an LLM from scratch is astronomically expensive and completely unnecessary for this use case — and still would not solve the "policy updated last week" problem.

---

### Q4. (Easy — MCQ)

A team lead describes the required behaviour of a support chatbot: *"When a customer asks something, the bot should first look up the correct policy document, and only then compose the final answer."*

Which of the following best represents the four-step high-level flow of RAG that matches this description?

- A. Generate → Retrieve → Query → Context
- B. Context → Query → Generate → Retrieve
- C. Query → Retrieve → Context → Generate
- D. Retrieve → Generate → Query → Context

**Answer:** C

**Explanation:**

- **C is correct.** The session explicitly defines the RAG flow as **Query → Retrieve → Context → Generate**: the user asks, the system retrieves relevant chunks, those chunks are added to the prompt as context, and the LLM generates the final grounded answer.
- **A, B, D are wrong.** They all reorder steps in ways that break the logic — for example, you cannot "generate" before there is even a "query," and retrieval must always happen *before* context is passed to the LLM.

---

### Q5. (Moderate — MCQ)

A healthcare startup says: *"We fine-tuned a general LLM on our medical guidelines six months ago. Last week, the Ministry of Health updated the dosage guidelines. Our chatbot is now giving outdated dosages to doctors."*

Which option is the **most practical and safe** fix, given the session's discussion of why RAG is preferred over fine-tuning for changing data?

- A. Fine-tune the model from scratch every time the guidelines change.
- B. Just switch to a larger, more expensive LLM.
- C. Build a RAG pipeline that retrieves from the latest guideline documents at query time, and keep the knowledge base updated whenever the Ministry publishes new guidelines.
- D. Ask doctors to phrase their questions more carefully.

**Answer:** C

**Explanation:**

- **C is correct.** The session directly addresses this: *"Fine-tuning is expensive, slow to update, and does not give you traceability. RAG lets you simply update the knowledge base whenever policy changes — no retraining needed."* In a safety-critical domain like healthcare, this is exactly the required approach.
- **A is wrong.** Frequent full re-fine-tuning is expensive, slow, and does not solve hallucination or traceability. Guidelines may change weekly — re-fine-tuning weekly is impractical.
- **B is wrong.** A bigger LLM still has a **static knowledge cutoff**. It does not magically know about guidelines released *after* its training.
- **D is wrong.** Prompting tricks can help a little, but the session explicitly says the *only real fix* is giving the model real retrieved information — not rephrasing the user's query.

---

### Q6. (Moderate — MCQ)

An e-commerce team's RAG chatbot uses **keyword search** for retrieval. A customer asks: *"What is the work from home policy?"* The policy document actually says: *"Remote working is allowed two days per week."* The chatbot replies, "No information found."

What is the correct diagnosis, and what should the team change?

- A. The LLM is too small — upgrade to a larger LLM.
- B. Keyword search can only match exact words, not meaning. Replace it with **vector search using embeddings**, so semantically similar phrases like "work from home" and "remote working" can be matched.
- C. The document is too short — add more text to it.
- D. The user's wording is wrong — force customers to use the exact phrase "remote working."

**Answer:** B

**Explanation:**

- **B is correct.** This is the exact scenario from the session used to motivate vector search: *"If the document says 'remote working is allowed two days per week' but the user asks 'what is our work from home policy?', keyword search may find nothing."* Embeddings capture *meaning*, so the two phrases end up close in vector space and retrieval succeeds.
- **A is wrong.** The LLM never got the chance to answer because retrieval failed first — a bigger LLM does not fix retrieval.
- **C is wrong.** The document already contains the correct information; the issue is purely that keyword search cannot match it.
- **D is wrong.** Forcing users to learn internal document wording defeats the whole purpose of a natural-language assistant.

---

## Section B — Multiple Select Questions (Multiple Correct)

### Q7. (Moderate — MSQ)

Which of the following are **genuine limitations of a plain LLM** that RAG is specifically designed to solve? *(Select all that apply.)*

- A. Static, fixed knowledge (the training cutoff).
- B. Inability to translate between English and Hindi.
- C. No access to private / domain-specific documents like HR policies or internal wikis.
- D. No default access to real-time external data (live APIs, today's stock prices, today's score).
- E. Inability to produce grammatically correct sentences.

**Answer:** A, C, D

**Explanation:**

- **A is correct.** The session names **static knowledge** as Limitation 1: training data is frozen at the cutoff date.
- **C is correct.** **Lack of domain-specific context** is Limitation 2: the model has never seen your private docs.
- **D is correct.** **No built-in access to external or real-time data** is Limitation 3: the model cannot call APIs or open the internet on its own.
- **B is wrong.** Modern LLMs are actually *very strong* at translation; the session even lists translation-style tasks (summarization, paraphrasing, explanation) as their strengths. RAG is not designed to fix translation.
- **E is wrong.** LLMs are explicitly called out in the session as strong at **language generation** — grammar is not a problem they struggle with, and certainly not what RAG is designed to fix.

---

### Q8. (Moderate — MSQ)

An internal IT helpdesk **agent** answers the query *"How do I request VPN access?"* by first retrieving the latest IT SOP from the internal wiki, then reasoning over it, and then replying.

Which of the following are **genuine benefits** the agent gets *because* it used RAG before acting? *(Select all that apply.)*

- A. The agent can justify its response by pointing to a specific source document.
- B. The agent's reasoning is based on the most recent IT policy, not a stale training memory.
- C. The agent completely replaces the company's HR and IT departments.
- D. The agent reduces the risk of confidently sending the user to the wrong team or wrong form.
- E. Using RAG automatically turns a small LLM into a much larger LLM.

**Answer:** A, B, D

**Explanation:**

- **A is correct.** Traceability / citation is explicitly listed as a RAG benefit — the agent can point to the SOP chunk it used.
- **B is correct.** The session says agents get to *"work with updated information even after the LLM's training cutoff."*
- **D is correct.** The session gives this exact IT helpdesk example: *"Without retrieval, it might share an outdated process and send the user to the wrong team."* RAG reduces this risk.
- **C is wrong.** RAG improves answers, but it does not replace entire departments — this is an over-claim not supported by the session.
- **E is wrong.** RAG does not change the size or weights of the LLM. It changes what *information* is passed to the LLM at prompt time.

---

### Q9. (Hard — MSQ)

A legal-tech company notices that even after adding a RAG pipeline over their contracts database, their chatbot occasionally gives wrong or incomplete answers about specific contract clauses. The LLM itself has been verified as high-quality.

Based on the session's discussion of retrieval quality, which of the following are **realistic retrieval-side causes** of the wrong answers? *(Select all that apply.)*

- A. Chunks are either too large (noisy, lots of irrelevant text) or too small (missing important context).
- B. Embeddings are generated by a weak embedding model, so semantically relevant clauses are not ranked near the top.
- C. The vector database was never updated after the latest contract revisions — it still contains old clauses.
- D. Top-k is set so low (e.g., k = 1) that the most relevant clause sometimes falls just outside the retrieved results.
- E. Lawyers are typing their queries in English instead of Latin, which breaks vector search.

**Answer:** A, B, C, D

**Explanation:**

The session explicitly lists the factors that affect retrieval quality: chunking, embeddings, similarity search, ranking/top-k, metadata filters, and whether the knowledge base is kept updated. Options A, B, C, and D map one-to-one onto these factors.

- **A is correct.** *"Too big = noisy, too small = missing context"* is a direct quote from the session's discussion of chunking.
- **B is correct.** Embedding model quality directly affects whether semantically similar chunks are ranked near the top.
- **C is correct.** A stale knowledge base is called out as a retrieval-quality risk: *"whether the knowledge base is kept updated."*
- **D is correct.** If top-k is too low, the correct clause can be cut off before reaching the LLM — this is why re-ranking and tuned top-k matter.
- **E is wrong.** Vector search works on embeddings of the input language; English is perfectly supported. Latin has nothing to do with retrieval correctness.

---

### Q10. (Hard — MSQ)

A fintech team is comparing two versions of their customer chatbot:

- **System X:** Plain LLM, no retrieval.
- **System Y:** RAG system over the latest product + compliance documents.

Both are asked: *"Can a customer pre-close a personal loan after 6 months, and what is the foreclosure charge?"*

Which of the following statements about the **expected differences** between System X and System Y are **correct**? *(Select all that apply.)*

- A. System X is more likely to hallucinate a plausible-sounding but wrong foreclosure charge.
- B. System Y can cite the exact policy section from which the foreclosure charge was taken.
- C. System Y is **completely immune** to wrong answers, even if retrieval fetches the wrong document.
- D. System Y can stay correct even when the foreclosure policy changes next month — as long as the knowledge base is updated.
- E. System X automatically pulls today's RBI circulars from the internet before answering.

**Answer:** A, B, D

**Explanation:**

- **A is correct.** Without retrieval, System X falls back to generic memory and is prone to hallucinating numbers — exactly the "fake policy numbers" example discussed in the session.
- **B is correct.** The session highlights **traceability** as a key RAG benefit: *"you can cite the source document/chunk."*
- **D is correct.** RAG supports live updates: *"RAG lets you simply update the knowledge base whenever policy changes — no retraining needed."*
- **C is wrong.** The session is explicit that *"hallucination risk is lower but **not zero** if retrieval is bad."* If the wrong document is retrieved, the LLM can still give a wrong answer. This is literally the "Retrieval Quality" section's main point.
- **E is wrong.** Plain LLMs do not have default internet access — *"the model cannot look things up on its own"* is stated directly in Limitation 3.

---

## Final Answer Key

| Q | Type | Difficulty | Correct Answer |
|---|------|------------|----------------|
| 1 | MCQ | Easy | B |
| 2 | MCQ | Easy | B |
| 3 | MCQ | Easy | C |
| 4 | MCQ | Easy | C |
| 5 | MCQ | Moderate | C |
| 6 | MCQ | Moderate | B |
| 7 | MSQ | Moderate | A, C, D |
| 8 | MSQ | Moderate | A, B, D |
| 9 | MSQ | Hard | A, B, C, D |
| 10 | MSQ | Hard | A, B, D |
