# Assignment question QC report — Session 25

**Sources:** `OS_Assignment_Questions_GenerationPrompt.md`, `Lecture Notes Released.md`  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`  
**Reuse note:** Reused from **iitr-as-260113 / Module3 / Session34** (same title: *Ollama: Exploring Another World of LLMs*). Two objective items aligned to Session 25 live coverage (Q2 verify command; Q10 distractor).

---

## Per-question QC (objective)

| Question | Type | Remarks |
| --- | --- | --- |
| 1 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — local open-source inference for privacy-sensitive prompts. |
| 2 | MCQ (Easy) | Correct: **B** (`ollama --version`); relevancy: **Yes** — matches Session 25 install validation command (adapted from Session 34 `ollama -v`). |
| 3 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — default local chat URL `localhost:11434/api/chat` in released notes. |
| 4 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — proprietary GPT weights not downloadable. |
| 5 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — avoid heavy RAM models on 8 GB laptop. |
| 6 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — cloud vs local: URL, Bearer header, model tag; same JSON shape. |
| 7 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — cost, privacy, learning benefits; C is false distractor. |
| 8 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — small-model hallucination, sandbox use, nuance; C false on live stock data. |
| 9 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — HTTP chat payload/response pattern; D false (OpenAI SDK not required). |
| 10 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — `list`, `rm`, no local API key; D false (`pull` needs no API key). Adapted from Session 34 `ollama stop` distractor (not taught in Session 25). |

---

## Per-question QC (subjective)

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Practical (single `.py`) | Medium difficulty; case **(c)**; starter with `save_resume_html` as-is; local vs cloud via same prompt; two-column + styling in `RESUME_PROMPT`; open HTML via double-click or file:// path; 2 comment lines; paste full file in LMS. Reused unchanged — aligns with Session 25 local-vs-cloud compare LO. |

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

**Outcome:** All ratings meet the expected threshold (≥ 5; no logical or presentation issues).

---

## OS prompt checklist (both assignments)

| OS requirement | Status |
| --- | --- |
| Exactly **2** assignments (objective + subjective) | Met |
| Objective: **10** Qs — 6 MCQ (4 Easy, 2 Moderate) + 4 MSQ (2 Moderate, 2 Hard) | Met — ordered Easy → Hard |
| Subjective: **1** medium practical task | Met — `resume_generator.py` (HTML resume, local vs cloud) |
| Scope limited to session notes | Met — Ollama install/CLI, local vs cloud HTTP, trade-offs, API key handling |
| No “as taught in the session” phrasing | Met |
| Answer explanations for every question | Met — inline in both `.md` files |
| QC table + overall ratings | Met |

---

## CSV export QC — `AssignmentCreation.csv`

**Trigger:** CSV export with `tagRelationships` = `6a3a2b20b59fd37f6abddb16`.

| Check | Result |
| --- | --- |
| Row count | 11 (6 mcsc + 4 mcmc + 1 subjective) |
| `tagRelationships` on all rows | `6a3a2b20b59fd37f6abddb16` |
| Difficulty order | Easy (0) → Moderate (0.5) → Hard (1) |
| Q2 correct option | `ollama --version` (option.2, mcscAnswer=2) |
| Q10 option D | `ollama pull` API-key distractor (Session 25 aligned) |
| Subjective body | Starter code + submission instructions in `contentBody` |
| Subjective solution | Reference `ask_ollama` in `answerExplanation` only |
| CSV parse test | Pass — no field-count or quoting errors |

**Outcome:** PASS
