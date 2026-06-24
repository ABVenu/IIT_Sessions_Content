# Assignment Question QC Report: Structured Outputs for Agents

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests medical-notes scenario — typed DB columns reject free-form strings like `"80 KGs"`. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `json.loads()` as the safe way to parse LLM JSON strings into Python dicts. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `required` keyword — all listed keys must appear in valid output. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests separate `schemas/` and `prompts/` files — blueprint vs instruction roles. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests Groq `json_object` mode — syntax guarantee vs enum semantics still needing Python validation. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests skipping validation after parse — wrong-case enum reaching UI. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests schema-file contents (`required`, `properties`, `type`); rejects user message (C) and persona prompt (E). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests defensive parsing pipeline; rejects `eval()` (C) and deleting schema (E). |
| 9 | Objective MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Tests parse → validate → route order and `validate_or_raise`; rejects writing invalid data to DB (C) and skipping validation because of JSON mode (E). |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests JSON debugging checklist; rejects removing `required` keys to force pass (D). |
| 1 | Subjective - Easy Practical Task | Easy difficulty: Yes — starter code provides all parsing helpers and test cases; student completes `validate_ticket`, `validate_or_raise`, and `main()` only. Clear submission instructions (case c): Yes — single `.py` file, no API key. Two test cases: valid ticket (SUCCESS) + invalid priority `HIGH` (FAILED). |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | All released-note topics tested: JSON schema (`required`, `properties`, `enum`), prompt vs schema separation, Groq JSON mode limits, defensive parsing (`strip_markdown_fences`, `extract_json_object`, `safe_parse_model_json`), lite validation (`validate_ticket`, `validate_or_raise`), pipeline order, debugging checklist. Pydantic/ReAct surface concepts omitted from subjective (preview only — not implementation scope). |
| Creativity | 5 | ShopEasy support-ticket classifier scenario throughout; hospital-notes typed-table motivator in Q1; staging raw-output cleanup task mirrors production gate-before-UI pattern. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one easy fill-in coding task with starter code, case-c submission, full answer explanation with reference solution. |
| No Logical Mistakes | True | Correct options verified against Lecture Notes Released.md; subjective reference: Case 1 SUCCESS, Case 2 `FAILED: Invalid priority: 'HIGH'`. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations for all 11 questions; Case A described without nested markdown fence breakage. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.

---

## CSV Generation QC

**File:** `assignment.csv`  
**tagRelationships:** `6a3b7fc06e8d0f08b2ae1df6`

| Check | Result |
|---|---|
| Row count | 11 questions (10 objective + 1 subjective) + header |
| CSV parse | Passed — all rows have 21 columns, no parse errors |
| Question types | 6 mcsc, 4 mcmc, 1 subjective |
| Difficulty levels | Easy MCQ 0 (×4), Moderate MCQ 0.5 (×2), Moderate MSQ 0.5 (×2), Hard MSQ 1 (×2), Subjective 0 |
| Options format | No A/B/C/D prefixes — content only |
| Answer explanations | All 11 rows populated; subjective solution in answerExplanation only |
| Content fidelity | Matches assignment-objective.md and assignment-subjective.md without session references |
