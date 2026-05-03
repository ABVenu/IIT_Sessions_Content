# Assignment: Time Series — Forecasting Feature Engineering

## Subjective Assignment

**Total Questions: 1 | Type: Coding Implementation | Difficulty: Medium**

---

### Question 1 — Cafe Sales Forecasting With Rolling Features and Baselines

**Background:**

BeanBox Cafe records its daily sales in rupees. The owner wants a simple forecasting workflow that respects time order, creates useful recent-history features, and compares simple baseline forecasts before attempting any complex model.

You are the data analyst assigned to prepare this workflow in Python.

---

**Your program must complete all of the following steps:**

**Step 1 — Create the Daily Sales Dataset**  
Use the dataset generation code provided below. Do not change the dates or sales values.

**Step 2 — Prepare the Time Series**  
Convert the `date` column to datetime format and set it as the DataFrame index. Make sure the data is sorted from oldest date to newest date.

**Step 3 — Create Rolling Window Features**  
Create the following columns:
- `rolling_mean_3`: 3-day rolling average of sales
- `rolling_std_3`: 3-day rolling standard deviation of sales
- `rolling_max_3`: 3-day rolling maximum sales value

**Step 4 — Create Lag Features**  
Create the following columns:
- `lag_1`: previous day's sales
- `lag_7`: sales from 7 days ago

**Step 5 — Build a Chronological Train-Test Split**  
Use the first 80% of rows as training data and the last 20% as test data. Do not shuffle the data.

**Step 6 — Compare Two Baseline Forecasts on the Test Data**
Create these two baseline predictions:
- `naive_forecast`: predict today's sales as yesterday's sales using `lag_1`
- `rolling_mean_forecast`: predict today's sales using the 3-day rolling mean

**Step 7 — Evaluate With MAPE**
Write a function to calculate MAPE and print the MAPE for both baseline forecasts on the test set.

**Step 8 — Print the Final Output**
Print:
- The first 10 rows of the DataFrame after feature creation
- The train and test date ranges
- The MAPE values for both baseline forecasts
- A short sentence stating which baseline performed better

---

**Dataset Generation Code — Use exactly as given:**

```python
import pandas as pd

data = {
    "date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "sales": [
        200, 220, 215, 230, 250, 245, 260, 270, 265, 280,
        300, 295, 310, 330, 325, 340, 360, 355, 370, 390,
        410, 405, 420, 440, 435, 450, 470, 465, 480, 500
    ]
}

df = pd.DataFrame(data)
```

---

**Expected Output:**

1. A DataFrame preview showing rolling and lag feature columns.
2. Clear train and test date ranges based on chronological splitting.
3. MAPE values for `naive_forecast` and `rolling_mean_forecast`.
4. A printed comparison sentence identifying the better baseline.

**Submission Instructions:**
- Code all the steps mentioned above in VS Code in a single `.py` file (for example, `cafe_sales_time_series.py`)
- Run the code and verify it works correctly
- Then submit the code in the code editor/answer box in the LMS

-------------------------------------------

**Answer Explanation (Ideal Solution Walkthrough):**

This task tests the core time series workflow from the session: preserving date order, creating rolling window features, creating lag features, avoiding random train-test split, evaluating forecasts with MAPE, and comparing against simple baselines. The dataset has a clear upward trend, so the learner must make predictions using only past information.

Key solution steps:
1. Convert the `date` column to datetime and set it as the index.
2. Use `.rolling(window=3)` to create rolling mean, standard deviation, and maximum features.
3. Use `.shift(1)` and `.shift(7)` to create lag features.
4. Use a chronological 80:20 split, not a random split.
5. Evaluate `lag_1` and `rolling_mean_3` as baseline forecasts using MAPE.
6. Drop rows with missing forecast values from the test comparison before calculating MAPE.

**Complete Reference Solution:**

```python
import numpy as np
import pandas as pd

data = {
    "date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "sales": [
        200, 220, 215, 230, 250, 245, 260, 270, 265, 280,
        300, 295, 310, 330, 325, 340, 360, 355, 370, 390,
        410, 405, 420, 440, 435, 450, 470, 465, 480, 500
    ]
}

df = pd.DataFrame(data)

# Step 2: Prepare the time series
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df = df.set_index("date")

# Step 3: Rolling window features
df["rolling_mean_3"] = df["sales"].rolling(window=3).mean()
df["rolling_std_3"] = df["sales"].rolling(window=3).std()
df["rolling_max_3"] = df["sales"].rolling(window=3).max()

# Step 4: Lag features
df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)

# Step 5: Chronological train-test split
split_index = int(len(df) * 0.8)
train_df = df.iloc[:split_index]
test_df = df.iloc[split_index:].copy()

# Step 6: Baseline forecasts
test_df["naive_forecast"] = test_df["lag_1"]
test_df["rolling_mean_forecast"] = test_df["rolling_mean_3"]

# Step 7: MAPE function
def calculate_mape(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    return np.mean(np.abs((actual - predicted) / actual)) * 100

comparison_df = test_df.dropna(subset=["naive_forecast", "rolling_mean_forecast"])

naive_mape = calculate_mape(comparison_df["sales"], comparison_df["naive_forecast"])
rolling_mean_mape = calculate_mape(
    comparison_df["sales"],
    comparison_df["rolling_mean_forecast"]
)

# Step 8: Final output
print("DataFrame preview after feature creation:")
print(df.head(10))

print("\nTrain date range:")
print(train_df.index.min().date(), "to", train_df.index.max().date())

print("\nTest date range:")
print(test_df.index.min().date(), "to", test_df.index.max().date())

print(f"\nNaive Forecast MAPE: {naive_mape:.2f}%")
print(f"Rolling Mean Forecast MAPE: {rolling_mean_mape:.2f}%")

if naive_mape < rolling_mean_mape:
    print("The naive forecast performed better because it had the lower MAPE.")
elif rolling_mean_mape < naive_mape:
    print("The rolling mean forecast performed better because it had the lower MAPE.")
else:
    print("Both baseline forecasts performed equally based on MAPE.")
```

**Why this solution is correct:**
- The date column is used as the index, preserving the time-series structure.
- Rolling features are calculated only from the current and previous rows in each window.
- Lag features use past values, not future values.
- The split is chronological, so training data comes before test data.
- MAPE expresses each baseline's error as a percentage, which matches the evaluation method covered in the session.
- The baselines are simple but meaningful starting points before building a complex model.
