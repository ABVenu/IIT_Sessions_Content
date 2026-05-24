# Lecture Script: Embeddings & Vector Search

**Session duration:** 1 hour 50 minutes (110 minutes)  
**Audience:** Absolute beginners — Indian learners who may have no formal tech background; they should have completed **RAG Foundations** (library metaphor, five-step RAG flow, manual context demo, and an **Ollama embeddings preview**). Today is **concepts + full Chroma hands-on lab** — embed, store, and **top-k semantic search**; not a full RAG chatbot or PDF chunking pipeline.

---

**How to use this document**  
This file is **for timing and facilitation only**. It does not replace `Lecture Notes.md`; it tells you *what to do in the room*, when to circulate, and how to bridge topics. Keep definitions, code, and diagram URLs on the notes file / projector from there.

**Break rule**  
After **approximately 55–65 minutes** from session start (typically once **Chroma terminology** is clear and **pip installs** are done — **before** or **just after** the first successful `upsert` if the room is fast), take **one pause of 5–8 minutes**. Do **not** count the break as a numbered block; resume with the data-prep / client block or upsert block as noted below.

---

## 1. Opening, Recap & Today's Map (5 minutes)

- Screen-share `Lecture Notes.md` — **60-second** recap: last session = **RAG** as a library, five steps, **manual paste** demo, **text → numbers** with Ollama.
- State today aloud: **embeddings as meaning coordinates**, how to **read similarity scores**, and a **Chroma lab** — store five FAQs and run **top-k** search. **Not** today: PDF loading, chunk tuning, full RAG script.
- Read the **"In this session, you will"** bullets; **thumbs up** if anyone is unsure what a **vector** is (promise replay in Block 2).
- **Cold-call:** "In one phrase, what job does the **retriever** do in RAG?" *(finds relevant chunks before the LLM writes.)*

**Bridge sentence:** "Last time you pasted the right paragraph by hand; today you learn how machines **sort and search** sentences by meaning, then you code it in **Chroma**."

---

## 2. Embeddings as Semantic Coordinates (8 minutes)

- Official definition + **In Simple Words** from notes — embeddings = **meaning coordinates**; similar meaning → nearby numbers.
- **Music app / humming** real-life example — 30 seconds.
- **Vectors** table row: ordered list, **384** or **768** dimensions; refund sentences **near**, weather **far**.
- **Common mistake** aloud: mixing vectors from **different models** — distances become meaningless.
- Screen-share **granularity** table: **sentence** (query) vs **document chunk** (stored FAQ); **same model rule** for store and query.
- **Check for thumbs:** "Who can say in one word what we compare — spelling or **meaning**?"

**Bridge sentence:** "Coordinates are useless until you know how **text becomes numbers** and how to **read** a match score — that's the pipeline next."

---

## 3. Text to Vectors, Similarity Scores & Keyword vs Semantic (10 minutes)

- Walk the four steps: raw text → tokenization → encoding → store/compare; screen-share **session16-06** pipeline image from notes.
- **Meaning printer** analogy; link back to **Ollama** preview — today’s lab uses **Sentence Transformers** (`all-MiniLM-L6-v2`), same idea.
- On projector, run or scroll the **Encode Two Sentences** preview block — point at **vector length 384** and **first five numbers**; mention first-run **~80 MB** download.
- **Semantic similarity** + **distance** table: rank 1–3, **lower distance often = closer**, no "100% correct" — scores are **relative**.
- **Keyword vs semantic** table — one minute each; SQL for `user_id`, vectors for paraphrases.
- **Pair-share (20 seconds):** give one question that keyword search handles well vs one that needs **meaning**.

**Bridge sentence:** "Before you run code, let's **predict** which FAQ should win — then we'll prove it with vectors in the lab."

---

## 4. Predict-the-Match Activity & Why Vector Databases (7 minutes)

- Post the three FAQ lines + user question from notes on slide: *"I want to return my shoes and get my money back."*
- **Room action:** everyone writes predicted **#1** line and **one reason** in notebook — **do not reveal** answer yet.
- **Why vector DBs** — five FAQs in a Python loop is fine; **thousands** need a vector store.
- Screen-share **session17-02** SQL vs vector image; name **Chroma** (today), **FAISS** (alternative), **pgvector** (mention only).
- **Common doubt:** Chroma is **not** the embedding model — **you** encode, Chroma **stores and searches**.
- Screen-share **session18-01** Chroma lab pipeline image; narrate seven steps: Prepare → Embed → Upsert → Verify → Query → Read results.
- Define **top-k** in one sentence; repeat **same model rule**.

**Bridge sentence:** "Pipeline on screen — now we learn **Chroma vocabulary** so every line of code has a SQL-shaped mental model."

---

## 5. Chroma Terminology, Methods & get vs query (12 minutes)

- Screen-share **Chroma vs SQL** table — hit highlights: **client**, **collection**, **id**, **document**, **metadata**, **embedding**, **upsert**, **query**, **get**.
- **Coaching cupboard** analogy for collection — 30 seconds.
- Explain **`PersistentClient(path="./chroma_store")`** and **`embedding_function=None`** — you pass vectors on **upsert** and **query_embeddings** on **query**.
- Methods table: `get_or_create_collection`, `upsert`, `count`, `peek`, `query` — don't read every cell aloud.
- Screen-share **session18-04** get vs query image — **`get`** = exact id; **`query`** = nearest meaning (what RAG retrieval uses).
- **Cold-call:** "Name the **four** parallel lists you pass to **`upsert`**." *(ids, documents, metadatas, embeddings.)*
- **Pair-share (3 min):** Partner A defines **collection**; Partner B defines **embedding**; swap — B defines **query**, A defines **get**.

> **Break placement:** Target break **after Block 5** (~55 min) if installs are not started; if the room is fast and Block 6 setup is underway, break **after Block 7** (`count()` still **0**) — never skip break entirely past **70 minutes**.

---

**Break:** 5–8 minutes. Remind learners: stay in **`vector_search_lab`** folder; first **SentenceTransformer** download may still be running after break.

---

## 6. Environment Setup & Project Folder (5 minutes)

- Screen-share install commands:
  - `pip install chromadb`
  - `pip install -U sentence-transformers`
- **`python --version`** — 3.10+; mention **venv** if environments are messy.
- Live: `mkdir vector_search_lab`, `cd vector_search_lab`.
- Everyone runs imports: `import chromadb`, `from sentence_transformers import SentenceTransformer`.
- **Circulate / scan chat:** fix `ModuleNotFoundError` before FAQ data.
- **Thumbs-up check:** "Thumbs up when both imports work with no red error."

**Bridge sentence:** "Environment green — we paste **five** FAQ rows, then open an empty **collection** on disk."

---

## 7. Prepare Sample Data & Create Client + Collection (9 minutes)

- Explain one **record** = id + text + metadata; show the **five-row** `records` list from notes — **live-type or paste**; stress **index alignment** (index 2 in every list = same FAQ).
- Live-code **Create the Chroma Client and Collection** block:
  - `PersistentClient`, `get_or_create_collection(name="support_knowledge_base", embedding_function=None)`
  - print name and **`collection.count()`** — expect **0** on first run.
- Point at **`chroma_store`** folder in file explorer / Colab files.
- **Common mistake:** wrong working directory → empty or duplicate store.
- **Cold-call:** "Why is **`embedding_function=None`** in our lab?"

**Bridge sentence:** "Empty shelf confirmed — load **all-MiniLM-L6-v2**, batch-encode five sentences, and **upsert** in one shot."

---

## 8. Add Data — Embed and Upsert (12 minutes)

- Screen-share upsert prose from notes before coding.
- Live-code **Add Data** block:
  - `SentenceTransformer("all-MiniLM-L6-v2")` — narrate download on first run.
  - build `documents`, `ids`, `metadatas` from `records`
  - `model.encode(..., convert_to_numpy=True).tolist()`
  - `collection.upsert(...)`
  - print **`collection.count()`** — must be **5**.
- **Pause the room** until most screens show **5** — troubleshoot stragglers (wrong folder, model still downloading, upsert error).
- Trace **doc2** verbally: refund FAQ text → vector → row in collection.
- **Thumbs-up:** "Thumbs up if your count is **5**."

**Bridge sentence:** "Data is in — never demo search on faith; we **count** and **peek** before any similarity query."

---

## 9. Verify Storage — count, peek, get (7 minutes)

- Run **`count()`** — expect **5**; then **`peek()`** — eyeball ids, text, metadata.
- Live **`get(ids=["doc4"])`** — password FAQ; tie back to get vs query image.
- **Room action (2 min):** learners note one **id** from peek and **category** metadata for doc2.
- If **count ≠ 5:** delete `./chroma_store`, rerun from client creation — demo once if several are stuck.

**Bridge sentence:** "Storage verified — embed the shoe-return question with the **same model** and ask Chroma for **top-3** neighbours."

---

## 10. Retrieve — Query and Top-k Similarity Search (15 minutes)

- Live-code **Retrieve** block:
  - `user_query = "I want to return my shoes and get my money back"`
  - `query_embedding = model.encode([user_query], ...).tolist()`
  - `collection.query(query_embeddings=..., n_results=3)`
  - print Rank 1–3: id, document, metadata, distance if present.
- **Debrief predict activity:** was line **#2** (doc2) rank 1? Why doc1 may also appear high.
- **Common doubt aloud:** why not pass raw string to `query`? — `embedding_function=None`; **you** supply **`query_embeddings`** only.
- **Optional extension (if time):** second query *"How do I change my login password?"* — expect **doc4** first.
- **Circulate** — check `results["documents"][0][i]` indexing; same-model mistakes (second model instance is OK if same name, but reusing **`model`** is cleaner).

**Bridge sentence:** "You retrieved — now we read ranks honestly, including when Rank 1 is mathematically right but business-wrong."

---

## 11. Interpret Results, Wrong Match & Results Check (8 minutes)

- Screen-share **session18-06** top-k results image; table: rank order, documents, metadatas, distances (**lower often = nearer**).
- Say twice: **Rank 1 ≠ always the business-correct answer** — closest vector in the collection.
- Walk **wrong-match example** from notes: *"When will my order reach me?"* — nearest vector ≠ the FAQ you wished you had; fix **chunks**, not the tool; **top-k > 1** helps.
- **Defer** metadata filtering and tuning **k** to **later RAG work** on the track.
- **Results check (3 min):** shoe-return — note Rank 1 **id**, **category**, **distance**; one sentence on **get** vs **query**.
- Skim **What Comes Next** table — chunking, grounded generation, agent track — 60 seconds.

**Bridge sentence:** "Today you built the **retriever half** of RAG — let's lock vocabulary and preview how this collection feeds a generator later."

---

## 12. Key Takeaways, Terminology Sweep & Close (5 minutes)

- Rapid five bullets from **Key Takeaways** — optional repeat-after-me.
- Verbal spotlight: **embedding**, **same model rule**, **upsert**, **query** vs **get**, **top-k**, **Chroma** vs **FAISS**.
- **Exit ticket (verbal):** "What are the three steps from FAQ text to ranked search result?" or "Why must query and store use the same encoder?"
- Homework if needed: optional second query from notes; skim **Important Commands, Libraries, and Terminologies** table.
- Point learners to keep **`vector_search_lab`** — same embed-and-upsert pattern returns when **real documents** are chunked.

**Bridge sentence:** *None — session ends.*

---

## Timing flex — if you are running late

**Cut-first (save ~15–22 min total):**

- Block **12** — one takeaway + exit ticket only (~3 min saved).
- Block **11** — narrate wrong-match example; skip written results check (~3 min saved).
- Block **10** — one query only (shoe-return); skip password extension (~5 min saved).
- Block **9** — `count()` + `peek()` only; skip **`get`** demo (~3 min saved).
- Block **5** — skip pair-share; instructor reads terminology table (~3 min saved).
- Block **3** — show encode preview on projector only; students watch (~4 min saved).

**Sacrifice next if still late:**

- Merge Blocks **2 + 3** into a **12-minute** "embeddings + scores whistle-stop" (images + one encode run).
- Block **4** — instructor states prediction; learners skip notebook write (~2 min saved).
- Block **6** — assume pre-installed packages; imports check only (~3 min saved).
- Blocks **11 + 12** → **5-minute** combined close.

**Never drop:**

- **`PersistentClient`** + **`get_or_create_collection(..., embedding_function=None)`**.
- **`model.encode` → `upsert` → `count()` is 5** before **`query`**.
- **Same embedding model** for all stored chunks and every query.
- **`collection.query`** with **`query_embeddings`** and **`n_results=3`** — at least one live ranked output for the shoe-return question.
- **`get` vs `query`** distinction (exact id vs meaning search).
- One-sentence bridge: today's lab = **retriever** foundation for **full RAG** later (chunking + generator), not a chatbot yet.

**If you are ahead:** extend Block **10** with the password query and distance comparison; or Block **4** debrief with a second user question on the board; or Block **3** live-run encode preview on student machines before the lab.

**If model download fails room-wide:** instructor completes upsert and query once on projector; students copy script and retry download after class — still walk through **predict → verify → query** flow verbally.
