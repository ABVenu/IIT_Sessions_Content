# Subjective Assignment - Medium Difficulty

## Practical Task: GreenGrid Daily Electricity Forecast

**GreenGrid** supplies power to a mid-size city. The operations team has **150 consecutive days** of daily electricity consumption (MWh) and wants a **baseline forecast** for the near future. You do not have a pre-built model — you must engineer time-based features, split data correctly, train two regressors, and report which one forecasts more accurately on unseen future days.

### Requirements

1. **Create reproducible data in code** (`random_state=42`):
   - Build a DataFrame with **150 daily rows**: a `date` column (consecutive days starting `2024-01-01`) and a numeric `consumption_mwh` column.
   - You may generate `consumption_mwh` with `numpy` (e.g. base level + mild trend + small noise). Column names must match the task (`date`, `consumption_mwh`).

2. **Feature engineering:**
   - Set `date` as the index (or keep it as a column but ensure rows stay sorted by time).
   - Add **`lag_1`** (previous day's consumption), **`lag_7`** (same weekday last week), and **`rolling_mean_7`** (7-day rolling average of `consumption_mwh`).
   - **Drop rows with NaN** after creating these features.

3. **Train/test split (time-aware):**
   - Let **X** = `[lag_1, lag_7, rolling_mean_7]` and **y** = `consumption_mwh`.
   - Split **80% train / 20% test** with `shuffle=False` and `test_size=0.2`.

4. **Train and compare two models** on the **same train split**:
   - `LinearRegression`
   - `GradientBoostingRegressor(n_estimators=100, random_state=42)`
   - For each model, print **train R²** and **test R²** (use `model.score`).

5. **MAPE on the test set:**
   - Write a small function or inline code to compute **MAPE** on test predictions:  
     `mean(|actual - predicted| / actual) × 100`
   - Print **test MAPE** for both models (2 decimal places is fine).

6. **Decision line (text output):**
   - Print **one sentence** naming which model has the **lower test MAPE** and whether its **test R²** is also higher.

### Expected Output (minimum)

```
LR train R²: ...
LR test R²: ...
GB train R²: ...
GB test R²: ...
LR test MAPE: ...%
GB test MAPE: ...%
Winner: ... (one sentence)
```

### Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

### Answer Explanation (Reference Approach)

#### Step-by-step solution walkthrough

1. Generate 150 days of synthetic consumption with a fixed seed so runs are reproducible.
2. Build `lag_1`, `lag_7`, and `rolling_mean_7`; `dropna()` removes the first rows without full history.
3. Chronological split with `shuffle=False` — test = last 20% of time.
4. Fit LR and GB on train; score R² on train and test.
5. Predict on `X_test`, compute MAPE per model, compare — GB often wins on synthetic data but either outcome is valid if metrics are computed correctly.

#### Complete exact code (single-file reference solution)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor

# 1) Reproducible 150-day electricity series
np.random.seed(42)
n_days = 150
dates = pd.date_range(start="2024-01-01", periods=n_days, freq="D")
trend = np.linspace(0, 15, n_days)
noise = np.random.normal(0, 2.5, n_days)
consumption = 120 + trend + noise

df = pd.DataFrame({"date": dates, "consumption_mwh": consumption})
df = df.set_index("date")

# 2) Lag + rolling features
df["lag_1"] = df["consumption_mwh"].shift(1)
df["lag_7"] = df["consumption_mwh"].shift(7)
df["rolling_mean_7"] = df["consumption_mwh"].rolling(window=7).mean()
df = df.dropna()

feature_cols = ["lag_1", "lag_7", "rolling_mean_7"]
X = df[feature_cols]
y = df["consumption_mwh"]

# 3) Chronological split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# 4) Train LR and GB; print R²
lr = LinearRegression()
lr.fit(X_train, y_train)
print(f"LR train R²: {lr.score(X_train, y_train):.4f}")
print(f"LR test R²: {lr.score(X_test, y_test):.4f}")

gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb.fit(X_train, y_train)
print(f"GB train R²: {gb.score(X_train, y_train):.4f}")
print(f"GB test R²: {gb.score(X_test, y_test):.4f}")


def mape(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    return np.mean(np.abs((actual - predicted) / actual)) * 100


# 5) Test MAPE
lr_mape = mape(y_test, lr.predict(X_test))
gb_mape = mape(y_test, gb.predict(X_test))
print(f"LR test MAPE: {lr_mape:.2f}%")
print(f"GB test MAPE: {gb_mape:.2f}%")

# 6) Winner sentence
lr_r2_test = lr.score(X_test, y_test)
gb_r2_test = gb.score(X_test, y_test)
if gb_mape < lr_mape:
    winner = "Gradient Boosting"
    better_r2 = gb_r2_test > lr_r2_test
else:
    winner = "Linear Regression"
    better_r2 = lr_r2_test > gb_r2_test

r2_note = "also has higher test R²" if better_r2 else "does not have higher test R²"
print(f"Winner: {winner} has lower test MAPE and {r2_note} on this run.")
```

#### Alternative approaches

- `consumption_mwh` may be loaded from a provided CSV instead of synthetic data, as long as dates are consecutive and all six requirement blocks are met.
- MAPE can be computed with a pandas one-liner; numeric results should match within rounding.
- A matplotlib forecast plot is optional bonus work — not required for full credit.

#### Notes for evaluation

- Accept solutions that follow lag → rolling → `dropna` → `shuffle=False` → LR + GB → R² + MAPE.
- Penalise missing `shuffle=False`, using future rows in training via shuffled split, or skipping `dropna()` after lags.
- Winner sentence must reference **test MAPE** (and ideally test R² comparison).
