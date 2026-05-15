# Assignment: Objective — Session 14: Data Prep — Handling Messy Data

**Total Questions: 10 | Format: 6 MCQs (Single Correct) + 4 MSQs (Multiple Correct)**
**Order: Easy → Moderate → Hard**

---

## MCQ 1 — Easy (Single Correct)

A city transport analytics team opens a CSV of daily bus trips. They want a quick first look at the table without loading every row into the notebook output. Which pandas call is the most appropriate first step?

**A)** `df.describe()`
**B)** `df.head()`
**C)** `df.drop_duplicates()`
**D)** `df.fillna(0)`

**Correct Answer: B**

**Answer Explanation:**
`df.head()` shows the first five rows so you can spot obvious formatting issues, missing cells, and wrong types before deeper analysis. `describe()` summarizes numeric columns only and skips a visual row-by-row check. `drop_duplicates()` and `fillna()` change the data; inspection should come first.

---

## MCQ 2 — Easy (Single Correct)

A clinic spreadsheet lists patient ages. One row shows `-3` years, which cannot be real. The team wants to mark that value as missing so a later imputation step can replace it. Which approach matches that intent?

**A)** `df['age'] = df['age'].abs()`
**B)** `df['age'] = df['age'].replace(-3, np.nan)`
**C)** `df['age'] = df['age'].fillna(df['age'].mean())`
**D)** `df = df.drop_duplicates()`

**Correct Answer: B**

**Answer Explanation:**
An impossible age should become missing (`NaN`) for imputation, not stay as a valid number. `replace(-3, np.nan)` does that. `abs()` would turn `-3` into `3`, which is still not trustworthy domain data. `fillna(mean)` only fills existing blanks; it does not fix a bad recorded value. `drop_duplicates()` removes repeated rows, not invalid entries.

---

## MCQ 3 — Easy (Single Correct)

An online store export shows the same order line copied twice with identical values in every column. Before modelling repeat purchase behaviour, what should the team check first?

**A)** How many rows are exact duplicates using `df.duplicated().sum()`
**B)** The column-wise missing-value percentage using `df.isnull().mean() * 100`
**C)** Whether numeric columns need min–max scaling
**D)** Whether categorical columns need one-hot encoding

**Correct Answer: A**

**Answer Explanation:**
Identical repeated rows are a duplicate-row problem. `duplicated().sum()` counts how many rows match an earlier row exactly. Missing-value percentages, scaling, and encoding matter later; they do not tell you whether the same order was stored twice.

---

## MCQ 4 — Easy (Single Correct)

A used-car listing file has a few negative prices caused by a sign error in the source system. Price must stay non-negative, and the magnitude is still useful. What is the most direct fix?

**A)** `df['price'] = df['price'].fillna(df['price'].median())`
**B)** `df['price'] = df['price'].abs()`
**C)** `df['price'] = df['price'].replace(-1, np.nan)`
**D)** `df = pd.get_dummies(df, columns=['price'])`

**Correct Answer: B**

**Answer Explanation:**
For a sign error on a price column, taking the absolute value keeps the amount while removing the negative sign. Median fill addresses missing values, not wrong signs. Replacing `-1` with `NaN` only handles that one value and drops usable magnitude information. One-hot encoding is for categorical text columns, not numeric prices.

---

## MCQ 5 — Moderate (Single Correct)

A hiring dataset has a `seniority_band` column with values `Junior`, `Mid`, and `Senior` in a clear career order. The team needs a single numeric feature for a tree-based model. Which encoding choice is the best fit?

**A)** One-hot encoding with `pd.get_dummies(..., drop_first=True)`
**B)** Label encoding with `LabelEncoder().fit_transform(...)`
**C)** Min–max scaling on the original text labels
**D)** Replacing every category with the column mean

**Correct Answer: B**

**Answer Explanation:**
`seniority_band` is ordinal: the categories have a natural order. Label encoding maps ordered categories to integers in one column. One-hot encoding fits nominal categories without order, such as fuel type or brand. Min–max scaling applies to numbers, not raw text labels. Mean replacement is for numeric imputation, not category encoding.

---

## MCQ 6 — Moderate (Single Correct)

After splitting features and labels, a data scientist fits `MinMaxScaler` on the full dataset and then splits into train and test sets. What is the main problem with that workflow?

**A)** `MinMaxScaler` cannot scale more than two numeric columns at once
**B)** Test-set statistics influenced the scaler fit, which can make evaluation look better than it should
**C)** The label column must be scaled before `train_test_split`
**D)** `MinMaxScaler` only works after one-hot encoding every column

**Correct Answer: B**

**Answer Explanation:**
Fitting a scaler on data that includes the test portion lets test-set min/max (or mean/std) leak into preprocessing. That is data leakage and can inflate test performance. `MinMaxScaler` can scale many numeric columns. Labels are usually not scaled as features. Scaling is not limited to running only after one-hot encoding.

---

## MSQ 7 — Moderate (Multiple Correct)

A delivery-time dataset has missing values in `distance_km` (numeric, mild outliers) and `vehicle_type` (text categories). Which imputation choices are reasonable for these columns? (Select **all** that apply)

**A)** Fill missing `distance_km` with the column median
**B)** Fill missing `distance_km` with the column mean
**C)** Fill missing `vehicle_type` with the most frequent category from `vehicle_type`
**D)** Fill missing `vehicle_type` with the median of `distance_km`
**E)** Fill missing `distance_km` with `0` for every blank without checking the column distribution

**Correct Answers: A, B, C**

**Answer Explanation:**
- **A — Correct:** Median imputation is a standard choice for numeric columns, especially when outliers are present.
- **B — Correct:** Mean imputation is also valid for numeric columns when outliers are not dominating the column.
- **C — Correct:** Mode (most frequent category) imputation is the usual approach for categorical text columns.
- **D — Incorrect:** A distance median does not represent a vehicle category; the substitute must come from the same column’s valid values.
- **E — Incorrect:** Filling every blank with `0` without context can invent unrealistic distances and distort the feature.

---

## MSQ 8 — Moderate (Multiple Correct)

Before changing a customer-support ticket dataset, which inspection steps help surface common data-quality problems? (Select **all** that apply)

**A)** `df.shape` to see row and column counts
**B)** `df.info()` to check data types and non-null counts
**C)** `df.isnull().sum()` to count missing values per column
**D)** `df.describe()` to summarize numeric columns
**E)** Fitting `MinMaxScaler` on the full table before any missing-value handling

**Correct Answers: A, B, C, D**

**Answer Explanation:**
- **A — Correct:** Shape gives a quick size check before and after cleaning.
- **B — Correct:** `info()` reveals dtypes and how many non-null values each column has.
- **C — Correct:** Per-column null counts show where imputation or row decisions are needed.
- **D — Correct:** `describe()` highlights numeric ranges that may expose outliers or scale differences.
- **E — Incorrect:** Fitting a scaler on the full raw table before cleaning and before a proper train/test split risks leakage and skips foundational inspection.

---

## MSQ 9 — Hard (Multiple Correct)

A team is preparing a tabular dataset for supervised learning. They will split features and labels, then clean and encode features without leaking test information. Which statements describe a sound preprocessing order? (Select **all** that apply)

**A)** Fix domain-invalid values (such as negative prices) before systematic imputation
**B)** Impute missing feature values before removing duplicate rows
**C)** Remove duplicate rows before fitting encoders or scalers on the training split
**D)** Learn one-hot column mappings from the training split only, then apply the same mapping to validation/test data
**E)** Fit `MinMaxScaler` on the combined training and test feature matrices so both sets share identical min and max values

**Correct Answers: A, C, D**

**Answer Explanation:**
- **A — Correct:** Impossible values should be corrected or marked missing before you impute or model.
- **B — Incorrect:** Dropping duplicate rows first avoids wasting imputation work on rows that will be removed anyway.
- **C — Correct:** De-duplication is an early hygiene step before learning transformations from the training split.
- **D — Correct:** Encoders and scalers should be fit on training data only, then applied to other splits with the learned mapping.
- **E — Incorrect:** Fitting on train plus test leaks test-set information into preprocessing and makes metrics overly optimistic.

---

## MSQ 10 — Hard (Multiple Correct)

A car resale dataset includes `brand` (nominal), `fuel` (nominal), `kilometers_driven` (numeric), and `price` (numeric target). The team has already handled missing values and duplicate rows. Which next-step decisions are appropriate? (Select **all** that apply)

**A)** Apply one-hot encoding to `brand` and `fuel` because they are unordered categories
**B)** Apply label encoding to `brand` because it creates a single compact numeric column for every tree model
**C)** Apply min–max scaling to numeric input features such as `kilometers_driven` when large numeric ranges could dominate learning
**D)** Scale the `price` target with `MinMaxScaler` before splitting into train and test
**E)** Compare row counts and remaining missing values after cleaning to verify the pipeline’s impact

**Correct Answers: A, C, E**

**Answer Explanation:**
- **A — Correct:** Brand and fuel are nominal categories; one-hot encoding avoids inventing a false order between labels.
- **B — Incorrect:** Label encoding on nominal categories implies ranking (for example, Brand A < Brand B), which is usually misleading.
- **C — Correct:** Scaling numeric inputs can keep large-magnitude columns from overpowering smaller-scale features during training.
- **D — Incorrect:** The target label is not treated like an input feature for routine feature scaling in this workflow.
- **E — Correct:** Before/after checks on rows and missing values confirm whether cleaning steps actually improved data quality.
