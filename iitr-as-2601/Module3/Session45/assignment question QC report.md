# Assignment Question QC Report: Prompt Versioning & API Rate Limits

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests inline notebook prompt edits vs saved versioning (baseline loss risk). |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests separating prompt prose from config/model settings. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests HTTP 429 as rate-limit / slow-down signal on shared Groq key. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests qualitative eval fairness — same input required for v1 vs v2. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests half-updated registry bundle (v2 prompt + v1 config mismatch). |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests `stop_after_attempt(4)` total attempt cap with Tenacity. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests complete registry bundle fields; rejects laptop serial (D). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests qualitative eval checklist including injection resistance; rejects GPU fan (D). |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests RPM/TPM, agent multiplier, sleep prevention vs backoff, Tenacity recovery; rejects 401→backoff (D). |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests Tenacity decorator, wait_exponential, before_sleep_log, jitter; rejects infinite retry (D). |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes (full implementation of `shopeasy_order_retry.py` from requirements spec — no fill-in-the-blanks). Clear submission instructions (case c): Yes — single file, no API key. ShopEasy Diwali sale e-commerce scenario (order lookup throttling). Expected: 2 WARNING retry logs, order status for ORD-7842, `Total API attempts: 3`, `logs/api_retries.log` written. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | All released-note topics tested: versioned files/config split, registry bundles, qualitative eval fairness & injection, HTTP 429 & RPM/TPM, Tenacity exponential backoff, retry logging via before_sleep_log, jitter mention in Q10. |
| Creativity | 5 | ShopEasy e-commerce scenario throughout; Diwali flash-sale order lookup throttling, injection eval on support bot, retry handler for customer order-status API. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one medium coding task, case-c submission, full answer explanation with reference solution. |
| No Logical Mistakes | True | Correct options verified against Lecture Notes Released.md; subjective reference: full `lookup_order_status` implementation — 2 fake 429s then success on attempt 3, log file + console retry trail. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations for all 11 questions; grammar checked. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.

---

## CSV Generation QC

**File:** `assignment.csv`  
**tagRelationships:** `6a34f2248b72b1cc691ce9f2`

| Check | Result |
|---|---|
| Row count | 11 questions (10 objective + 1 subjective) + header |
| CSV parse | Passed — all rows have 21 columns, no parse errors |
| Question types | 6 mcsc, 4 mcmc, 1 subjective |
| Difficulty levels | Easy MCQ 0 (×4), Moderate MCQ 0.5 (×2), Moderate MSQ 0.5 (×2), Hard MSQ 1 (×2), Subjective 0.5 |
| Options format | No A/B/C/D prefixes — content only |
| Answer explanations | All 11 rows populated; subjective solution in answerExplanation only |
| Content fidelity | Matches assignment-objective.md and assignment-subjective.md without session references |
