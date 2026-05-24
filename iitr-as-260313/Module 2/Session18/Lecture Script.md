# Lecture Script: Implementing Vector Search Systems

**Session Duration:** 1 hour 50 minutes (110 minutes)  
**Audience:** Absolute beginners — Indian students who may have no formal tech background; completed the **previous session** on vector database concepts (embeddings, similarity search, indexing, ANN at a conceptual level); today is **hands-on Chroma lab only** — learners type code live.

---

**How to use this file**  
Use this script for **timing, room flow, and facilitation only**. It does not replace the detailed explanations, code blocks, diagram URLs, and glossary in `Lecture Notes.md`. Keep lecture notes open on a second screen or tab while you live-code.

---

**Break rule**  
After roughly **60–70 minutes** of instruction (typically after **upsert completes** and learners have verified `count()` is **6**, before the **retrieve / query** block), pause for **one** break of **5–8 minutes**. Do **not** count the break inside the numbered blocks below — resume with the bridge for the next block.

---

## 1. Welcome, agenda, and lab rules (5 minutes)

- Greet the cohort; link to the **previous session**: embeddings, vector DB **store / index / retrieve**, **top-k**, **same embedding model** rule — today you **implement** embed → store → query in **Chroma**, not theory.
- State today’s outcome aloud: *By the end, every learner runs a script that stores six FAQ rows and returns top-3 meaning matches for a plain-English question.*
- Screen-share the **“In this session, you will”** list from lecture notes; emphasise **no metadata filtering lab**, **no collection-update lab** — those come in the **RAG track** starting **next session**.
- **Check for thumbs-up:** “Thumbs up if Python is open — Colab or local VS Code — and you can see today’s lecture notes.”
- Set lab rules: stay in one project folder (`vector_search_lab`); first model download may take 1–2 minutes — don’t panic; raise hand or chat if `count()` is not **6** before querying.

**Bridge sentence:** “You drew the pipeline last time — let’s walk the six lab boxes on screen, then name every Chroma term before anyone installs anything.”

---

## 2. Bridge — pipeline recall and Chroma intro (8 minutes)

- Tell the **shoe-return / refund** e-commerce story from notes — user words ≠ stored FAQ words, meaning still matches.
- Screen-share **session18-01** Chroma lab pipeline image; narrate: Prepare → Embed → Add to Chroma → Verify → Query → Read results.
- State **same model rule** again — centimetres vs inches analogy; non-negotiable for docs **and** queries.
- Show the mermaid / six-box activity from notes; give **90 seconds** for learners to sketch in notebook (or type labels in a comment cell).
- **Cold-call:** “What four things land inside Chroma on **Add** — name all four.” *(id, document, metadata, embedding.)*
- One line on **Chroma**: beginner-friendly vector DB; **`PersistentClient`** keeps data on disk in `./chroma_store`.

**Bridge sentence:** “The pipeline is our north star — next we map Chroma words to **SQL** words you already know, because confusion here breaks every line of code later.”

---

## 3. Chroma terminology, record shape, and methods (15 minutes)

- Screen-share **Chroma vs SQL** table from notes; show **session18-02** concept map image.
- Hit highlights only — don’t read every row: **client** ≈ connection, **collection** ≈ table, **record** ≈ row, **id** ≈ primary key, **document** ≈ text column, **metadata** ≈ extra columns, **embedding** ≈ vector column.
- **Coaching cupboard** analogy for collection + record (30 seconds).
- **Three client types** table — today = **`PersistentClient(path="./chroma_store")`** only; in-memory and HTTP = name-drop.
- Show **session18-03** four-part record image: id, document, metadata, embedding.
- Explain **`embedding_function=None`**: *we* pass vectors on upsert and query — no hidden auto-embed in this lab.
- **What is a method?** — function on an object; `collection.count()` pattern; WhatsApp “Search messages” analogy (1 minute).
- Screen-share methods table + **session18-05** methods image: upsert, count, peek, get, query.
- **add vs upsert** — one sentence each; today we **upsert**.
- **Pair-share (3 min):** Partner A defines **collection** in one sentence; Partner B defines **embedding**; swap — Partner B defines **get**, Partner A defines **query**.
- Optional **terminology match** activity from notes as homework if short on time.

**Bridge sentence:** “Vocabulary locked — open your terminal, install **chromadb** and **sentence-transformers**, and confirm imports before we touch FAQ data.”

---

## 4. Environment setup and project folder (10 minutes)

- Screen-share install commands from notes:
  - `pip install chromadb`
  - `pip install -U sentence-transformers`
- Have learners run **`python --version`** — need 3.10+; mention **venv** if anyone’s environment is messy.
- Live: `mkdir vector_search_lab`, `cd vector_search_lab`.
- Everyone runs in Python:
  - `import chromadb`
  - `from sentence_transformers import SentenceTransformer`
- **Circulate / scan chat:** fix `ModuleNotFoundError` before moving on — common on first pip install in Colab vs local.
- **Thumbs-up check:** “Thumbs up when both imports work with no red error.”

**Bridge sentence:** “Environment green — we’ll paste six FAQ rows, then connect to Chroma and open an empty collection named like a SQL table.”

---

## 5. Prepare sample data and create client + collection (12 minutes)

- Explain one **record** = id + text + metadata; show the six-row `records` list from notes — **live-type or paste**; don’t rush past **index alignment** (position 0 in every list = same FAQ).
- Optional: invite one learner to suggest replacing **one** FAQ sentence for coaching/travel — keep structure.
- Live-code **Create the Chroma Client and Collection** block from notes:
  - imports, `PersistentClient`, `get_or_create_collection(name="support_knowledge_base", embedding_function=None)`
  - print collection name and **`collection.count()`** — expect **0** on first run.
- Point at **`chroma_store`** folder appearing in file explorer / Colab files.
- **Common mistake callout:** wrong working directory → wrong or missing `chroma_store`.
- **Cold-call:** “Why is **`embedding_function=None`** in our lab?”

**Bridge sentence:** “Empty collection confirmed — now load **all-MiniLM-L6-v2**, turn six sentences into vectors, and **upsert** them in one batch.”

---

## 6. Add data — embed and upsert (15 minutes)

- Screen-share **upsert()** prose from notes before coding.
- Live-code **Add Data** block:
  - `SentenceTransformer("all-MiniLM-L6-v2")` — warn first run downloads ~80 MB; narrate “downloading model weights” if spinner shows.
  - build `documents`, `ids`, `metadatas` lists from `records`
  - `model.encode(..., convert_to_numpy=True).tolist()`
  - `collection.upsert(ids=..., documents=..., metadatas=..., embeddings=...)`
  - print **`collection.count()`** — must be **6**.
- **Pause the room** until most screens show **6** — troubleshoot stragglers (wrong folder, upsert error, model still downloading).
- **Trace doc3** verbally: free-shipping text → numbers → row in collection.
- **Thumbs-up:** “Thumbs up if your count is **6**.”

**Bridge sentence:** “Data is in — never demo search on faith; we **count**, **peek**, and **get** by id before any similarity query.”

---

## 7. Verify storage — count, peek, get (10 minutes)

- For each method, read the **heading prose** from notes, then run the snippet:
  - **`count()`** — one number, expect 6
  - **`peek()`** — eyeball ids, documents, metadata
  - **`get(ids=["doc4"])`** — exact row, password FAQ
- Show **session18-04** get vs query image — **`get`** = SQL `WHERE id = ...`; **`query`** = meaning search (coming next).
- **Verification log activity (3 min):** learners fill expected vs actual count, one id from peek, one metadata value, doc1 text from get — chat “pass” or “fail”.
- If **fail:** delete `./chroma_store`, rerun from client creation — demo once if several are stuck.

**Bridge sentence:** “Storage verified — now embed a real user question with the **same model** and let Chroma return **top-3** neighbours.”

---

## 8. Retrieve — query and top-k similarity search (18 minutes)

- Screen-share **query()** prose from notes.
- Live-code **Retrieve** block:
  - user query: *“I want to return my shoes and get my money back”*
  - `query_embedding = model.encode([user_query], ...).tolist()`
  - `collection.query(query_embeddings=..., n_results=3)`
  - print Rank 1–3: id, document, metadata, distance if present
- **Predict-before-run (2 min):** learners write expected top-3 ids in notebook; run; compare — debrief why doc1/doc2 win.
- Live-code **second query**: *“How do I change my login password?”* — expect **doc4** high in ranks.
- **Common doubt aloud:** why not pass raw string to `query`? — because `embedding_function=None`; **you** embed, Chroma searches vectors.
- **Circulate** during second query — check aligned list indexing (`results["documents"][0][i]`).

**Bridge sentence:** “You’ve retrieved — last stretch is reading ranks honestly, including when Rank 1 looks wrong even though the math is ‘correct’.”

---

## 9. Interpret results, wrong match, and RAG bridge (10 minutes)

- Show **session18-06** top-k results image; table: rank order, documents, metadatas, distances (lower often = nearer).
- **Rank 1 ≠ always business-correct** — say it twice.
- Walk **wrong-match example**: *“When will my order reach me?”* — hope doc3/doc5; might get doc6; missing/vague chunks, not “broken Chroma.”
- Explicitly **defer**: metadata `where` filters, upsert updates, tuning **k** → **RAG sessions** (name the four upcoming titles from notes table briefly).
- **Results journal (3 min):** shoe-return ranks + password Rank 1; one sentence: **get(doc4)** vs **query** for password question.
- Read **Key Takeaways** from notes (or paraphrase five bullets).

**Bridge sentence:** “Today you built the **retriever shelf** — **next session** we ask *why* LLMs need retrieved chunks at all; then we stack a **generator** on this same Chroma collection.”

---

## 10. Close and prep for next session (7 minutes)

- Recap chain aloud: **client → collection → upsert → verify → query → interpret**.
- Remind learners to **keep** `vector_search_lab` folder — **RAG Architecture** lab reuses this collection pattern.
- Point to **Important Commands, Libraries, and Terminologies** table for review.
- Parking-lot: 1–2 questions; assign optional **terminology match** / **draw next layer** activities from notes if not done live.
- End on energy: *“You didn’t just understand vectors — you shipped retrieval.”*

**Bridge sentence:** *None — session ends.*

---

## Timing flex (running late — what to trim)

**Cut-first (save ~18–25 min total):**

- Block 3: skip pair-share; instructor reads terminology table only (~3 min saved).
- Block 5: paste full `records` list instead of typing live; skip learner FAQ swap (~4 min saved).
- Block 6: pre-download model before class if possible; skip doc3 trace (~3 min saved).
- Block 7: run only `count()` + `peek()` — skip `get` demo (~4 min saved).
- Block 8: one query only (shoe-return); skip second password query (~5 min saved).
- Block 9: narrate wrong-match example without notebook journal (~3 min saved).
- Block 10: **2-minute** close — one takeaway + next-session tease.

**Sacrifice next if still late:**

- Merge Blocks 2 + 3 into **12-minute** “pipeline + vocabulary whistle-stop” with images only.
- Block 4: assume pre-installed env — imports check only (~5 min saved).
- Block 9 + 10 → **5-minute** combined close.

**Never drop:**

- **`PersistentClient`** + **`get_or_create_collection(..., embedding_function=None)`**.
- **`model.encode` → `upsert` → `count()` is 6** before query.
- **Same embedding model** for documents and every query.
- **`collection.query`** with **`query_embeddings`** and **`n_results=3`** — at least one live demo with ranked output.
- **`get` vs `query`** distinction (exact id vs meaning).
- One-sentence bridge to **next session** RAG track — today’s lab is the retriever foundation.
