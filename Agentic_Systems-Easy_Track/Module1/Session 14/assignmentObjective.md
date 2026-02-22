# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

What is returned when you select a single column using:

```python
df["Score"]
```

A) A DataFrame
B) A Series
C) A NumPy array
D) A list

**Correct answer:** B

**Explanation:**
Selecting a single column using bracket notation returns a **Series**, which represents one labeled column from the DataFrame. It is not a DataFrame unless double brackets are used.

---

### **2. (MCQ)**

What is returned when selecting multiple columns using:

```python
df[["Name", "Score"]]
```

A) A Series
B) A dictionary
C) A DataFrame
D) A tuple

**Correct answer:** C

**Explanation:**
Using double brackets with a list of column names returns a new **DataFrame** containing only those columns. This is commonly used when selecting features for modeling.

---

### **3. (MCQ)**

What is the primary difference between `iloc` and `loc`?

A) `iloc` filters rows, `loc` sorts rows
B) `iloc` selects by position, `loc` selects by label
C) `iloc` selects columns only
D) `loc` works only with integers

**Correct answer:** B

**Explanation:**
`iloc` uses numerical position (index-based selection), while `loc` uses label-based indexing. If your DataFrame has meaningful labels (IDs, names, timestamps), `loc` is typically used.

---

### **4. (MCQ)**

What does the following code return?

```python
df.iloc[0:3]
```

A) The first three columns
B) The first three rows
C) The last three rows
D) A sorted DataFrame

**Correct answer:** B

**Explanation:**
`iloc` performs position-based indexing. The slice `0:3` returns rows at positions 0, 1, and 2 (the first three rows).

---

### **5. (MCQ)**

Why must parentheses be used when combining Boolean conditions in Pandas?

A) To improve performance
B) Because Pandas requires explicit grouping for element-wise operations
C) To convert DataFrames into Series
D) To enable sorting

**Correct answer:** B

**Explanation:**
When combining conditions using `&` or `|`, each condition must be enclosed in parentheses. This ensures correct element-wise evaluation and avoids ambiguity in operator precedence.

---

### **6. (MCQ)**

Which operator should be used instead of `and` when combining Pandas Boolean conditions?

A) `and`
B) `&&`
C) `&`
D) `|`

**Correct answer:** C

**Explanation:**
Pandas performs element-wise logical operations across Series. Therefore, `&` must be used instead of Python’s `and`. Using `and` will raise an error.

---

### **7. (MCQ)**

What does the following expression do?

```python
df[~(df["Passed"] == True)]
```

A) Sorts the DataFrame
B) Selects rows where Passed is True
C) Negates the entire DataFrame
D) Filters rows where Passed is False

**Correct answer:** D

**Explanation:**
The `~` operator negates a Boolean Series. This expression selects rows where the condition inside parentheses is False — effectively filtering rows where `"Passed"` is False.

---

### **8. (MCQ)**

What does this code accomplish?

```python
df.sort_values("Score", ascending=False)
```

A) Filters scores greater than 0
B) Sorts rows by Score in descending order
C) Removes duplicate scores
D) Groups rows by Score

**Correct answer:** B

**Explanation:**
`sort_values()` sorts the DataFrame based on a column. Setting `ascending=False` orders the rows from highest to lowest score, which is useful for ranking and analysis.
