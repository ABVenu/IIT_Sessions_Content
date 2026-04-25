# Objective Assignment — Classification Models and Evaluation Metrics

---

## MCQ — Single Correct Answer

---

**Question 1** *(Easy)*

A bank's loan approval system uses a Decision Tree to classify applicants as "Approve" or "Reject." The tree checks "Is annual income > ₹6,00,000?" at its root node, and after several more questions, arrives at a leaf node. What does the leaf node represent?

A) The feature that contributed the most to the decision
B) A new question to further refine the prediction
C) The final class prediction — Approve or Reject — with no further questions asked
D) The threshold used to split the data at the root

**Correct Answer:** C

**Answer Explanation:**
A leaf node is the terminal node at the bottom of a branch in a Decision Tree. Once a data point reaches a leaf node, the tree delivers its final class prediction without asking any more questions. Option A describes feature importance, not a leaf node. Option B describes an internal node. Option D describes the split value at a node, not the leaf itself.

---

**Question 2** *(Easy)*

Priya is training a Decision Tree to predict whether a customer will buy a product. She notices that on the training data the model is nearly perfect, but on new unseen customers it performs poorly. A fellow data scientist suggests setting `max_depth=5`. Why does this help?

A) It increases the number of features the tree considers at each split
B) It forces the tree to learn general patterns by limiting how many question layers it can build, preventing it from memorising training noise
C) It makes the tree use Recall instead of Gini Impurity to choose splits
D) It increases the training dataset size automatically through bootstrapping

**Correct Answer:** B

**Answer Explanation:**
Without a depth limit, a Decision Tree grows until it perfectly memorises every training data point — including noise and quirks that don't generalise. Setting `max_depth=5` stops the tree at 5 levels, forcing it to capture only the broadest, most consistent patterns. Option A describes random feature selection (used in Random Forest). Option C is incorrect — Gini Impurity is always used for split selection regardless of depth. Option D describes bagging, a Random Forest concept.

---

**Question 3** *(Easy)*

A content moderation model reviews 200 posts and flags 50 as "Harmful." Upon manual review, 40 of those 50 flagged posts are genuinely harmful. What is the Precision of this model?

A) 40%
B) 60%
C) 80%
D) 20%

**Correct Answer:** C

**Answer Explanation:**
Precision = TP / (TP + FP). The model flagged 50 posts as Harmful (predicted positives). Of those, 40 were truly harmful (True Positives) and 10 were incorrectly flagged (False Positives). Precision = 40 / (40 + 10) = 40 / 50 = 0.80 = 80%. The other options arise from confusing Precision with Recall or with overall accuracy.

---

**Question 4** *(Easy)*

A data scientist plots the ROC curve for two models. Model A's curve hugs the top-left corner of the plot, while Model B's curve closely follows the diagonal dashed line. What can be concluded?

A) Model B is better because it predicts more students as positive
B) Both models are equally good — the diagonal line represents a strong baseline
C) Model A is better; its curve being close to the top-left means high True Positive Rate with low False Positive Rate
D) Model B has a higher AUC than Model A

**Correct Answer:** C

**Answer Explanation:**
The diagonal line on an ROC plot represents a random classifier with AUC = 0.5 — it has no real predictive power. A curve that hugs the top-left corner means the model achieves a high True Positive Rate (Recall) while keeping the False Positive Rate low, which corresponds to high AUC (excellent model). Model B, tracking the diagonal, is essentially guessing randomly. Option D is directly backwards.

---

**Question 5** *(Moderate)*

A healthcare startup builds a model to screen patients for early-stage diabetes. A false negative (missing a sick patient) could mean the disease goes undetected for years, causing serious harm. A false positive (flagging a healthy patient) results only in a follow-up blood test. Which single metric should the team prioritise when selecting between model versions?

A) Precision — it penalises false positives, reducing unnecessary follow-up tests
B) Accuracy — it measures the overall correctness of the model
C) F1 Score — it balances both Precision and Recall equally
D) Recall — it minimises false negatives, ensuring the fewest sick patients are missed

**Correct Answer:** D

**Answer Explanation:**
Recall = TP / (TP + FN). When the cost of a False Negative far exceeds the cost of a False Positive, Recall is the correct priority metric. In this scenario, missing a sick patient (False Negative) is severely harmful, while an unnecessary follow-up (False Positive) is a minor inconvenience. Accuracy is misleading in healthcare contexts where one class dominates. F1 balances both errors equally, which is inappropriate when one error type is clearly more costly. Precision focuses on reducing false alarms, which is the wrong priority here.

---

**Question 6** *(Moderate)*

A data scientist evaluates two fraud detection models:

| Model | Precision | Recall |
|---|---|---|
| Model A | 0.92 | 0.15 |
| Model B | 0.68 | 0.74 |

Which model has a higher F1 Score, and why?

A) Model A, because its Precision is significantly higher
B) Model B, because its Precision and Recall are both reasonably high and balanced
C) Both models have the same F1 Score since the differences cancel out
D) F1 Score cannot be determined without the full confusion matrix

**Correct Answer:** B

**Answer Explanation:**
F1 Score = 2 × (Precision × Recall) / (Precision + Recall). The harmonic mean severely penalises extreme imbalance.
- Model A: F1 = 2 × (0.92 × 0.15) / (0.92 + 0.15) = 0.276 / 1.07 ≈ 0.258
- Model B: F1 = 2 × (0.68 × 0.74) / (0.68 + 0.74) = 1.006 / 1.42 ≈ 0.709

Model B's F1 is far higher. A near-perfect Precision with terrible Recall (Model A) produces a very low F1 — the harmonic mean is designed to be pulled down by whichever value is weakest.

---

## MSQ — Multiple Correct Answers

---

**Question 7** *(Moderate)*

Rahul is explaining Random Forest to a client. Which of the following statements are **correct** about how a Random Forest works? **Select ALL that apply.**

A) Each tree in the forest is trained on a bootstrapped sample — a random subset of the training data drawn with replacement
B) At every split in every tree, only a random subset of features is considered, not all features
C) All 100 trees in a `RandomForestClassifier(n_estimators=100)` see exactly the same training data
D) For classification, the final prediction is determined by majority vote across all trees
E) Because it is an ensemble model, a Random Forest is always slower to train than a single Decision Tree with the same `max_depth`

**Correct Answers:** A, B, D, E

**Answer Explanation:**
- **A (Correct):** Bagging (Bootstrap Aggregating) trains each tree on a different randomly sampled subset of the training data, with replacement — so some records appear multiple times and others not at all.
- **B (Correct):** Random feature selection at each node forces further diversity between trees, preventing them from all learning the same dominant patterns.
- **C (Incorrect):** Each tree sees a *different* bootstrapped sample — this diversity is the core mechanism that makes Random Forest more robust than a single tree.
- **D (Correct):** For classification, the class that receives the most votes from the individual trees becomes the final prediction.
- **E (Correct):** Training 100 trees (even shallower ones) takes more computation than training one tree. This is the trade-off you accept for higher accuracy and stability.

---

**Question 8** *(Moderate)*

A data scientist is working on a credit default prediction model. She uses `precision_recall_curve` on the Random Forest's probability outputs and observes the results at different thresholds. Which of the following effects will **definitely occur** if she lowers the classification threshold from 0.5 to 0.25? **Select ALL that apply.**

A) More applicants will be classified as "Default" (positive class)
B) Recall for the positive class will increase
C) Precision for the positive class will increase
D) The number of False Positives will increase
E) The model will now catch a higher fraction of applicants who will actually default

**Correct Answers:** A, B, D, E

**Answer Explanation:**
Lowering the threshold means predicting "positive" for any applicant whose P(Default) ≥ 0.25 instead of ≥ 0.5. This casts a wider net:
- **A (Correct):** More applicants cross the lower threshold → more positive predictions.
- **B (Correct):** More actual defaulters are now captured → Recall increases.
- **C (Incorrect):** By including more borderline cases (lower probability scores), the fraction of false alarms among positive predictions rises → Precision *decreases*.
- **D (Correct):** More non-defaulters will cross the lower threshold and be incorrectly predicted as Default → False Positives increase.
- **E (Correct):** Higher Recall means more of the true positives (actual defaulters) are correctly caught.

---

**Question 9** *(Hard)*

An e-commerce platform trains three fraud detection models and plots their ROC curves on the same chart. The AUC values are: Model X = 0.94, Model Y = 0.78, Model Z = 0.51. Which of the following statements are **correct**? **Select ALL that apply.**

A) Model X's ROC curve lies closest to the top-left corner of the plot
B) All three models are better than a random classifier
C) Model Z's ROC curve is nearly indistinguishable from the diagonal baseline
D) AUC is computed from probability scores, not hard class labels, making it threshold-independent
E) Selecting Model X guarantees it will have the highest Precision at every possible threshold

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A (Correct):** Higher AUC → curve closer to the top-left corner (high TPR with low FPR). Model X at 0.94 has the best-positioned curve.
- **B (Incorrect):** A random classifier has AUC = 0.5. Model Z at 0.51 is only marginally above random — practically no better than chance. Model Y (0.78) and Model X (0.94) are clearly better, but Model Z is borderline useless.
- **C (Correct):** AUC = 0.51 is essentially the diagonal line (AUC = 0.5). Model Z's curve will track closely along that diagonal.
- **D (Correct):** `roc_auc_score(y_true, y_prob)` takes probability outputs, not binary predictions. It evaluates ranking ability across all thresholds simultaneously.
- **E (Incorrect):** AUC measures overall ranking ability, not Precision at any particular threshold. A model with higher AUC can still have lower Precision at specific thresholds depending on the data distribution.

---

**Question 10** *(Hard)*

Sana is using the following code on her Random Forest model to find the optimal classification threshold:

```python
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob_rf)
f1_scores = 2 * precisions[:-1] * recalls[:-1] / (precisions[:-1] + recalls[:-1] + 1e-9)
best_idx = f1_scores.argmax()
best_threshold = thresholds[best_idx]
y_pred_optimised = (y_prob_rf >= best_threshold).astype(int)
```

Which of the following statements about this code and the threshold tuning process are **correct**? **Select ALL that apply.**

A) `precision_recall_curve` internally tests every unique probability value in `y_prob_rf` as a candidate threshold
B) The `[:-1]` slicing on `precisions` and `recalls` is needed because those arrays have one more entry than the `thresholds` array
C) `f1_scores.argmax()` returns the threshold value itself, not the index of that threshold
D) If `best_threshold` turns out to be 0.35, then any test student with `y_prob_rf >= 0.35` will be predicted as positive (1)
E) The `1e-9` term in the F1 formula prevents a division-by-zero error at extreme thresholds where both Precision and Recall could be zero

**Correct Answers:** A, B, D, E

**Answer Explanation:**
- **A (Correct):** `precision_recall_curve` sweeps through every unique probability score in `y_prob_rf` as a threshold, returning the resulting Precision and Recall arrays — this is what makes it exhaustive across all thresholds.
- **B (Correct):** By design, scikit-learn's `precision_recall_curve` returns `len(thresholds) + 1` values for Precision and Recall (the last entry corresponds to the trivial threshold where nothing is predicted positive). The `[:-1]` removes this extra entry to align the arrays for F1 computation.
- **C (Incorrect):** `argmax()` returns the *index* of the maximum value, not the value itself. The threshold value is then accessed as `thresholds[best_idx]`.
- **D (Correct):** `(y_prob_rf >= best_threshold).astype(int)` converts every probability ≥ `best_threshold` to 1 (positive) and every probability below it to 0 (negative). This is the standard way to apply a custom threshold.
- **E (Correct):** At extreme thresholds (e.g., threshold = 1.0), both Precision and Recall can be 0, making the denominator 0. Adding `1e-9` (an extremely small number) avoids a `ZeroDivisionError` or `NaN` without meaningfully affecting the F1 scores at valid thresholds.
