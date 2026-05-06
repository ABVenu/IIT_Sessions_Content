# Subjective Assignment — ML Workshop: Model Selection & Comparison

**Total Questions:** 1 | **Practical Coding Task**

---

## Q1 — The Tumour Triage Pipeline: Build, Compare, Select & Preserve

You are an ML intern at **MediScan Analytics**, a company that builds decision-support tools for hospitals. Your team has been asked to produce a production-ready artefact for the **Tumour Risk Classifier** — a tool that predicts whether a tumour is malignant or benign based on diagnostic measurements taken from cell samples.

Before the model can be handed to the application engineering team (who will wrap it in a Gradio interface for doctors to use), your manager needs you to complete the full model evaluation, selection, and persistence pipeline — across five structured parts.

---

### Part 1 — Build a Metric Comparison Table

Train the following three models on the **`load_breast_cancer()`** dataset from sklearn. Use `test_size=0.2` and `random_state=42` for the train-test split. Apply `StandardScaler` to features (fit only on training data, then transform both sets).

| Model | Parameters |
|---|---|
| Logistic Regression | `max_iter=1000` |
| Decision Tree | `max_depth=5`, `random_state=42` |
| Random Forest | `n_estimators=100`, `random_state=42` |

Display a metric comparison table (as a `pd.DataFrame`) showing **Accuracy, Precision, Recall, and F1-Score** for all three models side by side. Set `"Model"` as the row index.

---

### Part 2 — Overfitting Check on the Decision Tree

For the **Decision Tree model only**, compute and print:
- Training Accuracy
- Test Accuracy
- Train-Test Gap (Train Accuracy − Test Accuracy)

Based on the gap value, print a one-line diagnostic:
- If gap > 0.05 → print `"⚠ Overfitting detected — gap exceeds 5%"`
- If training accuracy < 0.85 → print `"⚠ Underfitting detected — training accuracy too low"`
- Otherwise → print `"✓ Model is at the sweet spot — acceptable gap"`

---

### Part 3 — Apply the "Start Simple, Go Complex" Protocol

Using the **2% F1-Score complexity filter**, programmatically identify and print the selected model.

Requirements:
- Define your models dictionary in order **from simplest to most complex** (Logistic Regression → Decision Tree → Random Forest)
- Compute F1-Score for each model on the test set
- Find the best F1-Score across all models
- Iterate simplest-to-most-complex: select the **first** model whose F1-Score is within 2 percentage points of the best
- Print: `"Selected Model: <model_name> | F1-Score: <score>"`

---

### Part 4 — Save the Selected Model

Use `joblib` to save both of the following to disk:
- The **selected model** as `tumour_classifier_v1.joblib`
- The **fitted StandardScaler** as `tumour_scaler_v1.joblib`

Print a confirmation message after each save:
```
✓ Model saved as tumour_classifier_v1.joblib
✓ Scaler saved as tumour_scaler_v1.joblib
```

---

### Part 5 — Verify Model Persistence

Load both saved files back from disk using `joblib.load()`. Apply the loaded scaler to transform `X_test`, then run `model.predict()` using the loaded model.

Print the **first 10 predictions alongside their actual labels** in a readable format, for example:

```
Predictions vs Actual (first 10):
Predicted: [1 0 0 1 1 0 0 0 1 1]
Actual:    [1 0 0 1 1 0 0 0 1 1]
```

If the two rows match, the pipeline has been verified successfully end-to-end.

---

### Submission Instructions

- Code all five parts in VS Code in a **single `.py` file** named `tumour_pipeline.py`
- Run the code and verify it executes successfully — all five parts should produce visible output in the terminal
- Then **submit the code in the code editor / answer box in the LMS**

---

### Answer Explanation (for platform entry)

**Ideal solution walkthrough:**

```python
# ============================================================
# Tumour Triage Pipeline — Model Selection & Persistence
# ============================================================

import pandas as pd
import numpy as np
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ---- Load dataset and split ----
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Scale features ----
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ============================================================
# Part 1 — Metric Comparison Table
# ============================================================
models_dict = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree":       DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42)
}

table_results = []
trained_models = {}
for name, model in models_dict.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    trained_models[name] = model
    table_results.append({
        "Model":     name,
        "Accuracy":  round(accuracy_score(y_test, y_pred),  4),
        "Precision": round(precision_score(y_test, y_pred), 4),
        "Recall":    round(recall_score(y_test, y_pred),    4),
        "F1-Score":  round(f1_score(y_test, y_pred),        4)
    })

comparison_df = pd.DataFrame(table_results).set_index("Model")
print("=== Part 1: Metric Comparison Table ===")
print(comparison_df)
print()

# ============================================================
# Part 2 — Overfitting Check on Decision Tree
# ============================================================
dt_model   = trained_models["Decision Tree"]
train_acc  = accuracy_score(y_train, dt_model.predict(X_train))
test_acc   = accuracy_score(y_test,  dt_model.predict(X_test))
gap        = round(train_acc - test_acc, 4)

print("=== Part 2: Overfitting Check — Decision Tree ===")
print(f"Train Accuracy : {train_acc:.4f}")
print(f"Test Accuracy  : {test_acc:.4f}")
print(f"Train-Test Gap : {gap:.4f}")

if gap > 0.05:
    print("⚠ Overfitting detected — gap exceeds 5%")
elif train_acc < 0.85:
    print("⚠ Underfitting detected — training accuracy too low")
else:
    print("✓ Model is at the sweet spot — acceptable gap")
print()

# ============================================================
# Part 3 — "Start Simple, Go Complex" — 2% F1-Score Filter
# ============================================================
f1_results = {}
for name, model in trained_models.items():
    f1 = f1_score(y_test, model.predict(X_test))
    f1_results[name] = {"model_object": model, "F1-Score": round(f1, 4)}

best_f1       = max(v["F1-Score"] for v in f1_results.values())
selected_name = None
for name, info in f1_results.items():
    if best_f1 - info["F1-Score"] <= 0.02:
        selected_name = name
        break

print("=== Part 3: Complexity Filter ===")
print(f"Best F1-Score : {best_f1}")
print(f"Selected Model: {selected_name} | F1-Score: {f1_results[selected_name]['F1-Score']}")
print()

# ============================================================
# Part 4 — Save Selected Model and Scaler
# ============================================================
selected_model = f1_results[selected_name]["model_object"]
joblib.dump(selected_model, "tumour_classifier_v1.joblib")
print("✓ Model saved as tumour_classifier_v1.joblib")
joblib.dump(scaler, "tumour_scaler_v1.joblib")
print("✓ Scaler saved as tumour_scaler_v1.joblib")
print()

# ============================================================
# Part 5 — Verify Model Persistence
# ============================================================
loaded_model  = joblib.load("tumour_classifier_v1.joblib")
loaded_scaler = joblib.load("tumour_scaler_v1.joblib")

X_test_original = data.data[train_test_split(
    np.arange(len(data.data)), test_size=0.2, random_state=42
)[1]]
X_test_scaled  = loaded_scaler.transform(X_test_original)
predictions    = loaded_model.predict(X_test_scaled)
actual_labels  = y_test

print("=== Part 5: Persistence Verification ===")
print("Predictions vs Actual (first 10):")
print(f"Predicted: {predictions[:10]}")
print(f"Actual:    {actual_labels[:10]}")
```

**Key points in the solution:**
- `scaler.fit_transform(X_train)` fits AND transforms training data in one step; `scaler.transform(X_test)` only transforms (never fits on test data).
- The models dictionary is ordered simplest → most complex so the 2% filter loop selects the simplest qualifying model first.
- `joblib.dump` serialises both the model and the scaler; `joblib.load` reconstructs them exactly.
- In Part 5, the loaded scaler must be applied before calling `predict()` — using the loaded scaler (not a new one) guarantees the same scaling transformation used during training.

**Alternative approaches:**
- `pickle` could be used in place of `joblib`, but `joblib` is preferred for sklearn models.
- `precision_score` and `recall_score` default to binary averaging, which is appropriate for this binary classification dataset.
- Descriptive filenames like `tumour_classifier_v1.joblib` follow the versioning best practice covered in the session.
