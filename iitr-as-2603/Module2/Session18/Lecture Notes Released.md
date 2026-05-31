# Classification: Logistic Regression Fundamentals

## Context of This Session

In the previous session, you stayed in the **regression** world — controlling model complexity with **Ridge** and **Lasso**, reporting **MAE**, **RMSE**, and **R²** on test data, and running **error analysis** by feature groups. Every answer was a **number on a scale** (exam marks, salary, house price).

Many real questions are different: *Will this student **pass or fail**? Is this email **spam or not spam**? Is this transaction **fraud or genuine**?* The output is a **category**, not a measured quantity. This session introduces **classification** and your first classifier: **Logistic Regression**.

**In this session, you will:**

- Contrast **classification** with **regression** and name common use cases
- Understand **Logistic Regression** as a **probability-based** predictor and meet the **sigmoid** idea
- Read **class labels** and **probability outputs** from a trained model
- See how the **decision threshold** changes predictions and mistake types
- Build and interpret a **confusion matrix** (TP, TN, FP, FN)
- See how a **decision boundary** separates classes (unlike a regression best-fit line)
- Apply the same **train–test + pipeline** workflow on real datasets (breast cancer, credit default)

---

## Classification Basics: When the Answer Is a Category

**Classification:**

- **Official Definition:** A supervised learning task where the model predicts which **category (class)** a row belongs to, based on its **features**.
- **In Simple Words:** The model picks a label from a fixed list — pass/fail, spam/not spam, fraud/genuine — instead of guessing a number.
- **Real-Life Example:** Your bank scans a transaction and labels it **Fraud** or **Genuine**. It is not predicting *how fraudulent* on a rupee scale — it is choosing a box.

![Regression vs classification: what the model outputs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/regression_vs_classification.png)

**Regression (quick contrast):** Predicts a **continuous number** — exam score, house price, delivery minutes. You measured this in the previous session with MAE and RMSE.

| Question shape | Example | Problem type |
|---|---|---|
| How much / how many? | What exam score? What salary? | **Regression** |
| Which category? | Pass or fail? Spam or not? | **Classification** |

**Two common forms:**

- **Binary classification** — exactly **two** classes (Pass/Fail, Yes/No). Logistic Regression starts here.
- **Multi-class classification** — **three or more** classes (Grade A/B/C/D/F, or slow/medium/fast). Same ideas extend later; today's focus is **binary**.

**Decision boundary (intuition):**

- **Official Definition:** The line, plane, or surface learned by a classifier that **best separates** the classes in feature space; new rows are labelled by which side they fall on.
- **In Simple Words:** Imagine red and green points on a chart — classification draws the **best dividing line** between them. Regression, by contrast, draws a line **through** the points to predict a number.
- **Real-Life Example:** A bank separates "likely default" vs "likely pay on time" customers using credit history and bill patterns — the model's boundary is that dividing rule, not a salary-style number.

Logistic Regression learns this separation during **`fit`**, then uses **`predict`** to place new data on one side of the boundary.

**Why plain linear regression fails here:** Linear regression can output **any** number — 1.73, −0.4, 85.2. For pass/fail (0 or 1), values like −0.4 or 1.73 are meaningless. Regression also has no built-in **probability** ("80% chance of pass"). Logistic Regression fixes both.

| Domain | Question | Classes |
|---|---|---|
| Banking | Fraudulent transaction? | Fraud / Genuine |
| Email | Spam? | Spam / Not Spam |
| HR | Will employee resign? | Yes / No |
| Education | Will student pass? | Pass / Fail |

### Quick Activity — Regression or Classification?

Write **R** or **C** for each:

1. Predict tomorrow's max temperature in °C  
2. Predict loan **approved** or **rejected**  
3. Predict exact exam **score** out of 100  
4. Predict whether email is **spam**

**Answers:** 1 → R, 2 → C, 3 → R, 4 → C.

---

## Logistic Regression and the Sigmoid Function

The name says "regression," but Logistic Regression is a **classification** algorithm. It estimates **probability**, then converts that into a class label.

**Logistic Regression:**

- **Official Definition:** An algorithm that models the **probability** of class membership using a **sigmoid** function to map a raw score into a value between **0 and 1**.
- **In Simple Words:** "Based on study hours and distractions, this student has a **73% chance** of passing." If that probability crosses a cut-off, you label them Pass.
- **Real-Life Example:** A doctor says "about 75% chance of this condition" — not "1.75 units of disease." Logistic Regression does the same, from data.

**Core flow:**

1. Compute a **raw score** — same weighted-sum idea as linear regression: `w1×feature1 + w2×feature2 + … + bias`
2. Pass it through the **sigmoid** — squeezes any number into **(0, 1)** as a probability
3. Compare probability to a **threshold** (default **0.5**) → final class **0** or **1**

**Sigmoid Function:**

- **Official Definition:** An S-shaped function mapping any real number to a value strictly between 0 and 1.
- **In Simple Words:** Large positive raw score → probability near **1**. Large negative → near **0**. Raw score **0** → probability **0.5** (uncertain).
- **Real-Life Example:** A tap flow is always between fully closed (0%) and fully open (100%) — never negative or above 100%. Sigmoid is the mathematical version for probabilities.

![The Sigmoid Function: How Raw Scores Become Probabilities](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/sigmoid_function.png)

**Link to the previous session:** Ridge and Lasso learned **coefficients** that weight each feature. Logistic Regression learns weights the same way — then applies sigmoid instead of outputting a raw mark or price.

**One-sentence contrast:** Linear regression asks *"how much?"* Logistic Regression asks *"how likely?"* — then picks a category.

---

## Training Logistic Regression: Labels, Probabilities, and Predictions

**Scenario:** Students with **study hours**; **Pass (1)** if exam score ≥ 70, else **Fail (0)**. Train a model to predict pass/fail from hours alone.

```python
# Import libraries for data, model, split, and accuracy
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Reproducible sample data — 300 students
rng = np.random.default_rng(seed=42)
study_hours = rng.uniform(1, 10, size=300)
scores = 40 + 7.5 * study_hours + rng.normal(0, 8, size=300)

# Binary label: 1 = Pass (score >= 70), 0 = Fail
y = (scores >= 70).astype(int)
X = study_hours.reshape(-1, 1)

# Honest split — same habit as regression work
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train Logistic Regression (default threshold = 0.5)
model = LogisticRegression()
model.fit(X_train, y_train)

# Class labels: 0 or 1
y_pred = model.predict(X_test)

# Probabilities: [P(Fail), P(Pass)] per row — always sum to 1.0
y_prob = model.predict_proba(X_test)

# Inspect first few test students
print(f"{'Study hrs':>10} {'Pred':>6} {'P(Fail)':>10} {'P(Pass)':>10}")
for i in range(5):
    pred_label = "Pass" if y_pred[i] == 1 else "Fail"
    print(f"{X_test[i][0]:>10.1f} {pred_label:>6} {y_prob[i][0]:>10.2f} {y_prob[i][1]:>10.2f}")

acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {round(acc * 100, 1)}%")
```

**How the code works:**

- **`(scores >= 70).astype(int)`** — turns True/False into **1/0** labels; standard way to build a binary target.
- **`model.predict(X_test)`** — final **class** answer (Pass/Fail) using the default **0.5** threshold.
- **`model.predict_proba(X_test)`** — **confidence** behind the label; column `[1]` is **P(Pass)**.
- **`accuracy_score`** — fraction of test rows where prediction matches actual label.

**Labels vs probabilities in practice:**

- Use **`predict()`** when you need one action: approve loan, flag fraud, mark pass.
- Use **`predict_proba()`** when **confidence** matters: auto-approve at P(Pass) > 0.9, manual review between 0.5 and 0.9.
- Two students both labelled **Pass** with P(Pass) = 0.92 vs 0.51 are very different — probabilities expose that; labels alone do not.

### Quick Activity — Read Probabilities

| Student | P(Pass) | Prediction at threshold 0.7 | Prediction at threshold 0.5 |
|---:|---:|---|---|
| A | 0.91 | ? | ? |
| B | 0.48 | ? | ? |

**Answers:** A → **Pass** at both thresholds. B → **Fail** at 0.7 and at 0.5 (0.48 < 0.5).

---

## Decision Threshold: Where Probability Becomes Yes or No

By default, Logistic Regression predicts **Pass** when **P(Pass) ≥ 0.5**. That cut-off is the **decision threshold** — you can change it, and the **types of mistakes** shift.

**Decision Threshold:**

- **Official Definition:** The probability value above which a row is assigned to the **positive class** (class 1); below it, class 0.
- **In Simple Words:** P(Pass) = 0.48 → **Fail** at threshold 0.5; **Pass** at threshold 0.4. Same probability, different decision.
- **Real-Life Example:** Disease screening at threshold **0.8** → fewer false alarms, more missed cases. At **0.3** → catch more real cases, more false alarms. The right cut-off is a **business choice**.

![Decision Threshold Effect on Classification Predictions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/decision_threshold_effect.png)

| Change | Effect | Use when |
|---|---|---|
| **Lower** threshold (e.g. 0.3) | More predicted Pass; fewer missed passes (↓ FN); more false passes (↑ FP) | Missing a positive is costly (e.g. disease, fraud) |
| **Raise** threshold (e.g. 0.7) | Fewer predicted Pass; fewer false passes (↓ FP); more missed passes (↑ FN) | False alarms are costly (loan default, spam filter) |

```python
# After model.fit on X_train, y_train — get P(Pass) for all test rows
y_prob_pass = model.predict_proba(X_test)[:, 1]

for threshold in [0.3, 0.5, 0.7]:
    # Manual labels: Pass if probability >= threshold
    y_pred_t = (y_prob_pass >= threshold).astype(int)
    fp = ((y_pred_t == 1) & (y_test == 0)).sum()  # predicted Pass, was Fail
    fn = ((y_pred_t == 0) & (y_test == 1)).sum()  # predicted Fail, was Pass
    acc = (y_pred_t == y_test).mean()
    print(f"Threshold {threshold}: accuracy={round(acc*100,1)}%  FP={fp}  FN={fn}")
```

**How the code works:**

- **`[:, 1]`** — second column of `predict_proba` = **P(Pass)** only.
- **`(y_prob_pass >= threshold).astype(int)`** — custom threshold without retraining the model.
- **FP / FN counts** — show the trade-off accuracy alone hides.

---

## Confusion Matrix: Four Types of Right and Wrong

**Accuracy** is one number — correct fraction. It does not say *which* mistakes happened. The **confusion matrix** is a 2×2 table every classifier should get.

**Confusion Matrix:**

- **Official Definition:** A table comparing predicted vs actual labels, counting **True Positive**, **True Negative**, **False Positive**, and **False Negative** outcomes.
- **In Simple Words:** Not just "87% correct" — but how many passes were caught, how many fails were caught, and how many wrong calls in each direction.
- **Real-Life Example:** A disease screen on 1,000 people: always predicting "No disease" gives **90% accuracy** if 900 are healthy — but **TP = 0** (zero sick people caught). The matrix exposes that; accuracy alone misleads.

![Confusion Matrix — Four Outcomes of a Binary Classifier](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session30/confusion_matrix.png)

| | **Predicted Pass (1)** | **Predicted Fail (0)** |
|---|---|---|
| **Actual Pass (1)** | **TP** — correct pass | **FN** — missed pass |
| **Actual Fail (0)** | **FP** — false alarm | **TN** — correct fail |

**Memory trick:** **True/False** = was the prediction correct? **Positive/Negative** = what did the model predict?

- **FP:** Said Pass, was Fail — false alarm (too optimistic; e.g. bad loan approval).
- **FN:** Said Fail, was Pass — missed case (e.g. patient has disease but model says healthy).

```python
from sklearn.metrics import confusion_matrix, accuracy_score

# y_pred from model.predict(X_test) on the same test split
cm = confusion_matrix(y_test, y_pred)

# sklearn layout: [[TN, FP], [FN, TP]]
tn, fp, fn, tp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

print("                     Pred Fail    Pred Pass")
print(f"  Actual Fail  :     TN = {tn:<6}  FP = {fp}")
print(f"  Actual Pass  :     FN = {fn:<6}  TP = {tp}")

accuracy = (tp + tn) / (tp + tn + fp + fn)
print(f"\nAccuracy = (TP + TN) / Total = {round(accuracy * 100, 1)}%")
print(f"sklearn check: {round(accuracy_score(y_test, y_pred) * 100, 1)}%")
```

**How the code works:**

- **`confusion_matrix(y_test, y_pred)`** — always returns `[[TN, FP], [FN, TP]]` for binary problems.
- **Diagonal (TP + TN)** — correct predictions; off-diagonal (FP + FN) — errors.
- **High FP** → model too generous; try **raising** threshold. **High FN** → too strict; try **lowering** threshold.

### Quick Activity — Spot the Risk

A fraud model: **TP = 40**, **TN = 850**, **FP = 5**, **FN = 105**.

1. Which error type is larger — false alarms or missed fraud?  
2. Would you lower or raise the threshold to catch more fraud?

**Answers:** 1 → **FN = 105** (missed fraud). 2 → **Lower** threshold (accept more FP to reduce FN) — if missing fraud is costly.

---

## Real-World Case Studies: Same Workflow, New Domains

The pass/fail study-hours example shows the mechanics. In class you also ran the **same pipeline pattern** on real problems: **medical diagnosis** and **credit default**. The steps do not change — only the data and the business meaning of FP vs FN.

### Breast Cancer: Malignant vs Benign

**Goal:** Use tumour measurements to predict **malignant** vs **benign**. Several features need scaling before logistic regression — use a **Pipeline** (same habit as the housing regression case study).

```python
# Built-in breast cancer dataset from scikit-learn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load features (X) and labels (y): 0 = malignant, 1 = benign
data = load_breast_cancer()
X, y = data.data, data.target

# Train/test split — evaluate only on held-out rows
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features, then fit logistic regression (no leakage: scaler fits on train only)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipe.fit(X_train, y_train)

# Hard labels and probabilities on test data
y_pred = pipe.predict(X_test)
y_prob = pipe.predict_proba(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"Test accuracy: {round(acc * 100, 1)}%")
print("Confusion matrix [[TN, FP], [FN, TP]]:")
print(cm)
```

**How the code works:**

- **`load_breast_cancer()`** — ready-made dataset; no CSV upload needed.
- **`Pipeline`** — applies scaling on train, then the classifier; test rows use the same scaler learned from train.
- **`predict_proba`** — same as the student example; inspect **FN** if missing malignant cases is unacceptable in healthcare.

High test accuracy here is encouraging — but always read the **confusion matrix**, not accuracy alone.

### Credit Card Default: When 80% Accuracy Hides Bad Mistakes

**Goal:** From billing and payment history, predict whether a customer will **default next month** (1) or **not** (0). The UCI credit-card dataset (course CSV) is real bank-style data.

**Business angle:** A **false negative** means the model said "will not default" but the customer **did** — the bank loses money. Executives care about **how many** FN and FP, not just one accuracy number.

```python
# UCI "Default of Credit Card Clients" — use the CSV from course materials
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load data; last column is default next month (0/1)
df = pd.read_csv("uci_credit_card.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].astype(int).values

# Split, pipeline, fit — same pattern as breast cancer
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

print(f"Accuracy: {round(acc * 100, 1)}%")
print(f"FN (predicted no default, actually defaulted): {fn}")
print(f"FP (predicted default, actually paid): {fp}")
```

**How the code works:**

- **`read_csv`** — features include limit balance, bill amounts, payment history; target is **default next month**.
- **`confusion_matrix`** — in a live run you may see **high accuracy** (e.g. ~80%) but **large FN** (many defaults missed). That is why the matrix matters more than a single percentage.
- **Positive class** — here "default" is usually coded as **1**; the class you care most about detecting is the **positive** label when discussing TP/FN with stakeholders.

### Quick Activity — Medical vs Banking Priority

1. Disease detection: Is a **false negative** or **false positive** usually worse for the patient?  
2. Credit default: The bank wants to catch defaulters early — should it **lower** or **raise** the default threshold?

**Answers:** 1 → **False negative** (missed disease). 2 → **Lower** threshold (more defaults flagged; more false alarms acceptable if missing a defaulter is costly).

---

## Key Takeaways

- **Classification** picks a **category**; **regression** predicts a **number** — Logistic Regression is for the former, despite its name.
- A **decision boundary** separates classes; **`fit`** learns it, **`predict`** applies it to new rows.
- The model outputs **probabilities** via the **sigmoid**; **`predict()`** applies the default **0.5 threshold** to get 0/1 labels.
- Changing the **threshold** trades **false positives** against **false negatives** — choose based on business cost (medical vs banking), not accuracy alone.
- The **confusion matrix** (TP, TN, FP, FN) explains *what kind* of mistakes happen; real datasets can show high accuracy with dangerous FN counts.
- Same **train–test split** and **Pipeline** discipline from regression applies: fit on train, evaluate on held-out test rows.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Classification** | Predict a category label | Use when output is pass/fail, spam/not spam, etc. |
| **Binary classification** | Exactly two classes | Default setting for Logistic Regression |
| **Multi-class classification** | Three or more classes | Same ideas later; not today's focus |
| **Decision boundary** | Line/plane/surface separating classes | Core visual for classification vs regression |
| **Logistic Regression** | Probability-based classifier using sigmoid | Foundational, interpretable first classifier |
| **Pipeline** | Chained steps (e.g. scale → classify) | Reuse from regression; avoids leakage |
| **`load_breast_cancer()`** | Built-in tumour dataset | Medical binary classification demo |
| **Sigmoid** | Maps raw score to probability in (0, 1) | Makes outputs valid probabilities |
| **Decision threshold** | Cut-off on P(class=1) (default 0.5) | Tunes FP vs FN trade-off |
| **Confusion matrix** | 2×2 table: TP, TN, FP, FN | Full picture of error types |
| **True Positive (TP)** | Predicted positive, was positive | Correct detection |
| **False Positive (FP)** | Predicted positive, was negative | False alarm |
| **False Negative (FN)** | Predicted negative, was positive | Missed case |
| **Accuracy** | (TP + TN) / total | Overall correctness; can mislead if classes imbalanced |
| **`LogisticRegression()`** | Create classifier | `sklearn.linear_model` |
| **`model.predict(X)`** | Class labels 0/1 | Final decision |
| **`model.predict_proba(X)`** | [P(class=0), P(class=1)] | Confidence; use `[:, 1]` for P(Pass) |
| **`confusion_matrix(y_true, y_pred)`** | Returns [[TN, FP], [FN, TP]] | `sklearn.metrics` |
| **`accuracy_score(y_true, y_pred)`** | Fraction correct | Quick summary — pair with confusion matrix |
