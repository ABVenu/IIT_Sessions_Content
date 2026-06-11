# Objective Assignment - ML Workshop: Model Selection & Comparison

## Instructions
- Total questions: 10
- Question types: 6 MCQs (single correct), 4 MSQs (multiple correct)
- Difficulty progression: Easy → Moderate → Hard

---

## MCQs (Single Correct)

### Q1 (Easy)
A hospital data team trains **three tumour classifiers** and wants one table showing each model's **Accuracy, Precision, Recall, and F1** on the same test set. What is this table called?

A. Confusion matrix  
B. Metric comparison table  
C. Hyperparameter grid  
D. Pipeline manifest  

**Correct Answer:** B  
**Explanation:** A metric comparison table places multiple models and their scores side by side for fair evaluation. A confusion matrix (A) is per-model error breakdown, not a multi-model summary. A hyperparameter grid (C) lists tuning values. A pipeline manifest (D) is not a standard ML term for model scoring.

---

### Q2 (Easy)
A bank's loan-default model reports **78% accuracy**, but the **F1 score for the "default" class is 0%** — it never flags actual defaulters. What is the best next step for the risk team?

A. Deploy immediately because 78% accuracy is strong  
B. Prioritise **F1, Precision, and Recall** alongside accuracy before choosing a model  
C. Switch to regression because accuracy failed  
D. Remove the test set so accuracy improves  

**Correct Answer:** B  
**Explanation:** High accuracy can hide failure on the minority class that matters most. F1, precision, and recall reveal class-level performance. Deploying on accuracy alone (A) is risky. The problem is still classification (C is wrong). Removing the test set (D) is invalid evaluation.

---

### Q3 (Easy)
A fraud-detection model shows **99% train accuracy** and **72% test accuracy** on the same split. What is most likely happening?

A. Underfitting — the model is too simple  
B. Overfitting — the model memorised training noise  
C. Data leakage — test rows were copied into train  
D. Perfect generalisation — deploy with confidence  

**Correct Answer:** B  
**Explanation:** A large train–test gap with very high train score is a classic overfitting signal. Underfitting (A) shows low scores on both train and test. Leakage (C) is possible but the pattern described matches overfitting. 72% test with 99% train is not perfect generalisation (D).

---

### Q4 (Easy)
An ML engineer trains a model once on historical data, saves it to disk, and loads it weeks later for instant predictions without retraining. What concept does this describe?

A. Hyperparameter tuning  
B. Model persistence  
C. Cross-validation  
D. Feature engineering  

**Correct Answer:** B  
**Explanation:** Model persistence means saving a trained model (or pipeline) for later reuse — "train once, load anytime." Hyperparameter tuning (A) searches settings during training. Cross-validation (C) evaluates during training. Feature engineering (D) builds inputs, not save/load.

---

### Q5 (Moderate)
A developer trains a `Pipeline` with `StandardScaler` + `RandomForestClassifier`, but saves **only** the forest model with `joblib.dump(rf_model, ...)`. At inference, they call `rf_model.predict(raw_features)` without scaling. What is the most likely outcome?

A. Predictions stay correct because Random Forest ignores feature scale  
B. Predictions may be **wrong** because features are not scaled with the **same fitted scaler** used in training  
C. `joblib` automatically reloads the missing scaler from disk  
D. sklearn retrains the scaler inside `.predict()`  

**Correct Answer:** B  
**Explanation:** If training used scaled features, inference must apply the same transformation. Saving only the model drops that step. Trees are less scale-sensitive than logistic regression, but a pipeline trained on scaled data still expects scaled input — and the real issue is inconsistent preprocessing. joblib (C) and sklearn (D) do not auto-fix missing preprocessing.

---

### Q6 (Moderate)
You tune a `Pipeline` whose final step is named `"model"`. Which `param_grid` key correctly searches **`n_estimators`** inside that step?

A. `n_estimators`  
B. `model__n_estimators`  
C. `pipeline__n_estimators`  
D. `estimator__n_estimators`  

**Correct Answer:** B  
**Explanation:** GridSearchCV uses `stepname__parameter` for pipeline steps — here `model__n_estimators`. Bare `n_estimators` (A) does not target the nested step. `pipeline__` (C) and `estimator__` (D) are not valid step names in this setup.

---

## MSQs (Multiple Correct)

### Q7 (Moderate)
Three models compete on the **same patient dataset**. Which practices make the comparison **fair**?

A. Use the **same train/test split** for every model.  
B. Fit preprocessing (e.g. scaler) on **train only**, then transform test.  
C. Report each model on a **different random test split** to get variety.  
D. Place all models and metrics in **one side-by-side table**.  

**Correct Answers:** A, B, D  
**Explanation:** Fair comparison needs identical splits (A), identical preprocessing rules (B), and one readable table (D). Different test splits per model (C) make scores incomparable.

---

### Q8 (Moderate)
A decision tree shows **100% train accuracy** and **94% test accuracy**; a logistic model shows **97% train** and **97% test**. Which statements are **valid**?

A. The tree's **train–test gap** is a possible overfitting warning.  
B. The logistic model's **small gap** suggests more stable generalisation here.  
C. **100% train accuracy** always means the best model to deploy.  
D. You should compare **train and test together**, not train score alone.  

**Correct Answers:** A, B, D  
**Explanation:** Large gap + perfect train fits overfitting risk (A). Similar train/test scores suggest stability (B). Perfect train alone (C) can mean memorisation — not automatic best choice. Always read both splits (D).

---

### Q9 (Hard)
A **fintech startup** predicts **loan default (yes/no)** on **800 labelled rows**. Regulators require a **written reason** for every rejection. Which checklist decisions are **sound**?

A. Treat it as **binary classification** and start with **Logistic Regression** or a **shallow tree**.  
B. Jump straight to the largest **Random Forest** with no baseline table.  
C. Build a **metric table** and weigh **F1**, not accuracy alone.  
D. Favour **interpretable** models because auditors need rejection reasons.  
E. Use a **different train/test split** for each algorithm to explore more data.  

**Correct Answers:** A, C, D  
**Explanation:** Small labelled data + interpretability needs → simple classifiers first (A), F1-aware comparison (C), explainable choices (D). Skipping baselines (B) and varying splits (E) break fair comparison and good practice.

---

### Q10 (Hard)
A team is ready to ship a tuned **sklearn pipeline** to production. Which actions align with **safe, correct persistence**?

A. `joblib.dump(full_pipeline, 'model_v1.joblib')` — save scaler and model together.  
B. Load a `.joblib` file from an **unknown email attachment** without security review.  
C. Run **test predictions** on a small batch after `joblib.load()` before full rollout.  
D. Never load `.joblib` / `.pkl` files from **untrusted sources** — they can run malicious code.  
E. Prefer **pickle** over **joblib** for large sklearn models because sklearn recommends pickle.  

**Correct Answers:** A, C, D  
**Explanation:** Save the full fitted pipeline (A), sanity-check after load (C), treat serialized files as security-sensitive (D). Loading untrusted files (B) is dangerous. sklearn recommends **joblib** for models, not pickle as primary (E is false).

---
