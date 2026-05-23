# Lecture Script: Hands-on RAG — LearnBridge Student Playbook Assistant

**Session Duration:** 2 hours  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, example-led, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style.

**Break rule:** After **60–70 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

---

## 1. Welcome, Capstone Frame, and VS Code Setup Check (10 minutes)

- Welcome the group; frame today as a **Module 2 RAG capstone**: embeddings → vector DB → retrieval → grounded generation on one realistic EdTech job — **LearnBridge** student playbook Q&A.
- Read the four outcomes from “What You Will Learn” in Lecture Notes: S3 JSON download, chunk + index, full pipeline, grounded vs LLM-only, mini evaluation.
- **Room action:** Ask everyone to open **VS Code**, create folder `learnbridge_playbook_rag`, open integrated terminal.
- **Engagement — thumbs up:** “Have you created `venv` and run `pip install openai chromadb`?” Circulate (or watch screens) and help with Python extension / interpreter selection (`venv` Python).
- Paste the three **S3 policy URLs** into chat (from Lecture Notes table) for students who will download manually if needed.
- Confirm **`OPENAI_API_KEY`** is set — quick poll: `python -c "import os; print(bool(os.getenv('OPENAI_API_KEY')))"`.

**Bridge sentence:** “Once VS Code and the API key are ready, we’ll see why LearnBridge needs a playbook bot instead of guessing answers from the LLM’s memory.”

---

## 2. LearnBridge Story and RAG Recap Sprint (10 minutes)

- Screen-share the **production RAG workflow** image from Lecture Notes (session30 pipeline overview).
- Narrate LearnBridge: three policies — **attendance**, **assignment**, **evaluation** — students ask repeat questions; bot must use **only** playbook text.
- **Do not** re-teach full Module 2 theory. Hit only: embeddings = meaning fingerprints; Chroma = filing cabinet; retriever vs generator; garbage in, garbage out.
- Show **retriever vs generator** image briefly.
- **Engagement — cold-call:** “If the retriever picks the **assignment** policy for an **attendance** question, who is at fault — the LLM or the retriever?” (Retriever.)
- **Pair-share (2 min):** One sentence: *“Confident wrong answers often start with wrong retrieval.”* One volunteer reads aloud.

**Bridge sentence:** “Story is set — next we pull the real JSON policies from the course S3 bucket onto everyone’s laptop.”

---

## 3. Notes Step 1 — Live Download from S3 (10 minutes)

- **Live-coding:** Walk through `download_policy_files()` and `POLICY_URLS` from Lecture Notes (or run full script’s download section).
- **Room action:** Students run download; confirm `policy_data/` contains three `.json` files. Open `attendance_policy.json` in VS Code — point at `sections` array.
- **Engagement — cold-call:** “What field tells us this file is attendance policy?” (`policy_type`.)
- **Common doubt (30 sec):** Browser can open URL but Python fails — check VPN/firewall; manual save into `policy_data/` is acceptable fallback.

**Bridge sentence:** “Files are on disk — now we turn each JSON section into chunks the vector database can search.”

---

## 4. Notes Step 2 — JSON to Chunks (10 minutes)

- **Live-coding:** `load_policy_chunks_from_json()` — show one chunk dict: `id`, `text`, `metadata`.
- Emphasize: **one section = one chunk** for this masterclass (simple, debuggable).
- **Activity (2 min):** Students print chunk count — expect **15** total. If not 15, a file failed to download.
- **Engagement — thumbs up:** “Does your first chunk id start with `attendance_`?”

**Bridge sentence:** “Chunks are ready — we embed them, store them in Chroma, and never re-download until policies change.”

---

## 5. Notes Step 3 — Index: Embeddings + Chroma (35 minutes)

- **Before this block:** Everyone should have **`learnbridge_rag.py`** from Lecture Notes **Step 3** (full script) saved in their project folder. Steps 1–2 snippets are already inside that file.
- **Live-coding:** Run the **offline indexing** path only: `create_embeddings` → `setup_vector_database()` → `index_policy_chunks()` — narrate `PersistentClient`, `upsert`, cosine space.
- **Room action:** This block is the longest hands-on stretch. Circulate while embeddings API runs; watch for missing API key errors.
- When `chroma_playbook_db/` appears on disk, explain persistence: close VS Code, reopen — data still there.
- **Engagement — cold-call:** “What three things does Chroma store per chunk?” (id, document text, metadata + embedding.)
- If someone’s index is stale from an old run: delete `chroma_playbook_db` and re-index — demo once.

**Bridge sentence:** “Knowledge base is built — every student question from here is runtime: retrieve, then generate.”

---

## 6. Notes Step 4 — Run Grounded Answers (25 minutes)

- **Live-coding:** Run `python learnbridge_rag.py` **or** call `answer_with_rag` for: minimum attendance; late assignment penalty; grade weightage (same questions as in Notes `main()` test list).
- Screen-share **retrieved chunk printout** — students must see policy type and heading before the final answer.
- **Engagement — cold-call:** “Which policy type appeared for the late penalty question?” (`assignment`.)
- Run **hostel curfew** out-of-scope question — expect fallback: *“I don't have that information…”*
- **Activity (3 min):** Students note in a comment whether fallback worked; if LLM invented a hostel rule, prompt rule 2 needs emphasis.

**Bridge sentence:** “Grounded answers work — let’s prove why RAG beats asking the LLM alone.”

---

## 7. Notes Step 5 — Comparison, Top-K, and Mini Evaluation (20 minutes)

- **Live-coding:** `generate_answer_without_retrieval` vs grounded for resubmission at 35% — compare specificity and numbers (matches Notes `main()` comparison block).
- Brief **`top_k_experiment`** — show `k=1` vs `k=3` on approved-leave question; mention precision vs recall trade-off briefly (no separate theory lecture).
- Demo **`policy_type_filter="evaluation"`** on passing marks question.
- Screen-share Notes **Step 5** improvement table and evaluation checklist image.
- **Engagement — pair-share (2 min):** When would you filter by `policy_type` before search? (When student says “final exam” / “certificate”.)
- Walk the **mini evaluation table** from Lecture Notes Step 5 — students fill one row live.

**Bridge sentence:** “You’ve built and tuned a real assistant — we’ll close with what to carry forward.”

---

## 8. Wrap-Up and Key Takeaways (5 minutes)

- Recite three takeaways: retriever first; grounding + fallback; top-k and metadata are tuning knobs.
- Point to Lecture Notes **Quick Reference** table for revision.
- Mention optional stretch: swap JSON loader for PDF loader using same pipeline skeleton.
- **Engagement — exit ticket (chat or verbal):** “Name one failure mode you debugged today.” (Wrong top-k, no API key, stale Chroma, hallucination without fallback, etc.)

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 10+ min late | Shorten Block 2 recap to 5 min; skip pair-share in Block 2 |
| 15+ min late | Skip `top_k_experiment` demo; only show `top_k=3` vs `top_k=1` verbally |
| 20+ min late | Pre-build Chroma index on instructor machine; students only run query half |
| If you are **ahead** | Let students add one custom question; peer-review grounded vs not |

| If you are **ahead** | Add |
|----------------------|-----|
| 5–10 min spare | Students implement a `while True:` input loop for interactive Q&A |
| 15 min spare | Homework preview: log retrieved `section_id` with each answer for audit trail |

**Hard stop at 2 hours:** Ensure everyone has run at least one successful `answer_with_rag` and seen the out-of-scope fallback once.

---

## Lecture Notes Alignment Map

Use this map so script blocks match **Lecture Notes** section headings and code steps.

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 10 min | What You Will Learn + **Step 0** (VS Code setup) | `venv`, `pip install`, `OPENAI_API_KEY` check |
| 2 | 10 min | LearnBridge Problem + **Module 2 RAG Quick Revision** | Pipeline + retriever/generator images; retrieval activity |
| 3 | 10 min | **Step 1** — Download from S3 | `download_policy_files()`, `POLICY_URLS`, `policy_data/` |
| 4 | 10 min | **Step 2** — JSON to chunks | `load_policy_chunks_from_json()`, expect **15** chunks |
| 5 | 35 min | **Step 3** — Full script (offline Phase 1: Steps A–E) | `create_embeddings`, `setup_vector_database`, `index_policy_chunks` |
| 6 | 25 min | **Step 4** — Run the assistant | `python learnbridge_rag.py`, `answer_with_rag`, hostel fallback |
| 7 | 20 min | **Step 5** — Improve retrieval | LLM-only compare, `top_k_experiment`, metadata filter, mini eval table |
| 8 | 5 min | **Key Takeaways** + Quick Reference | Three takeaways; optional PDF stretch |

**Break placement:** After Block 5 or early Block 6 (~60–70 min cumulative).

**Images to screen-share from Notes:**

- `session30-01-rag-pipeline-overview.png` (Block 2)
- `session30-07-retriever-generator-split.png` (Block 2)
- `session31-04-evaluation-four-steps.png` (Block 7)
