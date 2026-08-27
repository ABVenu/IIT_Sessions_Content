# Assignment Question QC Report

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests RAG definition using hospital manual-search scenario. |
| Q2 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests grounded answer when output matches retrieved policy text. |
| Q3 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests why chunking is needed for large manuals. |
| Q4 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests metadata filter purpose with product/status labels. |
| Q5 | Objective MCQ (Moderate) | Correct option: A. Relevancy: Yes. Tests indexing time vs inference time for chunking. |
| Q6 | Objective MCQ (Moderate) | Correct option: A. Relevancy: Yes. Tests semantic chunking trade-off for technical manuals. |
| Q7 | Objective MSQ (Moderate) | Correct options: A, B, C. Relevancy: Yes. Tests common metadata fields; D correctly excluded. |
| Q8 | Objective MSQ (Moderate) | Correct options: A, B, D. Relevancy: Yes. Tests grounding rules; C correctly excluded as ungrounded guesswork. |
| Q9 | Objective MSQ (Hard) | Correct options: A, B, C. Relevancy: Yes. Tests RAG triad components; D correctly excluded. |
| Q10 | Objective MSQ (Hard) | Correct options: A, B, C. Relevancy: Yes. Tests retrieval debugging symptom-fix pairs; D correctly excluded. |
| Subjective | Practical coding (single file) | Medium difficulty: Yes. Clear submission instructions (case c): Yes. Dataset needed: No — `chunks` list and filter tests provided in question. Scope: metadata filters, filter-first retrieval, source citations — all from released notes. Archived laptop policy exclusion verified for Test 1. Expected output verified by running reference logic. |

## Overall QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers RAG recap, grounding, chunking purpose, metadata filters, indexing vs inference, semantic chunking trade-off, RAG triad, debugging, and source tagging. |
| Creativity | 5 | ShopSphere / hospital / technician scenarios; applied grounding checks; offline metadata-first retrieval mirrors class demo without out-of-scope APIs. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: 1 practical task with submission instructions and full answer explanation. |
| No Logical Mistakes | True | All correct options verified against released notes; subjective expected outputs match reference solution logic. |
| No Presentation Mistakes | True | Self-contained questions; no session references; grammar and formatting consistent with Module4 Session48 style. |

## Final Result

QC passed. No modifications required.

**QC iteration:** 1 — passed.
