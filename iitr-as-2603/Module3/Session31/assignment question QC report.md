# Assignment Question QC Report — Session 31

**Batch:** `iitr-as-2603` · **Session folder:** `Module3/Session31`  
**Source for reuse:** `iitr-as-2601/Module3/Session41` assignments  
**Aligned to:** `Lecture Notes Released.md`  
**Review date:** 2026-07-14

---

## Reuse decision

| Aspect | Verdict |
|---|---|
| **Can we reuse?** | **Yes — with adaptations** (not a blind copy) |
| **Shared core** | Retrieve → augment → generate, top-k, same-model rule, Groq `temperature=0`, informal grounding, refusal when out of context |
| **Must adapt** | Delimiters `#` → `##`; API `invoke` → `get_relevant_documents`; drop ChatGPT/enterprise MSQ (not in this batch’s released notes); drop heavy `persist_directory` emphasis |

### What was changed from the Session41 assignment

| Item | Change |
|---|---|
| Q2 models | MiniLM-vs-mpnet → MiniLM-vs-**gte-large** (matches Tesla encoder story) |
| Q4 / Q9 delimiters | `#context` → `##context` / `##question` |
| Q6 scenario | Apple stock → **leave policy on Tesla corpus** (matches grounding demo) |
| Q6 difficulty | Marked **Moderate** (MCQ mix: 4 Easy + 2 Moderate) |
| Q7 API | `invoke` + persist → **`get_relevant_documents`** + metadata grounding option |
| Q10 | Replaced ChatGPT/enterprise contrast with **k / latency / indexing vs retrieval** |
| Subjective | `##` delimiters, `get_relevant_documents`, no required persist reload |

---

## Iteration 1 — Objective

| Q# | Type | Remarks |
|---|---|---|
| 1 | MCQ Easy | Correct **A** — relevant yes (Retrieve step) |
| 2 | MCQ Easy | Correct **A** — relevant yes (same-model rule) |
| 3 | MCQ Easy | Correct **A** — relevant yes (`temperature=0`) |
| 4 | MCQ Easy | Correct **A** — relevant yes (`##` delimiters) |
| 5 | MCQ Moderate | Correct **A** — relevant yes (raise k when missing second page) |
| 6 | MCQ Moderate | Correct **A** — relevant yes (I don't know / grounded refusal) |
| 7 | MSQ Moderate | Correct **A,B,C,E** — relevant yes; **D** correctly excluded |
| 8 | MSQ Moderate | Correct **A,B,C,E** — relevant yes (informal grounding); **D** correctly excluded |
| 9 | MSQ Hard | Correct **A,B,D** — relevant yes (grounding illusion); **C,E** correctly excluded |
| 10 | MSQ Hard | Correct **A,B,C,E** — relevant yes (k extremes, latency, indexing vs retrieval); **D** correctly excluded |

| Criterion | Rating / Result |
|---|---|
| Content Coverage | **5 / 5** |
| Creativity | **5 / 5** |
| Structural Adherence | **5 / 5** (6 MCQ: 4E+2M; 4 MSQ: 2M+2H; Easy→Hard order) |
| No Logical Mistakes | **True** |
| No Presentation Mistakes | **True** |

**Objective QC:** Passed.

---

## Iteration 1 — Subjective

| Q# | Type | Remarks |
|---|---|---|
| 1 | Subjective / coding | **Medium** difficulty; single-file Lab path; corpus provided; expected grounded vs refusal behaviours clear; submission = case **c** (VS Code → LMS editor). Dataset/corpus embedded in prompt — **yes**. Scope matches retrieve/augment/generate taught in notes. |

| Criterion | Rating / Result |
|---|---|
| Content Coverage | **5 / 5** |
| Creativity | **5 / 5** (FinSight / NovaTech scenario) |
| Structural Adherence | **5 / 5** |
| No Logical Mistakes | **True** |
| No Presentation Mistakes | **True** |

**Subjective QC:** Passed.

---

## Combined QC summary

| Criterion | Objective | Subjective |
|---|---|---|
| Content Coverage | 5 | 5 |
| Creativity | 5 | 5 |
| Structural Adherence | 5 | 5 |
| No Logical Mistakes | True | True |
| No Presentation Mistakes | True | True |

**Expected result:** Met — no further iteration required.

### Out-of-syllabus check

| Potential risk | Status |
|---|---|
| ChatGPT session RAG / Gradio UI | Not asked |
| RAG triad automated judges | Not asked (mentioned only as later work in notes) |
| Image / multimodal implementation | Not asked (surface concept only) |
| MiniLM in subjective | Lightweight encoder for a 4-doc corpus; same-model rule enforced; notes teach `HuggingFaceEmbeddings` pattern (GTE-large on Tesla). Alternative `gte-large` called out in Answer Explanation. |

---

## CSV export QC — `AssignmentCreation.csv`

**File:** `AssignmentCreation.csv`  
**tagRelationships:** `6a55d98be268c63cc3a27834`  
**Review date:** 2026-07-14

### Row-level QC

| Q# | Type | Remarks |
|---|---|---|
| 1 | MCQ Easy | Correct **1** — relevant yes (Retrieve step) |
| 2 | MCQ Easy | Correct **1** — relevant yes (same-model rule / gte-large vs MiniLM) |
| 3 | MCQ Easy | Correct **1** — relevant yes (`temperature=0`) |
| 4 | MCQ Easy | Correct **1** — relevant yes (`##context` / `##question` delimiters) |
| 5 | MCQ Moderate | Correct **1** — relevant yes (raise k) |
| 6 | MCQ Moderate | Correct **1** — relevant yes (grounded refusal) |
| 7 | MSQ Moderate | Correct **1,2,3,5** — relevant yes |
| 8 | MSQ Moderate | Correct **1,2,3,5** — relevant yes |
| 9 | MSQ Hard | Correct **1,2,4** — relevant yes |
| 10 | MSQ Hard | Correct **1,2,3,5** — relevant yes |
| 11 | Subjective | Medium; corpus in prompt; `##` delimiters + `get_relevant_documents`; solution in **answerExplanation** only; submission case **c** |

### CSV structure QC

| Criterion | Rating / Result | Notes |
|---|---|---|
| Content Coverage | **5 / 5** | All 10 objective + 1 subjective rows from assignment markdown |
| Creativity | **5 / 5** | Scenario-based prompts preserved |
| Structural Adherence | **5 / 5** | 6 MCQ + 4 MSQ + 1 subjective; Easy→Hard order; no question-number prefixes in bodies |
| No Logical Mistakes | **True** | mcsc/mcmc answers match source assignments |
| No Presentation Mistakes | **True** | Options without A)/B) labels; markdown preserved; `tagRelationships` on all rows |
| CSV parse check | **True** | Python `csv.DictReader` parsed **11** rows with no errors |

**CSV outcome:** Ready for Assess upload.
