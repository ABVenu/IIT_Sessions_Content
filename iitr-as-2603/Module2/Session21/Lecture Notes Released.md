# Time Series: Understanding Data That Changes Over Time

## Context of This Session

In the previous session, you explored **unsupervised learning** — **K-Means** grouped similar rows without labels, and **PCA** compressed many columns into a few summary directions for plotting. In both cases, **the order of rows did not matter**. You could shuffle customer segments or medical readings and the model still made sense.

Not all data works that way. Some datasets carry a **clock** — daily sales, hourly temperature, monthly revenue. Here, **when** something happened is as important as **what** happened. This session introduces **time series** — data that moves forward in time — and the special rules for splitting, feature-building, and evaluation.

**In this session, you will:**

- Understand what makes **time series** different from regular tabular data
- Spot **trend** (long-term direction) and **seasonality** (repeating calendar patterns)
- Use **time-aware splits** instead of random shuffling — and avoid **future leakage**
- Build **rolling window** and **lag** features from recent history
- Train **linear regression** and **gradient boosting** models on engineered features
- **Evaluate** forecasts with R², MAE, RMSE, and **MAPE**, and compare model scores on a chronological test set

---

## Introduction to Time Series Data

Imagine tracking your weight every Monday for one year: Week 1 — 72 kg, Week 2 — 71.5 kg, Week 3 — 72.2 kg, and so on. **Does the order matter?** Yes. Week 5 comes after Week 4. Shuffle the weeks and the story breaks.

**Time Series:**

- **Official Definition:** A sequence of data points recorded at successive points in time, usually at equal intervals (hourly, daily, weekly, monthly).
- **In Simple Words:** A list of numbers arranged in time order — the **when** is as important as the **what**.
- **Real-Life Example:** A weather station records temperature every hour. Over a year you get 8,760 readings in order. Shuffle them randomly and the chart becomes meaningless.

| Date       | City Temperature (°C) |
|---|---|
| 2024-01-01 | 18.2 |
| 2024-01-02 | 17.8 |
| 2024-01-03 | 19.1 |
| 2024-01-04 | 20.5 |
| 2024-01-05 | 21.0 |

- Each row is one day's reading in strict date order.
- The **date column is the anchor** — it gives the data its time-series nature.
- Shuffling rows destroys the date–value relationship and makes forecasting impossible.

![Time-ordered points follow a meaningful sequence along the timeline; shuffling the same values destroys the story the data tells](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-time-order-vs-shuffle.png)

### Why Time Series Is Different

In a regular dataset (student marks, customer segments), each row is **independent**. Shuffle freely — the model still works.

In time series, **each row depends on what came before**:

- Yesterday's sales affect today's stock orders.
- Last week's temperature hints at this week's rainfall.
- Last month's traffic shapes this month's server planning.

This time dependency changes everything — how you split data, build features, and measure success.

### Quick Activity — Order Matters or Not?

Mark **T** (time series — order matters) or **R** (regular — order does not matter):

1. Daily ice cream sales for 365 days  
2. Customer segments from K-Means on purchase history  
3. Hourly electricity demand for a city  
4. Tumour measurements compressed with PCA  

**Answers:** 1 → T, 2 → R, 3 → T, 4 → R.

---

## Trend vs Seasonality

Before building any forecast model, learn the two main patterns hiding in most time series: **trend** and **seasonality**. Real data usually has **both** at once.

![Trend is the long-term direction; seasonality is the repeating wiggle on top—real series often have both at once](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-trend-vs-seasonality.png)

---

### What Is a Trend?

**Trend:**

- **Official Definition:** The long-term direction in time series data — consistently going up, going down, or staying flat over months or years.
- **In Simple Words:** The big-picture direction when you zoom out from daily ups and downs.
- **Real-Life Example:** Stock indices like **Nifty** or **Sensex** often show an upward trend over five to ten years — minor dips happen, but the long arc points up. Print newspaper sales fell steadily over decades — a **negative trend**.

| Month    | Units Sold (Lakhs) | Note |
|---|---|---|
| Jan 2022 | 42 | — |
| Feb 2022 | 39 | Small dip — trend still upward |
| Dec 2023 | 78 | Clear upward direction overall |

- February dipped to 39, but the path from 42 (Jan 2022) to 78 (Dec 2023) is clearly **upward**. That is the trend.
- Day-to-day noise sits on top; trend is the long arc.

---

### What Is Seasonality?

**Seasonality:**

- **Official Definition:** Regular, repeating patterns at fixed, known intervals — daily, weekly, monthly, or yearly cycles.
- **In Simple Words:** The same pattern repeats on a schedule — like a calendar alarm.
- **Real-Life Example:** **Air conditioner sales** peak every May–June and drop in winter — **yearly seasonality**. A pizza app gets more orders every Friday night — **weekly seasonality**. Airline demand often peaks in **July–August** and dips in **November–December**.

| Date       | Day       | Orders |
|---|---|---|
| 2024-01-03 | Wednesday | 118 |
| 2024-01-05 | **Friday**    | **210** |
| 2024-01-06 | **Saturday**  | **225** |
| 2024-01-12 | **Friday**    | **208** |

- Fridays and Saturdays spike to 200+ while weekdays stay near 115–125.
- The pattern repeats **every week** — weekly seasonality with period 7 days.

---

### Trend vs Seasonality — Side by Side

| | **Trend** | **Seasonality** |
|---|---|---|
| What it is | Long-term direction | Repeating cycle at fixed intervals |
| Repeats? | No — continuous movement | Yes — on a schedule |
| Duration | Months or years | Daily, weekly, yearly |
| Example | Rising smartphone sales over 10 years | Ice cream spikes every summer |
| On a graph | Sloping line up or down | Peaks at the same point each cycle |

- An e-commerce app might show **upward trend** (more users each year) **plus** **seasonal spikes** every festive sale season.
- Beyond these two, data also has **noise** (random jitter) and sometimes **cycles** (long waves without a fixed period). For most problems, trend and seasonality are enough to start.

### Quick Activity — Trend, Seasonality, or Both?

An ice cream cart sells **120 cups/day in January** and **480 cups/day in May** every year, but **total yearly sales rise 8%** each year.

- Which part is **seasonality**? → The Jan vs May swing (repeats every year).
- Which part is **trend**? → The 8% yearly growth (long-term direction).
- Why is a single "average daily sales" number misleading? → It hides both the summer spike and the growth path — bad for stock planning.

---

## Time-Aware Splits

You know **train/test splits** from earlier work. For time series, the split rule changes completely.

---

### Why Random Split Fails

In regular ML (house prices, customer segments), you shuffle rows and split 80/20. Rows are independent — this works fine.

For time series, a **random split is a serious mistake**:

- Imagine predicting tomorrow's stock price. A random split might put **future** prices in training. The model "sees the answer sheet" during study — high test scores, real-world failure.

**Data Leakage (Future Leakage):**

- **Official Definition:** Future data points enter training, giving the model information it would never have at deployment time.
- **In Simple Words:** Peeking at tomorrow's answers while preparing for today's exam.
- **Real-Life Example:** A student practises on the exact exam paper the night before — scores 100% in practice, 40% in the real test.

---

### The Correct Way: Chronological Split

**Always split by time** — older data trains, newer data tests.

**How it works:**

- Sort data by date (oldest first).
- First **80%** of time points → **training set**.
- Last **20%** of time points → **test set**.
- Rule: **the model learns only from the past, never from the future.**

![Random splits mix past and future between train and test, causing future leakage; a chronological split keeps all training points before the test period](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-chronological-vs-random-split.png)

| Month | Sales (₹ Lakhs) | Split |
|---|---|---|
| Jan–Aug 2024 | 80–105 | **Train** |
| Sep–Oct 2024 | 110–115 | **Test** |

- Model learns Jan–Aug, is tested on Sep–Oct — exactly how real forecasting works.
- A random split might put September in training and February in testing — nonsense for prediction.

In code, `train_test_split` **shuffles by default**. For time series you must pass **`shuffle=False`** so the first 80% stays in train and the last 20% in test — in date order.

```python
from sklearn.model_selection import train_test_split  # import split helper

# X = feature columns, y = target column (e.g. tomorrow's sales)
X_train, X_test, y_train, y_test = train_test_split(  # split 80/20
    X, y,  # features and target
    test_size=0.2,  # last 20% for testing
    shuffle=False  # keep chronological order — critical for time series
)
```

**How the code works:**

- `test_size=0.2` reserves the **last 20%** of rows for testing when `shuffle=False`.
- Without `shuffle=False`, sklearn randomises rows — that causes **future leakage** on dated data.
- Train always comes **before** test in time — same rule as the Jan–Aug / Sep–Oct table above.

### Quick Activity — Fix the Split

You randomly split **730 days** of sales 80/20. The test set has **March** days; training has **November** of the same year. What went wrong?

- **Problem:** Future (November) trained the model; past (March) was tested — backwards and leaky.
- **Fix:** Sort by date. Train on the **first ~584 days**, test on the **last ~146 days** — always past → future. Use **`shuffle=False`**.

---

## Rolling Windows

Raw daily values jump up and down — noisy and hard for a model to read. **Rolling windows** smooth the noise and create rich features from recent history.

---

### What Is a Rolling Window?

**Rolling Window (Sliding Window):**

- **Official Definition:** A fixed-size window that moves one step at a time through the series, computing statistics (mean, std, max) over the values inside the window.
- **In Simple Words:** Every day, look at the last N days and compute their average — drop the oldest day, add the newest, repeat.
- **Real-Life Example:** Stock analysts track the **30-day moving average** and **200-day moving average** — each day, average of the last 30 or 200 prices. The window **rolls** forward in time. A smaller window reacts faster; a larger window smooths more noise.

![A rolling window of fixed size slides one step at a time; each position computes stats (like the mean) over only the values inside the frame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session33/session33-rolling-window.png)

**Why use them:**

- **Smooth noise** — jagged daily spikes become a readable curve; internal fluctuations shrink so the **trend** is easier to see.
- **Create features** — instead of only "yesterday's value," give the model "average of last 7 days," "max of last 14 days," and more.

---

### Code: Rolling Windows and Lag Features

```python
import pandas as pd  # import pandas for tables and time tools

# Build 10 days of sample sales with consecutive dates
data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),  # 10 daily dates
    'sales': [200, 220, 215, 230, 250, 245, 260, 270, 265, 280]  # sales per day
}

df = pd.DataFrame(data)  # turn dict into a DataFrame table
df = df.set_index('date')  # use date as row label — standard for time series

# Rolling stats over the last 3 days (window slides one day at a time)
df['rolling_mean_3'] = df['sales'].rolling(window=3).mean()  # 3-day average
df['rolling_std_3']  = df['sales'].rolling(window=3).std()   # 3-day spread
df['rolling_max_3']  = df['sales'].rolling(window=3).max()   # 3-day peak

# Lag features — pull past values into new columns
df['lag_1'] = df['sales'].shift(1)  # yesterday's sales (t minus 1)
df['lag_2'] = df['sales'].shift(2)  # sales from 2 days ago (t minus 2)
df['lag_7'] = df['sales'].shift(7)  # sales from 7 days ago (weekly hint)

print(df)  # show table with new feature columns
```

**How the code works:**

- `pd.date_range()` builds consecutive dates automatically.
- `set_index('date')` makes the date the row index — time series convention.
- `.rolling(window=3).mean()` averages the current row plus the 2 rows before it (3 total).
- First 2 rows show `NaN` — not enough history yet. This is expected.
- `.shift(1)` moves values down one row so each day sees yesterday's sales.
- `.shift(7)` captures weekly seasonality — "what happened exactly one week ago?"
- In practice you may create **many lags** (lag 1 through lag 100) and **several rolling means** (7-day, 30-day, etc.) — the model picks what helps.
- New columns become **features** for a forecasting model. Drop `NaN` rows before training.

**Choosing window size:**

- **Tiny window (e.g., 1–2 days):** The curve hugs every small jump — you see all the noise, but the overall **trend** is harder to spot.
- **Small (3–7 days):** Reacts fast to recent changes; still fairly noisy.
- **Large (e.g., 40 days):** The line smooths out — in class, a **40-day rolling average** made the long-term trend much clearer than a window of 1 or 2.
- **Very large (30–90 days):** Captures slow-moving movement; slower to react to sudden changes.
- Often create **multiple window sizes** and let the model pick what matters.

### Quick Activity — Window Size Trade-off

A sudden **heatwave** triples sales for one day. Will a **7-day** rolling average react immediately or gradually? **Gradually** — the spike blends in over the next week.

- **College canteen (daily patterns):** Shorter window (7 days) — weekly rhythm matters.
- **Monthly billing metric:** Longer window (28–30 days) — smooths daily noise.

---

## Building a Time Series Forecast Model

Once you have **lag** and **rolling** columns, the modeling step is familiar supervised learning — with one rule: **chronological split only**.

**End-to-end workflow:**

1. Engineer **lag** and **rolling mean** features from the target column.
2. **Drop rows with NaN** (early rows lack enough history).
3. Separate **X** (features) and **y** (target — e.g. today's sales).
4. **Chronological train/test split** with `shuffle=False`.
5. Fit **linear regression** and **gradient boosting regressor**; compare **R²** and **MAPE** on the test period.
6. Plot predictions vs actuals on the **test window** — forecast always happens on unseen future data.

```python
import pandas as pd  # tables and time features
import numpy as np  # numeric helpers
from sklearn.model_selection import train_test_split  # train/test split
from sklearn.linear_model import LinearRegression  # simple linear model
from sklearn.ensemble import GradientBoostingRegressor  # stronger tree-based model

# Sample daily sales (replace with your CSV in practice)
data = {
    'date': pd.date_range(start='2024-01-01', periods=140, freq='D'),  # 140 days
    'sales': np.random.randint(180, 320, size=140)  # placeholder sales values
}
df = pd.DataFrame(data)  # build DataFrame
df = df.set_index('date')  # date as index

# Step 1 — create lag and rolling features
df['lag_1'] = df['sales'].shift(1)  # yesterday
df['lag_2'] = df['sales'].shift(2)  # two days ago
df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()  # 7-day average

# Step 2 — drop rows with missing feature values
df = df.dropna()  # remove NaN rows from early lags/rolling

# Step 3 — define X and y
feature_cols = ['lag_1', 'lag_2', 'rolling_mean_7']  # input columns
X = df[feature_cols]  # all feature rows
y = df['sales']  # target to predict

# Step 4 — chronological split (no shuffle)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,  # features and target
    test_size=0.2,  # last 20% for test
    shuffle=False  # preserve time order
)

# Step 5a — linear regression
lr = LinearRegression()  # create model
lr.fit(X_train, y_train)  # train on past data
print('LR train R²:', lr.score(X_train, y_train))  # fit on train
print('LR test R²:', lr.score(X_test, y_test))  # score on future holdout

# Step 5b — gradient boosting (often stronger on same features)
gb = GradientBoostingRegressor(n_estimators=100, random_state=42)  # 100 trees
gb.fit(X_train, y_train)  # train on same split
print('GB train R²:', gb.score(X_train, y_train))  # train score
print('GB test R²:', gb.score(X_test, y_test))  # test score — compare to LR
```

**How the code works:**

- Lags and rolling mean turn **past sales** into columns the model can learn from.
- `dropna()` removes the first rows where lags/rolling are not yet defined.
- `shuffle=False` keeps the **last 20%** of time as the honest test set.
- `model.score()` returns **R²** — higher means better fit on that split.
- In class, **gradient boosting** often beat **linear regression** on the same features (higher test R², lower MAPE).
- On a forecast plot: **train** is the left block; **test actuals** are the right block; compare how closely each model's line follows the black actual curve.

---

## Evaluation for Time Series

You built features and split data correctly. Now — how good are the predictions?

You already met **MAE** and **RMSE** in regression work — both apply here too. Forecasting is a **regression** problem (predict a number). MAE = average absolute error; RMSE punishes large misses more heavily.

**R² (coefficient of determination)** is the main score you used in class for regression models:

- **Official Definition:** The fraction of variance in the target explained by the model — ranges from negative (worse than guessing the mean) up to 1.0 (perfect fit).
- **In Simple Words:** "How much of the pattern did the model catch?" — shown by `model.score(X_test, y_test)`.
- **Real-Life Example:** Test R² of 0.87 means the model explains 87% of sales variation on the future holdout — decent, but always check with plots and MAPE too.

- Higher **R²** on the chronological test set usually means **lower MAPE** — better forecasts and smaller percentage errors.
- Always compute metrics on the **future holdout** after a time-aware split — never on shuffled rows.

One metric especially handy for time series comparison across scales: **MAPE**.

---

### MAPE — Mean Absolute Percentage Error

**MAPE:**

- **Official Definition:** Prediction error expressed as a **percentage of the actual value** rather than in absolute units.
- **In Simple Words:** Instead of "off by ₹20," say "off by 5%." Easy to compare across products with different scales.
- **Formula:** `MAPE = Average of ( |Actual − Predicted| / Actual ) × 100`

| Day | Actual (₹) | Predicted (₹) | % Error |
|---|---|---|---|
| 1 | 100 | 110 | 10.0% |
| 2 | 200 | 190 | 5.0% |
| 3 | 150 | 160 | 6.7% |
| **MAPE** | — | — | **~7.2%** |

- MAPE ≈ 7% means predictions are off by about 7% of the actual value on average.
- In the hands-on demo, **linear regression** had MAPE around **9.67%**; **gradient boosting** achieved a **lower MAPE** and **higher R²** on the same test split.

```python
import numpy as np  # import numpy for array math

actual_arr    = np.array([100, 200, 150, 300, 250])  # true values
predicted_arr = np.array([110, 190, 160, 280, 260])  # model predictions

mape = np.mean(np.abs((actual_arr - predicted_arr) / actual_arr)) * 100  # % error averaged
print(f"MAPE: {mape:.2f}%")  # print result as percentage
```

**How the code works:**

- `actual_arr - predicted_arr` gives raw error per day.
- `np.abs(...)` keeps only magnitude (direction does not matter).
- Dividing by `actual_arr` turns each error into a fraction of the true value.
- `np.mean(...) * 100` averages and converts to percentage.

**Watch out:** MAPE fails when actual values are **0** or near 0 (division by zero). Use MAE in those cases.

---

### Choosing Metrics

| Metric | Best when | Weakness |
|---|---|---|
| **R²** | Quick overall fit check on regression models | Hard to interpret alone — use with plots |
| **MAE** | All errors equally important | Ignores rare big outliers |
| **RMSE** | Large errors are very costly | Sensitive to outliers |
| **MAPE** | Comparing across different scales | Breaks when actual ≈ 0 |

- Report **more than one metric** — e.g. R² + MAPE — for a full picture.
- Compute all metrics only on the **future holdout period** after a time-aware split.

---

## Case Study: Air Passengers (1949–1960)

A second worked example tied every idea together — monthly passenger counts from **January 1949 to December 1960** (144 months).

**What the chart shows:**

- **Trend:** Passenger numbers rise over the years — more people flew as air travel grew.
- **Seasonality:** Peaks around **July–August**; sharp drops in **November–December** — the same pattern repeats every year.

**Feature engineering for this dataset:**

- **Time index** — row number 1 to 144 so the model sees progression through time.
- **One-hot encoding for month** — January, February, … become dummy columns (0/1) so the model captures seasonal months without treating "December" as bigger than "January" as a raw number.

**Modeling steps:**

1. Load the CSV; plot passengers vs month to spot trend and seasonality.
2. Add time index and month dummies (`pd.get_dummies` on the month column).
3. Drop the raw month column after dummies are created — month info lives in the dummy columns.
4. **X** = time index + month dummies; **y** = passenger count.
5. Chronological **train/test split**; fit **linear regression** — e.g. ~95% train R² and ~62% test R² in the demo (not perfect, but illustrative).
6. Plot train vs test predictions; optionally repeat with **gradient boosting** for a stronger fit.

- This case study uses **calendar features** (month dummies) instead of only lags — both styles appear in real forecasting work.
- Always drop datetime columns that sklearn cannot use directly before fitting.

---

## Practice: Apply on Financial Time Series

To build confidence after class, apply the same pipeline on a **Bitcoin** (or any financial asset) CSV with **one-minute interval** prices:

1. Load the shared dataset.
2. Create **lag** and **rolling mean** features.
3. Chronological split with **`shuffle=False`**.
4. Train **linear regression** and **gradient boosting**; compare **R²** and **MAPE**.
5. Plot forecasts on the test window.

- Goal is a working **baseline model** — not a perfect trader bot.
- The same steps work for stocks, mutual funds, or gold — any ordered price history.

---

## Key Takeaways

- **Time series data is order-dependent** — shuffling destroys meaning. This is the opposite of clustering or PCA tables where row order did not matter.
- **Trend** is the long-term direction; **seasonality** is the repeating calendar pattern. Real business data (stocks, AC sales, airline passengers) usually has both.
- **Never use random train-test split** on dated data. Split **chronologically** with **`shuffle=False`** — past trains, future tests — to avoid future leakage.
- **Rolling windows** and **lag features** turn recent history into model-ready columns — the main feature-engineering tool for tabular time series work.
- Fit familiar models (**linear regression**, **gradient boosting**) on engineered features; compare **R²** and **MAPE** on the chronological test set and inspect forecast plots.
- The **Air Passengers** case study showed trend, seasonality, month dummies, and regression scores on real monthly data.
- Next you will connect these ideas to broader model comparison and real-world forecasting workflows where timestamps drive every decision.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means |
|---|---|
| **Time series** | Data recorded at successive, ordered time points |
| **Trend** | Long-term upward, downward, or flat direction |
| **Seasonality** | Repeating pattern at fixed intervals (weekly, yearly) |
| **Data leakage** | Future information accidentally used in training |
| **Chronological split** | Past rows = train, future rows = test |
| **`shuffle=False`** | Keep row order in `train_test_split` for time series |
| **Rolling window** | Fixed-size slice sliding through time for stats |
| **Lag feature** | Past value as a new column (e.g. yesterday's sales) |
| **R²** | Fraction of target variance explained by the model |
| **MAPE** | Mean Absolute Percentage Error — error as % of actual |
| **Gradient boosting regressor** | Tree ensemble regressor; often stronger than linear regression |
| `pd.date_range()` | Generate a sequence of dates in pandas |
| `df.set_index('date')` | Set date column as the DataFrame index |
| `.rolling(window=N).mean()` | N-step rolling average |
| `.shift(N)` | Shift values by N steps for lag features |
| `pd.get_dummies()` | One-hot encode categorical columns (e.g. month) |
