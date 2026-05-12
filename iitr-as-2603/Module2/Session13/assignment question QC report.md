# Assignment Question QC Report — Session 13: The ML Workflow & Habits

---

## Objective Assignment QC

| Q# | Type | Difficulty | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|---|
| Q1 | MCQ (Single) | Easy | B | Yes — "Google Colab runs code on Google's cloud servers" directly answers why a budget laptop performs well | Scenario-based, self-contained, clear distractors |
| Q2 | MCQ (Single) | Easy | D | Yes — `result` (Pass/Fail) is clearly the prediction target; all other columns are inputs | Clean dataset table provided; no ambiguity |
| Q3 | MCQ (Single) | Easy | C | Yes — explicit if-else smart home logic is the definition of Rule-based AI | Real-world scenario; distractors are meaningfully distinct |
| Q4 | MCQ (Single) | Easy | C | Yes — `DummyClassifier(strategy="most_frequent")` always predicts the dominant class, and 68% matches the class distribution | Code snippet included; explanation tests conceptual understanding, not just recall |
| Q5 | MCQ (Single) | Moderate | C | Yes — examining classification report for imbalanced healthcare data is the correct next step | Applied judgment question; tests critical thinking about accuracy vs recall trade-off |
| Q6 | MCQ (Single) | Moderate | C | Yes — 25% of 4,000 (remaining after test split) = 1,000 rows is mathematically correct | Numerical reasoning; code is provided and unambiguous; calculation verified |
| Q7 | MSQ (Multiple) | Moderate | A, B, D | Yes — all three correct options are explicitly taught habits from the session | Distractors (C, E) represent common beginner mistakes clearly described in lecture |
| Q8 | MSQ (Multiple) | Moderate | A, B, D | Yes — baseline floor, imbalance signal, and DummyClassifier definition are all directly from session content | Distractor C (ensemble/feature engineering) directly contradicts the "simplest model" principle |
| Q9 | MSQ (Multiple) | Hard | A, B, D, E | Yes — label, feature selection, problem type are all correctly identified; circular logic (C) is a common framing mistake explicitly taught | Real-world logistics scenario; tests ability to identify future-information leakage |
| Q10 | MSQ (Multiple) | Hard | A, B, D | Yes — 98.5% accuracy, 0% fraud recall, and F1 ≈ 0 are all verified logical outcomes of a most-frequent classifier on this distribution | Distractor C (precision = 100%) specifically tests understanding that baseline never predicts the minority class |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear? | Dataset Provided? | Remarks |
|---|---|---|---|---|---|
| Q1 | Practical Coding (Colab Notebook) | Medium | Yes — step-by-step Colab setup, share link instructions, and viewing permission explicitly stated | Yes — synthetic data generation code is embedded in Cell 1; no external download required | 7-cell structured workflow covering problem framing, EDA, feature/label separation, 60/20/20 split, baseline, and interpretation. Scenario is creative and applied. Full answer explanation included: ideal solution walkthrough per cell, complete exact code for all 6 code cells, and 4 alternative approaches. |

---

## Subjective Question — Detailed QC

### Code Logic Verification

| Cell | Code / Logic Checked | Verdict |
|---|---|---|
| Cell 1 — Data Generation | `data` is a dict of numpy arrays; `(data["col"] < 20).astype(int)` comparison on numpy arrays is valid. `cancel_prob / cancel_prob.max()` normalises correctly to [0,1]. `np.where(cancel_prob > 0.55, "Yes", "No")` produces a ~70–75% / 25–30% class split. `df.to_csv(..., index=False)` writes file without adding index column. | ✅ No issues |
| Cell 3 — Load & Inspect | `pd.read_csv("streamnow_users.csv")` loads correctly. Shape comment (1200, 8) verified: 8 columns (user_id + 6 features + will_cancel = 8). | ✅ No issues |
| Cell 4 — Features & Label | `df.drop(columns=["user_id", "will_cancel"])` removes both non-feature columns from 8 → 6 features. `X.shape` comment (1200, 6) mathematically verified. | ✅ No issues |
| Cell 5 — Split | Step 1: 1200 × 0.20 = 240 test rows, 960 remaining. Step 2: 960 × 0.25 = 240 val rows, 960 × 0.75 = 720 train rows. Comments ~720 / ~240 / ~240 verified. | ✅ No issues |
| Cell 6 — Baseline | `DummyClassifier(strategy="most_frequent")` fitted on `X_train`, predicts on `X_test`. DummyClassifier never predicts minority class "Yes" → recall for "Yes" = 0.00, F1 for "Yes" = 0.00. `accuracy_score` and `classification_report` used correctly. | ✅ No issues |
| Alternatives | `strategy="stratified"` — valid sklearn DummyClassifier strategy ✅. `f1_score(y_test, baseline_preds, pos_label="Yes")` — correct API ✅. `stratify=y` in `train_test_split` — correct parameter ✅. | ✅ No issues |

### Presentation Issues Found & Fixed

| Issue | Location | Fix Applied |
|---|---|---|
| Cell 2 problem framing template was inside a fenced code block (``` ```) — this could confuse students into thinking it should go in a code cell rather than a Markdown cell | Cell 2 task description | Changed to a blockquote (`>`) format which clearly signals this is text/Markdown content, not code |
| Typo "Co py" in submission instructions | Submission Instructions | Fixed to "Copy" (applied in previous revision) |

---

## Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | All major session topics covered: Colab, Rule-based AI vs ML, Features/Labels, Data Splitting math, Baseline models (DummyClassifier), Imbalanced data metrics, Problem Framing |
| Creativity | 5 | All questions are scenario-based — Zara's laptop, school teacher dataset, smart home script, Rohit's pipeline, healthcare screening, logistics framing, fraud detection. No abstract/rote recall questions. |
| Structural Adherence | 5 | Exactly 10 questions: 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard). Ordered Easy → Moderate → Hard. All have correct answers + full explanations of correct and incorrect options. |
| No Logical Mistakes | True | All correct answers verified: Q6 calculation confirmed (25% × 4000 = 1000 ✓), Q10 distractor C (precision=100%) verified as incorrect since baseline never predicts minority class ✓ |
| No Presentation Mistakes | True | All questions are grammatically correct, self-contained, clearly formatted with tables/code where needed |

### Subjective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Covers all core session skills: problem framing, load/inspect, feature-label separation, 60/20/20 split, DummyClassifier baseline, classification report interpretation |
| Creativity | 5 | StreamNow music streaming churn scenario is relatable and industry-relevant; dataset is realistic with engineered label (low-engagement users more likely to cancel); not a direct copy of any lecture example |
| Structural Adherence | 5 | Exactly 1 practical task at medium difficulty; submission instruction follows Colab shareable link format (aligned with Case B); dataset provided inline via generation code; answer explanation with walkthrough + complete code + alternatives is present |
| No Logical Mistakes | True | All code cells verified (see table above); column counts, split math, DummyClassifier behaviour all confirmed correct |
| No Presentation Mistakes | True | Cell 2 template block fixed from code fence to blockquote; typo fixed; all cells numbered; submission sharing instructions unambiguous |

---

## QC Summary

All criteria for both assignments meet the required standard:

- Content Coverage: **5 / 5** ✅
- Creativity: **5 / 5** ✅
- Structural Adherence: **5 / 5** ✅
- No Logical Mistakes: **True** ✅
- No Presentation Mistakes: **True** ✅

**Both assignments are approved for platform upload.**
