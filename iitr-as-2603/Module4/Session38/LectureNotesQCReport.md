# Lecture Notes QC Report — Hands-On: Agentic RAG

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-08-08  
**Metadata source:** `metadata.md` (iitr-as-2603 Module4 Session38)

---

## Iteration 1

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata topics and subtopics covered: static vs agentic RAG; query rewrite; retrieval as a tool (0+ calls); iterative retrieve → reason → retrieve; stop conditions; one-shot baseline comparison with Q1–Q4 eval table. |
| **Creativity** | **5 / 5** | ShopEasy thread continued; chai-stall catalogue rewrite; sticky-note assistant; IRCTC multi-hop; UPI retry stop; Hindi-mixed rewrite activity; drawer vs careful support agent analogy. |
| **Structural Adherence** | **5 / 5** | Starts with `#` title only; Context of This Session + What you will learn; Official / In Simple Words / Real-Life Example on core terms; full runnable-style scripts with line comments and "How the code works"; student-facing activities (no instructor phrasing); Key Takeaways; terminology table. 482 lines (within 480–500 max). |
| **No Logical Mistakes** | **True** | Pipeline order rewrite → retrieve tool → reason → optional next hop → stop is correct; `MAX_HOPS` + empty-results + enough-evidence stops consistent; allow-list mirrors prior guardrails habit; greeting path uses zero retrieves. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata in notes; paragraphs kept short; activities written for students; markdown tables and fences clean. |
| **No Previous Session Number References** | **True** | Uses **previous** / **next** only — no `Session N` references. |
| **No Metadata/internal reference** | **True** | No leakage of internal instructions (e.g. keep-lite, notes-length labels, session-type dial). |

**Expected Result:** Met — all ratings ≥ 5; all boolean checks True.

**Action:** None required. Proceed to re-verification.

---

## Iteration 2 (re-verification)

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Re-checked against `metadata.md` line-by-line. Five topic bullets and five detailed subtopics each map to dedicated sections (contrast; rewrite; tool; loop; baseline compare). |
| **Creativity** | **5 / 5** | Re-read analogies and activities — cohort-appropriate Plain Indian English; ShopEasy continuity from prior Module 4 notes. |
| **Structural Adherence** | **5 / 5** | Confirmed connecting sentences between static → rewrite → tool → loop → stops → compare; code modules (`static_rag_baseline`, `query_rewrite`, `retrieve_tool`, `agentic_rag`) form a coherent lab path. |
| **No Logical Mistakes** | **True** | Re-traced Q4 multi-hop path and greeting short-circuit; stop-condition table matches loop implementation. |
| **No Presentation Mistakes** | **True** | Re-grep: no session numbers, no metadata leakage, no "Ask students" phrasing. |
| **No Previous Session Number References** | **True** | Verified via search after full read. |
| **No Metadata/internal reference** | **True** | Verified — headings and body are student-facing documentation only. |

**Expected Result:** Met — all ratings ≥ 5; all boolean checks True.

**Post-edit (Static vs Agentic first + Groq API):** Notes now open with an exact difference table; both pipelines call shared `groq_helper.groq_answer`. Line count ~498 (≤500). QC criteria still all 5 / True.

---

## Coverage Checklist (metadata subtopics)
|---|---|
| Contrast static RAG with agentic RAG | What You Already Built — Normal (Static) RAG; Static RAG vs Agentic RAG |
| Rewrite or expand a user query | Query Rewrite — Improve Hit Quality Before Search |
| Retrieval as a tool (zero or more times) | Retrieval as a Tool — The Agent Chooses When to Search |
| Iterative retrieve → reason → retrieve + stop | Iterative loop; Stop Conditions; Build the Agentic RAG Loop |
| Compare vs one-shot baseline | Compare Quality — One-Shot Baseline vs Agentic Loop |
