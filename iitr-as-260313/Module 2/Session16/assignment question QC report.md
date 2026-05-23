# Assignment question QC report — Session 16

## Per-question QC (Objective) — transcript-aligned (v5)

| Question | Type | Remarks | Transcript / live coverage |
| --- | --- | --- | --- |
| Q1 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** | Cross join / Cartesian product on customers × orders |
| Q2 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** | Table aliases `c`, `o` (replaced column-only alias Q to match live emphasis) |
| Q3 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** | Remote work vs work-from-home keyword failure |
| Q4 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** | Embedding = sequence of numbers / meaning |
| Q5 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** | Conditional join; customer with no orders excluded |
| Q6 | MCQ (Moderate) | Correct: **A**; relevancy: **Yes** | Same embedding model for data and query |
| Q7 | MSQ (Moderate) | Correct: **A, B, C, E**; relevancy: **Yes** | Collect → clean → chunk → embed → compare workflow |
| Q8 | MSQ (Moderate) | Correct: **A, B, C, D**; relevancy: **Yes** | Fixed / paragraph / semantic / recursive chunking named live |
| Q9 | MSQ (Hard) | Correct: **A, B, D**; relevancy: **Yes** | Closer vectors; cosine finds closest; no hand formula; same model |
| Q10 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** | SQL vs semantic; retrieve + LLM answer (RAG-style preview) |

**Removed / revised from v4 objective:** Q2 column `AS fn` only (table aliases taught more prominently); Q9 option on **vector angle** (angle not spoken in transcript—replaced with “cosine finds closest vector”).

## Per-question QC (Subjective) — v5

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Written explanation (Medium) | **One task**, four prompts in one 250–400 word answer: keyword limits, why semantic search, why embeddings, why not synonym-dictionary-only; optional one-line cosine role. **No code**. Submission: **case a**. Scenario: **Agentic Systems Designer** at company—fix legacy SQL + text-match chatbot—applied rationale. |

---

## Structural adherence check

| Rule (from generation prompt) | Status |
| --- | --- |
| Objective count = 10 | Met |
| MCQ 4 Easy + 2 Moderate | Met |
| MSQ 2 Moderate + 2 Hard | Met |
| Progressive Easy → Hard | Met |
| Subjective count = 1 | Met |
| Subjective medium, creative, applied | Met |
| Scope = transcript / live coverage | Met (objective v5 + subjective v5) |
| No session-reference phrasing in stems | Met |
| Answer explanations | Met |

---

## Aggregate QC ratings

| Criterion | Rating (1–5) | Notes |
| --- | ---: | --- |
| Content coverage | 5 | SQL spillover + embeddings, keyword vs semantic, workflow, chunking, cosine (concept), same-model rule, SQL+semantic together. |
| Creativity | 5 | Agentic Systems Designer / company help-bot scenario; concrete mismatch example required. |
| Structural adherence | 5 | Counts, ordering, case-a subjective, facilitator rubric. |
| No logical mistakes | True | All keys checked; Q8 all options true per live chunking segment. |
| No presentation mistakes | True | |

---

## Revision log

- **v1 → v2:** Chunk A keyword-gap wording.
- **v2 → v3:** Three queries + `run_query_*` tasks.
- **v3 → v4:** Precomputed scores (no dot product).
- **v4 → v5:** Subjective → single written explanation (case a); objective aligned to transcript (Q2 table alias, Q3 remote-work example, Q9 no angle formula); full QC rerun.
- **v5 → v5.1:** Subjective scenario → company **Agentic Systems Designer** fixing SQL + text-match chatbot (removed junior-mentoring / “after class” framing).
