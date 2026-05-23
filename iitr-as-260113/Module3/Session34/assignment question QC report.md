# Assignment question QC report — Session 34

**Sources:** `OS_Assignment_Questions_GenerationPrompt.md`, `Lecture Notes Released.md`  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`

---

## Per-question QC (objective)

| Question | Type | Remarks |
| --- | --- | --- |
| 1 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — local open-source inference for privacy-sensitive prompts. |
| 2 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — `ollama -v` install verification. |
| 3 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — default local chat URL `localhost:11434/api/chat`. |
| 4 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — proprietary GPT weights not downloadable. |
| 5 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — avoid heavy RAM models on 8 GB laptop. |
| 6 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — cloud vs local: URL, Bearer header, model tag; same JSON shape. |
| 7 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — cost, privacy, learning benefits; C is false distractor. |
| 8 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — small-model hallucination, sandbox use, nuance; C false on live stock data. |
| 9 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — `requests.post`, `stream: false`, parse `message.content`; D false (no OpenAI SDK required). |
| 10 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — `list`, `rm`, no local API key; D false (auto-start after stop). |

---

## Per-question QC (subjective)

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Practical (single `.py`) | Medium difficulty; case **(c)**; starter with `save_resume_html` as-is; two-column + styling in `RESUME_PROMPT`; open HTML via double-click or file:// path; quality check includes styling compare; 2 comment lines; paste full file in LMS. |

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

**Outcome:** All ratings meet the expected threshold (≥ 5; no logical or presentation issues). No further revision pass required.

---

## OS prompt checklist (both assignments)

| OS requirement | Status |
| --- | --- |
| Exactly **2** assignments (objective + subjective) | Met |
| Objective: **10** Qs — 6 MCQ (4 Easy, 2 Moderate) + 4 MSQ (2 Moderate, 2 Hard) | Met — ordered Easy → Hard |
| Subjective: **1** medium practical task | Met — `resume_generator.py` (HTML resume, local vs cloud) |
| Scope limited to session notes | Met — Ollama install/CLI, local vs cloud HTTP, trade-offs; no deep embeddings implementation |
| No “as taught in the session” phrasing | Met |
| Answer explanations for every question | Met — inline in both `.md` files |
| QC table + overall ratings | Met |
