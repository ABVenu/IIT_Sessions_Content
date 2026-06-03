# Assignment Question QC Report: RAG — Chunking & Document Preparation

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests whole-file embedding vs chunked retrieval for multi-topic policies. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests purpose of chunk overlap at boundaries. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests that only chunk text is embedded, not metadata. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `page: 0` for plain `.txt` corpus records. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests sliding-window step `500 - 75 = 425`. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests chat whole-file upload vs chunked persistent RAG. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests `source_id`, `page`, and `chunk_index` roles. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests post-upsert verification and aligned upsert lists. |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, D. Relevancy: Yes. Tests 512/16 step math, overlap rules, and Strategy 1 on large docs. |
| 10 | Objective MSQ - Hard | Correct options: A, B, E. Relevancy: Yes. Tests tuning chunk size/overlap before blaming the vector DB; rejects bad overlap and mixed models. |
| 1 | Subjective - Easy–Medium Practical Task | Easier scope: Yes (2 policies, starter chunk code provided, 1 query, no peek/get/interpretation block). Clear submission instructions (case c): Yes. Dataset needed: No external download. Tests chunk → upsert → single semantic query with `source_id` on Rank 1. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective covers full session concepts; subjective focuses on core chunk + upsert + one traced query (appropriate for easier scope). |
| Creativity | 5 | ShopEasy scenario retained; subjective simplified to two-policy demo with one return-window question. |
| Structural Adherence | 5 | Objective: 6 MCQs + 4 MSQs, ordered Easy → Hard. Subjective: one easy–medium single-file task with case-c submission and full answer explanation. |
| No Logical Mistakes | True | Math and overlap rules match released notes; subjective Rank 1 expects `returns_policy.txt`. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations; grammar checked. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
