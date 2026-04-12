# **Assignment: Pandas Cleaning & Grouping**

---

## **Question 1. (MCQ)**

What does `df.isnull().sum()` return?

A) Total number of rows
B) Total number of columns
C) Count of missing values per column
D) Boolean values for each row

**Correct answer:** C

**Explanation:**
`df.isnull()` creates a Boolean DataFrame marking missing values as `True`. Calling `.sum()` on it counts the number of `True` values per column, giving the total missing values in each column.

---

## **Question 2. (MCQ)**

What does the following code do?

```python
df_clean = df.dropna()
```

A) Fills missing values with zero
B) Removes rows containing any missing values
C) Removes columns containing missing values
D) Replaces NaN with mean

**Correct answer:** B

**Explanation:**
`dropna()` removes rows where at least one column contains a missing value. This reduces dataset size and must be used carefully to avoid losing important data.

---

## **Question 3. (MCQ)**

How can you drop columns instead of rows when handling missing data?

A) `df.dropna(axis=0)`
B) `df.dropna(axis=1)`
C) `df.dropna(columns=True)`
D) `df.remove_na(axis=1)`

**Correct answer:** B

**Explanation:**
Setting `axis=1` tells Pandas to operate across columns. Thus, `dropna(axis=1)` removes columns containing missing values.

---

## **Question 4. (MCQ)**

What is the effect of this code?

```python
df["Score"] = df["Score"].fillna(df["Score"].mean())
```

A) Removes the Score column
B) Replaces missing values in Score with the column mean
C) Replaces all values with the mean
D) Sorts the column

**Correct answer:** B

**Explanation:**
`fillna()` replaces only missing (`NaN`) values. Using the column mean is a common strategy for imputing numerical data in AI preprocessing.

---

## **Question 5. (MCQ)**

What does `groupby()` primarily do?

A) Sorts data
B) Removes duplicates
C) Splits data into groups for aggregation
D) Merges DataFrames

**Correct answer:** C

**Explanation:**
`groupby()` follows the split–apply–combine paradigm. It splits the DataFrame into groups based on categories, applies aggregation functions, and combines results.

---

## **Question 6. (MCQ)**

What does `count()` compute in a grouped DataFrame?

A) Total rows including null values
B) Only non-null entries
C) Number of unique values
D) Sum of values

**Correct answer:** B

**Explanation:**
`count()` counts only non-null values. It ignores missing entries, which is important when analyzing incomplete datasets.

---

## **Question 7. (MCQ)**

What is the purpose of `rename()`?

A) Permanently changes database schema
B) Deletes columns
C) Changes column names for clarity
D) Sorts column names alphabetically

**Correct answer:** C

**Explanation:**
`rename()` updates column names without modifying data. Clean naming improves readability and reduces confusion in pipelines.

---

## **Question 8. (MCQ)**

What does this line accomplish?

```python
df = df.drop(columns=["Unnecessary_Column"])
```

A) Removes rows
B) Removes the specified column
C) Renames the column
D) Replaces the column with null values

**Correct answer:** B

**Explanation:**
The `drop(columns=...)` argument removes the specified column(s) from the DataFrame, simplifying the dataset and preventing accidental use in modeling.

---

## **Question 9. (Subjective)**

### **AI-Style Employee Data Cleaning & Aggregation Pipeline**

You are given a dataset representing employee records with the following columns:

* Employee
* Department
* Salary
* Temporary_Notes

The dataset contains missing salary values and an irrelevant column.

### **Tasks**

1. Create a sample DataFrame with at least 5 rows including:

   * At least one missing Salary value
   * A Temporary_Notes column
2. Detect and print missing values.
3. Fill missing Salary values using the column mean.
4. Drop the Temporary_Notes column.
5. Rename Salary to Annual_Salary.
6. Group by Department and compute:

   * Mean salary
   * Count of employees
7. Print the final summary table.

---

# ✅ **Solution**

```python
import pandas as pd
import numpy as np

# Step 1: Create sample dataset
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 70000, np.nan, 80000, 60000],
    "Temporary_Notes": ["Temp", "Temp", "Temp", "Temp", "Temp"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 2: Detect missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 3: Fill missing Salary values with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Step 4: Drop irrelevant column
df = df.drop(columns=["Temporary_Notes"])

# Step 5: Rename column
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\nCleaned DataFrame:")
print(df)

# Step 6: Group and aggregate
summary = df.groupby("Department")["Annual_Salary"].agg(["mean", "count"])

print("\nDepartment Summary:")
print(summary)
```