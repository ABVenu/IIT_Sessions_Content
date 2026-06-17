# Assignment Question QC Report: LLM Internals for Designers

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests API billing on input/output tokens via GreenCart cost scenario. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests tokens vs words / tokenisation divergence (36 words vs 64 tokens pattern). |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests context window definition (full prompt stack in one forward pass). |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests disk persistence vs what the model sees per API call. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests temperature=0 for refund-policy RAG consistency. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests MAX_CONTEXT_TOKENS chunk-cap loop stopping before overflow. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests shared context-window components; rejects .env key as prompt payload (D). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests temperature/seed per feature (refund, lookup, SMS); rejects high temp on policy (D). |
| 9 | Objective MSQ - Hard | Correct options: A, B, D, E. Relevancy: Yes. Tests silent truncation, windowed history, fixes, agent token growth; rejects temp deleting disk (C). |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests designer playbook trimming priorities, observation cap, safety margin; rejects full PDF paste (D). |
| 1 | Subjective - Easy Practical Task | Easy difficulty: Yes (two small TODO functions only). Clear submission instructions (case c): Yes — single `prompt_budget_checker.py`, starter code provided, submit in LMS. No dataset or API key. Student implements `count_tokens` and `windowed_history` only; expected: tokens > words, 4 kept / 3 dropped, grounding rule in first dropped message. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective unchanged. Subjective now covers core token counting and windowed-history truncation — two foundational skills from released notes, without RAG chunk-loop implementation. |
| Creativity | 5 | GreenCart support-bot scenario throughout; applied billing, policy, and truncation bugs; single-file budget checker mirrors lab exercises. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one easy fill-in coding task with starter scaffold, case-c submission, full answer explanation. |
| No Logical Mistakes | True | Correct options verified against Lecture Notes Released.md; subjective reference solution: token count > word count, 4 kept / 3 dropped with grounding rule first in dropped list. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations for all 11 questions; grammar checked. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.

---

## CSV Generation QC

**File:** `assignment.csv`  
**tagRelationships:** `6a324cb246c3cf883764aed3`

| Check | Result |
|---|---|
| Row count | 11 questions (10 objective + 1 subjective) + header |
| CSV parse | Passed — all rows have 20 columns, no parse errors |
| Question types | 6 mcsc, 4 mcmc, 1 subjective |
| Difficulty levels | Easy MCQ 0 (×4), Moderate MCQ 0.5 (×2), Moderate MSQ 0.5 (×2), Hard MSQ 1 (×2), Subjective 0 |
| Options format | No A/B/C/D prefixes — content only |
| Answer explanations | All 11 rows populated; subjective solution in answerExplanation only |
| Content fidelity | Matches assignment-objective.md and assignment-subjective.md without session references |
