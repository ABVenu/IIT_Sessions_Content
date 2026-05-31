# Lecture Script: Introduction to RAG

**Session Duration:** 1 hour 50 minutes (110 minutes)  
**Audience:** Absolute beginners — Indian students who may have no formal tech background; completed **Session 18** (Chroma embed → upsert → **query** with top-k); today is **theory only** — no live coding lab; learners use notebooks, comparison tables, and short paper/diagram activities.

---

**How to use this file**  
Use this script for **timing, room flow, and facilitation only**. It does not replace the detailed explanations, comparison tables, diagram URLs, mermaid flow, and glossary in `Lecture Notes.md`. Keep lecture notes open on a second screen or tab while you facilitate.

---

**Break rule**  
After roughly **60–75 minutes** of instruction (typically after the **RAG flow** and **conceptual pipeline sketch** in Block 5, before the long **ungrounded vs grounded** comparison block), pause for **one** break of **5–8 minutes**. Do **not** count the break inside the numbered blocks below — resume with the bridge for the next block.

---

## 1. Welcome, agenda, and bridge from Session 18 (8 minutes)

- Greet the cohort; link to **last session**: you built the **retriever shelf** — embed FAQ text, **upsert** into Chroma, **query** with **top-k**, read ranked chunks and distances.
- State the shift aloud: *Last time we answered “How do we find the most relevant stored text?” Today: “How do we use that text so an LLM gives trustworthy answers instead of confident guesses?”*
- Screen-share the **“In this session, you will”** list from lecture notes; emphasise **theory only** — diagrams, tables, solo notebook work; **implementation** starts **next session**.
- **Check for thumbs-up:** “Thumbs up if you have lecture notes open and a notebook (physical or digital) ready — we will write in it several times today.”
- Set room norm: when you see **Simple Activity** in notes, you get quiet work time; facilitator **circulates** and spot-checks screens/notebooks.

**Bridge sentence:** “You already know how to **find** similar policy text — let’s meet **ShopKart**, the company whose rule book we will carry through Sessions 20–22.”

---

## 2. ShopKart running example and knowledge base (12 minutes)

- Introduce **ShopKart**: online store; customers ask about **returns**, **shipping**, **warranty**, **refunds**; answers must come from **official policy**, not internet memory.
- Screen-share the four-row **ShopKart Policy Snippets** table from notes — have learners **copy all four rows** into their notebook now (they are today’s “truth”).
- Define **knowledge base** aloud using the three-line pattern from notes (Official / Simple / Real-life — **railway timetable** example).
- Screen-share **session19-01** knowledge-base image; point at four policy areas as the curated **rule book**.
- **Cold-call:** “In one sentence — what is a knowledge base for ShopKart?” *(Curated trusted docs the bot may cite — not whatever the model memorized from training.)*
- **Pair-share (2 min):** Partner A names one policy area; Partner B gives one customer question that should hit that area.

**Bridge sentence:** “ShopKart’s rule book is on your desk — next we ask why a fluent LLM still fails when it never saw that book.”

---

## 3. When LLM knowledge is insufficient (18 minutes)

- One line on what LLMs are **good** at (language, tone, general patterns) vs what they **lack** by default (your private 2026 PDF).
- Screen-share the **three gaps** table — **static knowledge**, **missing domain context**, **hallucination**; give one ShopKart symptom per row (30-day return vs **7 days**, invented lifetime warranty, **24-hour** refund vs **5–7 business days**).
- Screen-share **session19-02** gaps image.
- **Integrated learning point aloud:** *Good English ≠ good knowledge* — separate writing quality from organizational correctness.
- Walk **confidence vs correctness** table; show **session19-03** image — polite tone and specific numbers do not prove eligibility.
- Define **hallucination** and **calibration** using notes’ three-line pattern (**exam date** / **WhatsApp stock tip** analogies — keep brief).
- List what support bots need: **organization-specific**, **current**, **verifiable** — one sentence each.
- **Simple Activity — Spot the Trust Gap (7 min):**
  - Read aloud: *“I opened the Bluetooth speaker and don't like the sound. Can I return it within two weeks?”*
  - Learners draft one fluent LLM-style answer **without** re-reading the policy table (2 min).
  - Then re-read **Returns** row; underline unsupported sentences (3 min).
  - **Circulate**; invite 2 volunteers to read one “sounds helpful but wrong” line.
  - Debrief: opened items + **7 calendar days** — caring tone can still mislead.

**Bridge sentence:** “Fluent guesses hurt customers — policy work needs **grounding**: look up evidence before you explain.”

---

## 4. Why grounding matters for policy questions (10 minutes)

- Define **grounding** (Official / Simple / Real-life — **CA with Form 16**).
- Contrast without grounding = **creative writing**; with grounding = **reading comprehension + explanation**.
- Screen-share **session19-04** “show your work” image: retrieve → evidence in prompt → plain-language reply.
- **Connecting sentence aloud** from notes: embeddings + top-k **find** text; **RAG** means that text **rides into** the LLM prompt.
- **Thumbs-up check:** “Thumbs up if you can finish this: Grounding means the bot ___ before it speaks.” *(Looks up verifiable evidence / shows its work.)*

**Bridge sentence:** “Grounding is the habit — **RAG** is the architecture name for search-first, answer-second.”

---

## 5. RAG as a grounding strategy — flow and pipeline sketch (20 minutes)

- Screen-share retrieval vs generation two-row table — **librarian** + **support agent** analogies.
- Define **RAG** (Official / Simple / **open-book exam**).
- Screen-share mermaid flowchart: **query → retrieve → context → generate**; narrate each box.
- Screen-share **session19-05** image; walk the **refund timing** example step by step from notes (query, retrieve, context, generate).
- Screen-share the **conceptual Python sketch** (not production code) — read line groups aloud:
  - user question
  - `vector_search` / top-k (callback to **Session 18**)
  - prompt with **POLICY EXCERPTS** + **ONLY using** instruction
  - `llm.generate`
- **Common doubt aloud:** *“If retrieval is wrong, will RAG still sound confident?”* — Yes; RAG **reduces** guessing; evaluate retrieval and generation **separately** later.
- **Simple Activity — Paper RAG (8 min):**
  - Question on screen: *“Does express shipping reach my village in Bihar?”*
  - Learners draw four boxes: **Question → Retrieved lines → Prompt idea → Final answer**; copy **Shipping** policy by hand; two-sentence grounded answer.
  - **Circulate**; quick show of hands: “Every fact in your answer appears in retrieved lines?”
  - Debrief: express = **1–2 business days**, **metro cities only** — village may be out of scope; grounded can be stricter than comforting.

**Bridge sentence:** “You paper-walked one RAG loop — now we stress-test **ungrounded** vs **grounded** on four real ShopKart questions.”

---

## 6. Ungrounded vs grounded response quality (22 minutes)

- Frame: same polite tone, different **trustworthiness** when numbers and eligibility matter.
- For each comparison, screen-share the table + speak the **customer question**; spend ~4 minutes per row:

| # | Topic | Customer question (from notes) |
|---|--------|--------------------------------|
| 1 | Return window | Phone case, unopened — how many days? |
| 2 | Shipping | Standard shipping yesterday — arrive tomorrow? |
| 3 | Warranty | Earphones stopped charging at 10 months |
| 4 | Refund | Defective kettle returned — when money back? |

- After comparison 1, screen-share **session19-06** image; for 2–4, tables only (save time if needed).
- Read **student checklist** from notes: Evidence, Specificity, Eligibility, Honesty — one cold-call per bullet across the four examples.
- **Simple Activity — Side-by-Side Scoring (6 min):**
  - Learners copy four tables (or mark in pre-printed handout if you provide one).
  - Mark **Trustworthy for ShopKart? Yes/No** for ungrounded and grounded columns.
  - One sentence: *“Grounding improved trust because ___.”*
  - **Pair-share:** partners compare one sentence; facilitator hears 2–3 aloud.

**Bridge sentence:** “Grounded wins on policy facts — the **retrieve** step is exactly the Chroma pipeline you already coded.”

---

## 7. Relate the retrieve step to vector search (12 minutes)

- State clearly: RAG does **not** replace vector search — it **uses** it.
- Screen-share mapping table: **index building** (offline upsert/count/peek) → **retrieve** (embed + query + top_k) → **generate** (next session).
- Define **retriever** (Official / Simple / **Justdial** listings analogy).
- Screen-share **session19-07** image; repeat **same embedding model** rule for index and queries.
- **Meaning-based search** examples: “money back” → Refund/Returns; Hindi paraphrase → Shipping.
- Screen-share **when retrieval misses** table + **session19-08** image — wrong chunk, empty top-k, evidence ignored; **RAG quality = retrieval × generation discipline**.
- **Simple Activity — Retrieve on Paper (5 min):**
  - Learners label policy area for three customer lines from notes; one keyword sentence they hope appears in the chunk.
  - Quick answer key aloud: (1) Shipping, (2) Warranty, (3) Returns — discuss if anyone picked wrong area and why wording tricked them.

**Bridge sentence:** “ShopKart is one store — the same RAG pattern shows up wherever answers must cite **documents you control**.”

---

## 8. Application patterns and honest limits of RAG (8 minutes)

- Screen-share application patterns table — support bot, document Q&A, education assistant, agentic workflows; one sentence each.
- Screen-share **session19-09** image.
- **Agentic systems** paragraph: agent needs lookup before acting — return ticket when past **7-day** window.
- **Limits** — read four bullets from notes without rushing:
  - reduces hallucination, not zero errors
  - garbage in, garbage out on stale PDFs
  - test retrieval **and** generation
  - operational updates after launch
- **Common doubt aloud:** *“If we have vector search, do we have RAG?”* — Not until chunks feed an LLM with **use-this-evidence** instructions.

**Bridge sentence:** “No magic — next session you wire **retriever + generator** for ShopKart in real Python.”

---

## 9. Bridge to next session, recap, and close (10 minutes)

- Screen-share **Bridge — What You Will Build Next** milestone table: today theory → next minimal RAG loop → later chunking and evaluation.
- Ask cohort to say in unison (or chat): **question → retrieve policy chunks → add context → generate grounded reply**.
- **Simple Activity — One-Minute Elevator (3 min):** learners speak 60 seconds to self or partner using ShopKart + words **retrieve**, **context**, **grounded**, **vector search**; optional 1 volunteer to demo.
- Paraphrase **Key Takeaways** (five bullets from notes).
- Point to **Important Commands, Libraries, Terminologies** table — no new commands today; vocabulary for Session 20 lab.
- Parking lot: 1–2 questions; remind: keep **Session 18** lab folder mindset — next session reuses Chroma as retriever.
- End on energy: *“You can now explain **why** search-first beats memory-only — next class you **build** it.”*

**Bridge sentence:** *None — session ends.*

---

## Timing flex (running late — what to trim)

**Cut-first (save ~18–25 min total):**

- Block 2: skip pair-share; learners only copy policy table (~2 min saved).
- Block 3: shorten Spot the Trust Gap — instructor shows one wrong draft on screen instead of full solo write (~5 min saved).
- Block 5: narrate pipeline sketch without line-by-line Python read; skip Paper RAG or do it as homework (~8 min saved).
- Block 6: cover **two** comparisons (Returns + Refund) instead of four (~8 min saved).
- Block 7: instructor gives retrieve-on-paper answers; learners only do lines 1–2 (~3 min saved).
- Block 9: skip elevator activity; 2-minute close (~5 min saved).

**Sacrifice next if still late:**

- Merge Blocks 4 + 5 into **15-minute** “grounding + RAG flow whistle-stop” with images only.
- Block 8: one-minute limits list — skip application patterns table (~4 min saved).
- Block 6 + 7 → **15-minute** combined “compare two questions + retriever = Chroma” without notebook scoring.

**Never drop:**

- **ShopKart** four-policy reference sheet in learner notebooks.
- **Three LLM knowledge gaps** + **hallucination** in plain language.
- **Grounding** definition and **query → retrieve → context → generate** flow (mermaid or image).
- At least **two** ungrounded vs grounded comparisons with **ShopKart numbers** (7-day return, 5–7 business day refund, or 12-month warranty).
- Explicit link: **retrieve = Session 18 embedding + top-k vector search**; **same model rule**.
- **Limits** one-liner: RAG reduces guessing; wrong/missing retrieval still fails.
- Bridge to **next session** — minimal ShopKart RAG implementation in code.
