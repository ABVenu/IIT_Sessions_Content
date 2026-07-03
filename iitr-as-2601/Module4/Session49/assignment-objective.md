# Objective Assignment: Retrieval & Grounding — Chunking & Metadata

## Multiple Choice Questions (Single Correct)

### Q1. Easy

A **hospital helpdesk bot** is asked about MRI safety rules. Instead of guessing, it searches stored manual chunks and then writes an answer from those chunks.

What approach is this?

A. Retrieval-Augmented Generation (RAG)  
B. Model fine-tuning only  
C. Random token sampling  
D. Database backup scheduling  

**Correct Answer:** A

**Answer Explanation:**  
RAG first **retrieves** useful documents or chunks, then the model **generates** an answer using that retrieved context. Fine-tuning, random sampling, and backups are different activities.

---

### Q2. Easy

A support bot retrieves this policy line:

> "Refunds take 7 working days."

It answers:

> "Refunds take 7 working days."

How should this answer be classified?

A. Grounded  
B. Not grounded  
C. Prompt injection  
D. Metadata filter error  

**Correct Answer:** A

**Answer Explanation:**  
The answer matches the retrieved source text, so it is **grounded**. It is not inventing facts outside the context.

---

### Q3. Easy

An **equipment manual** has 400 pages. A technician asks for one fault-code explanation, but search keeps returning the whole PDF instead of the exact section.

What is the most direct reason to split documents into **chunks**?

A. To make smaller searchable pieces so the right section can be retrieved  
B. To remove the need for a vector database  
C. To stop users from asking follow-up questions  
D. To avoid storing metadata  

**Correct Answer:** A

**Answer Explanation:**  
Chunking breaks large documents into smaller searchable units so retrieval can return the **exact useful section**, not the entire file.

---

### Q4. Easy

A **shopping support bot** has chunks labelled with `product`, `status`, and `doc_type`. Before similarity search, the engineer applies:

```text
product = "laptop"
status = "active"
```

What is this step called?

A. Metadata filter  
B. Embedding training  
C. Output sanitization  
D. Prompt injection  

**Correct Answer:** A

**Answer Explanation:**  
A **metadata filter** restricts retrieval to chunks whose labels match selected conditions — like searching only one shelf before picking the best book.

---

### Q5. Moderate

A company is preparing its policy PDFs for a RAG system. Chunking, embedding, and storing vectors in the vector database happen once during setup. A user question is answered later when someone opens the chat app.

When does **chunking** mainly happen in this workflow?

A. At indexing time  
B. At inference time only  
C. Only when the user gives thumbs down  
D. Only during human evaluation  

**Correct Answer:** A

**Answer Explanation:**  
Chunking is part of **indexing time** — the offline preparation phase. At **inference time**, the system retrieves already-chunked content and generates an answer.

---

### Q6. Moderate

A team is building a RAG bot for a **technical equipment manual**. Retrieval quality is weak with 512-character recursive chunks because answers are getting cut mid-procedure.

Which chunking choice best matches the notes for improving meaning-focused retrieval, even though indexing takes longer?

A. Semantic chunking  
B. Removing all metadata  
C. Storing one full PDF as a single chunk always  
D. Disabling the vector database  

**Correct Answer:** A

**Answer Explanation:**  
**Semantic chunking** groups related ideas by meaning, which often improves retrieval for manuals and technical docs. It is slower during indexing but can return better chunks at answer time.

---

## Multiple Select Questions (Multiple Correct)

### Q7. Moderate

A **product support team** is designing chunk metadata so retrieval can narrow the corpus before similarity search.

Which of the following are common metadata fields discussed for RAG chunks?

A. `doc_type`  
B. `product`  
C. `status`  
D. `batch_normalization_rate`  

**Correct Answers:** A, B, C

**Answer Explanation:**  
`doc_type`, `product`, and `status` are standard metadata examples used for filtering policies, products, and active versus archived content. `batch_normalization_rate` is not a RAG metadata field from this lesson.

---

### Q8. Moderate

A **banking FAQ bot** must follow grounding rules when answering from retrieved policy chunks.

Which statements about **grounding** are correct?

A. If the answer is not visible in retrieved context, the bot should not invent it  
B. When context says "return within 10 days," answering "10 days" is grounded  
C. When no relevant context is found, answering "usually 10 days" from general guesswork is grounded  
D. Grounding means making the model output depend on verified retrieved context  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Grounded answers must come from retrieved source material. Matching retrieved text is grounded, and outputs should depend on verified context. Guessing when no context is found is **not grounded**.

---

### Q9. Hard

After a RAG demo, the engineering lead asks which quality checks failed for a bad answer about **Tesla 2022 revenue**.

Which items belong to the **RAG triad**?

A. Context relevance — did retrieval bring the right chunks for the question?  
B. Groundedness — is the answer supported by the retrieved chunks?  
C. Answer relevance — is the answer on-topic for what was asked?  
D. Git commit hash — is the repository clean?  

**Correct Answers:** A, B, C

**Answer Explanation:**  
The **RAG triad** evaluates context relevance, groundedness, and answer relevance as separate checks. A Git commit hash is unrelated to RAG answer quality.

---

### Q10. Hard

A **field technician bot** gives slow, confusing, or outdated answers. The team is debugging retrieval before changing prompts.

Which symptom-and-fix pairs are correct according to the debugging guidance?

A. Wrong product information → likely missing `product` metadata filter  
B. Slow answers from searching the full corpus → add metadata filters before similarity search  
C. No citation shown to the user → likely missing source tags such as `source_file`  
D. Old policy answer → first fix should always be retraining the LLM from scratch  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Wrong-product answers, slow full-corpus search, and missing citations map to missing product filters, missing pre-filters, and missing source metadata. For stale content, the notes recommend **re-indexing** outdated chunks — not jumping straight to full LLM retraining.

---
