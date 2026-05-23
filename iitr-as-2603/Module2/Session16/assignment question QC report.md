# Assignment Question QC Report — Session 16: Linear Regression Fundamentals

---

## Objective Assignment QC

| Q# | Type | Difficulty | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|---|
| Q1 | MCQ (Single) | Easy | B | Yes — fare in rupees is a continuous regression target | QuickRide trip-fare scenario; distractors name classification, clustering, RL |
| Q2 | MCQ (Single) | Easy | B | Yes — salary is numeric target; job_level is categorical feature | HR table story; tests “numeric column ≠ regression target” doubt from notes |
| Q3 | MCQ (Single) | Easy | B | Yes — constant term in score ≈ 7.5×hours + 40 is the intercept | Coaching-app equation; distractor A is the coefficient |
| Q4 | MCQ (Single) | Easy | A | Yes — 62−58=+4 means under-prediction | Residual sign drill; arithmetic verified |
| Q5 | MCQ (Single) | Moderate | B | Yes — coefficient is Δy per one-unit Δx holding others fixed | Housing income coefficient interpretation |
| Q6 | MCQ (Single) | Moderate | B | Yes — low train and test with small gap → underfitting | Matches California housing example (~61% / ~58%) from notes |
| Q7 | MSQ (Multiple) | Moderate | A, C | Yes — bill in rupees and exact exam score are numeric targets | Distractors B and D are classification |
| Q8 | MSQ (Multiple) | Moderate | A, B, D | Yes — split first, pipeline fit on train, score on held-out test | Distractor C is pre-split scaler leakage |
| Q9 | MSQ (Multiple) | Hard | A, B, C | Yes — stable gap, overfit gap, and underfit pattern all valid | Distractor D is illogical evaluation advice |
| Q10 | MSQ (Multiple) | Hard | A, B, D | Yes — mean from y_train only, same test metric, beating baseline shows signal | Distractor C leaks full y into baseline |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear? | Dataset Provided? | Remarks |
|---|---|---|---|---|---|
| Q1 | Practical Coding (single `.py` file) | Medium | Yes — Case C: single file, run verification, LMS code-box submission | Yes — inline synthetic `study_hours` / `exam_score` bootstrap | Three tasks: split-first LR; baseline R² + top-3 residual table + two comment lines |

---

## Subjective Question — Detailed QC

### Code Logic Verification

| Step | Code / Logic Checked | Verdict |
|---|---|---|
| Synthetic data | `seed=42`, 80 rows, linear trend + noise | ✅ No issues |
| Split first | `train_test_split` before `.fit()` | ✅ No issues |
| Linear regression | Intercept/coef/scores on train and test; predict 6 hours | ✅ No issues |
| Mean baseline | `y_train.mean()` only; constant preds on test; `r2_score` | ✅ No issues |
| Residual table | `actual − predicted`; sort by absolute residual | ✅ No issues |
| Reference run | Train 64 / Test 16; train score 0.96, test 0.97; baseline R² −0.02 | ✅ Verified locally |
| Alternatives | CSV or `make_regression` OK if same discipline | ✅ No issues |

### Presentation Issues Found & Fixed

| Issue | Location | Fix Applied |
|---|---|---|
| None | — | Initial draft met structural and logical checks on first QC pass |

---

## Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Regression vs classification, target/features, intercept/coefficient, residuals, Pipeline habits, train–test fit diagnosis, mean baseline |
| Creativity | 5 | QuickRide, StudyBoost, HR salary, property analyst, and model-review board scenarios; no session-reference phrasing |
| Structural Adherence | 5 | 10 questions: 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard); progressive difficulty; full answer explanations |
| No Logical Mistakes | True | Q4 arithmetic, Q6 diagnosis, and Q10 baseline leakage rules checked |
| No Presentation Mistakes | True | Self-contained prompts; grammatically clean; independent of lecture wording |

### Subjective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | `LinearRegression`, split-first, `.score`/R², mean baseline comparison, residual table, generalization comment |
| Creativity | 5 | StudyBoost ed-tech pilot; mirrors study-hours workflow without California CSV dependency |
| Structural Adherence | 5 | One medium coding task (3 tasks); Case C submission and complete answer explanation |
| No Logical Mistakes | True | Reference script run confirms expected parameter order and outputs |
| No Presentation Mistakes | True | Seeds, rounding, print labels, and comment requirements are unambiguous |

---

## QC Summary

All criteria for both assignments meet the required standard:

- **Content Coverage:** 5 (objective and subjective)  
- **Creativity:** 5 (objective and subjective)  
- **Structural Adherence:** 5 (objective and subjective)  
- **No Logical Mistakes:** True  
- **No Presentation Mistakes:** True  

**Status:** Ready for Assess platform upload (enter each question’s answer explanation in the platform fields).
