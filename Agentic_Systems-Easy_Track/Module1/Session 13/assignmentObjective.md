# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

What is the primary structural difference between a Pandas Series and a DataFrame?

A) A Series is two-dimensional, a DataFrame is one-dimensional
B) A Series is unlabeled, a DataFrame is labeled
C) A Series represents one labeled column, a DataFrame represents a full table
D) A Series stores only strings

**Correct answer:** C

**Explanation:**
A **Series** is a one-dimensional labeled array (similar to a single column in Excel). A **DataFrame** is a two-dimensional table composed of multiple aligned Series, representing rows and columns.

---

### **2. (MCQ)**

What does `pd.read_csv("data.csv")` return?

A) A Python list
B) A NumPy array
C) A Pandas Series
D) A Pandas DataFrame

**Correct answer:** D

**Explanation:**
`read_csv()` reads a CSV file, parses its rows and columns, infers data types, and constructs a **DataFrame**, which is Pandas’ primary tabular data structure.

---

### **3. (MCQ)**

What is the main purpose of using `df.head()` immediately after loading a dataset?

A) To clean missing values
B) To check the first few rows and verify structure
C) To compute summary statistics
D) To sort the dataset

**Correct answer:** B

**Explanation:**
`head()` displays the first few rows of the dataset. This helps verify column names, formatting, and basic structure before performing further analysis or modeling.

---

### **4. (MCQ)**

Which method provides column data types and non-null counts?

A) `df.describe()`
B) `df.tail()`
C) `df.info()`
D) `df.columns()`

**Correct answer:** C

**Explanation:**
`info()` displays essential structural information, including column names, data types, and counts of non-null values. This is critical in AI workflows because incorrect data types can silently break models.

---

### **5. (MCQ)**

What does `df.describe()` return for numerical columns?

A) Only the mean
B) Column names
C) Summary statistics including mean, std, min, max, and quartiles
D) Missing values

**Correct answer:** C

**Explanation:**
`describe()` provides descriptive statistics such as count, mean, standard deviation, minimum, maximum, and quartiles. This helps identify outliers, scale differences, and distribution characteristics.

---

### **6. (MCQ)**

What is returned when you execute `df["Score"]`?

A) A Python list
B) A NumPy array
C) A Series
D) A DataFrame

**Correct answer:** C

**Explanation:**
Selecting a single column using bracket notation returns a **Series**, which represents one labeled column from the DataFrame.

---

### **7. (MCQ)**

What does the following code return?

```python
df[["Name", "Score"]]
```

A) A Series
B) A DataFrame with two columns
C) A NumPy matrix
D) A tuple

**Correct answer:** B

**Explanation:**
Selecting multiple columns using double brackets returns a **new DataFrame** containing only the specified columns.

---

### **8. (MCQ)**

What does the following expression do?

```python
df[df["Score"] > 85]
```

A) Sorts the dataset
B) Updates the "Score" column
C) Filters rows where Score is greater than 85
D) Deletes rows

**Correct answer:** C

**Explanation:**
This is boolean indexing. It filters the DataFrame and returns only rows where the condition `Score > 85` is true. This technique is widely used in feature engineering and data cleaning.
