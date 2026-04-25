# Classification Models and Evaluation Metrics

---

## Context: Where We Came From and Where We Are Heading

In the previous session, we built our first classification model — **Logistic Regression** — and used it to predict whether a student would pass or fail based on study habits. We also built the **Confusion Matrix**, which broke every prediction into four buckets: True Positives, True Negatives, False Positives, and False Negatives. We ended that session realising that **accuracy alone can be deeply misleading**, especially when one class dominates the data.

**This session picks up exactly from that gap and fills it completely.** We will:

- Build two new and powerful classification models: **Decision Trees** and **Random Forest**
- Learn a full toolkit of evaluation metrics: **Precision, Recall, and F1 Score**
- Understand **ROC-AUC** — a metric that works across all thresholds at once
- Master **Threshold Tuning** to control what the model catches vs what it lets through

---

## Decision Trees: How a Model Can Think in Rules

Before we add new metrics, let's first expand our classifier toolbox. The first new model is the **Decision Tree** — arguably the most intuitive machine learning algorithm ever built, because it makes decisions the same way a human would: by asking a sequence of yes/no questions.

**Decision Tree:**
- **Official Definition:** A supervised machine learning model that predicts class labels by learning a tree-shaped sequence of if-else rules from the training data, splitting the data at each node based on the feature that best separates the classes.
- **In Simple Words:** The model looks at your data and learns a flowchart. It asks questions like "Is study_hours > 5.2?" — if yes, go left; if no, go right — and keeps narrowing down until it reaches a final answer.
- **Real-Life Example:** When a bank employee decides whether to approve a loan, they don't use a single formula — they ask questions: "Is income above ₹50,000?" → Yes → "Is credit score above 700?" → No → Reject. A Decision Tree learns exactly this kind of structured question logic from past data.

**Key vocabulary inside a Decision Tree:**

- **Root Node** — The very first question at the top of the tree. It is the single question that most powerfully divides the data into two groups, e.g., "Is study_hours > 5.2?"
- **Branch** — Each answer (Yes or No) leads to a branch — a path going left or right down the tree.
- **Internal Node** — Any question node that is not the root and not the final answer. It asks one more feature-based question to further refine the prediction.
- **Leaf Node** — The final node at the bottom of a branch. No more questions are asked here — the model delivers its class prediction: Pass or Fail.
- **Depth** — How many layers of questions the tree has. A tree of depth 1 asks one question; depth 3 asks up to three questions in sequence. Deeper trees can learn more complex rules but risk overfitting.

**How the tree decides which questions to ask:**

The Decision Tree tries every possible feature and every possible split value and picks the one that creates the **purest** groups — meaning one group has mostly Pass students and the other has mostly Fail students. This purity is measured using a score called **Gini Impurity** — a perfectly pure group (all Pass or all Fail) has Gini = 0, while a 50/50 split has the highest impurity. The tree keeps splitting until it reaches maximum depth or groups are pure enough.

**The overfitting risk with Decision Trees:**

- A tree with unlimited depth will ask so many specific questions that it perfectly memorises every training student — including noise and random quirks.
- On new test students, it will perform poorly because the rules it learned are too specific to the training set.
- The **`max_depth`** parameter is the primary tool for preventing this — it stops the tree from asking more questions than a set limit, forcing it to learn general patterns.

![Decision Tree Structure: Nodes, Branches, and Leaves](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/decision_tree_visualization.png)

---

**Complete Code: Training and Interpreting a Decision Tree**

**Dataset used:** 400 students, 3 features (`study_hours`, `sleep_hours`, `distractions`), binary target `pass_fail` (1 = Pass if exam score ≥ 70, 0 = Fail). Seed = 7, 80/20 train-test split with `random_state=7`.

**First 10 rows (rounded):**

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

```python
# Import numpy for data creation and numerical operations
import numpy as np

# Import DecisionTreeClassifier — the rule-based classification model
from sklearn.tree import DecisionTreeClassifier

# Import train_test_split to separate training and test data
from sklearn.model_selection import train_test_split

# Import accuracy_score to measure overall prediction correctness
from sklearn.metrics import accuracy_score

# Set seed for reproducibility
rng = np.random.default_rng(seed=7)

# Create 400 students with 3 features
n = 400
study_hours  = rng.uniform(1, 10, size=n)    # daily study hours (1 to 10)
sleep_hours  = rng.uniform(4, 9, size=n)     # daily sleep hours (4 to 9)
distractions = rng.uniform(0, 5, size=n)     # daily distraction hours (0 to 5)

# Simulate exam scores using the same formula as last session
scores = (
    40
    + 6.5 * study_hours         # study hours have the biggest positive effect
    + 1.2 * sleep_hours         # sleep has a moderate positive effect
    - 2.0 * distractions        # distractions reduce the score
    + rng.normal(0, 7, size=n)  # random noise for realism
)

# Create binary target: 1 = Pass (score >= 70), 0 = Fail
y = (scores >= 70).astype(int)

# Stack features into a 2D table (400 rows x 3 columns)
X = np.column_stack([study_hours, sleep_hours, distractions])

# Name the features — used for labelling outputs
feature_names = ["study_hours", "sleep_hours", "distractions"]

# Split: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=7
)

# Create a Decision Tree with maximum depth of 4
# max_depth=4 means the tree can ask at most 4 questions in sequence
# Without this limit, the tree would overfit by memorising every training student
tree = DecisionTreeClassifier(max_depth=4, random_state=42)

# Train the tree — it learns the best set of if-else rules from the training data
tree.fit(X_train, y_train)

# Predict class labels for test students
y_pred_tree = tree.predict(X_test)

# Predict probabilities for test students
y_prob_tree = tree.predict_proba(X_test)

# --- Display Feature Importances ---
# Feature importance tells us which features the tree relied on most for its splits
print("Decision Tree — Feature Importances:")
print("(Higher = this feature was used more often, for more impactful splits)")
for name, importance in zip(feature_names, tree.feature_importances_):
    bar = "█" * int(importance * 30)
    print(f"  {name:<15}: {round(importance, 3):>6}  {bar}")

# --- Show predictions for the first 8 test students ---
print("\nPredictions on 8 Test Students:")
print(f"{'#':<4} {'Study':>6} {'Sleep':>6} {'Dist':>5} {'Actual':>8} {'Pred':>8} {'P(Pass)':>9}")
print("-" * 55)
for i in range(8):
    study  = X_test[i][0]
    sleep  = X_test[i][1]
    dist   = X_test[i][2]
    actual = "Pass" if y_test[i] == 1 else "Fail"
    pred   = "Pass" if y_pred_tree[i] == 1 else "Fail"
    p_pass = y_prob_tree[i][1]
    print(f"{i+1:<4} {study:>6.1f} {sleep:>6.1f} {dist:>5.1f} {actual:>8} {pred:>8} {p_pass:>9.2f}")

# --- Print overall accuracy ---
acc_tree = accuracy_score(y_test, y_pred_tree)
print(f"\nDecision Tree Accuracy: {round(acc_tree * 100, 1)}%")
```

**How the code works:**

- **`DecisionTreeClassifier(max_depth=4, random_state=42)`** — Creates a Decision Tree limited to 4 levels of questions. The `random_state` ensures that when there are tie-breaking decisions during training, the same choice is made every run.
- **`tree.fit(X_train, y_train)`** — Trains the tree by examining the training data, trying all possible splits at each node, and selecting the one that creates the most pure groups using Gini Impurity.
- **`tree.feature_importances_`** — A NumPy array with one value per feature. Each value represents the fraction of the total impurity reduction that feature contributed across all splits. Values sum to 1.0 — a feature with importance 0.72 was responsible for 72% of the tree's splitting power.
- **`tree.predict(X_test)`** — Runs each test student through the learned tree: starts at the root, answers each question using the student's feature values, and follows branches until a leaf node is reached.
- **`tree.predict_proba(X_test)`** — At each leaf node, the tree stores the proportion of training students who passed vs failed. A leaf with 8 passes and 2 fails gives P(Pass) = 0.8 for any student who lands there.
- **The bar visualisation** — `"█" * int(importance * 30)` creates a simple visual bar proportional to each feature's importance, making the comparison instantly readable.

**What to observe in the output:**

- `study_hours` should have the highest feature importance — it had the strongest effect in the data formula.
- `sleep_hours` should show moderate importance.
- `distractions` may show lower importance depending on how the tree splits.
- A tree with `max_depth=4` may not achieve the highest possible accuracy, but it generalises better to new data than an unlimited-depth tree.

---

## Random Forest: When Many Trees Are Better Than One

A single Decision Tree, even with controlled depth, has a known weakness: it is sensitive to the specific training data it sees. Change a few students in the training set and the tree's structure can shift significantly — making individual trees somewhat fragile. The solution to this problem is **Random Forest**.

**Random Forest:**
- **Official Definition:** An ensemble learning algorithm that trains a large number of Decision Trees — each on a randomly sampled subset of the training data and a randomly sampled subset of features — and combines their predictions by majority vote (for classification) or averaging (for regression).
- **In Simple Words:** Instead of trusting one tree completely, Random Forest builds hundreds of trees, each learning from a slightly different version of the data. When predicting a new student, it asks all 100 trees and the majority answer wins.
- **Real-Life Example:** Imagine trying to pick the best cricket player. Instead of asking one expert, you ask 100 cricket analysts — each with slightly different knowledge and perspective. The consensus of 100 experts is far more reliable than any single opinion. That's exactly how Random Forest works.

**Why Random Forest is more accurate and stable than a single tree:**

- **Bagging (Bootstrap Aggregating)** — Each tree is trained on a different random sample of the training data, drawn with replacement. Some students appear multiple times in one tree's data and not at all in another's — this diversity prevents all trees from making the same mistake.
- **Random Feature Selection** — At each split in each tree, only a random subset of features is considered. This forces further diversity between trees so they don't all learn the same patterns.
- **Majority Voting** — For a final prediction, each tree casts a vote. If 80 trees say Pass and 20 say Fail, the prediction is Pass.

**The trade-off with Random Forest:**

- A single Decision Tree is very easy to visualise and explain — you can literally draw its flowchart.
- Random Forest with 100 trees cannot be visualised the same way — it is a **black box** model where reasoning is distributed across hundreds of trees.
- In return for this loss of direct interpretability, you gain substantially higher accuracy and robustness. In real projects, Random Forest is almost always the better choice unless explainability to non-technical stakeholders is a strict requirement.

![Random Forest: How Multiple Trees Vote Together](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/random_forest_ensemble.png)

---

**Complete Code: Training a Random Forest and Comparing with the Decision Tree**

```python
# Import RandomForestClassifier — the ensemble of many Decision Trees
from sklearn.ensemble import RandomForestClassifier

# Import accuracy_score (already imported above, included here for clarity)
from sklearn.metrics import accuracy_score

# (All data and train/test split from the Decision Tree section above are reused here)

# Create a Random Forest with 100 trees, each limited to depth 4
# n_estimators=100 means 100 trees will be trained and their votes combined
# max_depth=4 is applied to each individual tree to prevent overfitting
# random_state=42 ensures the same forest is built every run
rf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)

# Train the Random Forest on the same training data as the Decision Tree
# Internally: 100 trees are trained, each on a bootstrapped sample of the data
rf.fit(X_train, y_train)

# Predict class labels for test students — majority vote across 100 trees
y_pred_rf = rf.predict(X_test)

# Predict probabilities — average of P(Pass) across all 100 trees
y_prob_rf = rf.predict_proba(X_test)[:, 1]

# --- Feature Importances from Random Forest ---
# These are averaged across all 100 trees — much more stable than a single tree
print("Random Forest — Feature Importances (averaged across 100 trees):")
for name, importance in zip(feature_names, rf.feature_importances_):
    bar = "█" * int(importance * 30)
    print(f"  {name:<15}: {round(importance, 3):>6}  {bar}")

# --- Side-by-side accuracy comparison ---
acc_tree = accuracy_score(y_test, y_pred_tree)
acc_rf   = accuracy_score(y_test, y_pred_rf)

print(f"\nAccuracy Comparison:")
print(f"  Decision Tree (max_depth=4)        : {round(acc_tree * 100, 1)}%")
print(f"  Random Forest (100 trees, depth=4) : {round(acc_rf * 100, 1)}%")

if acc_rf > acc_tree:
    print(f"  → Random Forest is better by {round((acc_rf - acc_tree) * 100, 1)} percentage points")
else:
    print(f"  → Both models perform similarly on this dataset")

# --- Show predictions for the first 8 test students (both models side by side) ---
print("\nSide-by-Side Predictions (8 Test Students):")
print(f"{'#':<4} {'Study':>6} {'Actual':>8} {'Tree Pred':>10} {'RF Pred':>10} {'RF P(Pass)':>11}")
print("-" * 55)
for i in range(8):
    study  = X_test[i][0]
    actual = "Pass" if y_test[i] == 1 else "Fail"
    tree_p = "Pass" if y_pred_tree[i] == 1 else "Fail"
    rf_p   = "Pass" if y_pred_rf[i] == 1 else "Fail"
    p_pass = y_prob_rf[i]
    print(f"{i+1:<4} {study:>6.1f} {actual:>8} {tree_p:>10} {rf_p:>10} {p_pass:>11.2f}")
```

**How the code works:**

- **`RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)`** — Creates a forest of 100 individual Decision Trees. `n_estimators` controls how many trees are trained — more trees means higher accuracy and stability, but longer training time.
- **`rf.fit(X_train, y_train)`** — Trains all 100 trees simultaneously. Each tree sees a randomly sampled subset of training students (with replacement) and at each node considers only a random subset of features. This diversity is the source of the forest's strength.
- **`rf.predict(X_test)`** — For each test student, all 100 trees cast a vote. The majority class wins. This collective voting is far more stable than a single tree's decision.
- **`rf.predict_proba(X_test)[:, 1]`** — Returns the average P(Pass) across all 100 trees for each test student. Averaging probabilities from 100 trees produces smoother, more reliable confidence scores than a single tree.
- **`rf.feature_importances_`** — Averaged feature importances across all 100 trees. Because this is an average across many trees with different random splits, it is a much more stable and trustworthy indicator of feature relevance than a single tree's importances.

---

## Evaluation Metrics: Going Beyond Accuracy

Now that we have three classifiers — Logistic Regression (from last session), Decision Tree, and Random Forest — we need better tools to compare them properly. Accuracy is the starting point, but it often tells an incomplete and even misleading story. We need **Precision**, **Recall**, and **F1 Score**.

**Why accuracy alone is not enough:**

- Consider a school where 90% of students pass. A model that always predicts "Pass" achieves 90% accuracy — but it never correctly identifies a single failing student.
- It has 0% usefulness for the actual task of catching students at risk, yet accuracy says it is doing great.
- Precision, Recall, and F1 Score are designed to catch exactly this kind of misleading model.

---

### Precision: Of Everything We Called Positive, How Many Were Actually Positive?

**Precision:**
- **Official Definition:** The fraction of all data points predicted as the positive class that were truly positive. Formula: `Precision = TP / (TP + FP)`.
- **In Simple Words:** Of all the students the model said "Pass" — what fraction genuinely passed? If the model said "Pass" 80 times and 72 of those students really did pass, Precision = 72/80 = 90%.
- **Real-Life Example:** A search engine returns 20 results for your query. 16 are genuinely relevant. Precision = 16/20 = 80%. It measures: "Of everything I gave you, how much was actually useful?"

**What Precision tells you:**

- **High precision** = When the model says "Yes" (positive), it is usually right. The false positive rate is low.
- **Low precision** = The model is triggering too many false alarms — it calls too many things positive when they're actually negative.
- Precision matters most when **false positives are costly** — e.g., falsely approving loans for people who will default, or sending unnecessary aggressive treatment to healthy patients.

---

### Recall: Of Everything That Was Actually Positive, How Many Did We Catch?

**Recall:**
- **Official Definition:** The fraction of all truly positive data points that were correctly predicted as positive by the model. Formula: `Recall = TP / (TP + FN)`.
- **In Simple Words:** Of all the students who genuinely passed, what fraction did the model correctly identify? If 100 students actually passed and the model caught 85 of them, Recall = 85%. The other 15 were missed (False Negatives).
- **Real-Life Example:** A security camera system detects 90 out of 100 actual intruders. Recall = 90%. The other 10 slipped through undetected. Recall measures: "Of all the real events that happened, how many did I catch?"

**What Recall tells you:**

- **High recall** = The model is very good at catching real positives. The false negative rate is low.
- **Low recall** = The model is missing too many real positives — genuine cases are going undetected.
- Recall matters most when **false negatives are costly** — e.g., a disease screening test that misses sick patients, or a fraud detection system that misses fraudulent transactions.

---

### The Precision-Recall Trade-off

Precision and Recall are in constant tension with each other. If you make the model more generous (lower threshold → predicts positive more often), Recall goes up but Precision goes down. If you make the model more strict (higher threshold → predicts positive less often), Precision goes up but Recall goes down.

- **You cannot maximise both simultaneously** — there is always a trade-off.
- The right balance depends on your use case: medical diagnostics prioritise Recall; spam filtering prioritises Precision.

---

### F1 Score: The Balanced Compromise Between Precision and Recall

**F1 Score:**
- **Official Definition:** The harmonic mean of Precision and Recall, providing a single metric that balances both. Formula: `F1 = 2 × (Precision × Recall) / (Precision + Recall)`.
- **In Simple Words:** F1 takes the middle ground between Precision and Recall. If your model has perfect Precision (1.0) but terrible Recall (0.1), the F1 score will be low — penalising the extreme imbalance. A high F1 means both Precision and Recall are reasonably high at the same time.
- **Real-Life Example:** A student who scores 100% in written exams but 10% in practicals has a terrible combined score — one perfect result doesn't compensate for the failure elsewhere. F1 Score works the same way: both Precision and Recall must be decent for F1 to be good.

**Why use harmonic mean instead of simple average?**

- Simple average of Precision=1.0 and Recall=0.1 would be 0.55 — misleadingly high.
- Harmonic mean of 1.0 and 0.1 is 0.18 — more accurately reflecting the poor balance.
- The harmonic mean is always lower than the arithmetic mean and is especially sensitive to very low values in either metric — exactly what we want.

---

**Complete Code: Computing Precision, Recall, F1 Score, and Comparing All Models**

```python
# Import precision, recall, and F1 score functions from scikit-learn
from sklearn.metrics import precision_score, recall_score, f1_score

# Import confusion_matrix to see the full breakdown of predictions
from sklearn.metrics import confusion_matrix

# Import classification_report for a clean formatted summary
from sklearn.metrics import classification_report

# We also need Logistic Regression for comparison — re-train it here
from sklearn.linear_model import LogisticRegression

# Train Logistic Regression on the same training data as before
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# --- Evaluate all three models using a helper function ---
def evaluate_classifier(name, y_true, y_pred):
    """Compute and print all four key classification metrics."""
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()    # unpack the 2x2 matrix into four values

    acc       = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall    = recall_score(y_true, y_pred, zero_division=0)
    f1        = f1_score(y_true, y_pred, zero_division=0)

    print(f"\n{'='*50}")
    print(f"  {name}")
    print(f"{'='*50}")
    print(f"  Confusion Matrix:  TN={tn}  FP={fp}  FN={fn}  TP={tp}")
    print(f"  Accuracy  : {round(acc * 100, 1):>6}%")
    print(f"  Precision : {round(precision, 3):>6}  → Of all predicted Pass, {round(precision*100,1)}% were actually Pass")
    print(f"  Recall    : {round(recall, 3):>6}  → Of all actual Pass, {round(recall*100,1)}% were correctly identified")
    print(f"  F1 Score  : {round(f1, 3):>6}  → Balanced trade-off between Precision and Recall")

    return {"model": name, "Accuracy": round(acc,3), "Precision": round(precision,3),
            "Recall": round(recall,3), "F1": round(f1,3)}

# Run evaluation for all three models
results = []
results.append(evaluate_classifier("Logistic Regression", y_test, y_pred_lr))
results.append(evaluate_classifier("Decision Tree (depth=4)", y_test, y_pred_tree))
results.append(evaluate_classifier("Random Forest (100 trees)", y_test, y_pred_rf))

# --- Print a clean summary comparison table ---
print(f"\n\n{'Summary Comparison':^55}")
print(f"{'Model':<28} {'Acc':>6} {'Prec':>6} {'Rec':>6} {'F1':>6}")
print("-" * 55)
for r in results:
    print(f"{r['model']:<28} {r['Accuracy']:>6} {r['Precision']:>6} {r['Recall']:>6} {r['F1']:>6}")

# --- Show sklearn's built-in classification report for the best model ---
print("\n\nsklearn Classification Report — Random Forest:")
print(classification_report(y_test, y_pred_rf, target_names=["Fail (0)", "Pass (1)"]))
```

**How the code works:**

- **`precision_score(y_true, y_pred, zero_division=0)`** — Computes TP / (TP + FP). The `zero_division=0` argument handles edge cases where no positive predictions are made at all, returning 0.0 instead of crashing.
- **`recall_score(y_true, y_pred, zero_division=0)`** — Computes TP / (TP + FN). The same zero_division protection applies.
- **`f1_score(y_true, y_pred, zero_division=0)`** — Computes `2 × Precision × Recall / (Precision + Recall)`. If both are zero, it safely returns 0.0.
- **`cm.ravel()`** — Flattens the 2×2 confusion matrix into a single array `[TN, FP, FN, TP]` in that fixed order. This is a clean shortcut to extract all four cells without using `cm[0][0]`, `cm[0][1]` etc. individually.
- **`evaluate_classifier()` function** — A reusable helper that wraps the full evaluation workflow. Defining it once and calling it for each model avoids repetition and ensures all models are evaluated identically.
- **`classification_report()`** — Produces a formatted table showing Precision, Recall, and F1 for each class separately, plus a weighted average. The `target_names` argument replaces default "0" and "1" labels with readable names.

**Reading the classification_report output:**

The report shows metrics for both classes — Fail (0) and Pass (1). A model could be excellent at predicting Pass but poor at predicting Fail. The report breaks it down class by class, and the "support" column shows how many actual students belonged to each class in the test set.

---

## ROC-AUC: Measuring How Well the Model Separates the Two Classes

Precision, Recall, and F1 are all computed at a **specific threshold** (usually 0.5). But a model's probability scores carry information that a single threshold cannot fully capture. **ROC-AUC** evaluates the model across all possible thresholds at once — giving you a completely threshold-independent view of model quality.

**ROC Curve:**
- **Official Definition:** The Receiver Operating Characteristic curve is a plot of the **True Positive Rate (Recall)** on the y-axis against the **False Positive Rate** on the x-axis, computed at every possible decision threshold from 0 to 1.
- **In Simple Words:** Imagine slowly lowering the decision threshold from 1.0 (predict almost no one as Pass) down to 0.0 (predict everyone as Pass). At each threshold, you compute: how many real passes did we catch (TPR)? and how many false alarms did we create (FPR)? The ROC curve draws a line through all these points.
- **Real-Life Example:** A quality inspector at a factory adjusts their strictness from "flag only obviously defective items" to "flag anything that looks slightly off." As they become less strict, they catch more real defects (higher recall) but also flag more good items (more false alarms). The ROC curve plots this exact trade-off at every possible strictness level.

**AUC — Area Under the Curve:**
- **Official Definition:** The numerical area under the ROC curve, ranging from 0.0 to 1.0. It represents the probability that the model will rank a randomly chosen positive example higher than a randomly chosen negative example.
- **In Simple Words:** AUC tells you: if you pick one random Pass student and one random Fail student, what is the probability that the model assigned a higher probability to the Pass student? AUC = 0.95 means it gets this ranking right 95% of the time.
- **Real-Life Example:** A hospital has 50 sick patients and 50 healthy patients. AUC = 0.90 means that if you randomly pick one sick and one healthy patient, 90% of the time the model will rank the sick patient as "more likely to be sick" — even before you pick any specific threshold.

**Interpreting AUC values:**

| AUC Value | What It Means |
|---|---|
| 1.00 | Perfect model — ranks all positives above all negatives |
| 0.90 – 0.99 | Excellent separation |
| 0.80 – 0.89 | Good — model has strong ranking ability |
| 0.70 – 0.79 | Fair — some useful signal |
| 0.60 – 0.69 | Poor — barely better than random |
| 0.50 | Random model — no better than a coin flip |
| Below 0.50 | Worse than random — the model is predicting backwards |

**Why AUC is better than accuracy for imbalanced data:**

- AUC is computed from probabilities and ranks — it doesn't depend on any specific threshold. This makes it immune to the class imbalance problem.
- A model that always predicts "Pass" achieves high accuracy on imbalanced data but has an AUC of exactly 0.5 — clearly revealing it has no real predictive power.

![ROC Curve: TPR vs FPR at All Thresholds](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/roc_auc_curve.png)

---

**Complete Code: Computing ROC Curve and AUC for All Three Models**

```python
# Import roc_auc_score to compute the AUC metric directly from probabilities
from sklearn.metrics import roc_auc_score

# Import roc_curve to get the data points needed to draw the ROC curve
from sklearn.metrics import roc_curve

# Import matplotlib for plotting the ROC curve
import matplotlib.pyplot as plt

# --- Get probability outputs from all three models ---
# We need P(Pass) — the positive class probability — for each model
y_prob_lr   = lr.predict_proba(X_test)[:, 1]          # Logistic Regression
y_prob_tree = tree.predict_proba(X_test)[:, 1]        # Decision Tree
y_prob_rf   = rf.predict_proba(X_test)[:, 1]          # Random Forest

# --- Compute AUC score for each model ---
auc_lr   = roc_auc_score(y_test, y_prob_lr)
auc_tree = roc_auc_score(y_test, y_prob_tree)
auc_rf   = roc_auc_score(y_test, y_prob_rf)

print("AUC Scores (higher is better; 1.0 = perfect, 0.5 = random):")
print(f"  Logistic Regression            : {round(auc_lr, 4)}")
print(f"  Decision Tree (depth=4)        : {round(auc_tree, 4)}")
print(f"  Random Forest (100 trees)      : {round(auc_rf, 4)}")

# --- Compute ROC curve data points for each model ---
# roc_curve returns three arrays: FPR values, TPR values, and the threshold at each point
fpr_lr,   tpr_lr,   _ = roc_curve(y_test, y_prob_lr)
fpr_tree, tpr_tree, _ = roc_curve(y_test, y_prob_tree)
fpr_rf,   tpr_rf,   _ = roc_curve(y_test, y_prob_rf)

# --- Plot all three ROC curves on one chart ---
plt.figure(figsize=(8, 6))

# Plot the ROC curve for each model with its AUC in the legend
plt.plot(fpr_lr,   tpr_lr,   label=f"Logistic Regression  (AUC = {round(auc_lr, 3)})")
plt.plot(fpr_tree, tpr_tree, label=f"Decision Tree        (AUC = {round(auc_tree, 3)})")
plt.plot(fpr_rf,   tpr_rf,   label=f"Random Forest        (AUC = {round(auc_rf, 3)})")

# Draw the diagonal baseline — this is a random classifier with AUC = 0.5
plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random Classifier (AUC = 0.5)")

# Label the axes
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate / Recall (TPR)")
plt.title("ROC Curves — Comparing All Three Models")
plt.legend()
plt.tight_layout()
plt.show()

# --- Print a combined summary: all metrics for all models ---
print("\nFull Metric Summary:")
print(f"{'Model':<30} {'Accuracy':>9} {'Precision':>10} {'Recall':>8} {'F1':>8} {'AUC':>8}")
print("-" * 78)

all_models = [
    ("Logistic Regression",       y_pred_lr,   auc_lr),
    ("Decision Tree (depth=4)",   y_pred_tree, auc_tree),
    ("Random Forest (100 trees)", y_pred_rf,   auc_rf),
]
for model_name, y_pred, auc in all_models:
    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec  = recall_score(y_test, y_pred, zero_division=0)
    f1   = f1_score(y_test, y_pred, zero_division=0)
    print(f"{model_name:<30} {round(acc,3):>9} {round(prec,3):>10} {round(rec,3):>8} {round(f1,3):>8} {round(auc,3):>8}")
```

**How the code works:**

- **`roc_auc_score(y_test, y_prob)`** — Computes the AUC directly from actual labels and the model's probability scores. It uses raw probabilities — not class labels — so it is completely threshold-independent.
- **`roc_curve(y_test, y_prob)`** — Returns three arrays: `fpr` (False Positive Rates), `tpr` (True Positive Rates / Recall), and `thresholds`. Each triplet `(fpr[i], tpr[i], thresholds[i])` represents one point on the ROC curve.
- **`plt.plot(fpr, tpr, label=...)`** — Draws one model's ROC curve by connecting all its (FPR, TPR) points. A curve that hugs the top-left corner (high TPR with low FPR) has high AUC and is an excellent model.
- **The diagonal line** — `plt.plot([0, 1], [0, 1])` draws the baseline random classifier line. Any model whose ROC curve is below this line is worse than random — something is fundamentally wrong (likely the classes are inverted).
- **The combined summary table** — Brings together Accuracy, Precision, Recall, F1, and AUC in one place. This is the standard comparison table a data scientist produces before selecting the final model.

---

## Threshold Tuning: Finding the Right Cut-off for Your Use Case

All the metrics above were computed at the default threshold of 0.5 — but this is not always the best choice. **Threshold Tuning** is the process of systematically finding the probability cut-off that meets a specific business requirement, rather than blindly using the default.

**Threshold Tuning:**
- **Official Definition:** Adjusting the probability cut-off to achieve a desired Precision-Recall balance, or to maximise a target metric like F1 Score.
- **In Simple Words:** The model gives you probabilities. The threshold is a dial you turn. Ask: "What threshold gives the best F1?" or "What threshold ensures Recall ≥ 90%?" — then use the data to find the exact answer.
- **Real-Life Example:** A bank risk team says "we cannot miss more than 10% of defaulters." The data scientist uses `precision_recall_curve` to find the exact threshold that achieves Recall ≥ 0.90 for the Fail class — even if Precision drops slightly in exchange.

![Precision-Recall Trade-off Curve at Different Thresholds](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/precision_recall_tradeoff.png)

---

**Complete Code: Finding the Best Threshold Using Precision-Recall Curve**

```python
# Import precision_recall_curve to compute Precision and Recall at every threshold
from sklearn.metrics import precision_recall_curve

# y_prob_rf already contains P(Pass) for all test students (from the RF model above)

# Compute Precision and Recall at every possible threshold
# precisions[i] and recalls[i] = metrics if thresholds[i] is used as the cut-off
# Note: precisions and recalls have one extra entry — use [:-1] to align with thresholds
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob_rf)

# Compute F1 at every threshold to find the best balance point
# 1e-9 in the denominator prevents division by zero at extreme thresholds
f1_scores = (
    2 * precisions[:-1] * recalls[:-1]
    / (precisions[:-1] + recalls[:-1] + 1e-9)
)

# Find the threshold index where F1 is highest
best_idx       = f1_scores.argmax()
best_threshold = thresholds[best_idx]

print("Best Threshold (Maximises F1 Score):")
print(f"  Threshold : {round(best_threshold, 3)}")
print(f"  Precision : {round(precisions[best_idx], 3)}")
print(f"  Recall    : {round(recalls[best_idx], 3)}")
print(f"  F1 Score  : {round(f1_scores[best_idx], 3)}")

# --- Compare default (0.5) vs best threshold side by side ---
y_pred_default   = (y_prob_rf >= 0.5).astype(int)            # standard cut-off
y_pred_optimised = (y_prob_rf >= best_threshold).astype(int) # data-driven cut-off

print("\nDefault (0.5) vs Optimised Threshold:")
print(f"{'Metric':<12} {'Default':>10} {'Optimised':>12}")
print("-" * 36)
for label, fn in [("Precision", precision_score), ("Recall", recall_score), ("F1 Score", f1_score)]:
    d = fn(y_test, y_pred_default,   zero_division=0)
    o = fn(y_test, y_pred_optimised, zero_division=0)
    print(f"{label:<12} {round(d, 3):>10} {round(o, 3):>12}")
```

**How the code works:**

- **`precision_recall_curve(y_test, y_prob_rf)`** — Tests every unique probability score in `y_prob_rf` as a candidate threshold, returning the resulting Precision and Recall at each point. The arrays have one extra entry at the end; `[:-1]` aligns them with the `thresholds` array.
- **`f1_scores.argmax()`** — Returns the index where F1 is highest. The threshold at that index is the mathematically optimal cut-off for balancing Precision and Recall.
- **`(y_prob_rf >= best_threshold).astype(int)`** — Applies the custom threshold manually. Any student with P(Pass) at or above the threshold is predicted as Pass (1); others as Fail (0).
- **The comparison print** — Shows the concrete improvement (or trade-off) from switching away from 0.5. In most real datasets, the optimised threshold produces a noticeably higher F1 than the default.

---

## Key Takeaways

- **Decision Trees** make predictions by learning a flowchart of if-else rules; `max_depth` is the most important parameter to control overfitting.
- **Random Forest** solves the fragility of a single tree by training hundreds of trees on random subsets of data and features, then combining their votes — giving you higher accuracy and stability at the cost of interpretability.
- **Precision** and **Recall** expose what accuracy hides: how many false alarms is the model raising, and how many real positives is it missing? The right balance between them depends entirely on the business cost of each type of error.
- **F1 Score** combines Precision and Recall into one balanced number; **ROC-AUC** goes further by measuring model quality across every possible threshold at once.
- **Threshold Tuning** is the final dial: once you have a good model, you can adjust the probability cut-off to meet specific business requirements — maximising F1, enforcing minimum recall, or reducing false alarms. In coming sessions, we will apply these same evaluation tools to regression problems and explore how model selection works at scale.

---

## Quick Reference: Important Terms, Tools, and Python Commands

| Term / Tool | What It Means | Why It Matters |
|---|---|---|
| **Decision Tree** | Rule-based model that predicts by asking a sequence of if-else questions | Highly interpretable; can be visualised as a flowchart |
| **Root Node** | The first question at the top of the Decision Tree | Splits the data using the most powerful single feature |
| **Leaf Node** | Final decision node at the bottom of a branch | Where the model delivers its class prediction |
| **max_depth** | Maximum number of question layers allowed in the tree | Controls overfitting; lower depth = simpler, more generalised tree |
| **Gini Impurity** | Score measuring how mixed (impure) a group is after a split | Tree uses this to select the best question at each node |
| **feature_importances_** | Array of how much each feature contributed to all splits | Tells you which features the model relied on most |
| **Random Forest** | Ensemble of many Decision Trees trained on random data/feature subsets | More accurate and stable than a single tree |
| **Bagging** | Training each tree on a bootstrapped (random with replacement) sample | Creates diversity between trees, reducing overfitting |
| **n_estimators** | Number of trees in the Random Forest | More trees = more stable predictions; increases training time |
| **Majority Voting** | Final Random Forest prediction = class most trees agreed on | Collective wisdom of many trees beats any single tree |
| **Precision** | TP / (TP + FP) — of predicted positives, how many were actually positive | High precision = few false alarms |
| **Recall** | TP / (TP + FN) — of actual positives, how many were correctly caught | High recall = few missed detections |
| **F1 Score** | Harmonic mean of Precision and Recall | Balanced single metric when both P and R matter |
| **Precision-Recall Trade-off** | Lowering threshold increases Recall but decreases Precision, and vice versa | Core tension in all threshold decisions |
| **ROC Curve** | Plot of TPR (Recall) vs FPR at every possible threshold | Visual tool showing model performance across all thresholds |
| **AUC** | Area under the ROC curve; 0.5 = random, 1.0 = perfect | Threshold-independent measure of model ranking ability |
| **Precision-Recall Curve** | Plot of Precision vs Recall at every possible threshold | Better than ROC for imbalanced datasets |
| **Threshold Tuning** | Choosing the optimal probability cut-off for a specific business need | Converts probability scores into the most useful class labels |
| **`DecisionTreeClassifier(max_depth=n)`** | Creates a Decision Tree with limited depth | Import from `sklearn.tree` |
| **`RandomForestClassifier(n_estimators=n)`** | Creates a Random Forest with n trees | Import from `sklearn.ensemble` |
| **`precision_score(y_true, y_pred)`** | Computes Precision from actual labels and predictions | Import from `sklearn.metrics` |
| **`recall_score(y_true, y_pred)`** | Computes Recall from actual labels and predictions | Import from `sklearn.metrics` |
| **`f1_score(y_true, y_pred)`** | Computes F1 Score from actual labels and predictions | Import from `sklearn.metrics` |
| **`classification_report(y_true, y_pred)`** | Prints Precision, Recall, F1 for every class | Import from `sklearn.metrics`; standard model summary |
| **`roc_auc_score(y_true, y_prob)`** | Computes AUC from actual labels and probability scores | Import from `sklearn.metrics`; uses probabilities, not labels |
| **`roc_curve(y_true, y_prob)`** | Returns FPR, TPR, thresholds arrays for plotting ROC | Import from `sklearn.metrics` |
| **`precision_recall_curve(y_true, y_prob)`** | Returns Precisions, Recalls, Thresholds arrays | Import from `sklearn.metrics`; use for threshold tuning |
| **`cm.ravel()`** | Flattens confusion matrix into `[TN, FP, FN, TP]` | Quick one-line extraction of all four confusion matrix values |
| **`(y_prob >= threshold).astype(int)`** | Applies a custom threshold to probability outputs | Standard approach to threshold tuning |

---
