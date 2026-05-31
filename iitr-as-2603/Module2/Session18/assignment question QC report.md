# Assignment Question QC Report

## Session

Classification: Logistic Regression Fundamentals

---

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests regression vs classification using temperature and hiring scenarios. |
| 2 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests sigmoid as the probability mapping function in Logistic Regression. |
| 3 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests reading `predict_proba` columns and that probabilities sum to 1. |
| 4 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests default 0.5 decision threshold used by `predict()`. |
| 5 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests threshold 0.5 labelling for P(Pass) = 0.48 and 0.91. |
| 6 | Objective MCQ | Correct option: A. Relevancy: Yes. Tests why high accuracy can mislead when TP = 0 on imbalanced data. |
| 7 | Objective MSQ | Correct options: A, B, C. Relevancy: Yes. Tests lowering threshold effects on positives, FN, and FP. |
| 8 | Objective MSQ | Correct options: A, B, C, E. Relevancy: Yes. Tests TP, TN, FP, and FN definitions in a credit-default context. |
| 9 | Objective MSQ | Correct options: A, B, D. Relevancy: Yes. Tests Pipeline + scaler on train, held-out evaluation, and confusion matrix use. |
| 10 | Objective MSQ | Correct options: A, C, E. Relevancy: Yes. Tests `predict_proba` for multi-band business rules without retraining. |
| Subjective | Coding Implementation | Difficulty reduced to Easy. Correct option: N/A. Relevancy: Yes. Clear submission instructions: Yes (case c — single `.py` file). Dataset needed: No external dataset; fixed 16-row DataFrame with one feature. Covers `LogisticRegression`, `predict`, `predict_proba`, accuracy, and confusion matrix (no Pipeline or threshold loop). |

---

## Assignment-Level QC

| Criteria | Rating / Result | Remarks |
|---|---:|---|
| Content Coverage | 5 / 5 | Covers classification vs regression, sigmoid, `predict` vs `predict_proba`, default and custom thresholds, confusion matrix cells, pipeline with scaling, and threshold trade-offs aligned with session notes. |
| Creativity | 5 / 5 | Uses PayLite, EdTech routing, fraud, disease screening, hiring, and weather scenarios instead of direct recall-only prompts. |
| Structural Adherence | 5 / 5 | Objective: 10 questions (6 MCQs: 4 Easy + 2 Moderate; 4 MSQs: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: one easy coding task with case c submission instructions. |
| No Logical Mistakes | True | Correct options verified against sigmoid behaviour, sklearn defaults, confusion-matrix layout, and threshold FP/FN trade-offs. |
| No Presentation Mistakes | True | Standalone professional wording, complete answer explanations, consistent headings, and no session-reference phrases in questions. |

---

## QC Result

All criteria meet the expected result: ratings are 5 / 5, no logical mistakes are present, and no presentation mistakes are present. No modification is required.
