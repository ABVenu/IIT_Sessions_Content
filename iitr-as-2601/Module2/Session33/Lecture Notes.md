# Time Series: Understanding Data That Changes Over Time

## What You Will Learn in This Session

In the previous session, we explored **Unsupervised Learning** — a world where the machine finds patterns in data all on its own, without labeled answers. We learned how **K-Means Clustering** groups similar data points into buckets, and how **PCA** helps us shrink many features down to fewer dimensions.

Both of those techniques worked on data where the **order of rows didn't matter**. But not all data works like this.

In this session, we explore a completely different type of data — **data where time matters**. This is called **Time Series data**, and it powers everything from stock market predictions to weather forecasts to sales planning. You will learn:

- What time series data is and why it is different from regular data
- What **Trend** and **Seasonality** mean and how to spot them
- Why you cannot use a regular train-test split for time series data — and what to use instead
- How **Rolling Windows** help the model learn from recent patterns
- How to properly **evaluate** a time series model

---

## Introduction to Time Series Data

Imagine you are tracking your own weight every Monday morning for one year. You write down: "Week 1 — 72 kg, Week 2 — 71.5 kg, Week 3 — 72.2 kg..." and so on. At the end of the year, you have 52 data points — one for each week.

Now here's the important question: **does the order of these measurements matter?** Absolutely yes. Week 5 comes after Week 4. You cannot shuffle these around and still make sense of the data.

**Official Definition:** A **Time Series** is a sequence of data points collected or recorded at successive points in time, usually at equal intervals (hourly, daily, weekly, monthly).

**In Simple Words:** It is just a list of numbers arranged in time order — where the "when" is just as important as the "what."

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

- Each row is one day's temperature reading, in strict date order.
- If you randomly shuffled these rows, the date–temperature relationship would be lost and the data would be useless for forecasting.
- The **date column is always the anchor** that gives the data its time-series nature.

![Time-ordered points follow a meaningful sequence along the timeline; shuffling the same values destroys the story the data tells](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-time-order-vs-shuffle.png)

---

### Why Is Time Series Different From Regular Data?

In a regular dataset (like a list of students with marks and attendance), each row is **independent**. Row 5 has nothing to do with Row 4. You can shuffle rows and still train a model perfectly well.

In time series data, **each row depends on what came before it**.

- Yesterday's sales affect today's stock orders.
- Last week's temperature affects this week's rainfall.
- Last month's website traffic affects this month's server capacity planning.

This dependency on time is what makes time series a completely separate topic in machine learning. The techniques, the splits, the evaluation — everything changes.

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
| 2024-01-05 | **Friday**    | **210** |
| 2024-01-06 | **Saturday**  | **225** |
| 2024-01-07 | Sunday    | 165 |
| 2024-01-08 | Monday    | 119 |
| 2024-01-12 | **Friday**    | **208** |
| 2024-01-13 | **Saturday**  | **220** |

- See how **Fridays and Saturdays always spike** to 200+ while weekdays stay around 115–125?
- This same pattern repeats **every single week** — that is weekly seasonality with a period of 7 days.
- A model that understands this seasonality will know: "It's Friday → expect around 210 orders today."

---

### Trend vs. Seasonality: The Core Difference

| Feature | Trend | Seasonality |
|---|---|---|
| Definition | Long-term direction of data | Repeating pattern at fixed intervals |
| Repeats? | No — it is a continuous movement | Yes — at fixed periods |
| Duration | Months or years | Could be daily, weekly, yearly |
| Example | Rising smartphone sales over 10 years | Ice cream sales spiking every summer |
| Looks like in a graph | A sloping line going up or down | Waves or peaks repeating at the same time each cycle |

- A real-world time series usually has **both** trend and seasonality happening together.
- For example, an e-commerce app might have a **long-term upward trend** (more users every year) **plus** a **seasonal pattern** (massive spike every October during the festive sale).

> **Note:** Beyond trend and seasonality, time series data also contains **Noise** (random, unpredictable fluctuations) and sometimes **Cyclical Patterns** (long-term waves without a fixed schedule, like economic boom-bust cycles). For most problems, focusing on trend and seasonality is sufficient.

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
- In a **random split**, Sep might land in the training set and Feb in the test set — which makes no logical sense for forecasting.

---

### Walk-Forward Validation (A Quick Note)

A more advanced technique called **Walk-Forward Validation** takes chronological splitting further — it progressively expands the training window over time and tests on the very next period at each step (train on months 1–6, test on month 7; then train on 1–7, test on month 8; and so on). This gives multiple evaluation results instead of just one, making the assessment more reliable. You will encounter this in more advanced time series work — for now, chronological split is the foundation to master.

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

### How Rolling Windows Are Implemented in Python

```python
import pandas as pd

# Sample daily sales data
data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'sales': [200, 220, 215, 230, 250, 245, 260, 270, 265, 280]
}

df = pd.DataFrame(data)
df = df.set_index('date')

# Create a rolling window of size 3 (last 3 days)
df['rolling_mean_3'] = df['sales'].rolling(window=3).mean()
df['rolling_std_3']  = df['sales'].rolling(window=3).std()
df['rolling_max_3']  = df['sales'].rolling(window=3).max()

print(df)
```

**How the code works:**
- `pd.date_range()` generates 10 consecutive dates automatically.
- `set_index('date')` makes the date column the row label (index) — standard practice for time series.
- `.rolling(window=3).mean()` tells pandas: "For each row, look at the current row and the 2 rows before it (3 total) and compute the average."
- The first 2 rows will have `NaN` (missing value) because there aren't enough past rows to fill the 3-day window yet. This is expected behavior.
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

- The first 2 rows show **NaN** for all rolling columns — expected, as we need at least 3 rows of history.
- From Row 3 onwards, the rolling mean is the average of that row and the 2 rows before it. For Jan 3: (200 + 220 + 215) / 3 = **211.67**.

How do you decide the size of the window?
- **Small window (3–7 days):** Captures very recent short-term behavior. Reacts quickly but is more sensitive to noise.
- **Large window (30–90 days):** Captures long-term trends. More stable but slower to react to sudden changes.
- In practice, you often create **multiple window sizes** and let the model decide which time scale matters most.

---

### Lag Features — A Close Cousin of Rolling Windows

A related concept is **Lag Features** — instead of computing a window average, you simply bring a past value forward as a new column.

```python
df['lag_1'] = df['sales'].shift(1)   # Yesterday's sales
df['lag_7'] = df['sales'].shift(7)   # Sales from 7 days ago
```

- `.shift(1)` moves all values down by 1 row — so each row now knows what yesterday's value was.
- `lag_7` tells the model: "Here is what happened exactly one week ago." This is extremely powerful for capturing weekly patterns.
- Rows at the start will have `NaN` (no history yet) — these are removed with `dropna()` before training.

---

## Evaluation for Time Series

You have built your time series model. Now how do you measure how good or bad it is?

You already learned **MAE** and **RMSE** in the previous session on *Regression: Regularization and Evaluation*. Both apply here too — MAE gives you the average absolute error, RMSE penalises large errors more heavily. For time series forecasting (which is a regression problem), these same metrics work exactly the same way.

However, there is one important new metric that is especially useful for time series: **MAPE**.

---

### MAPE — Mean Absolute Percentage Error

**Official Definition:** **MAPE (Mean Absolute Percentage Error)** expresses the prediction error as a **percentage of the actual value** rather than in absolute units.

**In Simple Words:** Instead of saying "I was off by ₹20," MAPE says "I was off by 5%." This makes it easy to compare models across different datasets or products with different scales.

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
- This is much more meaningful than saying "MAE = 12 rupees" when you don't know whether that is a lot or a little for your use case.

```python
import numpy as np

actual_arr    = np.array([100, 200, 150, 300, 250])
predicted_arr = np.array([110, 190, 160, 280, 260])

mape = np.mean(np.abs((actual_arr - predicted_arr) / actual_arr)) * 100
print(f"MAPE: {mape:.2f}%")
```

**How the code works:**
- `actual_arr - predicted_arr` gives us the raw error for each point.
- `np.abs(...)` removes the negative sign (we care about magnitude, not direction).
- Dividing by `actual_arr` converts each error to a fraction of the actual value.
- Multiplying by 100 converts it to a percentage, and `np.mean(...)` averages them all.

**Watch out:** MAPE breaks down when actual values are 0 or very close to 0 — you cannot divide by zero. In such cases, use MAE instead.

---

### Baseline Models: Your Starting Point for Evaluation

Before you build a complex machine learning model, always start with a **baseline model** — the simplest possible prediction strategy. It answers: "Can my fancy model at least beat this naive approach?"

Common baselines for time series:

- **Naive Forecast:** Predict that tomorrow's value = today's value. Surprisingly hard to beat!
- **Seasonal Naive:** Predict that tomorrow's value = the same day last week (or last year). Great for strongly seasonal data.
- **Rolling Mean Forecast:** Predict tomorrow's value as the rolling average of the last N days.

If your complex model cannot beat the naive forecast, something is wrong with your approach. Always check this first.

---

### Choosing the Right Metric

| Metric | Best When | Weakness |
|---|---|---|
| MAE *(covered previously)* | All errors are equally important; easy interpretation | Does not penalise big outliers |
| RMSE *(covered previously)* | Large errors are very costly | Sensitive to outliers |
| MAPE | Comparing accuracy across products of different scales | Fails when actual = 0 |

In practice, report **more than one metric** — for example, both MAE and MAPE — to get a complete picture of your model's performance.

---

## Key Takeaways

- **Time Series data is order-dependent** — the sequence of records matters. Shuffling destroys the meaning of the data.
- **Trend** is the long-term upward or downward direction; **Seasonality** is the repeating pattern at fixed intervals. Real data usually has both.
- **Never use random train-test split** for time series. Always split chronologically — older data trains, newer data tests.
- **Rolling Windows** are your primary feature engineering tool — they convert raw time-ordered values into meaningful statistics (mean, std, max) that capture recent history for the model.
- **MAPE** is the go-to new metric for time series — it expresses error as a percentage, making it scale-independent. MAE and RMSE from *Regression: Regularization and Evaluation* apply here too.
- Always compare your model against a simple **baseline** (like Naive Forecast) before declaring success.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | What It Means |
|---|---|
| **Time Series** | Data recorded at successive, ordered time points |
| **Trend** | Long-term upward or downward direction in data |
| **Seasonality** | Repeating pattern at fixed, predictable intervals |
| **Data Leakage** | When future information accidentally leaks into model training |
| **Chronological Split** | Splitting data in time order (past = train, future = test) |
| **Walk-Forward Validation** | Advanced technique: expands training window over time with sequential test steps |
| **Rolling Window** | A fixed-size window that slides through time to compute statistics |
| **Lag Feature** | A past value used as a new feature (e.g., yesterday's sales) |
| **MAPE** | Mean Absolute Percentage Error — error expressed as a percentage |
| **Naive Forecast** | Predict next value = current value; simplest baseline |
| `pd.date_range()` | Generates a sequence of dates in pandas |
| `df.set_index('date')` | Sets the date column as the DataFrame index |
| `.rolling(window=N).mean()` | Computes the N-step rolling average |
| `.shift(N)` | Shifts values by N steps to create lag features |
