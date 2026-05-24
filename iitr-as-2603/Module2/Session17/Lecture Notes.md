# Regression: Regularization and Evaluation

## Context of This Session

In the previous session, you trained your first **linear regression** models — from a simple study-hours example to the **California housing** case study with a **Pipeline**. You compared train vs test scores, met the **mean baseline**, and inspected **residuals** row by row to spot bias and large mistakes. You also named **underfitting** and **overfitting** using the train–test gap.

Two questions were left open: *What do you do when a model fits training data too aggressively?* And *how do you measure and defend performance with standard numbers — not just a single score from `.score()`?* This session answers both.

**In this session, you will:**

- Understand **regularization** and how **Ridge** and **Lasso** control model complexity
- Compare **Linear**, **Ridge**, and **Lasso** on the same train–test split
- Report **MAE**, **RMSE**, and **R²** on held-out test data with correct interpretation
- Run simple **error analysis** by feature groups to find where predictions fail
- Choose the right metric for a business use case

---

## Regularization: Keeping the Model from Getting Too Clever

When a model **overfits**, it learns noise in the training rows — not only the real pattern. With many features, plain linear regression can assign **very large coefficients** to weak or random columns. Predictions then swing on new data.

**Regularization:**

- **Official Definition:** A technique that adds a **penalty** during training to discourage excessively large coefficients, reducing overfitting and improving **generalization**.
- **In Simple Words:** You tell the model: "Be accurate, but don't make any feature weight extreme — I will penalise you if you do."
- **Real-Life Example:** A new intern over-customises every report with unnecessary detail. A good manager says: "Keep it accurate **and** reusable." Regularization is that manager.

The penalty strength is controlled by **`alpha`** in scikit-learn — **higher alpha → stronger shrinkage**.

---

### Ridge Regression

**Ridge Regression:**

- **Official Definition:** Linear regression plus an **L2 penalty** — the sum of **squared** coefficients — which shrinks weights but rarely sets any to exactly zero.
- **In Simple Words:** All features can stay, but loud weights are turned down.
- **Real-Life Example:** A restaurant review system still lists every dish, but rarely ordered items get lower weight in the overall score.

**Key behaviour:** All features remain; coefficients move toward zero but not usually to **0.0**. Best when most features matter at least a little.

---

### Lasso Regression

**Lasso Regression:**

- **Official Definition:** Linear regression plus an **L1 penalty** — the sum of **absolute** coefficients — which can shrink some weights to **exactly zero**, removing those features.
- **In Simple Words:** If a feature is useless, Lasso can drop it completely — built-in **feature selection**.
- **Real-Life Example:** A talent show eliminates weak performers each round. Ridge keeps everyone but lowers their volume; Lasso removes them.

**Key behaviour:** The model becomes **sparse** — only important features survive. Best when many columns may be irrelevant.

---

**Side-by-side comparison**

![Regularization: Ridge vs Lasso — What Happens to Coefficients](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/ridge_vs_lasso_coefficients.png)

| | **Linear Regression** | **Ridge** | **Lasso** |
|---|---|---|---|
| Penalty? | No | Yes — squared coeffs | Yes — absolute coeffs |
| Coefficients reach zero? | No restriction | Shrunk, not zero | Some become **0.0** |
| Feature elimination? | No | No | Yes |
| Best when | Few clean features | Many somewhat relevant features | Many likely irrelevant features |

### Quick Activity — Ridge or Lasso?

A salary model has **25 input columns**. HR suspects **8 are survey noise** with no real link to pay; the rest are experience, role, and location.

1. Which regularized model is better suited to **drop useless columns automatically**?  
2. If you believe **every** column helps a little, which model fits better?

**Answers:** 1 → **Lasso**. 2 → **Ridge**.

---

## Model Comparison: Seeing Regularization in Action

Theory is useful; comparing **coefficients** on the same split makes the idea concrete. Fit all three models on **`X_train`**, then inspect **`coef_`** and test predictions.

**Example setup:** 300 student rows (`seed=42`). Five features — `study_hours`, `sleep_hours`, `attendance`, `distractions`, `random_noise` — and target **`exam_score`**. Only the first four truly drive the score; `random_noise` is deliberately useless.

```python
# Import numpy and the three regression models
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split

# Reproducible random data
rng = np.random.default_rng(seed=42)
n_samples = 300

# Five features — last one is pure noise
study_hours  = rng.uniform(1, 10, size=n_samples)
sleep_hours  = rng.uniform(4, 9, size=n_samples)
attendance   = rng.uniform(60, 100, size=n_samples)
distractions = rng.uniform(0, 5, size=n_samples)
random_noise = rng.uniform(0, 10, size=n_samples)

# Stack features into one table (300 rows × 5 columns)
X = np.column_stack([study_hours, sleep_hours, attendance, distractions, random_noise])

# Build scores from real features only, plus small random noise
y = (
    40 + 6.0 * study_hours + 1.5 * sleep_hours
    + 0.3 * attendance - 2.0 * distractions
    + rng.normal(0, 5, size=n_samples)
)

# 80% train, 20% test — same honest split as before
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Three models on the same training rows
lr    = LinearRegression()
ridge = Ridge(alpha=10)
lasso = Lasso(alpha=1)

lr.fit(X_train, y_train)
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

# Compare learned weights side by side
names = ["study_hours", "sleep_hours", "attendance", "distractions", "random_noise"]
print(f"{'Feature':<18} {'Linear':>10} {'Ridge':>10} {'Lasso':>10}")
print("-" * 52)
for i, name in enumerate(names):
    print(f"{name:<18} {lr.coef_[i]:>10.3f} {ridge.coef_[i]:>10.3f} {lasso.coef_[i]:>10.3f}")
```

**How the code works:**

- **`random_noise`** has no true relationship to `exam_score` — a fair test of whether a model chases spurious patterns.
- **`Ridge(alpha=10)`** shrinks all coefficients; **`Lasso(alpha=1)`** often sets `random_noise` to **0.0**.
- **Same `train_test_split`** as in the previous session — never fit on test rows.

**What to observe:**

- Linear regression may give `random_noise` a small nonzero weight — misleading signal from training noise.
- Ridge makes that weight smaller but still present.
- Lasso zeros it — automatic feature removal.

---

## Evaluation Metrics: Measuring How Good Predictions Are

After predictions exist on **`X_test`**, you need numbers you can explain in a review. Three metrics appear constantly in regression work: **MAE**, **RMSE**, and **R²**. They answer different questions — use more than one.

---

### MAE — Mean Absolute Error

**MAE:**

- **Official Definition:** The average of **absolute** differences between actual and predicted values.
- **In Simple Words:** "On average, how many units off are we?" — same units as the target (marks, ₹, minutes).
- **Real-Life Example:** A delivery app is off by 4.5 minutes on average across 100 orders — that is MAE.

**Use MAE when** all errors are roughly equally costly and stakeholders want a plain-language number.

---

### RMSE — Root Mean Squared Error

**RMSE:**

- **Official Definition:** The square root of the average **squared** errors — large mistakes count more than small ones.
- **In Simple Words:** Like MAE, but a single huge error pulls the score up sharply.
- **Real-Life Example:** In hospital vitals prediction, being off by 30 points is far worse than being off by 5 — RMSE reflects that.

**Practical rule:** If **RMSE ≫ MAE**, investigate **outliers** or weak segments. If **RMSE ≈ MAE**, errors are fairly uniform.

![MAE vs RMSE: How Each Metric Handles Large Errors](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/mae_vs_rmse_comparison.png)

---

### R-Squared (R²)

**R-Squared:**

- **Official Definition:** The proportion of target **variance** explained by the model compared to always predicting the **mean**.
- **In Simple Words:** How much better you are than guessing the class average every time.
- **Real-Life Example:** R² = 0.85 means the model explains 85% of why scores spread above and below the average.

| R² | Plain meaning |
|---|---|
| ~1.0 | Excellent fit on this test set |
| 0.6 – 0.85 | Good — substantial pattern captured |
| ~0.0 | No better than mean baseline |
| Negative | Worse than always predicting the mean |

**Important:** R² is **relative** — it does not say whether absolute errors are acceptable for business. Pair it with **MAE** or **RMSE**. You already saw `.score()` return R² for linear regression in the previous session; now you compute and interpret it explicitly alongside error-size metrics.

![R-Squared: How Much Variation Does the Model Explain?](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/r_squared_visualization.png)

### Quick Activity — Read Two Models

| Model | MAE | RMSE |
|---|---:|---:|
| A | ₹3,000 | ₹3,200 |
| B | ₹3,000 | ₹9,500 |

Same average miss — which model has riskier **large** mistakes? Which metric revealed that?

**Answers:** **Model B** — RMSE is much higher than MAE, signalling a few very bad predictions.

---

## Metrics and Model Comparison — One Workflow

The professional pattern: **fit → predict on test → compute all metrics**. Below, the same helper evaluates Linear, Ridge, and Lasso on one split.

```python
# Imports for models, split, and metrics
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Sample data: three real features → exam_score
rng = np.random.default_rng(seed=33)
study_hours  = rng.uniform(1, 10, size=500)
sleep_hours  = rng.uniform(4, 9, size=500)
distractions = rng.uniform(0, 5, size=500)
X = np.column_stack([study_hours, sleep_hours, distractions])
y = 40 + 6.5 * study_hours + 1.8 * sleep_hours - 2.5 * distractions + rng.normal(0, 5, size=500)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

def evaluate_model(name, model):
    # Train on train only; predict on unseen test rows
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # Three complementary metrics
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)
    print(f"\n{name}:")
    print(f"  MAE  = {round(mae, 2)} marks")
    print(f"  RMSE = {round(rmse, 2)} marks")
    print(f"  R²   = {round(r2, 4)}")
    return mae, rmse, r2

evaluate_model("Linear Regression", LinearRegression())
evaluate_model("Ridge (alpha=5)", Ridge(alpha=5))
evaluate_model("Lasso (alpha=0.5)", Lasso(alpha=0.5))
```

**How the code works:**

- **`mean_absolute_error(y_test, y_pred)`** — actual first, predicted second; returns MAE in target units.
- **`mean_squared_error`** then **`np.sqrt(...)`** — standard way to get RMSE in scikit-learn.
- **`r2_score(y_test, y_pred)`** — compares model error to the mean baseline (R² = 0 reference).
- **Same test rows for all three models** — fair comparison; never report metrics on `y_train` when choosing a winner.

**How to read the output:**

- Similar MAE/RMSE across models → data was already clean; regularization helped little.
- Lower RMSE for Ridge/Lasso vs Linear → slight overfitting was reduced.
- Always check metrics in **business units** (₹, marks) — not only R².

---

## Error Analysis: Finding Patterns in Mistakes

MAE and RMSE summarise *how much* the model is wrong on average. **Error analysis** asks *where* and *for whom* — the same idea as reading a residual table in the previous session, now grouped systematically.

**Error Analysis:**

- **Official Definition:** Examining prediction errors by **feature range**, category, or segment to find systematic failure patterns.
- **In Simple Words:** "Is the model worse for low-study students? For junior hires?" — not just "average error is 5 marks."
- **Real-Life Example:** Navigation ETA error is 4 minutes on average, but 9 minutes in city traffic and 1 minute on highways. The average hid the real problem.

Start from **residuals** (`actual − predicted`), build a table, then **group** with `pd.cut` and aggregate **absolute error** per group.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(seed=77)
study_hours = rng.uniform(1, 10, size=500)
# Harder to predict when study hours are low — realistic pattern
noise = rng.normal(0, 5 + (10 - study_hours) * 0.8, size=500)
y = 40 + 7.5 * study_hours + noise
X = study_hours.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# One row per test student
results = pd.DataFrame({
    "study_hours": X_test.flatten(),
    "actual": y_test,
    "predicted": y_pred,
    "residual": y_test - y_pred,
    "abs_error": np.abs(y_test - y_pred),
})

# Bucket students: low / medium / high study hours
results["study_group"] = pd.cut(
    results["study_hours"], bins=[0, 4, 7, 10],
    labels=["Low (1-4 hrs)", "Medium (4-7 hrs)", "High (7-10 hrs)"]
)

# Average absolute error per group
print(results.groupby("study_group", observed=True)["abs_error"].agg(["count", "mean", "max"]).round(2))

# Average residual per group: positive = under-predicted, negative = over-predicted
print(results.groupby("study_group", observed=True)["residual"].mean().round(2))
```

**How the code works:**

- **`pd.cut`** splits a continuous column into labelled buckets — standard for segment-level debugging.
- **`.groupby(...).agg(...)`** shows count, mean error, and worst case per segment.
- **Mean residual near zero per group** suggests no strong bias; one group with high `mean` abs_error flags where to improve features or models.

![Error Analysis by Study Hour Group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/error_analysis_by_group.png)

**What to look for:**

- One group with much higher **avg_error** → model misses that segment; consider new features or a different model.
- Strongly **positive** average residual in a group → consistent under-prediction.
- **RMSE ≫ MAE** plus high error in one group → connect global metrics to local failure.

### Quick Activity — Deployment Readiness

Test **R² = 0.80**, but grouped analysis shows **doubled MAE** for candidates with under two years of experience.

1. Is "R² looks good" enough for HR rollout?  
2. Name one number and one table you would add to the report.

**Sample answers:** 1 → No — a strong average hides a critical segment. 2 → **MAE by experience band** and worst-case rows from error analysis.

---

## Practical Perspective: Choosing Metrics for Your Use Case

| Situation | Prefer |
|---|---|
| Explain typical error in plain language | **MAE** |
| Large errors are especially dangerous | **RMSE** (with MAE alongside) |
| Compare models on the same dataset | **R²** + **MAE** or **RMSE** |
| Before deployment | **Error analysis** by segment + beat **mean baseline** on test |

**Deployment checklist (regression):**

- Metrics computed on **held-out test** data — not training rows
- **Train vs test** gap is stable (no obvious overfitting)
- **MAE/RMSE** acceptable in real units (₹, marks, minutes)
- No critical user segment with unchecked high error
- When many features exist, compare **Linear vs Ridge vs Lasso** — best model is the one with the best **test** numbers for your use case, not the fanciest name

---

## Key Takeaways

- **Regularization** penalises extreme coefficients; **Ridge** shrinks all weights, **Lasso** can zero out useless features.
- **MAE**, **RMSE**, and **R²** are complementary — report more than one, always on **test** predictions.
- **Error analysis** turns a global average into segment-level evidence — essential before trusting a model in production.
- These tools build directly on **linear regression**, **residuals**, and **train–test splits** from the previous session; later work assumes you can compare and defend regression results numerically.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Regularization** | Penalty during training to limit coefficient size | Reduces overfitting when many features or noise exist |
| **Ridge** | L2-regularized regression; shrinks, rarely zeros coeffs | Stability when most features matter a little |
| **Lasso** | L1-regularized regression; can zero coeffs | Automatic feature selection; sparse models |
| **`alpha`** | Regularization strength in Ridge/Lasso | Higher → stronger penalty |
| **MAE** | Mean absolute error | Simple, unit-friendly typical error |
| **RMSE** | Root mean squared error | Weights large mistakes more heavily |
| **R²** | Variance explained vs mean baseline | Compare relative fit; pair with MAE/RMSE |
| **Error analysis** | Group errors by feature bins or segments | Finds *where* the model fails |
| **`Ridge(alpha=...)`** / **`Lasso(alpha=...)`** | Regularized models | `sklearn.linear_model` |
| **`mean_absolute_error(y, y_pred)`** | Computes MAE | `sklearn.metrics` |
| **`mean_squared_error` + `np.sqrt`** | Computes RMSE | Standard two-step pattern |
| **`r2_score(y, y_pred)`** | Computes R² | 0 ≈ mean baseline |
| **`pd.cut(col, bins, labels)`** | Bucket continuous values | Core tool for grouped error analysis |
| **`.groupby().agg()`** | Summary stats per group | Segment-level MAE and bias checks |
