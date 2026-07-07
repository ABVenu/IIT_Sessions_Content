# Assignment Question QC Report: Embeddings & Vector Search

**Cohort:** iitr-as-2603 / Module3 / Session29  
**Aligned to:** `Lecture Notes Released.md`

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests embedding definition through an e-commerce FAQ storage scenario. |
| 2 | Objective MCQ - Easy | Correct option: C. Relevancy: Yes. Tests `all-MiniLM-L6-v2` output size (384 dimensions) from the lab. |
| 3 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests why Chroma does not auto-encode when `embedding_function=None`. |
| 4 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests the same-model rule for stored chunks and queries. |
| 5 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests reading Chroma distance values where lower usually means closer meaning. |
| 6 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests `get()` vs `query()` for exact id lookup vs semantic search. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests manual-embedding Chroma setup: encode, upsert, same model, `query_embeddings`. |
| 8 | Objective MSQ - Moderate | Correct options: A, C, D. Relevancy: Yes. Tests semantic closeness, vector representation, paraphrase matching, and non-interpretable dimensions. |
| 9 | Objective MSQ - Hard | Correct options: A, B, D, E. Relevancy: Yes. Tests SQL exact lookup vs semantic FAQ retrieval, metadata filtering, model-mixing mistake, and vector DB behaviour. |
| 10 | Objective MSQ - Hard | Correct options: A, C, D, E. Relevancy: Yes. Tests UPI missing-FAQ edge case, Rank 1 limits, grounding, and top-k usefulness. |
| 1 | Subjective - Medium Practical Task | **Reused from iitr-as-2601 / Module3 / Session39.** Medium difficulty: Yes. Clear submission instructions: Yes (single `.py` file, LMS code box). Dataset needed: No external dataset; all five FAQ rows provided in question. Tests full Chroma lab: upsert, `count`, `peek`, `get(ids=["doc4"])`, three semantic queries (shoes return, password, UPI), gap analysis for weak Rank 1, and inline comments on same-model rule and `get` vs `query`. Aligns with live session demo and UPI edge-case discussion. |

---

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective covers all released-note concepts. Subjective reused from Session39 matches live Chroma lab, `get` vs `query`, UPI weak-match gap analysis, and same-model rule — all taught in Session29. |
| Creativity | 5 | E-commerce support lead scenario; three-query flow including UPI gap analysis; objective questions use practical helpdesk and SQL-vs-vector settings. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ, 4 MSQ), Easy → Hard. Subjective: one medium coding task with submission instructions, constraints, expected behaviour, and complete answer explanation. |
| No Logical Mistakes | True | Correct answers align with released notes. Subjective uses same paths/collection as lecture notes (`./chroma_store`, `support_knowledge_base`). No out-of-scope PDF chunking or full RAG generation. |
| No Presentation Mistakes | True | Self-contained questions, complete explanations, no unprofessional session references. |

---

## Subjective Reuse Note

| Item | Detail |
|---|---|
| Source | `iitr-as-2601/Module3/Session39/assignment-subjective.md` |
| Target | `iitr-as-2603/Module3/Session29/assignment-subjective.md` |
| Change | Copied as-is — no wording changes required |
| Rationale | Session39 subjective matches Session29 live delivery more closely than the earlier two-query draft (includes UPI query, `get()` demo, gap analysis, lecture-note Chroma paths) |

---

## Final Status

Approved. Subjective assignment updated to Session39 reuse. All required QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.

---

# Assignment CSV QC Report — Embeddings & Vector Search

**File reviewed:** `AssignmentCreation.csv`  
**Review date:** 2026-07-07  
**tagRelationships:** `6a4c9f286d6e3a5537a8edac`

---

## CSV Structure QC

| Check | Result |
|---|---|
| Total data rows | 11 (6 MCSC + 4 MCMC + 1 subjective) |
| Header columns | 20 — matches template |
| CSV parsing | Pass — all rows parse to 20 columns |
| tagRelationships on all rows | Pass — `6a4c9f286d6e3a5537a8edac` |
| Answer explanations on all rows | Pass |
| Subjective solution in answerExplanation only | Pass — `subjectiveAnswer` column empty |
| Question bodies start with content (no Q numbers in body) | Pass |
| Options without A)/B) prefixes | Pass |
| Markdown preserved in contentBody and answerExplanation | Pass |

---

## Per-Row CSV QC

| Row | Type | mcsc/mcmc Answer | Correct option relevancy | Remarks |
|---|---|---|---|---|
| 1 | mcsc | 2 | Yes | Embedding definition |
| 2 | mcsc | 3 | Yes | 384-dim vector length |
| 3 | mcsc | 2 | Yes | `embedding_function=None` manual encode |
| 4 | mcsc | 2 | Yes | Same-model rule |
| 5 | mcsc | 2 | Yes | Distance 1.17 = closest |
| 6 | mcsc | 2 | Yes | `get()` for exact id |
| 7 | mcmc | 1,2,3,5 | Yes | Chroma setup steps |
| 8 | mcmc | 1,3,4 | Yes | Semantic similarity properties |
| 9 | mcmc | 1,2,4,5 | Yes | SQL vs vector search |
| 10 | mcmc | 1,3,4,5 | Yes | UPI edge case + grounding |
| 11 | subjective | — | Yes | Session39 `support_vector_search.py` lab; complete code in answerExplanation |

---

## Overall CSV QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | All 10 objective + 1 subjective questions exported from assignment markdown files |
| Creativity | 5 | Scenario-based questions preserved in CSV format |
| Structural Adherence | 5 | Matches AssignmentCreationTemplate.csv column structure |
| No Logical Mistakes | True | mcsc/mcmc indices align with option order; difficulty levels mapped (Easy=0, Moderate=0.5, Hard=1, Subjective=0.5) |
| No Presentation Mistakes | True | No parsing errors; code indentation preserved in subjective answerExplanation |

**Outcome:** CSV QC passed — `AssignmentCreation.csv` ready for Assess upload.
