# Pandas: Data Cleanup & Combining DataFrames

In the previous session, we built a strong foundation with pandas. We created and read DataFrames, filtered rows using boolean conditions, applied basic aggregation functions like `sum()`, `mean()`, `count()`, `min()`, and `max()`, and then used **`groupby()`** to group data by categories. We also mastered the powerful **`agg()`** function, which lets you apply multiple different aggregation operations on multiple columns in one shot — for example, getting the total sales and average sales per product at the same time.

**In this session, we continue from where we left off. Here is what we will cover:**

- How to **rename columns** in a DataFrame (including result DataFrames from `groupby`)
- How to **drop columns and rows** from a DataFrame (including conditional row deletion)
- Understanding **`reset_index()`** and when to use it
- How to **combine two DataFrames** using `pd.merge()` — and the four types of merges: Inner, Left, Right, and Outer
- How `df.join()` works and how it differs from `pd.merge()`
- How to **chain multiple operations together** in a clean pipeline
- A brief peek into **why SQL is needed** and what is coming next

---

## Quick Recap: The `agg()` Function

Before we move to new topics, let us take a very quick look at what we covered at the end of the last session — the **`agg()`** function. This is important because we will use `rename()` on its output in just a few minutes.

- **Official Definition:** **`agg()`** (aggregate) is a pandas method that allows you to apply **multiple aggregation functions** to one or more columns of a grouped DataFrame in a single step.
- **In Simple Words:** Instead of writing three lines to get sum, mean, and max separately, `agg()` gives you all of them in one clean shot.
- **Real-Life Example:** In a company's monthly report, the manager wants to see the **total sales**, **average sales**, and **maximum units sold** — all per product category. Writing this three times would be messy. `agg()` does it in one command.

Here is our running dataset for the session — a small product sales table called `df`:

```python
# Import pandas library — always use 'pd' as the alias
import pandas as pd

# Create our running dataset: Product sales data
df = pd.DataFrame({
    "Product":  ["A", "B", "A", "C", "B", "A", "C", "B"],    # Product category
    "Region":   ["East", "West", "West", "East", "East", "East", "West", "West"],  # Region
    "Sales":    [300, 200, 380, 100, 130, 250, 400, 420],     # Sales in rupees
    "Units":    [10,  8,   15,  4,   5,   9,   16,  17],      # Units sold
    "Discount": [5,   8,   6,   4,   7,   5,   9,   6]        # Discount percentage
})

# Group by Product and apply multiple aggregations at once
result = df.groupby("Product")["Sales"].agg(["sum", "mean"])

# Print the result
print(result)
```

**How the code works:**

- `df.groupby("Product")` splits the data into groups — one group for Product A, one for B, one for C.
- `["Sales"]` tells pandas to focus only on the Sales column after grouping.
- `.agg(["sum", "mean"])` calculates **both sum and mean** for each product group in one step.
- The output is a **new DataFrame** with columns named `sum` and `mean` — these are generic names. Now, we need to rename them to something more meaningful, which is exactly what we learn next.

---

## Data Cleanup: Renaming Columns

When you apply `groupby()` + `agg()`, the result DataFrame has column names like **`sum`** and **`mean`**. If someone else reads your report, they will ask: *"Sum of what? Mean of what?"* That is where **renaming columns** becomes important.

- **Official Definition:** **`df.rename()`** is a pandas method that lets you change the column names (or index labels) of a DataFrame by passing a dictionary of old-name-to-new-name mappings.
- **In Simple Words:** You are giving new, more meaningful labels to existing columns — like crossing out a vague heading in a notebook and writing a better one.
- **Real-Life Example:** Imagine a student marksheet where columns are named `col1`, `col2`, `col3`. That is confusing. Renaming them to `Maths`, `Science`, `English` makes the report readable.

### Syntax

```python
# Basic syntax — return a NEW renamed DataFrame
df_new = df.rename(columns={"old_name": "new_name"})

# Use inplace=True to modify the original DataFrame directly
df.rename(columns={"old_name": "new_name"}, inplace=True)
```

### Example 1: Renaming Columns of an Aggregation Result

```python
# Import pandas
import pandas as pd

# Create our product sales DataFrame
df = pd.DataFrame({
    "Product":  ["A", "B", "A", "C", "B", "A", "C", "B"],
    "Region":   ["East", "West", "West", "East", "East", "East", "West", "West"],
    "Sales":    [300, 200, 380, 100, 130, 250, 400, 420],
    "Units":    [10,  8,   15,  4,   5,   9,   16,  17],
    "Discount": [5,   8,   6,   4,   7,   5,   9,   6]
})

# Step 1: Group by Product and calculate sum and mean of Sales
result = df.groupby("Product")["Sales"].agg(["sum", "mean"])

# Step 2: Print the result — columns are currently named 'sum' and 'mean'
print(result)

# Step 3: Rename 'sum' to 'Total Sales' and 'mean' to 'Average Sales'
result.rename(columns={"sum": "Total Sales", "mean": "Average Sales"}, inplace=True)

# Step 4: Print the renamed result
print(result)
```

**How the code works:**

- `agg(["sum", "mean"])` generates a result DataFrame with columns named exactly `sum` and `mean` by default.
- `result.rename(columns={"sum": "Total Sales", "mean": "Average Sales"}, inplace=True)` replaces those generic names with meaningful ones.
- `inplace=True` means the change happens **inside the same `result` variable** — no new variable is created.
- Without `inplace=True`, the renamed version is returned as a **new DataFrame** which you must store separately: `result_new = result.rename(...)`.

### Example 2: Renaming Columns of the Raw DataFrame

You can rename columns in any DataFrame, not just aggregation results. Here we rename columns directly in `df`:

```python
# Rename 'Sales' to 'Revenue', 'Units' to 'Quantity', 'Discount' to 'Discount Rate'
df.rename(columns={"Sales": "Revenue", "Units": "Quantity", "Discount": "Discount Rate"}, inplace=True)

# Print to verify changes
print(df)
```

**How the code works:**

- Each `"old_name": "new_name"` pair inside the dictionary tells pandas exactly what to change.
- `inplace=True` updates `df` itself, so there is no need to write `df = df.rename(...)`.
- You can rename **one column or multiple columns** in the same call — just add more key-value pairs to the dictionary.

> **Common Mistake:** Forgetting that `rename()` without `inplace=True` returns a copy. If you do `df.rename(...)` without storing the result, nothing changes in your original `df`.

---

## Understanding `reset_index()`

When you apply `groupby()`, the **group-by column** (like `Product`) becomes the **index** of the result DataFrame. You might notice that the column is sitting at the left edge, not behaving like a regular column. **`reset_index()`** converts that index back into a regular column.

- **Official Definition:** **`reset_index()`** resets the index of a DataFrame back to the default integer range (0, 1, 2, …) and moves the old index into a regular column.
- **In Simple Words:** It is like saying *"stop treating Product as a special label and just treat it like any other normal column again."*
- **Real-Life Example:** Imagine a shelf of files where the file names are the shelf labels. `reset_index()` takes those labels off the shelf and places them as content inside the files — now they are just regular data.

![Before and after reset_index(): group-by key as index vs regular column](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/Session10/lecture-notes-images/session10-reset-index-diagram.png)

```python
# Group by Product, get sum of Sales
result = df.groupby("Product")["Sales"].sum()

# 'Product' is currently the INDEX — reset it to become a normal column
result = pd.DataFrame(result)       # Convert Series to DataFrame first
result.reset_index(inplace=True)    # Move index back to a column

# Print the final result
print(result)
```

**How the code works:**

- After `groupby().sum()`, the output is a **pandas Series** (single column), not a DataFrame. We convert it using `pd.DataFrame(result)`.
- `reset_index()` moves the `Product` index into a proper column so the final table has clean row numbers (0, 1, 2, …) as its index.
- You may or may not apply `reset_index()` — it depends on how you want to use the result. If you plan to rename columns, working with a proper DataFrame (not a Series) is cleaner.

> **Pro Tip:** When your group-by result has **more than one column** (from `agg()`), it is already a DataFrame. `reset_index()` still converts the group-by column into a regular column.

---

## Data Cleanup: Dropping Columns and Rows

Cleaning data often means removing information you no longer need. `drop()` is the tool for this.

- **Official Definition:** **`df.drop()`** removes specified rows or columns from a DataFrame and returns a new DataFrame (or modifies in place if `inplace=True`).
- **In Simple Words:** It is like tearing a page out of a notebook or erasing a column from a register — the data is gone.
- **Real-Life Example:** Think of a payroll sheet that has 15 columns. HR only needs name, department, and salary for a report. The remaining 12 columns are dropped to create a clean, shareable sheet.

### Dropping a Single Column

```python
# Drop the 'Discount' column from df (returns a new DataFrame)
clean_df = df.drop(columns=["Discount"])

# Print columns remaining after the drop
print(clean_df.columns)
```

### Dropping Multiple Columns

```python
# Drop both 'Units' and 'Discount' at once
clean_df = df.drop(columns=["Units", "Discount"])

# Print columns remaining
print(clean_df.columns)
```

**How the code works:**

- Always pass column names as a **list** inside `columns=[...]`.
- Without `inplace=True`, `drop()` returns a **new DataFrame**. The original `df` is not changed unless you write `df = df.drop(...)`.
- The older way was `df.drop("Discount", axis=1)` — `axis=1` means columns. The newer, clearer way is `df.drop(columns=["Discount"])`. **Prefer the newer way** — it is more readable.

### Dropping Specific Rows by Index

```python
# Drop the rows at index position 0 and 2 (first and third rows)
clean_df = df.drop([0, 2])

# Print the cleaned DataFrame
print(clean_df)
```

### Conditional Row Deletion

This is very powerful. We drop all rows where `Sales` is less than 150:

```python
# Find the INDEX values of all rows where Sales < 150
rows_to_drop = df[df["Sales"] < 150].index   # Returns a list of index labels

# Drop those rows from df and store the result
result = df.drop(rows_to_drop)

# Print the cleaned result
print(result)
```

**How the code works:**

- `df[df["Sales"] < 150]` filters the DataFrame to show only rows where the Sales column value is less than 150.
- `.index` extracts the **index labels** (row numbers) of those matching rows — not the data itself.
- `df.drop(rows_to_drop)` removes those specific rows by their index labels.
- This is very useful in real data cleaning: you can remove all rows below a quality threshold, delete test data, or filter out incorrect entries.

> **Key Insight — `axis` parameter:** `axis=0` (the default) refers to rows. `axis=1` refers to columns. That is why when dropping rows, you do not need to mention `axis`. But when using the older syntax with just a name (not the `columns=` keyword), you must write `axis=1` to tell pandas you mean a column, not a row.

---

## Combining DataFrames: Why We Need Merge

So far we have been working with **one DataFrame at a time**. But in real-world applications, data is spread across **multiple tables**. For example:

- An e-commerce app has an **orders table** (Order ID, Customer ID, Amount)
- And a **customers table** (Customer ID, Name, City)

To find out *"Which city placed the most orders?"* you need **both tables together**. You need to combine them based on the common column (`Customer ID`). This is called **merging** (or joining).

- **Official Definition:** **Merging** is the process of combining two DataFrames into one by matching rows based on a **common column** (called the key column).
- **In Simple Words:** It is like matching two registers using the Roll Number. Once matched, you can see the student's name (from one register) and their marks (from another register) side by side.
- **Real-Life Example:** Think of **Swiggy**. There is one database for orders and another for restaurants. When you track your order, Swiggy **merges** both to show you: Order #4567 is from Domino's (Koramangala branch) and it was placed at 8 PM.

### Our Running Example: Orders and Customers

For all merge examples, we will use these two DataFrames:

```python
# Import pandas
import pandas as pd

# DataFrame 1: Orders table — who ordered what and how much they paid
df1 = pd.DataFrame({
    "OrderID":    [1, 2, 3, 4],          # Unique ID for each order
    "CustomerID": ["C01", "C02", "C01", "C04"],  # Who placed the order
    "Amount":     [250, 300, 150, 500]   # Amount paid in rupees
})

# DataFrame 2: Customers table — customer details
df2 = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04"],  # Customer ID (matches df1)
    "Name":       ["Alice", "Bob", "Charlie", "Dave"],  # Customer name
    "City":       ["New York", "Mumbai", "Pune", "Chennai"]  # City where they live
})

print("Orders Table:")
print(df1)
print("\nCustomers Table:")
print(df2)
```

**How the code works:**

- `df1` (Orders) has 4 orders. Notice that C01 appears twice (Alice placed 2 orders) and C03 never appears (Charlie placed no orders).
- `df2` (Customers) has 4 customers, including Charlie who has no orders.
- Both DataFrames share the **`CustomerID`** column — this is the **key** used for merging.
- All four types of merges we cover next use these same two DataFrames.

---

## Types of Merges (Joins)

There are four main types of merges in pandas, and each one answers a different business question.

![Four merge types in pandas: Inner, Left, Right, and Outer — what each keeps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/Session10/lecture-notes-images/session10-merge-types-four-joins.png)

### 1. Inner Join — Only Matching Rows from Both Tables

- **Official Definition:** **Inner join** returns only the rows where the key column has a **matching value in both DataFrames**.
- **In Simple Words:** Only keep rows that exist in **both** tables. If a customer has no orders, skip them. If an order has no customer, skip it.
- **Real-Life Example:** It is like finding students who are **both** present in the attendance register **AND** the marks register. Anyone missing from either list is excluded.

```python
# Inner join: only rows where CustomerID exists in BOTH df1 and df2
result_inner = pd.merge(df1, df2, on="CustomerID", how="inner")

# Print the merged result
print(result_inner)
```

**How the code works:**

- `pd.merge(df1, df2, ...)` — `df1` is the **left** DataFrame, `df2` is the **right** DataFrame.
- `on="CustomerID"` tells pandas which column is the **key** — it must exist in **both** DataFrames with the **same name**.
- `how="inner"` specifies the join type. This is also the **default** if you don't mention `how`.
- **Result:** 4 rows — Orders 1, 2, 3, 4 map to Alice, Bob, Alice, Dave respectively (C01=Alice, C02=Bob, C04=Dave). All 4 orders have matching customers in df2, so all 4 rows appear.
- Charlie (C03) is **only in df2** (Customers) — since Charlie has no orders in df1, Charlie is **completely excluded** from the inner join result.

> **Key Rule for Inner Join:** A row is included **only if** the CustomerID appears in **both tables**. Missing from either side = excluded.

### 2. Left Join — All Rows from Left, Matching Rows from Right

- **Official Definition:** **Left join** returns **all rows from the left DataFrame**, plus matching rows from the right. Where there is no match on the right, the right-side columns are filled with **NaN** (null/missing).
- **In Simple Words:** Keep everything from the left table. If the right table has matching data, bring it in. If not, put blank/NaN there.
- **Real-Life Example:** A teacher has a **list of all students** (left). She wants to add their exam scores (right). If a student was absent during the exam, their score column shows **NaN** — but the student is still listed.

```python
# Left join: ALL rows from df1 (orders), matching rows from df2 (customers)
result_left = pd.merge(df1, df2, on="CustomerID", how="left")

# Print the result
print(result_left)
```

**How the code works:**

- All 4 rows of `df1` (orders) are **guaranteed** to appear in the result.
- For each order, pandas looks up the matching `CustomerID` in `df2` to get Name and City.
- In our current dataset, all 4 CustomerIDs (C01, C02, C01, C04) have matches in df2 — so no NaN appears here.
- **If we had an order from C05** (a deactivated customer not in df2), that row would still appear, but `Name` and `City` would be **NaN**.

> **Key Rule for Left Join:** Every row from the **left DataFrame is always present** in the result. Right-side columns will be NaN for rows with no match.

### 3. Right Join — All Rows from Right, Matching Rows from Left

- **Official Definition:** **Right join** returns **all rows from the right DataFrame**, plus matching rows from the left. Where there is no match on the left, the left-side columns are filled with **NaN**.
- **In Simple Words:** This is the mirror image of left join. The **right table is the priority** — every row from it is kept.
- **Real-Life Example:** HR has a **list of all departments** (right). They want to map it to employee names (left). Even departments with no employees are included — with NaN in the name column.

```python
# Right join: ALL rows from df2 (customers), matching rows from df1 (orders)
result_right = pd.merge(df1, df2, on="CustomerID", how="right")

# Print the result
print(result_right)
```

**How the code works:**

- All 4 rows of `df2` (customers) are **guaranteed** to appear in the result.
- Charlie (C03) has **no orders** in df1. So in the result, Charlie appears but `OrderID` and `Amount` are **NaN**.
- Alice (C01) placed 2 orders — so she appears **twice** in the result (once for each order).
- Dave (C04) placed 1 order — appears once with order details filled in.

> **Key Rule for Right Join:** Every row from the **right DataFrame is always present** in the result. Left-side columns will be NaN for rows with no match.

### 4. Outer Join — All Rows from Both Tables

- **Official Definition:** **Outer join** (also called Full Outer Join) returns **all rows from both DataFrames**. Where there is no match on either side, NaN is used to fill the missing columns.
- **In Simple Words:** Keep everything from both tables. No one gets excluded. If there is no matching data, fill it with NaN.
- **Real-Life Example:** You are combining two guest lists from two different parties. **Everyone from both lists** is included in the final combined list — even if they attended only one party (their info from the other party is blank/NaN).

```python
# Outer join: ALL rows from BOTH df1 and df2
result_outer = pd.merge(df1, df2, on="CustomerID", how="outer")

# Print the result
print(result_outer)
```

**How the code works:**

- Every row from `df1` (orders) is included. Every row from `df2` (customers) is included.
- Charlie (C03) has no orders → `OrderID` and `Amount` are NaN.
- If there were a C05 order not in df2 → `Name` and `City` would be NaN.
- This is the **most inclusive** join — it leaves no data behind, using NaN for everything that cannot be matched.

### Quick Comparison of All Four Join Types

| Join Type | What It Keeps | NaN Appears When |
| :--- | :--- | :--- |
| **Inner** | Only rows matching in **both** tables | Never (unmatched rows are dropped) |
| **Left** | All rows from **left** + matched from right | Right-side columns for unmatched left rows |
| **Right** | All rows from **right** + matched from left | Left-side columns for unmatched right rows |
| **Outer** | All rows from **both** tables | Both sides — wherever there is no match |

---

## Merging When Column Names Are Different

In our example, both DataFrames had the column named `CustomerID`. But in real projects, the **same data might have different column names** in different tables.

For example: `df1` calls it `"CustID"` and `df2` calls it `"CustomerID"`. You cannot use `on=` in this case. Instead, use **`left_on`** and **`right_on`**:

```python
# Example: key column has different names in each DataFrame
df1_renamed = df1.rename(columns={"CustomerID": "CustID"})  # Rename to simulate different names

# Use left_on and right_on when column names differ
result = pd.merge(df1_renamed, df2, left_on="CustID", right_on="CustomerID", how="inner")

# Print the result
print(result)
```

**How the code works:**

- `left_on="CustID"` says: the key column in the **left DataFrame (df1_renamed)** is called `CustID`.
- `right_on="CustomerID"` says: the key column in the **right DataFrame (df2)** is called `CustomerID`.
- Both columns will appear in the result (CustID and CustomerID are both included). You can drop one of them afterwards.

---

## The `suffixes` Parameter

When both DataFrames have a **non-key column with the same name** (e.g., both have a column called `Name`), pandas cannot distinguish them in the merged result. It automatically adds suffixes `_x` and `_y`. You can control these:

```python
# If both DataFrames had a column called 'ID', pandas would add _x and _y
# To customize the suffixes, use the 'suffixes' parameter
result = pd.merge(df1, df2, on="CustomerID", how="inner", suffixes=("_order", "_customer"))

# Now overlapping column names would be like 'ID_order' and 'ID_customer' instead of 'ID_x' and 'ID_y'
print(result)
```

**How the code works:**

- `suffixes=("_order", "_customer")` tells pandas to append `_order` for columns from `df1` and `_customer` for columns from `df2` when there is a name clash.
- This makes the final merged DataFrame much more readable — you always know which column belongs to which original table.

---

## `df.join()` — The Older Join Method

Besides `pd.merge()`, pandas has a method called `df.join()`. It is an **older** way to combine DataFrames and works based on **index columns**.

- **Official Definition:** **`df.join()`** combines two DataFrames based on their **index** (row labels), not on a regular column.
- **In Simple Words:** `join()` is an older sibling of `merge()`. It works only if the linking data is in the **index** of the DataFrame, not a regular column.
- **Key difference:** `pd.merge()` is **flexible** — works on any column. `df.join()` works **only on the index** by default. The default join type in `join()` is **left**, while in `merge()` it is **inner**.

```python
# Step 1: Set CustomerID as the index for BOTH DataFrames
orders_indexed = df1.set_index("CustomerID")      # CustomerID becomes index of orders
customers_indexed = df2.set_index("CustomerID")   # CustomerID becomes index of customers

# Step 2: Join using the .join() method (left join by default)
result_join = orders_indexed.join(customers_indexed)

# Print the result
print(result_join)
```

**How the code works:**

- `set_index("CustomerID")` moves the `CustomerID` column out of regular data and makes it the **row label (index)** of the DataFrame.
- `orders_indexed.join(customers_indexed)` then matches rows based on these index labels and combines the two tables.
- **Recommendation:** In practice, **use `pd.merge()`** — it is more flexible, more readable, and works on any column without needing `set_index()`. Use `join()` only if you are specifically working with index-based DataFrames.

---

## Method Chaining — Building a Pipeline

One of the most powerful things about pandas is that you can **chain multiple operations together** in one clean, flowing statement. Instead of storing intermediate results in many different variables, you can connect steps with a `.` (dot).

- **Official Definition:** **Method chaining** is the practice of calling multiple methods one after another on the same object, where each method returns the DataFrame for the next method to work on.
- **In Simple Words:** It is like an assembly line in a factory. The raw material goes in, passes through station 1 (merge), then station 2 (groupby), then station 3 (rename), and the finished product comes out at the end.

![Method chaining: merge → groupby → agg → reset_index → rename → sort_values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/Session10/lecture-notes-images/session10-method-chaining-pipeline.png)

### Example: A Full Business Analysis Pipeline

*Question: For each city, what is the total revenue and number of orders? Show cities sorted by total revenue (highest first).*

```python
# Import pandas
import pandas as pd

# Orders DataFrame
df1 = pd.DataFrame({
    "OrderID":    [1, 2, 3, 4],
    "CustomerID": ["C01", "C02", "C01", "C04"],
    "Amount":     [250, 300, 150, 500]
})

# Customers DataFrame
df2 = pd.DataFrame({
    "CustomerID": ["C01", "C02", "C03", "C04"],
    "Name":       ["Alice", "Bob", "Charlie", "Dave"],
    "City":       ["Delhi", "Mumbai", "Pune", "Chennai"]
})

# Full pipeline using method chaining
result = (
    pd.merge(df1, df2, on="CustomerID", how="inner")   # Step 1: Merge orders with customers
      .groupby("City")                                  # Step 2: Group by city
      .agg(                                             # Step 3: Aggregate
          Total_Revenue=("Amount", "sum"),              #   Total amount per city
          Order_Count=("OrderID", "count")              #   Number of orders per city
      )
      .reset_index()                                    # Step 4: Make City a regular column
      .rename(columns={"City": "Capital City"})         # Step 5: Rename 'City' column
      .sort_values(by="Total_Revenue", ascending=False) # Step 6: Sort by revenue (highest first)
)

# Print the final result
print(result)
```

**How the code works:**

- **Step 1 (merge):** Combines orders and customer data on `CustomerID`. Only inner-matched rows are kept.
- **Step 2 (groupby):** Groups the merged data by `City`.
- **Step 3 (agg):** For each city, calculates the **total revenue** (sum of Amount) and **order count** (count of OrderID).
- **Step 4 (reset_index):** Moves `City` from the index back into a regular column.
- **Step 5 (rename):** Renames `City` to `Capital City` for the output report.
- **Step 6 (sort_values):** Sorts cities so the **highest revenue city** appears at the top.
- The parentheses `(...)` around the whole block are just to allow writing it across multiple lines without a `\` backslash. This is a clean Python style for long chains.

> **Common Mistake with chaining + groupby:** After `groupby()["SomeColumn"].sum()`, the result is a **pandas Series** (single column), not a DataFrame. If you target a single column, use `agg()` instead, which always returns a DataFrame and works better in a chain.

---

## Common Mistakes & Fixes

Let us quickly look at the mistakes students often make in these operations, so you do not repeat them.

- **`rename()` without `inplace=True` or reassignment:** `df.rename(columns={"A":"B"})` does **not change** `df`. You must either write `df = df.rename(...)` or add `inplace=True`.
- **Dropping a column without `columns=` keyword:** `df.drop("Discount")` will try to drop a **row** labelled "Discount", not the column. Always use `df.drop(columns=["Discount"])` or `df.drop("Discount", axis=1)`.
- **Using `on=` when column names are different:** If `df1` calls it `CustID` and `df2` calls it `CustomerID`, `on="CustomerID"` will fail on `df1`. Use `left_on` and `right_on` instead.
- **Forgetting that `groupby()` on a single column returns a Series:** After `df.groupby("X")["Y"].sum()`, the result is a Series. Converting to DataFrame with `pd.DataFrame(...)` before chaining further operations avoids confusion.
- **Using `join()` without setting the index:** `df1.join(df2)` will not work as expected if the linking column is not the index. Either `set_index()` first, or just use `pd.merge()`.
- **Not knowing the default join types:** `pd.merge()` defaults to **inner join**. `df.join()` defaults to **left join**. Forgetting this leads to unexpected missing rows.
- **Forgetting `NaN` means missing, not zero:** In a left join, if a row from the left has no match in the right, the right-side columns show **NaN** — not 0. Treating NaN as 0 in calculations gives wrong results.

---

## A Brief Look Ahead: Why SQL is Next

In today's session, all our data was **hard-coded** inside the Python program. Those DataFrames live in your **RAM (temporary memory)**. The moment you close your terminal or restart VS Code, the data is **gone forever**.

![Pandas data in RAM (session memory) vs SQL in a database (persistent storage)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/Session10/lecture-notes-images/session10-pandas-ram-vs-sql-database.png)

In real companies, data is never hard-coded. Millions and billions of rows are stored **permanently** in **databases** — special software designed to store, protect, and quickly retrieve data.

To talk to a database, we use a language called **SQL (Structured Query Language)**. You will see that **almost everything you did in pandas has a direct SQL equivalent** — `groupby` becomes `GROUP BY`, filtering becomes `WHERE`, and selecting columns becomes `SELECT`.

In the next session, we will start with:

- What are databases and why are they needed?
- Setting up practice on **DB Fiddle** (online SQL playground at dbfiddle.com)
- Writing your first `SELECT`, `WHERE`, `ORDER BY`, and `LIMIT` queries
- Mapping what you know in pandas to SQL syntax

---

## Key Takeaways

- **`df.rename(columns={...})`** is how you give meaningful names to columns — always use `inplace=True` or reassign to make the change stick.
- **`df.drop(columns=[...])` and `df.drop([row_indices])`** are your tools for removing unwanted columns and rows, including conditional deletion using `.index`.
- **`pd.merge()`** is the standard, flexible way to combine two DataFrames using a key column — it supports Inner, Left, Right, and Outer joins using the `how=` parameter.
- **The four join types** answer different questions: Inner = only matches, Left = all from left, Right = all from right, Outer = everyone from both sides.
- **Method chaining** lets you write a multi-step data pipeline in one clean, readable block — merge → groupby → agg → reset_index → rename → sort_values.
- SQL is what comes next — it solves the problem of **permanent, large-scale data storage** and uses nearly the same mental model as pandas.

---

## Important Commands & Terminologies (Quick Reference)

| Command / Method | What It Does | Simple Example |
| :--- | :--- | :--- |
| `df.rename(columns={...})` | Rename one or more columns | `df.rename(columns={"Sales": "Revenue"})` |
| `inplace=True` | Modify the original DataFrame directly, no copy | `df.rename(..., inplace=True)` |
| `df.drop(columns=[...])` | Drop one or more columns | `df.drop(columns=["Discount", "Units"])` |
| `df.drop([index_list])` | Drop rows by their index labels | `df.drop([0, 2])` |
| `df[condition].index` | Get index labels of rows that match a condition | `df[df["Sales"] < 150].index` |
| `df.reset_index()` | Convert the DataFrame index back to a regular column | `result.reset_index(inplace=True)` |
| `df.set_index("col")` | Set a column as the DataFrame index | `df.set_index("CustomerID")` |
| `pd.merge(df1, df2, on=..., how=...)` | Merge two DataFrames on a common column | `pd.merge(df1, df2, on="CustomerID", how="inner")` |
| `how="inner"` | Only rows that match in both DataFrames | Default join type in `pd.merge()` |
| `how="left"` | All rows from left + matching from right | Right-side is NaN for no match |
| `how="right"` | All rows from right + matching from left | Left-side is NaN for no match |
| `how="outer"` | All rows from both DataFrames | NaN wherever no match exists |
| `left_on=`, `right_on=` | Key columns with different names in each DataFrame | `pd.merge(df1, df2, left_on="CustID", right_on="CustomerID")` |
| `suffixes=(...)` | Custom suffixes for overlapping non-key columns | `pd.merge(..., suffixes=("_order","_customer"))` |
| `df.join(other)` | Older index-based join method | `orders_indexed.join(customers_indexed)` |
| Method Chaining | Chain multiple operations with `.` in one block | `pd.merge(...).groupby(...).agg(...).rename(...)` |
| `NaN` | Not a Number — represents a missing/null value | Appears in unmatched rows of left/right/outer joins |
| `pd.merge()` default | Inner join | `pd.merge(df1, df2, on="key")` → inner |
| `df.join()` default | Left join | `df1.join(df2)` → left |
