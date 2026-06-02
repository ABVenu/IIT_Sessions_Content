# Assignment Objective: Introduction to RAG

## Q1 (MCQ - Easy)
A support chatbot answers, "Most stores allow 30-day returns," without checking company policy. Which core risk is this?

- A. Better retrieval precision
- B. Hallucination
- C. Index normalization
- D. Chunk overlap

**Correct Answer:** B  
**Explanation:** This is hallucination: fluent but unsupported information not grounded in trusted policy evidence.

---

## Q2 (MCQ - Easy)
Which statement best defines **grounding** in a policy chatbot?

- A. Let the LLM answer from pretraining knowledge only
- B. Add style instructions so answers look polite
- C. Support answers using retrieved, verifiable policy text
- D. Increase model temperature for creative responses

**Correct Answer:** C  
**Explanation:** Grounding ties the response to external evidence (policy chunks), improving factual reliability.

---

## Q3 (MCQ - Easy)
In a RAG flow, what should happen immediately **before** generation?

- A. Delete low-frequency vocabulary
- B. Build prompt context with retrieved chunks
- C. Re-train the LLM
- D. Increase top-k until 100

**Correct Answer:** B  
**Explanation:** The retrieved evidence is inserted into prompt context, and then the LLM generates the final reply.

---

## Q4 (MCQ - Easy)
A student says: "If the bot sounds confident, it is probably correct." What is the best correction?

- A. Confidence is the same as correctness
- B. Correctness must be verified against policy evidence
- C. Confidence improves if top-k is always 1
- D. Correctness depends only on empathy lines

**Correct Answer:** B  
**Explanation:** Tone and confidence are not proof. Correctness must be validated using trusted policy documents.

---

## Q5 (MCQ - Moderate)
An e-commerce assistant returns answer text that cites "next-day standard delivery," but the policy says standard delivery is 3-5 business days. Which component likely failed first?

- A. Prompt token counting
- B. Retrieval or evidence selection quality
- C. Markdown rendering
- D. API key rotation

**Correct Answer:** B  
**Explanation:** If irrelevant or wrong chunks were retrieved, generation can still sound polished but produce incorrect policy statements.

---

## Q6 (MCQ - Moderate)
Which statement is most accurate about vector search in RAG?

- A. Vector search replaces generation completely
- B. Vector search is optional and unrelated to retrieval
- C. Vector search is commonly the retriever mechanism for top-k relevant chunks
- D. Vector search only works for exact keyword matches

**Correct Answer:** C  
**Explanation:** In RAG, vector search is a common way to implement retrieval by semantic similarity.

---

## Q7 (MSQ - Moderate)
You are auditing a policy bot answer. Which checks directly improve trustworthiness? (Select all that apply)

- A. Verify each factual claim against retrieved policy lines
- B. Prefer answers with more adjectives and empathy
- C. Check whether conditions (e.g., opened/unopened) are preserved
- D. Confirm that numeric values match official documents

**Correct Answers:** A, C, D  
**Explanation:** Trustworthiness depends on factual alignment and condition correctness, not stylistic polish.

---

## Q8 (MSQ - Moderate)
Which are valid goals of grounding in document-backed assistants? (Select all that apply)

- A. Make answers organization-specific
- B. Make answers current with latest policy updates
- C. Remove the need for any retrieval system
- D. Make answers verifiable by source text

**Correct Answers:** A, B, D  
**Explanation:** Grounding targets specificity, freshness, and verifiability; retrieval remains essential.

---

## Q9 (MSQ - Hard)
You are designing a RAG system for policy support. Which failure modes can still happen even when RAG is used? (Select all that apply)

- A. Wrong chunk retrieved for the question
- B. No relevant chunk found in top-k
- C. LLM ignores provided evidence and adds unsupported details
- D. Hallucination becomes impossible by design

**Correct Answers:** A, B, C  
**Explanation:** RAG reduces hallucination risk but does not eliminate it; both retrieval and generation can fail.

---

## Q10 (MSQ - Hard)
Which actions belong to an ingestion/index-refresh lifecycle that keeps RAG answers reliable over time? (Select all that apply)

- A. Collect source policy documents from trusted channels
- B. Clean/normalize text before chunking and embedding
- C. Schedule periodic refresh runs for changed policies
- D. Freeze index forever to preserve reproducibility in production

**Correct Answers:** A, B, C  
**Explanation:** Reliable retrieval requires continuous ingestion hygiene and refresh. Freezing forever causes stale answers.
