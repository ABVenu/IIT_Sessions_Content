# Lecture Script: RAG Architecture and Pipeline

**Session Duration:** 1 hour 50 minutes (110 minutes)  
**Audience:** Absolute beginners — Indian students who may have no formal tech background; completed **Session 19** (why RAG / grounding for ShopKart) and **Session 18** (Chroma embed → upsert → query); today is **hands-on** — one Python script wires **knowledge sources + retriever + generator** into a minimal RAG loop.

---

**How to use this file**  
Use this script for **timing, room flow, and facilitation only**. It does not replace the detailed explanations, code blocks, diagram URLs, and glossary in `Lecture Notes.md`. Keep lecture notes open on a second screen or tab while you live-code.

---

**Break rule**  
After roughly **60–70 minutes** of instruction (typically after **`Indexed 4 ShopKart policy records`** and learners have verified **`collection.count()` is 4**, before the **retriever / `retrieve_policy_chunks`** block), pause for **one** break of **5–8 minutes**. Do **not** count the break inside the numbered blocks below — resume with the bridge for the next block.

---

## 1. Welcome, agenda, and bridge from Session 19 (6 minutes)

- Greet the cohort; link to **last session**: ungrounded vs grounded, *search first — answer second*, retrieve = your Chroma top-k pipeline — today you **implement** the full loop in code.
- State today’s outcome aloud: *By the end, every learner runs `shopkart_rag.py` that retrieves ShopKart policy chunks and generates answers grounded in those excerpts — then compares the same questions to an LLM-only baseline.*
- Screen-share the **“In this session, you will”** list from lecture notes; emphasise **one complete script**, **four policy chunks**, **`top_k=2`** — metadata filtering and advanced tuning deferred to **Session 22**.
- **Check for thumbs-up:** “Thumbs up if Python is open and you still remember what **`collection.query`** does from the vector search lab.”
- Set lab rules: work only inside **`shopkart_rag_lab`**; **`OPENAI_API_KEY`** in the terminal — never paste keys into the `.py` file or Git.

**Bridge sentence:** “Theory told us *why* — let’s frame ShopKart support as a RAG problem: who uses the bot, what documents it may cite, and which policy shelf each question should hit first.”

---

## 2. ShopKart framing — stakeholders, knowledge boundary, policy map (10 minutes)

- Screen-share **session20-01** knowledge-boundary image; narrate stakeholders table (customer, support team, business).
- One line each: **knowledge boundary** = company rule book only; **bank brochure** analogy from notes.
- Screen-share the four-row **policy table** + **session20-02** policy-chunks image — each row → one Chroma chunk in **`shopkart_policy_kb`**.
- **Integrated learning point aloud:** return questions may need **Returns + Refunds**, not **Warranty** alone — retriever finds the shelf before the writer speaks.
- **Pair-share (3 min):** Partner A answers Q1 (*opened earphones — send back?*); Partner B answers Q4 (*COD refund to UPI?*) — name primary policy area + one-sentence *why* (use the four lines in notes activity).
- **Cold-call:** “For express delivery to Delhi — which policy area is the best **starting** search target?” *(Shipping.)*

**Bridge sentence:** “ShopKart’s rule book is clear — before we open the editor, name the three roles every RAG pipeline splits into: sources, retriever, generator.”

---

## 3. Three components of a minimal RAG pipeline (8 minutes)

- Screen-share mermaid flowchart from notes (customer question → retriever → context → generator → grounded answer).
- Walk the three-row table: **knowledge sources** = `POLICY_RECORDS` → Chroma; **retriever** = Sentence Transformers + **`collection.query`**; **generator** = OpenAI chat API.
- **Library assistant** + **support executive** analogies — 30 seconds each.
- Screen-share **session20-03** three-components image.
- **Common doubt aloud:** *“Is vector search alone RAG?”* — No until generation runs with **use-this-evidence** rules.
- **Thumbs-up check:** “Thumbs up if you can say in one sentence what the **generator** does that **`query()`** alone does not.”

**Bridge sentence:** “Roles mapped — create **`shopkart_rag_lab`**, install three libraries, and set your API key before we paste policy records.”

---

## 4. Project setup — installs, API key, environment checklist (10 minutes)

- Screen-share install block from notes:
  - `mkdir shopkart_rag_lab` → `cd shopkart_rag_lab`
  - `pip install chromadb sentence-transformers openai`
- Explain split: **retriever local**, **generator hosted** — show **session20-04** lab-stack image.
- Demo **`export OPENAI_API_KEY="..."`** (Mac/Linux) or PowerShell variant; stress **environment variable**, not hard-coded string.
- Everyone runs import check from notes activity:
  - `import chromadb`
  - `from sentence_transformers import SentenceTransformer`
  - `from openai import OpenAI`
- **Circulate / scan chat:** fix pip errors before policy code.
- **Thumbs-up:** “Thumbs up when all three imports succeed in the same terminal you will use to run the script.”

**Bridge sentence:** “Environment green — we’ll define four **`POLICY_RECORDS`** dicts: id, text, metadata — the knowledge base every retrieval search will see.”

---

## 5. Step 1 — Define knowledge sources as `POLICY_RECORDS` (10 minutes)

- Explain **one main idea per chunk**; four areas = four rows — enough for a **minimal** pipeline.
- Live-type or paste the opening of **`shopkart_rag.py`**: imports, **`POLICY_RECORDS`** list, **`EMBEDDING_MODEL_NAME`**, **`GENERATION_MODEL_NAME`** from notes (don’t run yet).
- Point at each row: **`id`**, **`text`**, **`metadata`** (`category`, `source`).
- **Cold-call:** “Why must **`shopkart_returns_1`** id stay unique?” *(upsert primary key / safe updates.)*
- **Same model rule** callback: **`all-MiniLM-L6-v2`** for index **and** every query.
- Optional **trace one record** (30 sec): verbal walkthrough **`shopkart_refunds_1`** — text, category, sample customer question.
- **Common mistake callout:** wrong policy text in this list → “grounded” but **wrong** answers with extra confidence.

**Bridge sentence:** “Policy rows are defined — next we reconnect to Chroma, open **`shopkart_policy_kb`**, embed all four texts, and upsert in one batch.”

---

## 6. Step 2 — Connect to Chroma and index policy chunks (13 minutes)

- Screen-share **session20-05** index-Chroma image before coding.
- Live-code from notes:
  - **`create_embedding_model()`**
  - **`setup_chroma_collection()`** — `PersistentClient("./chroma_store")`, **`get_or_create_collection(name="shopkart_policy_kb", embedding_function=None)`**
  - **`index_policy_records()`** — parallel lists, **`model.encode`**, **`collection.upsert`**
  - print **`Indexed {collection.count()} ShopKart policy records.`** — must be **4**
- Show **`chroma_store`** folder; **`embedding_function=None`** = same teaching pattern as Session 18.
- **Pause the room** until most screens show **4** — troubleshoot wrong working directory / first model download.
- Quick **verify activity (2 min):** learners add temporary **`count()`** + **`peek()`** lines; chat one **`id`** and one **`category`** they see.
- **Thumbs-up:** “Thumbs up if count is **4** and all four policy areas appear in peek.”

**Bridge sentence:** “Knowledge is indexed offline — now wrap **`collection.query`** in a named retriever that returns ranked evidence for any customer question.”

---

## 7. Step 3 — Build the retriever (13 minutes)

- Define **retriever** in one sentence; **top-k** = bring the **k** best-matching paragraphs by meaning — **session20-06** image.
- Live-code **`retrieve_policy_chunks`**: encode query → **`collection.query`** with **`n_results=top_k`**, loop zip documents / metadatas / distances into clean dicts.
- Stress: retriever **never** calls the LLM — only returns evidence.
- **Predict-before-run (2 min):** question from notes — *“I want my money back after returning a COD order.”* — learners write expected **`category`** for Rank 1; run retriever only; debrief refunds vs returns.
- **Circulate** during run — check **`results["documents"][0]`** indexing.
- **Cold-call:** “What does a **lower** distance usually mean in our lab?” *(closer vector / nearer meaning — not a guarantee of business correctness.)*

**Bridge sentence:** “You have ranked excerpts on screen — now stitch them into a grounded prompt and hand that to the generator.”

---

## 8. Step 4 — Grounded prompt and generator (12 minutes)

- Screen-share **session20-07** grounded-generator image.
- Live-code **`build_grounded_prompt`**: numbered excerpts, rules 1–4 (especially rule 2 — admit insufficient info).
- Live-code **`generate_grounded_answer`**: **`client.chat.completions.create`**, system + user messages, return stripped content.
- Narrate **context injection** — retrieved chunks = evidence block from Session 19 diagrams.
- Run **one** grounded answer live for the COD refund question; screen-share printed excerpts + final reply side by side.
- **Evidence audit (2 min):** learners underline numbers in the answer — each must trace to an excerpt; circle any orphan line.
- **Common doubt:** LLM can ignore excerpts — today we **inspect**; evaluation discipline comes later.

**Bridge sentence:** “Grounded path works — run the **same** model on the **same** question with **zero** policy text and watch generic guessing appear.”

---

## 9. Step 5 — LLM-only baseline (6 minutes)

- Live-code **`generate_llm_only_answer`** — generic system prompt, user message = raw question only.
- Screen-share **session20-08** LLM-only vs RAG image; run baseline for COD kettle / refund question from notes table.
- Read one contrast aloud: *“Usually 3–5 days”* vs *“5–7 business days after warehouse verification; COD to UPI.”*
- **Thumbs-up check:** “Thumbs up if you see the baseline sounds polite but misses ShopKart’s exact numbers.”

**Bridge sentence:** “Contrast proven — wire **`answer_with_rag`**, print retrieval ranks for every demo question, and run **`main()`** end to end.”

---

## 10. Steps 6–7 — Full RAG loop, `main()`, and demo queries (14 minutes)

- Screen-share **session20-09** answer-with-rag-loop image.
- Live-code **`print_retrieved_chunks`** and **`answer_with_rag`** — order: retrieve → inspect → generate; swapping order breaks grounding.
- Paste **`main()`** block: **`OpenAI()`**, model, collection, **`index_policy_records`**, **`demo_queries`** loop — LLM-only print first, then RAG block per question.
- **How to run** from notes: `cd shopkart_rag_lab`, export key, `python shopkart_rag.py`.
- **Circulate** while script runs — expect four question cycles with ranks + grounded answers.
- **Baseline vs RAG scorecard (3 min):** for at least **two** demo queries, learners fill LLM-only claim vs RAG claim vs *matches ShopKart policy?* — one sentence why RAG won.
- If API rate limits hit: instructor runs full demo on screen; learners complete scorecard from shared output.

**Bridge sentence:** “Pipeline runs — last pass: did retrieval hit the right policy **intent**, and did generation stay inside the excerpts?”

---

## 11. Validation, end-to-end picture, and close (8 minutes)

- Screen-share retrieval checklist table from notes (unopened return → Returns; COD UPI → Refunds; etc.).
- **Semantic retrieval** one-liner — intent match, not keyword copy-paste.
- Screen-share **session20-10** end-to-end pipeline image; six-step breath from notes (offline index → online retrieve → ground → generate → inspect).
- **Two-stage debug** prompt: if an answer felt wrong — retrieval stage or generation stage? (one sentence in notebook).
- Read **Key Takeaways** (five bullets) or paraphrase; point to terminology table for review.
- Parking-lot: 1–2 questions; remind **`top_k` tuning / metadata filtering** → **Session 22**; real PDF ingestion → later sessions.
- End on energy: *“You didn’t just search policies — you shipped retrieve → generate and proved grounding beats guessing.”*

**Bridge sentence:** *None — session ends.*

---

## Timing flex (running late — what to trim)

**Cut-first (save ~20–28 min total):**

- Block 2: instructor reads policy map answers; skip pair-share (~3 min saved).
- Block 3: show image only; skip mermaid live draw (~2 min saved).
- Block 4: assume pre-installed packages; imports-only check (~4 min saved).
- Block 5: paste full `POLICY_RECORDS`; skip trace-one-record (~2 min saved).
- Block 6: skip peek activity; count-only verify (~3 min saved).
- Block 7: one retrieval demo only; skip predict-before-run (~4 min saved).
- Block 8: paste generator functions; one live answer only; skip evidence audit (~4 min saved).
- Block 9: narrate baseline contrast from instructor output; learners don’t run baseline locally (~3 min saved).
- Block 10: run **`main()`** for **two** demo queries instead of four (~5 min saved).
- Block 11: **3-minute** close — one takeaway + Session 22 tease.

**Sacrifice next if still late:**

- Merge Blocks 2 + 3 into **12-minute** “ShopKart + three components whistle-stop.”
- Blocks 8 + 9 → **12-minute** “generator + baseline on one question only.”
- Block 11 folded into Block 10 close.

**Never drop:**

- **`POLICY_RECORDS`** with four policy areas and unique ids.
- **`shopkart_policy_kb`** + **`embedding_function=None`** + **`count()` is 4** after upsert.
- **`retrieve_policy_chunks`** with **same embedding model** for index and query.
- **`build_grounded_prompt`** with **use-only-excerpts** rules.
- Side-by-side **LLM-only vs RAG** on at least **one** representative refund or return question.
- **`answer_with_rag`** order: **retrieve → print ranks → generate**.
- **`print_retrieved_chunks`** so learners judge retrieval **intent** before trusting the final reply.
- Explicit bridge: today completes minimal RAG; **Session 22** deepens retrieval tuning.
