# Objective Assignment: Logistic Regression Fundamentals

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A weather app team wants to forecast tomorrow's maximum temperature in degrees Celsius for each city. A hiring platform wants to label each job application as **Selected** or **Rejected**. Which pairing correctly matches each task to the problem type?

A. Temperature forecast → Regression; Application label → Classification  
B. Temperature forecast → Classification; Application label → Regression  
C. Both tasks are regression because both use numeric inputs  
D. Both tasks are classification because both produce a single final answer

**Correct Answer:** A

**Answer Explanation:**  
A is correct because temperature is a continuous number (regression), while Selected/Rejected is a category choice (classification).

B reverses the two problem types. C is incorrect because numeric inputs alone do not define the problem type; the output shape does. D is incorrect because only the application task is classification.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A health app estimates the chance that a user has a certain condition before showing a yes/no alert. The model must output a value that always lies strictly between 0 and 1. Which function is used in Logistic Regression to convert a raw weighted score into that probability?

A. Sigmoid  
B. Mean squared error  
C. Train-test split  
D. StandardScaler

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the sigmoid maps any real number into the interval (0, 1), which is valid for probability.

B is incorrect because mean squared error is a loss metric for regression, not a probability mapping. C is incorrect because train-test split is an evaluation practice, not a squashing function. D is incorrect because StandardScaler rescales features; it does not produce class probabilities.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

An exam-coaching platform trains Logistic Regression to predict **Pass (1)** or **Fail (0)**. For one student, `predict_proba` returns `[0.27, 0.73]`. What do these two numbers represent?

A. P(Fail) = 0.27 and P(Pass) = 0.73; they sum to 1.0 for that row  
B. P(Pass) = 0.27 and the model is 73% accurate on the full test set  
C. The student failed 27 times and passed 73 times in the training data  
D. The raw regression score is 0.27 and the threshold is 0.73

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `predict_proba` returns class probabilities for each label, and for binary problems the two columns sum to 1.0.

B incorrectly swaps the meaning of the columns and confuses row probability with dataset accuracy. C is incorrect because these are model outputs, not historical counts. D is incorrect because the values are probabilities, not a raw score paired with a threshold.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A bank uses Logistic Regression with scikit-learn defaults to flag loan defaults. Without changing any settings, which probability rule does `model.predict(X_test)` apply to assign class **1** (default)?

A. Predict class 1 when P(class 1) ≥ 0.5  
B. Predict class 1 only when P(class 1) = 1.0  
C. Predict class 1 when P(class 1) ≥ 0.9  
D. Predict class 1 when the raw linear score is exactly 0

**Correct Answer:** A

**Answer Explanation:**  
A is correct because scikit-learn's default decision threshold for `predict()` is 0.5 on the positive-class probability.

B is incorrect because probabilities are rarely exactly 1.0 before thresholding. C describes a custom high threshold, not the default. D is incorrect because `predict()` uses probability after sigmoid, not the raw score alone.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A tutor reviews model output for two students. Student **M** has P(Pass) = 0.48. Student **N** has P(Pass) = 0.91. The team uses threshold **0.5** for final labels. What labels does the model assign?

A. M → Fail, N → Pass  
B. M → Pass, N → Pass  
C. M → Fail, N → Fail  
D. M → Pass, N → Fail

**Correct Answer:** A

**Answer Explanation:**  
A is correct because 0.48 < 0.5 gives Fail for M, and 0.91 ≥ 0.5 gives Pass for N.

B is wrong because M's probability is below the threshold. C is wrong because N's probability is above the threshold. D reverses both decisions.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A disease-screening model is evaluated on 1,000 patients. **900** are healthy and **100** are sick. The model predicts **No disease** for every patient and reports **90% accuracy**. Why is accuracy alone misleading here?

A. The confusion matrix would show TP = 0, so no sick patients were correctly detected  
B. Accuracy is undefined for binary classification  
C. Logistic Regression cannot use accuracy on medical data  
D. A 90% score proves the model is better than random guessing in every segment

**Correct Answer:** A

**Answer Explanation:**  
A is correct because always predicting the majority class can yield high accuracy while missing every positive case (TP = 0), which the confusion matrix reveals.

B is incorrect because accuracy is defined for classification. C is incorrect because accuracy can be computed for any binary classifier. D is incorrect because high overall accuracy can still hide complete failure on the minority class.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A fraud team lowers the decision threshold from **0.5** to **0.3** on an existing Logistic Regression model (weights unchanged). Which outcomes are generally expected?

A. More rows are predicted as fraud (positive class)  
B. False negatives usually decrease  
C. False positives usually increase  
D. The model must be retrained from scratch for every threshold change  
E. True negatives always become zero

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C are correct. A lower threshold flags more positives, which catches more real fraud (fewer FN) but also raises false alarms (more FP).

D is incorrect because thresholding is applied after `predict_proba`; retraining is not required. E is incorrect because TN does not always become zero; it usually decreases but not necessarily to zero.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A credit-risk analyst reads a binary confusion matrix for **default (1)** vs **paid on time (0)**. Which statements correctly describe the error cells?

A. **False positive:** predicted default, customer actually paid on time  
B. **False negative:** predicted no default, customer actually defaulted  
C. **True positive:** predicted default, customer actually defaulted  
D. **False negative:** predicted default, customer actually paid on time  
E. **True negative:** predicted no default, customer actually paid on time

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are correct definitions of FP, FN, TP, and TN for a default-detection setting.

D is incorrect because it describes a false positive (predicted positive, actual negative), not a false negative.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A data scientist builds a tumour **benign vs malignant** classifier using `load_breast_cancer()` with several numeric features on different scales. Which practices align with a sound sklearn workflow?

A. Use a `Pipeline` with `StandardScaler` before `LogisticRegression`  
B. Fit the pipeline on training rows only, then evaluate on held-out test rows  
C. Fit `StandardScaler` on the full dataset including test rows to improve scaling  
D. Read `confusion_matrix(y_test, y_pred)` to inspect TP, TN, FP, and FN  
E. Report only test accuracy and ignore the confusion matrix when classes are imbalanced

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D are correct. Scaling inside a pipeline on train data avoids leakage, and the confusion matrix shows error types that accuracy alone can hide.

C is incorrect because fitting the scaler on test data leaks information. E is incorrect because high accuracy can mask dangerous false negatives in medical or imbalanced settings.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

An EdTech platform uses Logistic Regression for course completion. Product rules are:

- Auto-enroll in advanced track if P(complete) > 0.85  
- Human mentor call if 0.45 ≤ P(complete) ≤ 0.85  
- Send remedial plan if P(complete) < 0.45  

Which implementation choices support this design?

A. Use `predict_proba(X)[:, 1]` to read P(complete) per learner  
B. Use `predict()` alone, because it returns probabilities for each band  
C. Apply custom threshold rules in code after probabilities are computed  
D. Retrain separate models for each band (0.45 and 0.85) before routing learners  
E. Use the same trained model and change only post-processing rules when business cut-offs change

**Correct Answers:** A, C, E

**Answer Explanation:**  
A, C, and E are correct. Probabilities from `predict_proba` enable multiple business bands; routing logic can be updated without retraining when only cut-offs change.

B is incorrect because `predict()` returns class labels, not graded probability bands. D is unnecessary for threshold bands on one trained model.

---
