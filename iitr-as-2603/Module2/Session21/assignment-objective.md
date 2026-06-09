# Objective Assignment - Time Series: Understanding Data That Changes Over Time

## Instructions
- Total questions: 10
- Question types: 6 MCQs (single correct), 4 MSQs (multiple correct)
- Difficulty progression: Easy → Moderate → Hard

---

## MCQs (Single Correct)

### Q1 (Easy)
A campus canteen records **meal counts for 90 consecutive days** and wants to forecast next week's demand. Why must the rows stay in **date order**?

A. Because sklearn requires rows to be sorted alphabetically by column name  
B. Because each day depends on the time sequence; shuffling destroys the forecasting story  
C. Because PCA only works on chronologically sorted tables  
D. Because K-Means assigns clusters by calendar month  

**Correct Answer:** B  
**Explanation:** Time series rows are order-dependent — yesterday influences today. Shuffling breaks the timeline and makes forecasting meaningless. sklearn does not require alphabetical order (A). PCA and K-Means are unrelated to why canteen daily counts need date order (C, D).

---

### Q2 (Easy)
Over the last **10 years**, India's total smartphone users grew steadily even though some months dipped. Which pattern best describes that **long-term growth**?

A. Seasonality  
B. Trend  
C. Data leakage  
D. Lag feature  

**Correct Answer:** B  
**Explanation:** Trend is the long-term direction over months or years. Seasonality (A) is a repeating cycle at fixed intervals (e.g. summer spikes every year). Leakage (C) is a train/test mistake. Lag feature (D) is engineered input, not a pattern type.

---

### Q3 (Easy)
An ice-cream delivery app sees orders **jump every summer and drop every winter**, repeating each year on a fixed calendar rhythm. Which pattern is this?

A. Trend  
B. Seasonality  
C. Random noise only  
D. Future leakage  

**Correct Answer:** B  
**Explanation:** Repeating peaks and dips at fixed yearly intervals is seasonality. A decade-long rise in total users would be trend (A). Noise alone (C) does not explain a predictable yearly rhythm. Leakage (D) is about train/test contamination, not sales cycles.

---

### Q4 (Easy)
A data team is about to shuffle rows before modeling. For which dataset is **random shuffling most dangerous**?

A. Customer segments from K-Means on purchase history (no date column)  
B. Daily stock closing prices for the last 2 years  
C. Tumour measurements after PCA with no time column  
D. Student exam marks from different colleges with no date column  

**Correct Answer:** B  
**Explanation:** Daily stock prices are time series — shuffling causes future leakage. Options A, C, and D are tabular data where row order does not carry time meaning; random splits are acceptable there.

---

### Q5 (Moderate)
Daily sales for three consecutive days are **₹200**, **₹220**, and **₹215**. What is the **3-day rolling mean** for the **third day** (including that day and the two before it)?

A. ₹205  
B. ₹211.67  
C. ₹220  
D. ₹635  

**Correct Answer:** B  
**Explanation:** Rolling mean for day 3 = (200 + 220 + 215) / 3 = 635 / 3 ≈ **211.67**. ₹205 (A) is a wrong average. ₹220 (C) is only day 2's value. ₹635 (D) is the sum, not the mean.

---

### Q6 (Moderate)
Priya has an **ordered** daily sales DataFrame. She runs:

```python
train_test_split(X, y, test_size=0.2, shuffle=False)
```

What does the **test set** contain?

A. A random 20% of rows picked from anywhere in the timeline  
B. The **last 20%** of rows in time order  
C. The **first 20%** of rows in time order  
D. Only rows where sales increased compared to the previous day  

**Correct Answer:** B  
**Explanation:** With `shuffle=False`, sklearn keeps row order; `test_size=0.2` takes the final 20% as test — the future holdout. Random 20% (A) needs default `shuffle=True`. First 20% (C) would be train, not test. Sales increases (D) are not how the split works.

---

## MSQs (Multiple Correct)

### Q7 (Moderate)
Which statements about **lag features** built with `.shift()` on a daily `sales` column are correct?

A. `lag_1 = sales.shift(1)` puts **yesterday's** sales on today's row.  
B. The **first row** will typically show **NaN** for `lag_1`.  
C. Creating lag features removes the need for any train/test split.  
D. `sales.shift(7)` can help the model see **what happened one week ago**.  

**Correct Answers:** A, B, D  
**Explanation:** `.shift(1)` pulls the previous row's value down (A). Row 1 has no prior day, so NaN is expected (B). Lags are features only — you still need a chronological split (C is false). Weekly seasonality hints come from shift(7) (D).

---

### Q8 (Moderate)
A team forecasts **monthly electricity use** for a city. Which practices help avoid **future leakage**?

A. Sort the data by date before splitting.  
B. Pass `shuffle=False` in `train_test_split`.  
C. Train on future months and test on past months.  
D. Compute MAPE only on the **chronological holdout** test period.  

**Correct Answers:** A, B, D  
**Explanation:** Past → future split with no shuffle prevents the model from seeing tomorrow during training (A, B). Evaluating on the honest future holdout (D) matches real deployment. Training on future and testing on past (C) is backwards and leaky.

---

### Q9 (Hard)
A retail analyst compares two forecast models on the **same chronological test split**. Which statements are **valid**?

A. **MAPE** expresses error as a percentage of actual values, which helps compare forecasts across products with different scales.  
B. **MAPE** is reliable when many test **actual values are exactly zero**.  
C. A model with **higher test R²** on that split will **often** show **lower MAPE** than a weaker model.  
D. **MAE** and **RMSE** from regression evaluation also apply to time-series forecasting tasks.  

**Correct Answers:** A, C, D  
**Explanation:** MAPE is scale-free in percentage terms (A). MAPE divides by actual — it breaks when actual ≈ 0 (B is false). Better fit (higher R²) usually means smaller errors and lower MAPE (C). Forecasting is regression on numeric targets, so MAE/RMSE apply (D).

---

### Q10 (Hard)
An analyst builds a **daily sales forecast** using lag and rolling features. Which steps belong in a **sound pipeline**?

A. Create `lag_1` and `rolling_mean_7`, then `dropna()` before fitting a model.  
B. Randomly shuffle all rows, then use the first 80% as train and last 20% as test without `shuffle=False`.  
C. Fit **LinearRegression** and **GradientBoostingRegressor** on the **same chronological train split** and compare test **R²** (and/or MAPE).  
D. Use `train_test_split(..., shuffle=True)` on dated sales data because it balances the classes.  

**Correct Answers:** A, C  
**Explanation:** Engineer features, drop early NaN rows, then model (A). Compare LR and GB on the same honest split (C). Shuffling dated sales (B, D) causes future leakage — there are no "classes" to balance in regression (D).

---
