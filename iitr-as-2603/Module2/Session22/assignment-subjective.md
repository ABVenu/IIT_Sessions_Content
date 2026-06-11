# Subjective Assignment - Medium Difficulty

## Practical Task: CareScan Tumour Model Selection & Handover

**CareScan** is a diagnostics startup building a **benign vs malignant tumour** classifier. The ML lead wants a reproducible workflow: compare three candidates fairly, check for overfitting, pick a winner using the **start-simple rule**, and **persist** the chosen pipeline so the inference team can load it without retraining.

Use the built-in **`load_breast_cancer()`** dataset from sklearn (569 rows, 30 features, binary target). No external CSV is required.

### Requirements

1. **Data split (reproducible):**
   - Load features `X` and target `y` from `load_breast_cancer()`.
   - `train_test_split(X, y, test_size=0.2, random_state=42)`.

2. **Build three sklearn `Pipeline` objects** (each with `StandardScaler` + model):
   - **Logistic Regression (Simple):** `LogisticRegression(max_iter=1000)`
   - **Decision Tree (Medium):** `DecisionTreeClassifier(random_state=42)` — no `max_depth` limit
   - **Random Forest (Complex):** `RandomForestClassifier(n_estimators=100, random_state=42)`

3. **Metric comparison table (test set):**
   - Train each pipeline on `X_train, y_train`.
   - For each model, compute **test Accuracy** and **test F1** (use `f1_score` with default settings).
   - Print a pandas DataFrame with columns: `Model`, `Test_Accuracy`, `Test_F1` (round to 4 decimals).

4. **Overfitting check:**
   - For each pipeline, also compute **train accuracy** and **test accuracy**.
   - Print one line per model: `Model: train_acc=..., test_acc=..., gap=...` where `gap = train_acc - test_acc` (4 decimals).

5. **Start-simple selection rule:**
   - Find the **best test F1** across the three models.
   - Select the **first model in this order** whose test F1 is within **0.02** of the best:  
     `Logistic Regression (Simple)` → `Decision Tree (Medium)` → `Random Forest (Complex)`.
   - Print: `Selected model: <name>`.

6. **Model persistence:**
   - `joblib.dump(selected_pipeline, 'carescan_selected_pipeline.joblib')`
   - Load it back with `joblib.load(...)`.
   - Predict on **`X_test[0:1]`** (first test row) using the loaded pipeline.
   - Print: `Loaded pipeline prediction for first test row: <value>`

### Expected Output (minimum)

```
   Model  Test_Accuracy  Test_F1
0  ...

Logistic Regression (Simple): train_acc=..., test_acc=..., gap=...
Decision Tree (Medium): train_acc=..., test_acc=..., gap=...
Random Forest (Complex): train_acc=..., test_acc=..., gap=...

Selected model: ...

Loaded pipeline prediction for first test row: ...
```

### Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

### Answer Explanation (Reference Approach)

#### Step-by-step solution walkthrough

1. Load breast cancer data and split with `random_state=42` for reproducibility.
2. Define three pipelines so preprocessing is identical and bundled with each model.
3. Fit each pipeline, score test Accuracy and F1, build a comparison DataFrame.
4. Compute train vs test accuracy and gap to surface overfitting (Decision Tree often shows the largest gap here).
5. Apply the start-simple rule: pick the first model in simple → complex order within 0.02 of best F1 (typically **Logistic Regression** on this split).
6. Save the winning pipeline with `joblib`, reload, and predict one test row to prove persistence works.

#### Complete exact code (single-file reference solution)

```python
import joblib
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# 1) Load data and split
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2) Three pipelines — simple → complex
model_order = [
    ("Logistic Regression (Simple)", LogisticRegression(max_iter=1000)),
    ("Decision Tree (Medium)", DecisionTreeClassifier(random_state=42)),
    ("Random Forest (Complex)", RandomForestClassifier(n_estimators=100, random_state=42)),
]

pipelines = {}
for name, estimator in model_order:
    pipelines[name] = Pipeline([
        ("scaler", StandardScaler()),
        ("model", estimator),
    ])

# 3) Metric comparison table (test set)
rows = []
for name, pipe in pipelines.items():
    pipe.fit(X_train, y_train)
    y_test_pred = pipe.predict(X_test)
    rows.append({
        "Model": name,
        "Test_Accuracy": round(accuracy_score(y_test, y_test_pred), 4),
        "Test_F1": round(f1_score(y_test, y_test_pred), 4),
    })

comparison_df = pd.DataFrame(rows)
print(comparison_df.to_string(index=False))

# 4) Overfitting check — train vs test gap
for name, pipe in pipelines.items():
    train_acc = accuracy_score(y_train, pipe.predict(X_train))
    test_acc = accuracy_score(y_test, pipe.predict(X_test))
    gap = train_acc - test_acc
    print(
        f"{name}: train_acc={train_acc:.4f}, test_acc={test_acc:.4f}, gap={gap:.4f}"
    )

# 5) Start-simple selection rule
best_f1 = comparison_df["Test_F1"].max()
selected_name = None
selected_pipeline = None
for name, _ in model_order:
    f1 = comparison_df.loc[comparison_df["Model"] == name, "Test_F1"].iloc[0]
    if best_f1 - f1 <= 0.02:
        selected_name = name
        selected_pipeline = pipelines[name]
        break

print(f"Selected model: {selected_name}")

# 6) Persist, reload, predict one test row
joblib.dump(selected_pipeline, "carescan_selected_pipeline.joblib")
loaded_pipeline = joblib.load("carescan_selected_pipeline.joblib")
prediction = loaded_pipeline.predict(X_test[0:1])
print(f"Loaded pipeline prediction for first test row: {prediction[0]}")
```

#### Alternative approaches

- The comparison table may use `.set_index("Model")` or `print(comparison_df)` — formatting may vary slightly.
- `f1_score(..., zero_division=0)` is acceptable if a model fails on a class; not expected on this dataset.
- A short comment block explaining why the selected model's gap is smaller than the tree's is good practice but not required for full credit.

#### Notes for evaluation

- Full credit requires: three pipelines, metric table, train/test gap lines, start-simple rule in correct order, `joblib` save + load + single-row predict.
- Penalise: fitting scaler on full data before split, saving only the model without the pipeline, or skipping the 0.02 selection rule.
- With `random_state=42`, expected selection is typically **Logistic Regression (Simple)**; other winners only if the student changes data or seed and still applies the rule correctly.
