# Assignment Question QC Report — Session 15: Leakage & Imbalance

---

## Objective Assignment QC

| Q# | Type | Difficulty | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|---|
| Q1 | MCQ (Single) | Easy | B | Yes — post-outcome `refund_issued` is classic temporal leakage | NovaBank fraud scenario; distractors name imbalance, CV, and recall |
| Q2 | MCQ (Single) | Easy | B | Yes — split → fit scaler on train → transform test is the guard workflow | Campus health vitals pipeline; leaky orders in A, C, D |
| Q3 | MCQ (Single) | Easy | C | Yes — 9,800/10,000 = 98% when always predicting safe | SecureLogin login monitor; tests accuracy trap on skewed labels |
| Q4 | MCQ (Single) | Easy | A | Yes — high accuracy can hide failure to catch rare sick cases | Rare-disease screen stakeholder story |
| Q5 | MCQ (Single) | Moderate | A | Yes — precision 85/100 = 0.85; recall 51/60 = 0.85 | Factory defect TP/FP/FN counts verified arithmetically |
| Q6 | MCQ (Single) | Moderate | B | Yes — lower score after fixing leakage means a more honest estimate | Product-owner scenario; D correctly flagged as wrong (SMOTE on test) |
| Q7 | MSQ (Multiple) | Moderate | A, B, D | Yes — split first, train-only fit, real-time features are core guards | Distractor C is test-set tuning / leakage |
| Q8 | MSQ (Multiple) | Moderate | A, B, C | Yes — FP, FN, and TN definitions for fraud positive class | Distractor D swaps precision and recall meanings |
| Q9 | MSQ (Multiple) | Hard | A, B, C | Yes — SMOTE on train only, realistic test ratio, fair classification report | Distractor D leaks by SMOTE on train+test |
| Q10 | MSQ (Multiple) | Hard | A, B, D | Yes — averaging folds, stable band vs single lucky 0.95, reading spread | Distractor C overclaims CV replaces all final holdouts |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear? | Dataset Provided? | Remarks |
|---|---|---|---|---|---|
| Q1 | Practical Coding (single `.py` file) | Medium | Yes — Case C: single file, run verification, LMS code-box submission | Yes — inline `make_classification` bootstrap | Four-part task: split first, baseline report, SMOTE on train only, two comment lines on recall vs accuracy |

---

## Subjective Question — Detailed QC

### Code Logic Verification

| Step | Code / Logic Checked | Verdict |
|---|---|---|
| Imbalanced data | `make_classification` with `weights=[0.99, 0.01]`, `random_state=42` | ✅ No issues |
| Split first | `train_test_split` before SMOTE | ✅ No issues |
| Baseline | `LogisticRegression` on imbalanced train; `classification_report` on test | ✅ No issues |
| SMOTE scope | `fit_resample` on training only; test never resampled | ✅ No issues |
| Reference run | Baseline recall class `1` = 0.0; SMOTE recall class `1` = 1.0 on same split | ✅ Verified locally |
| Alternatives | Other classifiers acceptable if split/SMOTE-on-train-only discipline kept | ✅ No issues |

### Presentation Issues Found & Fixed

| Issue | Location | Fix Applied |
|---|---|---|
| Subjective task too long (scaling, confusion matrices, three comments) | Subjective assignment | Simplified to 4 parts, classification reports only, two comment lines |

---

## Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Leakage definition/guards, split-first scaling, imbalance, accuracy trap, precision/recall, SMOTE practice, cross-validation concept |
| Creativity | 5 | NovaBank, SecureLogin, PayGuard, factory QC, and clinic-style scenarios without session-reference phrasing |
| Structural Adherence | 5 | 10 questions: 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard); progressive difficulty; full answer explanations |
| No Logical Mistakes | True | Q5 arithmetic and Q3 accuracy checked; distractors map to common misconceptions |
| No Presentation Mistakes | True | Self-contained prompts; grammatically clean; no “as taught in session” wording |

### Subjective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Split-first, imbalanced baseline vs SMOTE, classification report, recall vs accuracy insight |
| Creativity | 5 | Bank fraud pilot scenario; mirrors lecture demo without extra scaling steps |
| Structural Adherence | 5 | One medium coding task with Case C submission and complete answer explanation |
| No Logical Mistakes | True | Pipeline order and test-set discipline verified by reference run |
| No Presentation Mistakes | True | Steps, seeds, sanity checks, and comment requirements are unambiguous |

---

## QC Summary

All criteria for both assignments meet the required standard:

- **Content Coverage:** 5 (objective and subjective)  
- **Creativity:** 5 (objective and subjective)  
- **Structural Adherence:** 5 (objective and subjective)  
- **No Logical Mistakes:** True  
- **No Presentation Mistakes:** True  

**Status:** Ready for Assess platform upload (enter each question’s answer explanation in the platform fields).
