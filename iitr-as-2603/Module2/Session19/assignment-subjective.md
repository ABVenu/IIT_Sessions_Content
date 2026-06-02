# Subjective Assignment - Medium Difficulty

## Practical Task: Model Comparison and Decision Memo

A student support team wants to identify students likely to **Pass** so they can plan mentorship outreach for students likely to **Fail**.  
Build and evaluate three classifiers - **Logistic Regression**, **Decision Tree**, and **Random Forest** - on a synthetic student dataset, then recommend one model using metric evidence.

### Requirements
1. Generate a dataset of at least 400 rows with the following features:
   - `study_hours` (float)
   - `sleep_hours` (float)
   - `distractions` (float)
   - target label `pass_fail` (0/1)
2. Split data into train and test (80/20) using a fixed random seed.
3. Train:
   - `LogisticRegression`
   - `DecisionTreeClassifier` (with controlled depth)
   - `RandomForestClassifier` (at least 100 trees)
4. For each model, report:
   - Confusion matrix values (TN, FP, FN, TP)
   - Accuracy
   - Precision
   - Recall
   - F1 score
   - ROC-AUC (must use predicted probabilities)
5. Print a final recommendation paragraph that:
   - picks one model,
   - justifies the choice using at least two metrics,
   - explains one trade-off (e.g., interpretability vs stability).

### Expected Output (minimum)
- Clearly printed metric summary for all three models
- One recommendation paragraph (4-6 lines)

### Submission Instruction
- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

### Answer Explanation (Reference Approach)

#### Step-by-step solution walkthrough
1. Use NumPy with a fixed seed to generate reproducible synthetic student features.
2. Create a target label `pass_fail` using a score formula and threshold (>= 70 as Pass).
3. Split into train and test sets using an 80/20 split.
4. Train `LogisticRegression`, `DecisionTreeClassifier`, and `RandomForestClassifier` on the same training set.
5. Compute confusion matrix, accuracy, precision, recall, F1, and ROC-AUC for each model.
6. Compare models and choose one model using metric evidence plus one practical trade-off.

#### Complete exact code (single-file reference solution)
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

# -----------------------------
# 1) Reproducible synthetic data
# -----------------------------
rng = np.random.default_rng(seed=7)
n = 500  # at least 400 rows

study_hours = rng.uniform(1, 10, size=n)
sleep_hours = rng.uniform(4, 9, size=n)
distractions = rng.uniform(0, 5, size=n)

# Score formula to create realistic signal + noise
scores = (
    40
    + 6.5 * study_hours
    + 1.2 * sleep_hours
    - 2.0 * distractions
    + rng.normal(0, 7, size=n)
)

pass_fail = (scores >= 70).astype(int)  # 1 = Pass, 0 = Fail

X = np.column_stack([study_hours, sleep_hours, distractions])
y = pass_fail

# ----------------------------------
# 2) Train-test split (80/20, fixed)
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# ---------------------------
# 3) Model initialization
# ---------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, max_depth=4, random_state=42
    ),
}


def evaluate_model(name, model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    metrics = {
        "TN": tn,
        "FP": fp,
        "FN": fn,
        "TP": tp,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, zero_division=0),
        "Recall": recall_score(y_test, y_pred, zero_division=0),
        "F1": f1_score(y_test, y_pred, zero_division=0),
        "ROC-AUC": roc_auc_score(y_test, y_prob),
    }

    print(f"\n{name}")
    print(f"Confusion Matrix -> TN={metrics['TN']} FP={metrics['FP']} FN={metrics['FN']} TP={metrics['TP']}")
    print(f"Accuracy : {metrics['Accuracy']:.3f}")
    print(f"Precision: {metrics['Precision']:.3f}")
    print(f"Recall   : {metrics['Recall']:.3f}")
    print(f"F1 Score : {metrics['F1']:.3f}")
    print(f"ROC-AUC  : {metrics['ROC-AUC']:.3f}")

    return metrics


# ---------------------------
# 4) Train + evaluate models
# ---------------------------
all_results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    all_results[model_name] = evaluate_model(model_name, model, X_test, y_test)

# ----------------------------------------------
# 5) Final recommendation paragraph (example)
# ----------------------------------------------
best_model_name = max(all_results, key=lambda k: all_results[k]["ROC-AUC"])
best_metrics = all_results[best_model_name]

print("\nRecommendation:")
print(
    f"{best_model_name} is recommended because it gives strong ranking quality "
    f"(ROC-AUC={best_metrics['ROC-AUC']:.3f}) and balanced positive-class performance "
    f"(F1={best_metrics['F1']:.3f}). "
    "Compared to a single Decision Tree, it is usually more stable on new data due to ensemble voting, "
    "though interpretability is lower than one shallow tree."
)
```

#### Notes for evaluation
- Any solution with equivalent logic, correct metric computation, and a valid evidence-based recommendation can be accepted.
- Hyperparameters can vary, but all required metrics and justification must be present.

