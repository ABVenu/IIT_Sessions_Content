# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A bank branch chatbot answers: *"What is the fee for early loan closure?"* using only a general LLM API — no company PDFs. Customers often get wrong fee amounts.

What is the **most likely** reason?

A. The LLM was never given this bank’s internal fee schedule as retrieved context  
B. The LLM cannot process English text  
C. Vector databases delete fee schedules every midnight  
D. Loan fees can only be answered by fine-tuning, never by retrieval

**Correct Answer:** A

**Answer Explanation:**  
Company fees are private documents. Without retrieving those passages into the prompt, the model guesses from general training memory.

**Why other options are wrong:**  
- B: LLMs handle English; the gap is missing private knowledge.  
- C: Vector DBs do not auto-delete nightly as a rule of RAG.  
- D: RAG retrieves policy text at query time; fine-tuning is not required for this use case.

---

## Q2 (MCQ, Easy)

A developer loads every PDF inside a folder with one LangChain call:

```python
loader = PyPDFDirectoryLoader("Annual_Reports")
documents = loader.load()
```

What does this loader return?

A. A list of LangChain **Document** objects (text + metadata such as source and page)  
B. A finished LLM answer string for each PDF  
C. Only file names, without reading page text  
D. A SQL table of financial ratios

**Correct Answer:** A

**Answer Explanation:**  
`PyPDFDirectoryLoader` reads each PDF in the folder into LangChain **Document** objects that carry `page_content` and metadata.

**Why other options are wrong:**  
- B: Loading is ingest, not generation.  
- C: The loader reads page text, not names alone.  
- D: No SQL table is created by this call.

---

## Q3 (MCQ, Easy)

A long annual report is cut into overlapping windows using `RecursiveCharacterTextSplitter` with `chunk_size=512` and `chunk_overlap=16`.

Why is **chunk overlap** useful?

A. A shared margin helps text split at a boundary still appear complete in at least one neighbouring chunk  
B. It encrypts embeddings before Chroma storage  
C. It replaces the need for a document loader  
D. It permanently increases the LLM’s maximum context window

**Correct Answer:** A

**Answer Explanation:**  
Overlap copies characters from the end of one chunk into the start of the next so boundary sentences are less likely to be lost.

**Why other options are wrong:**  
- B: Overlap is a splitting idea, not encryption.  
- C: Loaders still read the source files.  
- D: Overlap does not change the model’s token limit.

---

## Q4 (MCQ, Easy)

In a RAG notebook, retrieved chunks are placed under `##context` and the user question under `##question` inside one user message.

What is the main purpose of these **delimiters**?

A. Help the LLM reliably separate evidence text from the question  
B. Compress the Chroma index to half its size  
C. Replace the embedding model with keywords  
D. Force the LLM temperature to 1.0

**Correct Answer:** A

**Answer Explanation:**  
Labelled sections (`##context` / `##question`) make it clearer which part of the user message is evidence and which part is the ask.

**Why other options are wrong:**  
- B: Delimiters do not compress the vector store.  
- C: Embeddings still drive retrieval.  
- D: Temperature is set on the LLM call, not by delimiter text.

---

## Q5 (MCQ, Moderate)

An engineer embeds Tesla report chunks with **GTE-large**, then later queries Chroma using a **different** embedding model.

What is the **most likely** symptom?

A. Similarity search returns poor or meaningless matches  
B. Chroma automatically re-embeds all chunks with the new model  
C. The PDF loader stops reading metadata  
D. Delimiters in the prompt become invalid UTF-8

**Correct Answer:** A

**Answer Explanation:**  
Query vectors and stored vectors must live in the **same** embedding space. Mixing models breaks distance comparisons.

**Why other options are wrong:**  
- B: Chroma does not silently re-embed when the query model changes.  
- C: Loaders are unrelated to the query-time embedding mismatch.  
- D: Delimiters are plain text labels; encoding is unrelated.

---

## Q6 (MCQ, Moderate)

A RAG app sets `search_kwargs={"k": 100}` on a large product-manual corpus. Users complain answers feel **slow**, even when many chunks look related.

What is the **best** explanation from a latency trade-off view?

A. Higher **k** fetches more chunks and fills a larger prompt, so retrieval and generation take longer  
B. Higher **k** always deletes the Chroma collection  
C. Higher **k** turns off the system message  
D. Higher **k** forces temperature to 1.0

**Correct Answer:** A

**Answer Explanation:**  
Raising **k** increases retrieval work and prompt size. Accuracy and speed trade off; **k = 5** is a common demo default before tuning.

**Why other options are wrong:**  
- B: **k** does not delete collections.  
- C: System messages stay under your control.  
- D: Temperature is independent of **k**.

---

## Q7 (MSQ, Moderate)

Which steps belong to the **offline prepare / ingest** path (done until documents change)?

A. Load PDFs with `PyPDFDirectoryLoader`  
B. Split text with `RecursiveCharacterTextSplitter`  
C. Call `retriever.get_relevant_documents` on a live user question  
D. Embed chunks and store them with `Chroma.from_documents`

**Correct Answers:** A, B, D

**Answer Explanation:**  
Prepare = load → split → embed → store. Live retrieval runs on the **online answer** path when a user asks a question.

**Why other options are wrong:**  
- C: `get_relevant_documents` is query-time retrieval, not offline prepare.

---

## Q8 (MSQ, Moderate)

A grounded RAG system message includes:

- Answer **only** using the supplied context  
- If the answer is missing, say **I don't know**  
- Do not mention the context block in the final reply  

Which behaviours match these rules?

A. A revenue question answered using numbers that appear in retrieved chunks  
B. An off-topic leave-policy question on a finance PDF gets an honest **I don't know**  
C. The model invents a confident fee schedule when no chunk mentions fees  
D. The model quotes random internet knowledge instead of the retrieved PDF text

**Correct Answers:** A, B

**Answer Explanation:**  
Grounding rules keep answers tied to retrieved text and force refusal when evidence is missing.

**Why other options are wrong:**  
- C/D: Inventing or using outside knowledge violates “answer only from context.”

---

## Q9 (MSQ, Hard)

A support engineer debugs a LangChain + Chroma RAG notebook that sometimes invents numbers and sometimes misses facts that exist in the PDF.

Which issues can **realistically** cause these symptoms?

A. Chunk size is extreme (entire PDF = one chunk, or tiny one-character chunks)  
B. `temperature` is set to 0 on the Groq generation call  
C. The app calls the LLM with the question only (no `##context` block)  
D. Top-k is set to 1 for a question that needs facts from two distant pages

**Correct Answers:** A, C, D

**Answer Explanation:**  
Bad chunking hurts retrieval, skipping context causes ungrounded answers, and too-low **k** can omit needed pages. **`temperature=0`** is preferred for deterministic RAG — it is not a cause of inventing numbers in the usual case.

**Why other options are wrong:**  
- B: Temperature 0 typically *reduces* random variation; it is recommended for grounded policy/finance answers.

---

## Q10 (MSQ, Hard)

Which statements correctly describe the **imperative** RAG answer path used with a prepared Chroma retriever?

A. `retriever.get_relevant_documents(query)` embeds the query and returns top-k Documents  
B. Retrieved `page_content` strings are joined into one context block before generation  
C. A Groq chat call uses a RAG **system** message plus a user message that contains context and question  
D. `RunnablePassthrough()` must pipe the question through an LCEL `|` chain for any RAG answer to work

**Correct Answers:** A, B, C

**Answer Explanation:**  
This session’s answer path is retrieve → join context → fill delimiter template → call the LLM (for example Groq with `temperature=0`). LCEL pipe chains are a later composition style, not required for the imperative pattern.

**Why other options are wrong:**  
- D: LCEL / `RunnablePassthrough` is not required for the imperative retrieve-augment-generate path taught here.
