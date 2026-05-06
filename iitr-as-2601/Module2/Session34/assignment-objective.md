# Objective Assignment — ML Workshop: Model Selection & Comparison

**Total Questions:** 10 | **6 MCQs (Single Correct) + 4 MSQs (Multiple Correct)**

> Questions are ordered progressively: Easy → Moderate → Hard

---

## MCQ — Easy (4 Questions)

---

### Q1 (MCQ — Easy)

Priya, a data scientist at a fintech company, has just trained three models — Logistic Regression, Decision Tree, and Random Forest — to predict credit card defaults. Instead of checking each model's Accuracy, Precision, Recall, and F1-Score separately from different output cells, she wants to see all models and all metrics laid out in a single, clean, readable view.

What is the name of the structured tool she is building?

- A) Confusion Matrix
- B) Correlation Matrix
- C) Metric Comparison Table
- D) Feature Importance Plot

**Correct Answer:** C

**Answer Explanation:**
A **Metric Comparison Table** (also called a Model Comparison Table) is a DataFrame that displays the performance scores of multiple models across multiple evaluation metrics side by side — exactly what Priya needs. It is built by collecting one dictionary of results per model, converting the list into a `pd.DataFrame`, and calling `.set_index("Model")`.

- **A is wrong:** A Confusion Matrix shows correct vs. incorrect predictions for a *single* model only.
- **B is wrong:** A Correlation Matrix shows linear relationships *between features*, not model performance.
- **D is wrong:** A Feature Importance Plot ranks individual features by their predictive power in a single model — it does not compare multiple models.

---

### Q2 (MCQ — Easy)

An ML engineer at a hospital tech company spent 3 hours training a Random Forest model on 500,000 patient records to predict readmission risk. The model will be embedded into a hospital application where it must return predictions instantly whenever a nurse submits a patient record — without retraining from scratch each time.

Which Python library is **officially recommended by scikit-learn** for saving this model efficiently?

- A) pickle
- B) numpy
- C) pandas
- D) joblib

**Correct Answer:** D

**Answer Explanation:**
`joblib` is the officially recommended library for saving scikit-learn models. It is specially optimised for objects that contain large NumPy arrays internally — like Random Forests with hundreds of decision trees — making it faster and more memory-efficient than `pickle` for ML models. The saving syntax is simply `joblib.dump(model, 'filename.joblib')` and loading is `joblib.load('filename.joblib')`.

- **A is wrong:** `pickle` works for any Python object but is not optimised for large array-heavy ML models. The session explicitly recommends `joblib` over `pickle` for sklearn models.
- **B is wrong:** `numpy` is a numerical computing library — it cannot serialise and save ML model objects.
- **C is wrong:** `pandas` is a data manipulation library — it cannot save trained model objects.

---

### Q3 (MCQ — Easy)

A developer builds a Decision Tree classifier for an e-commerce customer churn prediction system. After training, he observes the following scores:

- **Training Accuracy:** 99.6%
- **Test Accuracy:** 73.2%

What problem does this clearly indicate?

- A) Underfitting — the model is too simple to learn real patterns
- B) Data Drift — the production data has changed over time
- C) Overfitting — the model has memorised the training data
- D) Label Drift — the definition of "churn" has changed

**Correct Answer:** C

**Answer Explanation:**
**Overfitting** is characterised by a very high training accuracy combined with a significantly lower test accuracy — a large Train-Test Gap. Here the gap is 99.6% − 73.2% = **26.4%**, which is a classic, unmistakable overfitting signal. The Decision Tree has grown deep enough to memorise every training point (including noise), but fails to generalise to new, unseen data.

- **A is wrong:** Underfitting shows *low accuracy on both* training and test data. A 99.6% training score rules out underfitting entirely.
- **B is wrong:** Data Drift is a post-deployment phenomenon where real-world input data shifts over time — it is not observed during the initial train/test evaluation.
- **D is wrong:** Label Drift refers to a change in the target variable's definition, which is again a post-deployment issue unrelated to the train-test gap.

---

### Q4 (MCQ — Easy)

After weeks of model experimentation, Aditya finalises his best Random Forest classifier for a product recommendation engine. The application server must serve recommendations to thousands of users per minute. Rather than retraining the model from scratch for each prediction request, Aditya writes `joblib.dump(model, 'recommender_rf_v1.joblib')` and hands the file to the application team.

Which core ML concept is Aditya practising?

- A) Cross Validation
- B) Hyperparameter Tuning
- C) Model Persistence
- D) Model Monitoring

**Correct Answer:** C

**Answer Explanation:**
**Model Persistence** is the process of saving a trained ML model to disk so it can be loaded and reused later — without needing to retrain. This is exactly what Aditya is doing: train once, save the result, and the application loads it for instant real-time predictions. The analogy from the session: it is like saving a game at Level 10 — you do not restart from Level 1 every time you play.

- **A is wrong:** Cross Validation is a technique for evaluating model performance reliably across multiple data folds — it is used during training evaluation, not saving.
- **B is wrong:** Hyperparameter Tuning is the process of searching for optimal model settings like `n_estimators` or `max_depth`.
- **D is wrong:** Model Monitoring is the ongoing tracking of a deployed model's accuracy in production to detect degradation over time.

---

## MCQ — Moderate (2 Questions)

---

### Q5 (MCQ — Moderate)

A regulatory compliance team at a national bank commissions a Loan Approval Model. The product manager delivers one non-negotiable requirement: *"Every rejection decision must be explainable in plain language — to the customer who was rejected and to the banking regulator. A black-box model is legally unacceptable."*

According to the **6-Question Model Selection Checklist**, which factor should be treated as the **primary constraint** when selecting a model for this use case?

- A) Dataset size — choose the model designed for the largest number of rows
- B) Training speed — choose the fastest model to reduce infrastructure costs
- C) Interpretability — choose a model whose decisions can be explained in simple language
- D) Non-linearity handling — choose a model that captures complex non-linear patterns

**Correct Answer:** C

**Answer Explanation:**
Question 3 of the Model Selection Checklist asks: *"Do you need to explain the model's decisions to a non-technical person?"* When the answer is **Yes** — as it is here due to legal and regulatory requirements — **Interpretability becomes the primary filter**. This immediately eliminates black-box models like Random Forest (Medium interpretability), Gradient Boosting (Low), and Neural Networks (Very Low).

The appropriate choices in this scenario are:
- **Logistic Regression** — Very High interpretability; each feature's coefficient shows its exact contribution to the decision.
- **Shallow Decision Tree (depth 3–7)** — High interpretability; generates human-readable if-then rules that a loan officer can walk a customer through.

Dataset size, training speed, and non-linearity handling are secondary considerations that come *after* the interpretability constraint has been satisfied.

---

### Q6 (MCQ — Moderate)

A data scientist runs a complexity experiment on a classification dataset, training three Decision Tree classifiers with different depth limits:

| Max Depth | Train Accuracy | Test Accuracy | Gap (Train − Test) |
|---|---|---|---|
| 1 | 0.9253 | 0.9123 | 0.0130 |
| 5 | 0.9714 | 0.9474 | 0.0240 |
| Unlimited | 1.0000 | 0.9035 | 0.0965 |

Which row represents the **"sweet spot"** — strong generalisation with an acceptable overfitting gap?

- A) Max Depth = 1, because it has the smallest train-test gap of all three
- B) Max Depth = 5, because it achieves the highest test accuracy with a small, acceptable gap
- C) Unlimited Depth, because it achieves a perfect training accuracy of 1.0000
- D) All three are equally valid — the choice depends on personal preference

**Correct Answer:** B

**Answer Explanation:**
**Max Depth = 5** is the sweet spot because it achieves the **highest test accuracy (0.9474)** with only a modest 0.0240 gap — strong generalisation without significant overfitting.

- **Max Depth = 1** underfits — the tree is too shallow to learn real patterns. Both train (0.9253) and test (0.9123) scores are moderate, and the small gap here is not a virtue; it simply reflects that neither score is good.
- **Unlimited Depth** overfits severely — perfect 1.0000 training accuracy but test accuracy actually *drops* to 0.9035. The 0.0965 gap (nearly 10%) is a clear red flag. The model has memorised every training point including noise.
- **The rule:** Never judge a model by its training score alone. The sweet spot is where test accuracy peaks before the gap becomes problematic — not the extreme (shallowest or deepest).

---

## MSQ — Moderate (2 Questions)

---

### Q7 (MSQ — Moderate)

Meera trains a Logistic Regression model using `StandardScaler` to normalise her features before fitting. She saves only the trained model: `joblib.dump(lr_model, 'lr_model.joblib')` — but **forgets to save the scaler**. Six months later, a colleague loads the model and passes **raw, unscaled** test data directly to `loaded_model.predict(X_test_raw)`.

Which of the following are **correct consequences** of this mistake? *(Select all that apply)*

- A) The model receives feature values on completely different scales than it was trained on, causing incorrect predictions
- B) Scikit-learn will immediately raise a `ValueError` and refuse to run `predict()`
- C) The model silently produces wrong predictions without raising any error or warning
- D) The correct practice is to always save and load the fitted scaler alongside the model

**Correct Answers:** A, C, D

**Answer Explanation:**

- **A is correct:** `StandardScaler` was fitted on training data to produce zero mean and unit variance. If raw unscaled data is passed (e.g., a feature like "tumour area" with values in the hundreds), the model receives inputs in a completely different distribution from what it learned on — causing its coefficients to produce incorrect predictions.
- **B is incorrect:** Scikit-learn's `predict()` has **no mechanism to detect** that input data was not scaled. It performs the matrix multiplication regardless, making no complaint. This silent failure is what makes the mistake so dangerous.
- **C is correct:** This is the most critical risk — the model runs without errors but outputs meaningless or dangerously wrong predictions. In a medical context, this could mean wrong diagnoses.
- **D is correct:** The rule from the session: *"Always save preprocessing objects alongside the model."* The correct pattern is `joblib.dump(scaler, 'scaler.joblib')` paired with `joblib.dump(model, 'model.joblib')`. Both must be loaded and used in sequence.

---

### Q8 (MSQ — Moderate)

A fraud detection model was deployed at a payment gateway in 2023 and initially achieved 94% accuracy. By early 2026, accuracy has dropped to 77%. The engineering team investigates the root cause of performance degradation.

Which of the following could be **valid reasons** for this accuracy drop? *(Select all that apply)*

- A) Fraudsters have adopted entirely new attack patterns (e.g., AI-generated synthetic identities) that were not present in the 2023 training data
- B) The `.joblib` model file has physically deteriorated on the server's storage drive over time
- C) Average transaction amounts have increased significantly due to inflation, shifting the feature distribution away from training data
- D) The company's compliance team redefined which transaction categories are legally classified as "fraudulent"

**Correct Answers:** A, C, D

**Answer Explanation:**

- **A is correct:** This is **Concept Drift** — the underlying relationship between features (transaction patterns) and the label (fraud) has changed because fraudsters evolved their tactics. The model never saw these new patterns during training and cannot recognise them.
- **B is incorrect:** `.joblib` files are binary files stored on disk — they do not "deteriorate" over time. A file either loads correctly or is corrupted by a specific event (disk failure, file tampering). Normal age does not degrade a saved model file.
- **C is correct:** This is **Data Drift** — the distribution of the input feature (transaction amount) has shifted. The model was trained on 2023 transaction amounts; 2026 amounts look significantly different due to inflation, so the model's learned thresholds are no longer appropriate.
- **D is correct:** This is **Label Drift** — the definition of the target variable itself has changed. The model was trained on the old definition of "fraud"; new compliance rules mean some transactions it learned as "not fraud" are now classified as fraud (and vice versa).

---

## MSQ — Hard (2 Questions)

---

### Q9 (MSQ — Hard)

A startup's ML team is building a customer churn predictor for their sales platform. The full business context is:

- **Dataset:** 750 labelled customer records (historical churn data)
- **Task:** Binary classification — Will the customer churn? (Yes / No)
- **Business Constraint:** The regional sales managers must present churn reasons to clients in plain language during review meetings — every prediction must be explainable

Applying the **6-Question Model Selection Checklist** systematically, which models are **appropriate choices** for this use case? *(Select all that apply)*

- A) Logistic Regression
- B) Gradient Boosting (e.g., XGBoost)
- C) Neural Network (Deep Learning)
- D) Shallow Decision Tree (max_depth = 3–7)

**Correct Answers:** A, D

**Answer Explanation:**

Systematically applying the checklist:

1. **Problem Type:** Binary Classification → candidates are Logistic Regression, Decision Tree, Random Forest, SVM.
2. **Data Size:** 750 rows = **Small dataset** → prefer Logistic Regression, SVM, shallow Decision Tree. Complex models like Random Forest and Gradient Boosting need much more data to generalise — on 750 rows, they are likely to overfit.
3. **Interpretability:** **Required** (sales managers must explain decisions) → eliminates any black-box model.

Evaluating each option:
- **A (Logistic Regression):** ✅ Very Low complexity, **Very High interpretability**, works reliably on small datasets. Each feature's coefficient directly quantifies its influence on churn probability — highly explainable.
- **B (Gradient Boosting):** ❌ Very High complexity, **Low interpretability**, requires large datasets to avoid overfitting. Fails on both the data size and interpretability criteria.
- **C (Neural Network):** ❌ Highest complexity, **Very Low interpretability** (complete black box), requires large datasets. Fails all three relevant criteria.
- **D (Shallow Decision Tree):** ✅ Medium complexity, **High interpretability** — generates human-readable if-then rules (e.g., "If tenure < 12 months AND support_tickets > 3 → Churn"). Perfect for a sales team presentation.

---

### Q10 (MSQ — Hard)

A data scientist applies the **"Start Simple, Go Complex" protocol** on a classification problem. After training three models (added to the results dictionary in order from simplest to most complex), the F1-Scores are:

| Model | F1-Score |
|---|---|
| Logistic Regression | 0.9185 |
| Decision Tree | 0.9340 |
| Random Forest | 0.9390 |

She now applies the **2% complexity filter** — the code logic is:
```python
best_f1 = max(v["F1-Score"] for v in results.values())
for name, info in results.items():   # iterates simplest → most complex
    if best_f1 - info["F1-Score"] <= 0.02:
        selected_name = name
        break
```

Which of the following statements are **correct**? *(Select all that apply)*

- A) The best F1-Score is 0.9390, so the 2% threshold cutoff is 0.9190
- B) Logistic Regression (F1 = 0.9185) does **not** qualify because it falls just below the 0.9190 cutoff
- C) Decision Tree (F1 = 0.9340) qualifies under the 2% filter
- D) Decision Tree would be selected as the final model because it is the simplest qualifying model in the iteration order

**Correct Answers:** A, B, C, D

**Answer Explanation:**

Working through the filter logic step by step:

- **A is correct:** `best_f1 = 0.9390`. The cutoff = `0.9390 − 0.02 = 0.9190`. Any model scoring **≥ 0.9190** qualifies as "within 2% of the best."
- **B is correct:** Logistic Regression scores 0.9185. Since 0.9185 < 0.9190, `best_f1 - 0.9185 = 0.0205 > 0.02` — the condition `<= 0.02` is **False**. Logistic Regression does NOT qualify. (It misses by just 0.0005, but the filter is strict.)
- **C is correct:** Decision Tree scores 0.9340. Since 0.9340 ≥ 0.9190, `best_f1 - 0.9340 = 0.0050 ≤ 0.02` — the condition is **True**. Decision Tree qualifies.
- **D is correct:** The loop iterates in insertion order (simplest → most complex). Logistic Regression is checked first — it fails. Decision Tree is checked second — it passes and the loop `break`s immediately. Decision Tree is selected. The loop never even evaluates Random Forest, because we stop at the first qualifying (simplest) model.

**The key insight:** The purpose of this filter is to avoid the *unnecessary* complexity and maintenance cost of a more complex model when a simpler one is nearly as good. Here, Decision Tree achieves 0.9340 vs. Random Forest's 0.9390 — a gap of just 0.5% — making the added complexity of Random Forest unjustifiable.
