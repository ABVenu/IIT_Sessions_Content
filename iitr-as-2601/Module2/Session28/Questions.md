# Session 28 — Practice Questions
*Topics: Regression vs classification, target and features, linear regression (intercept, coefficients), training with sklearn, train–test split and overfitting, residuals.*

---

## Objective Questions (8)

### Easy

**Q1 (Single Correct).** Which problem is best described as a **regression** task?

- (A) Predict whether an email is spam or not spam
- (B) Assign each customer to one of three loyalty tiers
- (C) Detect whether an image contains a cat or a dog
- (D) Predict the exact cab fare in rupees from distance and time of day

**Answer:** **(D)**  
Regression predicts a **continuous numeric** outcome. The other options are classification or labeling tasks.

---

**Q2 (Single Correct).** In linear regression, the **coefficient** on a feature is best described as:

- (A) The learned multiplier showing how much the prediction changes per one-unit increase in that feature
- (B) The average of all target values in the training set
- (C) The number of rows in the training data
- (D) The random seed used for `train_test_split`

**Answer:** **(A)**  
The **intercept** is the baseline; **coefficients** are the per-feature slopes/weights.

---

**Q3 (Multiple Correct).** Select all statements that correctly use the vocabulary from this session.

- (A) Any column of integers (e.g. job level coded 1, 2, 3) is always a valid regression target without further thought.
- (B) The **target variable** is the numeric outcome the model predicts.
- (C) **Features** are input columns used to form predictions.
- (D) **Linear regression** predicts the target as a weighted combination of features plus an intercept.

**Answer:** **(B), (C), (D)**  
Ordered category codes may be **labels disguised as numbers**—they are not necessarily a meaningful continuous scale.

---

### Medium

**Q4 (Single Correct).** You have one feature: **200** study-hour values (one number per student). For `sklearn.linear_model.LinearRegression().fit(X, y)`, how should **`X`** be organized?

- (A) A two-dimensional table with **1** row and **200** columns
- (B) A square table with **200** rows and **200** columns
- (C) A two-dimensional table with **200** rows and **1** column (each row is one student, one feature)
- (D) A single one-dimensional list of **200** numbers (only one axis — no separate “feature” dimension)

**Answer:** **(C)**  
scikit-learn expects **`X` to be two-dimensional** (one row per sample, one column per feature). With one feature, that means **200** rows and **1** column — for example by reshaping with **`reshape(-1, 1)`**.

---

**Q5 (Multiple Correct).** Which statements about **`train_test_split`** and **generalisation** are correct?

- (A) If test error is much worse than training error, the model may have **overfit** the training data.
- (B) The test set should be used during `.fit()` so the model learns from harder examples.
- (C) The model should be **fit** only on the training portion, not on the test portion.
- (D) Comparing training error to test error helps detect **overfitting**.

**Answer:** **(A), (C), (D)**  
The test set is held out for **evaluation**, not for training.

---

**Q6 (Single Correct).** The **residual** for one data point is defined as:

- (A) The training loss summed over all points
- (B) The coefficient of the first feature
- (C) Predicted minus actual
- (D) Actual minus predicted

**Answer:** **(D)**  
As in the notes: **residual = actual − predicted** (positive ⇒ model under-predicted).

---

### Hard

**Q7 (Multiple Correct).** Which patterns are **consistent** with the session’s discussion of **residuals**?

- (A) If residuals are mostly negative, the model always has a bug in `predict()`.
- (B) A **strongly positive average residual** suggests the model tends to **under-predict** on average.
- (C) Residuals scattered randomly around zero suggest the model has no strong systematic bias in that respect.
- (D) A few very large residuals may indicate **outliers** or unusual cases worth inspecting.

**Answer:** **(B), (C), (D)**  
Systematic bias is a modeling/data issue, not proof of a coding bug by itself.

---

**Q8 (Single Correct).** Which situation best describes **underfitting**?

- (A) Both training and test error are high because the model is too simple to capture the pattern
- (B) Training error is low but test error is much higher
- (C) The model memorises training labels perfectly and achieves 0 error on the test set
- (D) The average residual on training data is exactly zero, so the model must be wrong

**Answer:** **(A)**  
Underfitting = **too simple**; high error on **both** train and test. Large train–test gap is more typical of **overfitting**.

---

## Subjective Question (1)

**Difficulty:** Medium to Hard  
**Type:** Implementation (coding)

### Q9 — Question (what students answer)

Start from the **`df`** below (the **only** provided code — do **not** change the random seed or the score formula). Decide how you take features and target from **`df`**, how you fit **`LinearRegression`**, and how you add **`predicted_score`** and **`residual`**. For each row, the residual is **actual minus predicted**; in symbols you can write $r = y - \hat{y}$ where $y$ is the actual exam score and $\hat{y}$ is the predicted score.

**Provided: create the DataFrame**

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)
n = 200
study_hours = rng.uniform(1, 10, size=n)
exam_score = 40 + 7.5 * study_hours + rng.normal(0, 5, size=n)

df = pd.DataFrame({"study_hours": study_hours, "exam_score": exam_score})
```

**Deliverable**

Implement **`add_predictions_and_residuals(df)`** that fits **`LinearRegression`** to predict **`exam_score`** from **`study_hours`**, returns a **new** DataFrame including **`predicted_score`** and **`residual`**, and **print** the **mean** of **`residual`**.

```python
def add_predictions_and_residuals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fit LinearRegression on df['study_hours'] vs df['exam_score'],
    return a new DataFrame with columns predicted_score and residual.
    """
    ...
```

---

### Requirements (for submission)

- Use **`sklearn.linear_model.LinearRegression`** with a valid **2D** feature matrix of shape $(n,\,1)$: $n$ rows (samples) and one feature column.

---

### Rubric (for evaluators)

- **`df`** matches the provided snippet; **`LinearRegression`** fit and predict on aligned rows.
- Output includes **`predicted_score`** and residual $r_i = y_i - \hat{y}_i$ using the **`exam_score`** and **`predicted_score`** columns; mean **`residual`** printed.

---

### Sample detailed solution *(placed last — for instructors / self-check)*

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(seed=42)
n = 200
study_hours = rng.uniform(1, 10, size=n)
exam_score = 40 + 7.5 * study_hours + rng.normal(0, 5, size=n)

df = pd.DataFrame({"study_hours": study_hours, "exam_score": exam_score})


def add_predictions_and_residuals(df: pd.DataFrame) -> pd.DataFrame:
    X = df[["study_hours"]]
    y = df["exam_score"]

    model = LinearRegression()
    model.fit(X, y)

    out = df.copy()
    out["predicted_score"] = model.predict(X)
    out["residual"] = out["exam_score"] - out["predicted_score"]
    return out


result_df = add_predictions_and_residuals(df)
print("Mean residual:", round(result_df["residual"].mean(), 6))
print(result_df[["study_hours", "exam_score", "predicted_score", "residual"]].head())
```
