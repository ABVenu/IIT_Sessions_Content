# Pandas: Cleaning & Grouping

## What You’ll Learn

In this lesson, you’ll learn how to clean messy datasets and summarize information using Pandas. You’ll understand how to detect and handle missing values, how to use `groupby()` to organize data into meaningful categories, how to compute basic aggregations like sum, mean, and count, and how to rename or drop columns safely. These operations form the backbone of real-world data preparation in AI systems.

![Cleaning](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/b6c87e5d-7145-4e94-aae2-c0795d7d21fb/FwThkFRGNcPEnIgl.png)

---

## 1. Why Data Cleaning Is Non-Negotiable

In practice, real datasets are messy.

They contain:
- Missing values
- Incorrect data types
- Duplicates
- Irrelevant columns
- Inconsistent naming

Before building models, engineers must ensure data is:
- Complete enough
- Consistent
- Structured correctly

Poor data cleaning leads to poor models. Many ML failures are not modeling failures—they are preprocessing failures.

Pandas provides tools that make cleaning systematic and reproducible.

---

## 2. Handling Missing Values

### Detecting Missing Data

Pandas represents missing values as `NaN` (Not a Number) or `None`.

To check for missing values:

```python
df.isnull()
````

To count missing values per column:

```python
df.isnull().sum()
```

This step is essential before any modeling or analysis.

---

### Dropping Missing Values

If missing values are minimal or not useful, you can drop them.

Drop rows with missing values:

```python
df_clean = df.dropna()
```

Drop columns with missing values:

```python
df_clean = df.dropna(axis=1)
```

Drop rows only if a specific column is missing:

```python
df_clean = df.dropna(subset=["Score"])
```

Dropping data reduces dataset size, so it must be done carefully.

---

### Filling Missing Values

Sometimes missing data should be filled instead of removed.

Fill with a constant:

```python
df["Score"] = df["Score"].fillna(0)
```

Fill with column mean:

```python
df["Score"] = df["Score"].fillna(df["Score"].mean())
```

Common strategies:

* Mean (for numerical columns)
* Median (for skewed data)
* Mode (for categorical data)
* Forward fill (for time series)

Choosing a strategy depends on context.

---

## 3. GroupBy: Organizing Data by Categories

### What Is GroupBy?

`groupby()` splits data into groups based on one or more columns, allowing you to perform aggregations on each group.

It follows a three-step pattern:

1. Split
2. Apply
3. Combine

Example dataset:

| Department | Salary |
| ---------- | ------ |
| HR         | 50000  |
| IT         | 70000  |
| HR         | 55000  |

---

### Basic GroupBy Example

```python
df.groupby("Department")["Salary"].mean()
```

This calculates the average salary per department.

GroupBy is fundamental in AI pipelines when:

* Aggregating features
* Computing statistics
* Summarizing behavior per category

---

## 4. Basic Aggregations: Sum, Mean, Count

### Sum

```python
df.groupby("Department")["Salary"].sum()
```

Adds salaries within each department.

---

### Mean

```python
df.groupby("Department")["Salary"].mean()
```

Computes average salary per department.

---

### Count

```python
df.groupby("Department")["Salary"].count()
```

Counts non-null entries.

---

### Multiple Aggregations at Once

```python
df.groupby("Department")["Salary"].agg(["sum", "mean", "count"])
```

This produces a summary table.

This style of aggregation is common in:

* Feature engineering
* KPI dashboards
* Business analytics

---

## 5. Renaming Columns

Clean column names improve readability and downstream compatibility.

Rename a single column:

```python
df = df.rename(columns={"Salary": "Annual_Salary"})
```

Rename multiple columns:

```python
df = df.rename(columns={
    "Salary": "Annual_Salary",
    "Dept": "Department"
})
```

Clear naming reduces confusion in larger pipelines.

---

## 6. Dropping Columns

Sometimes columns are unnecessary or irrelevant.

Drop a column:

```python
df = df.drop(columns=["Unnecessary_Column"])
```

Drop multiple columns:

```python
df = df.drop(columns=["Col1", "Col2"])
```

Dropping unused columns:

* Simplifies datasets
* Reduces memory usage
* Prevents accidental leakage into models

---

## 7. A Realistic Example

```python
import pandas as pd

df = pd.read_csv("employees.csv")

# Handle missing salaries
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Drop irrelevant column
df = df.drop(columns=["Temporary_Notes"])

# Rename for clarity
df = df.rename(columns={"Dept": "Department"})

# Group and summarize
summary = df.groupby("Department")["Salary"].agg(["mean", "count"])

print(summary)
```

This sequence:

* Cleans missing values
* Simplifies structure
* Improves clarity
* Produces aggregated insights

This pattern is common in AI feature preparation.

---

## 8. Common Beginner Mistakes

* Dropping too much data without understanding impact
* Filling missing values blindly
* Forgetting that `count()` ignores null values
* Overwriting the original DataFrame unintentionally

Good practice:

* Inspect before modifying
* Keep intermediate copies
* Document assumptions

---

## Key Takeaways

Cleaning data ensures reliability. Missing values must be handled intentionally—either dropped or filled appropriately. GroupBy enables structured aggregation, which is critical for summarizing data and engineering features. Renaming and dropping columns improves clarity and prevents errors. Data preparation is not a side task—it is the foundation of effective AI systems.

**Mental model:**
Clean first.
Group intelligently.
Aggregate clearly.
Rename for clarity.
Drop what you don’t need.

---

## Additional Reading

* Pandas Missing Data Guide:
  [https://pandas.pydata.org/docs/user_guide/missing_data.html](https://pandas.pydata.org/docs/user_guide/missing_data.html)

* GroupBy Documentation:
  [https://pandas.pydata.org/docs/user_guide/groupby.html](https://pandas.pydata.org/docs/user_guide/groupby.html)

* Data Cleaning with Pandas (Real Python):
  [https://realpython.com/python-data-cleaning-numpy-pandas/](https://realpython.com/python-data-cleaning-numpy-pandas/)