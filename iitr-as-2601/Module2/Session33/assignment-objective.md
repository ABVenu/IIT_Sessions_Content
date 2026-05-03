# Assignment: Time Series — Forecasting Data That Changes Over Time

## Objective Assignment

**Total Questions: 10 | Format: MCQ (Single Correct) and MSQ (Multiple Correct)**  
**Order: Easy → Moderate → Hard**

---

### Question 1 — MCQ (Easy)

Meera records her cafe's total sales every evening for 90 days. She wants to use this data to understand how sales change over time. What makes this dataset a time series dataset?

- A) It contains many rows, so it is automatically a time series
- B) The order of records by date matters for understanding the pattern
- C) The sales values are numeric, so the data must be time series data
- D) The dataset can be shuffled without losing meaning

**Correct Answer: B**

**Answer Explanation:**  
A time series is a sequence of data points recorded at successive points in time. The key feature is that the order matters. In Meera's cafe data, Day 10 comes after Day 9, and shuffling the rows would destroy the meaning of the pattern. Option A is incorrect because row count does not define time series data. Option C is incorrect because numeric data can also exist in regular non-time-series datasets. Option D is the opposite of time series behavior; shuffling time series data removes the time relationship.

---

### Question 2 — MCQ (Easy)

A fitness app tracks the number of active users every month. Over three years, the number generally rises from 20,000 users to 85,000 users, even though a few months show small drops. Which time series pattern is this mainly showing?

- A) Positive trend
- B) Weekly seasonality
- C) Future leakage
- D) Random split

**Correct Answer: A**

**Answer Explanation:**  
A trend is the long-term direction of a time series. Since the app's active users generally increase over several years, the series shows a positive trend. Small month-to-month drops do not remove the overall upward direction. Option B is incorrect because weekly seasonality refers to a repeating weekly cycle, which is not described here. Option C is incorrect because future leakage is a train-test split problem. Option D is incorrect because random split is a data splitting method, not a pattern in the data.

---

### Question 3 — MCQ (Easy)

A pizza delivery platform sees high order volumes every Friday and Saturday, while Monday to Thursday orders stay lower. This pattern repeats almost every week. What is this an example of?

- A) Flat trend
- B) Weekly seasonality
- C) Mean Absolute Percentage Error
- D) Naive forecast

**Correct Answer: B**

**Answer Explanation:**  
Seasonality is a regular repeating pattern that occurs at a fixed interval. Since the order spike repeats every week on Friday and Saturday, this is weekly seasonality. Option A is incorrect because the question describes a repeated weekly cycle, not a long-term flat direction. Option C is a model evaluation metric. Option D is a baseline forecasting method where the next value is predicted as the current value.

---

### Question 4 — MCQ (Easy)

Kabir is preparing a time series model to predict next month's sales. He randomly shuffles all monthly sales records before splitting them into train and test sets. What is the biggest risk in this approach?

- A) The model may train much slower than usual
- B) The test set may contain only low sales values
- C) Future data may leak into the training set, making evaluation unrealistic
- D) The model will be unable to calculate rolling averages

**Correct Answer: C**

**Answer Explanation:**  
Random splitting is unsafe for time series because future records can enter the training set while earlier records remain in the test set. This creates future leakage: the model gets information it would not have in a real forecasting situation. Option A may or may not happen and is not the core issue. Option B is not the main guaranteed risk. Option D is incorrect because rolling averages can still be calculated, but the evaluation would be logically wrong.

---

### Question 5 — MCQ (Moderate)

A grocery chain has 10 months of sales data and wants an 80:20 chronological split for forecasting:

| Month | Sales |
|---|---:|
| Jan | 80 |
| Feb | 85 |
| Mar | 90 |
| Apr | 88 |
| May | 95 |
| Jun | 100 |
| Jul | 102 |
| Aug | 105 |
| Sep | 110 |
| Oct | 115 |

Which split is correct?

- A) Train on Sep-Oct and test on Jan-Aug
- B) Randomly choose any 8 months for training and any 2 months for testing
- C) Train on Jan-Aug and test on Sep-Oct
- D) Train on Jan, Mar, May, Jul, Sep and test on Feb, Apr, Jun, Aug, Oct

**Correct Answer: C**

**Answer Explanation:**  
For time series, the correct split is chronological: older data goes into training, newer data goes into testing. With 10 months and an 80:20 split, the first 8 months (Jan-Aug) should be training data, and the last 2 months (Sep-Oct) should be test data. Option A reverses time and trains on the future. Option B causes future leakage. Option D breaks the time order by alternating months between train and test.

---

### Question 6 — MCQ (Moderate)

An analyst creates a 3-day rolling mean on this sales series: Day 1 = 100, Day 2 = 120, Day 3 = 110, Day 4 = 130. What should be the 3-day rolling mean for Day 4?

- A) 110.00
- B) 115.00
- C) 120.00
- D) 130.00

**Correct Answer: C**

**Answer Explanation:**  
A 3-day rolling mean for Day 4 uses Day 2, Day 3, and Day 4: `(120 + 110 + 130) / 3 = 120`. Option A incorrectly averages Day 1-Day 3. Option B is the average of all four days, which is not a 3-day rolling window. Option D is only the Day 4 value, not an average.

---

### Question 7 — MSQ (Moderate)

Which of the following statements about rolling windows and lag features are TRUE? (Select all that apply)

- A) A rolling window computes statistics over a fixed-size recent time period
- B) A 7-day rolling mean can help smooth noisy daily values
- C) A lag feature uses a past value, such as yesterday's sales, as a new feature
- D) A rolling window should use future test values while creating training features

**Correct Answers: A, B, C**

**Answer Explanation:**  
- **A — CORRECT:** A rolling window slides through time and computes statistics such as mean, standard deviation, or maximum over a fixed-size window.  
- **B — CORRECT:** Rolling means smooth noisy day-to-day fluctuations and make the underlying pattern easier to see.  
- **C — CORRECT:** Lag features bring previous values forward, such as `lag_1` for yesterday's sales or `lag_7` for the value from one week ago.  
- **D — INCORRECT:** Using future test values while creating training features would cause future leakage. Time series features must respect time order.

---

### Question 8 — MSQ (Moderate)

A forecasting team is evaluating a time series model. Which of the following are valid evaluation or comparison ideas covered in the session? (Select all that apply)

- A) Use MAE to measure average absolute error
- B) Use RMSE when large errors are especially costly
- C) Use MAPE to express error as a percentage of actual value
- D) Skip baseline models because complex models are always better

**Correct Answers: A, B, C**

**Answer Explanation:**  
- **A — CORRECT:** MAE can be used for time series forecasting because forecasting is a regression problem.  
- **B — CORRECT:** RMSE is useful when large errors should be penalized more strongly.  
- **C — CORRECT:** MAPE expresses error as a percentage, making it useful when comparing different scales.  
- **D — INCORRECT:** The session clearly states that every complex model should be compared against simple baselines such as naive forecast, seasonal naive, or rolling mean forecast.

---

### Question 9 — MSQ (Hard)

An online grocery company forecasts demand for three product categories. Which statements about MAPE are correct? (Select all that apply)

- A) MAPE reports prediction error as a percentage of the actual value
- B) MAPE makes it easier to compare errors across products with different sales scales
- C) MAPE works safely even when actual values are zero
- D) If actual sales are 200 and predicted sales are 180, the percentage error for that point is 10%

**Correct Answers: A, B, D**

**Answer Explanation:**  
- **A — CORRECT:** MAPE stands for Mean Absolute Percentage Error and expresses error as a percentage.  
- **B — CORRECT:** Because MAPE is scale-independent, it helps compare models across products with different sales volumes.  
- **C — INCORRECT:** MAPE breaks down when actual values are zero or very close to zero because the formula divides by the actual value. In such cases, MAE is safer.  
- **D — CORRECT:** The absolute error is `|200 - 180| = 20`; `20 / 200 = 0.10`, so the percentage error is 10%.

---

### Question 10 — MSQ (Hard)

Rohan is designing a forecasting workflow for daily website traffic. Which decisions correctly follow time series principles from the session? (Select all that apply)

- A) Sort the dataset by date before splitting or creating time-based features
- B) Train on older records and test on newer records
- C) Compare the model against a naive forecast or rolling mean baseline
- D) Shuffle all rows first so that the model sees every kind of pattern equally

**Correct Answers: A, B, C**

**Answer Explanation:**  
- **A — CORRECT:** Time series data must be sorted by time so that the sequence is meaningful.  
- **B — CORRECT:** Chronological split is the correct time-aware split: past data for training, future data for testing.  
- **C — CORRECT:** Baselines are essential because they show whether a complex model is actually better than a simple forecasting rule.  
- **D — INCORRECT:** Shuffling rows breaks time order and can cause future leakage during training and evaluation.
