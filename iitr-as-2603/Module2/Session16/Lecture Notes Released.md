# Regression: Linear Regression Fundamentals

## Context of This Session

In the previous session, you learned how models can look brilliant in a notebook and fail in real life. You studied **data leakage** — why test information must never sneak into training — and built a **split-first, train-only preprocessing** habit. You also saw **class imbalance**, why **accuracy** can mislead, and how ideas like **precision**, **recall**, resampling, and **cross-validation** help you evaluate models more honestly.

Until now, most of your ML examples asked *which category* something belongs to. Today the question changes shape: *what number should we expect?* You will meet **regression** — predicting continuous values like salary, house price, or exam score — and train your first numeric models with **linear regression**, a real **Kaggle-style case study**, and honest **train vs test** checks.

**In this session, you will:**

- Contrast **regression** with **classification** using everyday examples
- Build intuition for the **best-fit line**, **features**, **target**, **slope**, and **intercept**
- Distinguish **simple** vs **multiple** linear regression and interpret coefficients in business language
- **Fit** and **predict** with `LinearRegression` in a notebook (study hours → exam score, then California housing)
- Bundle preprocessing and modelling with a sklearn **Pipeline**
- Meet a **mean baseline** and compare models on the same split
- Spot **underfitting**, **overfitting**, and **good fit** using train vs test performance
- Understand **residuals** from a table and pattern view — with a pointer to formal regression metrics ahead

---

## Regression for Continuous Targets

Machine learning problems usually fall into two families. **Classification** picks a label from a fixed list. **Regression** estimates a number on a scale.

**Regression:**

- **Official Definition:** A supervised machine learning task where the model learns to predict a **continuous numeric output** (the target) from input **features**.
- **In Simple Words:** You show the computer past examples where the answer is a number — like ₹45,000, 72 minutes, or an exam score — and it learns a pattern to guess new numbers.
- **Real-Life Example:** A ride-hailing app estimating **trip fare in rupees** from distance and time is regression — the answer is a amount, not a category name.

**Classification (quick contrast):**

- **Official Definition:** A supervised task where the model predicts a **category** or **class label** from features.
- **In Simple Words:** The answer is a box — spam or not spam, pass or fail, fraud or genuine.
- **Real-Life Example:** Sorting email into **Inbox** vs **Promotions** — fixed categories, not a measured quantity.

| Question type | Example question | Type of answer |
|---|---|---|
| How much? | What will this flat sell for? | **Regression** (₹ amount) |
| How many? | How many units will we sell next month? | **Regression** (count) |
| Which one? | Is this transaction fraud? | **Classification** (label) |
| Which bucket? | Will this student pass or fail? | **Classification** (label) |

![Regression predicts a number on a scale; classification picks a category](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_classification_vs_regression.png)

### How to Decide: Look at the Output, Not the Column Type

- **Rule of thumb:** If the **output** you care about is numeric, it is usually **regression**. If the output is a named category, it is **classification**.
- **Common doubt:** A column with digits is not always regression. Values like `1 = junior, 2 = mid, 3 = senior` are **categories written as numbers**. Ask: *Is this a measurement on a scale, or a label in disguise?*

### Everyday Regression Examples

- **House / district price:** Given location, rooms, income, and age — predict **median housing value** (as in the California census case study).
- **Salary:** Given years of experience and skills — predict monthly salary in rupees.
- **Exam score:** Given study hours — predict marks out of 100.
- **Stock / sales / oil price:** Predict tomorrow’s numeric level — all regression because the answer is a number on a scale.

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
  - **Real-Life Example:** Years of experience and weekly learning hours are features for salary.

![Target variable (y): what you predict — Features (x): the clues the model uses](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_target_and_features.png)

**Features can be non-numeric.** For regression the **target** must be numeric, but **features** may be categories (e.g. skills = Python, Java). You handle that with preprocessing you already know — for example **one-hot encoding** — so each category becomes its own numeric column before training.

### Quick Activity — Regression or Classification?

On paper, write **R** for regression or **C** for classification. Check: does the answer have to be a **specific number**, or a **named category**?

1. Predict tomorrow’s maximum temperature in °C  
2. Predict whether a loan will be **approved** or **rejected**  
3. Predict a student’s **exact exam score** out of 100  
4. Predict whether an email is **spam** or **not spam**  
5. Predict monthly **electricity bill** in rupees  

**Answer key:** 1 → R, 2 → C, 3 → R, 4 → C, 5 → R.

---

## Linear Regression Intuition — The Best-Fit Line

Once you know the answer must be a number, the next question is: *how does the model pick that number?* **Linear regression** is the simplest and most important answer — it learns a straight-line relationship (or a straight-line **combination** when you have many features).

**Linear Regression:**

- **Official Definition:** A regression model that predicts the target as a **weighted sum of features** plus a constant — each feature is multiplied by a learned weight and the results are added.
- **In Simple Words:** “For every extra hour of study, add about 7–8 marks” — the model learns those multipliers from data.
- **Real-Life Example:** A taxi meter starts at a base fare (**intercept**) and adds money per km (**coefficient**). Linear regression learns the software version of “base fare” and “rate per km” from past trips.

### Intercept and Coefficient in Plain Language

- **Intercept (c in y = mx + c):**
  - **Official Definition:** A constant term added to every prediction, even when all features are zero.
  - **In Simple Words:** The model’s starting point before it looks at the clues — like a minimum score you might get even with zero study hours in some exam schemes.
  - **Real-Life Example:** Base salary before experience is counted.

- **Coefficient (slope / m):**
  - **Official Definition:** The learned multiplier for a feature — how much the prediction changes when that feature increases by one unit.
  - **In Simple Words:** One more hour of study might add ~7.5 marks on average.
  - **Real-Life Example:** Each extra year of experience might add ₹2,000 to predicted salary in a simple two-feature story.

You also met **slope** as “rise over run”: for every one unit forward on **x**, how much does **y** change? That is the same idea as a **coefficient** when you have one feature.

### The Best-Fit Line — Without Heavy Formulas

Picture students on a graph: **study hours** on the horizontal axis, **exam score** on the vertical axis. Each student is a dot.

You could draw countless straight lines — steep, flat, high, low. The **best-fit line** is the one where the **vertical gaps** from dots to the line are collectively as small as possible. Linear regression finds that line automatically.

- With **one feature**, you can imagine one line on a scatter plot.
- With **many features**, you cannot draw it on paper — but the idea is the same: one formula that balances errors across all rows.

![Best-fit line through study hours vs exam scores — vertical gaps are residuals](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_best_fit_line.png)

### Optional Scatter Plot in Your Notebook (One Feature)

If you want to **see** the cloud of points before training, a scatter plot helps. This is optional intuition.

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
- After you train a model, the learned line should follow the same upward story.

### Quick Activity — Intercept and Slope in Your Head

A shop prices sweets: **₹20 base** plus **₹5 per piece**.

1. How much for **0 pieces**? (This is the **intercept**.)  
2. How much for **7 pieces**?  
3. If the price per piece rises to **₹6** but the base stays ₹20, how much for **7 pieces** now?

**Answers:** 1 → ₹20, 2 → ₹55, 3 → ₹62.

---

## Simple vs Multiple Linear Regression

After the straight-line story with **one** input, you extend to **many** inputs — still linear regression, but with more than one feature.

| Name | When to use it | Example |
|---|---|---|
| **Simple linear regression** | Exactly **one** feature (one **x**) | Study hours → exam score |
| **Multiple linear regression** | **Two or more** features | Experience + skills → salary; latitude + rooms + income → house price |

- **Official Definition:** **Multiple linear regression** still predicts y as a **weighted sum of all features plus intercept** — there is no curve in the formula, only more weights.
- **In Simple Words:** `salary ≈ base + (weight₁ × experience) + (weight₂ × skill_python) + …`
- **Real-Life Example:** Predicting **median housing value** from latitude, longitude, rooms, population, and median income — each column gets its own coefficient.

**Interpretation matters.** When the model prints an equation like `score ≈ 7.87 × hours + 37.66`, you should be able to say in plain language:

- **Coefficient on hours:** “For every **one extra hour** of study, the model expects about **7.87 more marks** on average.”
- **Intercept:** “When hours are zero, the model’s starting prediction is about **37.66**” — treat this as the model’s baseline, not always a real-world policy.

The same reading applies to salary or housing: each coefficient answers *“If this feature increases by one unit, how much does the predicted price/salary move, holding other features fixed?”*

### Quick Activity — Read a Two-Feature Story

A simplified salary equation is `salary = 1 + 2 × experience` (in lakhs, for intuition only).

1. What does **2** mean for experience?  
2. What does **1** represent?  
3. If experience goes from 3 to 4 years, how much should predicted salary change?

**Answers:** 1 → +2 lakhs per extra year. 2 → baseline / intercept term. 3 → +2 lakhs.

---

## Fit and Predict — Study Hours to Exam Score

You already know the ML habit: **split first**, keep the test set locked away, and **fit only on training data**. The instructor walked through this in a **Jupyter notebook** with a small table: **study hours** as **x**, **exam score** as **y**.

**Business problem:** Given how many hours past students studied, predict the exam score for a new student.

**Model training:**

- **Official Definition:** Fitting a model means learning intercept and coefficients from labelled training examples.
- **In Simple Words:** The computer adjusts the line until it matches past `(hours → score)` pairs as well as it can.
- **Real-Life Example:** A coaching centre studies past batches and learns “typical marks per study hour.”

### Complete Notebook Workflow — Split, Train, Predict, Interpret

```python
# Import numpy for numbers and arrays
import numpy as np

# Import pandas for tables (DataFrames)
import pandas as pd

# Import train_test_split to separate train and test rows
from sklearn.model_selection import train_test_split

# Import LinearRegression — our numeric prediction model
from sklearn.linear_model import LinearRegression

# --- Assume df has columns: "study_hours", "exam_score" ---
# In class, the instructor used a curated sample table on screen.

# Separate features (X) and target (y)
X = df[["study_hours"]]
y = df["exam_score"]

# Split: 80% train, 20% test — test stays untouched during fit
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model ONLY on training rows
model = LinearRegression()
model.fit(X_train, y_train)

# Learned parameters — these match the "best-fit line" story
print("Intercept:", round(model.intercept_, 2))
print("Coefficient (per hour):", round(model.coef_[0], 2))

# Predict on held-out test rows
y_test_pred = model.predict(X_test)

# Training score = how well the model fits what it studied
# Testing score = how well it does on unseen rows (like a mock paper)
print("Training score:", round(model.score(X_train, y_train), 4))
print("Testing score:", round(model.score(X_test, y_test), 4))

# Predict for one new student: 6 hours of study
new_student = pd.DataFrame({"study_hours": [6.0]})
print("Predicted score:", round(model.predict(new_student)[0], 2))
```

**How the code works:**

- `X` is a DataFrame with one column; `y` is the numeric exam score column.
- `train_test_split` holds back test rows — **split before** any learning step.
- `model.fit(X_train, y_train)` learns the best-fit line; test data is never passed to `.fit()`.
- `model.intercept_` and `model.coef_[0]` are the **c** and **m** from `y = mx + c`.
- `model.score(...)` returns a score where **higher is better** (in sklearn this is **R²** for linear regression) — use it to compare train vs test, not as exam “accuracy percent” from classification.
- `model.predict(new_student)` is the live use case: one new row in, one score out.

In class, train and test scores were **close** (for example ~94% train and ~93% test on the score metric used in the notebook) — a sign the simple line generalizes reasonably on that small example. You will see weaker scores on harder real data next.

---

## Case Study — California Housing Prices (Kaggle)

Real projects rarely stop at one toy column. The session moved to the **California housing prices** dataset on **Kaggle** — census data from **1990 California** used to predict **median house value**.

**Problem framing:**

- **Official Definition:** Predict **median housing value** from district-level features such as latitude, longitude, housing median age, total rooms, bedrooms, population, households, and median income.
- **In Simple Words:** Each row is a **district block**, not a single flat — you predict a typical price for that area from area statistics.
- **Real-Life Example:** Property platforms (Magicbricks, 99acres-style use cases) estimating prices from location and neighbourhood stats.

**Read the data before coding.** On Kaggle, scroll through column descriptions, note which column is the **target**, and check scales — latitude, room counts, and income live on very different numeric ranges.

### Why Scaling Appears Here (Reminder Only)

Features like **population** and **median income** sit on different scales. **MinMaxScaler** (which you met when preprocessing) maps values into a common range so one huge column does not dominate just because its numbers are bigger.

**Split-first habit still applies:** fit the scaler on **training data only**, then transform train and test — or use a **Pipeline** so you do not do this manually step by step.

### Complete Code — Manual Steps vs Pipeline

```python
# Import splitting, scaling, pipeline, and regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Load your cleaned California housing table (from Kaggle export or course file)
# df = pd.read_csv("california_housing.csv")

# X = all feature columns; y = median_house_value (target)
X = df.drop(columns=["median_house_value"])
y = df["median_house_value"]

# Split once — all models judged on the same test rows
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Option A: manual (more steps, easier to leak if careless) ---
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
print("Manual — train score:", round(lin_reg.score(X_train_scaled, y_train), 2))
print("Manual — test score:", round(lin_reg.score(X_test_scaled, y_test), 2))

# --- Option B: Pipeline (recommended pattern from class) ---
pipe = Pipeline([
    ("scaler", MinMaxScaler()),
    ("model", LinearRegression()),
])

# One fit on raw train rows — scaler fits inside on train only
pipe.fit(X_train, y_train)

print("Pipeline — train score:", round(pipe.score(X_train, y_train), 2))
print("Pipeline — test score:", round(pipe.score(X_test, y_test), 2))
```

**How the code works:**

- `Pipeline([...])` chains **preprocessing** then **model** so `.fit(X_train, y_train)` learns scaler statistics from train only.
- `pipe.score(X_test, y_test)` evaluates on held-out rows — fair comparison.
- In class, **linear regression** on this data gave roughly **~61% train** and **~58% test** on the score shown — both modest, which the instructor used as an **underfitting** example (the line is too simple for the real pattern).
- A **Pipeline** can also include encoders or imputers from preprocessing — same idea: define steps in order, then one `.fit()`.

**Data leakage reminder:** Manually scaling before splitting, or fitting the scaler on the full dataset, repeats the leakage mistakes from the previous session. Pipelines help you keep the workflow tight.

### Quick Activity — Read District-Level Data

1. If each row is a **district**, can you predict one individual flat’s exact price without extra house-level features?  
2. Why might **median income** help predict **median house value**?  
3. If train score is **61%** and test score is **58%**, is the gap huge or small? What might that suggest?

**Sample answers:** 1 → Not precisely — district stats are averages. 2 → Richer areas tend to have higher housing medians. 3 → Gap is small but both scores are low → likely **underfitting**, not memorisation.

---

## Mean Baseline — The “Always Guess Average” Floor

You have already met **baselines** in classification. In regression, the simplest baseline is: **predict the average target** (mean of **y**) for every row — often using the mean from **training** labels only.

**Mean baseline:**

- **Official Definition:** A rule that outputs the same value — the mean of training targets — for every prediction.
- **In Simple Words:** Ignore all features; always guess the “typical” price or score.
- **Real-Life Example:** Saying every district’s house price is **₹2.5 lakh** because that was the historical average — no feature logic.

On California housing, the instructor computed the **average of all y (prices)** to illustrate the idea. In practice you still build real models that use **X** to predict **y** — the baseline is mainly a **vocabulary** and sanity check, not the final solution.

**Fair comparison rule:** Any model and any baseline must be judged on the **same test split** with the same metric. Beating the mean shows your features add something; losing to the mean means the line is not learning useful signal yet.

### Quick Activity — Baseline Thinking

1. If average training salary is **₹50,000**, what does a mean baseline predict for **every** test row?  
2. Why compute the mean from **`y_train` only**?  
3. If your regression test score is **much higher** than a lazy mean guess on the same test rows, what does that suggest?

**Answers:** 1 → ₹50,000 each time. 2 → Using full **y** leaks test information. 3 → Features are helping beyond “always average.”

---

## Overfitting, Underfitting, and Generalization

A model’s job is to work on **new** data, not only rows it already saw. You already guard against **leakage**; now you name **fit quality** with three ideas from class.

![Underfitting, sweet spot, overfitting — train-test split helps spot overfitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_complexity_train_test.png)

| Idea | Train performance | Test performance | Plain story |
|---|---|---|---|
| **Underfitting** | Low | Low | The model did not learn the pattern — too simple |
| **Good fit** | Reasonably high | Close to train | Learns the main pattern and generalizes |
| **Overfitting** | Very high | Much lower than train | Memorised noise on training rows |

**Generalization:**

- **Official Definition:** Performing well on unseen data from the same kind of problem.
- **In Simple Words:** The formula still makes sense on tomorrow’s rows, not only yesterday’s sheet.
- **Real-Life Example:** A student understands **types** of questions, not one memorised paper.

### What You Saw in Class

1. **Study hours model:** Train and test scores were **close** — reasonable generalization for a simple line on a small dataset.  
2. **California linear regression:** Train **~61%**, test **~58%** — **both low** → treated as **underfitting** (model too weak for the data).  
3. **Stronger algorithm demo:** The instructor swapped **linear regression** for **gradient boosting regressor** inside the same pipeline — train and test scores **jumped** (a **better fit** demo). You will study ensembles later; today the lesson is **compare models on the same split**.  
4. **Turning up complexity:** Increasing **`n_estimators`** in the boosting model pushed train score up; after a point, test score can **stop improving or fall** — a practical hint at **overfitting** when a model becomes too flexible.

Today we **do not** run Ridge, Lasso, or cross-validation labs — those deepen control in upcoming work.

### Quick Activity — Read the Gap

| Train score | Test score | Likely story |
|---:|---:|---|
| 94% | 93% | Stable — test close to train on simple data |
| 61% | 58% | Both low — underfitting on hard data |
| 95% | 60% | Large gap — possible overfitting |

Write one sentence for each row: what would you try next (more features, different algorithm, more data, or tune complexity)?

---

## Residuals and Error Intuition

After predictions exist, ask: *how wrong are we row by row, and is the wrongness random or patterned?* That is what **residuals** answer.

**Residual:**

- **Official Definition:** For one row, **residual = actual target − predicted target**.
- **In Simple Words:** The gap between truth and guess for that single example.
- **Real-Life Example:** Predicted 98 marks, actual 86 → residual **+12** (model **under-predicted**). Predicted 50, actual 60 → residual **−10** (model **over-predicted**).

![Residual = actual − predicted (positive: under-predicted; negative: over-predicted)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_residuals.png)

### Residual Table — How Class Checked Errors

Instead of drawing a matplotlib residual plot live, the instructor built a small table:

| study_hours | y_actual | y_predicted | residual (actual − predicted) |
|---:|---:|---:|---:|
| … | … | … | … |

From this table you can:

- Spot **large mistakes** (e.g. many hours studied but score far below the line’s guess).  
- See whether errors are mostly **positive** or **negative** → systematic bias.  
- Flag **outliers** worth opening in the raw data.

```python
# After model.predict on test set, build a residual view
results = pd.DataFrame({
    "study_hours": X_test["study_hours"].values,
    "y_actual": y_test.values,
    "y_predicted": y_test_pred,
})
results["residual"] = results["y_actual"] - results["y_predicted"]

# Sort to find largest errors
print(results.sort_values("residual", key=abs, ascending=False).head())
```

**How the code works:**

- `y_actual - y_predicted` applies the definition row by row.
- Sorting by absolute residual surfaces the worst predictions first.
- Residuals **diagnose** problems; fixing them means better features, better models, or cleaner data — not “deleting” residuals.

### Patterns You Will Meet Later (Including Quiz Ideas)

When you plot **predicted value vs residual** in future work:

- **Scattered around zero with no shape** → errors look random; a straight line may be okay.  
- **Curve-shaped residuals** → a straight line may be too simple; a **curved** model might fit better.  
- **Funnel shape** → error grows for large predictions.

Formal scores — **MAE**, **RMSE**, and **R-squared** — come when you study regression metrics in depth. **Ridge**, **Lasso**, and deeper **R²** work were pointed to for upcoming classes.

### Quick Activity — Sign of the Residual

| Actual score | Predicted score | Residual | Plain meaning |
|---:|---:|---:|---|
| 62 | 58 | ? | Model predicted too ___ |
| 41 | 47 | ? | Model predicted too ___ |
| 55 | 55 | ? | Perfect on that row |

**Answers:** Row 1 → +4, under-predicted. Row 2 → −6, over-predicted. Row 3 → 0.

### Bridge Ahead

You can now tell regression from classification, train a linear model, read coefficients in business language, use a **Pipeline** on real housing data, compare models and baselines on one split, and inspect **residuals** from a table. Upcoming work adds **regression metrics**, **regularization**, and more algorithms — on the same honest **split-first** habits you practise today.

---

## Key Takeaways

- **Regression** predicts a **continuous number**; **classification** picks a **category** — decide from the **output**, not from whether a column “looks numeric.”
- **Simple** linear regression uses one feature; **multiple** linear regression adds more coefficients — always interpret what each weight means in plain language.
- **`LinearRegression`** in sklearn learns intercept and coefficients with `.fit()` on **train only**; `.predict()` applies the frozen line; `.score()` helps compare train vs test.
- The **California housing** case study shows **real features**, **scaling**, and a **Pipeline** that reduces leakage risk; modest train/test scores illustrated **underfitting**.
- **Baselines**, **residual tables**, and **train–test gaps** are quick honesty checks before you trust a notebook — formal metrics and stronger models come next.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Regression** | Predict a continuous numeric target | Use when the answer is a number on a scale |
| **Classification** | Predict a category label | Contrast — today’s focus is numeric targets |
| **Simple vs multiple linear regression** | One feature vs many features in the same linear formula | Names the two setups you practised |
| **Target (y)** | Numeric column to predict | Always numeric in regression |
| **Feature (x)** | Input columns | May need encoding if categorical |
| **Intercept / coefficient** | Baseline + per-feature weight | Read as business impact (₹, marks, price) |
| **Best-fit line** | Line minimising training error | What `.fit()` finds |
| `LinearRegression()` | sklearn regression model | First numeric model |
| `.fit(X_train, y_train)` | Learns parameters on train only | Never pass test data here |
| `.predict(X_new)` | Numeric predictions | No learning during predict |
| `.score(X, y)` | Model quality on a set (R² for linear reg) | Compare train vs test |
| `train_test_split` | Hold-out test rows | Same habit as before |
| `MinMaxScaler` | Scales features to a common range | Used in housing case study |
| `Pipeline` | Chains preprocessing + model | Safer, shorter workflow |
| **Mean baseline** | Predict training mean every time | Floor idea — same test split |
| **Underfitting / overfitting / good fit** | Too simple / memorising / balanced | Read from train vs test |
| **Gradient boosting regressor** | Stronger non-linear model (demo only) | Shows swapping algorithms in same pipeline |
| **Residual** | Actual − predicted | Diagnose bias and big errors |
| `numpy` / `pandas` | Arrays and tables | Data handling |
| `matplotlib.pyplot` | Charts | Optional scatter plots |
| `sklearn.linear_model` | `LinearRegression` | Core import |
| `sklearn.pipeline` | `Pipeline` | Bundle steps |
| `sklearn.preprocessing` | `MinMaxScaler` | Feature scaling |
