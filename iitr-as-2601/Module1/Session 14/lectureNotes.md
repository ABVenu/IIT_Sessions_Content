# Pandas: Selection & Filtering

## What You’ll Learn

In this lesson, you’ll learn how to query structured data using Pandas. You’ll understand how to select specific columns, access rows using indexing methods, filter data using Boolean logic, and sort DataFrames to reveal patterns. These techniques allow you to answer precise questions from raw datasets—an essential skill in AI and data-driven systems.

![Selection](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/e366bcf9-cda6-4741-aa3d-f085d3a6fbb7/XcvvbOdXxdlmsnPf.png)

---

## 1. Why Selection and Filtering Matter

Loading a dataset is only the beginning. The real power of Pandas lies in its ability to answer questions such as:

- Which users have scores above 90?
- What are the top-performing models?
- Which rows contain missing data?
- How does a subset of the dataset behave?

AI workflows depend on slicing and querying data correctly before training models. If you filter incorrectly, your model trains on the wrong data. If you sort incorrectly, you misinterpret results.

Precision in selection is precision in analysis.

---

## 2. Selecting Columns

### Selecting a Single Column

Columns in a DataFrame are selected using bracket notation:

```python
import pandas as pd

df = pd.read_csv("data.csv")

scores = df["Score"]
````

This returns a **Series**, not a DataFrame.

Selecting a column is one of the most common operations in data analysis and feature engineering.

---

### Selecting Multiple Columns

To select multiple columns, use a list inside brackets:

```python
subset = df[["Name", "Score"]]
```

This returns a new **DataFrame** containing only those columns.

This pattern is used frequently when:

* Choosing features for a model
* Creating smaller working subsets
* Dropping irrelevant columns

---

## 3. Row Indexing

Rows can be accessed using either position-based indexing (`iloc`) or label-based indexing (`loc`). Understanding the difference is important.

---

### Position-Based Indexing: `iloc`

`iloc` selects rows by numerical position.

```python
first_row = df.iloc[0]
```

This selects the first row.

Selecting multiple rows:

```python
df.iloc[0:3]
```

This returns the first three rows.

Use `iloc` when:

* You care about position
* You are slicing by index number
* You are working with ordered data

---

### Label-Based Indexing: `loc`

`loc` selects rows using labels.

```python
df.loc[0]
```

If your DataFrame has custom indices:

```python
df = df.set_index("Name")
df.loc["Alice"]
```

Use `loc` when:

* Your index carries meaning
* You are filtering by labels

In professional AI systems, meaningful indices (such as IDs or timestamps) are common.

---

## 4. Boolean Filtering

Boolean filtering is one of the most powerful features of Pandas. It allows you to select rows based on conditions.

---

### Basic Filtering

```python
high_scores = df[df["Score"] > 85]
```

This returns all rows where the Score column is greater than 85.

Behind the scenes:

* `df["Score"] > 85` produces a Boolean Series
* Pandas keeps rows where the value is `True`

---

### Multiple Conditions

To combine conditions, use logical operators:

```python
filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
```

Important:

* Use `&` instead of `and`
* Use `|` instead of `or`
* Wrap each condition in parentheses

This difference exists because Pandas operates element-wise across Series.

---

### Negation

To filter rows that do not meet a condition:

```python
not_passed = df[~(df["Passed"] == True)]
```

The `~` operator negates a Boolean Series.

---

### Why Boolean Filtering Is Essential in AI

Filtering allows you to:

* Remove invalid samples
* Separate training and validation sets
* Identify anomalies
* Segment users or predictions

Most real-world AI data preparation relies heavily on Boolean filtering.

---

## 5. Sorting DataFrames

Sorting reveals structure and patterns.

---

### Sorting by One Column

```python
sorted_df = df.sort_values("Score")
```

To sort in descending order:

```python
sorted_df = df.sort_values("Score", ascending=False)
```

Sorting is often used to:

* Rank predictions
* Identify top-performing records
* Analyze extremes

---

### Sorting by Multiple Columns

```python
df.sort_values(["Passed", "Score"], ascending=[False, False])
```

This sorts first by Passed status, then by Score.

---

### Sorting by Index

```python
df.sort_index()
```

Useful when index order matters.

---

## 6. Combining Selection and Filtering

A typical AI-style query might look like this:

```python
top_students = (
    df[df["Score"] > 85]
      [["Name", "Score"]]
      .sort_values("Score", ascending=False)
)
```

This chain:

1. Filters rows
2. Selects columns
3. Sorts results

This pattern mirrors how analysts and engineers query structured data efficiently.

---

## 7. Common Beginner Mistakes

* Forgetting parentheses around Boolean conditions
* Using `and` instead of `&`
* Confusing `loc` and `iloc`
* Overwriting the original DataFrame unintentionally

These are normal early mistakes and improve with practice.

---

## Key Takeaways

Selection and filtering allow you to query data precisely. Columns are selected using brackets, rows can be accessed by position or label, Boolean conditions filter subsets, and sorting reveals structure. These operations are fundamental to AI data preparation and analysis.

**Mental model:**
Select columns.
Index rows.
Filter with logic.
Sort to understand.

---

## Additional Reading

* Pandas Indexing and Selecting Data:
  [https://pandas.pydata.org/docs/user_guide/indexing.html](https://pandas.pydata.org/docs/user_guide/indexing.html)

* Boolean Indexing in Pandas:
  [https://realpython.com/pandas-boolean-indexing/](https://realpython.com/pandas-boolean-indexing/)

* Sorting DataFrames:
  [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
