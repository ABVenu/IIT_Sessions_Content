# Objective Assignment: Building a RAG Pipeline

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

ShopKart's engineering team replaces four hardcoded policy strings with files inside a `policy_documents/` folder. What is the main responsibility of a **document loader** in this pipeline?

A. Write grounded customer replies without reading any file  
B. Read external policy files and return text for cleaning, chunking, and indexing  
C. Retrain the BGE embedding model on every customer question  
D. Permanently delete the Chroma collection after each chat

**Correct Answer:** B

**Answer Explanation:**  
B is correct because a document loader is the file-reading step that brings TXT or PDF policy content into Python for downstream preparation.

A is incorrect because reply generation happens later in the RAG loop. C is incorrect because BGE is loaded once and reused, not retrained per question. D is incorrect because Chroma persistence is intentional, not deleted after each chat.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A developer runs `build_knowledge_base()` once on Monday morning. Through the week, hundreds of customer questions use only `retrieve_policy_chunks(...)` and `generate_grounded_answer(...)`. Why is ingestion described as an **offline** step?

A. It works only when the laptop has no internet connection  
B. File loading, chunking, and embedding are done before live queries—not repeated for every customer message  
C. Groq cannot run while Chroma files exist on disk  
D. PDF files can be opened only in airplane mode

**Correct Answer:** B

**Answer Explanation:**  
B is correct because ingestion (load → clean → chunk → embed → store) is a one-time preparation phase; the online loop handles individual questions.

A is incorrect because offline here means pipeline phase, not network status. C is incorrect because Groq and Chroma are used together in the online loop. D is incorrect because PDF reading is unrelated to airplane mode.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

The warranty team shares `warranty_policy.pdf` as a text-based PDF (not a scanned image). Which approach matches the lab pattern for extracting readable text page by page?

A. `pypdf` `PdfReader` with `page.extract_text()`  
B. Groq chat API summarising only the file name  
C. Chroma automatically parsing PDF bytes with no Python loader  
D. Skipping extraction and storing the raw PDF binary as one Chroma document

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `pypdf` reads PDF pages and returns extractable text for cleaning and chunking.

B is incorrect because the filename alone is not policy content. C is incorrect because Chroma stores prepared text and vectors, not automatic PDF parsing in this lab. D is incorrect because binary PDF data is not searchable text for embedding.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

After chunking, each stored excerpt carries metadata. A file named `returns_policy.txt` is loaded from `policy_documents/`. What **category** label should `infer_policy_category(...)` assign?

A. shipping  
B. refunds  
C. returns  
D. general

**Correct Answer:** C

**Answer Explanation:**  
C is correct because the helper checks the lowercase file name for keywords like `return` and maps it to the returns policy area.

A is incorrect because `shipping` would match a shipping file name. B is incorrect because `refund` maps to refunds, not returns. D is incorrect because the file name matches a known policy pattern.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A developer configures `DEFAULT_CHUNK_SIZE = 100` and `DEFAULT_CHUNK_OVERLAP = 20`. The first chunk covers words at indices 0–99. After that chunk is stored, where does the **second** chunk start in the word list?

A. Index 0 again  
B. Index 80  
C. Index 100 with no shared words  
D. Index 120

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the overlap stride moves the start forward by `chunk_size - overlap` → `100 - 20 = 80`, so the next chunk shares 20 words with the previous one.

A is incorrect because chunks progress forward, not restart from zero. C is incorrect because overlap deliberately shares tail words. D is incorrect because 120 would skip words without the intended overlap window.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A customer asks about warranty repair, but Rank 1 retrieval shows `category: shipping`. The grounded answer sounds polite yet cites delivery timelines. Debugging guidance says to suspect **ingestion or chunking** before blaming the generator. Why?

A. Groq cannot read category metadata inside the grounded prompt  
B. Wrong policy area at Rank 1 usually means loaders, chunk boundaries, or indexing sent poor evidence—not that the LLM refused to read  
C. Chroma deletes all chunks when category metadata is wrong  
D. `top_k` must always be 1 for warranty questions

**Correct Answer:** B

**Answer Explanation:**  
B is correct because retrieval quality depends on how files were loaded, split, and indexed; a mismatched Rank 1 category is usually a retrieval-side issue.

A is incorrect because the prompt includes category labels from metadata. C is incorrect because Chroma does not delete data due to category mismatch. D is incorrect because top_k is a retrieval count, not a per-topic setting.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

Which steps occur inside `build_knowledge_base(...)` in the correct logical order for the ShopKart file-based pipeline?

A. `load_all_policy_documents(...)` reads `.txt` and `.pdf` files from `policy_documents/`  
B. `create_chunks_from_documents(...)` splits loaded text into searchable units with metadata  
C. `generate_grounded_answer(...)` writes the final customer reply before any file is read  
D. `index_policy_chunks(...)` encodes chunks with BGE and upserts them into Chroma  
E. `retrieve_policy_chunks(...)` runs before any policy file is loaded

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because loading is the first ingestion step. B is correct because chunking happens on loaded documents before indexing. D is correct because embedding and upsert are the final offline storage step.

C is incorrect because generation belongs to the online question-answering loop, not `build_knowledge_base`. E is incorrect because retrieval happens after the knowledge base exists.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A quality analyst reviews terminal output right after `retrieve_policy_chunks(...)` runs for a ShopKart ticket. Which inspection steps are appropriate?

A. Check whether Rank 1 `metadata["category"]` matches the expected policy area  
B. Read Rank 1 chunk `text` and confirm it relates to the customer's question  
C. Ignore `distance` values completely because they are never useful  
D. Compare the customer's intent with the excerpt meaning, not only exact keyword overlap  
E. Assume Rank 1 is always business-correct without reading the excerpt text

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because category tags show which policy file area surfaced first. B is correct because the excerpt body must be read before trusting the answer. D is correct because semantic retrieval matches meaning, not just identical words.

C is incorrect because distance helps compare relative match strength across ranks. E is incorrect because Rank 1 is the nearest vector, not a guarantee of business correctness in every edge case.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A learner loads four ShopKart TXT policies, chunks them, and indexes with `SentenceTransformer("BAAI/bge-small-en-v1.5")` into `shopkart_policy_kb_v2` using `embedding_function=None`. Which statements are technically correct?

A. Total chunk count after ingestion should be greater than four because each file produces multiple chunks  
B. The same embedding model must encode policy chunks at index time and customer queries at search time  
C. `collection.query(...)` needs manually supplied `query_embeddings` in this setup  
D. Storing each entire policy file as one Chroma row without chunking always gives the best retrieval precision for long policies  
E. Metadata fields like `source` and `category` help trace which policy file supplied each excerpt

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because multi-paragraph files are split into many chunks. B is correct because distances are meaningful only in the same embedding space. C is correct because `embedding_function=None` means manual `model.encode(...)` for queries. E is correct because metadata supports auditing retrieval provenance.

D is incorrect because long whole-file rows are too coarse for precise retrieval—the lab chunks for better search granularity.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A ShopKart file-based assistant tells a customer they have **30 days** to return an unopened phone, but `returns_policy.txt` in `policy_documents/` says **7 calendar days**. Which failure explanations are plausible?

A. The TXT file in `policy_documents/` was outdated or edited incorrectly before indexing  
B. A chunk boundary split eligibility wording across chunks, so retrieval missed the correct rule  
C. Retrieval surfaced weak evidence, but the generator faithfully followed those excerpts—still producing a wrong business answer  
D. Running retrieval once makes hallucination impossible in all cases  
E. Renaming the folder to `policy_files/` without updating `POLICY_FOLDER` can lead to no files loaded or an empty knowledge base

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because indexed text is the source of truth—stale files produce wrong answers. B is correct because bad splits can hide the right rule from top-k results. C is correct because generation can be faithful to bad evidence. E is correct because the loader path must match the actual folder name.

D is incorrect because RAG reduces guessing risk but does not make hallucination impossible.
