# Pandas: The Data Table

## What You’ll Learn

In this lesson, you’ll learn how to work with structured, table-like data using **Pandas**, the standard data analysis library in Python. You’ll understand the difference between a Series and a DataFrame, how to load CSV files into Python, and how to inspect datasets quickly and effectively. These skills are essential for AI workflows, where real-world data almost always begins in tabular form.

![Data](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/3642d954-a6fb-411a-aa2f-b990b413f6b7/QDmMdBvbY0SmQXyz.png)

---

## 1. Why Pandas Matters in AI

Most real-world data looks like an Excel sheet:
- Rows represent records (users, transactions, samples)
- Columns represent attributes (age, score, label, timestamp)

Before training models, data must be:
- Loaded
- Cleaned
- Inspected
- Transformed

Pandas provides a high-level, expressive way to perform these tasks efficiently. It builds on NumPy but adds labels, indexing, and powerful data manipulation tools.

In modern AI pipelines, Pandas is often the first step before NumPy arrays and model training.

---

## 2. Pandas Series vs DataFrame

### What Is a Series?

A **Series** is a one-dimensional labeled array. It is similar to a NumPy array, but with an associated index.

```python
import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
````

Output:

```
0    10
1    20
2    30
dtype: int64
```

Each value has:

* A position
* An index label

You can also define custom indices:

```python
s = pd.Series([90, 85, 88], index=["Alice", "Bob", "Charlie"])
```

A Series is conceptually similar to:

* A single column in a spreadsheet
* A labeled NumPy array

---

### What Is a DataFrame?

A **DataFrame** is a two-dimensional labeled table. It consists of multiple Series aligned by a shared index.

```python
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [90, 85, 88],
    "Passed": [True, True, True]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```
      Name  Score  Passed
0    Alice     90    True
1      Bob     85    True
2  Charlie     88    True
```

A DataFrame:

* Has rows and columns
* Has column names
* Supports powerful filtering and transformation operations

This structure mirrors Excel tables and SQL query results.

---

### Key Conceptual Difference

* A **Series** is one column.
* A **DataFrame** is a full table.

Most AI workflows operate primarily on DataFrames.

---

## 3. Loading CSV Files

### Why CSV?

CSV (Comma-Separated Values) is one of the most common data formats in the world. Many datasets are stored as `.csv` files.

Pandas provides a simple method to load them.

---

### Reading a CSV File

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

That single line:

* Opens the file
* Parses rows and columns
* Infers data types
* Constructs a DataFrame

This simplicity is why Pandas is widely adopted.

---

### Inspecting the Loaded Data

Immediately after loading data, you should inspect it before using it for modeling.

This prevents:

* Hidden formatting issues
* Incorrect data types
* Missing values
* Misaligned columns

Professional AI workflows always begin with inspection.

---

## 4. Basic Inspection Methods

### `head()`: View the First Rows

```python
df.head()
```

By default, this shows the first 5 rows.

You can specify a number:

```python
df.head(10)
```

This helps verify:

* Column names
* Data format
* Basic structure

---

### `tail()`: View the Last Rows

```python
df.tail()
```

Useful for:

* Checking dataset completeness
* Verifying appended records
* Confirming file parsing

---

### `info()`: Understand Structure and Types

```python
df.info()
```

This provides:

* Number of rows
* Column names
* Data types
* Count of non-null values

This is one of the most important inspection tools because incorrect data types can break AI models silently.

---

### `describe()`: Summary Statistics

```python
df.describe()
```

For numerical columns, this shows:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

This helps identify:

* Outliers
* Scale differences
* Distribution patterns

In AI workflows, `describe()` is often the first diagnostic step before preprocessing.

---

## 5. Accessing Data in DataFrames

### Selecting a Column

```python
df["Score"]
```

This returns a Series.

---

### Selecting Multiple Columns

```python
df[["Name", "Score"]]
```

This returns a new DataFrame.

---

### Filtering Rows

```python
df[df["Score"] > 85]
```

This filters rows based on a condition—an essential skill in feature engineering and data cleaning.

---

## 6. How Pandas Fits into AI Pipelines

A typical AI data pipeline looks like this:

1. Load dataset using Pandas
2. Inspect structure with `head()`, `info()`, `describe()`
3. Clean and transform data
4. Convert to NumPy arrays
5. Feed into a model

Pandas acts as the structured “data preparation layer” before numerical computation.

---

## 7. Common Beginner Mistakes

* Skipping inspection steps
* Ignoring missing values
* Assuming data types are correct
* Modifying data without understanding indexing

Pandas is powerful, but incorrect assumptions can propagate errors into models.

---

## Key Takeaways

Pandas provides structured data handling for AI workflows. A Series represents a single labeled column, while a DataFrame represents a full table. CSV files can be loaded easily with `read_csv()`. Inspection methods like `head()`, `tail()`, `info()`, and `describe()` are essential for understanding datasets before modeling. Mastery of Pandas is the bridge between raw data and machine learning.

**Mental model:**
Series = column.
DataFrame = table.
`read_csv()` loads.
Inspection prevents mistakes.

---

## Additional Reading

* Pandas Official Documentation:
  [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

* Pandas 10-Minute Introduction:
  [https://pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)

* Data Inspection Best Practices:
  [https://realpython.com/pandas-python-explore-dataset/](https://realpython.com/pandas-python-explore-dataset/)
