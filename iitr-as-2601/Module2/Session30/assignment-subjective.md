# Subjective Assignment — Classification: Logistic Regression Fundamentals

## Problem Statement

You are a data analyst at **EduTrack**, an ed-tech company that wants to predict whether a student will **pass or fail** their final exam based on their study habits. Your goal is to build a Logistic Regression classifier, inspect its probability outputs, and evaluate it using a confusion matrix.

---

## Dataset

Generate your dataset inside your script using the following exact specification:

```python
import numpy as np
from numpy.random import default_rng

rng = default_rng(seed=99)
n = 500

study_hours        = rng.uniform(1, 10, size=n)       # daily study hours
attendance_percent = rng.uniform(40, 100, size=n)     # class attendance %
assignments_done   = rng.uniform(0, 10, size=n)       # assignments submitted (out of 10)

scores = (
    20
    + 5.5  * study_hours
    + 0.4  * attendance_percent
    + 3.0  * assignments_done
    + rng.normal(0, 8, size=n)
)

# Label: 1 = Pass, 0 = Fail
y = (scores >= 70).astype(int)
X = np.column_stack([study_hours, attendance_percent, assignments_done])
```

---

## Tasks

Complete all four tasks in a **single `.py` file**.

### Task 1 — Train a Logistic Regression model

- Split the dataset: **80% training, 20% testing** (`random_state=99`).
- Train a `LogisticRegression()` model (default settings).
- Print the **class distribution** of the full dataset — how many students Pass and how many Fail.

### Task 2 — Predict and display results

- Use `model.predict()` to get class labels for the test set.
- Use `model.predict_proba()` to get probabilities.
- Print a table for the **first 10 test students** with these columns:
  `# | Study Hrs | Attendance % | Assignments | Actual | Predicted | P(Pass) | Correct?`

### Task 3 — Evaluate with the confusion matrix

- Compute the confusion matrix using `confusion_matrix(y_test, y_pred)`.
- Extract and print **TP, TN, FP, FN** individually with clear labels.
- Compute and print **Accuracy** manually using the formula: `(TP + TN) / (TP + TN + FP + FN)`.

### Task 4 — Compare two decision thresholds

The EduTrack team wants to see how the model behaves at a **stricter threshold of 0.6** versus the default 0.5.

- Extract `P(Pass)` for all test students using `model.predict_proba(X_test)[:, 1]`.
- Apply both thresholds manually (without calling `model.predict()` again).
- For **each** threshold, print:
  - Number of students predicted as **Pass**
  - Number of students predicted as **Fail**
  - Overall **Accuracy**

---

## Submission Instructions

1. Open **Visual Studio Code**, create your Python file (e.g. `student_pass_predictor.py`), and install dependencies if needed (`pip install scikit-learn numpy`).
2. Run the script end-to-end until it produces output with no errors.
3. Copy your **complete Python code** and paste it into the answer box on the assessment platform.
4. At the top of your code (as comments), include:
   - Your Python version
   - The `pip install` command(s) used
   - How to run the file (e.g. `python student_pass_predictor.py`)

---

## Reference Solution

```python
# Python 3.10+ recommended
# pip install scikit-learn numpy
# Run: python student_pass_predictor.py

import numpy as np
from numpy.random import default_rng
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# ── Dataset generation ───────────────────────────────────────────────────────
rng = default_rng(seed=99)
n = 500

study_hours        = rng.uniform(1, 10, size=n)
attendance_percent = rng.uniform(40, 100, size=n)
assignments_done   = rng.uniform(0, 10, size=n)

scores = (
    20
    + 5.5  * study_hours
    + 0.4  * attendance_percent
    + 3.0  * assignments_done
    + rng.normal(0, 8, size=n)
)

y = (scores >= 70).astype(int)   # 1 = Pass, 0 = Fail
X = np.column_stack([study_hours, attendance_percent, assignments_done])

# ── Task 1: Class distribution and model training ────────────────────────────
unique, counts = np.unique(y, return_counts=True)
print("Class Distribution:")
for label, count in zip(unique, counts):
    print(f"  {'Pass' if label == 1 else 'Fail'} ({label}): {count} students")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=99
)

model = LogisticRegression()
model.fit(X_train, y_train)

# ── Task 2: Prediction table for first 10 test students ──────────────────────
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

print("\nFirst 10 Test Students:")
print(f"{'#':<4} {'Study':>6} {'Attend%':>8} {'Assign':>7} {'Actual':>7} {'Pred':>7} {'P(Pass)':>8} {'Correct?':>9}")
print("-" * 65)
for i in range(10):
    study  = X_test[i][0]
    attend = X_test[i][1]
    assign = X_test[i][2]
    actual = "Pass" if y_test[i] == 1 else "Fail"
    pred   = "Pass" if y_pred[i] == 1 else "Fail"
    p_pass = y_prob[i][1]
    ok     = "Yes" if y_test[i] == y_pred[i] else "No"
    print(f"{i+1:<4} {study:>6.1f} {attend:>8.1f} {assign:>7.1f} {actual:>7} {pred:>7} {p_pass:>8.2f} {ok:>9}")

# ── Task 3: Confusion matrix ─────────────────────────────────────────────────
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

print("\nConfusion Matrix (threshold = 0.5):")
print("=" * 50)
print(f"  True Positives  (TP) = {tp}  → Predicted Pass, Actually Pass")
print(f"  True Negatives  (TN) = {tn}  → Predicted Fail, Actually Fail")
print(f"  False Positives (FP) = {fp}  → Predicted Pass, Actually Fail")
print(f"  False Negatives (FN) = {fn}  → Predicted Fail, Actually Pass")
print("=" * 50)

accuracy_manual = (tp + tn) / (tp + tn + fp + fn)
print(f"  Accuracy: ({tp} + {tn}) / {tp + tn + fp + fn} = {round(accuracy_manual * 100, 1)}%")

# ── Task 4: Compare thresholds 0.5 vs 0.6 ───────────────────────────────────
p_pass_col = y_prob[:, 1]   # P(Pass) for all test students

print("\nThreshold Comparison:")
print("=" * 50)
for threshold in [0.5, 0.6]:
    y_pred_t = (p_pass_col >= threshold).astype(int)
    predicted_pass = y_pred_t.sum()
    predicted_fail = len(y_pred_t) - predicted_pass
    acc = accuracy_score(y_test, y_pred_t)
    print(f"\nThreshold = {threshold}:")
    print(f"  Predicted Pass : {predicted_pass} students")
    print(f"  Predicted Fail : {predicted_fail} students")
    print(f"  Accuracy       : {round(acc * 100, 1)}%")
```

**Notes for graders:** The seed and formula are fixed — outputs are deterministic. Key checks:
- Task 1: Pass and Fail counts printed.
- Task 2: table has all 8 required columns; P(Pass) uses `y_prob[i][1]`.
- Task 3: TP/TN/FP/FN extracted from `cm[0][0]..cm[1][1]`; accuracy computed manually without `accuracy_score`.
- Task 4: `[:, 1]` used to extract P(Pass); both thresholds compared with Pass count, Fail count, and accuracy printed for each.
