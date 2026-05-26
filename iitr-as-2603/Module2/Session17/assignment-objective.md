# Objective Assignment: Regression Regularization and Evaluation

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A data scientist trains a regression model with many weak input columns. The model performs very well on training data but becomes unstable on new customer data because some coefficients are extremely large. Which technique is designed to reduce this problem by adding a penalty during training?

A. Regularization  
B. Data leakage  
C. Random shuffling only  
D. Manual sorting of rows

**Correct Answer:** A

**Answer Explanation:**  
A is correct because regularization adds a penalty to discourage very large coefficients, which can reduce overfitting and improve generalization.

B is incorrect because data leakage is a mistake where test or future information enters training. C is incorrect because shuffling alone does not penalize large coefficients. D is incorrect because sorting rows does not control model complexity.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

In scikit-learn, a learner increases `alpha` while training a Ridge or Lasso regression model. What is the expected effect of a higher `alpha` value?

A. Stronger regularization penalty  
B. Automatic increase in the number of test rows  
C. Removal of the need for train-test split  
D. Conversion of regression into classification

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `alpha` controls regularization strength in Ridge and Lasso; a higher value applies stronger shrinkage to coefficients.

B is incorrect because `alpha` does not change the dataset split. C is incorrect because models still need honest evaluation on held-out data. D is incorrect because Ridge and Lasso remain regression models.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A school score model uses `study_hours`, `sleep_hours`, `attendance`, and a few mildly useful behavior features. The team believes most features matter a little and wants to shrink extreme weights without dropping columns completely. Which model is the better fit?

A. Ridge Regression  
B. Lasso Regression only because it always keeps all features  
C. A mean baseline as the final predictive model  
D. A residual table without fitting a model

**Correct Answer:** A

**Answer Explanation:**  
A is correct because Ridge uses an L2 penalty that shrinks coefficients while usually keeping all features in the model.

B is incorrect because Lasso can set some coefficients exactly to zero, so it does not always keep all features. C is incorrect because a mean baseline is useful for comparison but not a regularized model. D is incorrect because residuals are used after predictions exist, not as a replacement for model fitting.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A regression dataset contains one deliberately useless column called `random_noise`. After training, one model gives this column a coefficient of exactly `0.0`, effectively removing it from the prediction. Which model behavior does this best represent?

A. Lasso feature selection  
B. Ridge keeping every coefficient large  
C. R-squared becoming negative by definition  
D. MAE ignoring all prediction errors

**Correct Answer:** A

**Answer Explanation:**  
A is correct because Lasso uses an L1 penalty and can shrink irrelevant feature coefficients exactly to zero, which acts like automatic feature selection.

B is incorrect because Ridge shrinks coefficients but rarely sets them exactly to zero. C is incorrect because negative R-squared means worse than the mean baseline, not feature removal. D is incorrect because MAE measures absolute errors and does not ignore them.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A learner compares Linear Regression, Ridge, and Lasso on the same student score dataset. Which evaluation practice gives the fairest comparison?

A. Fit each model on `X_train`, predict on the same `X_test`, and compute metrics against `y_test`.  
B. Fit each model on the full dataset and report only training R-squared.  
C. Give each model a different random test set so every model has a unique challenge.  
D. Choose the model with the largest coefficient for `random_noise`.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because all models should be trained on training rows and evaluated on the same held-out test rows using the same metrics.

B is incorrect because training metrics can hide overfitting. C is incorrect because different test sets make the comparison unfair. D is incorrect because a large coefficient on noise suggests the model may be chasing irrelevant patterns.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Two apartment rent models have the same MAE of `2500`, but Model B has RMSE `9000` while Model A has RMSE `3100`. What is the most reasonable interpretation?

A. Model B likely has a few much larger mistakes and needs error analysis.  
B. Model B is automatically better because RMSE is larger.  
C. Both models must have identical error patterns because MAE is the same.  
D. RMSE cannot be used for regression model evaluation.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because RMSE penalizes large errors more strongly than MAE. When RMSE is much larger than MAE, outliers or weak segments should be investigated.

B is incorrect because lower error metrics are usually better. C is incorrect because the same MAE can hide very different error distributions. D is incorrect because RMSE is a standard regression metric.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A model report shows test R-squared of `0.78` for predicting delivery time. Which statements interpret or use R-squared correctly?

A. The model explains a substantial part of the variation in delivery time compared with predicting the mean.  
B. R-squared should be paired with MAE or RMSE because it does not directly show error size in minutes.  
C. R-squared is always enough to approve deployment for every user segment.  
D. A negative R-squared would mean the model is worse than always predicting the mean on that test set.  
E. R-squared and MAE always have the same units.

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D are correct. R-squared measures explained variance compared with the mean baseline, but it should be paired with unit-based error metrics such as MAE or RMSE. Negative R-squared indicates worse performance than the mean baseline on that evaluation set.

C is incorrect because deployment also requires checking absolute error size and segment-level failures. E is incorrect because R-squared is unitless, while MAE has the same units as the target.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A hiring team wants to know whether its salary prediction model performs worse for junior candidates than senior candidates. Which steps are appropriate for error analysis?

A. Create residuals using `actual - predicted`.  
B. Create absolute error values to measure error size per row.  
C. Use `pd.cut` or another grouping method to create experience bands.  
D. Use `groupby` to compare average absolute error across the bands.  
E. Delete rows from the weakest group before reporting results so the global score improves.

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A, B, C, and D are correct because error analysis starts from row-level prediction errors, then groups rows by a meaningful feature range and compares error statistics by segment.

E is incorrect because removing weak rows to improve the report is misleading. The weak segment should be identified and investigated, not hidden.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A product team is building a demand prediction model with 40 features. Some features are known business signals, while many campaign-tracking columns may be irrelevant. Which statements about choosing between Ridge and Lasso are technically correct?

A. Lasso is useful when many columns may be irrelevant because it can set some coefficients to zero.  
B. Ridge is useful when most features are expected to contribute at least a little.  
C. A higher `alpha` generally applies stronger shrinkage in both Ridge and Lasso.  
D. Lasso always produces better test metrics than Ridge on every dataset.  
E. The best final choice should be based on held-out test performance and the business cost of errors.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are correct. Lasso can perform feature selection by zeroing some coefficients, Ridge shrinks all coefficients and is suitable when many features matter a little, and `alpha` controls penalty strength. Final model choice should come from honest test evaluation and business needs.

D is incorrect because no regularized model is guaranteed to beat another on every dataset. The data, feature quality, target noise, and chosen metric all matter.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A bank wants to present a regression model that estimates loan processing time. The global test metrics look good, but complaints are common for applications from small businesses. Which items should be included before calling the model deployment-ready?

A. MAE or RMSE on held-out test data, reported in business units such as hours or days.  
B. A comparison against the mean baseline or another simple baseline.  
C. Error analysis grouped by application type, including the small-business segment.  
D. Only the highest training R-squared among Linear, Ridge, and Lasso.  
E. A check for large train-test gaps that may indicate overfitting.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are correct because a responsible regression report should include held-out test metrics in real units, baseline comparison, segment-level error analysis, and overfitting checks.

D is incorrect because training R-squared alone can reward overfitting and does not prove the model works for new cases or for important user segments.
