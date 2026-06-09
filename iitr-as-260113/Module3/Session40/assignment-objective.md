# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A startup builds a customer-support chatbot using only a general-purpose LLM API. Customers ask: *"What is your company's 7-day electronics return rule?"* The bot often gives vague or incorrect answers.

What is the **most likely** reason?

A. The LLM was never trained on this company's internal policy documents  
B. The LLM cannot process English text  
C. The API key automatically deletes company policies after 24 hours  
D. Return policies can only be stored in SQL tables, never in an LLM workflow

**Correct Answer:** A

**Answer Explanation:**  
Company-specific policies are usually **not** in public training data. Without retrieval from your own documents, the model guesses or generalises.

**Why other options are wrong:**  
- B: LLMs handle English well; the issue is missing private knowledge.  
- C: API keys do not erase domain knowledge.  
- D: Policies can be served via RAG + vector DB; SQL is not the only path.

---

## Q2 (MCQ, Easy)

In a LangChain ingest script, `Chroma` is created with `persist_directory="chroma_db"`.

What does **persist** mean in this setup?

A. Vectors are saved locally on disk so later scripts can reload them without re-embedding everything  
B. The LLM permanently memorises all policies inside its weights  
C. Markdown files are automatically deleted after embedding  
D. The retriever skips similarity search on the next run

**Correct Answer:** A

**Answer Explanation:**  
`persist_directory` tells Chroma to store embeddings on disk (for example `chroma_db/`) so the RAG app can reload the same collection across runs.

**Why other options are wrong:**  
- B: Persist is vector-store storage, not model fine-tuning.  
- C: Source `.md` files remain unless you delete them.  
- D: Similarity search still runs when you query the reloaded store.

---

## Q3 (MCQ, Easy)

A developer configures:

```python
DirectoryLoader("documents", glob="**/*.md", loader_cls=TextLoader)
```

What files will this loader read from the `documents` folder?

A. Only Markdown (`.md`) files  
B. Only PDF files  
C. Every file type including images and videos  
D. Only Python source files

**Correct Answer:** A

**Answer Explanation:**  
The glob `**/*.md` filters to Markdown files. `TextLoader` reads them as plain text with the encoding you pass in `loader_kwargs`.

**Why other options are wrong:**  
- B/C/D: Those types need different globs or loader classes (for example `PyPDFLoader` for PDFs).

---

## Q4 (MCQ, Easy)

A policy sentence is split across two chunks: chunk 1 ends with *"...within 7 days of"* and chunk 2 starts with *"delivery for electronics."*

Why is **`chunk_overlap`** used between neighbouring chunks?

A. To repeat a shared margin so important text split at a boundary can still appear complete in at least one chunk  
B. To encrypt embeddings before storing them in Chroma  
C. To replace the need for a document loader  
D. To increase the LLM context window size automatically

**Correct Answer:** A

**Answer Explanation:**  
Overlap copies characters from the end of one chunk into the start of the next, reducing lost context at hard cuts.

**Why other options are wrong:**  
- B: Overlap is a text-splitting idea, not encryption.  
- C: You still need loaders to read files.  
- D: Overlap does not change the model's token limit.

---

## Q5 (MCQ, Moderate)

An engineer edits `return_policy.md` on disk (changes **7 days** to **14 days**) but only re-runs `langchain_rag_app.py`. The bot still answers **7 days**.

What is the **best** fix?

A. Re-run the ingest script so chunks are re-embedded and stored in Chroma again  
B. Restart the laptop only  
C. Change the LLM temperature from 0 to 1  
D. Rename the Markdown file to `.txt` without re-ingesting

**Correct Answer:** A

**Answer Explanation:**  
The RAG app reads **stored vectors**, not live file edits. After policy text changes, you must re-ingest (often after cleaning old `chroma_db` data).

**Why other options are wrong:**  
- B: Restart does not rebuild vectors.  
- C: Temperature affects randomness, not stale index content.  
- D: Renaming without re-ingest leaves old vectors unchanged.

---

## Q6 (MCQ, Moderate)

In an LCEL RAG chain:

```python
{
    "context": retriever | format_docs,
    "question": RunnablePassthrough(),
}
```

What does **`RunnablePassthrough()`** do for the `question` field?

A. Forwards the user's input question unchanged into the prompt while retrieval runs separately for `context`  
B. Embeds the question into Chroma during offline ingest  
C. Deletes the user question before it reaches the LLM  
D. Automatically fine-tunes the LLM on every query

**Correct Answer:** A

**Answer Explanation:**  
`RunnablePassthrough` passes the invoke input as-is to the `{question}` slot in the prompt template while the retriever supplies `{context}`.

**Why other options are wrong:**  
- B: Ingest embeds **documents**, not live user queries in this pattern.  
- C: The question is required in the prompt.  
- D: No fine-tuning happens at inference time.

---

## Q7 (MSQ, Moderate)

Which steps belong to the **offline ingest / prepare** path (done once until documents change)?

A. Load files with `DirectoryLoader`  
B. Split documents with `RecursiveCharacterTextSplitter`  
C. Invoke the retriever on a live customer question  
D. Embed chunks and store them with `vector_store.add_documents`

**Correct Answers:** A, B, D

**Answer Explanation:**  
Offline prepare = load → split → embed → persist. Retriever invoke happens at **query time**, not during ingest.

**Why other options are wrong:**  
- C: Retriever runs when a user asks a question in the online RAG app.

---

## Q8 (MSQ, Moderate)

A retriever is built as:

```python
vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)
```

Which statements are **correct**?

A. `search_type="similarity"` ranks chunks by embedding similarity to the query  
B. `k: 3` asks for up to three top matches per search  
C. The retriever removes the need for any vector database  
D. `as_retriever()` wraps the existing Chroma vector store for LangChain chains

**Correct Answers:** A, B, D

**Answer Explanation:**  
Similarity search returns the nearest chunk vectors; `k` caps how many are returned. The retriever sits **on top of** Chroma, not instead of it.

**Why other options are wrong:**  
- C: The vector store still holds embeddings; the retriever is a search interface.

---

## Q9 (MSQ, Hard)

A support prompt includes:

- *Use only the retrieved context*  
- *If the answer is not present, say: I don't know based on the provided documents*  
- *Mention the source file name wherever possible*

Which outcomes match this **guardrail** design?

A. A question about electronics returns cites `return_policy.md` when the rule is in retrieved chunks  
B. A question about "baby items" (not in the corpus) gets an honest refusal instead of a invented policy  
C. The bot answers general world-news questions using outside knowledge even when unrelated to policies  
D. The bot invents a 30-day baby-item return rule when no chunk mentions baby items

**Correct Answers:** A, B

**Answer Explanation:**  
Guardrails encourage **grounded, cited** answers when context exists and **safe refusal** when it does not.

**Why other options are wrong:**  
- C: Outside-knowledge answers violate "use only retrieved context."  
- D: Inventing rules is hallucination—the prompt explicitly blocks this.

---

## Q10 (MSQ, Hard)

A team debugs poor retrieval quality in a LangChain + Chroma RAG app.

Which issues can **realistically** cause wrong or stale answers?

A. Ingest used `text-embedding-3-small` but the query path uses `text-embedding-3-large`  
B. Policy Markdown was updated on disk but Chroma was never re-ingested  
C. `chunk_overlap` is set equal to `chunk_size`, so the splitter never advances  
D. `StrOutputParser` is written as `StrOutputParser` with parentheses in the LCEL chain

**Correct Answers:** A, B, C

**Answer Explanation:**  
Embedding model mismatch breaks similarity geometry. Stale Chroma data ignores file edits. `overlap >= chunk_size` is an invalid splitter configuration.

**Why other options are wrong:**  
- D: `StrOutputParser()` **with** parentheses is the correct LCEL usage; omitting `()` causes errors, not semantic retrieval drift.
