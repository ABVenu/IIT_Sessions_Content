# Lecture Script: RAG Foundations

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian learners who may have no formal tech background; they should already have **Ollama** working from the previous session. Today is **concepts + one manual demo + embeddings lab** — not a full coded RAG app.

---

**How to use this document**  
This file is **for timing and facilitation only**. It does not replace `Lecture Notes.md`; it tells you *what to do in the room*, when to circulate, and how to bridge topics. Keep definitions and code on the notes / projector from the notes file.

**Break rule**  
After **approximately 62–72 minutes from session start**, take **one pause of 5–8 minutes**. Do **not** count the break as a numbered block; resume with the embeddings hands-on block.

---

## 1. Opening, Recap Bridge & Today's Map (8 minutes)

- Screen-share opening of Lecture Notes.md — **60-second** recap: last time **Ollama**, local/cloud Python, **embeddings preview** (text → numbers).
- State clearly today: **big picture of RAG** — giving AI a **library**; **no full RAG application in code** today; **embeddings demo at the end**.
- Read outcome bullets; **thumbs up** if anyone is unsure what an embedding is (promise replay in Block 8).
- Show five-step mermaid or table preview — "This is the map; we walk it slowly."
- **Cold-call:** "In one phrase, what did we use Ollama for last class?"

**Bridge sentence:** "Prompt engineering taught you how to ask; today we learn how to **feed the right pages** before the model answers."

---

## 2. Why LLMs Alone Are Not Enough (9 minutes)

- Three-problem table on screen — knowledge cutoff, no private data, hallucination; use **2026 refund rule** example from notes.
- **Common doubt** aloud: "Can't ChatGPT know our company?" — patterns vs your Google Doc.
- One line: prompt engineering = *how you talk*; RAG = *what pages you attach*.
- **Pair-share 20 seconds:** name one question at your college/job that must **not** be guessed.

**Bridge sentence:** "When guessing is dangerous, teams use **RAG** — search first, then speak."

---

## 3. What Is RAG? — Library Metaphor (10 minutes)

- Definition in plain language: external knowledge base → retrieve → prompt → generate.
- Walk library table: documents, catalog/embeddings, librarian, context, generator.
- DU photocopy shop story — keeper pulls folder, you read, you explain.
- Agent stakes one sentence: wrong policy → wrong **action** (refund email, ticket update).
- Optional: draw five boxes on whiteboard if no slide deck.

**Bridge sentence:** "Every tool — LangChain, custom Python, enterprise — tells the same five-step story; let's name those steps once."

---

## 4. The Five-Step RAG Flow — Concept Only (14 minutes)

- Teach **Ingest → Prepare → Retrieve → Augment → Generate** with the "we do it today?" column from notes.
- Screen-share mermaid `flowchart LR` (documents → prepare → vector DB → chunks → LLM).
- Emphasize: today = **Prepare** piece via embeddings only; **Retrieve/Augment** automated in **upcoming sessions**.
- **Common doubt:** "Why not paste the whole PDF?" — context limit; retrieval picks relevant slices later.
- **Check for thumbs:** "Who can name step 3 in one word?" (retrieve / search)

**Bridge sentence:** "Two roles do the work inside that pipeline — finder and writer — plus a rule called **grounding**."

---

## 5. Retriever, Generator, Grounding & Fine-Tuning Flash (11 minutes)

- Retriever = finds notes; generator = LLM writes; grounding = stick to open-book context.
- Railway platform board analogy — read the board vs guess platform 5.
- Read aloud the **one prompt rule** students should memorize (answer only from Context; say not found if missing).
- Glance at "if something goes wrong" table — **do not workshop** failures today; point to **future sessions** for chunking and top-k.
- **Fine-tuning flash (~2 min):** memorize book vs bring book each exam; table "changing PDFs → start with RAG" — optional reading only.

**Bridge sentence:** "Before we automate the librarian, you'll **be** the librarian — paste the page yourself and feel the difference."

---

## 6. Without Context vs With Context — Manual Demo & Activity (20 minutes)

**Instructor demo (~8 min)**  
- Standardize handbook sentence on slide (March 2026 late submission / 48 hours / 10% per day).
- **Step 1:** Ollama CLI or prior `ask_ollama` script — question **only**; read one invented/generic line aloud.
- **Step 2:** Same question with Context block from notes — highlight **48 hours** and **10%** in the answer.
- Table on screen: guess vs your document; "RAG automates **finding** the paragraph."

**Student activity — Two-Question Compare (~10–12 min)**  
- Everyone runs Step 1 and Step 2 on own machine (same model as last class).
- One sentence written in notebook: what changed?
- Optional fast track: question **not** in handbook — did model refuse?
- **Circulate** — help with prompt formatting; common bug: Context header missing.
- **Cold-call** two learners: read one sentence from Step 2 answer.

> **Break placement:** Target break **immediately after Block 6** (~65–70 min). If Block 6 ends early, stretch with optional out-of-handbook question demos until break window. If **behind** before Block 6, shorten pair discussion — do not skip both steps on projector.

---

**Break:** 5–8 minutes. Remind students: Ollama must stay running; `nomic-embed-text` should be pulled before Block 7.

---

## 7. Embeddings — Teach & Instructor Live Run (12 minutes)

- Bridge from break: "This morning you pasted text manually; embeddings are how machines **sort sentences by meaning**."
- Show embeddings meaning-space image from notes (`session37-08-embeddings-meaning-space.png` — same diagram as prior preview).
- GPS / library topic-sort analogies — 30 seconds each.
- On projector: `ollama pull nomic-embed-text` if not already pulled (or confirm homework).
- Open `text_to_embeddings_demo.py` — scroll slowly through **three sentences** and `text_to_vector`.
- **Live run** `python text_to_embeddings_demo.py` — point at **vector length** and **first five numbers** for all three lines.
- Read closing print lines: refund/return **closer** than exam sentence; **upcoming sessions** → vector DB + search.

**Bridge sentence:** "You've made numbers from text; next we run it on every laptop, then I'll show where those numbers live in the full course story."

---

## 8. Student Activity — Embedding Walkthrough (18 minutes)

- Post activity from notes on slide.
- **Room action:** students run script; verify **same vector length** for all three sentences.
- Task: change `sentence_exam` to another refund-related line; re-run once.
- **Circulate** — embed model not found, Ollama not running, typo in filename.
- **Pair-share:** answer in one sentence — *"What would a RAG system do after storing these numbers?"*
- **Cold-call** three pairs — listen for **store → search → paste → generate** (words need not be exact).

**Bridge sentence:** "Today stops at creating vectors; the course completes the loop in two upcoming chapters — vector database, then full RAG app."

---

## 9. From Embeddings to Full RAG — Closing Arc (11 minutes)

- **Step A** on screen: chunks → embeddings → **vector database** (Chroma/FAISS names only); filing cabinet for meaning.
- **Step B:** question embedded → DB returns chunks → prompt → Ollama answer — link back to **manual paste** demo in Block 6.
- Walk mermaid `flowchart TB` (This session → Next sessions → Later) — narrate without rushing code.
- Instructor closing story (three numbered lines from notes): today = text→numbers; next = DB+search; after = automated grounded answer.
- Explicitly say: **full coded RAG pipeline** is **not** today's homework focus.

**Bridge sentence:** "Let's lock the vocabulary and send you off knowing exactly what we're building next."

---

## 10. Key Takeaways, Terminology Sweep & Close (7 minutes)

- Rapid five bullets from Key Takeaways section — learner repeat-after-me optional.
- Verbal glossary spotlight: **RAG**, **grounding**, **embedding**, **vector database**, five pipeline verbs.
- **Exit ticket (verbal):** "Name the five RAG steps in order" or "What does the retriever do?"
- Homework if needed: finish embedding activity; ensure `nomic-embed-text` pulled; skim fine-tuning table only if curious.
- Preview titles only — **Embeddings & Vector Search**, then **Building a RAG App** — no numbered session labels unless your LMS requires them.

---

## Timing flex — if you are behind schedule

Cut in this **order**:

1. Block **10** — glossary becomes "read in notes"; exit ticket only.
2. Block **5** — drop fine-tuning flash entirely.
3. Block **8** — instructor runs script once; students watch, one volunteer re-runs.
4. Block **9** — narrate closing arc without mermaid; 3 bullet slides only.
5. Block **2** — pair-share → instructor gives one example.

**Protect these (do not cut):** Block **6** both steps on projector; Block **7–8** at least one successful `embed` output per student if possible.

If you are **ahead**, extend Block **6** with third prompt (out-of-handbook); or Block **8** discussion on similarity intuition before next topic.

If **Ollama fails room-wide**, fall back to instructor-only embed output screenshot + students copy prompt for manual demo from Block 6 into personal notes.
