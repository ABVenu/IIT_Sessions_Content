# Classification Models and Evaluation Metrics

## Context of This Session

In the previous session, you built **Logistic Regression**, read **probabilities** and **class labels**, and used a **confusion matrix** to see TP, TN, FP, and FN. You also saw why **accuracy alone** can mislead when classes are imbalanced (e.g. a model that always predicts Pass).

This session adds **two tree-based classifiers** and a practical **evaluation toolkit** so you can compare models fairly on real problems.

**In this session, you will:**

- Learn **Decision Trees** as rule-based models (if-else paths)
- Learn **Random Forest** as many trees voting together
- Go beyond accuracy with **precision** and **recall**
- Use **F1** and **ROC-AUC** to compare how well models separate Pass from Fail

---

## Decision Trees: Rules You Can Follow Like a Flowchart

**Decision Tree:**

- **Official Definition:** A supervised model that predicts a class by learning a **tree** of if-else splits on features.
- **In Simple Words:** The model asks questions: "Is `study_hours` > 5.2?" → Yes goes left, No goes right — until it reaches Pass or Fail.
- **Real-Life Example:** A bank officer approves loans by questions (income? credit score?) — not one formula. A Decision Tree learns that pattern from past data.

**Parts of a tree (quick map):**

| Part | Role |
|---|---|
| **Root node** | First question at the top |
| **Branch** | Path after Yes/No |
| **Internal node** | Another question mid-tree |
| **Leaf node** | Final prediction (Pass/Fail) |
| **Depth** | How many question layers — deeper can overfit |

**How splits are chosen:** At each node, the tree tries feature splits and picks the one that makes child groups **purest** (mostly one class). **Gini impurity** scores purity — 0 means one class only; 0.5 means 50/50 mix.

**Overfitting:** A very deep tree can **memorise** training rows and fail on new students. **`max_depth`** limits how many questions are allowed — a key knob for generalisation.

![Decision Tree Structure: Nodes, Branches, and Leaves](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/decision_tree_visualization.png)

### Quick Activity — Trace a Path

Features: `study_hours = 6`, `distractions = 2`. Tree rules: (1) If `study_hours` ≤ 4 → Fail; else (2) If `distractions` > 3 → Fail; else → Pass.

What is the prediction?

**Answer:** Pass (6 > 4, and 2 is not > 3).

---

## Random Forest: Many Trees, One Vote

A single tree can change a lot if you shuffle training data. **Random Forest** fixes that by training **many** trees and voting.

**Random Forest:**

- **Official Definition:** An **ensemble** of Decision Trees, each on a random sample of rows and random subset of features; classification prediction is **majority vote**.
- **In Simple Words:** 100 trees each give Pass or Fail — the label with the most votes wins.
- **Real-Life Example:** You ask 100 cricket experts instead of one — the crowd answer is usually more stable.

**Why it often beats one tree:**

- **Bagging** — each tree sees a different bootstrap sample of students
- **Random features at splits** — trees do not all copy the same rule
- **Majority vote** — one wrong tree matters less

**Trade-off:** One tree is easy to draw and explain; a forest is harder to explain but usually **more accurate and stable**.

![Random Forest: How Multiple Trees Vote Together](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/random_forest_ensemble.png)

---

## Complete Code: Data, Decision Tree, and Random Forest

**Setup:** 400 students, features `study_hours`, `sleep_hours`, `distractions`; target `pass_fail` (1 = Pass if exam score ≥ 70). Seed = 7, 80/20 train–test split.

```python
import numpy as np  # arrays and random data
from sklearn.tree import DecisionTreeClassifier  # single decision tree model
from sklearn.ensemble import RandomForestClassifier  # many trees voting together
from sklearn.model_selection import train_test_split  # split data into train and test
from sklearn.metrics import accuracy_score  # percent of correct predictions

rng = np.random.default_rng(seed=7)  # fixed seed so results repeat
n = 400  # number of student rows
study_hours  = rng.uniform(1, 10, size=n)  # feature 1: hours studied per day
sleep_hours  = rng.uniform(4, 9, size=n)  # feature 2: sleep hours per night
distractions = rng.uniform(0, 5, size=n)  # feature 3: distraction level

scores = (  # fake exam score from features plus small noise
    40 + 6.5 * study_hours + 1.2 * sleep_hours
    - 2.0 * distractions + rng.normal(0, 7, size=n)
)
y = (scores >= 70).astype(int)  # 1 = Pass, 0 = Fail
X = np.column_stack([study_hours, sleep_hours, distractions])  # feature matrix
feature_names = ["study_hours", "sleep_hours", "distractions"]  # labels for printing

X_train, X_test, y_train, y_test = train_test_split(  # 80% train, 20% test
    X, y, test_size=0.2, random_state=7
)

tree = DecisionTreeClassifier(max_depth=4, random_state=42)  # tree with depth cap
tree.fit(X_train, y_train)  # learn rules from training rows only
y_pred_tree = tree.predict(X_test)  # hard labels Pass/Fail on test set
y_prob_tree = tree.predict_proba(X_test)[:, 1]  # P(Pass) for each test row

rf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)  # 100 trees
rf.fit(X_train, y_train)  # fit forest on same training split
y_pred_rf = rf.predict(X_test)  # majority-vote labels on test set
y_prob_rf = rf.predict_proba(X_test)[:, 1]  # P(Pass) from forest for ROC later

print("Decision Tree — feature importances:")  # which features the tree used most
for name, imp in zip(feature_names, tree.feature_importances_):
    print(f"  {name}: {round(imp, 3)}")  # print one feature per line

print("\nRandom Forest — feature importances:")  # averaged importance across trees
for name, imp in zip(feature_names, rf.feature_importances_):
    print(f"  {name}: {round(imp, 3)}")

acc_tree = accuracy_score(y_test, y_pred_tree)  # tree accuracy on held-out test
acc_rf   = accuracy_score(y_test, y_pred_rf)  # forest accuracy on same test set
print(f"\nAccuracy — Tree: {round(acc_tree*100, 1)}%  |  RF: {round(acc_rf*100, 1)}%")
```

**How the code works:**

- **`max_depth=4`** — caps tree depth so rules stay general, not memorised noise.
- **`tree.fit` / `rf.fit`** — learn rules from **train** only; never tune on test.
- **`feature_importances_`** — higher value = feature used more in useful splits (RF averages across trees).
- **`predict_proba(X_test)[:, 1]`** — **P(Pass)** per student; needed for ROC-AUC.
- **`n_estimators=100`** — number of trees in the forest; more trees → stabler votes, slower training.

**What to notice:** `study_hours` should rank highest (it drives the score formula). Random Forest accuracy is often equal or slightly better than a single tree on the same split.

---

## Evaluation Metrics: Precision and Recall First

You now have **Logistic Regression** (from the previous session), a **Decision Tree**, and a **Random Forest**. Accuracy is a start, but two metrics answer sharper questions.

**Precision:**

- **Official Definition:** `TP / (TP + FP)` — of all **predicted Pass**, how many truly passed?
- **In Simple Words:** When the model says Pass, how often is it right?
- **Real-Life Example:** 20 search results, 16 useful → precision 16/20. Matters when **false alarms** are costly (spam filter, unnecessary alerts).

**Recall:**

- **Official Definition:** `TP / (TP + FN)` — of all **actual Pass**, how many did we catch?
- **In Simple Words:** Of real passes, what fraction did the model find?
- **Real-Life Example:** Security catches 90 of 100 intruders → recall 90%. Matters when **missed cases** are costly (fraud, disease screening).

**The trade-off (one line):** A **lower** probability threshold → more Pass predictions → **higher recall**, **lower precision**. A **higher** threshold does the opposite. You cannot maximise both at once; the business picks the balance.

```python
from sklearn.linear_model import LogisticRegression  # baseline model from previous topic
from sklearn.metrics import (  # metric functions for evaluation
    precision_score, recall_score, f1_score,
    confusion_matrix, accuracy_score, classification_report
)

lr = LogisticRegression()  # create logistic regression model
lr.fit(X_train, y_train)  # train on same split as trees (uses X_train, y_train above)
y_pred_lr = lr.predict(X_test)  # Pass/Fail labels on test set

def show_metrics(name, y_true, y_pred):  # helper to print one model's results
    cm = confusion_matrix(y_true, y_pred)  # 2x2 table of actual vs predicted
    tn, fp, fn, tp = cm.ravel()  # flatten to TN, FP, FN, TP counts
    print(f"\n{name}")  # model name as heading
    print(f"  TN={tn} FP={fp} FN={fn} TP={tp}")  # show all four counts
    print(f"  Accuracy  : {round(accuracy_score(y_true, y_pred)*100, 1)}%")  # overall correct %
    print(f"  Precision : {round(precision_score(y_true, y_pred, zero_division=0), 3)}")  # TP/(TP+FP)
    print(f"  Recall    : {round(recall_score(y_true, y_pred, zero_division=0), 3)}")  # TP/(TP+FN)
    print(f"  F1        : {round(f1_score(y_true, y_pred, zero_division=0), 3)}")  # balance of P and R

show_metrics("Logistic Regression", y_test, y_pred_lr)  # metrics for LR
show_metrics("Decision Tree", y_test, y_pred_tree)  # metrics for tree (from earlier code)
show_metrics("Random Forest", y_test, y_pred_rf)  # metrics for forest

print("\nClassification report — Random Forest:")  # sklearn summary table per class
print(classification_report(y_test, y_pred_rf, target_names=["Fail", "Pass"]))
```

**How the code works:**

- **`cm.ravel()`** — flattens matrix to `[TN, FP, FN, TP]` for quick counts.
- **`precision_score` / `recall_score`** — need **class labels** (`predict`), not probabilities.
- **`zero_division=0`** — safe when the model never predicts Pass (avoids crash).
- **`classification_report`** — sklearn table per class; check both Fail and Pass rows.

### Quick Activity — Which Metric Matters?

| Scenario | Care more about |
|---|---|
| Spam filter (users hate false spam flags) | **Precision** |
| Cancer screening (missing sick patients is dangerous) | **Recall** |
| Balanced report for management | **F1** (see below) |

---

## F1 Score — A Single Balance Number

**F1 Score:**

- **Official Definition:** Harmonic mean of precision and recall: `F1 = 2 × P × R / (P + R)`.
- **In Simple Words:** One score that punishes you if **either** precision or recall is very low.
- **Real-Life Example:** 100% precision but 10% recall is not a good model — F1 stays low; simple average would look misleadingly okay.

Use F1 when you want **one number** and both false alarms and misses matter. It does **not** replace reading the confusion matrix — it summarises precision and recall at the default **0.5** cut-off used by `predict`.

---

## ROC-AUC — Ranking Quality Without Picking a Threshold

Precision, recall, and F1 use **one threshold** (usually 0.5). **ROC-AUC** asks a different question: *Does the model rank Pass students above Fail students?*

**ROC curve (idea):** Plot **True Positive Rate (recall)** vs **False Positive Rate** as you move the threshold from strict to loose.

**AUC (Area Under Curve):**

- **Official Definition:** Area under the ROC curve, from 0 to 1.
- **In Simple Words:** Pick one random Pass and one random Fail — probability the model gives the Pass student a **higher** P(Pass).
- **Real-Life Example:** AUC 0.9 → 90% of such pairs are ranked correctly, before you fix a threshold.

| AUC | Rough meaning |
|---|---|
| ~1.0 | Excellent separation |
| 0.8–0.9 | Good |
| ~0.5 | No better than random guessing |

**Why it helps:** A model that always predicts Pass can have high **accuracy** on imbalanced data but **AUC ≈ 0.5** — useless ranking.

![ROC Curve: TPR vs FPR at All Thresholds](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/session31/roc_auc_curve.png)

```python
from sklearn.metrics import roc_auc_score, roc_curve  # AUC number and curve points
import matplotlib.pyplot as plt  # library to draw the ROC plot

y_prob_lr = lr.predict_proba(X_test)[:, 1]  # P(Pass) from logistic regression

print("AUC (uses probabilities, not 0/1 labels):")  # remind: pass probabilities in
print(f"  Logistic Regression : {round(roc_auc_score(y_test, y_prob_lr), 3)}")  # LR AUC
print(f"  Decision Tree       : {round(roc_auc_score(y_test, y_prob_tree), 3)}")  # tree AUC
print(f"  Random Forest       : {round(roc_auc_score(y_test, y_prob_rf), 3)}")  # forest AUC

fpr, tpr, _ = roc_curve(y_test, y_prob_rf)  # FPR and TPR at many thresholds for RF
plt.figure(figsize=(7, 5))  # new plot window size
plt.plot(fpr, tpr, label=f"Random Forest (AUC={round(roc_auc_score(y_test, y_prob_rf), 3)})")  # ROC line
plt.plot([0, 1], [0, 1], "--", color="gray", label="Random (0.5)")  # diagonal = random guess
plt.xlabel("False Positive Rate")  # x-axis label
plt.ylabel("True Positive Rate (Recall)")  # y-axis label (TPR is recall)
plt.title("ROC — Random Forest")  # chart title
plt.legend()  # show legend with model name and AUC
plt.tight_layout()  # reduce clipped labels
plt.show()  # display the figure
```

**How the code works:**

- **`roc_auc_score(y_test, y_prob)`** — needs **probabilities**, not hard labels.
- **`roc_curve`** — returns FPR/TPR points for plotting; underscore `_` ignores threshold array if you only plot.
- **Diagonal dashed line** — random classifier baseline (AUC 0.5).

**Report AUC when comparing models.** Use precision and recall when you care about mistakes at the cut-off your team actually uses (often 0.5 by default).

---

## Key Takeaways

- **Decision Trees** learn readable if-else rules; **`max_depth`** controls overfitting.
- **Random Forest** combines many trees by **vote** — usually more stable than one tree.
- **Precision** = trust when the model says Pass; **Recall** = how many real passes you catch — they trade off when you move the threshold.
- **F1** balances precision and recall in one number; **ROC-AUC** judges how well the model ranks Pass above Fail before you fix a cut-off.
- Always read the **confusion matrix** alongside any single metric — numbers hide who was misclassified.

Next you will build on these models and metrics when comparing and selecting classifiers for real pipelines.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Decision Tree** | Rule-based splits on features | Interpretable flowchart model |
| **max_depth** | Max question layers | Limits overfitting |
| **Gini impurity** | Split purity score | Tree picks best question per node |
| **Random Forest** | Many trees + majority vote | Stronger, stabler than one tree |
| **n_estimators** | Number of trees in forest | More trees → stabler, slower |
| **feature_importances_** | Feature contribution to splits | See what drove predictions |
| **Precision** | TP / (TP + FP) | Quality of positive predictions |
| **Recall** | TP / (TP + FN) | Coverage of actual positives |
| **F1 Score** | Harmonic mean of P and R | One balanced number at one threshold |
| **ROC-AUC** | Area under ROC curve | Threshold-free ranking quality |
| **`DecisionTreeClassifier`** | Single tree | `sklearn.tree` |
| **`RandomForestClassifier`** | Ensemble of trees | `sklearn.ensemble` |
| **`precision_score` / `recall_score` / `f1_score`** | Metric functions | `sklearn.metrics` on labels |
| **`roc_auc_score(y_true, y_prob)`** | AUC from probabilities | Compare models using ranking quality |

---
