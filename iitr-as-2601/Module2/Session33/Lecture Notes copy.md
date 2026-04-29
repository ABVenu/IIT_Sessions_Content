# Time Series: Understanding Data That Changes Over Time

## What You Will Learn in This Session

In the previous session, we explored **Unsupervised Learning** — a world where the machine finds patterns in data all on its own, without labeled answers. We learned how **K-Means Clustering** groups similar data points into buckets, and how **PCA (Principal Component Analysis)** helps us shrink many features down to fewer dimensions so we can visualize complex data in 2D.

Both of those techniques worked on data where the **order of rows didn't matter** — a customer record from January or December was treated the same way. But not all data works like this.

In this session, we are going to explore a completely different type of data — **data where time matters**. This is called **Time Series data**, and it powers everything from stock market predictions to weather forecasts to sales planning. You will learn:

- What time series data is and why it is different from regular data
- What **Trend** and **Seasonality** mean and how to spot them
- Why you cannot use regular train-test split for time series data — and what to use instead
- How **Rolling Windows** help the model learn from recent patterns
- How to properly **evaluate** a time series model

---

## Introduction to Time Series Data

Imagine you are tracking your own weight every Monday morning for one year. You write down: "Week 1 — 72 kg, Week 2 — 71.5 kg, Week 3 — 72.2 kg..." and so on. At the end of the year, you have 52 data points — one for each week.

Now here's the important question: **does the order of these measurements matter?** Absolutely yes. Week 5 comes after Week 4. You cannot shuffle these around and still make sense of the data.

**Official Definition:** A **Time Series** is a sequence of data points collected or recorded at successive points in time, usually at equal intervals (hourly, daily, weekly, monthly).

**In Simple Words:** It is just a list of numbers or measurements arranged in time order — where the "when" is just as important as the "what."

**Real-Life Example:** Think of a temperature chart at your local weather station. Each hour, the device records the temperature. Over a day, you get 24 readings. Over a year, you get 8,760 readings. That entire sequence — in order — is a time series. If you shuffle those readings randomly, the data becomes meaningless.

**Sample Dataset — What Time Series Data Looks Like:**

| Date       | City Temperature (°C) |
|---|---|
| 2024-01-01 | 18.2 |
| 2024-01-02 | 17.8 |
| 2024-01-03 | 19.1 |
| 2024-01-04 | 20.5 |
| 2024-01-05 | 21.0 |
| 2024-01-06 | 19.7 |
| 2024-01-07 | 18.4 |

- Each row is one day's temperature reading. The rows are in strict date order — this is what "time-ordered" means.
- If you randomly shuffled these rows, the date–temperature relationship would be lost and the data would be useless for forecasting.
- In real datasets, you may have many more columns (humidity, wind speed, rainfall) — but the **date column is always the anchor** that gives the data its time-series nature.

![Time-ordered points follow a meaningful sequence along the timeline; shuffling the same values destroys the story the data tells](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-time-order-vs-shuffle.png)

---

### Why Is Time Series Different From Regular Data?

In a regular dataset (like a list of students with marks and attendance), each row is **independent**. Row 5 has nothing to do with Row 4. You can shuffle rows and still train a model perfectly well.

In time series data, **each row depends on what came before it**.

- Yesterday's sales affect today's stock orders.
- Last week's temperature affects this week's rainfall.
- Last month's website traffic affects this month's server capacity planning.

This dependency on time is what makes time series a completely separate topic in machine learning. The techniques, the splits, the evaluation — everything changes. Let us explore each piece, step by step.

---

## Trend vs. Seasonality

Before building any time series model, you must first understand the two most important patterns hiding inside your data: **Trend** and **Seasonality**. These two are like the DNA of a time series — once you understand them, you understand your data.

![Trend is the long-term direction; seasonality is the repeating wiggle on top—real series often have both at once](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-trend-vs-seasonality.png)

---

### What Is a Trend?

**Official Definition:** A **Trend** is the long-term direction or movement in time series data — either consistently going up, going down, or staying flat over a long period.

**In Simple Words:** Trend is the big picture direction. Is the data generally increasing over months or years? Or is it falling? That general movement — ignoring daily ups and downs — is the trend.

**Real-Life Example:** Think about the number of smartphone users in India from 2010 to 2024. Every year, the number grows. There are minor dips or flat periods, but the overall direction is clearly **upward**. That is a **positive trend**. On the other hand, the number of people buying print newspapers has been going **downward** year after year. That is a **negative trend**.

Key points about trends:
- A trend does **not** mean the data goes up every single day. There will be small drops even in an upward trend.
- A trend is about the **overall direction** over a long period — months or years.
- **Flat trend** means no consistent direction — the data hovers around the same value.

**Sample Dataset — Spotting a Trend (Monthly Smartphone Sales in India):**

| Month    | Units Sold (Lakhs) | Observation |
|---|---|---|
| Jan 2022 | 42 | — |
| Feb 2022 | 39 | Small dip — but trend still upward |
| Mar 2022 | 45 | Recovering |
| Jun 2022 | 51 | Growing |
| Sep 2022 | 55 | Growing |
| Dec 2022 | 60 | Year-end high |
| Jun 2023 | 67 | Still climbing |
| Dec 2023 | 78 | Clear upward trend overall |

- Notice that February had a dip to 39 — but the **overall direction from 42 (Jan 2022) to 78 (Dec 2023) is clearly upward**. That is the trend.
- Month-to-month ups and downs are just noise on top of the trend. The trend is the big picture movement.

---

### What Is Seasonality?

**Official Definition:** **Seasonality** refers to regular, repeating patterns in time series data that occur at fixed, known intervals — like daily, weekly, monthly, or yearly cycles.

**In Simple Words:** Seasonality is when the same pattern repeats itself over and over at predictable intervals. It is like a pattern that is "on schedule."

**Real-Life Example:** Think about ice cream sales in a city. Every summer (April–June), sales shoot up. Every winter (November–January), sales drop. This pattern repeats **every single year**. That is seasonality — a predictable cycle driven by the seasons. Similarly, a pizza delivery app gets more orders every Friday night. That is **weekly seasonality** — a cycle that repeats every 7 days.

Key points about seasonality:
- Seasonality always has a **fixed period** — the pattern repeats after a known interval (7 days, 12 months, etc.).
- It is **not random**. You can predict when the spike or dip will happen.
- Multiple seasonal cycles can exist at the same time — for example, a retail store may have both **weekly patterns** (weekends are busier) and **yearly patterns** (Diwali and Christmas spikes).

**Sample Dataset — Spotting Seasonality (Pizza Delivery Orders by Day of Week):**

| Date       | Day       | Orders |
|---|---|---|
| 2024-01-01 | Monday    | 120 |
| 2024-01-02 | Tuesday   | 115 |
| 2024-01-03 | Wednesday | 118 |
| 2024-01-04 | Thursday  | 122 |
| 2024-01-05 | **Friday**    | **210** |
| 2024-01-06 | **Saturday**  | **225** |
| 2024-01-07 | Sunday    | 165 |
| 2024-01-08 | Monday    | 119 |
| 2024-01-09 | Tuesday   | 116 |
| 2024-01-12 | **Friday**    | **208** |
| 2024-01-13 | **Saturday**  | **220** |

- See how **Fridays and Saturdays always spike** to 200+ while weekdays stay around 115–125?
- This same pattern repeats **every single week** — that is weekly seasonality with a period of 7 days.
- A model that understands this seasonality will know: "It's Friday → expect around 210 orders today."

---

### Trend vs. Seasonality: The Core Difference

Let us place these two side by side to make the distinction crystal clear:

| Feature | Trend | Seasonality |
|---|---|---|
| Definition | Long-term direction of data | Repeating pattern at fixed intervals |
| Repeats? | No — it is a continuous movement | Yes — at fixed periods |
| Duration | Months or years | Could be daily, weekly, yearly |
| Example | Rising smartphone sales over 10 years | Ice cream sales spiking every summer |
| Looks like in a graph | A sloping line going up or down | Waves or peaks repeating at the same time each cycle |

- A real-world time series usually has **both** trend and seasonality happening together.
- For example, an e-commerce app might have a **long-term upward trend** (more users every year) **plus** a **seasonal pattern** (massive spike every October during the festive sale).
- Understanding which part of your data is trend and which is seasonality is called **Time Series Decomposition** — a technique used before modeling.

---

### Other Components: Noise and Cyclical Patterns

Beyond trend and seasonality, two more components appear in time series data:

- **Noise (Residuals):** The random, unpredictable fluctuations in data that cannot be explained by trend or seasonality. Think of this as the "random jitter" — a spike in sales because of an unexpected viral tweet, for example.
- **Cyclical Patterns:** Long-term waves that do **not** have a fixed period — like economic boom-and-bust cycles that might last 5 years or 10 years. Unlike seasonality, these are not on a strict schedule.

For most beginner problems, you will focus on **Trend + Seasonality + Noise** as the three building blocks.

---

## Time-Aware Splits

Now that you understand the nature of time series data, let us talk about the most common mistake beginners make — using the **wrong kind of train-test split**.

---

### Why Regular Random Split Fails for Time Series

In regular machine learning (like predicting house prices), you randomly shuffle the dataset and put 80% in training and 20% in testing. This works perfectly because each row is independent.

But in time series, doing a **random split is a serious mistake**. Here is why:

Imagine you want to predict tomorrow's stock price. In a random split, some of tomorrow's data might accidentally end up in your training set. Your model "sees the future" while training. When you then test it, it scores very high — but only because it cheated. In the real world, this model will fail completely.

**This problem has a special name: Data Leakage — specifically "Future Leakage."**

- **Official Definition:** **Data Leakage** in time series happens when future data points are used to train the model, giving it unfair information it would never have in a real deployment.
- **In Simple Words:** You are letting the model "peek at the answer sheet" during study time. It passes the exam but fails in real life.
- **Real-Life Example:** Imagine a student who is given the exact exam questions to practice the night before. They score 100%. But put them in a real exam with different questions, and they score 40%. The training was fake. The same thing happens to a model trained with a random split on time series data.

---

### The Correct Way: Chronological Split

The correct approach is to **always split time series data chronologically** — earlier data goes into training, later data goes into testing. The training set must always be "in the past" relative to the test set.

**How it works:**
- Sort your data by time (oldest first).
- Take the **first 80%** of time points as your **training set**.
- Take the **last 20%** of time points as your **test set**.
- The model is trained on past data and tested on future data — exactly how it will be used in real life.

Think of it as this rule: **the model can only learn from the past, never from the future.**

![Random splits mix past and future between train and test, causing future leakage; a chronological split keeps all training points before the test period](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-chronological-vs-random-split.png)

**Sample Dataset — Chronological Split Visualised (10 months of sales):**

| Month | Sales (₹ Lakhs) | Split Assignment |
|---|---|---|
| Jan 2024 | 80 | **Train** |
| Feb 2024 | 85 | **Train** |
| Mar 2024 | 90 | **Train** |
| Apr 2024 | 88 | **Train** |
| May 2024 | 95 | **Train** |
| Jun 2024 | 100 | **Train** |
| Jul 2024 | 102 | **Train** |
| Aug 2024 | 105 | **Train** (80% cutoff here) |
| Sep 2024 | 110 | **Test** |
| Oct 2024 | 115 | **Test** |

- The model **learns from Jan–Aug** (the past) and is **evaluated on Sep–Oct** (the future).
- Notice that Sep and Oct were never shown to the model during training — this is the correct way to simulate real forecasting.
- In a **random split**, Sep might land in the training set and Feb in the test set — which makes no logical sense for forecasting.

---

### Walk-Forward Validation (Time Series Cross-Validation)

A more advanced and powerful version of the chronological split is called **Walk-Forward Validation** (also called **Rolling Origin Cross-Validation**).

**Official Definition:** Walk-Forward Validation is a technique where the training window is progressively expanded over time, and the model is tested on the immediate next period at each step.

**In Simple Words:** Imagine you are a weather forecaster. In January, you train on data from 2020–2022 and predict February. In February, you add that month's data to training and predict March. You keep "walking forward" in time, always training on everything you know so far and predicting the next unknown period.

**The steps look like this:**

- **Step 1:** Train on months 1–6, test on month 7.
- **Step 2:** Train on months 1–7, test on month 8.
- **Step 3:** Train on months 1–8, test on month 9.
- **Step 4:** Train on months 1–9, test on month 10.
- Continue until you reach the end of the data.

![Walk-forward validation: the training window grows over time and each step tests on the very next future slice—no peeking ahead](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-walk-forward-validation.png)

**Why this is better:**
- You get multiple evaluation results, not just one — making your assessment more reliable.
- The model is always trained on data that "looks like" real deployment conditions.
- You can see whether your model's accuracy is improving, staying stable, or degrading as time goes on.

| Split Type | Good for Time Series? | Reason |
|---|---|---|
| Random Split | No | Causes future leakage |
| Chronological Split | Yes | Respects time order |
| Walk-Forward Validation | Best | Multiple evaluations, no leakage |

---

## Rolling Windows

Now let us talk about **Rolling Windows** — one of the most powerful and commonly used techniques in time series feature engineering.

---

### What Is a Rolling Window?

**Official Definition:** A **Rolling Window** (also called a **Sliding Window**) is a fixed-size window that moves through time series data, one step at a time, to compute statistics (like mean or standard deviation) over that window.

**In Simple Words:** Imagine you are tracking your daily running distance. Instead of looking at each day in isolation, you want to know: "What was my average distance over the last 7 days?" Every day, you calculate this average using the most recent 7 days — dropping the oldest day and adding the newest one. That moving calculation is a rolling window.

**Real-Life Example:** A stock market analyst says, "Let us look at the 30-day moving average of this stock." Every day, they calculate the average price of the last 30 days. As a new day's price comes in, the oldest day's price drops out. This "window" rolls forward in time — hence, **Rolling Window**.

![A rolling window of fixed size slides one step at a time; each position computes stats (like the mean) over only the values inside the frame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-rolling-window.png)

---

### Why Do We Use Rolling Windows?

Raw time series data is often very noisy. Day-to-day values jump up and down, making it hard for a model to learn the real underlying pattern. Rolling windows help in two ways:

- **Smoothing the noise:** Instead of a jagged, spiky line, you get a smooth curve that clearly shows the actual trend.
- **Creating features for the model:** Instead of just saying "yesterday's value," you give the model richer information — "what was the average of the last 7 days? The last 30 days? The standard deviation of the last 14 days?"

These rolling statistics become **new features** (new columns in your dataset) that your machine learning model can use to understand the recent history of the time series.

---

### Common Rolling Window Features

Here are the most commonly computed rolling window statistics:

- **Rolling Mean (Moving Average):** Average value over the last N time steps. Smooths out noise and shows the trend direction.
- **Rolling Standard Deviation:** How much the values varied over the last N time steps. High std = volatile/unstable period; Low std = stable period.
- **Rolling Min / Max:** The minimum or maximum value in the last N steps. Useful for capturing extreme behavior.
- **Rolling Sum:** Total value over the last N steps. Used in sales forecasting to measure cumulative recent activity.

---

### How Rolling Windows Are Implemented in Python

```python
import pandas as pd  # Import the pandas library for data handling

# Sample daily sales data
data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),  # Create 10 dates starting Jan 1
    'sales': [200, 220, 215, 230, 250, 245, 260, 270, 265, 280]       # Daily sales numbers
}

df = pd.DataFrame(data)          # Create a DataFrame from the dictionary
df = df.set_index('date')        # Set the date column as the index of the DataFrame

# Create a rolling window of size 3 (last 3 days)
df['rolling_mean_3'] = df['sales'].rolling(window=3).mean()   # Calculate 3-day rolling average
df['rolling_std_3']  = df['sales'].rolling(window=3).std()    # Calculate 3-day rolling std deviation
df['rolling_max_3']  = df['sales'].rolling(window=3).max()    # Calculate 3-day rolling maximum

print(df)  # Print the DataFrame to see the new rolling feature columns
```

**How the code works:**
- We first create a small DataFrame with 10 days of sales data.
- `pd.date_range()` generates 10 consecutive dates automatically — so we don't have to type them manually.
- `set_index('date')` makes the date column the row label (index), which is standard practice for time series.
- `.rolling(window=3).mean()` tells pandas: "For each row, look at the current row and the 2 rows before it (3 total) and compute the average."
- The first 2 rows will have `NaN` (missing value) for the rolling mean because there aren't enough past rows to fill the 3-day window yet. This is expected behavior.
- Each new column (`rolling_mean_3`, `rolling_std_3`, `rolling_max_3`) becomes a **feature** that a machine learning model can use.

**Sample Output — What the DataFrame Looks Like After Rolling Features:**

| date       | sales | rolling_mean_3 | rolling_std_3 | rolling_max_3 |
|---|---|---|---|---|
| 2024-01-01 | 200 | NaN | NaN | NaN |
| 2024-01-02 | 220 | NaN | NaN | NaN |
| 2024-01-03 | 215 | **211.67** | **10.41** | **220** |
| 2024-01-04 | 230 | **221.67** | **7.64** | **230** |
| 2024-01-05 | 250 | **231.67** | **17.56** | **250** |
| 2024-01-06 | 245 | **241.67** | **10.41** | **250** |
| 2024-01-07 | 260 | **251.67** | **7.64** | **260** |
| 2024-01-08 | 270 | **258.33** | **12.58** | **270** |
| 2024-01-09 | 265 | **265.00** | **5.00** | **270** |
| 2024-01-10 | 280 | **271.67** | **7.64** | **280** |

- The first 2 rows show **NaN** for all rolling columns — this is expected. We need at least 3 rows of history to fill a window of size 3.
- From Row 3 onwards, the rolling mean is the average of that row and the 2 rows before it. For Jan 3: (200 + 220 + 215) / 3 = **211.67**.
- The `rolling_max_3` for Jan 6 is **250** — because among Jan 4, 5, 6 (values 230, 250, 245), the maximum is 250.

How do you decide the size of the window? This is a judgment call based on the data:

- **Small window (3–7 days):** Captures very recent short-term behavior. Reacts quickly to new changes but is more sensitive to noise.
- **Large window (30–90 days):** Captures long-term trends and seasonal patterns. More stable but slower to react to sudden changes.
- In practice, you often create **multiple window sizes** (e.g., 7-day, 14-day, 30-day) and provide all of them as features to the model. The model then learns which time scale matters most.

---

### Lag Features — The Close Cousin of Rolling Windows

A concept closely related to rolling windows is **Lag Features**.

**Official Definition:** A **Lag Feature** is when you shift a column in time so that the value from N steps ago becomes a new feature for the current row.

**In Simple Words:** Instead of computing a window average, you simply say: "What was the sales value 1 day ago? 7 days ago? 30 days ago?" Those past values become new columns in your dataset.

```python
df['lag_1'] = df['sales'].shift(1)   # Yesterday's sales becomes a new feature column
df['lag_7'] = df['sales'].shift(7)   # Sales from 7 days ago becomes a new feature column
```

**How the code works:**
- `.shift(1)` moves all values down by 1 row — so row 2 gets row 1's value, row 3 gets row 2's value, etc.
- Row 1 will have `NaN` because there is no "day before Day 1."
- `lag_1` tells the model: "Here is what happened yesterday." `lag_7` tells it: "Here is what happened exactly one week ago." This is extremely powerful for capturing weekly patterns.

**Sample Output — What Lag Features Look Like:**

| date       | sales | lag_1 | lag_7 |
|---|---|---|---|
| 2024-01-01 | 200 | NaN | NaN |
| 2024-01-02 | 220 | 200 | NaN |
| 2024-01-03 | 215 | 220 | NaN |
| 2024-01-04 | 230 | 215 | NaN |
| 2024-01-05 | 250 | 230 | NaN |
| 2024-01-06 | 245 | 250 | NaN |
| 2024-01-07 | 260 | 245 | NaN |
| 2024-01-08 | 270 | **260** | **200** |
| 2024-01-09 | 265 | **270** | **220** |
| 2024-01-10 | 280 | **265** | **215** |

- `lag_1` for Jan 8 is **260** — that is exactly Jan 7's sales (one day ago).
- `lag_7` for Jan 8 is **200** — that is exactly Jan 1's sales (seven days ago).
- The first 7 rows have NaN in `lag_7` because there is no "7 days ago" data for those early dates. These rows are dropped with `dropna()` before training.

---

## Evaluation for Time Series

You have built your time series model. Now how do you measure how good or bad it is? This is where **time series evaluation metrics** come in.

---

### Why Standard Classification Metrics Don't Apply

In regular classification problems, we use accuracy, precision, recall. In time series, we are almost always doing **forecasting (regression)** — predicting a continuous value like temperature, sales, or price. So we use regression-style error metrics.

The key question is: **how far off were our predictions from the actual values?**

---

### MAE — Mean Absolute Error

**Official Definition:** **MAE (Mean Absolute Error)** is the average of the absolute differences between the predicted values and the actual values.

**In Simple Words:** For each prediction, calculate how much you were off (ignore + or − sign). Then average all those errors. Lower MAE = better model.

**Real-Life Example:** You predicted it would rain 5mm today. It actually rained 8mm. Your error is 3mm. Do this for 30 days and average all the daily errors — that is the MAE.

**Formula:** `MAE = Average of |Actual - Predicted|`

- **Easy to understand** — it is in the same unit as your data (rupees, degrees, kg).
- **Does not heavily penalize large errors** — a big miss is treated the same way as a small miss, proportionally.

**Sample Data — Step-by-Step MAE Calculation:**

| Day | Actual Sales (₹) | Predicted Sales (₹) | Absolute Error \|A - P\| |
|---|---|---|---|
| 1 | 100 | 110 | 10 |
| 2 | 200 | 190 | 10 |
| 3 | 150 | 160 | 10 |
| 4 | 300 | 280 | 20 |
| 5 | 250 | 260 | 10 |
| **Average** | — | — | **(10+10+10+20+10) / 5 = MAE = 12** |

- All five errors are added up (10 + 10 + 10 + 20 + 10 = 60) and divided by 5 predictions.
- The final MAE is **12** — meaning on average, the model's prediction was off by ₹12 per day.

```python
from sklearn.metrics import mean_absolute_error  # Import MAE function from scikit-learn

actual    = [100, 200, 150, 300, 250]    # Actual values from the test set
predicted = [110, 190, 160, 280, 260]    # Model's predicted values

mae = mean_absolute_error(actual, predicted)  # Calculate MAE
print(f"MAE: {mae}")                          # Print the result
```

**How the code works:**
- We import `mean_absolute_error` from scikit-learn's metrics module.
- We provide the actual test values and the model's predictions.
- The function calculates the average absolute error automatically and returns a single number.

---

### RMSE — Root Mean Squared Error

**Official Definition:** **RMSE (Root Mean Squared Error)** is the square root of the average of the squared differences between predictions and actual values.

**In Simple Words:** Similar to MAE, but it **punishes big errors more severely**. If your prediction is way off on a few days, RMSE will be much higher than MAE.

**Formula:** `RMSE = √ ( Average of (Actual - Predicted)² )`

**Why use RMSE over MAE?**
- Use RMSE when **large errors are particularly bad** for your use case. For example, if you are forecasting demand for medicine — being off by 1,000 units is much worse than being off by 100 units. RMSE captures this severity.
- Use MAE when all errors are roughly equally bad regardless of size.

**Sample Data — Why RMSE Punishes Large Errors More:**

| Day | Actual | Predicted | Abs Error (MAE) | Squared Error (RMSE) |
|---|---|---|---|---|
| 1 | 100 | 110 | 10 | 100 |
| 2 | 200 | 190 | 10 | 100 |
| 3 | 150 | 160 | 10 | 100 |
| 4 | 300 | **160** | **140** | **19,600** |
| 5 | 250 | 260 | 10 | 100 |
| **Result** | — | — | MAE = **36** | RMSE = **√(20,000/5) = 63.2** |

- Day 4 had a massive error of 140 (the model predicted 160 but actual was 300).
- MAE treats this the same as other errors — it gives a result of 36.
- RMSE **squares** the 140 error → 19,600 — which dominates the average and gives a much larger RMSE of 63.2.
- This is intentional: RMSE is designed to "shout louder" when there is a big mistake.

![MAE averages absolute errors in an even-handed way; RMSE squares errors first, so a few very large mistakes inflate the score more than MAE would suggest](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-mae-vs-rmse.png)

```python
import numpy as np                              # Import numpy for the square root function
from sklearn.metrics import mean_squared_error  # Import MSE function

mse  = mean_squared_error(actual, predicted)   # Calculate Mean Squared Error first
rmse = np.sqrt(mse)                            # Take square root to get RMSE
print(f"RMSE: {rmse}")                         # Print the result
```

**How the code works:**
- `mean_squared_error` gives us the average of squared errors (MSE).
- We apply `np.sqrt()` to get RMSE — bringing the value back to the original unit of the data.
- A lower RMSE is always better, and it is always ≥ MAE for the same dataset.

---

### MAPE — Mean Absolute Percentage Error

**Official Definition:** **MAPE (Mean Absolute Percentage Error)** expresses the prediction error as a **percentage of the actual value** rather than in absolute units.

**In Simple Words:** Instead of saying "I was off by 20 units," MAPE says "I was off by 5%." This makes it easy to compare models across different datasets or products with different scales.

**Formula:** `MAPE = Average of ( |Actual - Predicted| / Actual ) × 100`

**Real-Life Example:** If you predicted ₹500 of sales and actual was ₹600, your error is ₹100 — but as a percentage, it is 100/600 = 16.7%. If you predicted ₹50,000 and actual was ₹60,000, the absolute error is ₹10,000 but the percentage error is still 16.7%. MAPE lets you compare these two fairly.

**Sample Data — MAPE Step-by-Step Calculation:**

| Day | Actual (₹) | Predicted (₹) | \|A-P\| / A | % Error |
|---|---|---|---|---|
| 1 | 100 | 110 | 10/100 | 10.0% |
| 2 | 200 | 190 | 10/200 | 5.0% |
| 3 | 150 | 160 | 10/150 | 6.7% |
| 4 | 300 | 280 | 20/300 | 6.7% |
| 5 | 250 | 260 | 10/250 | 4.0% |
| **MAPE** | — | — | — | **(10+5+6.7+6.7+4) / 5 = 6.48%** |

- MAPE for this model is **6.48%** — meaning on average, predictions are off by about 6.5% of the actual value.
- This is much more meaningful than saying "MAE = 12 rupees" — because 12 rupees out of ₹100 is a 12% error, but 12 rupees out of ₹10,000 is almost nothing. MAPE accounts for this scale difference.

```python
import numpy as np  # Import numpy for array operations

actual_arr    = np.array([100, 200, 150, 300, 250])   # Convert actual values to numpy array
predicted_arr = np.array([110, 190, 160, 280, 260])   # Convert predictions to numpy array

mape = np.mean(np.abs((actual_arr - predicted_arr) / actual_arr)) * 100  # MAPE formula
print(f"MAPE: {mape:.2f}%")                                               # Print formatted result
```

**How the code works:**
- `actual_arr - predicted_arr` gives us the raw error for each point.
- `np.abs(...)` removes the negative sign (we care about magnitude, not direction).
- Dividing by `actual_arr` converts each error to a fraction of the actual value.
- Multiplying by 100 converts it to a percentage.
- `np.mean(...)` averages all those percentages to give us the final MAPE.

**Watch out:** MAPE breaks down when actual values are 0 or very close to 0 — you cannot divide by zero. In such cases, use MAE or RMSE instead.

---

### Choosing the Right Metric

| Metric | Best When | Weakness |
|---|---|---|
| MAE | All errors are equally important; easy interpretation | Does not penalize big outliers |
| RMSE | Large errors are very costly | Harder to interpret; sensitive to outliers |
| MAPE | Comparing across products of different scales | Fails when actual = 0 |

In practice, you often report **more than one metric** — for example, both MAE and MAPE — to get a complete picture of your model's performance.

---

### Baseline Models: Your Starting Point for Evaluation

Before you build a complex machine learning model, always start with a **baseline model**. A baseline is the simplest possible prediction strategy, and it tells you: "Can my fancy model at least beat this naive approach?"

Common baselines for time series:

- **Naive Forecast:** Simply predict that tomorrow's value = today's value. Surprisingly hard to beat!
- **Seasonal Naive:** Predict that tomorrow's value = the same day last week (or last year). Great for strongly seasonal data.
- **Rolling Mean Forecast:** Predict tomorrow's value as the rolling average of the last N days.

If your complex model cannot beat the naive forecast, something is wrong with your approach. Always check this first.

---

### Putting It All Together: A Simple End-to-End Time Series Workflow

Let us look at how all these concepts connect in a real workflow:

```python
import pandas as pd                             # Import pandas for data manipulation
import numpy as np                              # Import numpy for numerical operations
from sklearn.ensemble import RandomForestRegressor   # Import Random Forest model
from sklearn.metrics import mean_absolute_error      # Import MAE metric

# Step 1: Create sample time series data
dates  = pd.date_range(start='2024-01-01', periods=100, freq='D')  # Generate 100 daily dates
sales  = [200 + i * 2 + np.random.randint(-10, 10) for i in range(100)]  # Upward trend + noise
df     = pd.DataFrame({'date': dates, 'sales': sales})             # Build the DataFrame
df     = df.set_index('date')                                       # Set date as the index

# Step 2: Create rolling window features and lag features
df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()   # 7-day rolling average
df['rolling_std_7']  = df['sales'].rolling(window=7).std()    # 7-day rolling std deviation
df['lag_1']          = df['sales'].shift(1)                   # Yesterday's sales
df['lag_7']          = df['sales'].shift(7)                   # Sales from 7 days ago

df = df.dropna()  # Drop rows with NaN values (the first few rows without full window history)

# Step 3: Define features (X) and target (y)
X = df[['rolling_mean_7', 'rolling_std_7', 'lag_1', 'lag_7']]  # Features for the model
y = df['sales']                                                  # Target variable to predict

# Step 4: Chronological split (NO random shuffling)
split_index = int(len(df) * 0.8)         # 80% of the data goes to training
X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]   # Split features chronologically
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]   # Split target chronologically

# Step 5: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)  # Initialize the model
model.fit(X_train, y_train)                                        # Train on historical data

# Step 6: Predict and evaluate
predictions = model.predict(X_test)           # Generate predictions on the test (future) data
mae = mean_absolute_error(y_test, predictions)  # Calculate MAE
print(f"Test MAE: {mae:.2f}")                   # Print the mean absolute error
```

**How the code works:**
- We generate 100 days of synthetic sales data with an upward trend and some random noise.
- We create four new features: a 7-day rolling mean, a 7-day rolling standard deviation, and two lag features (lag-1 and lag-7).
- `dropna()` removes the first 7 rows where the rolling window and lag features don't have enough history.
- We split the data **chronologically** — first 80% is training data, last 20% is test data.
- We train a Random Forest Regressor — the same model you learned earlier, now applied to time series features.
- Finally, we evaluate using MAE to see how far off our predictions were on average.

---

## Key Takeaways

- **Time Series data is order-dependent** — the sequence of records matters. Shuffling destroys the meaning of the data.
- **Trend** is the long-term upward or downward direction; **Seasonality** is the repeating pattern at fixed intervals. Real data usually has both.
- **Never use random train-test split** for time series. Always split chronologically — older data trains, newer data tests. Walk-Forward Validation takes this further by testing at multiple time steps.
- **Rolling Windows** are your primary feature engineering tool — they convert raw time-ordered values into meaningful statistics (mean, std, min, max) that capture recent history for the model.
- **MAE, RMSE, and MAPE** are the core evaluation metrics for time series forecasting — each with its own strength. Always compare your model against a simple baseline before declaring success.

In the next session, we will go deeper into **advanced forecasting models** like ARIMA and explore how **deep learning** (LSTMs) can capture complex long-range dependencies in time series data — something that simple rolling windows cannot always capture.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | What It Means |
|---|---|
| **Time Series** | Data recorded at successive, ordered time points |
| **Trend** | Long-term upward or downward direction in data |
| **Seasonality** | Repeating pattern at fixed, predictable intervals |
| **Data Leakage** | When future information accidentally leaks into model training |
| **Chronological Split** | Splitting data in time order (past = train, future = test) |
| **Walk-Forward Validation** | Expanding training window over time with sequential test steps |
| **Rolling Window** | A fixed-size window that slides through time to compute statistics |
| **Lag Feature** | A past value used as a new feature (e.g., yesterday's sales) |
| **MAE** | Mean Absolute Error — average magnitude of prediction errors |
| **RMSE** | Root Mean Squared Error — penalizes large errors more heavily |
| **MAPE** | Mean Absolute Percentage Error — error expressed as a percentage |
| **Naive Forecast** | Predict next value = current value; simplest baseline |
| `pd.date_range()` | Generates a sequence of dates in pandas |
| `df.set_index('date')` | Sets the date column as the DataFrame index |
| `.rolling(window=N).mean()` | Computes the N-step rolling average |
| `.shift(N)` | Shifts values by N steps to create lag features |
| `mean_absolute_error()` | scikit-learn function to compute MAE |
| `mean_squared_error()` | scikit-learn function to compute MSE (take sqrt for RMSE) |
| `np.sqrt()` | NumPy function to compute square root |
| `RandomForestRegressor` | Ensemble model from scikit-learn used for regression/forecasting |
