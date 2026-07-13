# Assignment Question QC Report: Hands-on Logic Building & DSA Problem Solving – II

**Cohort:** iitp-sdai-2606 / Module1 / Session10  
**Aligned to:** `Lecture Notes Released.md`

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Common elements of two roll-number lists. |
| 2 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Inner loop starts at `i + 1` for unique pairs. |
| 3 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Second-last index `size - 2` after ascending sort. |
| 4 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Early return wrong when all even-product pairs are required. |
| 5 | Objective MCQ - Moderate | Correct option: **A**. Relevancy: **Yes**. Early return appropriate for one pair-with-sum answer. |
| 6 | Objective MCQ - Moderate | Correct option: **A**. Relevancy: **Yes**. `sorted()` ~ O(n log n) vs single-pass O(n). |
| 7 | Objective MSQ - Moderate | Correct options: **A, B, D, E**. Relevancy: **Yes**. Problem-analysis checklist; C wrong. |
| 8 | Objective MSQ - Moderate | Correct options: **A, B, C, D**. Relevancy: **Yes**. Even/odd product flag design; E wrong. |
| 9 | Objective MSQ - Hard | Correct options: **A, B, C, E**. Relevancy: **Yes**. O(n²), O(n log n), O(n), `i + 1`; D wrong. |
| 10 | Objective MSQ - Hard | Correct options: **A, B, D**. Relevancy: **Yes**. Pair-with-sum behaviour; C and E wrong. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (single `.py`, LMS box). Dataset needed: **No** (samples given). Tests even-product collect-all nested loops + `sorted()` second largest. Dictionary two-sum / Bubble / Selection Sort not required (surface/out of released scope). |

---

## Overall Assignment QC — Iteration 1

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers common elements, nested index loops, early return vs collect-all, even/odd product ideas, second largest via sorting, complexity, problem analysis. Stays inside released notes. |
| Creativity | 5 | Fest booth ratings, WhatsApp batch rolls, dish-price pairs, debugging scenarios. |
| Structural Adherence | 5 | Objective: 10 Qs (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), Easy → Hard. Subjective: one medium coding task with samples, submission case c, full explanation + code. |
| No Logical Mistakes | True | Sample outputs verified (`[[8, 3], [8, 5]]`, second largest `40` for both sample lists). Correct options match released notes. |
| No Presentation Mistakes | True | No “as taught in the session” phrasing; complete answer explanations; clear expected I/O. |

**Expected result:** All criteria met — **QC passed**. No further modification required.

---

## Scope Guardrails Applied

| Out of released-notes scope | Assignment treatment |
|---|---|
| Bubble Sort / Selection Sort | Not asked |
| Nested string problems | Not asked |
| Dictionary frequency / O(n) two-sum implementation | Not in subjective; not required in objective beyond general complexity contrast already in notes |
| Sort-based duplicate neighbour scan / ordered merge | Not asked |
