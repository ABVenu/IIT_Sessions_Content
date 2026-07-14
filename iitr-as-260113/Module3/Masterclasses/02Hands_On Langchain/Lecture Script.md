# Lecture Script: Hands-On LangChain II — UPI Dispute Desk

**Session Duration:** 1 hour 50 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, payments-themed, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style. Lean on `Lecture Notes.md` for definitions, code, and diagrams.

**Break rule:** After **55–65 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

**Prerequisite framing:** If students completed Hands-On I (T20), say today is a **domain port + eval depth** lab. If not, treat the Module 3 map as a fast refresher — still do all three phases.

---

## 1. Welcome, Module Map, and How Today Differs (10 minutes)

- Welcome the group; frame today as **Hands-On LangChain II** — same Module 3 stack, **new product** (UPI dispute desk), **deeper Phase 3**.
- Screen-share the recap table from Lecture Notes (LCEL → tools → AgentExecutor → memory → RAG → integrated agent → eval harness → debug).
- Contrast with Hands-On I: T20 → UPI; light eval → **results log + failure-class patch**.
- **Engagement — cold-call:** "If the architecture is the same, what must change when we switch products?" (Documents, tool names/descriptions, system prompt, eval cases.)
- **Room action:** Confirm Ollama + venv still work (`ollama list`, activate prior venv or create `langchain_hands_on_2`).

**Bridge sentence:** "Map is clear — next we meet the product we will ship in one file: the UPI Payment Dispute Desk."

---

## 2. UPI App Story, Architecture, and Three-Phase Agenda (8 minutes)

- Narrate the domain: **failed UPI debit**, auto reverse, TXN lookup, polite refusal of stock tips. Relatable for every Indian learner.
- Walk the ASCII two-source diagram: FAQ search vs transaction status vs refusal.
- Walk the four-part table: `upi_faq_search_tool`, `get_transaction_status`, `chat_history`, safety.
- Show **one file, three phases**: `demo_lcel_chain()` → build → `run_eval()` + patch menu.
- **Pair-share (2 min):** "In one sentence, why does a payments desk need *two* data sources?" One volunteer reads aloud.

**Bridge sentence:** "Story is set — bootstrap the file before we reason about agents."

---

## 3. Environment Setup and Full File Bootstrap (10 minutes)

- **Live-coding / screen-share:** Setup commands from Lecture Notes (venv, pip packages, model pulls if needed).
- **Room action:** Students create **`upi_dispute_assistant.py`** and paste the **full file**.
- **Engagement — thumbs up:** "Do you see PHASE 1 / 2 / 3 comment headers and `UPI_FAQ_DOCS`?"
- If someone is behind: share file via chat; they catch up during Phase 1.

**Bridge sentence:** "File is on disk — Phase 1 proves LCEL still works in the new domain voice."

---

## 4. Phase 1 — LCEL Warm-Up and Swap-Topic Activity (10 minutes)

- **Live-coding:** Walk `demo_lcel_chain()` — UPI-flavoured system prompt, pipe operator, `invoke`.
- Students run:

```bash
python3 -c "from upi_dispute_assistant import demo_lcel_chain; demo_lcel_chain()"
```

- **Activity (3 min):** Change topic to collect-request fraud; re-run — only input changes.
- **Engagement — cold-call:** "Name the three runnables left to right." (Prompt, LLM, parser.)

**Bridge sentence:** "Warm-up passed — now we ingest the UPI FAQ and expose it as a searchable tool."

---

## 5. Phase 2a–2b — FAQ Corpus and RAG Ingest Path (14 minutes)

- Scroll **`UPI_FAQ_DOCS`** — six inline `Document` objects (auto reverse, pending, dispute SLA, PIN, collect fraud, complaint).
- Trace ingest aloud: splitter → embeddings → Chroma → retriever → `create_retriever_tool`.
- Emphasize **agentic RAG**: retrieval is optional capacity, not always-on.
- **Engagement — cold-call:** "What does `k=2` control?" (Chunks returned per search.)
- Quick topic → question table from Notes.

**Bridge sentence:** "FAQ is indexed — next we add the transaction log and teach arbitration."

---

## 6. Phase 2c — Tool Arbitration and `get_transaction_status` (12 minutes)

- Walk **`TRANSACTIONS`** dict and `@tool` on `get_transaction_status`.
- Routing table: policy → FAQ tool; `TXN-xxx` → status tool; share price → neither.
- Read tool **descriptions** aloud — routing failures start here.
- **Pair-share (2 min):** "Auto reverse window → which tool? TXN-503 → which tool?"
- **Cold-call:** "Why can't the FAQ tool answer TXN-501 alone?" (Static policy ≠ live ops row.)

**Bridge sentence:** "Two tools registered — wire agent, memory, and `ask()`."

---

## 7. Phase 2d — Agent, Memory, and `demo_live_queries()` (14 minutes)

- Walk `_agent_prompt`, `MessagesPlaceholder`, `AgentExecutor` (`verbose`, `max_iterations=4`).
- Contrast **`chat_history`** vs **`agent_scratchpad`**.
- Walk `ask()` append pattern.
- **Live-coding:** Run `demo_live_queries()`; narrate Q1–Q4 and verbose tools.
- **Engagement — thumbs up:** "Did Q2 show `get_transaction_status` in the trace?"

**Bridge sentence:** "App runs — prove routing deliberately, then break memory on purpose."

---

## 8. Tool Routing Table and Break-Memory Activity (12 minutes)

- **Activity — Tool Routing Table (6 min):** Fill four rows from Notes while watching verbose traces.
- **Activity — Break Memory (5 min):** Comment out `chat_history.append` lines; Q3 should forget TXN-501; restore.
- **Cold-call:** "Failure signature name?" (Missing memory.)

**Bridge sentence:** "You have seen live behaviour — Phase 3 turns vibes into a score sheet."

---

## 9. Phase 3 — Eval Results Log and One Patch (12 minutes)

- Walk `EVAL_CASES` — four cases including out-of-domain.
- Explain `chat_history.clear()` between cases.
- Students run `run_eval()`; walk the printed **EVAL RESULTS LOG** (`N/M` summary).
- Show `apply_debug_patch_example()` failure-class menu.
- **Activity — One Patch (5 min):** Change **one** thing; re-run eval; compare summary line.
- **Cold-call:** "Wrong tool on TXN id — fix first?" (Tool description.)

**Bridge sentence:** "Measure → classify → one patch → re-measure — that is professional agent work."

---

## 10. Confidence Checkpoint, Takeaways, and Wrap-Up (8 minutes)

- Rapid-fire five Confidence Checkpoint questions from Notes.
- Recap takeaways: portability, arbitration, results log, one-patch discipline.
- Point to import/package table for revision.
- **Exit ticket:** "Name one thing that stayed the same from T20 (or Module 3) and one thing that changed for UPI."
- Preview: multi-agent / automation stacks ahead — this lab proves single-agent mastery transfers.

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 8–10 min late | Shorten Block 2; skip pair-share |
| 12–15 min late | Paste full file via chat; compress Block 5 to live scroll only |
| 18+ min late | Skip Break-Memory; describe outcome verbally |
| 20+ min late | Instructor demo for `demo_live_queries()`; students run Phase 1 + `run_eval()` only |
| If you are **ahead** | Students add one custom `EVAL_CASES` row and peer-check expected tool |

| If you are **ahead** | Add |
|----------------------|-----|
| 5–8 min spare | Tweak `chunk_size` / `k` and note retrieval change on auto-reverse question |
| 10–15 min spare | Add one new FAQ `Document` and re-ingest (restart process) |

**Hard stop at 1 hour 50 minutes:** Everyone has run Phase 1, seen at least one verbose tool trace, and executed `run_eval()` once with a visible results summary.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 10 min | Module 3 Recap + How this differs | Map; contrast table |
| 2 | 8 min | What You Will Build + Agenda | Architecture ASCII; phases |
| 3 | 10 min | Before You Start + Complete App paste | `upi_dispute_assistant.py` |
| 4 | 10 min | Phase 1 — LCEL Warm-Up | `demo_lcel_chain()`, swap topic |
| 5 | 14 min | Phase 2 — 2a/2b FAQ + ingest | `UPI_FAQ_DOCS`, Chroma, FAQ tool |
| 6 | 12 min | Phase 2 — 2c Transaction tool | `get_transaction_status`, arbitration |
| 7 | 14 min | Phase 2 — 2d Memory + agent | `ask()`, `demo_live_queries()` |
| 8 | 12 min | Activities — Routing + Break Memory | Verbose table; append lines |
| 9 | 12 min | Phase 3 — Eval & debug | `run_eval()`, patch menu, before/after |
| 10 | 8 min | Confidence Checkpoint + Takeaways | Five questions |

**Break placement:** After Block 5 or early Block 6 (~55–65 min cumulative).
