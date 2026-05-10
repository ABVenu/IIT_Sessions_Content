# Assignment — Objective (Pandas: DataFrames, aggregation & cleanup)

**Instructions:** Answer all questions. For multiple-select questions (MSQ), select **all** options that apply.

**Scope:** This assignment covers: creating and reading DataFrames, `read_csv`, selecting and filtering, `drop` with `axis=1`, column aggregations (`sum`, `mean`, `count`, `min`, `max`, `median`), `groupby`, `agg` (list, dict, named), `reset_index`, and NaN behaviour. **`merge` and joins are not used here.**

---

## Section A — Multiple Choice, Single Correct (MCQ)

### Q1 (Easy)

Ananya exports a small **monthly sales** sheet from her billing software as `sales_march.csv` (comma-separated). She wants a pandas table in Python with rows and columns she can filter and summarise. Which line correctly **loads** that file into a DataFrame called `sales`?

- A) `sales = pd.read_csv("sales_march.csv")`  
- B) `sales = pd.DataFrame("sales_march.csv")`  
- C) `sales = pd.load_csv("sales_march.csv")`  
- D) `sales = open("sales_march.csv")`  

**Answer Explanation (for Assess):**  
**Correct answer: A.** `pd.read_csv(...)` reads a CSV path and returns a DataFrame—the standard pandas API for loading comma-separated files.  
**B** is wrong: `pd.DataFrame(...)` expects tabular data (e.g. dict of lists), not a filename string. **C** is wrong: pandas does not use `load_csv` for this. **D** returns a raw file handle, not a DataFrame.

---

### Q2 (Easy)

Vikram has a DataFrame `df` with columns `Product`, `Units`, and `Price`. He wants to **remove** the column `Price` from his analysis copy and keep working with the result. By default, `drop` returns a new DataFrame. Which pattern is correct?

- A) `df.drop("Price")` and continue using `df`  
- B) `df = df.drop("Price", axis=1)`  
- C) `df.drop("Price", axis=0)`  
- D) `df.delete("Price")`  

**Answer Explanation (for Assess):**  
**Correct answer: B.** Columns are dropped with **`axis=1`**, and you should **assign back** (`df = ...`) unless you use `inplace=True`.  
**A** omits `axis=1` (pandas treats labels as row index by default) and may error or drop the wrong thing; even if it ran, without assignment the original `df` would not update as intended. **C** uses `axis=0` (rows), not columns. **D** is not a standard pandas DataFrame method for dropping columns.

---

### Q3 (Easy)

A `customers` DataFrame has a column `Age`. Riya wants only rows where age is **strictly greater than 25**. Which expression keeps just those rows?

- A) `customers["Age"] > 25`  
- B) `customers.filter(Age > 25)`  
- C) `customers[customers["Age"] > 25]`  
- D) `customers.loc["Age"] > 25`  

**Answer Explanation (for Assess):**  
**Correct answer: C.** Build a boolean Series with `customers["Age"] > 25`, then pass it inside `customers[...]` to filter rows.  
**A** is only the mask (True/False Series), not the filtered DataFrame. **B** is not the usual pattern for filtering rows with column conditions. **D** misuses `loc`—that is for labels, not “all rows where Age > 25”.

---

### Q4 (Easy)

Karan runs `df.groupby("City")["Sales"].mean()`. What happens to **`City`** in the **result**?

- A) `City` disappears completely  
- B) `City` becomes the **index** of the result Series  
- C) `City` stays a normal column with no index change  
- D) `City` is sorted alphabetically and dropped  

**Answer Explanation (for Assess):**  
**Correct answer: B.** After `groupby("City")`, the grouping key becomes the **index** of the aggregated output (until you `reset_index()`).  
**A** and **D** are wrong: the city values are still there as index labels. **C** is wrong until you call `.reset_index()`.

---

### Q5 (Moderate)

Neha has a DataFrame `emp` with columns `Age` and `Salary`. She wants employees who are **older than 30** **and** earn **more than 50,000**. Which line is **valid pandas** for row filtering?

- A) `emp[(emp["Age"] > 30) and (emp["Salary"] > 50000)]`  
- B) `emp[emp["Age"] > 30 and emp["Salary"] > 50000]`  
- C) `emp[(emp["Age"] > 30) & (emp["Salary"] > 50000)]`  
- D) `emp.where("Age > 30 and Salary > 50000")`  

**Answer Explanation (for Assess):**  
**Correct answer: C.** Use **`&`** between boolean Series and **wrap each condition in parentheses** so pandas evaluates the conditions element-wise.  
**A** and **B** use Python **`and`**, which does not combine two Series the way we need here. **D** is not the usual boolean-indexing pattern; `where` does not take a string expression like that.

---

### Q6 (Moderate)

Isha writes:

```python
report = df.groupby("Dept").agg(
    Total_Pay=("Salary", "sum"),
    Avg_Tenure=("Years", "mean"),
)
```

What is this style of `agg` called, and what is the main benefit?

- A) Dictionary aggregation; it always creates a MultiIndex on columns  
- B) Named aggregation; readable, business-style column names in one step  
- C) List aggregation; it can only apply one function per column  
- D) Split-apply-combine; it replaces the need for `groupby`  

**Answer Explanation (for Assess):**  
**Correct answer: B.** **Named aggregation** uses `NewName=("column", "function")` so the output columns are clear (e.g. `Total_Pay`) without awkward default names.  
**A** is wrong: a dict inside `.agg({...})` is different from this keyword form; MultiIndex is more typical when passing a **list** of functions on one column. **C** describes list-style `agg`, not this syntax. **D** is wrong: you still use `groupby` before `agg`.

---

## Section B — Multiple Select, Multiple Correct (MSQ)

*Select all correct options.*

### Q7 (Moderate — MSQ)

Which statements match typical pandas behaviour for **`groupby`** and related output?

- A) The grouping column(s) typically become the **index** of the aggregated result  
- B) `df.groupby("Region")["Sales"].sum()` returns one total **per region**  
- C) Calling `.reset_index()` can turn the group key back into a normal column  
- D) `groupby` always drops every row that contains **any** NaN in **any** column of the DataFrame  

**Answer Explanation (for Assess):**  
**Correct: A, B, C.**  
**A:** The group key moves to the index unless you reset it.  
**B:** That expression groups by `Region` and sums `Sales` within each group.  
**C:** `.reset_index()` is the standard way to promote the index back to a column.  
**D is incorrect:** By default, rows where the **grouping column** is NaN are excluded (`dropna=True` by default for the key). A NaN in some other column does not, by itself, cause `groupby` to drop the row.

---

### Q8 (Moderate — MSQ)

For a numeric column `s = df["Score"]`, which claims align with default pandas behaviour?

- A) `s.sum()` **skips** NaN values  
- B) `s.mean()` **skips** NaN values  
- C) `s.count()` counts **non-null** entries  
- D) `s.min()` always returns NaN if there is at least one NaN in the column  

**Answer Explanation (for Assess):**  
**Correct: A, B, C.**  
By default, `sum`, `mean`, `median`, `min`, `max`, and `count` on a Series skip NaN where applicable (`count` counts non-null values).  
**D is incorrect:** `min()` ignores NaN by default and returns the minimum of the non-null values (or NaN if the whole column is null).

---

### Q9 (Hard — MSQ)

Suppose `df` has columns `Team`, `Sales`, `Bonus`, and **`Rep`** (one salesperson id per row; no nulls). Arjun wants **one row per Team** with:

- total `Sales`  
- average `Bonus`  
- number of rows (headcount), using **`Rep`**

Which approaches are **valid** single-call patterns **after** `df.groupby("Team")`?

- A) `df.groupby("Team").agg({"Sales": "sum", "Bonus": "mean", "Rep": "count"})`  
- B) `df.groupby("Team").agg(Total_Sales=("Sales", "sum"), Avg_Bonus=("Bonus", "mean"), N=("Rep", "count"))`  
- C) `df.groupby("Team")["Sales"].agg(["sum", "mean"])` — this alone also returns average Bonus per Team  
- D) `df.groupby("Team")[["Sales", "Bonus"]].mean()` — this alone also returns total Sales per Team  

**Answer Explanation (for Assess):**  
**Correct: A, B.**  
**A** uses a **dictionary** `agg` to apply different functions to different columns in one grouped result.  
**B** uses **named aggregation** to get all three metrics with clear column names.  
**C is incorrect:** That aggregates only `Sales` with two functions; it does not compute Bonus mean or Rep count.  
**D is incorrect:** `mean()` on both columns does not produce **sum** of Sales; totals need `sum` (or a different aggregation).

---

### Q10 (Hard — MSQ)

Pooja runs:

```python
df.groupby("Store")["Revenue"].agg(["sum", "mean", "count"])
```

Which outcomes are **plausible** for this pattern?

- A) The result has **one row per Store**  
- B) The result may show **more than one summary column** (`sum`, `mean`, `count`)  
- C) Named aggregation with `Total=("Revenue","sum")` is the **only** way to avoid ever seeing more than one column of summaries  
- D) If she instead used `df.groupby("Store")[["Revenue", "Cost"]].agg(["sum", "mean"])`, the column index could become **hierarchical** (two levels)  

**Answer Explanation (for Assess):**  
**Correct: A, B, D.**  
**A:** Groupby produces one group per unique `Store` value.  
**B:** A list inside `agg` applies multiple functions—multiple summary columns.  
**C is incorrect:** Named aggregation is one **clean** way to get flat names; it is not the only possible approach in pandas. List-style `agg` on a single column is a common alternative; it may produce a MultiIndex unless you reshape or rename.  
**D:** Aggregating **multiple input columns** with a **list** of functions often yields a two-level column index (column × function).

---

*End of objective assignment.*
