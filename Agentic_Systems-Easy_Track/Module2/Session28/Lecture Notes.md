# Regression: Linear Regression Fundamentals

---

## What Is Regression? Predicting Real Numbers from Data

Every question in data science falls into one of two categories. Either you are asking *"which group does this belong to?"* — or you are asking *"what specific number should this be?"* Regression is the entire field of machine learning dedicated to answering that second kind of question.

**Regression:**
- **Official Definition:** A supervised machine learning task where the model learns to predict a continuous numeric output based on input features.
- **In Simple Words:** You give the computer a bunch of past examples where you already know the answer as a number, and the computer learns a formula so it can predict new answers for situations it has never seen.
- **Real-Life Example:** Imagine a cab booking app. Based on how far you're going, what time of day it is, and whether it's raining — the app predicts the exact fare in rupees. It's not saying "expensive or cheap." It is saying ₹347. That numeric prediction is regression.

The critical thing to understand right away is what makes regression *different from classification*. Classification gives you a label from a fixed list — "spam or not spam," "fraud or genuine." Regression gives you a position on a measuring scale — "₹43,500" or "72 minutes" or "8.4 kg." Whenever the answer to your question is a specific measurable number, you are working with a regression problem.

---

**Common real-world problems where regression is used:**

- **House price prediction:** Given the size, location, and age of a property — predict its selling price in rupees.
- **Student score prediction:** Given weekly study hours and attendance — predict the final exam score.
- **Delivery time estimation:** Given order size and restaurant distance — predict how many minutes until the food arrives.
- **Electricity bill forecasting:** Given number of appliances, usage hours, and season — predict the monthly bill.
- **Salary estimation:** Given years of experience and job role — predict the monthly take-home salary.

In every case, the final answer is not a tick in a box. It is a number on a scale. That is the signature of a regression problem.

![Regression predicts a number on a scale; classification picks a category](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_classification_vs_regression.png)

---

**The two core vocabulary terms every regression problem has:**

- **Target Variable:**
  - **Official Definition:** The continuous numeric output that the model is trained to predict — the "answer column" in your dataset.
  - **In Simple Words:** The number you are trying to guess. Whatever number you're predicting — that's your target variable.
  - **Real-Life Example:** In a house price prediction model, the target variable is the actual sale price — ₹42,00,000, ₹68,50,000, and so on.

- **Feature:**
  - **Official Definition:** Any input variable available to the model that it can use to form its prediction — also called a predictor or independent variable.
  - **In Simple Words:** The clues you give the model. The more relevant clues you give, the better the guesses.
  - **Real-Life Example:** In the house price model, the features are things like number of bedrooms, floor area in square feet, age of building, and whether it has parking.

![Target variable (y): what you predict — Features (x): the clues the model uses](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_target_and_features.png)

> **Common Beginner Mistake:** Just because a column contains numbers doesn't mean it is a regression target. A column that says "1 for junior, 2 for mid-level, 3 for senior" is a category disguised as a number. Always ask: "Is this a measurement on a scale, or just a label written as a digit?"

---

## How Linear Regression Works: The Best-Fit Line

Now that we know regression predicts numbers, the natural next question is: how does the model actually figure out what number to predict? The simplest and most important answer is **linear regression** — an approach based on drawing the best possible straight line through your data.

**Linear Regression:**
- **Official Definition:** A regression model that predicts the target variable as a weighted combination of input features — essentially, each feature is multiplied by a learned number and all results are added together to get the prediction.
- **In Simple Words:** The model says: "For every extra hour a student studies, I'll add 8 marks to their predicted score." It learns that multiplier (8 marks per hour) by looking at hundreds of past students and their actual scores.
- **Real-Life Example:** Think of how a taxi meter works. It starts at ₹30 as a base, then adds ₹15 for every kilometre. The ₹30 is the starting point, and ₹15/km is the rate. Linear regression learns the equivalent of "base fare" and "rate per km" from your historical data.

The two key components of any linear regression model:

- **Intercept (Baseline):**
  - **Official Definition:** A constant value that the model adds to its prediction regardless of the feature values — it acts as the starting point.
  - **In Simple Words:** Even before looking at any clues, the model already has a base prediction. The intercept is that starting number.
  - **Real-Life Example:** A hotel says every room starts at ₹2,000 per night — that is the baseline before any upgrades or peak-season adjustments.

- **Coefficient (Weight/Slope):**
  - **Official Definition:** The learned multiplier assigned to each feature — it represents how much the prediction changes for every one-unit increase in that feature.
  - **In Simple Words:** If the coefficient for "study hours" is 7.5, it means every extra hour of study adds 7.5 marks to the predicted score.
  - **Real-Life Example:** In a food delivery app, the coefficient for "distance in km" might be ₹12 — meaning every additional kilometre adds ₹12 to the predicted delivery fare.

**How the best-fit line is chosen:**

The model does not guess coefficients randomly. It tries millions of combinations and picks the one that makes its predictions as close as possible to the real answers in the training data. The way it measures "closeness" is by looking at how far off each prediction is — these gaps are called **errors** or **residuals**. It finds the line that makes the overall collection of these gaps as small as possible. You don't need to know the math — just understand that the model is searching for the formula that gives the smallest total prediction error across all training examples.

---

**The intuition of the best-fit line — visualised in plain language:**

Imagine plotting 200 students on a graph. The horizontal axis shows their study hours, the vertical axis shows their exam score. Each student is a dot on that graph. Now imagine stretching a straight line through the cloud of dots. There are infinitely many ways you could draw that line — steep, shallow, shifted up or down. The **best-fit line** is the one specific position where the vertical distances from all the dots to the line are collectively the smallest. That is exactly what linear regression computes. For problems with multiple features, you can't draw this on paper — but the principle is identical.

![Best-fit line through study hours vs exam scores — vertical gaps are residuals](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_best_fit_line.png)

---

## Model Training: Teaching the Model from Data

Knowing what linear regression is and knowing how to *train* one are two different things. Training is the process where you hand your historical data to the model, and it figures out the best intercept and coefficients to use for future predictions.

**Model Training:**
- **Official Definition:** The process of fitting a model's internal parameters (intercept and coefficients) to a labelled dataset by minimising the prediction error across all training examples.
- **In Simple Words:** You show the computer thousands of past examples where you know both the inputs and the correct answer. The computer adjusts its internal formula until it is as accurate as possible on those examples.
- **Real-Life Example:** Teaching a new employee to quote prices. You show them 500 past customer orders and their final prices. After studying all those examples, the employee starts to recognise the pattern — they have been "trained."

In Python, the `scikit-learn` library makes this entire process happen in three lines. You set up the model, you call `.fit()` to train it, and you call `.predict()` to generate predictions.

---

**Example dataset for the snippet below:** One feature (`study_hours`) and one target (`exam_score`, marks out of 100). The code generates **200** rows using `seed=42` and the rule “about 40 + 7.5 × hours plus noise”. Here are the **first 10 rows** (rounded) so you can see the table the model learns from:

| study_hours | exam_score |
| ---: | ---: |
| 7.97 | 102.96 |
| 4.95 | 75.15 |
| 8.73 | 105.43 |
| 7.28 | 93.76 |
| 1.85 | 55.54 |
| 9.78 | 120.39 |
| 7.85 | 99.33 |
| 8.07 | 103.78 |
| 2.15 | 45.90 |
| 5.05 | 77.66 |

---

**Complete Code: Training a Linear Regression Model on Student Score Data**

```python
# Import the numpy library for creating and working with numbers
import numpy as np

# Import LinearRegression from scikit-learn to build our model
from sklearn.linear_model import LinearRegression

# Set a seed so the random numbers are the same every time we run this
rng = np.random.default_rng(seed=42)

# Create 200 students with study hours between 1 and 10
study_hours = rng.uniform(low=1, high=10, size=200)

# Create exam scores using a realistic formula: base 40 + 7.5 per hour + some random noise
# The noise simulates that not every student performs the same even with same study hours
scores = 40 + 7.5 * study_hours + rng.normal(loc=0, scale=5, size=200)

# Reshape study_hours into a 2D array — scikit-learn requires features in this shape
X = study_hours.reshape(-1, 1)

# Store scores as the target variable
y = scores

# Create the LinearRegression model object — no settings needed for basic use
model = LinearRegression()

# Train the model: it reads all 200 (study_hours, score) pairs and learns the best formula
model.fit(X, y)

# Print the intercept — this is the model's base prediction with zero study hours
print("Intercept (baseline score):", round(model.intercept_, 2))

# Print the coefficient — this is how many marks the model adds per extra study hour
print("Coefficient (marks per study hour):", round(model.coef_[0], 2))

# Generate predicted scores for all 200 students using the learned formula
y_pred = model.predict(X)

# Print the first 5 actual scores and their predicted equivalents for comparison
for i in range(5):
    print(f"Student {i+1}: Actual = {round(y[i], 1)}, Predicted = {round(y_pred[i], 1)}")

# Predict the score for a new student who studies 6.5 hours
new_student = np.array([[6.5]])

# Use the trained model to get the prediction — no retraining needed
predicted_score = model.predict(new_student)

# Display the result
print(f"\nNew student (6.5 hours): Predicted score = {round(predicted_score[0], 1)}")
```

**How the code works:**

- **`rng.uniform(low=1, high=10, size=200)`** — Creates 200 random study-hour values spread between 1 and 10. This is our feature data.
- **`40 + 7.5 * study_hours + rng.normal(...)`** — Builds realistic exam scores. The true formula adds 7.5 marks per hour on top of a 40-mark baseline, with small random variation to simulate real-world unpredictability.
- **`study_hours.reshape(-1, 1)`** — Transforms the list of hours from a single flat row into a column format. scikit-learn requires features as a table (rows = students, columns = features), even when there's only one feature.
- **`model.fit(X, y)`** — This is where all the learning happens. The model looks at all 200 student records and finds the intercept and coefficient that produce the smallest total prediction error.
- **`model.intercept_`** — Stores the learned baseline (should be close to 40).
- **`model.coef_[0]`** — Stores the learned multiplier for study hours (should be close to 7.5).
- **`model.predict(X)`** — Applies the learned formula to all 200 students and returns 200 predicted scores. This is pure arithmetic — no learning happens here.
- **`model.predict(new_student)`** — Shows the real deployment scenario: one new person's data goes in, one predicted number comes out.

---

**What happens inside `.fit()` — without the math:**

When `.fit()` runs, the model tries out different values for the intercept and coefficient. For each combination it tries, it checks: "If I use these numbers, how wrong would my predictions be on the training data?" It keeps adjusting until it finds the combination that produces the smallest overall error. Once that's done, the model is "trained" — the best intercept and coefficient are locked in and stored. From that point, the model never needs to see the training data again. All the knowledge from 200 student records has been compressed into just two stored numbers.

---

## Model Complexity: Why More Isn't Always Better

Once you understand that a linear regression model learns from data, a natural follow-up question arises: what if the training data is too small, or too noisy, or the model is too complicated? This is where **model complexity** becomes important — and understanding it is the difference between a model that works in the real world and one that only works in the lab.

**Overfitting:**
- **Official Definition:** A condition where a model learns the training data so precisely — including its noise and random quirks — that it performs poorly on new, unseen data.
- **In Simple Words:** The model memorised the training examples instead of learning the general pattern. It's like a student who memorised every past exam paper word for word, but then failed when the actual exam had slightly different questions.
- **Real-Life Example:** Imagine a new delivery driver who memorises the exact turn-by-turn directions for 50 specific past deliveries. When a new delivery goes to an address that's slightly different, they are completely lost — because they memorised routes, not the logic of how roads connect.

**Underfitting:**
- **Official Definition:** A condition where a model is too simple to capture the real pattern in the data, resulting in high error on both training and new data.
- **In Simple Words:** The model's formula is so basic that it misses even the obvious patterns. It's like trying to predict cricket match scores by only considering the weather and nothing else.
- **Real-Life Example:** A salary prediction model that only uses "city" to estimate salary — ignoring experience, role, and skills — will be wildly inaccurate for most people because it's too simplified.

**Generalisation:**
- **Official Definition:** The ability of a trained model to make accurate predictions on new, unseen data from the same domain.
- **In Simple Words:** A model generalises well if it doesn't just "remember" training data but truly understands the underlying pattern that will hold for new situations.
- **Real-Life Example:** A doctor who has treated 1,000 patients doesn't just memorise each patient's case. They extract principles — "when these symptoms appear together, this is likely the cause" — and apply those principles to new patients. That's generalisation.

---

**The three zones of model complexity:**

- **Too Simple (Underfitting zone):** The model is missing important patterns. Predictions are consistently off even on the training data.
- **Just Right (Sweet spot):** The model captures the genuine patterns without chasing noise. It performs well both on training data and on new data.
- **Too Complex (Overfitting zone):** The model is chasing every small random bump in the training data. It looks perfect on training data but fails on new data.

![Underfitting, sweet spot, overfitting — and using a train-test split to spot overfitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_complexity_train_test.png)

For linear regression with a small number of features, overfitting is less common. But as you add more features or work with smaller datasets, this tension becomes very real and very important. The key insight: *your model's job is not to be perfect on past data — it is to be useful on future data.*

---

**How to detect overfitting in practice:**

- Split your data into two parts: a **training set** and a **test set**.
- Train the model only on the training set.
- Check predictions on both sets.
- If the model is dramatically more accurate on training data than on test data — it has overfit.
- If both accuracies are similarly poor — it has underfit.

This train-test split approach is how every real ML practitioner checks whether their model generalises or just memorises.

---

**Example dataset for the snippet below:** Same meaning as above — `study_hours` → `exam_score` — but **300** rows with `seed=7` and slightly larger noise than the first example. After you run `train_test_split`, 80% of rows train the model and 20% are held out for testing. **First 10 rows** (rounded):

| study_hours | exam_score |
| ---: | ---: |
| 6.63 | 90.99 |
| 9.07 | 106.55 |
| 7.98 | 98.64 |
| 3.03 | 63.03 |
| 3.70 | 76.83 |
| 8.86 | 109.80 |
| 1.05 | 47.50 |
| 8.39 | 99.46 |
| 8.17 | 97.49 |
| 5.21 | 88.70 |

---

**Code: Checking for Overfitting with a Train-Test Split**

```python
# Import train_test_split to divide data into training and testing portions
from sklearn.model_selection import train_test_split

# Import LinearRegression for the model
from sklearn.linear_model import LinearRegression

# Import numpy for data creation
import numpy as np

# Set a seed for reproducibility
rng = np.random.default_rng(seed=7)

# Create 300 students with random study hours
study_hours = rng.uniform(1, 10, size=300)

# Create realistic exam scores with the true formula + noise
scores = 40 + 7.5 * study_hours + rng.normal(0, 6, size=300)

# Reshape study hours for scikit-learn input requirements
X = study_hours.reshape(-1, 1)
y = scores

# Split the data: 80% goes to training, 20% goes to testing
# random_state ensures the split is the same every time
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a fresh LinearRegression model
model = LinearRegression()

# Train the model on only the training portion
model.fit(X_train, y_train)

# Predict on training data to see how well it fits what it learned from
train_predictions = model.predict(X_train)

# Predict on test data — these are students the model has never seen
test_predictions = model.predict(X_test)

# Calculate average prediction error on training data (manual average of absolute errors)
train_errors = abs(y_train - train_predictions)
train_avg_error = train_errors.mean()

# Calculate average prediction error on test data
test_errors = abs(y_test - test_predictions)
test_avg_error = test_errors.mean()

# Print both errors for comparison
print(f"Average error on training data: {round(train_avg_error, 2)} marks")
print(f"Average error on test data:     {round(test_avg_error, 2)} marks")

# Interpret the result
if abs(train_avg_error - test_avg_error) < 1:
    print("The model generalises well — no signs of overfitting.")
else:
    print("Large gap detected — the model may be overfitting.")
```

**How the code works:**

- **`train_test_split(X, y, test_size=0.2)`** — Randomly assigns 80% of students to the training group and 20% to the testing group. The model only learns from the training group.
- **`model.fit(X_train, y_train)`** — Training happens exclusively on the 80% training portion. The model never sees the test data during learning.
- **`model.predict(X_train)` and `model.predict(X_test)`** — Two separate prediction runs: one on data the model trained on, one on data it has never seen.
- **`abs(y_train - train_predictions).mean()`** — Computes the average absolute difference between real scores and predicted scores for training students.
- **`abs(y_test - test_predictions).mean()`** — Does the same for the test group. If this number is much larger than the training error, the model is overfitting.
- **The `if` block** — Automatically flags if the gap between training and test error is suspiciously large.

---

## Residuals: Understanding Your Model's Mistakes

Once a model is trained and generating predictions, the next question is: how wrong is it, and in what way? The answer lives in the **residuals** — the individual errors the model makes on each prediction.

**Residual:**
- **Official Definition:** The difference between the actual observed value and the model's predicted value for a single data point — calculated as actual minus predicted.
- **In Simple Words:** For every student in your dataset, the residual is the gap between what the model said their score would be and what it actually was. Positive residual means the model predicted too low. Negative residual means the model predicted too high.
- **Real-Life Example:** If a delivery app predicted your food would arrive in 30 minutes and it actually arrived in 38 minutes — the residual is +8 minutes. If it arrived in 25 minutes — the residual is -5 minutes.

Residuals are not just about measuring error. They are a **diagnostic tool** that tells you whether your model is working well or whether something is wrong with your approach.

---

**What residuals tell you:**

- **Residuals scattered randomly around zero:** This is the ideal situation. It means the model is making errors, but those errors have no pattern — they're just unavoidable noise in the data. The model has captured the real relationship.
- **Residuals that consistently lean positive or negative:** This means the model is systematically biased. It is always over-predicting or always under-predicting. Something important is missing from the model.
- **Residuals that grow larger as predictions grow:** This suggests the model struggles more for extreme values. The relationship might not be perfectly linear.
- **A few residuals that are extremely large:** These are **outliers** — data points where the model was wildly wrong. Outliers are worth inspecting individually because they often reveal data quality issues or genuinely unusual cases.

![Residual = actual − predicted (positive: under-predicted; negative: over-predicted)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session28/session28_residuals.png)

---

**Example dataset for the snippet below:** Again **200** student rows (`study_hours`, `exam_score`), this time generated with `seed=99` (same formula style as the training example). The code fits on **all** rows, then compares actual minus predicted for each. **First 10 rows** (rounded):

| study_hours | exam_score |
| ---: | ---: |
| 5.55 | 84.93 |
| 6.09 | 85.58 |
| 5.61 | 78.47 |
| 9.75 | 111.61 |
| 6.53 | 87.09 |
| 6.11 | 80.61 |
| 3.58 | 57.11 |
| 5.99 | 86.78 |
| 5.21 | 80.34 |
| 6.49 | 95.33 |

---

**Code: Computing and Inspecting Residuals**

```python
# Import numpy for numerical operations
import numpy as np

# Import LinearRegression for building the model
from sklearn.linear_model import LinearRegression

# Set seed for reproducibility
rng = np.random.default_rng(seed=99)

# Create 200 students with study hours between 1 and 10
study_hours = rng.uniform(1, 10, size=200)

# Create exam scores using the true formula plus realistic noise
scores = 40 + 7.5 * study_hours + rng.normal(0, 5, size=200)

# Reshape hours for scikit-learn
X = study_hours.reshape(-1, 1)
y = scores

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate predictions for all 200 students
y_pred = model.predict(X)

# Calculate residuals: actual score minus predicted score for each student
residuals = y - y_pred

# Print the first 8 residuals to see individual errors
print("First 8 residuals (actual minus predicted):")
for i in range(8):
    direction = "under-predicted" if residuals[i] > 0 else "over-predicted"
    print(f"  Student {i+1}: residual = {round(residuals[i], 2)} ({direction})")

# Print the average of all residuals — should be very close to zero
avg_residual = residuals.mean()
print(f"\nAverage residual across all 200 students: {round(avg_residual, 4)}")

# Count how many predictions were too low vs too high
under_predicted = (residuals > 0).sum()
over_predicted = (residuals < 0).sum()
print(f"Times model predicted too low:  {under_predicted}")
print(f"Times model predicted too high: {over_predicted}")

# Find the student where the model made its biggest mistake
worst_idx = abs(residuals).argmax()
print(f"\nBiggest error: Student {worst_idx + 1}")
print(f"  Actual score:    {round(y[worst_idx], 1)}")
print(f"  Predicted score: {round(y_pred[worst_idx], 1)}")
print(f"  Residual:        {round(residuals[worst_idx], 1)}")
```

**How the code works:**

- **`y - y_pred`** — Creates 200 individual residuals by subtracting each prediction from the real score. This is a single numpy operation that works on all 200 values at once.
- **The `for` loop** — Prints the first 8 residuals with a human-readable label ("under-predicted" if positive, "over-predicted" if negative).
- **`residuals.mean()`** — If the model is balanced and not systematically biased, the average residual should be extremely close to zero. A large average residual would mean the model is consistently leaning in one direction.
- **`(residuals > 0).sum()` and `(residuals < 0).sum()`** — Counts how many predictions fell short and how many went too high. A well-behaved model will have roughly equal counts on both sides.
- **`abs(residuals).argmax()`** — Finds the index of the largest absolute error — the student where the model was most wrong. This is useful for investigating outliers and understanding edge cases.

---

**The three questions to ask when reading residuals:**

1. **Is the average residual close to zero?** If yes — the model is balanced, not systematically wrong. If no — it's consistently biased in one direction.
2. **Are positive and negative residuals roughly equal in count?** If yes — errors are symmetric and random. If no — the model may be missing a pattern.
3. **Are there any extremely large residuals?** If yes — investigate those specific cases. They are either data entry errors or genuinely unusual situations that your model's current formula cannot handle.

Residuals are the starting point for all model improvement. When you look at them carefully, they often point directly to what the model is missing — a feature that wasn't included, a relationship that isn't quite linear, or outliers in the data that are pulling the predictions in the wrong direction.

---

## Quick Reference: Important Terms, Tools, and Python Commands

| Term / Tool | What It Means | Why It Matters |
|---|---|---|
| **Regression** | Predicting a continuous numeric output from input features | Use when the answer is a number, not a category |
| **Target Variable (y)** | The number you want to predict — the "answer column" | Every regression problem has exactly one target |
| **Feature (x)** | An input column the model uses to make its prediction | More relevant features → better predictions |
| **Linear Regression** | A model that predicts y as a weighted sum of features | The foundational and most interpretable regression model |
| **Intercept** | The model's baseline prediction before any features are considered | Gives the line freedom to sit at the right height |
| **Coefficient** | The multiplier the model learns for each feature | Shows how much the prediction changes per one-unit increase |
| **Best-fit Line** | The line that minimises total prediction error across all training points | This is what the model is actually "finding" during training |
| **`LinearRegression()`** | Creates a linear regression model object in scikit-learn | Starting point for any linear regression task |
| **`.fit(X, y)`** | Trains the model by learning intercept and coefficients from data | All learning happens here — call once on training data |
| **`.predict(X)`** | Uses the trained model to generate numeric predictions | No learning here — pure arithmetic with locked-in weights |
| **`model.intercept_`** | The learned baseline value stored after training | Inspect to understand the model's starting point |
| **`model.coef_`** | Array of learned coefficients stored after training | One value per feature — inspect to understand feature impact |
| **Overfitting** | Model learns training noise; fails on new data | Test accuracy much worse than training accuracy signals this |
| **Underfitting** | Model too simple; misses real patterns even on training data | High error on both training and test data signals this |
| **Generalisation** | Model works well on new, unseen data | The real goal — not just accuracy on training examples |
| **`train_test_split()`** | Splits data into training and testing portions | Essential for honest evaluation of generalisation |
| **Residual** | Actual value minus predicted value for one data point | Positive = under-predicted; Negative = over-predicted |
| **`residuals.mean()`** | Average of all residuals | Should be near zero in a well-calibrated model |
| **`abs(residuals).argmax()`** | Finds the index of the largest prediction error | Use to identify and investigate worst-case predictions |
| **`numpy` (np)** | Python library for fast numeric array operations | Data creation, residual calculation, numeric summaries |
| **`sklearn.linear_model`** | scikit-learn module containing LinearRegression | Standard import for all linear regression work |
| **`sklearn.model_selection`** | scikit-learn module containing train_test_split | Standard import for splitting data |

---

