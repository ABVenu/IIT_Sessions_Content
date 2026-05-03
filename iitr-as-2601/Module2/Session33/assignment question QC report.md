# Assignment Question QC Report — Session 33

**Session:** Time Series: Understanding Data That Changes Over Time  
**Module:** Module 2  
**Course:** iitr-as-2601

---

## Objective Assignment QC

| Q# | Type | Correct Option(s) | Correct Option Relevancy | Remarks |
|---|---|---|---|---|
| Q1 | MCQ — Easy | B | Yes | Tests the defining property of time series: order by time matters. Scenario-based cafe sales context. Distractors are plausible but incorrect. |
| Q2 | MCQ — Easy | A | Yes | Tests trend as the long-term direction of data. The rising app-user scenario maps directly to positive trend from the notes. |
| Q3 | MCQ — Easy | B | Yes | Tests seasonality as a repeated fixed-interval pattern. Friday-Saturday spikes clearly represent weekly seasonality. |
| Q4 | MCQ — Easy | C | Yes | Tests why random split fails for time series. Correct option identifies future leakage, exactly as covered in the notes. |
| Q5 | MCQ — Moderate | C | Yes | Tests chronological splitting with a numerical 10-month dataset. Correct answer uses first 80% as train and last 20% as test. |
| Q6 | MCQ — Moderate | C | Yes | Tests rolling window calculation. Correct answer is computed from Day 2, Day 3, and Day 4: `(120 + 110 + 130) / 3 = 120`. |
| Q7 | MSQ — Moderate | A, B, C | Yes | Tests rolling windows, smoothing, and lag features together. Option D is a future-leakage trap and is correctly excluded. |
| Q8 | MSQ — Moderate | A, B, C | Yes | Tests time series evaluation and baseline comparison. Correct options cover MAE, RMSE, and MAPE; incorrect option rejects the false idea that complex models always beat baselines. |
| Q9 | MSQ — Hard | A, B, D | Yes | Tests deeper MAPE understanding, including scale-independent comparison, zero-actual limitation, and percentage-error calculation. |
| Q10 | MSQ — Hard | A, B, C | Yes | Tests end-to-end time series workflow decisions: sort by date, chronological split, and baseline comparison. Shuffling is correctly rejected. |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear | Dataset Dependency | Remarks |
|---|---|---|---|---|---|
| Q1 | Coding Implementation | Medium | Yes — Single `.py` file, run and verify, submit in LMS code editor/answer box | No external file needed — dataset is provided fully in-code using `pandas` | Creative applied scenario (cafe sales forecasting). Covers date index setup, rolling features, lag features, chronological split, naive and rolling mean baselines, and MAPE evaluation. The task stays within the session scope and does not ask learners to implement advanced forecasting models not taught in the notes. |

---

## Overall QC Ratings

| Metric | Objective Assignment | Subjective Assignment |
|---|---|---|
| Content Coverage | 5 / 5 | 5 / 5 |
| Creativity | 5 / 5 | 5 / 5 |
| Structural Adherence | 5 / 5 | 5 / 5 |
| No Logical Mistakes | True | True |
| No Presentation Mistakes | True | True |

---

## QC Verification Notes

**Structural Adherence:**
- Objective assignment has exactly 10 questions: 6 MCQs (4 Easy + 2 Moderate) and 4 MSQs (2 Moderate + 2 Hard).
- Questions are ordered progressively: Easy (Q1-Q4), Moderate (Q5-Q8), Hard (Q9-Q10).
- Subjective assignment contains exactly 1 medium-difficulty coding implementation task.
- Submission instructions follow the single-file coding submission pattern.

**Content Coverage:**
- Objective questions cover time series definition, trend, seasonality, future leakage, chronological split, rolling windows, lag features, MAE/RMSE/MAPE, baseline forecasts, and workflow best practices.
- Subjective assignment directly applies the session's coding concepts: `pd.date_range()`, datetime index setup, `.rolling(window=3)`, `.shift()`, chronological split, and MAPE.

**Creativity:**
- Objective questions use practical scenarios such as cafe sales, fitness app growth, pizza orders, grocery sales, website traffic, and product demand.
- Subjective task uses a realistic cafe forecasting workflow instead of copying the lecture's stock or temperature examples.

**Logical Accuracy:**
- Q5 chronological split is correct for 10 rows at 80:20: Jan-Aug train and Sep-Oct test.
- Q6 rolling mean calculation is correct: `(120 + 110 + 130) / 3 = 120`.
- Q9 MAPE calculation is correct: `|200 - 180| / 200 * 100 = 10%`.
- Subjective reference solution uses only past/current window information and avoids random splitting.
- No content outside the Session 33 lecture notes has been included.
