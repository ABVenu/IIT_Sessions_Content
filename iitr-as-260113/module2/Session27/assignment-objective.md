# Assignment — Objective (Vector search systems)

**Instructions:** Answer all questions. For multiple-select questions (MSQ), select **all** options that apply.

---

## Section A — Multiple Choice, Single Correct (MCQ)

### Q1 (Easy)

Priya runs a small help desk. Customers often type “I need my cash returned” instead of the exact phrase “refund policy” in the FAQ. Which approach best matches **meaning** between the user’s words and stored articles?

- A) Store only lowercase versions of FAQs and use exact string match  
- B) Split the query into keywords and require every keyword to appear  
- C) Convert the query and FAQs into embeddings and retrieve nearest neighbors in vector space  
- D) Sort FAQs alphabetically and return the first match  

**Answer Explanation (for Assess):**  
**Correct answer: C.** Vector search embeds text into vectors so “cash returned” and “refund” can be close in semantic space even when words differ.  
**A** only normalizes case; it does not fix different wording. **B** is keyword-only and can miss paraphrases. **D** is unrelated to relevance.

---

### Q2 (Easy)

For a typical **vector search** pipeline, what is the correct high-level order of steps?

- A) Query embedding → vector DB → raw text → embeddings  
- B) Data → embeddings → vector DB → query embedding → similarity search → top-k results  
- C) Vector DB → data → embeddings → top-k results  
- D) Similarity search → embeddings → data storage  

**Answer Explanation (for Assess):**  
**Correct answer: B.** You embed source text, store vectors (with text and metadata) in a vector database, embed the user query in the same space, then run nearest-neighbor search and return the top-k matches.  
**A, C, D** misorder ingestion vs query or omit embedding documents before storage.

---

### Q3 (Easy)

Ravi uses Chroma with `PersistentClient(path="./chroma_store")`. What is the main purpose of this choice compared to a purely in-memory client?

- A) It automatically downloads embedding models from the internet  
- B) It stores the database on disk so data can persist across program runs  
- C) It disables metadata filtering  
- D) It replaces the need for any embedding model  

**Answer Explanation (for Assess):**  
**Correct answer: B.** A persistent client writes data under the given path so collections survive process restarts—useful for local development and testing.  
**A** is not what `PersistentClient` does. **C** is false—metadata filtering still applies. **D** is false—you still need embeddings from a model or API.

---

### Q4 (Easy)

A collection is created with `embedding_function=None` and embeddings are supplied manually during `upsert` and `query`. What must you pass to `collection.query` for similarity search?

- A) Only `query_texts` — Chroma will infer vectors without an embedding function  
- B) `query_embeddings` built with the same kind of embedding process used at ingest  
- C) `where` alone, without any embeddings  
- D) The list of document IDs to compare  

**Answer Explanation (for Assess):**  
**Correct answer: B.** With no embedding function on the collection, Chroma does not compute vectors for you—you must supply `query_embeddings` that live in the same embedding space as the stored vectors.  
**A** is wrong: without an attached embedding function, Chroma will not create query vectors automatically. **C** applies filters but does not substitute for query vectors in similarity search. **D** describes ID-based lookup, not semantic search.

---

### Q5 (Moderate)

Neha ingests documents with `collection.upsert(...)`. She later adds another batch where some IDs already exist. She wants new rows inserted and existing IDs updated in one call. Why is `upsert` appropriate compared to `add`?

- A) `add` always overwrites; `upsert` never does  
- B) In Chroma, `add` ignores duplicate IDs; `upsert` inserts new records or updates existing ones  
- C) `upsert` only works for in-memory clients  
- D) `add` and `upsert` behave identically for duplicate IDs  

**Answer Explanation (for Assess):**  
**Correct answer: B.** Chroma’s semantics: duplicate IDs with `add` do not get overwritten; `upsert` is the right choice for insert-or-update in one step.  
**A** reverses the behavior. **C** is false. **D** is false—they differ when an ID already exists.

---

### Q6 (Moderate)

For a shipping-related question, you want **semantic** ranking but only among documents where `category` is `"shipping"`. Which approach is correct?

- A) `collection.query(query_embeddings=..., n_results=5)` with no filter, then manually delete non-shipping rows  
- B) `collection.get(where={"category": "shipping"})` without query embeddings  
- C) `collection.query(query_embeddings=..., n_results=2, where={"category": "shipping"})`  
- D) Store only shipping docs in a separate Python list and never use Chroma  

**Answer Explanation (for Assess):**  
**Correct answer: C.** Combine vector similarity with metadata filtering using `where` on `query`, so ranking happens only within the filtered set.  
**A** pulls irrelevant categories first, then filters in application code—wasteful and wrong if you need ranked results within a slice. **B** returns by metadata without ranking the query embedding. **D** sidesteps the vector database entirely.

---

## Section B — Multiple Select, Multiple Correct (MSQ)

*Select all correct options.*

### Q7 (Moderate — MSQ)

Which statements about **top-k** retrieval are correct?

- A) `n_results` in `collection.query` controls how many nearest neighbors are returned  
- B) Returning only k=1 is always best for RAG because it minimizes noise  
- C) Very large k can add irrelevant documents  
- D) In RAG setups, k is often chosen in ranges like 3, 5, or 10 depending on chunk size and the model’s context window  

**Answer Explanation (for Assess):**  
**Correct: A, C, D.**  
**A:** `n_results` sets how many neighbors are returned from similarity search.  
**C:** A very large k can dilute precision with less relevant chunks.  
**D:** Practitioners commonly tune k against chunk size and how much context the downstream model can consume.  
**B is incorrect:** k=1 can miss useful supporting documents; minimizing noise is not the only goal.

---

### Q8 (Moderate — MSQ)

You use Sentence Transformers locally with `SentenceTransformer("all-MiniLM-L6-v2")` and `model.encode(documents, convert_to_numpy=True)`. Which are true?

- A) The output vectors are human-readable sentences  
- B) Embeddings typically place paraphrases like “refund for returned item” and “money back after return” relatively close in vector space  
- C) `convert_to_numpy=True` helps obtain numerical arrays you can pass into Chroma as embeddings  
- D) Sentence Transformers officially recommends Python 3.10+ as a baseline  

**Answer Explanation (for Assess):**  
**Correct: B, C, D.**  
**B:** Dense sentence embeddings are trained so paraphrases and related meanings map nearby.  
**C:** Chroma expects numeric vectors; NumPy arrays convert cleanly to lists for the client.  
**D:** The Sentence Transformers project documents Python 3.10+ as the recommended baseline.  
**A is incorrect:** embedding vectors are arrays of numbers, not readable text.

---

### Q9 (Hard — MSQ)

After storing records with ids, documents, metadatas, and embeddings, which methods are appropriate to **verify or inspect** what Chroma actually stored?

- A) `collection.count()`  
- B) `collection.peek()`  
- C) `collection.query` with an empty `query_embeddings` list  
- D) Relying on `print(documents)` in Python before `upsert` only  

**Answer Explanation (for Assess):**  
**Correct: A, B.**  
`count()` confirms how many records exist; `peek()` surfaces a sample of stored entries—standard sanity checks after ingest.  
**C is incorrect:** similarity `query` needs valid query embeddings; an empty list is not a meaningful verification step.  
**D is incorrect:** printing in-memory Python structures before persistence does not prove the vector DB stored or can retrieve the data correctly.

---

### Q10 (Hard — MSQ)

Which options correctly contrast **API-based embeddings** (e.g., OpenAI) with **local Sentence Transformers** when feeding Chroma?

- A) API embeddings suit teams that want a hosted model and managed infrastructure  
- B) Local embeddings help keep recurring cost low for experiments and work offline when the model runs locally  
- C) OpenAI’s current embedding model lineup includes names such as `text-embedding-3-small` and `text-embedding-3-large`  
- D) Chroma requires API embeddings; local models are unsupported  

**Answer Explanation (for Assess):**  
**Correct: A, B, C.**  
**A:** Vendor APIs offload hosting and scaling of the embedding model.  
**B:** Running a local model avoids per-call API charges for many trials and can run without network once weights are available.  
**C:** Those model identifiers are valid OpenAI embedding model names as of common API documentation.  
**D is incorrect:** Chroma accepts any compatible float vectors—you can populate embeddings from a local model, an API, or another pipeline.

---

## Difficulty map (for authors)

| Q | Type | Difficulty |
|---|------|------------|
| Q1–Q4 | MCQ | Easy |
| Q5–Q6 | MCQ | Moderate |
| Q7–Q8 | MSQ | Moderate |
| Q9–Q10 | MSQ | Hard |
