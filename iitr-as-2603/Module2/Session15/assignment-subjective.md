# Assignment: Subjective — Session 15: Leakage & Imbalance

**Total Questions: 1 | Format: Practical Coding Task | Difficulty: Medium**

---

## Question 1 — Spot the Fraud: Baseline vs SMOTE

**Scenario**

A bank’s pilot fraud dataset is **heavily imbalanced** — almost every row is “not fraud.” You will use a small synthetic dataset, **split first**, train a simple model **without** balancing, then train the same model after **SMOTE on training data only**, and compare the results on the **same test set**.

---

### Your task

Write **one** Python file: `fraud_compare.py` with the four parts below.

Use these settings everywhere: `random_state=42`, `test_size=0.2`, `LogisticRegression(max_iter=500)`.

#### Part 1 — Create data and split first

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=1000,
    n_features=4,
    weights=[0.99, 0.01],
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Print: `Train size:` and `Test size:` (number of rows).

#### Part 2 — Baseline model (no SMOTE)

Train logistic regression on `X_train`, `y_train`. Predict on `X_test`.

Print:

```text
--- Baseline ---
```

then `classification_report(y_test, y_pred)` (from `sklearn.metrics`).

#### Part 3 — Same model after SMOTE on training only

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)
```

Train a **new** logistic regression on `X_train_bal`, `y_train_bal`. Predict on the **original** `X_test`, `y_test` (do **not** SMOTE the test set).

Print:

```text
--- After SMOTE ---
```

then `classification_report(y_test, y_pred)`.

#### Part 4 — Two comment lines

After you run the script, add **two** comment lines at the bottom of your file:

```python
# Recall for class 1 (fraud) — baseline: ___   after SMOTE: ___
# In one short sentence: why is accuracy alone not enough here?
```

Fill in the recall values you see in the reports (for class `1`).

---

### What you should notice

- **Baseline** often has **high accuracy** but **low recall** for class `1` (fraud).  
- **After SMOTE**, recall for class `1` on the test set usually **improves**.  
- The **test set** stays imbalanced — you only balance **training** data.

---

### Submission instructions (**case c** — single file)

- Write everything in **one** file: `fraud_compare.py`.  
- Install if needed: `pip install scikit-learn imbalanced-learn`  
- Run the script once and check both reports print.  
- Submit the full code (including your two comment lines) in the LMS **code editor / answer box**.

---

### Answer explanation (for Assess platform)

#### Ideal walkthrough

1. Student builds imbalanced data and **splits before** SMOTE — correct order.  
2. Baseline model tends to predict the majority class; **recall for fraud (class 1)** is often `0.0`.  
3. SMOTE balances **training only**; evaluation on the real test distribution stays honest.  
4. Comments should mention that **accuracy looks good** while the model **misses fraud** until recall is considered.

#### Reference solution (evaluators only)

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

X, y = make_classification(
    n_samples=1000,
    n_features=4,
    weights=[0.99, 0.01],
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", X_train.shape[0])
print("Test size:", X_test.shape[0])

baseline = LogisticRegression(max_iter=500)
baseline.fit(X_train, y_train)
y_pred_base = baseline.predict(X_test)

print("\n--- Baseline ---")
print(classification_report(y_test, y_pred_base))

smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)

model_smote = LogisticRegression(max_iter=500)
model_smote.fit(X_train_bal, y_train_bal)
y_pred_smote = model_smote.predict(X_test)

print("\n--- After SMOTE ---")
print(classification_report(y_test, y_pred_smote))

# Recall for class 1 (fraud) — baseline: 0.00   after SMOTE: 1.00
# Accuracy alone is not enough because the model can look accurate by always predicting "not fraud" and missing real fraud.
```

---

**End of subjective assignment.**
