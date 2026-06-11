# Assignment Question QC Report

## Objective + Subjective QC Table

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (metric comparison table definition) |
| Q2 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (accuracy vs F1 on imbalanced loan default) |
| Q3 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (99% train / 72% test = overfitting) |
| Q4 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (model persistence = train once, load anytime) |
| Q5 | MCQ (Moderate) | Correct option: B; relevancy to question: Yes (must save full pipeline / consistent preprocessing) |
| Q6 | MCQ (Moderate) | Correct option: B; relevancy to question: Yes (`model__n_estimators` GridSearchCV pipeline syntax) |
| Q7 | MSQ (Moderate) | Correct options: A, B, D; relevancy to question: Yes (fair comparison rules) |
| Q8 | MSQ (Moderate) | Correct options: A, B, D; relevancy to question: Yes (train–test gap / overfitting signals) |
| Q9 | MSQ (Hard) | Correct options: A, C, D; relevancy to question: Yes (selection checklist: small data, F1, interpretability) |
| Q10 | MSQ (Hard) | Correct options: A, C, D; relevancy to question: Yes (joblib pipeline persistence + security) |
| Q1 | Subjective (Medium) | Medium difficulty: Yes; clear submission instructions (case c, single `.py`): Yes; dataset requirement mentioned: Yes (`load_breast_cancer()` built-in, `random_state=42`) |

## Overall QC Ratings

| QC Parameter | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

## QC Outcome

All assignment files meet the expected quality threshold:

- **Structure:** 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard.
- **Scope:** Covers released notes — metric tables, accuracy vs F1, pipelines, overfitting gap, GridSearchCV syntax (objective only), model persistence, selection checklist, joblib security. Gradio omitted from subjective (surface-level deployment demo only).
- **Subjective:** CareScan tumour scenario — pipelines, metric table, train/test gap, start-simple 0.02 F1 rule, `joblib` save/load; medium difficulty, single-file submission (case c). Reference solution verified (`random_state=42` → Logistic Regression selected, prediction `1` on first test row).
- **Explanations:** Every objective question includes correct answer(s) and why distractors fail; subjective includes walkthrough, full code, alternatives, and grading notes.
- **Professional wording:** No “as taught in the session” phrasing in stems.
- **Ratings:** Content Coverage, Creativity, Structural Adherence all 5; no logical or presentation mistakes.

## Iteration 1 Notes

- Subjective reference code executed successfully; metrics match expected breast-cancer split behaviour.
- Q8 option C deliberately tests underfitting vs overfitting distinction — excluded from correct set by design.
- Q10 option E reverses joblib vs pickle recommendation — correctly marked incorrect.

**Expected result:** All criteria met — assignments ready for platform upload.
