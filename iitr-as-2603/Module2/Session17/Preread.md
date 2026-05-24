# Pre-read: Regression — Regularization and Evaluation

An analytics team at a company builds a model to predict **monthly salary** for new hires. In the demo, the chart looks strong: predicted salaries track actual salaries closely on the data used to build the model. Leadership is ready to roll it out.

Then someone asks a harder question: *“How wrong are we, in rupees, for candidates with less than two years of experience?”* Nobody has an answer. The team only has one headline number — “average error” — and it looks acceptable. A week later, HR reports that offers for junior candidates are consistently **₹8,000–₹12,000 off**, while mid-level predictions look fine. The **average** hid the real problem.

---

## The problem we need to solve

**What if** your regression model uses **twenty input columns** — experience, attendance, survey scores, and several columns that are mostly noise — and still shows **low error on training rows**? It may be **memorising quirks** of past data. On **new applicants**, predictions swing or fail for specific groups.

**What if** two models both claim to be “good,” but one makes a few **catastrophic** mistakes (wrong salary band, wrong inventory order) while the other only makes small, steady errors? A single summary number cannot tell you which risk profile you are choosing.

**What if** you can draw a best-fit line and compute residuals, but you still cannot **defend** the model in a review — no standard metrics, no comparison to **Ridge** or **Lasso**, no proof that you checked **where** errors cluster?

In the **previous session**, you learned to fit **linear regression**, compare against a **mean baseline**, and read **residuals** on a train/test split. That was the right foundation. The gap now is **control** (when the model becomes too complex) and **evidence** (how to measure and inspect performance properly).

**This session** addresses that gap: **regularization** to reduce overfitting, **MAE / RMSE / R²** to quantify error, and **error analysis** to find weak segments — not just “the model looks fine on average.”

---

Think of a regression model like a **marksheet summary** versus a **subject-wise report**. Saying “class average error is 5 marks” sounds fine until you discover Science errors are 1 mark but Maths errors are 14 marks for the same students. **Regularization** is the discipline that stops the model from overweighting every subject line on the sheet; **metrics and error analysis** are the subject-wise report that shows where marks were actually lost.

---

**In this pre-read, you'll discover:**

- **Why** models with many features can overfit — and how **Ridge** and **Lasso** shrink or remove unstable coefficients  
- **How** to compare **Linear**, **Ridge**, and **Lasso** on the same data using **`alpha`** and coefficient tables  
- **What** **MAE**, **RMSE**, and **R²** each measure — and why you need more than one number  
- **How** grouped **error analysis** exposes failure patterns that a global average error hides  

**Session objective:** Understand how to control model complexity and evaluate regression performance.

---

## 1. Why plain linear regression can overfit

With many features (or noisy columns), **ordinary least squares** can assign **large coefficients** to weak or spurious predictors. Training error may look strong while **test error** rises — the model fits noise, not only signal.

**Regularization** adds a **penalty** during training so coefficients stay smaller (Ridge) or some are removed (Lasso). Goal: better **generalization** on held-out data, not the lowest training error alone.

| Model | Penalty on coefficients | Typical effect |
| --- | --- | --- |
| **LinearRegression** | None | Full flexibility; higher overfitting risk with many features |
| **Ridge** (L2) | Sum of **squared** coefficients | Shrink all weights; rarely exactly zero |
| **Lasso** (L1) | Sum of **absolute** coefficients | Shrink; some weights become **exactly 0** |

**`alpha`** (in `sklearn`) controls penalty strength: **higher `alpha` → stronger shrinkage**.

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso

lr    = LinearRegression()
ridge = Ridge(alpha=10)
lasso = Lasso(alpha=1)
```

Fit each on the **same** `X_train`, `y_train`; compare **`coef_`** and test metrics.

---

## 2. Ridge vs Lasso — behaviour to compare

### Ridge regression

- **Definition:** Linear regression plus L2 penalty on coefficient magnitudes.
- **Effect:** All features usually **remain** in the model; coefficients move toward zero but not usually to exactly zero.
- **Use when:** Many features are **weakly but genuinely** related to the target; you want stability without dropping columns.

### Lasso regression

- **Definition:** Linear regression plus L1 penalty on coefficient magnitudes.
- **Effect:** Some coefficients become **exactly 0** → automatic **feature selection**; model is **sparse**.
- **Use when:** You suspect **many irrelevant** features (e.g. a random noise column in a teaching dataset).

**Classroom check:** On data with a deliberate **`random_noise`** feature, linear regression may give it a small nonzero weight; Ridge shrinks it; Lasso often sets it to **0.0**.

---

## 3. Model comparison workflow

After fitting **Linear**, **Ridge**, and **Lasso** on the same split:

1. Print **coefficient table** (feature names × three models).
2. Predict on **`X_test`** only.
3. Compute **MAE**, **RMSE**, **R²** for each model (same test labels).

Do not pick a model from training scores alone; compare on **unseen test rows**.

```text
fit(X_train, y_train)  →  predict(X_test)  →  metrics(y_test, y_pred)
```

---

## 4. Evaluation metrics

All three are computed on **test** predictions vs **actual** `y_test`.

### MAE — Mean Absolute Error

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|$$

- **Units:** Same as target (marks, ₹, minutes).
- **Interpretation:** Typical absolute miss.
- **Property:** Treats all errors linearly; **less sensitive** to a few huge outliers.

```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
```

### RMSE — Root Mean Squared Error

$$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

- **Units:** Same as target.
- **Interpretation:** Penalises **large** errors more than MAE (squaring before averaging).
- **Practical rule:** If **RMSE ≫ MAE**, investigate **outliers** or segments with very bad predictions.

```python
from sklearn.metrics import mean_squared_error
import numpy as np
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

### R² — coefficient of determination

- **Definition:** Share of target **variance** explained by the model vs predicting the **training mean** for everyone.
- **Scale:** Often between 0 and 1 on reasonable models; **0** ≈ mean baseline; **negative** = worse than mean.
- **Limitation:** Does **not** state whether absolute errors are acceptable for business (e.g. ₹5,000 MAE on salaries). Pair **R²** with **MAE** or **RMSE**.

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
```

| Metric | Answers | Does not answer |
| --- | --- | --- |
| **MAE** | Average error size in real units | Where errors cluster |
| **RMSE** | Error size with extra weight on big misses | Which feature groups fail |
| **R²** | Relative fit vs mean baseline | Whether errors are small enough for deployment |

---

## 5. Error analysis

**Residual** (per row): `residual = y_actual − y_predicted`.

**Error analysis** groups residuals (or `|residual|`) by **feature bins**, prediction ranges, or categories to find **systematic** failure — e.g. high MAE only for low `study_hours` — that a single global MAE hides.

Typical steps on **test** data:

1. Build a table: features, actual, predicted, residual, `abs_error`.
2. Add groups (`pd.cut` on a feature).
3. Aggregate **mean** / **max** absolute error per group.
4. Relate to **residual plots** from the previous session (fan shape, curve, bias).

```python
import pandas as pd
residuals = y_test - y_pred
# group by feature bins → mean(abs_error) per group
```

---

## 6. Choosing metrics in practice

| Situation | Prefer |
| --- | --- |
| All errors equally costly | **MAE** |
| Large errors especially dangerous (safety, finance caps) | **RMSE** (report alongside MAE) |
| Compare models on same dataset | **R²** + **MAE** or **RMSE** |
| Debug before deployment | **Error analysis** by segment |

**Deployment readiness** requires: beat **mean baseline** on test, stable **train vs test** gap, acceptable **MAE/RMSE** in business units, and no critical segment with unchecked high error.

---

## Topics covered in this session

- **Regularization** intuition — Ridge (L2) and Lasso (L1); role of **`alpha`**
- **Model comparison** — coefficient and prediction behaviour across Linear / Ridge / Lasso
- **MAE**, **RMSE**, **R²** — definitions, interpretation, sklearn usage
- **Error analysis** — patterns in residuals by feature groups
- **Practical perspective** — selecting and reporting metrics for regression

---

## Terminology quick reference

| Term | Meaning |
| --- | --- |
| **Regularization** | Penalty during fit to limit coefficient size / count |
| **Ridge** | L2-regularized regression; shrinks, rarely zeros coefficients |
| **Lasso** | L1-regularized regression; can zero coefficients (feature selection) |
| **`alpha`** | Regularization strength hyperparameter |
| **Sparse model** | Many coefficients exactly zero (common with Lasso) |
| **MAE** | Mean absolute prediction error |
| **RMSE** | Root mean squared error; weights large errors more |
| **R²** | Fraction of variance explained vs mean baseline |
| **Error analysis** | Segment-level study of where predictions fail |
| **Generalization** | Model performance on unseen data |

---

## Before class — checklist

- [ ] Previous session reviewed: **residual**, **train/test split**, **mean baseline**
- [ ] Comfortable with `LinearRegression`, `train_test_split`, basic plots in Colab
- [ ] Know difference between **training** and **test** rows when reporting metrics

---

## Questions to explore in the live session

1. Same dataset, three models — **Linear**, **Ridge**, **Lasso**. The **`random_noise`** column gets a coefficient in plain linear regression. **Which model zeros it out, and what does that imply for feature selection?**
2. Model A: MAE = **₹3,000**, RMSE = **₹3,200**. Model B: MAE = **₹3,000**, RMSE = **₹9,500**. Same average miss — **which would you trust for salary offers, and why?**
3. R² = **0.80** on test data, but grouped error analysis shows **doubled MAE** for low-experience candidates. **Is the model deployment-ready?** What would you report besides R²?

---

## Self-check (notebook)

1. In one sentence each: how do **Ridge** and **Lasso** treat a useless feature differently?
2. Test MAE = **4.2** marks, RMSE = **9.1** marks — what might that gap suggest?
3. R² = **0.72** but MAE = **15** marks on a 100-mark exam — is the model automatically “good enough” for placement decisions? Why or why not?
4. Why must **MAE/RMSE/R²** be computed on **`y_test`**, not `y_train`, when comparing models?

---

## After this session, you should be able to

- Fit and compare **Linear**, **Ridge**, and **Lasso** and interpret **`coef_`** changes  
- Report **MAE**, **RMSE**, and **R²** on held-out test data with correct units and meaning  
- Run simple **error analysis** by feature groups and link findings to residual patterns  
- Choose and justify metrics for a regression use case instead of relying on training fit alone  

---

## Key points to remember

- Low **training** error does not prove a model is ready; evaluate on **held-out test** data.
- **Ridge** keeps all features with smaller weights; **Lasso** can **drop** features via zero coefficients.
- **MAE**, **RMSE**, and **R²** are **complementary** — use more than one.
- **Error analysis** turns “average error” into “who is hurt by the model.”
- This session completes the regression evaluation thread started in the previous session; later modules assume you can **compare and defend** regression results numerically.
