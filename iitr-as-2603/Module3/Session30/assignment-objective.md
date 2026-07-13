# Objective Assignment: RAG — Chunking & Document Preparation

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

**Reuse note:** Adapted from `iitr-as-2601` Module3 Session40. Most items reused as-is against this cohort’s `Lecture Notes Released.md`. Question 6 replaced (chat-upload framing not in these notes). Question 9 wording fixed (512/16 is not ~15% overlap).

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A legal-tech team embeds an entire **80-page** policy PDF as **one vector** in Chroma. Users ask narrow questions such as *"What is the refund window?"* but search keeps returning unrelated sections about shipping and warranties.

What is the **most likely** root cause?

A. The whole document was embedded as one vector, so meanings get averaged across many topics  
B. Chroma cannot store PDF file names  
C. The embedding model only works on Python code, not English text  
D. Top-k search was disabled by using `n_results=1`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because one vector for a long multi-topic document blurs distinct ideas; chunking splits content so each row holds roughly one idea.

B is incorrect because file naming is handled via metadata, not the cause of vague whole-file embeddings. C is incorrect because sentence-transformer models encode English policy text. D is incorrect because `n_results=1` still returns the nearest vector—it does not explain topic mixing inside that single vector.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A support-bot engineer uses **fixed-size chunking with overlap**. A return rule is split across two windows: *"...within 30 days of"* ends chunk 4 and *"delivery. Items must..."* starts chunk 5.

Why is **overlap** added between neighbouring chunks?

A. To repeat a shared margin so a sentence split at a boundary can still appear whole in at least one chunk  
B. To encrypt metadata before upsert  
C. To double the embedding model size automatically  
D. To replace the need for a vector database

**Correct Answer:** A

**Answer Explanation:**  
A is correct because overlap copies text from the end of one chunk at the start of the next, reducing lost context at cuts.

B is incorrect because metadata is stored as labels, not encrypted by overlap. C is incorrect because overlap affects chunk count, not model dimensions. D is incorrect because overlap is a text-splitting idea; storage still needs a vector DB.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

In the manual `policy_chunks` lab, each row stores `text`, `metadata` (for example `source_id`, `page`), and an embedding vector.

Which part is **actually encoded** into the embedding vector?

A. Only the chunk `text`  
B. Only the `source_id` string  
C. The `text` plus all metadata fields combined  
D. Only the `page` number

**Correct Answer:** A

**Answer Explanation:**  
A is correct because embeddings are built from chunk body text; metadata is stored for citation and filters, not vectorized in this lab.

B, C, and D are incorrect because metadata fields are attached separately in `metadatas=` and are not passed to `model.encode` for the chunk vector.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A corpus loader ingests a plain `.txt` policy file named `returns_policy.txt` (no PDF pages).

What **`page`** value should be stored on each record from that file?

A. 0  
B. 1  
C. The number of chunks created  
D. Leave `page` empty / null

**Correct Answer:** A

**Answer Explanation:**  
A is correct because plain-text files use page index `0` in this workflow; PDFs use per-page indices starting at 0.

B is incorrect because page 1 would wrongly imply a second PDF page for a single text file. C is incorrect because chunk count is tracked separately as `chunk_index`, not `page`. D is incorrect because traceability expects an explicit page field.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A developer chunks ShopEasy policies with `chunk_size = 500` and `overlap = 75` using a sliding character window (step = `chunk_size - overlap`).

After finishing chunk 0 starting at index 0, where does chunk 1 **start** in the parent text?

A. Character index 425  
B. Character index 500  
C. Character index 75  
D. Character index 575

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the window advances by `500 - 75 = 425` characters while sharing 75 characters of overlap with the previous chunk.

B is incorrect because starting at 500 would mean **no** overlap. C is incorrect because 75 is only the overlap length, not the step. D is incorrect because 575 does not match the defined step rule.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A hospital support team wants a chatbot that can answer questions from a confidential MRI **operating manual**. A public LLM alone has never seen that private document.

Which approach is **most appropriate**?

A. Use **RAG**: chunk and index the manual, retrieve relevant chunks for each question, then ask the LLM to answer using that context  
B. Rely on **normal generation** only — the LLM will invent the correct error codes from general training  
C. Embed the whole manual as one vector and never retrieve smaller segments  
D. Store only file names in Chroma and skip embeddings entirely

**Correct Answer:** A

**Answer Explanation:**  
A is correct because proprietary manuals are not reliable in public LLM weights; RAG retrieves your chunks first, then the model answers from that context.

B is incorrect because normal generation fails on confidential company IP. C is incorrect because one whole-file vector blurs many topics. D is incorrect because semantic search needs embeddings of chunk text, not names alone.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A team builds traceable policy chunks before upserting to Chroma.

Which statements about **metadata** are correct?

A. `source_id` usually holds the file name so answers can cite which document matched  
B. `page` helps locate which PDF page a chunk came from; use `0` for plain `.txt` files  
C. Metadata vectors are averaged with text vectors inside `model.encode` in this lab  
D. `chunk_index` records the order of chunks created from the same parent page  
E. Storing metadata is optional if the collection name already says `policy_chunks`

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because `source_id` answers “which file?” B is correct because page indexing supports PDF traceability and `0` for text files. D is correct because `chunk_index` disambiguates multiple chunks from one page.

C is incorrect because only chunk text is embedded. E is incorrect because collection naming does not replace per-chunk traceability fields.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

After upserting chunked policies into `policy_chunks` with `embedding_function=None`, a learner wants to **verify storage** before running semantic queries.

Which checks are sensible?

A. `collection.count()` to confirm how many chunk rows were stored  
B. `collection.peek()` to sample ids, text, and metadata quickly  
C. `collection.get(ids=[one_known_id])` to spot-check one exact row  
D. Manually edit binary files inside `./chroma_store` to fix a typo in chunk text  
E. Keep `ids`, `documents`, `metadatas`, and `embeddings` lists index-aligned during `upsert`

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, and C are correct verification steps taught for count, sample peek, and exact id lookup. E is correct because misaligned parallel lists attach wrong vectors or metadata to a chunk.

D is incorrect because internal Chroma files should not be hand-edited; fix data in code and upsert again.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

An engineer chunks a large annual report with `chunk_size = 512` and `chunk_overlap = 16`.

Which statements are correct?

A. The window should advance by **496** characters between chunk starts (`512 - 16`)  
B. `overlap` must stay **smaller than** `chunk_size` or the splitter may never move forward  
C. Setting `overlap >= chunk_size` is invalid for a sliding window  
D. This pair follows the same fixed-size + overlap strategy used on shorter policy text, with numbers tuned for long documents  
E. Semantic chunking is the **primary hands-on strategy** required in this module’s core lab

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A is correct for the step size. B and C are correct safety rules for overlap versus chunk size. D is correct because large PDFs use the same Strategy 1 with tuned numbers (512/16), while short policies often use 500/75.

E is incorrect because semantic chunking was introduced only as an advanced look-ahead; fixed-size + overlap is the primary lab skill.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A ShopEasy retriever returns a **long wall of text** at Rank 1 for a short question about free shipping, and the text mixes return rules and shipping rules in one chunk.

Which tuning actions are **reasonable first steps**?

A. **Lower** `chunk_size` so each chunk holds fewer mixed ideas  
B. **Raise** `overlap` if an important sentence was cut across a boundary  
C. Switch the **query** embedding to a different model while keeping old document embeddings  
D. **Raise** `overlap` until it equals `chunk_size` to guarantee context  
E. Tune chunking and metadata quality before blaming the vector database tool alone

**Correct Answers:** A, B, E

**Answer Explanation:**  
A is correct because oversized chunks create blurry embeddings that mix topics. B is correct when boundary cuts lose half a rule. E is correct because retrieval quality often reflects preparation, not only the DB engine.

C is incorrect because mixing encoders breaks distance meaning. D is incorrect because `overlap >= chunk_size` stops proper window advancement.
