# Objective Assignment — Evaluating and Improving RAG Systems

**Total Questions:** 10 | **Format:** MCQ (Single Correct) + MSQ (Multiple Correct)

---

## MCQ — Single Correct Answer

---

### Question 1 *(Easy)*

Neha's team is debugging a RAG-powered customer support system that keeps giving wrong answers. Her tech lead says: *"Stop tuning the LLM — fix the librarian first."*

Which component of the RAG system is the tech lead referring to?

**A)** The Generator (LLM)
**B)** The Retriever
**C)** The Embedding Model
**D)** The Vector Database

**Correct Answer:** B

**Answer Explanation:**
The tech lead is referring to the **Retriever** — the component responsible for fetching relevant documents from the knowledge base. In the RAG analogy, the Retriever is the "librarian" who goes and fetches the right books (documents), while the Generator (LLM) is the "reader" who reads those books and writes the answer. If the librarian brings the wrong book, the reader's answer will be wrong — and it is not the reader's fault. This is why, when a RAG system underperforms, the Retriever should always be improved first before blaming the LLM.

- **A is wrong:** The Generator (LLM) is the "reader/author" in this analogy — it generates answers based on what it is given.
- **C is wrong:** The Embedding Model converts text to vectors; it is not the "librarian."
- **D is wrong:** The Vector Database stores the embeddings; it is the "library shelf," not the librarian.

---

### Question 2 *(Easy)*

Arjun's e-commerce chatbot tells a customer: *"You can return your product within 7 days."* However, the company updated its return policy 3 months ago — returns are now allowed within **30 days**. The RAG pipeline is fully functional and the LLM received context. What is the most likely root cause?

**A)** The LLM hallucinated the 30-day policy
**B)** The prompt template is overly restrictive
**C)** The system retrieved an outdated version of the return policy document
**D)** Metadata filtering excluded the return policy from the search

**Correct Answer:** C

**Answer Explanation:**
The most likely root cause is that the system retrieved an **outdated version of the policy document** still present in the knowledge base. This is the "Freshness" failure case — if the knowledge base is not updated and an old document is still being retrieved, the answer will be wrong even if the retrieval and generation logic is perfect. The session explicitly covers this: *"If the return policy was 7 days last year but updated to 30 days this year, your system should use the new rule."*

- **A is wrong:** The LLM did not hallucinate — it faithfully used the old retrieved document. Hallucination means generating information not in any document; here the retrieved document itself had the wrong date.
- **B is wrong:** A restrictive prompt would cause the LLM to say "I don't know" — not give a wrong date.
- **D is wrong:** If metadata filtering excluded the policy, no return-related answer would be generated at all.

---

### Question 3 *(Easy)*

A RAG-powered legal assistant responds to a contract query: *"As per the Employment Contract Policy (Section 4), the notice period for resignation is 30 days."* This response is an example of which essential property of a good RAG system?

**A)** Freshness
**B)** Completeness
**C)** Grounding
**D)** Safety and Privacy

**Correct Answer:** C

**Answer Explanation:**
This is an example of **Grounding** — every claim in the response is directly traceable to a specific document and section. The session defines a grounded response as one that is *"directly supported by the retrieved documents and contains no claims that come from outside the knowledge base."* The lawyer analogy from the session applies perfectly here: *"A good lawyer says 'As per Section 302 of the agreement...' — the first is grounded; saying 'I think this is how it works' is not."*

- **A is wrong:** Freshness refers to using the latest version of documents, not to citing sources.
- **B is wrong:** Completeness means covering all relevant aspects of the query — not specifically about citing the source.
- **D is wrong:** Safety and Privacy relate to not disclosing confidential internal information — not about citing sources.

---

### Question 4 *(Easy)*

When scoring retrieval quality on the **0–2 scale**, a query about a refund policy results in the RAG system retrieving the shipping policy document instead. What score does this retrieval receive and why?

**A)** Score 2 — the system retrieved a document, which is a success
**B)** Score 1 — partially relevant because both relate to orders
**C)** Score 0 — completely irrelevant; the wrong document was retrieved
**D)** Score 1 — the LLM can still generate an answer from the shipping policy

**Correct Answer:** C

**Answer Explanation:**
A retrieval that fetches the **wrong document entirely** scores **0** on the 0–2 Retrieval Quality Scale. Score 0 means "completely irrelevant — wrong document retrieved altogether." The session provides exactly this example: *"User asks about refund; system fetches the shipping policy → Score 0."* Just because a document was retrieved does not make it relevant — relevance is measured against what the query actually needed.

- **A is wrong:** Simply retrieving a document is not success if it is the wrong one. Relevance is the measure, not retrieval alone.
- **B and D are wrong:** Shipping policy and refund policy are distinct categories. The fact that both relate to orders does not make shipping policy relevant to a refund query.

---

### Question 5 *(Moderate)*

Rohan's RAG system processes a query about cancellation policy. It retrieves **4 documents** (top-K = 4): 3 are genuinely about cancellation, and 1 is about shipping. His knowledge base contains **6 documents** total that are relevant to cancellation.

What are the Precision and Recall for this query?

**A)** Precision = 50%, Recall = 75%
**B)** Precision = 75%, Recall = 50%
**C)** Precision = 60%, Recall = 80%
**D)** Precision = 80%, Recall = 60%

**Correct Answer:** B

**Answer Explanation:**
Using the session's formulas:

- **Precision** = Relevant Retrieved / Total Retrieved = **3 / 4 = 0.75 = 75%**
- **Recall** = Relevant Retrieved / Total Relevant in Knowledge Base = **3 / 6 = 0.5 = 50%**

Precision tells us that 75% of what was retrieved was actually useful (1 out of 4 was noise). Recall tells us that the system found only 50% of all cancellation-related documents in the knowledge base — it missed 3 relevant documents. To improve recall, Rohan should consider increasing the top-K value. However, doing so might lower precision by bringing in more irrelevant documents — this is the classic precision-recall trade-off.

- **A, C, D are wrong** due to arithmetic errors in applying the formulas.

---

### Question 6 *(Moderate)*

A customer asks: *"How long does express shipping take?"* The retrieved document states only: *"Express shipping is delivered within 1–2 business days."* The system responds: *"Express shipping is delivered within 1–2 business days. Also, express shipping includes a complimentary priority tracking upgrade on all orders this month."*

Using the **0–3 Response Accuracy Scale**, what is the most appropriate score for this response?

**A)** Score 3 — the core answer (1–2 days) is accurate and grounded
**B)** Score 0 — the entire response is completely wrong
**C)** Score 1 — partially correct; the timeline is right, but the "priority tracking upgrade" claim is a hallucination not present in the retrieved document
**D)** Score 2 — mostly correct; the extra detail is a minor unverified claim

**Correct Answer:** C

**Answer Explanation:**
The session's 0–3 Response Accuracy Scale defines:
- **Score 1:** Partially correct — some right information, but mixed with wrong or missing details.
- **Score 2:** Mostly correct — right answer with minor gaps or a **small** unverified claim.

The "complimentary priority tracking upgrade" is a **specific, fabricated promotional claim** absent from the retrieved document — this is hallucination. The session warns: *"The more specific a claim (exact timelines, conditions, offers), the higher the risk of hallucination."* Adding a concrete perk like a tracking upgrade is not a "minor gap" — it is a significant hallucinated claim that could mislead customers. This pulls the score down to **Score 1**, not Score 2.

- **A is wrong:** Score 3 requires the response to be accurate, complete, AND fully grounded. The hallucinated promotion disqualifies this.
- **B is wrong:** Score 0 means the response is completely wrong; the shipping timeline itself is correct.

---

## MSQ — Multiple Correct Answers (Select ALL that apply)

---

### Question 7 *(Moderate)*

Aisha's startup is auditing the quality of their customer support RAG system before launch. Their product brief says the system must score well on all core properties. Which of the following are listed as **essential properties of a good production RAG system** in the session?

**A)** Accuracy
**B)** Freshness
**C)** Grounding
**D)** Response Speed
**E)** Completeness

**Correct Answers:** A, B, C, E

**Answer Explanation:**
The session defines **five essential properties** every production RAG system must have:
1. **Accuracy** — the answer is factually correct and consistent with source documents.
2. **Grounding** — every claim is traceable to a specific retrieved document.
3. **Completeness** — the answer covers all relevant aspects of the query without leaving out important details.
4. **Safety and Privacy** — the system does not expose confidential internal documents to customers.
5. **Freshness** — the system uses the latest version of policy documents, not outdated ones.

**D (Response Speed)** is **not listed** as one of the five core properties in the session. While speed matters for user experience, the session specifically focuses on these five qualitative accuracy dimensions.

---

### Question 8 *(Moderate)*

The RAG system at a fintech startup is returning many irrelevant documents alongside relevant ones — causing the LLM to generate noisy, confusing answers. The team wants to improve **retrieval precision**. Which of the following actions would directly improve precision?

**A)** Decrease the top-K value (e.g., from 8 to 4)
**B)** Apply metadata filtering to restrict similarity search to only the relevant document category
**C)** Increase the top-K value (e.g., from 3 to 10)
**D)** Increase the number of test queries in the evaluation dataset
**E)** Run the RAG pipeline on the same queries 100 times for consistency testing

**Correct Answers:** A, B

**Answer Explanation:**
The session explicitly states two techniques for improving **precision**:

1. **Reduce the top-K value** — Retrieving fewer, more targeted documents means less noise. If K=8 brings in 4 irrelevant docs, reducing to K=4 may bring in 0 or 1 irrelevant docs. Precision = Relevant Retrieved / Total Retrieved — fewer irrelevant docs in the denominator improves this ratio.

2. **Apply metadata filtering** — By restricting the similarity search to only documents in the relevant category *before* running it, every result belongs to the right category. Even with K=5, all 5 will be from the correct category.

- **C is wrong:** Increasing K improves Recall (finds more relevant docs) but hurts Precision (brings in more irrelevant docs too).
- **D and E are wrong:** These are evaluation/testing practices — they help measure precision but do not directly improve it.

---

### Question 9 *(Hard)*

A RAG-powered HR chatbot at a manufacturing company retrieves 3 documents for the query: *"Can the company terminate an employee without notice?"* The retrieved documents are: [Employment Contract Terms], [Disciplinary Procedures], [Payroll Policy].

The final response states: *"Yes, the company can terminate without notice for gross misconduct. Additionally, employees terminated without notice are entitled to a ₹50,000 ex-gratia payment as per company policy."*

The **Employment Contract Terms** document only states: *"Termination without notice is permitted only in cases of gross misconduct."* The ₹50,000 ex-gratia claim does not appear in any retrieved document.

Which of the following statements are **TRUE**? (Select ALL that apply.)

**A)** The first part of the response (termination without notice for gross misconduct) is grounded in the retrieved document.
**B)** The ₹50,000 ex-gratia payment claim is a hallucination.
**C)** This response scores a 3 on the 0–3 Response Accuracy Scale.
**D)** The Payroll Policy document likely scores a 0 or 1 on the 0–2 Retrieval Quality Scale for this query.
**E)** This response should score a 1 on the 0–3 Response Accuracy Scale.

**Correct Answers:** A, B, D, E

**Answer Explanation:**

- **A is TRUE:** The first claim directly matches the retrieved Employment Contract Terms document — *"Termination without notice is permitted only in cases of gross misconduct."* This part is grounded.

- **B is TRUE:** The ₹50,000 ex-gratia claim does not appear in any retrieved document. This is hallucination — the LLM added a specific monetary figure from its own training knowledge, not from any provided context. The session warns: *"Always be suspicious of very specific numbers that you did not expect."*

- **C is FALSE:** Score 3 requires the response to be *"accurate, complete, and grounded in the retrieved document."* The hallucinated ex-gratia payment disqualifies this from Score 3.

- **D is TRUE:** Payroll Policy is about compensation structures and salaries — not about termination procedures. For a query about "termination without notice," retrieving Payroll Policy is either completely irrelevant (Score 0) or marginally tangential (Score 1 at best).

- **E is TRUE:** Score 1 = *"Partially correct — some right information, but mixed with wrong or missing details."* The correct termination clause + the hallucinated monetary claim together make this a Score 1 response.

---

### Question 10 *(Hard)*

A product team at a travel booking startup notices that their RAG chatbot consistently receives 1-star ratings for queries about flight cancellation refund policies. They want to follow the session's evaluation and improvement framework to diagnose and fix the issue. Which of the following steps are part of the **correct approach**? (Select ALL that apply.)

**A)** Immediately replace the LLM with a newer, more capable model
**B)** Verify whether the correct flight cancellation refund document (not the generic cancellation policy) was retrieved for these queries
**C)** Check whether the retrieved chunk contains the specific details needed (e.g., refund percentages, time windows, airline-specific rules)
**D)** Strengthen the prompt template so the LLM is restricted to using only the retrieved context and must say "I don't have that information" if the context is insufficient
**E)** Add or update missing or outdated flight cancellation refund documents in the knowledge base
**F)** Tune the top-K value and check whether precision or recall improves for this specific query category

**Correct Answers:** B, C, D, E, F

**Answer Explanation:**
The session's evaluation framework follows a 4-step diagnostic order: Right Document → Right Chunk → Correct Response → Grounded Response. Each step in the correct options maps to this framework:

- **B is correct:** Step 1 — "Did the system fetch the correct policy document?" If the system retrieves a general cancellation policy instead of the refund-specific one, all subsequent steps fail. This is analogous to the COD refund example where not distinguishing COD from online payments leads to wrong answers.

- **C is correct:** Step 2 — "From that document, did the system pick the right section/chunk?" Even the right document, if the wrong chunk is retrieved, will miss critical details (e.g., refund percentages or airline-specific conditions).

- **D is correct:** Improving the prompt template prevents hallucination and ensures the LLM uses only the retrieved context. A strong prompt also instructs the LLM to say "I don't know" rather than guessing — which is far less damaging than a confident wrong answer.

- **E is correct:** If the knowledge base has stale or missing documents, even perfect retrieval will return wrong information. Keeping the knowledge base current is a core part of the continuous improvement loop.

- **F is correct:** Tuning top-K is a direct way to improve retrieval precision or recall for specific query categories where the system is underperforming.

- **A is wrong:** The session explicitly states: *"When your RAG system is underperforming, always focus on improving your Retriever first. Do not blame the LLM for generating bad answers when the retrieved context itself is weak."* Replacing the LLM is the last resort, not the first.
