# Assignment Question QC Report — Session 22: Evaluating and Improving RAG Systems

## Per-Question QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Easy) | Correct option **A** (Retrieval problem) — relevant: wrong policy chunk surfaced for returns question. Distractors map to other failure modes or unrelated issues. |
| Q2 | MCQ (Easy) | Correct option **B** (Rank 1 inspection first) — relevant: matches separate-stage evaluation workflow. |
| Q3 | MCQ (Easy) | Correct option **C** (Hallucination) — relevant: invented prepaid UPI workflow not in excerpts. |
| Q4 | MCQ (Easy) | Correct option **A** (Diagnose first) — relevant: iterative evaluation / targeted fixes principle. |
| Q5 | MCQ (Moderate) | Correct option **B** (Raise top-k / chunking) — relevant: incomplete retrieval within correct category. |
| Q6 | MCQ (Moderate) | Correct option **B** (Full-index fallback) — relevant: `guess_category` returns `None` behaviour. |
| Q7 | MSQ (Moderate) | Correct options **A, B, D** — relevant: retrieval failure symptoms; C correctly excluded as generation. |
| Q8 | MSQ (Moderate) | Correct options **A, B, C** — relevant: improved-run configuration; D is baseline only. |
| Q9 | MSQ (Hard) | Correct options **A, B, C** — relevant: symptom-to-lever pairing; D correctly excluded. |
| Q10 | MSQ (Hard) | Correct options **A, B, C** — relevant: metadata filter behaviour and limitations; D correctly excluded. |
| Subjective Q1 | Practical (Medium, simplified) | Two-query improved run only (no baseline pass); `guess_category` + `retrieve_filtered` provided to paste; student writes strict prompt. Submission: case c (single `.py` in LMS). Assumes prior ShopKart build — no inline policy files. Correct option N/A — practical task. |

---

## Objective Assignment — Overall QC

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes:** 10 questions total — 6 MCQs (4 Easy Q1–Q4, 2 Moderate Q5–Q6) + 4 MSQs (2 Moderate Q7–Q8, 2 Hard Q9–Q10). Progressive Easy → Moderate → Hard. All questions scenario-based; no session-reference phrasing. Every question includes answer explanations with distractor reasoning. Topics: failure modes, Rank 1 diagnosis, levers (top-k, filter, strict prompt), `guess_category` fallback, improved vs baseline config, metadata filter limits.

**Outcome:** PASS

---

## Subjective Assignment — Overall QC (Pass 2 — simplified)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes:** Simplified per learner feedback — reduced from 3 queries + dual baseline/improved passes to **2 queries + improved pass only**. `guess_category` and `retrieve_filtered` supplied for copy-paste; student implements strict prompt and `main()` loop. Assumes existing ShopKart pipeline (no full policy-file recreation). Still tests metadata filter, top-k=5, strict grounding, and Rank-1-first evaluation. Reference solution trimmed to delta code only. Case-c submission clear.

**Outcome:** PASS

---

## Combined Expected Result

| Assignment | Content Coverage | Creativity | Structural Adherence | Logical Mistakes | Presentation Mistakes |
|---|---|---|---|---|---|
| Objective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |
| Subjective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |

**Final QC status:** PASS — all criteria meet expected thresholds (subjective re-QC after simplification: Pass 2).

---

## Subjective Assignment — QC Pass 1 (archived)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes (original):** Three queries, baseline + improved passes, full standalone reference solution (~250 lines). Superseded by simplified version above.
