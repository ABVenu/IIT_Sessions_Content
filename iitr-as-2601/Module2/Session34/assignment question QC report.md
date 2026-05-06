# Assignment Question QC Report
## Session: ML Workshop — Model Selection & Comparison (Session 34)

---

## Objective Assignment QC

| Q# | Type | Correct Option(s) | Option Relevancy | Remarks |
|---|---|---|---|---|
| Q1 | MCQ (Easy) | C — Metric Comparison Table | Yes | Correct option directly names the concept defined in the session. All distractors (Confusion Matrix, Correlation Matrix, Feature Importance Plot) are real ML tools but serve different purposes — good distractors. |
| Q2 | MCQ (Easy) | D — joblib | Yes | Correct option matches the session's explicit statement that `joblib` is the officially recommended library for scikit-learn models. Distractors (`pickle`, `numpy`, `pandas`) are plausible but incorrect for this specific question. |
| Q3 | MCQ (Easy) | C — Overfitting | Yes | Correct option is directly supported by the session's definition: very high train accuracy + significantly lower test accuracy = overfitting. The 26.4% gap is an unmistakable example. Distractors test conceptual discrimination (Underfitting, Data Drift, Label Drift). |
| Q4 | MCQ (Easy) | C — Model Persistence | Yes | Correct option is the exact concept covered in the Model Persistence section. Distractors (Cross Validation, Hyperparameter Tuning, Model Monitoring) are distinct ML lifecycle concepts — no ambiguity. |
| Q5 | MCQ (Moderate) | C — Interpretability | Yes | Correct option maps precisely to Question 3 of the 6-Question Checklist ("Do you need to explain the model's decisions?"). The regulatory/legal scenario makes the answer unambiguous. |
| Q6 | MCQ (Moderate) | B — Max Depth = 5 | Yes | Correct option correctly identifies the sweet spot using the train-test gap table from the session's sample output. Tests reading and interpreting a results table — not just recall. Unlimited depth is a deliberate tempting distractor (perfect training score). |
| Q7 | MSQ (Moderate) | A, C, D | Yes | All three correct options are directly grounded in the session's "Saving the scaler is critical" note. Option B (ValueError) is the key misconception trap — scikit-learn silently runs without errors, making the mistake dangerous. |
| Q8 | MSQ (Moderate) | A, C, D | Yes | Correct options map to the three drift types covered in the session: Concept Drift (A), Data Drift (C), Label Drift (D). Option B (file deterioration) is the distractor testing whether learners confuse real degradation causes with a non-real one. |
| Q9 | MSQ (Hard) | A, D | Yes | Correct options (Logistic Regression, Shallow Decision Tree) are derived by systematically applying all three relevant checklist dimensions: problem type, data size (750 rows = small), and interpretability requirement. Options B and C fail on at least two of these. |
| Q10 | MSQ (Hard) | A, B, C, D | Yes | All four statements are mathematically verifiable from the given F1 scores. Tests precise calculation of the 2% threshold (0.9390 − 0.02 = 0.9190), understanding that 0.9185 < 0.9190 eliminates Logistic Regression, and that the loop selects the first qualifying model. |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Clear Submission Instructions | Dataset Required | Remarks |
|---|---|---|---|---|---|
| Q1 | Coding — Practical Pipeline | Medium | Yes — Case (c): Single `.py` file → submit code in LMS code editor | No external dataset — uses `load_breast_cancer()` from sklearn (built-in, no download needed) | Five-part structure covers all core session concepts: metric table, overfitting detection, complexity filter, `joblib` save, and persistence verification. Creative framing (MediScan hospital scenario) provides real-world context without increasing complexity. |

---

## Overall QC Ratings

### Objective Assignment

| Criteria | Rating (1–5) |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Content Coverage — 5/5:** All major session topics are covered — Metric Comparison Tables (Q1, Q6, Q10), Model Complexity & Overfitting (Q3, Q6), Model Persistence (Q2, Q4, Q7), Model Selection Checklist (Q5, Q9), Model Degradation / Monitoring (Q8), and Start Simple protocol (Q10). No topic is repeated superficially; each question tests a different facet.

**Creativity — 5/5:** Every question is framed in a practical, scenario-based context: fintech credit risk (Q1), hospital readmission (Q2), e-commerce churn (Q3), product recommendation (Q4), bank loan compliance (Q5), experimental results table (Q6), medical scaler mistake (Q7), payment gateway fraud model (Q8), sales startup churn (Q9), and F1-score filter calculation (Q10). Zero dry theoretical questions.

**Structural Adherence — 5/5:** Exactly 6 MCQs (4 Easy + 2 Moderate) and 4 MSQs (2 Moderate + 2 Hard). Questions ordered progressively Easy → Moderate → Hard. Every question has correct answer(s) stated and full answer explanations with reasoning for each option.

---

### Subjective Assignment

| Criteria | Rating (1–5) |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Content Coverage — 5/5:** The single question integrates all five coding-heavy concepts from the session: building a metric comparison table with a loop, detecting overfitting via the train-test gap, applying the 2% complexity filter programmatically, saving with `joblib`, and verifying persistence by reloading and predicting.

**Creativity — 5/5:** The MediScan Analytics / Tumour Risk Classifier scenario provides authentic context (matching the session's own breast cancer dataset usage), grounds every technical step in a real deployment motivation, and gives learners a sense of building something end-to-end — not just executing isolated code snippets.

**Structural Adherence — 5/5:** Exactly 1 subjective question at medium difficulty. Submission instructions clearly state Case (c): single `.py` file submitted via the LMS code editor. No external dataset is required — `load_breast_cancer()` is built-in to sklearn. Complete ideal solution with answer explanation provided for the platform's explanation field.

---

## QC Verdict

| Check | Result |
|---|---|
| All Content Coverage ratings ≥ 5 | ✅ Pass |
| All Creativity ratings ≥ 5 | ✅ Pass |
| All Structural Adherence ratings ≥ 5 | ✅ Pass |
| No Logical Mistakes | ✅ Pass |
| No Presentation Mistakes | ✅ Pass |

**Overall Result: APPROVED — All criteria meet the required standard. No revision needed.**
