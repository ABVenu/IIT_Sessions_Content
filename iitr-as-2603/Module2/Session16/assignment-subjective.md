# Assignment: Subjective — Session 16: Linear Regression Fundamentals

**Total Questions: 1 | Format: Practical Coding Task | Difficulty: Medium**

---

## Question 1 — StudyBoost: From Hours to Marks (and Honest Errors)

**Scenario**

StudyBoost, a small ed-tech pilot, has past records linking **weekly study hours** to **exam scores out of 100**. You will build a **simple linear regression** model, check whether it beats a **mean baseline**, and surface the **largest mistakes** with a **residual table** — the same habits used when reviewing models before launch.

---

### Your task

Write **one** Python file: `studyboost_regression.py` with the **three** tasks below.

Use these settings everywhere: `random_state=42`, `test_size=0.2`, and `LinearRegression()` with default arguments.

#### Task 1 — Create data and split first

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(seed=42)
hours = rng.uniform(1, 10, size=80)
scores = 40 + 7.5 * hours + rng.normal(0, 4, size=80)

df = pd.DataFrame({"study_hours": hours, "exam_score": scores})

X = df[["study_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Print:

```text
Train rows: <count>
Test rows: <count>
```

(replace `<count>` with actual numbers)

#### Task 2 — Fit linear regression (train only)

Train `LinearRegression` on `X_train`, `y_train`. Print:

```text
Intercept: <value>
Coefficient (per hour): <value>
Training score: <value>
Testing score: <value>
```

Round printed numbers to **2 decimal places** where applicable.

Predict for **one new student** with **6.0** study hours. Print:

```text
Predicted score for 6 hours: <value>
```

#### Task 3 — Baseline, residuals, and reflection

**Mean baseline:** Compute `baseline_value = y_train.mean()`. Build a NumPy array of that value for **every** test row and score it with:

```python
from sklearn.metrics import r2_score
baseline_r2 = r2_score(y_test, baseline_preds)
```

Print:

```text
Mean baseline R2 on test: <value>
```

(round to 2 decimals)

**Residual table:** Using **test-set** predictions from your regression model, build a DataFrame with columns `study_hours`, `y_actual`, `y_predicted`, `residual` where `residual = y_actual - y_predicted`. Sort by **absolute residual** descending and print the **top 3 rows**.

**Comments:** Add **two** comment lines at the bottom of your file:

```python
# Train vs test score gap — what does it suggest about overfitting here? ___
# One row from your residual table — did the model over- or under-predict? ___
```

Fill in both blanks in **one short sentence each** based on **your** printed output.

---

### What you should notice

- **Split happens before** `.fit()` — test rows never train the line.  
- **Intercept** and **coefficient** should be near the data-generating story (roughly **40** and **7.5**).  
- **Regression test R²** should usually beat the **mean baseline** on the same test split.  
- **Residuals** show row-level error; positive residual → **under-predicted**.

---

### Submission instructions (**case c** — single file)

- Write everything in **one** file: `studyboost_regression.py`.  
- Install if needed: `pip install scikit-learn pandas numpy`  
- Run the script once and verify all sections print.  
- Submit the full code (including your two comment lines) in the LMS **code editor / answer box**.

---

### Answer explanation (for Assess platform)

#### Ideal walkthrough

1. **Task 1:** Build synthetic study data and **split before** fitting.  
2. **Task 2:** Learned **intercept** ≈ **40**, **coefficient** ≈ **7.5**; **train** and **test** scores should be **close** (good generalization on this simple line); predict **6 hours**.  
3. **Task 3:** **Mean baseline** R² on test is typically **low or negative**; regression should beat it. Residual table surfaces worst rows; comments note a **small train–test gap** and one **over- vs under-predict** example from a row’s sign.

#### Reference solution (evaluators only)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

rng = np.random.default_rng(seed=42)
hours = rng.uniform(1, 10, size=80)
scores = 40 + 7.5 * hours + rng.normal(0, 4, size=80)

df = pd.DataFrame({"study_hours": hours, "exam_score": scores})

X = df[["study_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Train rows: {X_train.shape[0]}")
print(f"Test rows: {X_test.shape[0]}")

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient (per hour): {model.coef_[0]:.2f}")
print(f"Training score: {model.score(X_train, y_train):.2f}")
print(f"Testing score: {model.score(X_test, y_test):.2f}")

new_student = pd.DataFrame({"study_hours": [6.0]})
print(f"Predicted score for 6 hours: {model.predict(new_student)[0]:.2f}")

baseline_value = y_train.mean()
baseline_preds = np.full(shape=len(y_test), fill_value=baseline_value)
baseline_r2 = r2_score(y_test, baseline_preds)
print(f"Mean baseline R2 on test: {baseline_r2:.2f}")

y_test_pred = model.predict(X_test)
results = pd.DataFrame({
    "study_hours": X_test["study_hours"].values,
    "y_actual": y_test.values,
    "y_predicted": y_test_pred,
})
results["residual"] = results["y_actual"] - results["y_predicted"]
print("\nTop 3 residuals (by absolute value):")
print(results.sort_values("residual", key=lambda s: s.abs(), ascending=False).head(3))

# Train vs test score gap — what does it suggest about overfitting here?
# Scores are close, so the line generalizes and is not heavily overfitting on this split.
# One row from your residual table — did the model over- or under-predict?
# Example: positive residual means the model under-predicted that student.
```

**Alternative approaches:** Using `make_regression` or a CSV with the same two columns is acceptable if split-first discipline, baseline from `y_train` only, and residual definition stay the same.

---

**End of subjective assignment.**
