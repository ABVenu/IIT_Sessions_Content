# Subjective Assignment — Classification Models and Evaluation Metrics

---

## Practical Task: Build a Loan Default Detection System

### The Scenario

You are a junior data scientist at a non-banking financial company (NBFC). The risk management team wants you to build a classification model that predicts which loan applicants are likely to default. They want to understand how different models compare and whether adjusting the decision threshold can lead to better predictions than the default cut-off of 0.5.

Your task is to build a complete classification pipeline using the techniques from this session.

---

### What You Must Build

Using the synthetic dataset described below, complete the following steps in a single Python script or Jupyter Notebook:

#### Step 1 — Generate the Dataset

Create a dataset of **600 loan applicants** with the following features and seed `rng = np.random.default_rng(seed=42)`:

| Feature | Description | Range |
|---|---|---|
| `monthly_income` | Applicant's monthly income in ₹ thousands | 10 to 100 |
| `loan_amount` | Loan amount requested in ₹ thousands | 50 to 500 |
| `credit_score` | Applicant's credit score | 300 to 850 |
| `num_existing_loans` | Number of active loans the applicant already has | 0 to 5 (integers) |

Compute a **default risk score** using this formula:

```python
risk_score = (
    -0.05 * monthly_income
    + 0.008 * loan_amount
    - 0.012 * credit_score
    + 1.5 * num_existing_loans
    + rng.normal(0, 2, size=n)
)
```

Create the binary target: `will_default = 1` if `risk_score > 0`, else `0`.

Use an **80/20 train-test split** with `random_state=42`.

---

#### Step 2 — Train Both Models

Train the following two models on the training data:

1. **Decision Tree** — `max_depth=5`, `random_state=42`
2. **Random Forest** — `n_estimators=100`, `max_depth=5`, `random_state=42`

---

#### Step 3 — Evaluate Both Models

For each model, print:
- Accuracy, Precision, Recall, and F1 Score
- The Confusion Matrix (showing TN, FP, FN, TP)
- The AUC score (using probability outputs)

Present all results in a clean side-by-side comparison table.

---

#### Step 4 — Find the Best Threshold Using the Precision-Recall Curve

The default cut-off of 0.5 may not be the optimal decision boundary for this problem.

Using the **Random Forest model's probability outputs**:
- Use `precision_recall_curve` to compute Precision and Recall at every candidate threshold
- Compute the F1 Score at each threshold
- Find the **threshold that maximises F1 Score**
- Print the selected threshold, and the resulting Precision, Recall, and F1 Score

---

#### Step 5 — Compare Default vs Optimised Threshold

Print a comparison table showing Precision, Recall, and F1 Score at:
- The **default threshold (0.5)**
- The **F1-optimised threshold** found in Step 4

Conclude with one sentence stating whether the optimised threshold improved the F1 Score compared to the default.

---

### Submission Format

- Code in a `.py` file in VS Code or `.ipynb` notebook. 
- paste the code directly in the answer box
- Your code must be clean, runnable from top to bottom without errors, and produce all the outputs described above.

---

### Answer Explanation (Complete Solution)

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, roc_auc_score,
    precision_recall_curve
)

# ── Step 1: Generate Dataset ──────────────────────────────────────────────────
rng = np.random.default_rng(seed=42)
n = 600

monthly_income     = rng.uniform(10, 100, size=n)
loan_amount        = rng.uniform(50, 500, size=n)
credit_score       = rng.uniform(300, 850, size=n)
num_existing_loans = rng.integers(0, 6, size=n)   # integers 0 to 5 inclusive

risk_score = (
    -0.05 * monthly_income
    + 0.008 * loan_amount
    - 0.012 * credit_score
    + 1.5 * num_existing_loans
    + rng.normal(0, 2, size=n)
)

y = (risk_score > 0).astype(int)
X = np.column_stack([monthly_income, loan_amount, credit_score, num_existing_loans])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Dataset: {n} applicants | Default rate: {round(y.mean()*100, 1)}%")
print(f"Train size: {len(X_train)} | Test size: {len(X_test)}\n")

# ── Step 2: Train Both Models ─────────────────────────────────────────────────
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

y_prob_dt = dt.predict_proba(X_test)[:, 1]
y_prob_rf = rf.predict_proba(X_test)[:, 1]

# ── Step 3: Evaluate Both Models ──────────────────────────────────────────────
def evaluate(name, y_true, y_pred, y_prob):
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    acc  = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec  = recall_score(y_true, y_pred, zero_division=0)
    f1   = f1_score(y_true, y_pred, zero_division=0)
    auc  = roc_auc_score(y_true, y_prob)

    print(f"\n{'='*52}")
    print(f"  {name}")
    print(f"{'='*52}")
    print(f"  Confusion Matrix:  TN={tn}  FP={fp}  FN={fn}  TP={tp}")
    print(f"  Accuracy  : {round(acc*100, 1):>6}%")
    print(f"  Precision : {round(prec, 3):>6}")
    print(f"  Recall    : {round(rec, 3):>6}")
    print(f"  F1 Score  : {round(f1, 3):>6}")
    print(f"  AUC       : {round(auc, 3):>6}")

    return {"model": name, "Accuracy": round(acc,3), "Precision": round(prec,3),
            "Recall": round(rec,3), "F1": round(f1,3), "AUC": round(auc,3)}

results = [
    evaluate("Decision Tree (depth=5)", y_test, y_pred_dt, y_prob_dt),
    evaluate("Random Forest (100 trees)", y_test, y_pred_rf, y_prob_rf),
]

print(f"\n\n{'Comparison Table':^60}")
print(f"{'Model':<28} {'Acc':>6} {'Prec':>6} {'Rec':>6} {'F1':>6} {'AUC':>6}")
print("-" * 60)
for r in results:
    print(f"{r['model']:<28} {r['Accuracy']:>6} {r['Precision']:>6} {r['Recall']:>6} {r['F1']:>6} {r['AUC']:>6}")

# ── Step 4: Find the F1-Optimised Threshold ───────────────────────────────────
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob_rf)

# Compute F1 at every threshold; [:-1] aligns arrays with thresholds
f1_scores = (
    2 * precisions[:-1] * recalls[:-1]
    / (precisions[:-1] + recalls[:-1] + 1e-9)
)

best_idx       = f1_scores.argmax()
best_threshold = thresholds[best_idx]
best_precision = precisions[best_idx]
best_recall    = recalls[best_idx]
best_f1        = f1_scores[best_idx]

print(f"\n\nBest Threshold (Maximises F1 Score):")
print(f"  Threshold : {round(best_threshold, 3)}")
print(f"  Precision : {round(best_precision, 3)}")
print(f"  Recall    : {round(best_recall, 3)}")
print(f"  F1 Score  : {round(best_f1, 3)}")

# ── Step 5: Default vs Optimised Threshold ────────────────────────────────────
y_pred_default   = (y_prob_rf >= 0.5).astype(int)
y_pred_optimised = (y_prob_rf >= best_threshold).astype(int)

print(f"\n\nDefault (0.5) vs Optimised ({round(best_threshold, 3)}) Threshold:")
print(f"{'Metric':<12} {'Default (0.5)':>15} {'Optimised':>12}")
print("-" * 42)
for label, fn in [("Precision", precision_score), ("Recall", recall_score), ("F1 Score", f1_score)]:
    d = fn(y_test, y_pred_default,   zero_division=0)
    o = fn(y_test, y_pred_optimised, zero_division=0)
    print(f"{label:<12} {round(d, 3):>15} {round(o, 3):>12}")

# Conclusion
f1_default   = f1_score(y_test, y_pred_default,   zero_division=0)
f1_optimised = f1_score(y_test, y_pred_optimised, zero_division=0)
if f1_optimised > f1_default:
    print(f"\nConclusion: The optimised threshold improved F1 from "
          f"{round(f1_default, 3)} to {round(f1_optimised, 3)}.")
else:
    print(f"\nConclusion: The default threshold (0.5) already produces the best F1 on this dataset.")
```

#### Walkthrough of the Solution

**Dataset Design:** The risk score formula is calibrated so that high loan amounts, many existing loans, and low credit scores drive default risk up — mirroring real-world lending dynamics. The random noise (`rng.normal(0, 2)`) ensures the boundary between defaulters and non-defaulters is not perfectly sharp, making the classification problem realistic.

**Why Random Forest outperforms the Decision Tree here:** A single Decision Tree at `max_depth=5` can ask at most 5 questions in sequence. Random Forest trains 100 such trees, each seeing a different random sample of applicants and features — the collective majority vote smooths out individual tree errors and captures more complex interaction patterns between features.

**The threshold-finding logic:** `precision_recall_curve` returns Precision and Recall values at every unique probability score in `y_prob_rf`, automatically sweeping all candidate thresholds. Since the arrays returned have one extra entry, `[:-1]` is used to align them with the `thresholds` array before computing F1. `f1_scores.argmax()` then picks the index with the highest F1 — this is the mathematically optimal cut-off that balances Precision and Recall on the test set.

**Why the optimised threshold often beats 0.5:** The default threshold of 0.5 was not chosen by looking at the data — it is a convention. The actual probability distribution of `y_prob_rf` may be skewed depending on class imbalance and model calibration, meaning 0.5 may split the population sub-optimally. The F1-optimised threshold is found directly from the data, making it a better-informed cut-off.
