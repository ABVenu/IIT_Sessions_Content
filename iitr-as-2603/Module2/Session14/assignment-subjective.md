# Assignment: Subjective — Session 14: Data Prep — Handling Messy Data

**Total Questions: 1 | Format: Practical Coding Task | Difficulty: Medium**

---

## Question 1 — Clean a Messy Used-Bike Listings Table

**Scenario:**

RideMetrics, a used two-wheeler marketplace, exported a small listing table for a pricing pilot. Several rows have sign errors, blanks, repeated listings, and text categories that models cannot use directly. Your job is to load the table, inspect it, apply the cleaning steps below, and print a short before-and-after summary.

---

### Dataset

Run this code once at the top of your solution to create `ride_bikes.csv` in the same folder as your script:

```python
import pandas as pd
import numpy as np

data = {
    "listing_id": ["RB101", "RB102", "RB103", "RB104", "RB105", "RB106", "RB102", "RB107", "RB108", "RB109"],
    "brand": ["Yamaha", "Honda", "Bajaj", "TVS", "Hero", "Yamaha", "Honda", "Suzuki", "Honda", "Yamaha"],
    "model_year": [2019, 2018, 2020, 2017, 2021, 2016, 2018, 2019, 2020, 2018],
    "kilometers_driven": [18000, np.nan, 22000, 35000, 9000, 41000, np.nan, np.nan, 15000, 27000],
    "fuel": ["Petrol", "Petrol", "Petrol", "Petrol", "Petrol", "Diesel", "Petrol", "Petrol", "Petrol", "Petrol"],
    "asking_price": [85000, -72000, 65000, 48000, 55000, 39000, -72000, 61000, np.nan, 70000],
}

pd.DataFrame(data).to_csv("ride_bikes.csv", index=False)
```

Column meanings:

| Column | Description |
|---|---|
| `listing_id` | Unique listing reference |
| `brand` | Manufacturer name (unordered category) |
| `model_year` | Year of manufacture |
| `kilometers_driven` | Odometer reading in km |
| `fuel` | Fuel type (unordered category) |
| `asking_price` | Listed price in INR (target for later modelling) |

---

### Tasks

Write a single Python file that does the following in order:

1. **Load and inspect**
   - Read `ride_bikes.csv` into a DataFrame.
   - Print `shape`, the first five rows, per-column missing-value counts, and `describe()` for numeric columns.

2. **Fix impossible asking prices**
   - Replace negative `asking_price` values with their absolute values.

3. **Handle missing values**
   - Fill missing `kilometers_driven` with the column median.
   - Fill missing `asking_price` with the column mean **after** the sign fix in step 2.

4. **Remove duplicate listings**
   - Drop duplicate rows and keep the first occurrence.
   - Print how many duplicate rows were removed.

5. **Encode nominal categories**
   - One-hot encode `brand` and `fuel` with `pd.get_dummies(..., drop_first=True)`.

6. **Scale numeric inputs**
   - Apply `MinMaxScaler` to `model_year` and `kilometers_driven` so both fall in the 0–1 range.
   - Do **not** scale `asking_price` (it is the target, not an input feature).

7. **Summarize the impact**
   - Print final `shape`, total missing values across the whole table, and `describe()` for `model_year` and `kilometers_driven` after scaling.

**Expected output checks (your numbers should match after the full pipeline):**

- Duplicate rows removed: **1**
- Final row count: **9**
- Total missing values after cleaning: **0**
- Scaled `model_year` and `kilometers_driven` min/max should each be **0.0** and **1.0** (allow tiny floating-point rounding).

---

### Submission Instructions

- Code all points above in a single `.py` file in VS Code.
- Run the script and confirm the printed summary matches the expected checks.
- Submit the complete code in the LMS code editor / answer box.

---

### Answer Explanation

#### Ideal Solution Walkthrough

The workflow mirrors a practical cleaning pipeline: inspect first, fix domain-invalid values, impute, de-duplicate, encode nominal text, scale numeric inputs, then verify the result with simple before/after metrics.

#### Complete Reference Solution

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# --- dataset bootstrap (provided in the question) ---
data = {
    "listing_id": ["RB101", "RB102", "RB103", "RB104", "RB105", "RB106", "RB102", "RB107", "RB108", "RB109"],
    "brand": ["Yamaha", "Honda", "Bajaj", "TVS", "Hero", "Yamaha", "Honda", "Suzuki", "Honda", "Yamaha"],
    "model_year": [2019, 2018, 2020, 2017, 2021, 2016, 2018, 2019, 2020, 2018],
    "kilometers_driven": [18000, np.nan, 22000, 35000, 9000, 41000, np.nan, np.nan, 15000, 27000],
    "fuel": ["Petrol", "Petrol", "Petrol", "Petrol", "Petrol", "Diesel", "Petrol", "Petrol", "Petrol", "Petrol"],
    "asking_price": [85000, -72000, 65000, 48000, 55000, 39000, -72000, 61000, np.nan, 70000],
}
pd.DataFrame(data).to_csv("ride_bikes.csv", index=False)

# 1) Load and inspect
df = pd.read_csv("ride_bikes.csv")
print("Initial shape:", df.shape)
print(df.head())
print("Missing per column:\n", df.isnull().sum())
print(df.describe())

# 2) Fix impossible asking prices
df["asking_price"] = df["asking_price"].abs()

# 3) Impute missing values
km_median = df["kilometers_driven"].median()
df["kilometers_driven"] = df["kilometers_driven"].fillna(km_median)
price_mean = df["asking_price"].mean()
df["asking_price"] = df["asking_price"].fillna(price_mean)

# 4) Remove duplicates
dup_count = df.duplicated().sum()
df = df.drop_duplicates()
print("Duplicate rows removed:", dup_count)

# 5) One-hot encode nominal categories
df = pd.get_dummies(df, columns=["brand", "fuel"], drop_first=True)

# 6) Scale numeric input features only
scaler = MinMaxScaler()
df[["model_year", "kilometers_driven"]] = scaler.fit_transform(
    df[["model_year", "kilometers_driven"]]
)

# 7) Summarize impact
print("Final shape:", df.shape)
print("Total missing values:", df.isnull().sum().sum())
print(df[["model_year", "kilometers_driven"]].describe())
```

**Why this order works:** absolute-value repair runs before mean imputation on `asking_price`, so `-72000` becomes `72000` and enters the mean honestly. Median imputation suits `kilometers_driven` as a numeric odometer column. Duplicate removal happens before encoding/scaling so derived columns are not built from repeated rows. One-hot encoding is used because `brand` and `fuel` are nominal. `MinMaxScaler` is applied only to numeric inputs, not the `asking_price` target.

#### Alternative Approaches

- **Leakage-safe scaling:** Split train/test first, fit `MinMaxScaler` on training rows only, then `transform` validation/test rows. That pattern is preferable when you report model metrics, even though this exercise focuses on a single-table cleaning summary.
- **Imputation choice:** Mean imputation for `kilometers_driven` would also be acceptable on this small table; median is slightly more robust if extreme odometer readings appear.
- **Duplicate handling:** `drop_duplicates(subset=["listing_id"], keep="first")` is a stricter business rule when IDs should be unique even if other fields differ.
