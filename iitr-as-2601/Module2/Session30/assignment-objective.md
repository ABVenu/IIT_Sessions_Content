# Objective Assignment — Classification: Logistic Regression Fundamentals

---

## MCQ — Single Correct (Easy)

---

**Question 1**

Priya is an analyst at an e-commerce company. Her task is to build a model that looks at a customer's browsing history and predicts whether the customer will **buy a product** or **not buy**. Which type of machine learning problem is she solving?

- A) Regression — because the output is a numeric score
- B) Binary Classification — because the output is one of exactly two categories
- C) Multi-class Classification — because there are many possible purchase amounts
- D) Clustering — because she is grouping similar customers together

**Correct Answer:** B

**Explanation:**
The output is exactly two categories ("Buy" or "Not Buy"), which is the definition of Binary Classification. A regression framing would expect a continuous numeric output, which doesn't match a yes/no label. A multi-class framing would require three or more output categories. A clustering framing is unsupervised and lacks a labelled target, so it doesn't fit this supervised buy/not-buy prediction.

---

**Question 2**

After training a Logistic Regression model on student exam data, Rajan calls `model.predict(X_test)`. What does this method return for each test student?

- A) The raw linear score before the sigmoid function is applied
- B) A probability between 0 and 1 indicating how likely the student is to pass
- C) A class label — either 0 (Fail) or 1 (Pass)
- D) Two values — the probability of Fail and the probability of Pass — that always sum to 1

**Correct Answer:** C

**Explanation:**
`model.predict()` applies the sigmoid internally and then applies the default 0.5 threshold to return a final class label — 0 or 1. A raw pre-sigmoid score is only used internally and is never exposed by `predict()`. Returning a probability or a pair of class probabilities is the behaviour of `model.predict_proba()`, not `predict()`.

---

**Question 3**

The **sigmoid function**, given by $\sigma(x) = \frac{1}{1 + e^{-x}}$, is at the heart of Logistic Regression. No matter what value you feed into it, the output is always:

- A) Any real number from negative infinity to positive infinity
- B) Either exactly 0 or exactly 1
- C) Strictly between 0 and 1
- D) Between minus 1 and plus 1

**Correct Answer:** C

**Explanation:**
The sigmoid formula $\sigma(x) = \frac{1}{1 + e^{-x}}$ squashes any real input into a value strictly between 0 and 1 — never touching the endpoints — which makes it ideal for representing probability. An unbounded real-number range describes the raw linear score, before sigmoid. A hard 0-or-1 output would require applying a threshold after sigmoid. The range minus 1 to plus 1 corresponds to the `tanh` activation, not sigmoid.

---

**Question 4**

A Logistic Regression model evaluates a loan applicant and `model.predict_proba()` returns `[0.67, 0.33]` — where column 0 is the probability of Reliable and column 1 is the probability of Default. With the **default decision threshold of 0.5**, what class label does `model.predict()` assign?

- A) 1 (Default) — because the predicted probability of Default is non-zero
- B) 0 (Reliable) — because the predicted probability of Reliable is 0.67, which is above 0.5
- C) 1 (Default) — because 0.33 rounds up to 0.5
- D) 0.33 — the raw probability output

**Correct Answer:** B

**Explanation:**
The model predicts class 1 only when the probability of class 1 is at least 0.5. Here the probability of Default is 0.33, which is less than 0.5, so the prediction is class 0 (Reliable). A positive probability alone does not trigger a "Default" label — the threshold rule must be applied. Rounding 0.33 up to 0.5 is not how thresholding works. And `model.predict()` always returns a discrete class label, never a raw probability.

---

## MCQ — Single Correct (Moderate)

---

**Question 5**

Meera's spam detector calls `model.predict_proba(X_test)` for two emails and receives `[[0.91, 0.09], [0.18, 0.82]]`, where class 1 = Spam. With the **default 0.5 threshold**, what does `model.predict()` output?

- A) Email 1 is Spam and Email 2 is Not Spam
- B) Email 1 is Not Spam and Email 2 is Spam
- C) Both emails are Spam, because all probabilities are positive
- D) Both emails are Not Spam

**Correct Answer:** B

**Explanation:**
The second column is always the probability of class 1, i.e., the probability of Spam. For Email 1, this probability is 0.09, which is less than 0.5 → Not Spam. For Email 2, this probability is 0.82, which is at least 0.5 → Spam. Swapping the two labels reverses the correct assignment. Claiming both are Spam ignores the threshold — a non-zero probability alone does not make a prediction positive. Labelling Email 2 as Not Spam directly contradicts its high probability of 0.82.

---

**Question 6**

A hospital uses a Logistic Regression model to screen patients for a serious illness (class 1 = Disease Detected, class 0 = Healthy). The default threshold is 0.5. The medical board says: *"Missing a real patient is catastrophic. A false alarm just means one extra test — inconvenient, but safe."* What threshold adjustment makes the most sense?

- A) Raise the threshold to 0.8, so the model flags only very confident cases
- B) Keep the threshold at 0.5, since the default is designed for balanced errors
- C) Lower the threshold to 0.3, so even a 30 percent suspicion triggers a positive flag
- D) Disable thresholding entirely and only read the raw probability outputs

**Correct Answer:** C

**Explanation:**
Lowering the threshold makes the model flag positives more readily, which reduces False Negatives — the catastrophic "missed patient" error the board is most worried about. Raising the threshold has the opposite effect: the model becomes stricter and misses more true cases. Keeping the default 0.5 assumes symmetric costs, but here the costs are highly asymmetric. Abandoning thresholds entirely leaves the probability outputs without any decision rule to act on.

---

## MSQ — Multiple Correct (Moderate)

---

**Question 7**

Which of the following statements about `model.predict_proba()` in scikit-learn's Logistic Regression are **correct**? *(Select all that apply.)*

- A) It returns two columns — one probability for each class — for every row
- B) The two column values for any single row always sum to exactly 1.0
- C) It returns raw scores before the sigmoid function is applied
- D) You can extract only the positive-class probabilities by selecting the second column

**Correct Answers:** A, B, D

**Explanation:**
In binary classification, `predict_proba` always returns two columns — the probability of class 0 and the probability of class 1 — and those two values must sum to exactly 1 for every row, because they form a probability distribution over the two classes. Selecting only the positive-class column (the second column) is the standard idiom used when tuning a custom threshold. The claim that `predict_proba` returns raw pre-sigmoid scores is incorrect — the sigmoid has already been applied; raw scores are never exposed by this method.

---

**Question 8**

Neha trains a Logistic Regression model to predict student pass/fail. After inspecting the confusion matrix she sees a **very high False Negative count**. Which statements are correct? *(Select all that apply.)*

- A) The model predicted Fail for students who actually Passed
- B) The model predicted Pass for students who actually Failed
- C) Lowering the decision threshold would help reduce False Negatives
- D) A False Negative is also known as a Type II Error

**Correct Answers:** A, C, D

**Explanation:**
A False Negative means the truth was Positive (Pass) but the model predicted Negative (Fail), so students who actually passed were mislabelled as failing. Lowering the threshold causes the model to predict "Pass" more readily, which directly reduces the number of missed passes (False Negatives). By standard terminology, a False Negative is a Type II Error. Predicting Pass for students who actually failed describes a False Positive (Type I Error), not a False Negative — so that statement is wrong.

---

## MSQ — Multiple Correct (Hard)

---

**Question 9**

A bank tests its loan-default Logistic Regression model on 300 applicants. In this problem, class 1 = **Will Default** and class 0 = **Will Not Default**. The confusion matrix is:

|  | **Predicted: Will Not Default (0)** | **Predicted: Will Default (1)** |
|---|---|---|
| **Actual: Will Not Default (0)** | TN = 180 | FP = 30 |
| **Actual: Will Default (1)** | FN = 20 | TP = 70 |

Accuracy is defined as $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$ and the False Positive Rate as $\text{FPR} = \frac{FP}{FP + TN}$.

Select **all** correct statements. *(Select all that apply.)*

- A) The model's overall accuracy is 83.3 percent
- B) 20 customers who would actually default slipped through as "safe" and were incorrectly approved
- C) 30 customers who would not default were incorrectly flagged and denied a loan
- D) The False Positive Rate is approximately 14.3 percent

**Correct Answers:** A, B, C, D

**Explanation:**
Accuracy evaluates to $(70 + 180)/300 = 0.833$, i.e., 83.3 percent. The 20 False Negatives represent actual defaulters whom the model approved — a dangerous business miss. The 30 False Positives represent reliable customers whom the model wrongly flagged as risky and denied. The False Positive Rate evaluates to $30/(30 + 180) \approx 0.143$, i.e., about 14.3 percent. All four statements correctly describe the information encoded in this confusion matrix.

---

**Question 10**

A healthcare startup builds a Logistic Regression model to detect diabetes. The dataset has **950 healthy patients** and **50 diabetic patients**. A junior data scientist proposes a shortcut: instead of training a model, just predict **"Healthy" for every single patient**. Which of the following are correct about this "shortcut" model? *(Select all that apply.)*

- A) Its accuracy would be 95 percent
- B) Its True Positive count would be 0
- C) Its False Negative count would be 50
- D) Accuracy is a reliable and sufficient metric to judge this model's quality

**Correct Answers:** A, B, C

**Explanation:**
With 950 healthy patients correctly labelled out of 1000 total, the shortcut model scores $950/1000 = 0.95$, i.e., 95 percent accuracy. But because it never predicts "Diabetic", its True Positive count is 0, and all 50 actual diabetics are missed, producing a False Negative count of 50. The claim that accuracy alone is a reliable and sufficient metric is wrong — accuracy is deeply misleading here due to class imbalance, since a 95 percent accurate model that catches zero diabetics is clinically worthless. This is exactly why the confusion matrix (TP, FN, precision, recall) must be consulted alongside accuracy.
