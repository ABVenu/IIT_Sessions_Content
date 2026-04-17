# Session 29 — Practice Questions
*Topics: Regularization (Ridge, Lasso, alpha), regression evaluation metrics (MAE, RMSE, R-squared), baseline comparison, and error analysis.*

---

## Objective Questions (8)

### Easy

**Q1 (Single Correct).** What is **regularization** in the context of linear regression?

- (A) Removing all features before training
- (B) Adding a penalty during training to discourage excessively large coefficients and reduce overfitting
- (C) Increasing the training set size by duplicating rows
- (D) Using only the intercept term and ignoring all features

**Answer:** **(B)**  
Regularization penalizes large weights so the model generalizes better instead of memorizing noise.

---

**Q2 (Single Correct).** Which statement best distinguishes **Ridge** from **Lasso**?

- (A) Ridge’s penalty is tied to the sum of **absolute** coefficient values, while Lasso’s penalty is tied to the sum of **squared** coefficient values
- (B) Ridge shrinks coefficients but typically does not set them to exactly zero; Lasso can set some coefficients exactly to zero
- (C) Ridge removes all features from the dataset before training; Lasso keeps all features
- (D) Neither Ridge nor Lasso uses a tuning setting such as **alpha**

**Answer:** **(B)**  
Ridge (L2) shrinks all coefficients; Lasso (L1) can produce exact zeros and thus feature elimination.

---

**Q3 (Multiple Correct).** Select all statements that are **true** about **Ridge regression**.

- (A) It adds a penalty related to the sum of squared coefficients
- (B) It can eliminate a feature by setting its coefficient exactly to zero
- (C) Increasing **alpha** generally increases the strength of shrinkage
- (D) It is often appropriate when many features are weakly but genuinely related to the target

**Answer:** **(A), (C), (D)**  
Ridge does not usually zero coefficients (that is Lasso’s behavior). Stronger **alpha** means a stronger penalty.

---

### Medium

**Q4 (Single Correct).** For regression, **MAE** and **RMSE** are both expressed in the same units as the target. Which statement is **most accurate**?

- (A) RMSE treats a 10-unit error as exactly twice as bad as a 5-unit error, same as MAE
- (B) MAE is more sensitive to a few very large errors than RMSE
- (C) RMSE penalizes large errors more heavily than MAE because errors are squared before averaging
- (D) MAE cannot be used when the target is continuous

**Answer:** **(C)**  
Squaring in MSE (and thus RMSE) makes large mistakes dominate more than in MAE.

---

**Q5 (Multiple Correct).** Which statements about **R-squared** are correct?

- (A) It measures the proportion of variance in the target explained by the model
- (B) A value of 0 means the model is equivalent to always predicting the mean of the target (on the evaluation setup used)
- (C) A negative R-squared is impossible
- (D) R-squared alone does not tell you whether absolute prediction errors are acceptable for a business use case

**Answer:** **(A), (B), (D)**  
R-squared can be negative for very poor models. Use MAE/RMSE for scale of errors; R-squared for explained variation relative to a mean baseline.

---

**Q6 (Single Correct).** In the lecture’s scikit-learn examples, what does the **`alpha`** setting control for **Ridge** and **Lasso** models?

- (A) The fraction of data used for training versus testing
- (B) The random seed used when shuffling or splitting data
- (C) How strong the regularization penalty is
- (D) Only the step size if you were using plain gradient descent by hand

**Answer:** **(C)**  
Higher **alpha** means a stronger penalty (more shrinkage in Ridge; more zeroing in Lasso).

---

### Hard

**Q7 (Multiple Correct).** In the lecture’s synthetic student dataset, an extra **random noise** column is **not** part of the true score formula, yet plain linear regression may still give it a nonzero coefficient. Which outcomes are **consistent** with the notes?

- (A) Ordinary linear regression may assign a nonzero weight to that noise column by chance on finite training data
- (B) Ridge typically shrinks the noise column’s coefficient compared to ordinary linear regression
- (C) Lasso may drive that noise column’s coefficient exactly to zero
- (D) Using regularization **always** improves test-set R-squared versus ordinary linear regression, in every run

**Answer:** **(A), (B), (C)**  
Regularization helps but does not guarantee better test metrics in every run or split.

---

**Q8 (Single Correct).** In **error analysis**, test-set residuals are grouped by study-hour bins. If the **average residual** for a group is **strongly positive**, what does that usually imply?

- (A) The model tends to **under-predict** actual values for that group
- (B) The model tends to **over-predict** actual values for that group
- (C) MAE must be zero for that group
- (D) R-squared must be negative

**Answer:** **(A)**  
Residual = actual − predicted; positive average residual means predictions are systematically too low.

---

## Subjective Question (1)

**Difficulty:** Medium to Hard  
**Type:** Implementation (coding)

### Q9 — Question (what students answer)

Start from the **`df`** created below (this is the **only** provided code — do **not** change **`seed`**, **`n_samples`**, or the score formula). Everything else — how you take features and target from **`df`**, how you split data, how you train **`LinearRegression`**, and how you build a table of **actual vs predicted** scores for evaluation — is for you to design, consistent with the session.

**Provided: create the DataFrame**

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=21)
n_samples = 400
study_hours = rng.uniform(1, 10, size=n_samples)
exam_score = 40 + 7.5 * study_hours + rng.normal(0, 6, size=n_samples)

df = pd.DataFrame({"study_hours": study_hours, "exam_score": exam_score})
```

**Deliverables**

1. Train a **linear regression** model to predict **`exam_score`** from **`study_hours`**, evaluate in a sound way (for example hold-out test data), and ensure you can compare **actual** targets to **predictions** in a DataFrame with aligned rows.
2. Implement **`regression_metrics_from_df(df, y_col, y_pred_col)`** that reads those two columns **by name** and returns **`{'mae', 'rmse', 'r2'}`** using **`sklearn.metrics`**. Let $y_i$ be actual values and $\hat{y}_i$ be predictions for $i=1,\ldots,n$. Use **`mean_absolute_error`** for MAE, **`mean_squared_error`** for MSE, define $\mathrm{RMSE} = \sqrt{\mathrm{MSE}}$, and **`r2_score`** for $R^2$.

```python
def regression_metrics_from_df(df, y_col: str, y_pred_col: str) -> dict:
    """
    Return a dict with keys: 'mae', 'rmse', 'r2'
    using sklearn.metrics (numpy only for sqrt of MSE).
    """
    ...
```

---

### Requirements (for submission)

- Use **`mean_absolute_error`**, **`mean_squared_error`**, and **`r2_score`** from **`sklearn.metrics`**. Pass **actual** first, **predicted** second (consistent with $y_i$ then $\hat{y}_i$).
- Report **RMSE** as $\mathrm{RMSE}=\sqrt{\mathrm{MSE}}$ with MSE from **`mean_squared_error`**.
- Metric logic belongs in **`regression_metrics_from_df`**, not inside **`.fit`**.

---

### Rubric (for evaluators)

- **`df`** matches the provided snippet; model trained and evaluated without data leakage; predictions aligned with actuals in the DataFrame passed to **`regression_metrics_from_df`**.
- **RMSE** computed as $\sqrt{\mathrm{MSE}}$ with sklearn’s **`mean_squared_error`**; **$R^2$** from **`r2_score`**; columns selected by name.

---

### Sample detailed solution *(placed last — for instructors / self-check)*

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

rng = np.random.default_rng(seed=21)
n_samples = 400
study_hours = rng.uniform(1, 10, size=n_samples)
exam_score = 40 + 7.5 * study_hours + rng.normal(0, 6, size=n_samples)

df = pd.DataFrame({"study_hours": study_hours, "exam_score": exam_score})

X = df[["study_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

test_df = X_test.copy()
test_df["exam_score"] = y_test.values
test_df["predicted_score"] = model.predict(X_test)


def regression_metrics_from_df(df, y_col: str, y_pred_col: str) -> dict:
    y_true = df[y_col].values
    y_pred = df[y_pred_col].values
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return {"mae": mae, "rmse": rmse, "r2": r2}


metrics = regression_metrics_from_df(
    test_df, y_col="exam_score", y_pred_col="predicted_score"
)
print(metrics)
```
