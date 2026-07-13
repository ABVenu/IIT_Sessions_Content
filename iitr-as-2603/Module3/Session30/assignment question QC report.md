# Assignment Question QC Report: RAG — Chunking & Document Preparation

**Cohort:** iitr-as-2603 / Module3 / Session30  
**Aligned to:** `Lecture Notes Released.md`  
**Source check:** Compared with `iitr-as-2601` / Module3 / Session40 assignments

---

## Reuse Decision Summary

| Item | Decision | Reason |
|---|---|---|
| Objective Q1–Q5, Q7–Q8, Q10 | **Reuse** | Concepts present in Session30 released notes (whole-file embedding, overlap, text-only encode, page=0, sliding step, metadata, verify storage, Rank-1 tuning). |
| Objective Q6 | **Replace** | Old Q6 used chat-upload vs chunked RAG; that framing was removed from Session30 released notes. New Q6 tests normal generation vs RAG for proprietary manuals (Siemens-style), which is in the notes. |
| Objective Q9 | **Reuse with fix** | Kept 512/16 logic; removed incorrect “~15% overlap” claim (16/512 ≠ 15%). |
| Subjective | **Reuse** | Matches manual ShopEasy → chunk → MiniLM → `policy_chunks` → query path in released notes. Medium coding, single `.py`, case-c submission. |

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Whole-file one-vector averaging vs chunking. |
| 2 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Overlap as shared margin across chunk boundaries. |
| 3 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Only chunk `text` is embedded; metadata is labels. |
| 4 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Plain `.txt` uses `page = 0`. |
| 5 | Objective MCQ - Moderate | Correct option: **A**. Relevancy: **Yes**. Step = 500 − 75 = 425. |
| 6 | Objective MCQ - Moderate | Correct option: **A**. Relevancy: **Yes**. New item: RAG for proprietary manuals vs normal generation. |
| 7 | Objective MSQ - Moderate | Correct options: **A, B, D**. Relevancy: **Yes**. `source_id`, `page`, `chunk_index`; C/E wrong. |
| 8 | Objective MSQ - Moderate | Correct options: **A, B, C, E**. Relevancy: **Yes**. count/peek/get + list alignment; D wrong. |
| 9 | Objective MSQ - Hard | Correct options: **A, B, C, D**. Relevancy: **Yes**. 512/16 step and overlap rules; E (semantic primary) wrong. |
| 10 | Objective MSQ - Hard | Correct options: **A, B, E**. Relevancy: **Yes**. Tune chunk size/overlap/metadata first; C/D wrong. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (single `.py`, LMS code box). Dataset needed: **No** (corpus provided). Tests chunk helpers, metadata ids, MiniLM upsert, same-model query, Rank 1 `returns_policy.txt`. |

---

## Overall Assignment QC — Iteration 1

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers chunking rationale, size/overlap math, metadata, Chroma persist/verify, normal gen vs RAG, Rank-1 tuning. Subjective covers core manual lab without out-of-scope Tesla/LangChain/Groq. |
| Creativity | 5 | Legal-tech / ShopEasy / hospital manual scenarios; practical sliding-window and debugging MSQs. |
| Structural Adherence | 5 | Objective: 10 Qs (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), Easy → Hard. Subjective: one medium coding task with explanation + full code. |
| No Logical Mistakes | True | Q6 aligned to released notes; Q9 overlap percentage error fixed; answers match notes. |
| No Presentation Mistakes | True | No “as taught in the session” phrasing; complete answer explanations; submission case c. |

**Expected result:** All criteria met — **QC passed**. No further modification required.
