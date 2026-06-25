# Assignment Question QC Report — Working with APIs and JSON

## Exclusion list (per authoring brief)

Questions must **not** test:

- `response.ok`
- 429 exponential-backoff retry loops
- `try`/`except` timeout retry guidance
- PATCH / PUT / DELETE CRUD details (GET + brief POST only)

---

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Live parcel tracking needs API, not prompt-only guessing. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. API as contract between components. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Read-only Open-Meteo → GET. DELETE/PATCH appear only as distractors. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `json.loads` string → dict. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. URL typo → 4xx/404; status-before-parse discipline. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. `status_code == 200` before `response.json()` — uses explicit status check, not `response.ok`. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C, E. Relevancy: Yes. Safe GET: params, timeout, status check, read-only GET. No backoff/try-except tested. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C, E. Relevancy: Yes. Field mapping: tokens, grounding, testing, weather_code → words. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C, E. Relevancy: Yes. Full two-call pipeline Open-Meteo → map → grounded prompt → Groq. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. 401/429/200 meanings; 429 as rate limit (not backoff implementation); mapping typo vs 404 distinction. |
| Q1 | Subjective (Applied, Medium) | Medium difficulty: Yes. FestRoute Pune weather agent — GET, status-first, map, prompt, Groq. Submission case c: Yes — single `festroute_weather_agent.py`, env key, LMS code box. Live Open-Meteo (no dataset file). Excluded topics not required. Complete solution in answer explanation. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria satisfied:

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective applied coding task (Open-Meteo + JSON mapping + Groq).
- Complete answer explanations for every question.
- No “as taught in session” phrasing in learner-facing prompts.
- Excluded topics (`response.ok`, backoff retry, try/except timeout, PATCH/PUT/DELETE depth) absent from questions and subjective rubric.
- Content Coverage, Creativity, Structural Adherence all **5**.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## CSV Export QC (`AssignmentCreation.csv`)

**Trigger:** CSV export with `tagRelationships` = `6a3ce7f8cf3ecfdba03315ed`.

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) + header |
| Question types | 6 `mcsc` + 4 `mcmc` + 1 `subjective` |
| `tagRelationships` on all rows | `6a3ce7f8cf3ecfdba03315ed` |
| Difficulty levels | Q1–Q4: 0; Q5–Q8: 0.5; Q9–Q10 + subjective: 1 |
| `mcscAnswer` values | Q1=2, Q2=3, Q3=1, Q4=2, Q5=1, Q6=2 |
| `mcmcAnswer` values | Q7=`1, 2, 3, 5`; Q8=`1, 2, 3, 5`; Q9=`1, 2, 3, 5`; Q10=`1, 2, 3` |
| Option format | No A)/B) prefixes — content only |
| Question bodies | Start with scenario content, no Q-number/difficulty labels |
| Subjective `answerExplanation` | Full solution code only (no rubric/grading table) |
| CSV parse test | Python `csv.DictReader` — 11 rows, 21 columns each, no parse errors |
| Content fidelity | All question/option/explanation text matches assignment markdown sources |
| Excluded topics | No `response.ok`, backoff retry, try/except timeout, or PATCH/PUT/DELETE depth in questions |

### CSV Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**CSV QC iteration:** 1 — passed.

---

## Coverage Checklist (Lecture Notes Released)

| Concept in notes | Objective / Subjective coverage |
| --- | --- |
| APIs vs prompts for live data | Q1 |
| API as contract | Q2 |
| Request–response / REST read with GET | Q3, Q7, Q9 |
| POST introduced (not PATCH/PUT/DELETE depth) | Q3 distractors only |
| HTTP status codes 200, 401, 404, 429, 500 | Q5, Q6, Q10 |
| Status before `response.json()` | Q6, Q7, Q9; Subjective fetch |
| `json.loads` / mapping / `response.json()` | Q4, Q8 |
| `requests.get` params + timeout | Q7; Subjective |
| Field mapping → LLM prompt | Q8, Q9; Subjective |
| Two-call weather + Groq pattern | Q9; Subjective |
| Grounding vs endpoint error (200 + mapping typo) | Q10 |
| Gemini LLM + external APIs (surface) | Not tested — introductory only; optional future easy MCQ |
| Fake Store / Frankfurter / GitHub demos | Not tested — surface demos; core pattern covered by Q9/Subjective |
| **Excluded:** `response.ok` | Not tested |
| **Excluded:** 429 backoff / try-except timeout | Not tested; Q10 names 429 meaning only |
| **Excluded:** PATCH/PUT/DELETE CRUD | Not tested beyond GET focus |
