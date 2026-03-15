# The EDA Checklist

## Inspect Data Quickly

## Core Concept: Initial Reconnaissance
Data inspection is the mandatory first step of Exploratory Data Analysis (EDA). These 5 methods (`head`, `tail`, `sample`, `shape`, `info`) form the standard operating procedure for loading any new dataset.

---

## 1. Visual Inspection
Never assume the data loaded correctly just because Pandas didn't throw an error.

```python
import pandas as pd
df = pd.read_csv('employees.csv')

# 1. Check the top 5 rows (default) to verify headers mapped correctly
df.head()

# 2. Check the last 10 rows to ensure file integrity at the EOF marker
df.tail(10)

# 3. Check 5 random rows to verify data isn't uniquely structured at the edges
df.sample(5, random_state=42) # random_state ensures reproducibility
```

---


![Quick DataFrame Inspection Methods](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-61-inspection-map.png)

## 2. Dimensionality with `.shape`
`.shape` is not a method; it is a DataFrame attribute derived from the underlying NumPy architecture. Therefore, it does not use parentheses `()`.

```python
dimensions = df.shape
print(f"The dataset has {dimensions[0]} rows and {dimensions[1]} columns.")
```

---

## 3. Deep Dive with `.info()`
`df.info()` is the diagnostic x-ray of your DataFrame. You must learn to read its output fluently.

```python
df.info()

# Expected output breakdown:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99                <- Validates exact row count
# Data columns (total 3 columns):                 <- Validates exact column count
#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   ID       100 non-null    int64             <- Perfect column, no missing data
#  1   Name     98 non-null     object            <- String column, 2 missing values!
#  2   Salary   100 non-null    float64           <- Decimal column
```
*(Cruciual takeaway: Comparing the `Non-Null Count` against the `RangeIndex` immediately exposes columns with missing `NaN` data).*

---

## Pro-Tip: Memory Usage
By default, `df.info()` estimates memory. To get the exact RAM usage of the DataFrame (crucial for large files), pass `memory_usage='deep'`.

```python
df.info(memory_usage='deep')
```


---

# Group Data with groupby

## 1. Why Group?
Data is only valuable if it tells a story. Raw data is often too noisy. 
By grouping data, we find patterns across categories. We move from looking at individual "data points" to looking at "segment behavior".

## 2. Analogy: The Laundry Service
The "Split-Apply-Combine" pattern is the industry standard for grouped operations:
- **Split**: Subdividing the data based on a key (e.g., Color).
- **Apply**: Calculating something for each group (e.g., counting items).
- **Combine**: Merging results back into a clean summary table.


![GroupBy: Split-Apply-Combine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-17-groupby-sac.png)

## 3. Key Concepts
- **`df.groupby('Col')`**: Returns a `DataFrameGroupBy` object (The "Lazy" object).
- **Aggregation Functions**: Tools like `.sum()`, `.mean()`, `.count()`, and `.min()/max()`.
- **Selecting Columns**: Using `df.groupby('Col')['Value_Col']` to target specific data. 
- **The `numeric_only` Rule**: In modern Pandas (2.0+), if you calculate a mean or sum on a group with text columns, you **must** specify `numeric_only=True` or Pandas will throw a `TypeError`.

## 4. Under the Hood: The "Lazy" GroupBy
What happens when you run `grouped = df.groupby('City')`?
1.  **No Calculation (Yet)**: Pandas does **not** calculate anything initially. It simply scans the 'City' column and creates a "map" of which rows belong to which city.
2.  **The Metadata Map**: It creates a hash table where the keys are the cities and the values are lists of row numbers (indices).
3.  **Efficiency**: This "Lazy Evaluation" is incredibly fast because Pandas waits until you specify the math (like `.mean()`) before it actually looks at the numeric data.

## 5. Detailed Examples

### 1. Basic Summation
```python
import pandas as pd
data = {'Region': ['North', 'South', 'North', 'South'], 'Sales': [1000, 2000, 1500, 3000]}
df = pd.DataFrame(data)

# Total sales per region
region_totals = df.groupby('Region')['Sales'].sum()
```

### 2. Multi-column Selection
```python
# Multiple metrics for one group (e.g., Sales and Units)
stats = df.groupby('Region')[['Sales', 'Units']].mean()
```

## 6. Common Pitfalls
- **The "Lost" Columns**: When you group by 'Department', any column that isn't the group key OR a numeric value will be dropped by default aggregation (like `.mean()`) because you can't find the "average" of a String.
- **The Forgotten Aggregation**:
    ```python
    res = df.groupby('City') 
    print(res) # Output: <pandas.core.groupby.generic.DataFrameGroupBy object...>
    ```
    *Fix*: Always follow groupby with an action like `.sum()` or `.mean()`.
- **Numeric vs. Non-numeric**: Attempting to `.mean()` on a column of Strings will result in an error or an empty result in newer Pandas versions (Numeric-only rule).


---

# Get Summary Statistics with describe

## 1. Why describe()?
In exploratory data analysis (EDA), `describe()` is often the very first command an analyst runs after loading data. It provides a statistical snapshot that reveals data quality issues (like negative prices or extreme outliers) and structural trends instantly.

## 2. Analogy: The Executive Summary
- **The 30,000-ft View**: Seeing the whole forest, not the individual trees.
- **The Vital Signs**: Checking the "Pulse" of the dataset.


![What .describe() Returns](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-23-describe-output.png)

## 3. Key Concepts
- **`.describe()`**: Automatically identifies numerical columns and calculates a 5-number summary (Min, Q1, Median, Q3, Max) plus the Count, Mean, and Std.
- **Percentiles**: The 25%, 50%, and 75% marks. 
    - *Example*: 75% means "75% of the values in this column are BELOW this number."
- **Non-Numerical Data**: By default, `describe()` ignores text columns. To see a summary of strings (Unique count, Top value, Frequency), use `df.describe(include='all')`.

## 4. Under the Hood: Handling Holes (NaN)
How does Pandas summarize data when some entries are missing?
1.  **Silent Exclusion**: Unlike raw Python math, Pandas statistics methods **ignore `NaN`** by default.
2.  **The Denominator logic**: When calculating the `mean`, Pandas divides the sum by the count of *valid* numbers, not the total number of rows.
3.  **Memory Efficiency**: `describe()` is a "Reduction" operation. It processes the entire column and returns a very small Series or DataFrame, making it extremely memory-efficient for reporting.

## 5. Detailed Examples

### 1. Basic Numerical Summary
```python
import pandas as pd
df = pd.DataFrame({'Age': [20, 30, 40, 50, 1000]}) # 1000 is an outlier!

print(df.describe())
# Look at the 'max'. If it's 1000 for 'Age', you instantly know there's a data entry error.
```

### 2. Including Text/Category Data
*For strings, it shows `unique` (how many categories), `top` (most common), and `freq` (how often 'top' appears).*
```python
df = pd.DataFrame({'Status': ['Active', 'Active', 'Pending']})
print(df.describe(include='object'))
```

### 3. Customizing Percentiles
```python
# See more specific slices (10th and 90th percentile)
df.describe(percentiles=[0.1, 0.9])
```

## 6. Common Pitfalls
- **The "Missing" Columns**: Expecting to see 'Name' in the numerical summary. (Pandas splits them; you need `include='all'`).
- **Standard Deviation Confusion**: Forgetting that `std` measures how spread out the data is. A `std` of 0 means every single row has the exact same value.
- **Transposing**: For very wide DataFrames (many columns), the report is hard to read. Use `df.describe().T` to flip it and read columns as rows.


---

# Handling outliers using Pandas logic

## Core Concept: Extreme Value Management
Machine Learning models are sensitive to massive numbers. A single typo (e.g., `Salary = 5,000,000` instead of `50,000`) can pull the statistical averages of an entire dataset wildly off-target. Outliers must be algorithmically identified and managed.

---

## 1. Algorithmic Detection: The IQR Method

The Interquartile Range (IQR) focuses on the "middle 50%" of your data, ignoring the extremes to find a stable baseline.

```python
import pandas as pd

# Assume 'df' holds 'Income' data
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1

# The standard multiplier is 1.5. A multiplier of 3.0 represents extreme outliers.
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```

![Detecting Outliers with the IQR Method](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/images/1773396036807-8c39878f8265.png)

---

## 2. Hard Removal: Trimming

By leveraging standard boolean indexing, we can permanently drop rows containing outliers. This is aggressive and reduces dataset size.

```python
# 1. Ask the question: Which rows are "normal"?
is_normal_mask = (df['Income'] >= lower_bound) & (df['Income'] <= upper_bound)

# 2. Extract only the normal rows
trimmed_df = df[is_normal_mask]
```

---

## 3. Soft Mitigation: Clipping (Winsorization)

Instead of dropping the entire row—which might contain perfectly valid data in other columns like `Age` or `Education`—we compress the extreme value down to the boundary limits.

```python
# The built in .clip() method takes the lower and upper arguments
df['Income_Clipped'] = df['Income'].clip(lower=lower_bound, upper=upper_bound)

# Example: If the upper bound is $150,000
# A raw income of $500,000 becomes $150,000.
# A raw income of $40,000 remains $40,000.
```

---

## 4. Alternate Detection: The Z-Score Method
While IQR is robust (resistant to outliers), the Z-Score method assumes your data is normally distributed (a bell curve). It measures how many standard deviations a value is away from the mean. A Z-score > 3 or < -3 is generally considered an outlier.

```python
mean_income = df['Income'].mean()
std_income = df['Income'].std()

# Calculate Z-scores manually
df['Z_Score'] = (df['Income'] - mean_income) / std_income

# Filter to keep only rows within 3 standard deviations
z_score_trimmed_df = df[(df['Z_Score'] > -3) & (df['Z_Score'] < 3)]
```


---
