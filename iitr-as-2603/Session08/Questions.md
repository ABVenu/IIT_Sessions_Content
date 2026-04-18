# Practice Questions — Pandas: CSV, DataFrames, Selection, Filtering, Sorting, Missing Data

*Concepts: `pd.read_csv`, DataFrame structure, inspection (`head`, `tail`, `shape`, `info`), column selection, `loc` vs `iloc`, `set_index` / `reset_index`, boolean filtering, multi-condition filters, `sort_values`, `isna` / `notna`, `fillna`, `dropna`.*

---

## Objective Questions (8)

### Easy

**Q1 (Single Correct).** What does **CSV** stand for, and how are columns usually separated in a typical CSV file?

- (A) Comma-Separated Values; columns are separated by commas
- (B) Compressed Spreadsheet Values; columns are separated by tabs
- (C) Character-Separated Variables; columns are separated by semicolons only
- (D) Column-Sorted Values; columns are separated by pipes

**Answer:** **(A)**  
CSV is plain text: one row per line, fields often separated by commas; a header row with column names is common.

---

**Q2 (Single Correct).** After `import pandas as pd`, which call loads a local file `data.csv` into a **DataFrame** using the default comma separator and first row as column names?

- (A) `pd.load_csv('data.csv')`
- (B) `pd.read_csv('data.csv')`
- (C) `pd.DataFrame.from_csv('data.csv')`
- (D) `pd.open('data.csv')`

**Answer:** **(B)**  
`pd.read_csv()` is the standard way to parse CSV text into a DataFrame.

---

**Q3 (Multiple Correct).** Which attributes or properties of a **DataFrame** `df` correctly describe its structure or contents?

- (A) `df.shape` returns the number of rows and columns as a tuple
- (B) `df.columns` holds the column labels
- (C) `df.values` is a NumPy array of the data **without** column names in the array itself
- (D) `df.dtypes` returns a single scalar describing the dtype of the entire DataFrame

**Answer:** **(A), (B), (C)**  
`df.dtypes` is a **Series** (one dtype per column), not one scalar for the whole frame.

---

### Medium

**Q4 (Single Correct).** What does **`df.info()`** primarily show you?

- (A) Only the first five rows of the DataFrame
- (B) A concise summary: index range, column names, **non-null counts**, dtypes, and approximate memory use
- (C) Only the list of column names, with no dtype or missing-value information
- (D) A correlation matrix for all numeric columns

**Answer:** **(B)**  
**`info()`** is a standard way to see structure and **where values are missing** (via non-null counts), along with dtypes.

---

**Q5 (Multiple Correct).** For row selection, which statements about **`.loc`** and **`.iloc`** are **true**?

- (A) `.loc` selects by **label**; `.iloc` selects by **integer position**
- (B) Label-based slicing with `.loc` is **inclusive** of both endpoints
- (C) Integer slicing with `.iloc` follows Python convention: the **stop** index is **exclusive**
- (D) `.iloc[0]` and `.loc[0]` always refer to the same row in every DataFrame

**Answer:** **(A), (B), (C)**  
If the index is not a default `0,1,2,...` or labels differ from positions, `.loc[0]` and `.iloc[0]` need not match.

---

**Q6 (Single Correct).** You want rows where **`Department`** is **`'Engineering'`** **and** **`Salary`** is **greater than 70000**. Which expression is **valid** in Pandas?

- (A) `df[df['Department'] == 'Engineering' and df['Salary'] > 70000]`
- (B) `df[(df['Department'] == 'Engineering') & (df['Salary'] > 70000)]`
- (C) `df[df['Department'] == 'Engineering' | df['Salary'] > 70000]`
- (D) `df.filter(Department='Engineering', Salary>70000)`

**Answer:** **(B)**  
Use **bitwise** `&` / `|` with **parentheses** around each condition; Python `and`/`or` do not work element-wise on Series.

---

### Hard

**Q7 (Multiple Correct).** A DataFrame has a column **`State`** with values like `'NY'`, `'NJ'`, `'CA'`. You want all rows where **`State`** is one of **`'NY'`**, **`'NJ'`**, or **`'CT'`**. Which approaches are **appropriate**?

- (A) `df[df['State'].isin(['NY', 'NJ', 'CT'])]`
- (B) `df[(df['State'] == 'NY') | (df['State'] == 'NJ') | (df['State'] == 'CT')]`
- (C) `df[df['State'] == 'NY' or 'NJ' or 'CT']`
- (D) `df[df['State'] in ['NY', 'NJ', 'CT']]`

**Answer:** **(A), (B)**  
`.isin()` is idiomatic for many OR conditions; chained `|` with parentheses also works. `(C)` and `(D)` are invalid or wrong for Series element-wise checks.

---

**Q8 (Single Correct).** You call `df.sort_values(by=['Department', 'Salary'], ascending=[True, False])`. What does this do?

- (A) Sorts first by `Department` ascending, then by `Salary` descending within each department
- (B) Sorts only by `Department` and ignores `Salary`
- (C) Sorts `Department` descending and `Salary` ascending
- (D) Raises an error because two columns cannot be sorted together

**Answer:** **(A)**  
`by` lists columns in sort priority; `ascending` is parallel: first key A→Z, second key high→low per group.

---

## Subjective Question (1)

**Difficulty:** Medium to Hard  
**Type:** Implementation (Pandas coding)

### Q9 — Question

The file **`orders.csv`** has the following contents (create this file locally or build the same table with **`pd.DataFrame`**):

```text
order_id,customer_id,product,city,amount,ship_date
1,C01,Widget A,New York,100.0,2024-01-10
2,C02,Widget B,,50.5,2024-01-11
3,C01,Widget A,New York,,2024-01-12
4,C03,Widget C,Los Angeles,200.0,2024-01-13
5,C02,Widget B,Mumbai,75.0,2024-01-14
```

**Tasks:**

1. Load **`orders.csv`** into **`df`** with **`pd.read_csv`**.
2. **Structure and inspection:** print **`df.shape`**, **`df.head(3)`**, and **`df.info()`**. In one or two sentences, state what **`info()`** reveals about missing values in this dataset.
3. **Boolean indexing:** build **`df_ny`** — rows where **`city`** equals **`'New York'`** (use the actual column name from the file).
4. **Compound condition:** build **`df_high`** — rows where **`amount`** is present **and** **`amount` > 60** (use **`&`** and parentheses as needed).
5. **Sorting and index:** build **`df_sorted`** — sort by **`amount`** descending, put missing **`amount`** first via **`na_position`**, then apply **`reset_index(drop=True)`**.
6. **Missing values — detection and handling:**  
   - Report per-column missing counts with **`isna().sum()`**.  
   - Build **`df_imputed`**: copy **`df`**; replace missing **`amount`** with the **mean** of **`amount`** (computed from non-null values); replace missing **`city`** with the string **`'Unknown'`**.  
   - Build **`df_dropped`**: starting from **`df`**, drop rows that have a missing **`amount`** using **`dropna`** with an appropriate **`subset`**.

**Submission Instructions**
- Code - Run - Test in any coding environment like VSCode and paste the answer in the answer box 


---

### Q9 — Sample detailed solution

```python
import pandas as pd

df = pd.read_csv("orders.csv")

print("shape:", df.shape)
print(df.head(3))
print(df.info())
# info() shows non-null counts: e.g. city 4/5, amount 4/5 — one missing in each.

df_ny = df[df["city"] == "New York"]

df_high = df[df["amount"].notna() & (df["amount"] > 60)]

df_sorted = df.sort_values(by="amount", ascending=False, na_position="first").reset_index(
    drop=True
)

print("nulls per column:\n", df.isna().sum())

df_imputed = df.copy()
mean_amount = df_imputed["amount"].mean()  # excludes NaN by default
df_imputed["amount"] = df_imputed["amount"].fillna(mean_amount)
df_imputed["city"] = df_imputed["city"].fillna("Unknown")

df_dropped = df.dropna(subset=["amount"])
```

**Checks:**

- **`df.shape`** → **(5, 6)**.
- **`df_ny`**: rows **`order_id`** **1** and **3**.
- **`df_high`**: **`order_id`** **1, 4, 5** (amounts 100, 200, 75).
- **`df_sorted`**: row with missing **`amount`** first if **`na_position='first'`**, then descending by **`amount`**.
- **`df_imputed`**: one missing **`amount`** filled with the mean of non-null amounts **(100, 50.5, 200, 75)** → **106.375**; missing **`city`** becomes **`'Unknown'`**.
- **`df_dropped`**: four rows (row with **`order_id`** **3** removed).

**Impute vs drop:** impute when you need to keep row count or every row matters for joins; drop when missingness means bad records or bias is worse than losing rows. **Mean imputation** pulls tails toward the center and can underestimate variance; outliers or skewed **`amount`** distributions make the mean a weak default.

---
