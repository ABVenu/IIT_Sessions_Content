# Regression: Linear Regression Fundamentals

## Context of This Session

In the previous session, you learned how models can look brilliant in a notebook and fail in real life. You studied **data leakage** — why test information must never sneak into training — and built a **split-first, train-only preprocessing** habit. You also saw **class imbalance**, why **accuracy** can mislead, and how ideas like **precision**, **recall**, resampling, and **cross-validation** help you evaluate models more honestly.

Until now, most of your ML examples asked *which category* something belongs to. Today the question changes shape: *what number should we expect?* You will meet **regression** — predicting continuous values like salary, house price, or delivery time — and train your first numeric model: **linear regression**.

**In this session, you will:**

- Contrast **regression** with **classification** using everyday examples
- Build intuition for the **best-fit line**, **features**, **target**, **slope**, and **intercept**
- **Fit** and **predict** with `LinearRegression` in Google Colab on a pre-cleaned numeric dataset
- Compare your model to a **mean-label baseline** on the same train–test split
- Spot **overfitting** briefly by comparing train vs test error
- Understand **residuals** and read a simple residual plot — with a pointer to regression metrics and classification topics ahead

---

## Regression for Continuous Targets

Machine learning problems usually fall into two families. **Classification** picks a label from a fixed list. **Regression** estimates a number on a scale.

**Regression:**

- **Official Definition:** A supervised machine learning task where the model learns to predict a **continuous numeric output** (the target) from input **features**.
- **In Simple Words:** You show the computer past examples where the answer is a number — like ₹45,000 or 72 minutes — and it learns a pattern to guess new numbers.
- **Real-Life Example:** A food-delivery app does not only say “late or on time.” It says **“32 minutes”** — that specific minute count is a regression answer.

**Classification (quick contrast):**

- **Official Definition:** A supervised task where the model predicts a **category** or **class label** from features.
- **In Simple Words:** The answer is a box — spam or not spam, pass or fail, fraud or genuine.
- **Real-Life Example:** Your email app sorting mail into **Inbox** vs **Promotions** — fixed categories, not a measured quantity.

| Question type | Example question | Type of answer |
|---|---|---|
| How much? | What will this flat sell for? | **Regression** (₹ amount) |
| How many? | How many units will we sell next month? | **Regression** (count) |
| Which one? | Is this transaction fraud? | **Classification** (label) |
| Which bucket? | Will this student pass or fail? | **Classification** (label) |

![Regression predicts a number on a scale; classification picks a category](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_classification_vs_regression.png)

### Everyday Regression Examples

- **House price:** Given area (sq ft), locality, and building age — predict sale price in rupees.
- **Salary:** Given years of experience and weekly learning hours — predict monthly salary.
- **Delivery time:** Given distance and order size — predict minutes until arrival.

In each case the output is **measurable**, not a tick in a box. That is the signature of regression.

### Features and Target — The Vocabulary You Already Know

You have already separated **features** (inputs) and **labels** (outputs). In regression, the label is numeric — we often call it the **target**.

- **Target variable (y):**
  - **Official Definition:** The continuous numeric column the model is trained to predict.
  - **In Simple Words:** The number you are trying to guess — the “answer column.”
  - **Real-Life Example:** In a salary model, `monthly_salary_inr` is the target.

- **Feature (x):**
  - **Official Definition:** Any input column the model uses to form its prediction.
  - **In Simple Words:** The clues — experience, hours, area, distance, and so on.
  - **Real-Life Example:** Years of experience and hours of upskilling per week are features for salary.

![Target variable (y): what you predict — Features (x): the clues the model uses](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_target_and_features.png)

- **Common doubt:** A column with digits is not always regression. Values like `1 = junior, 2 = mid, 3 = senior` are **categories written as numbers**. Ask: *Is this a measurement on a scale, or a label in disguise?*

### Quick Activity — Regression or Classification?

On paper, write **R** for regression or **C** for classification next to each problem. Then check your reasoning: does the answer have to be a **specific number**, or a **named category**?

1. Predict tomorrow’s maximum temperature in °C  
2. Predict whether a loan will be **approved** or **rejected**  
3. Predict a student’s **exact exam score** out of 100  
4. Predict whether an email is **spam** or **not spam**  
5. Predict monthly **electricity bill** in rupees  

**Answer key:** 1 → R, 2 → C, 3 → R, 4 → C, 5 → R.

---

## Linear Regression Intuition — The Best-Fit Line

Once you know the answer must be a number, the next question is: *how does the model pick that number?* **Linear regression** is the simplest and most important answer — it learns a straight-line relationship (or a straight-line combination when you have many features).

**Linear Regression:**

- **Official Definition:** A regression model that predicts the target as a **weighted sum of features** plus a constant — each feature is multiplied by a learned weight and the results are added.
- **In Simple Words:** “For every extra year of experience, add ₹8,000 to the predicted salary” — the model learns those multipliers from data.
- **Real-Life Example:** A taxi meter starts at ₹30 (**intercept**) and adds ₹15 per km (**coefficient**). Linear regression learns the software version of “base fare” and “rate per km” from past trips.

### Intercept and Coefficient in Plain Language

- **Intercept (baseline on the line):**
  - **Official Definition:** A constant term added to every prediction, even when all features are zero.
  - **In Simple Words:** The model’s starting point before it looks at the clues.
  - **Real-Life Example:** A PG rent might start at ₹6,000 before adding charges for AC or food.

- **Coefficient (slope / weight per feature):**
  - **Official Definition:** The learned multiplier for each feature — how much the prediction changes when that feature increases by one unit.
  - **In Simple Words:** One more year of experience might add ₹10,000 to the predicted salary.
  - **Real-Life Example:** Each extra km of delivery distance might add ₹12 to the fare.

### The Best-Fit Line — Without Heavy Formulas

Picture 200 students on a graph: **study hours** on the horizontal axis, **exam score** on the vertical axis. Each student is a dot.

You could draw countless straight lines through that cloud — steep, flat, high, low. The **best-fit line** is the one position where the **vertical gaps** from dots to the line are collectively as small as possible. Linear regression finds that line automatically.

- With **one feature**, you can imagine one line on a scatter plot.
- With **many features**, you cannot draw it on paper — but the idea is the same: one formula that balances errors across all rows.

![Best-fit line through study hours vs exam scores — vertical gaps are residuals](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_best_fit_line.png)

### Optional Scatter Plot in Colab (One Feature)

If you want to **see** the line before training, a scatter plot helps. This is optional intuition — not required for every project.

```python
# Import matplotlib for plotting charts
import matplotlib.pyplot as plt

# Import numpy for sample numbers
import numpy as np

# Set seed so the same dots appear every run
rng = np.random.default_rng(seed=42)

# Create 80 students with study hours between 1 and 10
hours = rng.uniform(1, 10, size=80)

# Create exam scores: base 40 + 7.5 per hour + small random noise
scores = 40 + 7.5 * hours + rng.normal(0, 4, size=80)

# Draw a scatter plot: each dot is one student
plt.scatter(hours, scores, alpha=0.6, label="Students")

# Label the axes so the chart is readable
plt.xlabel("Study hours per week")
plt.ylabel("Exam score")

# Add a title
plt.title("Study hours vs exam score")

# Show a legend and display the chart
plt.legend()
plt.show()
```

**How the code works:**

- `plt.scatter(hours, scores)` places one dot per student.
- The upward trend shows that more hours tend to mean higher scores — a good candidate for linear regression.
- After you train a model, you can add a second plot line for predictions; today we focus on the **cloud of dots** and the idea of a line through them.

### Quick Activity — Intercept and Slope in Your Head

A shop prices sweets: **₹20 base** plus **₹5 per piece**.

1. How much for **0 pieces**? (This is the **intercept**.)  
2. How much for **7 pieces**? (Use intercept + 7 × coefficient.)  
3. If the price per piece rises to **₹6** but the base stays ₹20, how much for **7 pieces** now?

**Answers:** 1 → ₹20, 2 → ₹55, 3 → ₹62.

---

## Fit and Predict with Linear Regression in Colab

You already know the ML habit: **split first**, keep the test set locked away, and fit any preprocessing **only on training data**. Today’s dataset is **pre-cleaned and all numeric** — so you can focus on training and predicting without repeating scaling or encoding lessons.

**Model training:**

- **Official Definition:** Fitting a model means learning its internal parameters (intercept and coefficients) from labelled training examples by reducing prediction error.
- **In Simple Words:** The computer adjusts its formula until it matches past `(features → target)` pairs as well as it can.
- **Real-Life Example:** A new billing clerk studies 500 past invoices and learns how hours and materials usually map to the final bill.

**Prediction:**

- **Official Definition:** Applying a trained model to new inputs to produce numeric outputs — no learning happens during prediction.
- **In Simple Words:** The formula is frozen; you feed new clues and get a number back.

### The Dataset We Will Use

Imagine a small HR analytics table (already clean):

| years_experience | weekly_learning_hours | monthly_salary_inr |
|---:|---:|---:|
| 1.2 | 3.0 | 32000 |
| 3.5 | 6.0 | 48000 |
| 5.0 | 8.0 | 62000 |
| … | … | … |

- **Features (`X`):** `years_experience`, `weekly_learning_hours`  
- **Target (`y`):** `monthly_salary_inr`  

The full notebook generates **400 rows** with a realistic pattern plus noise so your learned coefficients are close to the true story.

### Complete Colab Workflow — Split, Train, Predict on Hold-Out Test

```python
# Import numpy for numbers and arrays
import numpy as np

# Import pandas for tables (DataFrames)
import pandas as pd

# Import train_test_split to separate train and test rows
from sklearn.model_selection import train_test_split

# Import LinearRegression — our first numeric prediction model
from sklearn.linear_model import LinearRegression

# Set random seed so results repeat every time you run the notebook
rng = np.random.default_rng(seed=42)

# Create 400 rows of years of experience between 0.5 and 15
years_experience = rng.uniform(0.5, 15, size=400)

# Create weekly learning hours between 0 and 15
weekly_learning_hours = rng.uniform(0, 15, size=400)

# Build salary using a hidden real rule + noise (simulates real-world messiness)
# True story: base 25k + 3.5k per year + 800 per learning hour + random variation
monthly_salary_inr = (
    25000
    + 3500 * years_experience
    + 800 * weekly_learning_hours
    + rng.normal(0, 4000, size=400)
)

# Pack features into a DataFrame (table)
df = pd.DataFrame({
    "years_experience": years_experience,
    "weekly_learning_hours": weekly_learning_hours,
    "monthly_salary_inr": monthly_salary_inr,
})

# Separate feature columns (inputs) from the target column (output)
X = df[["years_experience", "weekly_learning_hours"]]
y = df["monthly_salary_inr"]

# Split: 80% train, 20% test — same habit as before; test stays untouched during fit
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the linear regression model object
model = LinearRegression()

# Train ONLY on training rows — model learns intercept and coefficients
model.fit(X_train, y_train)

# Show the learned baseline salary (intercept)
print("Intercept (baseline ₹):", round(model.intercept_, 2))

# Show learned weight for each feature (one number per column)
print("Coefficient for years_experience:", round(model.coef_[0], 2))
print("Coefficient for weekly_learning_hours:", round(model.coef_[1], 2))

# Predict salaries for the held-out test set (rows the model never trained on)
y_test_pred = model.predict(X_test)

# Print first 5 actual vs predicted salaries for a quick sanity check
for i in range(5):
    print(
        f"Row {i + 1}: Actual ₹{round(y_test.iloc[i]):,} | "
        f"Predicted ₹{round(y_test_pred[i]):,}"
    )

# Predict salary for one new person (6 years experience, 10 hours learning per week)
new_person = pd.DataFrame({
    "years_experience": [6.0],
    "weekly_learning_hours": [10.0],
})
new_salary = model.predict(new_person)
print(f"\nNew hire prediction: ₹{round(new_salary[0]):,}")
```

**How the code works:**

- `pd.DataFrame({...})` builds the salary table from generated columns — in a real project you would use `pd.read_csv("clean_salary.csv")` instead.
- `X` holds only feature columns; `y` is a single numeric column — the regression target.
- `train_test_split(..., test_size=0.2)` holds back 20% of rows for honest checking — **split before** any step that learns from data.
- `model.fit(X_train, y_train)` is where learning happens; the test set is never passed to `.fit()`.
- `model.intercept_` and `model.coef_` store the learned baseline and per-feature multipliers after training.
- `model.predict(X_test)` applies the frozen formula to unseen rows — this mirrors real deployment.
- `model.predict(new_person)` shows the live use case: one new row in, one salary estimate out.

### What Happens Inside `.fit()` — Conceptually

The model tries many intercept and coefficient combinations. For each try it asks: *How far off are we on training rows?* It keeps adjusting until total error is as small as practical. You do not need the calculus — only the habit: **train on train, check on test, predict on new data.**

### Quick Activity — Trace One Prediction

Suppose after training you see:

- Intercept ≈ **₹26,000**  
- Coefficient for `years_experience` ≈ **₹3,400**  
- Coefficient for `weekly_learning_hours` ≈ **₹750**  

For a candidate with **4 years** experience and **5 hours** learning per week, compute by hand:

`predicted ≈ 26000 + (4 × 3400) + (5 × 750)`

Compare your hand calculation with `model.predict()` for the same inputs in Colab. Small differences are normal because the computer’s learned numbers have more decimal places.

---

## Quick Check Against a Mean Baseline

You have already used a **baseline** for classification — a deliberately simple rule so you know the floor any real model must beat. For regression, the simplest baseline is often: **always predict the average salary (or average score) from the training set.**

**Mean baseline:**

- **Official Definition:** A baseline that predicts the same value — the mean of the training targets — for every test row.
- **In Simple Words:** Ignore all features; guess the “typical” answer every time.
- **Real-Life Example:** A weather app that always says “32°C” because that was the average last week — no forecast logic, just the middle of past readings.

If linear regression cannot beat this lazy guess on the **same test split**, your features may not be helping yet — or something in the workflow needs a closer look.

### Complete Code — Linear Regression vs Mean Baseline

```python
# Import numpy for creating arrays of predictions
import numpy as np

# Import pandas for the salary table
import pandas as pd

# Import splitting and the regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Rebuild the same clean dataset (same seed as before for fair comparison)
rng = np.random.default_rng(seed=42)
years_experience = rng.uniform(0.5, 15, size=400)
weekly_learning_hours = rng.uniform(0, 15, size=400)
monthly_salary_inr = (
    25000
    + 3500 * years_experience
    + 800 * weekly_learning_hours
    + rng.normal(0, 4000, size=400)
)
df = pd.DataFrame({
    "years_experience": years_experience,
    "weekly_learning_hours": weekly_learning_hours,
    "monthly_salary_inr": monthly_salary_inr,
})
X = df[["years_experience", "weekly_learning_hours"]]
y = df["monthly_salary_inr"]

# Split once — both models must be judged on the SAME test rows
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Mean baseline: every test prediction = average training salary ---
train_mean_salary = y_train.mean()
mean_baseline_pred = np.full(shape=len(y_test), fill_value=train_mean_salary)

# Average absolute error for mean baseline on test set
mean_baseline_errors = np.abs(y_test - mean_baseline_pred)
mean_baseline_avg_error = mean_baseline_errors.mean()

# --- Linear regression model ---
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
lin_test_pred = lin_model.predict(X_test)

# Average absolute error for linear regression on the same test set
lin_test_errors = np.abs(y_test - lin_test_pred)
lin_test_avg_error = lin_test_errors.mean()

# Print comparison (lower average error is better)
print(f"Mean baseline — avg error on test: ₹{round(mean_baseline_avg_error, 2):,}")
print(f"Linear regression — avg error on test: ₹{round(lin_test_avg_error, 2):,}")

if lin_test_avg_error < mean_baseline_avg_error:
    print("Linear regression beats the mean baseline — features are adding value.")
else:
    print("Linear regression did not beat the mean baseline — investigate features or data.")
```

**How the code works:**

- `y_train.mean()` computes the average salary using **only training labels** — never peek at test targets when building the baseline.
- `np.full(..., fill_value=train_mean_salary)` creates one constant prediction per test row.
- `np.abs(y_test - predictions).mean()` is a simple **average absolute error** — easy to read in rupees; formal metrics like MAE and R² come later.
- Both models are scored on **identical** `y_test` rows so the comparison is fair.
- Beating the mean baseline does not mean the model is production-ready — it only proves the model is learning something beyond “guess the average.”

### Quick Activity — Baseline Thinking

1. If every employee in the training set earns roughly **₹50,000** on average, what will the mean baseline predict for **every** test row?  
2. Why must we compute the mean from **`y_train` only**, not from the full dataset including test?  
3. If linear regression’s test error is **₹4,200** and the mean baseline’s is **₹9,800**, did features help?

**Answers:** 1 → About ₹50,000 each time. 2 → Using the full dataset would leak test information into the baseline. 3 → Yes — lower error on the same test split means the line is doing better than “always guess average.”

---

## Overfitting and Generalization — A Short Look

A model’s real job is not to shine on old rows — it must work on **new** rows from the same world. You already guard against **leakage** and unfair evaluation; now you add **generalization** for regression.

**Overfitting:**

- **Official Definition:** The model fits training data too closely — including noise — and performs worse on unseen data.
- **In Simple Words:** It memorised past examples instead of learning the general pattern.
- **Real-Life Example:** A student memorised last year’s question paper word-for-word but failed when the paper changed slightly.

**Generalization:**

- **Official Definition:** Accurate predictions on new data drawn from the same kind of problem.
- **In Simple Words:** The formula still makes sense tomorrow, not only on yesterday’s spreadsheet.
- **Real-Life Example:** A doctor applies principles from many patients to a new patient — not one memorised file.

![Underfitting, sweet spot, overfitting — train-test split helps spot overfitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_complexity_train_test.png)

For **simple linear regression** with few features, huge train–test gaps are less common than with very flexible models. Still, the habit matters: **compare error on train vs test** on the same split.

- **Similar train and test error** → healthy sign for this level of model.  
- **Much better on train than test** → possible overfitting or a lucky/unlucky split.  
- **Both errors very high** → model may be too simple or features may be weak (**underfitting**).

Today we **do not** cover Ridge, Lasso, or cross-validation labs — those deepen control later.

### Complete Code — Train vs Test Error Gap

```python
# Import libraries (same salary example, same seed)
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(seed=42)
years_experience = rng.uniform(0.5, 15, size=400)
weekly_learning_hours = rng.uniform(0, 15, size=400)
monthly_salary_inr = (
    25000
    + 3500 * years_experience
    + 800 * weekly_learning_hours
    + rng.normal(0, 4000, size=400)
)
df = pd.DataFrame({
    "years_experience": years_experience,
    "weekly_learning_hours": weekly_learning_hours,
    "monthly_salary_inr": monthly_salary_inr,
})
X = df[["years_experience", "weekly_learning_hours"]]
y = df["monthly_salary_inr"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Predict on training rows (model has seen these during fit)
train_pred = model.predict(X_train)
train_avg_error = np.abs(y_train - train_pred).mean()

# Predict on test rows (model has NOT seen these during fit)
test_pred = model.predict(X_test)
test_avg_error = np.abs(y_test - test_pred).mean()

print(f"Average error on TRAIN: ₹{round(train_avg_error, 2):,}")
print(f"Average error on TEST:  ₹{round(test_avg_error, 2):,}")

gap = train_avg_error - test_avg_error
if abs(gap) < 1500:
    print("Train and test errors are close — reasonable generalization for this example.")
else:
    print("Noticeable gap — worth checking data size, features, or split luck.")
```

**How the code works:**

- `train_pred` measures how well the model fits what it studied.
- `test_pred` measures performance on locked-away rows — the honest check.
- Comparing the two average errors is a quick overfitting screen without new formulas.
- A gap alone is not a verdict — small datasets and random splits can wobble — but a **large** gap is a warning flag.

### Quick Activity — Read the Gap

| Train avg error | Test avg error | Likely story |
|---:|---:|---|
| ₹3,000 | ₹3,200 | Stable — test close to train |
| ₹500 | ₹8,000 | Suspicious — may be overfitting or a bad split |
| ₹12,000 | ₹11,500 | Both high — model may be too weak for the pattern |

Write one sentence for each row explaining what you would do next (e.g., collect more data, add features, or retry split with `random_state` fixed).

---

## Residuals and Error Intuition

After predictions exist, the next question is: *how wrong are we, row by row, and is the wrongness random or patterned?* That is what **residuals** answer.

**Residual:**

- **Official Definition:** For one row, **residual = actual target − predicted target**.
- **In Simple Words:** The gap between truth and guess for that single example.
- **Real-Life Example:** Predicted delivery in 30 minutes, arrived in 38 → residual **+8** (model was too optimistic). Arrived in 25 → residual **−5** (model was too pessimistic).

![Residual = actual − predicted (positive: under-predicted; negative: over-predicted)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_residuals.png)

### What Residual Patterns Mean

- **Scattered above and below zero with no shape** → errors look random; the line may be reasonable for a linear story.
- **Mostly positive or mostly negative** → systematic bias; the model consistently under- or over-predicts.
- **Fan shape (spread grows as prediction grows)** → errors grow for large values; a straight line might be too simple.
- **A few huge residuals** → possible outliers or data issues — worth opening those rows.

Formal scores like **MAE**, **RMSE**, and **R-squared** will come when you study regression metrics in depth. Today stays **conceptual** — residuals as a diagnostic picture.

### Complete Code — Compute Residuals and a Simple Residual Plot

```python
# Import plotting and numeric tools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Build the salary dataset (same seed)
rng = np.random.default_rng(seed=42)
years_experience = rng.uniform(0.5, 15, size=400)
weekly_learning_hours = rng.uniform(0, 15, size=400)
monthly_salary_inr = (
    25000
    + 3500 * years_experience
    + 800 * weekly_learning_hours
    + rng.normal(0, 4000, size=400)
)
df = pd.DataFrame({
    "years_experience": years_experience,
    "weekly_learning_hours": weekly_learning_hours,
    "monthly_salary_inr": monthly_salary_inr,
})
X = df[["years_experience", "weekly_learning_hours"]]
y = df["monthly_salary_inr"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)

# Residuals on test set: actual minus predicted for each held-out row
residuals = y_test - y_test_pred

# Print first 6 residuals with plain-English direction
print("First 6 test residuals (actual - predicted):")
for i in range(6):
    direction = "under-predicted" if residuals.iloc[i] > 0 else "over-predicted"
    print(f"  Row {i + 1}: ₹{round(residuals.iloc[i], 2):,} ({direction})")

# Average residual should be near zero if the model is balanced
print(f"\nAverage residual on test: ₹{round(residuals.mean(), 2):,}")

# Residual plot: predicted salary on x-axis, residual on y-axis
plt.scatter(y_test_pred, residuals, alpha=0.6)
plt.axhline(0, color="red", linestyle="--", linewidth=1)
plt.xlabel("Predicted monthly salary (₹)")
plt.ylabel("Residual (actual - predicted) (₹)")
plt.title("Residual plot — test set")
plt.show()
```

**How the code works:**

- `y_test - y_test_pred` subtracts each prediction from the true salary on the test set only.
- Positive residual → actual salary **higher** than predicted → model **under-predicted**.
- Negative residual → model **over-predicted**.
- `residuals.mean()` near zero suggests no strong overall bias up or down.
- `plt.scatter(y_test_pred, residuals)` is the **residual plot**: you want points scattered around the red zero line without a clear curve or funnel.
- `plt.axhline(0, ...)` draws the reference line for “perfect prediction error = 0.”

### Three Questions to Ask Every Time

1. Is the **average residual** close to zero?  
2. Are **positive and negative** residuals roughly balanced in count?  
3. Does the **residual plot** show a pattern (curve, funnel) or random scatter?

### Quick Activity — Sign of the Residual

| Actual salary | Predicted salary | Residual | Plain meaning |
|---:|---:|---:|---|
| ₹62,000 | ₹58,000 | ? | Model predicted too ___ |
| ₹41,000 | ₹47,000 | ? | Model predicted too ___ |
| ₹55,000 | ₹55,000 | ? | Perfect or off? |

**Answers:** Row 1 → +₹4,000, under-predicted. Row 2 → −₹6,000, over-predicted. Row 3 → 0, perfect on that row.

### Bridge Ahead

You can now train a linear model, beat a mean baseline on a fair split, and read residuals. Upcoming topics will add **regression metrics** (MAE, RMSE, R²) and return to **classification** with new models — building on the same honest split-and-check habits you practise today.

---

## Key Takeaways

- **Regression** predicts a **continuous number** (price, salary, time); **classification** picks a **category** — choose the task by the shape of the answer, not by whether a column looks numeric.
- **Linear regression** learns an **intercept** and **coefficients** to form a best-fit relationship; `.fit()` trains on training data only, and `.predict()` applies the learned formula to new rows.
- A **mean baseline** on the same test split sets a simple floor — your model should beat “always guess the average training salary” before you trust it.
- Comparing **train vs test error** gives a quick read on **generalization**; large gaps warn you the model may be memorising noise.
- **Residuals** (actual − predicted) and a **residual plot** reveal bias and patterns that one average error number can hide — formal regression metrics come next, followed by deeper classification work.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Regression** | Predict a continuous numeric target from features | Use when the answer is a number on a scale |
| **Classification** | Predict a category label | Contrast only — today’s focus is numeric targets |
| **Target (y)** | The numeric column to predict | The “answer” column in regression |
| **Feature (x)** | Input columns used for prediction | More relevant features usually help |
| **Linear regression** | Weighted sum of features + intercept | Simplest, most interpretable regression model |
| **Intercept** | Baseline prediction before features | `model.intercept_` after `.fit()` |
| **Coefficient** | Change in prediction per one unit of a feature | `model.coef_` — one value per feature column |
| **Best-fit line** | Line (or hyperplane) minimising training error | What `.fit()` searches for |
| `LinearRegression()` | Creates the sklearn regression model | Starting point for numeric prediction |
| `.fit(X_train, y_train)` | Learns intercept and coefficients | Training happens here — never pass test data |
| `.predict(X_new)` | Returns numeric predictions | No learning — uses frozen weights |
| `train_test_split` | Holds out test rows for honest evaluation | Same split-first habit as before |
| **Mean baseline** | Predict training mean for every test row | Regression floor — beat this on the same test set |
| **Overfitting** | Great on train, worse on test | Large train–test error gap is a warning |
| **Generalization** | Good performance on unseen rows | Real goal of modelling |
| **Residual** | Actual − predicted for one row | Positive = under-predicted; negative = over-predicted |
| **Residual plot** | Predicted value vs residual scatter | Spots curves, funnels, and bias |
| `numpy` (`np`) | Arrays and numeric math | Baseline arrays, errors, seeds |
| `pandas` (`pd`) | Tables (DataFrames) | Load and slice clean numeric CSVs |
| `matplotlib.pyplot` | Charts | Scatter and residual plots |
| `sklearn.linear_model` | Home of `LinearRegression` | Standard regression import |
| `sklearn.model_selection` | Home of `train_test_split` | Same tool you already use for splits |
