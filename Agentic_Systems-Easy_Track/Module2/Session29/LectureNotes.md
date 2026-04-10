# Regression: Regularization and Evaluation

---

## Where We Left Off — and Where We Are Going

In the previous session, we built a complete linear regression model. We learned how it trains on data, generates predictions, and how we check for overfitting using a train-test split. We also learned about residuals — the individual gaps between actual and predicted values. But two important questions were left unanswered: *What do you do when your model is overfitting?* And *how do you measure your model's performance in a single, trustworthy number?* This session answers both of those questions directly.

---

## Regularization: Keeping the Model from Getting Too Clever

When a model overfits, it means it has learned too aggressively from the training data — it has memorised even the noise and random quirks. One powerful way to fix this is called **regularization**. Think of regularization as a penalty system that prevents the model from assigning extremely large coefficients to its features.

**Regularization:**
- **Official Definition:** A technique that adds a penalty to the model's learning process to discourage it from assigning excessively large weights to features, reducing overfitting and improving generalisation.
- **In Simple Words:** You tell the model: "Yes, try to be accurate — but don't go overboard. If you make your coefficients too extreme, I will penalise you for it." This keeps the model's formula simpler and more stable.
- **Real-Life Example:** Imagine a new intern who is so eager to impress that they over-customise every report with unnecessary complexity — making it impossible to reuse for future projects. A good manager would say: "Be accurate, but keep it simple and reusable." Regularization is that manager.

Without regularization, a model with many features can end up assigning very large coefficients — essentially betting everything on a few features while ignoring others. This makes the model fragile: a small change in input data leads to wildly different predictions. Regularization avoids this fragility by keeping coefficient sizes in check.

---

**The two types of regularization you need to know:**

### Ridge Regression

**Ridge Regression:**
- **Official Definition:** A regularized version of linear regression that adds a penalty proportional to the sum of the squared values of all coefficients, forcing them to stay small but never reducing any to exactly zero.
- **In Simple Words:** Ridge says: "All features can stay in the model, but I will shrink their multipliers if they are getting too large." It reduces the impact of less useful features without removing them.
- **Real-Life Example:** A restaurant menu review system rates all dishes, but for dishes that are rarely ordered, it gives them a lower weight — still keeping them on the menu, but not letting them dominate the overall restaurant score.

**Key behaviour of Ridge:**
- All features remain in the model — none are dropped.
- Coefficients are shrunk toward zero, but no coefficient ever becomes exactly zero.
- Best used when you believe most features contribute at least a little bit, and you want to reduce their overall scale.
- The strength of the shrinkage is controlled by a setting called **alpha** — a higher alpha means stronger penalty, smaller coefficients.

---

### Lasso Regression

**Lasso Regression:**
- **Official Definition:** A regularized version of linear regression that adds a penalty proportional to the sum of the absolute values of all coefficients — this can reduce some coefficients all the way to exactly zero, effectively removing those features from the model.
- **In Simple Words:** Lasso is more aggressive than Ridge. If a feature is not useful, Lasso will zero out its coefficient completely — it is a built-in feature elimination tool.
- **Real-Life Example:** Imagine a talent show where low-performing contestants are fully eliminated in each round, not just given a lower score. Ridge keeps everyone but reduces loud voices — Lasso kicks the irrelevant ones out entirely.

**Key behaviour of Lasso:**
- Some coefficients are reduced to exactly zero — those features are effectively removed.
- The resulting model is **sparse** — only the most important features survive.
- Best used when you suspect many of your features are irrelevant and you want the model to automatically identify and discard them.
- Also controlled by **alpha** — a higher alpha means more features get zeroed out.

---

**Side-by-side comparison: Linear vs Ridge vs Lasso**

![Regularization: Ridge vs Lasso — What Happens to Coefficients](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/ridge_vs_lasso_coefficients.png)

| | **Linear Regression** | **Ridge Regression** | **Lasso Regression** |
|---|---|---|---|
| Penalty applied? | No | Yes — on squared coefficients | Yes — on absolute coefficients |
| Can coefficients reach zero? | No restriction | No — only shrunk | Yes — some go to exactly zero |
| Feature elimination? | No | No | Yes |
| Best when | Data is clean, few features | Many features, all somewhat relevant | Many features, most irrelevant |
| Overfitting risk | Higher | Lower | Lower |

---

## Model Comparison: Seeing Regularization in Action

Understanding the theory of Ridge and Lasso is useful, but seeing them work on actual data makes the concept concrete. The key thing to compare is what happens to the coefficients as regularization strength (alpha) increases.

**Example dataset for the snippet below:** **300** student rows (`seed=42`). Five features — `study_hours`, `sleep_hours`, `attendance`, `distractions`, `random_noise` — and target **`exam_score`** built from the formula in the code (`random_noise` does not belong in the true score). **First 10 rows** (values rounded):

| study_hours | sleep_hours | attendance | distractions | random_noise | exam_score |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 7.97 | 7.89 | 79.10 | 2.34 | 5.66 | 123.50 |
| 4.95 | 4.67 | 90.46 | 1.30 | 5.51 | 97.63 |
| 8.73 | 6.68 | 96.13 | 0.23 | 8.29 | 126.50 |
| 7.28 | 6.57 | 88.83 | 2.41 | 7.11 | 117.65 |
| 1.85 | 8.29 | 98.53 | 4.80 | 0.27 | 88.43 |
| 9.78 | 6.31 | 91.28 | 3.26 | 0.49 | 129.21 |
| 7.85 | 5.93 | 94.67 | 2.48 | 6.02 | 113.00 |
| 8.07 | 7.20 | 64.56 | 0.55 | 4.86 | 110.71 |
| 2.15 | 5.33 | 89.30 | 1.26 | 2.60 | 78.05 |
| 5.05 | 4.70 | 77.60 | 1.47 | 4.19 | 88.86 |

---

**Complete Code: Comparing Linear, Ridge, and Lasso on the Same Data**

```python
# Import numpy for data creation and numerical operations
import numpy as np

# Import the three regression models we want to compare
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Import train_test_split to separate training and test data
from sklearn.model_selection import train_test_split

# Set a seed so results are identical every time we run this
rng = np.random.default_rng(seed=42)

# Create 300 students with 5 features each
# Features: study_hours, sleep_hours, attendance, distractions, random_noise_column
n_samples = 300

# Feature 1: study hours — genuinely useful (1 to 10)
study_hours = rng.uniform(1, 10, size=n_samples)

# Feature 2: sleep hours — moderately useful (4 to 9)
sleep_hours = rng.uniform(4, 9, size=n_samples)

# Feature 3: attendance percentage — genuinely useful (60 to 100)
attendance = rng.uniform(60, 100, size=n_samples)

# Feature 4: daily distraction hours — slightly negative impact (0 to 5)
distractions = rng.uniform(0, 5, size=n_samples)

# Feature 5: a completely random column — no real relationship to score
random_noise = rng.uniform(0, 10, size=n_samples)

# Stack all features into a 2D array (300 rows x 5 columns)
X = np.column_stack([study_hours, sleep_hours, attendance, distractions, random_noise])

# Build exam scores using only the genuinely important features + noise
scores = (
    40                       # base score
    + 6.0 * study_hours      # more study = higher score
    + 1.5 * sleep_hours      # more sleep helps slightly
    + 0.3 * attendance       # attendance has small positive impact
    - 2.0 * distractions     # distractions hurt the score
    + rng.normal(0, 5, size=n_samples)  # random noise to simulate real data
)
y = scores

# Split: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Model 1: Plain Linear Regression (no regularization) ---
lr = LinearRegression()
lr.fit(X_train, y_train)

# --- Model 2: Ridge Regression (alpha=10 — moderate shrinkage) ---
ridge = Ridge(alpha=10)
ridge.fit(X_train, y_train)

# --- Model 3: Lasso Regression (alpha=1 — will zero out weak features) ---
lasso = Lasso(alpha=1)
lasso.fit(X_train, y_train)

# Feature names to label each coefficient clearly
feature_names = ["study_hours", "sleep_hours", "attendance", "distractions", "random_noise"]

# Print the learned coefficients from all three models side by side
print("Learned Coefficients Comparison:")
print(f"{'Feature':<18} {'Linear':>10} {'Ridge':>10} {'Lasso':>10}")
print("-" * 52)
for i, name in enumerate(feature_names):
    print(f"{name:<18} {lr.coef_[i]:>10.3f} {ridge.coef_[i]:>10.3f} {lasso.coef_[i]:>10.3f}")

# Print test-set predictions for the first 3 students from each model
print("\nPrediction comparison on 3 test students:")
for i in range(3):
    lr_pred    = lr.predict(X_test[i].reshape(1, -1))[0]
    ridge_pred = ridge.predict(X_test[i].reshape(1, -1))[0]
    lasso_pred = lasso.predict(X_test[i].reshape(1, -1))[0]
    actual     = y_test[i]
    print(f"Student {i+1}: Actual={round(actual,1)}, Linear={round(lr_pred,1)}, Ridge={round(ridge_pred,1)}, Lasso={round(lasso_pred,1)}")
```

**How the code works:**

- **`np.column_stack([...])`** — Combines the 5 individual feature arrays into one table with 300 rows and 5 columns. Each row is one student.
- **The score formula** — Deliberately built so that `study_hours`, `sleep_hours`, `attendance`, and `distractions` are meaningful, but `random_noise` has zero real relationship to the score. This lets us verify whether Lasso zeros out the noise column.
- **`Ridge(alpha=10)`** — Creates a Ridge model with moderate penalty strength. Higher alpha → stronger shrinkage → smaller coefficients across all features.
- **`Lasso(alpha=1)`** — Creates a Lasso model. Because Lasso eliminates weak features, you should see `random_noise` coefficient drop to exactly 0.0 in the output.
- **The coefficient table** — Lets you visually compare how each model treats the same features. Linear regression may assign a notable (but misleading) coefficient to `random_noise`. Ridge shrinks it. Lasso zeroes it.
- **`X_test[i].reshape(1, -1)`** — Takes a single student's row and reshapes it so scikit-learn can process it as a one-row table for prediction.

---

**What to observe in the output:**

- The `random_noise` coefficient in Linear Regression will be small but nonzero — the model mistakenly assigned some weight to it.
- In Ridge, the `random_noise` coefficient will be smaller but still present.
- In Lasso, the `random_noise` coefficient should be exactly 0.0 — it was eliminated.
- The genuinely important features (`study_hours`, `distractions`) will retain meaningful coefficients in all three models.

This comparison demonstrates exactly why regularization exists — to prevent models from over-relying on features that happen to look useful in training data but aren't genuinely predictive.

---

## Evaluation Metrics: Measuring How Good Your Predictions Are

After training a model and generating predictions, you need a way to summarise its overall accuracy in a single number. This is what **evaluation metrics** do. For regression problems, there are three metrics you will use constantly: **MAE**, **RMSE**, and **R-squared**.

Each metric answers a slightly different question about your model's performance — and choosing the right one for the right situation is a practical skill.

---

### MAE — Mean Absolute Error

**MAE:**
- **Official Definition:** The average of the absolute differences between actual values and predicted values across all data points.
- **In Simple Words:** For every prediction, you check how far off it was — ignoring the direction (whether it predicted too high or too low). Then you average all those distances. The result tells you: on average, how many units is the model off by?
- **Real-Life Example:** If your food delivery app predicted arrival times for 100 orders, and you measured how many minutes it was off for each (ignoring whether it was early or late), MAE is the average of those minute-gaps. An MAE of 4.5 means the app is off by 4.5 minutes on average.

**What MAE tells you:**
- It is in the **same units as your target variable** — easy to interpret directly.
- An MAE of 500 on house prices (in rupees) means the model is off by ₹500 on average — meaningful and readable.
- It treats all errors equally — a 10-unit error counts exactly twice as much as a 5-unit error, no more.
- It is **not sensitive to outliers** — one wildly wrong prediction doesn't dominate the metric.

---

### RMSE — Root Mean Squared Error

**RMSE:**
- **Official Definition:** The square root of the average of the squared differences between actual values and predicted values — it penalises large errors more heavily than small ones.
- **In Simple Words:** Similar to MAE, but before averaging, you square each error. This makes big errors count much more than small ones. Then you take the square root to bring the result back to the original unit scale.
- **Real-Life Example:** In a hospital predicting patient blood pressure, being off by 30 points is much more dangerous than being off by 5 points. RMSE would penalise the 30-point error far more — making it the right metric when large mistakes are especially costly.

**What RMSE tells you:**
- Also in the **same units as your target variable** — readable.
- Higher RMSE than MAE signals that the model has some predictions that are very far off (outliers pulling the metric up).
- If RMSE ≈ MAE — errors are uniformly distributed, no extreme outliers.
- If RMSE >> MAE — the model is making a few very large mistakes that need attention.
- It is **sensitive to outliers** — use it when large errors are disproportionately harmful in your use case.

![MAE vs RMSE: How Each Metric Handles Large Errors](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/mae_vs_rmse_comparison.png)

---

### R-Squared — The Proportion of Variance Explained

**R-Squared (R²):**
- **Official Definition:** A metric that measures how much of the variation in the target variable is explained by the model, expressed as a value between 0 and 1 (or sometimes negative for very bad models).
- **In Simple Words:** If you know nothing about a student's study hours and you had to guess their exam score, you'd guess the class average. R-squared measures how much better your model is compared to that simple "always guess the average" strategy.
- **Real-Life Example:** If student scores range widely — some score 40, others 95 — and a model that only predicts the class average (70) for everyone has huge errors. An R² of 0.85 means your model explains 85% of that spread — it knows *why* some students score 40 and others 95.

**What R-squared values mean:**

| R² Value | What It Means |
|---|---|
| 1.0 | Perfect predictions — the model explains all variation |
| 0.85 – 0.99 | Excellent — model captures most of the pattern |
| 0.60 – 0.84 | Good — substantial explanatory power |
| 0.30 – 0.59 | Moderate — some signal captured, some missed |
| Below 0.30 | Weak — model barely better than guessing the average |
| 0.0 | The model is equivalent to always predicting the mean |
| Negative | The model is worse than simply predicting the mean — something is wrong |

**Important:** R-squared is a relative measure. It doesn't tell you if the model's absolute errors are acceptable for your use case — only MAE or RMSE can tell you that. Always use R-squared alongside MAE or RMSE, not instead of them.

![R-Squared: How Much Variation Does the Model Explain?](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/r_squared_visualization.png)

---

**Example dataset for the snippet below:** **400** rows, one feature **`study_hours`** and target **`exam_score`** (`seed=21`, then 80/20 split with `random_state=1`). **First 10 rows** (rounded):

| study_hours | exam_score |
| ---: | ---: |
| 8.03 | 93.14 |
| 6.45 | 85.97 |
| 7.39 | 104.29 |
| 1.80 | 50.18 |
| 6.68 | 89.97 |
| 9.83 | 117.54 |
| 4.81 | 77.90 |
| 2.01 | 53.16 |
| 9.62 | 122.40 |
| 7.08 | 101.20 |

---

**Complete Code: Computing MAE, RMSE, and R-Squared**

```python
# Import numpy for numerical operations
import numpy as np
import matplotlib.pyplot as plt

# Import LinearRegression for our model
from sklearn.linear_model import LinearRegression

# Import train_test_split to get a fair test set
from sklearn.model_selection import train_test_split

# Import the three evaluation metric functions from scikit-learn
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Set seed for reproducibility
rng = np.random.default_rng(seed=21)

# Create 400 students with study hours as the single feature
study_hours = rng.uniform(1, 10, size=400)

# Create exam scores with a realistic formula and noise
scores = 40 + 7.5 * study_hours + rng.normal(0, 6, size=400)

# Reshape feature for scikit-learn
X = study_hours.reshape(-1, 1)
y = scores

# Split into 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create and train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions on the test set — these are students the model never saw
y_pred = model.predict(X_test)

# --- Metric 1: MAE ---
# mean_absolute_error computes the average of abs(actual - predicted)
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE  (Mean Absolute Error):  {round(mae, 2)} marks")
print(f"  → On average, the model's predictions are off by {round(mae, 2)} marks")

# --- Metric 2: RMSE ---
# mean_squared_error gives the average of squared errors
# We take the square root manually to get RMSE in the original unit (marks)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nRMSE (Root Mean Squared Error): {round(rmse, 2)} marks")
print(f"  → RMSE penalises big mistakes more — compare to MAE to detect outlier errors")

# --- Metric 3: R-Squared ---
# r2_score computes how much better the model is vs always predicting the mean
r2 = r2_score(y_test, y_pred)
print(f"\nR²   (R-Squared):               {round(r2, 4)}")
print(f"  → The model explains {round(r2 * 100, 1)}% of the variation in exam scores")

# --- Comparison: Model vs Baseline (always predict the mean) ---
# The "dumb baseline" always predicts the average score
mean_score = y_train.mean()

# Create baseline predictions: the same value (mean) for every test student
baseline_pred = np.full(shape=len(y_test), fill_value=mean_score)

# Compute MAE for the baseline
baseline_mae = mean_absolute_error(y_test, baseline_pred)
print(f"\nBaseline MAE (always predict mean): {round(baseline_mae, 2)} marks")
print(f"Our model MAE:                       {round(mae, 2)} marks")
print(f"Improvement over baseline:           {round(baseline_mae - mae, 2)} marks")


# The following is for Visualization of the data
plt.figure()
plt.scatter(y_test, y_pred)

# Perfect prediction line
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])

plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted (R² Visualization)")
plt.show()
```
**The Following is the Visulization of the above 

**How the code works:**

- **`mean_absolute_error(y_test, y_pred)`** — Takes actual values and predictions, computes the absolute difference for each, then returns the average. Both arguments must be in the same order: actual first, predicted second.
- **`mean_squared_error(y_test, y_pred)`** — Squares each error before averaging, making large errors count much more. Returns the MSE (not yet RMSE).
- **`np.sqrt(mse)`** — Takes the square root of MSE to bring the result back to the original unit (marks, rupees, minutes — whatever your target is). scikit-learn doesn't have a standalone RMSE function, so this two-step approach is standard.
- **`r2_score(y_test, y_pred)`** — Computes R-squared by comparing the model's total error to the total error of a "predict the mean" baseline. A value of 0.82 means the model explains 82% of the spread in scores.
- **`np.full(shape=len(y_test), fill_value=mean_score)`** — Creates an array of the same length as the test set, filled entirely with the training mean. This simulates the dumbest possible model — one that always predicts the average regardless of input.
- **The baseline comparison** — Demonstrates that R-squared's 0.0 reference point is exactly this baseline. If your model can't beat the baseline's MAE, something is seriously wrong.

---

## Error Analysis: Finding Patterns in Your Model's Mistakes

Computing a single number like MAE or RMSE tells you *how much* the model is wrong on average. But it doesn't tell you *when* the model is wrong, or *which kinds of inputs* it struggles with. That deeper investigation is called **error analysis**.

**Error Analysis:**
- **Official Definition:** The process of systematically examining a model's prediction errors to identify whether those errors follow a pattern — grouped by a feature value, prediction range, or data segment.
- **In Simple Words:** Instead of asking "what is my model's average error?", you ask "is the model worse for certain types of students? Does it fail more for students who study very few hours? Or very many hours?"
- **Real-Life Example:** A navigation app calculates that its average ETA error is 4 minutes. But when engineers break it down, they find it is only 1 minute off for highway routes but 9 minutes off for city routes. That breakdown — that's error analysis. The average hid the real problem.

Error analysis almost always starts with residuals (which we computed in Session 28) and groups them to find patterns.

---

**Example dataset for the snippet below:** **500** rows (`seed=77`). Feature **`study_hours`**, target **`exam_score`**, with noise **larger for lower study hours** (as in the code). After `train_test_split(..., random_state=5)`, analysis uses test rows only. **First 10 rows** of the full generated table (rounded):

| study_hours | exam_score |
| ---: | ---: |
| 8.07 | 108.51 |
| 5.96 | 89.92 |
| 3.19 | 70.60 |
| 4.01 | 73.03 |
| 3.87 | 86.08 |
| 4.51 | 67.87 |
| 8.21 | 103.69 |
| 1.82 | 41.95 |
| 4.36 | 88.14 |
| 8.12 | 94.65 |

---

**Complete Code: Systematic Error Analysis by Feature Group**

```python
# Import numpy for array operations
import numpy as np

# Import pandas for easy data grouping and display
import pandas as pd

# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Import train_test_split
from sklearn.model_selection import train_test_split

# Set seed for reproducibility
rng = np.random.default_rng(seed=77)

# Create 500 students with study hours between 1 and 10
study_hours = rng.uniform(1, 10, size=500)

# Build exam scores — note: the noise is intentionally larger for low-study students
# This simulates a real pattern: low-study students are harder to predict
noise = rng.normal(0, 5 + (10 - study_hours) * 0.8, size=500)
scores = 40 + 7.5 * study_hours + noise
y = scores

# Reshape for scikit-learn
X = study_hours.reshape(-1, 1)

# Split: 80% training, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Generate predictions on test data
y_pred = model.predict(X_test)

# Calculate residuals for every test student
residuals = y_test - y_pred

# Build a dataframe to group and analyse residuals
results_df = pd.DataFrame({
    "study_hours": X_test.flatten(),    # the feature value for each test student
    "actual_score": y_test,             # the real exam score
    "predicted_score": y_pred,          # the model's prediction
    "residual": residuals,              # actual minus predicted
    "abs_error": abs(residuals)         # absolute error (ignoring direction)
})

# Create study-hour groups: low (1-4 hours), medium (4-7 hours), high (7-10 hours)
bins = [0, 4, 7, 10]
labels = ["Low (1-4 hrs)", "Medium (4-7 hrs)", "High (7-10 hrs)"]
results_df["study_group"] = pd.cut(results_df["study_hours"], bins=bins, labels=labels)

# Group by study_group and compute average absolute error for each group
group_analysis = results_df.groupby("study_group", observed=True)["abs_error"].agg(
    count="count",                     # how many students in each group
    avg_error="mean",                  # average absolute error for the group
    max_error="max"                    # worst single prediction in the group
).round(2)

# Print the grouped error table
print("Error Analysis by Study Hour Group:")
print(group_analysis.to_string())

# Flag the top 5 worst predictions — students the model got most wrong
print("\nTop 5 worst predictions:")
worst_5 = results_df.nlargest(5, "abs_error")[
    ["study_hours", "actual_score", "predicted_score", "residual"]
].round(2)
print(worst_5.to_string(index=False))

# Check for systematic bias: is the average residual per group near zero?
print("\nAverage residual per group (positive = under-predicted, negative = over-predicted):")
bias_check = results_df.groupby("study_group", observed=True)["residual"].mean().round(2)
print(bias_check.to_string())
```

**How the code works:**

- **`pd.DataFrame({...})`** — Creates a structured table with one row per test student, storing their feature value, actual score, predicted score, residual, and absolute error all together. This makes grouping easy.
- **`pd.cut(results_df["study_hours"], bins=bins, labels=labels)`** — Divides students into three buckets based on their study hours: Low (1–4 hrs), Medium (4–7 hrs), High (7–10 hrs). This is a standard error analysis technique — grouping errors by feature range.
- **`.groupby("study_group")["abs_error"].agg(...)`** — For each study group, computes the count of students, the average absolute error, and the maximum single error. If the model struggles more for one group, the `avg_error` for that group will be noticeably higher.
- **`results_df.nlargest(5, "abs_error")`** — Selects the 5 rows where the model was most wrong. These are the outlier cases — worth inspecting individually to understand if they represent data quality issues or genuinely unusual students.
- **The bias check** — If a group's average residual is consistently positive, the model is under-predicting for that group. If negative, it is over-predicting. A balanced model should have averages close to zero across all groups.

---

![Error Analysis by Study Hour Group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session29/error_analysis_by_group.png)

**What to look for in error analysis results:**

- **One group has much higher average error than others** → The model is not capturing that group well. Consider adding more features that distinguish that group.
- **A group has strongly positive average residual** → The model consistently under-predicts for those cases. It might be missing a feature that boosts scores for that group.
- **A group has strongly negative average residual** → The model consistently over-predicts. The relationship in that range may not be linear.
- **The worst 5 predictions are all from the same group** → That is where the model needs the most improvement.

---

## Practical Perspective: Choosing the Right Metric for the Right Situation

Having three metrics — MAE, RMSE, and R-squared — can feel overwhelming. But in practice, choosing between them is straightforward once you understand what each one prioritises.

**The practical decision guide:**

- **Use MAE when:**
  - You want a simple, easily explainable error number.
  - All prediction errors are roughly equally important — a ₹500 error is twice as bad as a ₹250 error, nothing more.
  - Your stakeholders need a metric in plain language: "on average, we are off by ₹450."
  - Examples: delivery time estimation, exam score prediction, energy bill forecasting.

- **Use RMSE when:**
  - Large errors are disproportionately harmful — a prediction that's wildly off is much worse than one that's slightly off.
  - You want the metric to flag outlier errors automatically.
  - Examples: financial forecasting, medical measurement prediction, safety-critical applications where large mistakes are dangerous.

- **Use R-squared when:**
  - You want to communicate how well the model explains variation in the target, relative to knowing nothing about the inputs.
  - You are comparing two different models on the same dataset — the model with higher R-squared explains more of the pattern.
  - You want a normalised measure that doesn't depend on the scale of the target variable.

---

**Example dataset for the snippet below:** **500** rows (`seed=33`). Features **`study_hours`**, **`sleep_hours`**, **`distractions`**, target **`exam_score`** from the formula in the code; 80/20 split with `random_state=10`. **First 10 rows** (rounded):

| study_hours | sleep_hours | distractions | exam_score |
| ---: | ---: | ---: | ---: |
| 4.99 | 7.60 | 4.33 | 74.70 |
| 6.12 | 5.58 | 1.00 | 85.49 |
| 9.17 | 7.26 | 3.27 | 99.55 |
| 3.29 | 6.54 | 0.64 | 70.59 |
| 6.30 | 5.71 | 4.15 | 79.49 |
| 4.23 | 7.66 | 4.46 | 74.47 |
| 7.81 | 7.58 | 4.94 | 89.72 |
| 5.89 | 8.51 | 2.33 | 99.17 |
| 2.82 | 8.02 | 0.84 | 67.02 |
| 5.64 | 8.30 | 1.11 | 88.98 |

---

**Complete Code: Comparing Models Using Multiple Metrics**

```python
# Import numpy for data and calculations
import numpy as np

# Import the three regression model types
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Import train_test_split for honest evaluation
from sklearn.model_selection import train_test_split

# Import all three evaluation metric functions
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Set seed for consistent results
rng = np.random.default_rng(seed=33)

# Create 500 students with 3 features
study_hours  = rng.uniform(1, 10, size=500)
sleep_hours  = rng.uniform(4, 9,  size=500)
distractions = rng.uniform(0, 5,  size=500)

# Stack into a feature table
X = np.column_stack([study_hours, sleep_hours, distractions])

# Build scores using a known formula
y = 40 + 6.5 * study_hours + 1.8 * sleep_hours - 2.5 * distractions + rng.normal(0, 5, size=500)

# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Define a helper function to evaluate any model and print all three metrics
def evaluate_model(name, model, X_train, y_train, X_test, y_test):
    # Train the model on training data
    model.fit(X_train, y_train)
    # Predict on the unseen test data
    y_pred = model.predict(X_test)
    # Compute all three metrics
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)
    # Print the results with the model name as a label
    print(f"\n{name}:")
    print(f"  MAE  = {round(mae, 2):>8} marks  (average absolute error)")
    print(f"  RMSE = {round(rmse, 2):>8} marks  (penalises large errors more)")
    print(f"  R²   = {round(r2, 4):>8}       (proportion of variation explained)")
    # Return metrics so we can compare later
    return {"model": name, "MAE": round(mae,2), "RMSE": round(rmse,2), "R2": round(r2,4)}

# Evaluate all three models using the same function
results = []
results.append(evaluate_model("Linear Regression", LinearRegression(),  X_train, y_train, X_test, y_test))
results.append(evaluate_model("Ridge (alpha=5)",   Ridge(alpha=5),      X_train, y_train, X_test, y_test))
results.append(evaluate_model("Lasso (alpha=0.5)", Lasso(alpha=0.5),    X_train, y_train, X_test, y_test))

# Print a clean summary table
print("\n\nSummary Comparison Table:")
print(f"{'Model':<25} {'MAE':>8} {'RMSE':>8} {'R2':>8}")
print("-" * 53)
for r in results:
    print(f"{r['model']:<25} {r['MAE']:>8} {r['RMSE']:>8} {r['R2']:>8}")
```

**How the code works:**

- **`evaluate_model()` function** — Wraps the fit → predict → evaluate workflow into a reusable block. Instead of writing the same metric code three times, we define it once and call it for each model. This is a standard professional pattern.
- **`model.fit(X_train, y_train)` inside the function** — Each model is trained fresh on the same training data, ensuring a fair comparison.
- **`model.predict(X_test)`** — All three models generate predictions on the same test set — same questions, different model answers.
- **The three metric functions** — `mean_absolute_error`, `mean_squared_error`, and `r2_score` from scikit-learn handle all the computation. We just pass in actual values and predictions.
- **`results.append(...)`** — Collects each model's metrics into a list so we can build a side-by-side comparison table at the end.
- **The summary table** — Lets you see at a glance which model wins on which metric. In this scenario, Ridge and Lasso should perform comparably to or slightly better than plain Linear Regression because the data has genuine patterns and regularization helps keep the model generalised.

---

**How to read the comparison output:**

- If all three models show very similar MAE and RMSE → regularization didn't help much (data is clean, linear regression already generalised well).
- If Ridge or Lasso shows noticeably lower RMSE than Linear Regression → the original model was slightly overfitting, and regularization fixed it.
- If R-squared is similar across models → all three models are capturing roughly the same amount of pattern from the data.

The practical takeaway: in real projects, always try all three models and compare using metrics. The best model is not the one with the fanciest name — it is the one with the best numbers on your specific dataset and use case.

---

## Quick Reference: Important Terms, Tools, and Python Commands

| Term / Tool | What It Means | Why It Matters |
|---|---|---|
| **Regularization** | Penalty added during training to keep coefficients from becoming too large | Prevents overfitting by discouraging overcomplicated formulas |
| **Ridge Regression** | Regularized model that shrinks all coefficients but never to zero | Use when all features are somewhat relevant; keeps the model stable |
| **Lasso Regression** | Regularized model that can reduce some coefficients exactly to zero | Built-in feature selection; eliminates irrelevant features automatically |
| **alpha** | Strength setting for regularization penalty in Ridge and Lasso | Higher alpha = stronger penalty = smaller / fewer coefficients |
| **Sparse model** | A model where most feature coefficients are zero (Lasso result) | Simpler, more interpretable model with automatic feature elimination |
| **MAE** | Average absolute difference between actual and predicted values | Simple, unit-friendly error — use when all mistakes are equally costly |
| **RMSE** | Square root of average squared errors — penalises large errors heavily | Use when large mistakes are especially dangerous or unacceptable |
| **R-squared (R²)** | Proportion of target variation explained by the model (0 to 1 scale) | Relative measure of fit — compare models; not a standalone accuracy metric |
| **Error Analysis** | Grouping prediction errors by feature range or category to find patterns | Reveals *where* and *when* the model fails, not just *how much* |
| **Baseline model** | A trivially simple model (e.g., always predict the mean) used as a comparison | R² = 0 corresponds to this baseline; any useful model must beat it |
| **`Ridge(alpha=...)`** | Creates a Ridge regression model with specified penalty strength | Import from `sklearn.linear_model` |
| **`Lasso(alpha=...)`** | Creates a Lasso regression model with specified penalty strength | Import from `sklearn.linear_model` |
| **`mean_absolute_error(y, y_pred)`** | Computes MAE between actual and predicted arrays | Import from `sklearn.metrics` |
| **`mean_squared_error(y, y_pred)`** | Computes MSE; use `np.sqrt()` on result to get RMSE | Import from `sklearn.metrics` |
| **`r2_score(y, y_pred)`** | Computes R-squared; 1.0 is perfect, 0.0 = predicting the mean | Import from `sklearn.metrics` |
| **`pd.cut(col, bins, labels)`** | Divides a continuous column into labelled groups/buckets | Used in error analysis to group errors by feature range |
| **`.groupby().agg()`** | Groups rows by a category and applies summary statistics to each group | Core pandas operation for error analysis breakdowns |
| **`.nlargest(n, column)`** | Returns the n rows with the largest values in a specified column | Used to find the worst predictions — outlier investigation tool |
| **`np.full(shape, fill_value)`** | Creates an array of fixed length filled with one repeated value | Used to create baseline predictions (always predict the mean) |

---

*End of Lecture Notes — Session 29: Regression / Regularization and Evaluation*
