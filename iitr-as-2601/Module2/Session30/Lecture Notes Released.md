# Classification: Logistic Regression Fundamentals

---

## Where We Left Off — and Where We Are Going

In the last two sessions, we worked entirely with **regression** — a type of machine learning that predicts a **continuous numeric value**, like a student's exam score out of 100, a house's price in rupees, or tomorrow's temperature. We also learned how to measure how good those numeric predictions are using MAE, RMSE, and R-squared. But not every real-world question asks "how much?" — sometimes the question is "which category?"

When you ask "will this student **pass or fail**?", "is this email **spam or not spam**?", or "is this transaction **fraudulent or genuine**?" — you are no longer predicting a number. You are asking the model to choose a **label** from a fixed set of options. This is an entirely different type of problem, and it needs an entirely different type of model — which is exactly what this session introduces.

![Regression vs classification: what the model outputs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/regression_vs_classification.png)

---

## Classification Basics: When Prediction Means Choosing a Category

**Classification:**
- **Official Definition:** A type of supervised machine learning problem where the goal is to predict which **category** (or class) a data point belongs to, based on its input features.
- **In Simple Words:** Instead of predicting a number, the model picks a label from a list. The list could have two options (yes/no, pass/fail, spam/not spam) or many options (cat/dog/bird, Grade A/B/C/D/F).
- **Real-Life Example:** When your bank's system scans your transaction and decides "this is genuine" or "this looks fraudulent," it is running a classification model. The model isn't calculating *how* fraudulent it is on a scale — it is picking a category.

![Binary vs multi-class: how many categories?](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/binary_vs_multiclass_classification.png)

**Two types of classification problems:**

- **Binary Classification** — The model chooses between exactly **two categories**.
  - Examples: Pass or Fail, Spam or Not Spam, Disease Detected or Not, Clicked or Not Clicked.
  - This is the most common starting point and what Logistic Regression is primarily designed for.

- **Multi-class Classification** — The model chooses between **three or more categories**.
  - Examples: Classifying a digit as 0 through 9, predicting a student's grade as A/B/C/D/F, identifying a fruit as mango/banana/apple.
  - This session focuses on binary classification — multi-class is a natural extension of the same ideas.

**Why classification cannot use linear regression:**

You might wonder — why not just use the linear regression we already know? The problem is that linear regression outputs any number on a continuous scale: it might predict 0.85, or 1.73, or even -0.4. But for classification, you need a crisp category: **pass or fail, 0 or 1**. A prediction of -0.4 or 1.73 makes no logical sense when the only valid answers are 0 and 1. Linear regression also does not model probability — it has no built-in way to say "I am 80% sure this student will pass." Logistic Regression solves both of these problems.

**Common real-world classification use cases:**

| Domain | Classification Question | Categories |
|---|---|---|
| Banking | Is this transaction fraudulent? | Fraud / Genuine |
| Healthcare | Does this patient have the disease? | Positive / Negative |
| Email | Is this message spam? | Spam / Not Spam |
| E-commerce | Will this customer buy the product? | Yes / No |
| HR | Will this employee resign this year? | Yes / No |
| Education | Will this student pass the exam? | Pass / Fail |

Now that we understand *what* classification is and *why* it's different from regression, let's look at the most foundational classification algorithm: **Logistic Regression**.

---

## Logistic Regression: Predicting Probability, Not Just a Category

The name "Logistic Regression" can be confusing — it has the word "regression" in it, but it is a **classification** algorithm. The name comes from the mathematics it uses internally (the **logistic function**), not from what it predicts. Do not let the name mislead you — Logistic Regression predicts categories, and it does so by first estimating **probability**.

**Logistic Regression:**
- **Official Definition:** A supervised machine learning algorithm that models the **probability** that a given input belongs to a particular class, using the logistic (sigmoid) function to map any input value to a probability between 0 and 1.
- **In Simple Words:** Logistic Regression looks at the features of each data point and asks: "Based on what I've learned, what is the **probability** that this point belongs to class 1?" If the probability is above a threshold (default: 50%), it predicts class 1. Otherwise, class 0.
- **Real-Life Example:** When a doctor looks at a patient's age, blood pressure, and cholesterol, they form a judgment: "There's about a 75% chance this patient has the condition." They don't say "1.75 units of disease" — they say probability. Logistic Regression does exactly this, in a mathematical, data-driven way.

**The core idea of Logistic Regression:**

- Linear Regression fits a straight line through data and reads off a number at any point.
- Logistic Regression fits an **S-shaped curve** through data and reads off a **probability** (between 0 and 1) at any point.
- That S-shaped curve is the **sigmoid function** — and it is the mathematical engine at the heart of every Logistic Regression model.

**The key difference from Linear Regression in one sentence:** Linear Regression asks "how much?" and Logistic Regression asks "how likely?" — and then converts that likelihood into a category.

---

## The Sigmoid Function: The Engine Inside Logistic Regression

The sigmoid function is what makes Logistic Regression work. Without it, the model would behave like linear regression — producing raw numbers that can go above 1 or below 0. The sigmoid function squeezes any input number — no matter how large or how small — into a value strictly between 0 and 1.

**Sigmoid Function:**
- **Official Definition:** A mathematical function with an S-shaped curve that maps any real number (from negative infinity to positive infinity) to a value strictly between 0 and 1, making it perfect for representing probability.
- **In Simple Words:** Feed any number into the sigmoid function and it gives you back a probability. Feed in a very large positive number → probability close to 1. Feed in a very large negative number → probability close to 0. Feed in zero → probability of exactly 0.5.
- **Real-Life Example:** Think of a water tap. No matter how far you turn it, the water flow is always between "fully closed" (0%) and "fully open" (100%) — it can never go negative or exceed 100%. The sigmoid function is like a mathematical tap that converts raw model scores into neat probabilities between 0 and 1.

**How the sigmoid works conceptually:**

- Logistic Regression first computes a **raw score** using the same formula as linear regression:
  `raw_score = w1×feature1 + w2×feature2 + ... + bias`
- This raw score can be any number — positive, negative, large, small.
- The sigmoid function then converts this raw score into a **probability**:
  `probability = 1 / (1 + e^(-raw_score))`
- If `raw_score` is very large and positive → `probability` approaches 1 (model strongly predicts class 1)
- If `raw_score` is very large and negative → `probability` approaches 0 (model strongly predicts class 0)
- If `raw_score` is exactly 0 → `probability` is exactly 0.5 (the model is uncertain)

![The Sigmoid Function: How Raw Scores Become Probabilities](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/sigmoid_function.png)

**What the S-shape tells you:**

- The **steep part in the middle** — around raw score = 0 — is where the model is most sensitive. A small change in input leads to a noticeable change in probability.
- At the **extreme ends** (far left, far right), the curve flattens — even a large change in input barely changes the probability. The model is very confident at the extremes.
- This is exactly what you want for a classifier — confident predictions when evidence is strong, uncertain predictions when evidence is mixed.

**Connecting to the previous sessions:** Just like ridge and lasso regression learned coefficients (weights) that multiplied each feature to compute a raw score, logistic regression does the same thing. The only difference is that logistic regression then passes that raw score through the sigmoid function to convert it into a probability.

---

## Building a Logistic Regression Model: The First Classification Code

Before writing code with multiple features, let's start with the simplest possible case: **one feature, two outcomes**. This makes the logic easiest to follow and the results easiest to interpret.

**Scenario:** We have 300 students. Each student's exam score was computed from their study hours. A student **passes** (label = 1) if their score is 70 or above, and **fails** (label = 0) otherwise. We want to train a Logistic Regression model that — given only a student's study hours — predicts whether they will pass or fail.

**Example dataset (first 10 rows, rounded):**

| study_hours | exam_score | pass_fail |
|---:|---:|---:|
| 7.97 | 100.3 | 1 |
| 4.95 | 78.1 | 1 |
| 8.73 | 107.0 | 1 |
| 1.85 | 55.8 | 0 |
| 9.78 | 115.4 | 1 |
| 2.15 | 59.5 | 0 |
| 3.07 | 64.7 | 0 |
| 5.05 | 78.4 | 1 |
| 6.12 | 88.9 | 1 |
| 1.22 | 49.8 | 0 |

---

**Complete Code: Training a Logistic Regression Model**

```python
# Import numpy for numerical operations and data generation
import numpy as np

# Import LogisticRegression — the classification model we will use today
from sklearn.linear_model import LogisticRegression

# Import train_test_split to divide data into training and testing sets
from sklearn.model_selection import train_test_split

# Import accuracy_score to measure how many predictions were correct
from sklearn.metrics import accuracy_score

# Set seed so results are identical every time we run
rng = np.random.default_rng(seed=42)

# Create 300 students with study hours randomly between 1 and 10
n = 300
study_hours = rng.uniform(1, 10, size=n)

# Simulate exam scores: base 40, each study hour adds 7.5 marks, plus random noise
scores = 40 + 7.5 * study_hours + rng.normal(0, 8, size=n)

# Create the classification target: 1 = Pass (score >= 70), 0 = Fail
pass_fail = (scores >= 70).astype(int)

# Reshape study_hours into a 2D array (scikit-learn requires this format)
X = study_hours.reshape(-1, 1)

# Our target variable — the label the model needs to learn to predict
y = pass_fail

# Print class distribution — how many students passed vs failed in the dataset
unique, counts = np.unique(y, return_counts=True)
print("Class Distribution in Full Dataset:")
for label, count in zip(unique, counts):
    print(f"  {'Pass' if label == 1 else 'Fail'} ({label}): {count} students")

# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a Logistic Regression model with default settings
model = LogisticRegression()

# Train the model — it learns the relationship between study hours and pass/fail
model.fit(X_train, y_train)

# Predict class labels for the test students — outputs 0 (Fail) or 1 (Pass)
y_pred = model.predict(X_test)

# Predict probabilities — returns [P(Fail), P(Pass)] for each student
y_prob = model.predict_proba(X_test)

# Print predictions for the first 8 test students with full detail
print("\nPredictions on Test Students:")
print(f"{'Student':<10} {'Study Hrs':>10} {'Prediction':>12} {'P(Fail)':>10} {'P(Pass)':>10}")
print("-" * 58)
for i in range(8):
    study  = X_test[i][0]
    pred   = y_pred[i]
    p_fail = y_prob[i][0]
    p_pass = y_prob[i][1]
    label  = "PASS" if pred == 1 else "FAIL"
    print(f"Student {i+1:<3} {study:>10.1f} {label:>12} {p_fail:>10.2f} {p_pass:>10.2f}")

# Overall accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {round(accuracy * 100, 1)}%")
print(f"  → Out of {len(y_test)} test students, {round(accuracy * len(y_test))} were correctly classified")
```

**How the code works:**

- **`(scores >= 70).astype(int)`** — Converts a True/False boolean array into 1s and 0s. This is the standard technique for creating a binary classification label from a continuous value.
- **`LogisticRegression()`** — Creates a Logistic Regression classifier with all default settings. The default decision threshold is 0.5 — a student is predicted as Pass if P(Pass) exceeds 50%.
- **`model.fit(X_train, y_train)`** — Trains the model. Internally, it learns the best sigmoid curve coefficients to separate passes from fails based on study hours.
- **`model.predict(X_test)`** — Returns the final class prediction for each student: either 0 (Fail) or 1 (Pass). The model applies the sigmoid function and threshold automatically.
- **`model.predict_proba(X_test)`** — Returns two probability values per student: `[P(Fail), P(Pass)]`. These always sum to exactly 1.0. This is the raw probability before the threshold converts it to a label.
- **`accuracy_score(y_test, y_pred)`** — Measures the fraction of test students correctly classified. An accuracy of 0.87 means 87 out of 100 students were correctly labelled.

**What to notice in the output:**

- Students with very high study hours (e.g., 8–10) will have P(Pass) values close to 1.0 — the model is very confident they pass.
- Students with very low study hours (e.g., 1–3) will have P(Pass) values close to 0.0 — the model is confident they fail.
- Students around 4–6 study hours may show probabilities near 0.5 — the model is genuinely uncertain about them, and these are the hardest cases to classify correctly.

---

## Model Predictions: Class Labels vs Probability Outputs

When you use `model.predict()`, the model gives you a crisp **label** — 0 or 1. When you use `model.predict_proba()`, it gives you the **underlying probability** that led to that label. Both are useful, but they answer slightly different questions.

**The difference between the two prediction types:**

- **`model.predict()`** — The final answer: *this student passes* or *this student fails*.
  - Useful when you need a definitive decision to act on: approve a loan, flag a transaction, admit a student.
  - The output is always a whole number category (0 or 1 in binary classification).

- **`model.predict_proba()`** — The confidence behind the answer: *this student has an 87% chance of passing*.
  - Useful when you need to know *how certain* the model is, not just what it decided.
  - Enables more nuanced decisions: "If P(Pass) > 0.9, auto-pass. If P(Pass) is between 0.5 and 0.9, send for manual review."
  - The output is always between 0 and 1, and the two columns always sum to 1.

**Why probabilities matter more than labels in practice:**

Consider two students both predicted as "Pass" by the model. Student A has a passing probability of 0.92, and Student B has a passing probability of 0.51. Both get the same label — but very different confidence levels. In a high-stakes scenario (like a scholarship decision), you'd treat these two students very differently. The probability output lets you make that distinction; the label alone cannot.

Now let's upgrade to a more realistic scenario with **three features**: study hours, sleep hours, and number of distractions.

**Example dataset (first 10 rows, rounded):**

| study_hours | sleep_hours | distractions | pass_fail |
|---:|---:|---:|---:|
| 5.6 | 6.2 | 3.1 | 1 |
| 2.3 | 5.8 | 4.4 | 0 |
| 9.1 | 7.4 | 1.2 | 1 |
| 3.8 | 4.5 | 3.9 | 0 |
| 7.2 | 8.1 | 0.7 | 1 |
| 1.4 | 6.0 | 2.8 | 0 |
| 6.5 | 7.0 | 4.0 | 1 |
| 4.9 | 5.5 | 1.5 | 1 |
| 8.7 | 8.5 | 2.1 | 1 |
| 2.8 | 4.9 | 4.9 | 0 |

---

**Complete Code: Multi-Feature Logistic Regression with Detailed Probability Output**

```python
# Import numpy for data creation and array operations
import numpy as np

# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# Import train_test_split
from sklearn.model_selection import train_test_split

# Import accuracy_score for evaluation
from sklearn.metrics import accuracy_score

# Set seed for reproducibility
rng = np.random.default_rng(seed=7)

# Create 400 students with 3 features
n = 400
study_hours  = rng.uniform(1, 10, size=n)   # hours of study (1 to 10)
sleep_hours  = rng.uniform(4, 9, size=n)    # hours of sleep (4 to 9)
distractions = rng.uniform(0, 5, size=n)    # distraction hours per day (0 to 5)

# Simulate exam scores using a realistic multi-feature formula
scores = (
    40
    + 6.5 * study_hours         # study hours contribute most to the score
    + 1.2 * sleep_hours         # sleep has a moderate positive impact
    - 2.0 * distractions        # distractions reduce the score
    + rng.normal(0, 7, size=n)  # random noise to simulate real-world variation
)

# Create the binary target: 1 = Pass (score >= 70), 0 = Fail
y = (scores >= 70).astype(int)

# Stack the three feature arrays into one 2D table (400 rows x 3 columns)
X = np.column_stack([study_hours, sleep_hours, distractions])

# Split: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Generate predictions and probabilities for the test set
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Print detailed predictions for the first 10 test students
print("Detailed Predictions on 10 Test Students:")
print(f"{'#':<4} {'Study':>6} {'Sleep':>6} {'Dist':>5} {'Actual':>8} {'Pred':>8} {'P(Pass)':>9} {'Correct?':>9}")
print("-" * 62)
for i in range(10):
    study  = X_test[i][0]
    sleep  = X_test[i][1]
    dist   = X_test[i][2]
    actual = "Pass" if y_test[i] == 1 else "Fail"
    pred   = "Pass" if y_pred[i] == 1 else "Fail"
    p_pass = y_prob[i][1]
    correct = "Yes" if y_test[i] == y_pred[i] else "No"
    print(f"{i+1:<4} {study:>6.1f} {sleep:>6.1f} {dist:>5.1f} {actual:>8} {pred:>8} {p_pass:>9.2f} {correct:>9}")

# Print overall accuracy
acc = accuracy_score(y_test, y_pred)
print(f"\nOverall Accuracy: {round(acc * 100, 1)}%")

# Show the learned feature weights — what the model thinks matters most
feature_names = ["study_hours", "sleep_hours", "distractions"]
print("\nLearned Feature Weights (Coefficients):")
for name, coef in zip(feature_names, model.coef_[0]):
    direction = "increases chance of passing" if coef > 0 else "decreases chance of passing"
    print(f"  {name:<15}: {round(coef, 3):>8}  → {direction}")
```

**How the code works:**

- **`np.column_stack([...])`** — Combines three separate feature arrays into one 2D table with 400 rows and 3 columns. Each row is one student's complete record.
- **`y_prob[i][1]`** — The probability of class 1 (Pass) for student i. Index `[0]` is always P(Fail), index `[1]` is always P(Pass). They always sum to 1.0.
- **`model.coef_[0]`** — The learned weight (coefficient) for each feature. A **positive coefficient** means higher values of that feature push the model toward predicting Pass. A **negative coefficient** means higher values push toward predicting Fail. This is very similar to how regression coefficients work.
- **The "Correct?" column** — Shows whether each prediction matched the actual label, making it easy to spot where the model goes wrong.
- **What the coefficients tell you** — If `study_hours` has a large positive coefficient and `distractions` has a large negative one, it confirms the model has correctly learned that more study helps and more distractions hurt — matching real life.

---

## Decision Threshold: Where the Line Gets Drawn

The default behaviour of Logistic Regression is: if P(Pass) >= **0.5**, predict Pass; otherwise, predict Fail. This 0.5 cut-off is called the **decision threshold**. It is not fixed — you can change it, and doing so has real consequences for the types of mistakes the model makes.

**Decision Threshold:**
- **Official Definition:** The probability value above which the model assigns a data point to the positive class (class 1). Below this value, the model assigns the data point to the negative class (class 0).
- **In Simple Words:** Imagine the model says "this student has a 48% chance of passing." With a threshold of 0.5, the model predicts Fail. If you lower the threshold to 0.4, the same 48% would now trigger a Pass prediction. The threshold is the line that converts a probability into a yes/no decision.
- **Real-Life Example:** A hospital screening test for a serious disease. If you use a high threshold (0.8), you only flag a patient as positive when very confident — reducing false alarms but potentially missing real cases. If you lower the threshold to 0.3, you flag more patients — catching more true cases but also generating more false alarms. Choosing the right threshold is a **business decision**, not just a mathematical one.

![Decision Threshold Effect on Classification Predictions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/decision_threshold_effect.png)

**The two trade-offs a threshold change creates:**

- **Lowering the threshold (e.g., from 0.5 to 0.3):**
  - More students get predicted as Pass — the model becomes more generous.
  - You catch more actual passes (fewer missed real positives), but you also falsely predict some failing students as passing.
  - Use this when: **missing a positive case is very costly** (e.g., not catching a disease, missing a fraud case).

- **Raising the threshold (e.g., from 0.5 to 0.7):**
  - Fewer students get predicted as Pass — the model becomes more strict.
  - You only predict Pass when very confident — but you may miss borderline students who actually passed.
  - Use this when: **a false positive is very costly** (e.g., falsely approving a loan for someone who will default).

---

**Complete Code: Seeing the Effect of Different Thresholds**

```python
# Import numpy for data generation and array operations
import numpy as np

# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# Import train_test_split
from sklearn.model_selection import train_test_split

# Set seed
rng = np.random.default_rng(seed=7)

# Build the same 400-student, 3-feature dataset as before
n = 400
study_hours  = rng.uniform(1, 10, size=n)
sleep_hours  = rng.uniform(4, 9, size=n)
distractions = rng.uniform(0, 5, size=n)

scores = (
    40
    + 6.5 * study_hours
    + 1.2 * sleep_hours
    - 2.0 * distractions
    + rng.normal(0, 7, size=n)
)
y = (scores >= 70).astype(int)
X = np.column_stack([study_hours, sleep_hours, distractions])

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Extract only the Pass probability (class 1) for all test students
# predict_proba returns [P(Fail), P(Pass)] — we take the second column
y_prob_pass = model.predict_proba(X_test)[:, 1]

# Define three different thresholds to compare
thresholds = [0.3, 0.5, 0.7]

print("Effect of Decision Threshold on Predictions:")
print("=" * 62)

for threshold in thresholds:
    # Apply the custom threshold manually to the probability array
    # Any student where P(Pass) >= threshold is labelled as Pass (1)
    y_pred_custom = (y_prob_pass >= threshold).astype(int)

    # Count predicted labels
    predicted_pass = y_pred_custom.sum()
    predicted_fail = len(y_pred_custom) - predicted_pass

    # Overall accuracy at this threshold
    correct  = (y_pred_custom == y_test).sum()
    accuracy = correct / len(y_test)

    # False Positives: model predicted Pass but student actually Failed
    false_positives = ((y_pred_custom == 1) & (y_test == 0)).sum()

    # False Negatives: model predicted Fail but student actually Passed
    false_negatives = ((y_pred_custom == 0) & (y_test == 1)).sum()

    print(f"\nThreshold = {threshold}:")
    print(f"  Predicted Pass  : {predicted_pass} students")
    print(f"  Predicted Fail  : {predicted_fail} students")
    print(f"  Accuracy        : {round(accuracy * 100, 1)}%")
    print(f"  False Positives : {false_positives}  (said Pass, was actually Fail)")
    print(f"  False Negatives : {false_negatives}  (said Fail, was actually Pass)")
```

**How the code works:**

- **`model.predict_proba(X_test)[:, 1]`** — Extracts only the Pass probability column from the output. The `[:, 1]` notation means "all rows, second column" — which is always P(class=1).
- **`(y_prob_pass >= threshold).astype(int)`** — Manual threshold application. For each student, if their P(Pass) is at or above the threshold, the prediction is 1 (Pass); otherwise 0 (Fail). This overrides the model's default 0.5 threshold.
- **`(y_pred_custom == 1) & (y_test == 0)`** — A condition that is True only when the model predicted Pass but the student actually failed. Summing this gives the total number of False Positives.
- **`(y_pred_custom == 0) & (y_test == 1)`** — The opposite: model predicted Fail but student actually passed. These are False Negatives — "missed" real passes.
- **The trade-off pattern in output** — As the threshold drops from 0.7 to 0.3, Predicted Pass goes up, False Negatives go down, but False Positives go up. Accuracy may slightly drop — but that doesn't mean a lower threshold is wrong. It depends entirely on which type of error is more costly in your real-world context.

**What to observe in the output:**

- At threshold = 0.3: More students predicted as Pass. Fewer real passes missed (low false negatives), but more false alarms (higher false positives).
- At threshold = 0.5: Balanced — the default. Works well when both types of errors are equally costly.
- At threshold = 0.7: Very strict. Few students predicted as Pass — only when the model is highly confident. Low false positives, but more real passes go undetected.

---

## Confusion Matrix: Unpacking What the Model Got Right and Wrong

A single accuracy number tells you what percentage of predictions were correct. But it doesn't tell you *what kinds of mistakes* the model is making. The **Confusion Matrix** is a simple 2×2 table that breaks down every prediction into four categories — and it is the most important diagnostic tool for any classification model.

**Confusion Matrix:**
- **Official Definition:** A table that compares a classification model's predictions against the actual true labels, categorising every prediction as a True Positive, True Negative, False Positive, or False Negative.
- **In Simple Words:** Instead of just counting "how many did the model get right?", the confusion matrix tells you: "how many did it correctly identify as Pass? How many did it correctly identify as Fail? And how many did it get wrong in each direction?"
- **Real-Life Example:** Imagine a doctor who reviews 100 patient test results and says "positive" or "negative" for a disease. A confusion matrix would show: how many actual sick patients were correctly called positive (caught), how many were missed (called negative but were actually sick), how many healthy patients were falsely alarmed, and how many were correctly cleared. These four outcomes have very different real-world consequences.

**The four cells of the Confusion Matrix:**

![Confusion Matrix — Four Outcomes of a Binary Classifier](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/confusion_matrix.png)

| | **Predicted: Pass (1)** | **Predicted: Fail (0)** |
|---|---|---|
| **Actual: Pass (1)** | **True Positive (TP)** | **False Negative (FN)** |
| **Actual: Fail (0)** | **False Positive (FP)** | **True Negative (TN)** |

**Breaking down each cell:**

- **True Positive (TP):**
  - Model said: Pass. Reality: Pass. **Correct!**
  - The model correctly identified a student who genuinely passed.
  - Example: The model predicted a student with 8 study hours would pass — and they did.
  - *You want this number to be high.*

- **True Negative (TN):**
  - Model said: Fail. Reality: Fail. **Correct!**
  - The model correctly identified a student who genuinely failed.
  - Example: The model predicted a student with 2 study hours would fail — and they did.
  - *You want this number to be high.*

- **False Positive (FP)** — also called a **Type I Error:**
  - Model said: Pass. Reality: Fail. **Wrong!**
  - The model was too optimistic — it predicted the student would pass, but they actually failed.
  - Real-life analogy: Approving a bank loan for a customer who ends up defaulting.
  - *This is dangerous when false alarms are costly.*

- **False Negative (FN)** — also called a **Type II Error:**
  - Model said: Fail. Reality: Pass. **Wrong!**
  - The model was too pessimistic — it predicted fail, but the student actually passed.
  - Real-life analogy: A disease screening test telling a sick person they are healthy — potentially life-threatening.
  - *This is dangerous when missed detections are costly.*

**Quick memory trick:**
- **True/False** = Was the model's prediction *correct*?
- **Positive/Negative** = What did the model *predict*?
- So: "True Positive" = Model predicted Positive AND was correct. "False Positive" = Model predicted Positive but was WRONG.

---

**Complete Code: Computing and Interpreting the Confusion Matrix**

```python
# Import numpy for data creation
import numpy as np

# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# Import train_test_split
from sklearn.model_selection import train_test_split

# Import confusion_matrix to build the 2x2 classification breakdown table
from sklearn.metrics import confusion_matrix

# Import accuracy_score for overall model correctness
from sklearn.metrics import accuracy_score

# Set seed
rng = np.random.default_rng(seed=7)

# Build the same 400-student, 3-feature dataset
n = 400
study_hours  = rng.uniform(1, 10, size=n)
sleep_hours  = rng.uniform(4, 9, size=n)
distractions = rng.uniform(0, 5, size=n)

scores = (
    40
    + 6.5 * study_hours
    + 1.2 * sleep_hours
    - 2.0 * distractions
    + rng.normal(0, 7, size=n)
)
y = (scores >= 70).astype(int)
X = np.column_stack([study_hours, sleep_hours, distractions])

# Split: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Get class label predictions for the test set
y_pred = model.predict(X_test)

# --- Step 1: Compute the confusion matrix ---
# sklearn layout: [[TN, FP], [FN, TP]]
# Row 0 = actual Negative (Fail), Row 1 = actual Positive (Pass)
# Column 0 = predicted Negative, Column 1 = predicted Positive
cm = confusion_matrix(y_test, y_pred)

# Extract each cell individually for clarity
tn = cm[0][0]   # True Negatives: predicted Fail, was actually Fail
fp = cm[0][1]   # False Positives: predicted Pass, was actually Fail
fn = cm[1][0]   # False Negatives: predicted Fail, was actually Pass
tp = cm[1][1]   # True Positives: predicted Pass, was actually Pass

# --- Step 2: Print the confusion matrix in a readable layout ---
print("Confusion Matrix:")
print("=" * 50)
print(f"                     Pred Fail    Pred Pass")
print(f"  Actual Fail  :     TN = {tn:<8}  FP = {fp}")
print(f"  Actual Pass  :     FN = {fn:<8}  TP = {tp}")
print("=" * 50)

# --- Step 3: Interpret each number in plain English ---
print("\nWhat Each Number Means:")
print(f"  True Positives  (TP) = {tp:<4} → Said Pass,  was actually Pass  ✓")
print(f"  True Negatives  (TN) = {tn:<4} → Said Fail,  was actually Fail  ✓")
print(f"  False Positives (FP) = {fp:<4} → Said Pass,  was actually Fail  ✗ (over-optimistic)")
print(f"  False Negatives (FN) = {fn:<4} → Said Fail,  was actually Pass  ✗ (missed real pass)")

# --- Step 4: Derive accuracy manually from the confusion matrix ---
total = tn + fp + fn + tp
accuracy_manual = (tp + tn) / total
print(f"\nManual Accuracy: (TP + TN) / Total = ({tp} + {tn}) / {total} = {round(accuracy_manual * 100, 1)}%")

# Verify using scikit-learn — both must give the same number
accuracy_sklearn = accuracy_score(y_test, y_pred)
print(f"sklearn accuracy_score result:                        {round(accuracy_sklearn * 100, 1)}%")

# --- Step 5: Compute and explain error rates ---
error_rate = (fp + fn) / total
print(f"\nOverall Error Rate: {round(error_rate * 100, 1)}%")

fp_rate = fp / (fp + tn) if (fp + tn) > 0 else 0
fn_rate = fn / (fn + tp) if (fn + tp) > 0 else 0

print(f"  False Positive Rate: {fp}/{fp + tn} = {round(fp_rate * 100, 1)}%")
print(f"    → Of all students who actually Failed, this % were wrongly called Pass")
print(f"  False Negative Rate: {fn}/{fn + tp} = {round(fn_rate * 100, 1)}%")
print(f"    → Of all students who actually Passed, this % were wrongly called Fail")
```

**How the code works:**

- **`confusion_matrix(y_test, y_pred)`** — Takes actual labels and model predictions, then returns a 2×2 NumPy array. The standard layout is always: `[[TN, FP], [FN, TP]]`. Memorise this layout — you will use it constantly.
- **`cm[0][0]`, `cm[0][1]`, `cm[1][0]`, `cm[1][1]`** — Direct cell extraction. Top-left is TN, top-right is FP, bottom-left is FN, bottom-right is TP.
- **`(tp + tn) / total`** — Accuracy computed manually from the confusion matrix. This confirms that accuracy is simply the fraction of predictions that landed on the "correct diagonal" (TP + TN).
- **False Positive Rate** — Of all students who actually failed, what fraction did the model incorrectly label as passing? This is the "false alarm rate."
- **False Negative Rate** — Of all students who actually passed, what fraction did the model incorrectly label as failing? This is the "miss rate" — especially critical in medical or safety contexts.

---

**What to look for in a Confusion Matrix:**

- **If FP is very high** → The model is too generous. It's calling too many students "Pass." Consider raising the decision threshold.
- **If FN is very high** → The model is too conservative. It's missing too many real passes. Consider lowering the decision threshold.
- **If TP + TN dominates** → The model is performing well on both classes.
- **If TP is near zero despite high accuracy** → Suspect a class imbalance problem. The model may be performing well only because it always predicts the majority class.

**A real-world worked example — medical screening:**

Imagine a COVID test run on 1,000 people where 100 are actually positive and 900 are actually negative. A model that always predicts "Negative" gets 90% accuracy — but TP = 0. It catches zero actual patients. The Confusion Matrix reveals this instantly: TP=0, FN=100, FP=0, TN=900. Accuracy alone completely misled us — the Confusion Matrix told the truth.

This is why the Confusion Matrix is one of the first things any data scientist inspects after training a classifier, and why you will keep using it in every classification project going forward. In the next session, we will build on this foundation by introducing Decision Trees, Random Forests, and more advanced classification evaluation metrics like Precision, Recall, F1 Score, and ROC-AUC.

---

## Key Takeaways

- **Classification predicts categories, not numbers.** When the question is "which class?" instead of "how much?", regression is the wrong tool — you need a model that outputs a discrete label like pass/fail, spam/not spam, or fraud/genuine.

- **Logistic Regression is a classification algorithm despite its name.** It uses the same linear formula as regression (`w1×f1 + w2×f2 + bias`) to compute a raw score, then passes that score through the sigmoid function to convert it into a probability between 0 and 1.

- **The sigmoid function is the engine that makes it all work.** It takes any real number — no matter how large or small — and squeezes it into a probability between 0 and 1. Large positive inputs → probability near 1, large negative inputs → probability near 0, input of 0 → probability of exactly 0.5.

- **Probabilities are more informative than labels.** `model.predict()` gives you a crisp 0 or 1, but `model.predict_proba()` tells you *how confident* the model is. Two students both predicted as "Pass" with probabilities 0.51 and 0.92 are very different cases — only probabilities reveal that.

- **Coefficients reveal what the model has learned.** `model.coef_[0]` shows the weight assigned to each feature. Positive coefficients push predictions toward class 1; negative coefficients push toward class 0. This makes Logistic Regression highly interpretable.

- **The decision threshold is a business choice, not a mathematical one.** The default 0.5 is just a convention — lowering it (e.g., to 0.3) catches more positives at the cost of more false alarms; raising it (e.g., to 0.7) makes the model stricter. The right threshold depends on which kind of error is more costly in your context.

- **Accuracy alone can mislead you.** A model that always predicts the majority class can achieve high accuracy on imbalanced data while catching zero real positives. Never trust accuracy in isolation — always inspect the Confusion Matrix.

- **The Confusion Matrix breaks predictions into four outcomes: TP, TN, FP, FN.** True Positives and True Negatives are correct predictions you want to maximise. False Positives (Type I errors — false alarms) and False Negatives (Type II errors — missed detections) have very different real-world consequences depending on the domain.

- **FP vs FN trade-off drives threshold tuning.** If False Positives dominate, raise the threshold to make the model more conservative. If False Negatives dominate, lower the threshold to make the model more generous. The Confusion Matrix tells you which direction to move.

- **Memory trick for the four cells:** "True/False" = was the prediction correct? "Positive/Negative" = what did the model predict? So "False Negative" means the model predicted Negative and was wrong — it missed a real positive case.

---

## Quick Reference: Important Terms, Tools, and Python Commands

| Term / Tool | What It Means | Why It Matters |
|---|---|---|
| **Classification** | Predicting which category a data point belongs to | Core task when output is a label, not a number |
| **Binary Classification** | Classification with exactly two possible output classes | Most common form; logistic regression is designed for this |
| **Multi-class Classification** | Classification with three or more output categories | Natural extension of binary classification |
| **Logistic Regression** | Algorithm that predicts probability of class membership using the sigmoid function | Foundational classification algorithm; simple and interpretable |
| **Sigmoid Function** | S-shaped curve converting any number into a probability between 0 and 1 | The mathematical engine of Logistic Regression |
| **Raw Score** | Linear combination of features before sigmoid is applied (`w1×f1 + w2×f2 + bias`) | Same formula as linear regression — sigmoid is applied on top |
| **P(Pass) / P(class=1)** | Probability the model assigns that a data point belongs to the positive class | Core output of logistic regression; drives the label decision |
| **Decision Threshold** | Probability cut-off above which a point is classified as positive (default: 0.5) | Changing it shifts the trade-off between false positives and false negatives |
| **Confusion Matrix** | A 2×2 table showing TP, TN, FP, FN counts for a classifier | The most complete picture of a classifier's error types |
| **True Positive (TP)** | Model predicted positive, and it was actually positive | Correct detection — you want this high |
| **True Negative (TN)** | Model predicted negative, and it was actually negative | Correct rejection — you want this high |
| **False Positive (FP)** | Model predicted positive, but it was actually negative — Type I Error | False alarm — costly in loan approval, ad targeting |
| **False Negative (FN)** | Model predicted negative, but it was actually positive — Type II Error | Missed detection — dangerous in medical or fraud contexts |
| **Accuracy** | (TP + TN) / Total predictions | Overall correctness; can be misleading with imbalanced classes |
| **False Positive Rate** | FP / (FP + TN) — fraction of actual negatives wrongly called positive | Measures how often the model raises false alarms |
| **False Negative Rate** | FN / (FN + TP) — fraction of actual positives wrongly called negative | Measures how often the model misses real positive cases |
| **`LogisticRegression()`** | Creates a Logistic Regression classifier | Import from `sklearn.linear_model` |
| **`model.fit(X_train, y_train)`** | Trains the model on labelled data | Must be called before predict or predict_proba |
| **`model.predict(X_test)`** | Returns predicted class labels (0 or 1) for each input row | Uses default 0.5 threshold internally |
| **`model.predict_proba(X_test)`** | Returns `[P(class=0), P(class=1)]` for each input row | Index `[:, 1]` to get just the positive-class probabilities |
| **`model.predict_proba(X_test)[:, 1]`** | Extracts only the positive-class probability column | Standard way to get P(class=1) for threshold tuning |
| **`(y_prob >= threshold).astype(int)`** | Manual threshold application to convert probabilities into labels | Overrides the default 0.5; use for custom threshold tuning |
| **`model.coef_[0]`** | Learned weights (coefficients) for each feature | Positive = pushes toward class 1; Negative = pushes toward class 0 |
| **`confusion_matrix(y_test, y_pred)`** | Returns `[[TN, FP], [FN, TP]]` as a 2×2 NumPy array | Import from `sklearn.metrics`; always inspect after training |
| **`accuracy_score(y_test, y_pred)`** | Returns fraction of correctly classified samples | Import from `sklearn.metrics`; use alongside confusion matrix |
| **`np.unique(y, return_counts=True)`** | Returns unique class labels and their counts | Useful for checking class distribution before training |
| **`(condition).sum()`** | Counts the number of True values in a boolean array | Used to count FP, FN, TP, TN manually from arrays |

---