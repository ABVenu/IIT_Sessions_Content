# Assignment question QC report — Session 35

**Sources:** `OS_Assignment_Questions_GenerationPrompt.md`, `Lecture Notes Released.md` (curriculum alignment reference)  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`

---

## Per-question QC (objective)

| Question | Type | Remarks |
| --- | --- | --- |
| 1 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — matches feature-engineering / tabular-vs-language bottleneck. |
| 2 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — word ambiguity + context (classic *bank* example framing). |
| 3 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — neuron ↔ linear regression standard analogy. |
| 4 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — Transformer simultaneous processing + attention. |
| 5 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — GPT pre-training / next-word objective. |
| 6 | MCQ (Moderate) | Correct: **C**; relevancy: **Yes** — 90 ÷ 0.75 = 120 tokens per stated rule. |
| 7 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — context window definition, overflow behaviour, widely published Gemini 1.5 Pro ~1M context claim. |
| 8 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — prompt vs completion billing, subword splits, completion length vs cost. |
| 9 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — hallucination definition, plausible-token training objective, knowledge cutoff; D is a deliberate false distractor. |
| 10 | MSQ (Hard) | Correct: **A, B, D**; relevancy: **Yes** — Word2Vec, RNN long-sequence weakness, attention; C false about hand-labelling every token. |

---

## Per-question QC (subjective)

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Practical (single `.py`) | Medium difficulty; case **(c)**; no dataset; `tiktoken` + heuristic + 4096 window + Part E paragraph + Part F **0.2 / 0.9** creativity compare; provider note + SDK method comment; skip rule clarified for non-OpenAI keys (see subjective-only QC). |

---

## Overall QC — objective assignment

| Criterion | Rating / Result |
| --- | --- |
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

---

## Overall QC — subjective assignment

| Criterion | Rating / Result |
| --- | --- |
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Outcome:** All ratings meet the expected threshold (≥ 5; no logical or presentation issues). No further revision pass required for this iteration.

---

## Subjective-only QC — `OS_Assignment_Questions_GenerationPrompt.md` (Iteration — 2026-05-13)

**Checklist (mapped to OS prompt §2–3)**

| OS requirement | Status |
| --- | --- |
| Exactly **1** practical subjective task | Met — single script, Parts A–F |
| **Medium** difficulty, applied (not rote definition) | Met — Eco-Council budgeting + API creativity check |
| Coding implementation where course includes coding | Met — `tiktoken`, prints, optional LLM calls |
| **Case (c)** submission (single file, VS Code, run, LMS paste) | Met — `## Submission instructions` |
| **Self-contained** stem; no “in the session” phrasing | Met |
| **Example** of expected console shape | Met — fenced `text` block + note when API key present |
| **Answer explanation** block: walkthrough + sketch code + alternatives | Met — `## Answer explanation (for Assess platform)` |
| Grammar / spelling | Met — minor typographic consistency only |

**Improvisation during QC:** **Part F, step 5** was tightened so learners who use **non-OpenAI** APIs are not forced to print the OpenAI-only skip line when a different provider’s key is missing.

**Subjective row (table)**

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Practical (single `.py`) | Medium difficulty; case **(c)**; no dataset; clear I/O labels; Part F **0.2 / 0.9**; provider flexibility + documented SDK call + skip rules clarified. |

**Overall QC — subjective (post-check)**

| Criterion | Rating / Result |
| --- | --- |
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Outcome (subjective vs OS prompt):** Threshold met after the Part F step-5 clarification.
