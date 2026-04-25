# Objective Assignment — Pandas: Data Cleanup & Combining DataFrames

---

## MCQ — Single Correct Answer

---

**Question 1** *(Easy)*

Arjun is cleaning up a sales report in pandas. He runs the following line:

```python
df.rename(columns={"Sales": "Revenue"})
```

He then prints `df` and is surprised to see the column is still called "Sales". What went wrong?

A) `rename()` cannot rename columns that contain numeric data
B) `rename()` returns a new DataFrame with the change applied; since Arjun didn't store the result or use `inplace=True`, the original `df` was never modified
C) The dictionary key "Sales" must match the exact data type of the column, not just its name
D) `rename()` only works after calling `reset_index()` first

**Correct Answer:** B

**Answer Explanation:**
`df.rename(columns={"Sales": "Revenue"})` creates and returns a **new DataFrame** with the renamed column. If that return value is not stored (e.g., `df = df.rename(...)`) and `inplace=True` is not used, the original `df` is left completely unchanged. Option A is incorrect — `rename()` works on any column regardless of data type. Option C is a fabricated rule that does not exist in pandas. Option D is also false — `rename()` works independently of `reset_index()`.

---

**Question 2** *(Easy)*

A student wants to remove the "Discount" column from a DataFrame `df`. She writes:

```python
df.drop("Discount")
```

What actually happens when this line runs?

A) The "Discount" column is successfully removed from `df`
B) pandas silently skips the operation since no axis was specified
C) pandas raises a `KeyError` because, without `columns=` or `axis=1`, it interprets "Discount" as a **row label** — and no row is labelled "Discount"
D) pandas removes all columns except "Discount"

**Correct Answer:** C

**Answer Explanation:**
`df.drop()` defaults to `axis=0`, meaning it operates on **rows**. Without specifying `columns=["Discount"]` or `axis=1`, pandas looks for a row with the index label "Discount". Since no such row exists, it raises a `KeyError`. The correct ways to drop a column are `df.drop(columns=["Discount"])` (preferred) or `df.drop("Discount", axis=1)`.

---

**Question 3** *(Easy)*

A data analyst writes:

```python
result = pd.merge(orders, customers, on="CustomerID")
```

No `how` parameter is specified. What type of join does pandas perform by default?

A) Left join — all rows from `orders` are kept
B) Outer join — all rows from both DataFrames are kept
C) Right join — all rows from `customers` are kept
D) Inner join — only rows where `CustomerID` exists in both DataFrames

**Correct Answer:** D

**Answer Explanation:**
`pd.merge()` uses **inner join** as its default when `how=` is not specified. Only rows where the key column (`CustomerID`) has a matching value in **both** DataFrames appear in the result. Rows that exist in only one DataFrame are excluded. This is different from `df.join()`, which defaults to a **left join**.

---

**Question 4** *(Easy)*

After running `result = df.groupby("Region")[["Revenue"]].sum()`, a developer notices that "Region" appears as the **index** of the result, not as a regular column. Which method should she use to convert "Region" back into a regular column with a default integer index (0, 1, 2…)?

A) `result.set_index("Region")`
B) `result.drop(index="Region")`
C) `result.reset_index()`
D) `result.rename(index={"Region": 0})`

**Correct Answer:** C

**Answer Explanation:**
`reset_index()` moves the current index of a DataFrame back into a regular column and replaces it with the default integer range (0, 1, 2, …). After a `groupby()`, the grouped column becomes the index. Calling `.reset_index()` converts it back to a regular column, making it easy to rename, merge with, or display in a report. Option A looks for a **column** named `"Region"` to promote to the index, but here `"Region"` is already the index (not a column), so it is not the right fix. Option B tries to drop a row by label. Option D renames an index label, not the index-to-column structure.

---

**Question 5** *(Moderate)*

A logistics company has a `shipments` DataFrame (left) with 6 rows and a `drivers` DataFrame (right) with 8 rows. Two drivers have never made a shipment, and one shipment has an unrecognised driver ID not present in the `drivers` table. A developer runs:

```python
result = pd.merge(shipments, drivers, on="DriverID", how="right")
```

Which of the following correctly describes the result?

A) Only shipments with a matching driver appear; both unmatched drivers and the unmatched shipment are excluded
B) All 6 shipments are included; the 2 unmatched drivers are excluded
C) All 8 drivers are included; the 2 with no shipments show NaN in shipment columns; the 1 unmatched shipment is excluded
D) All rows from both DataFrames appear, with NaN wherever there is no match

**Correct Answer:** C

**Answer Explanation:**
A **right join** guarantees every row from the **right DataFrame** (drivers) appears in the result. The 2 drivers with no shipments will be included, but their shipment-related columns (from the left DataFrame) will be **NaN**. The unmatched shipment — which exists in the left but not the right — is **excluded** from a right join. Option A describes an inner join. Option B describes a left join. Option D describes an outer join.

---

**Question 6** *(Moderate)*

A developer has two DataFrames: `df_sales` where the linking column is named `"Cust_ID"`, and `df_info` where the same concept is named `"CustomerID"`. She wants to perform an inner join between them. Which code is correct?

A) `pd.merge(df_sales, df_info, on="Cust_ID", how="inner")`
B) `pd.merge(df_sales, df_info, on="CustomerID", how="inner")`
C) `pd.merge(df_sales, df_info, left_on="Cust_ID", right_on="CustomerID", how="inner")`
D) `pd.merge(df_sales, df_info, key="Cust_ID", how="inner")`

**Correct Answer:** C

**Answer Explanation:**
When the key column has **different names** in each DataFrame, `on=` cannot be used (it requires the same name in both). Instead, `left_on=` specifies the key column name in the left DataFrame, and `right_on=` specifies it in the right DataFrame. Option A fails because "Cust_ID" doesn't exist in `df_info`. Option B fails because "CustomerID" doesn't exist in `df_sales`. Option D is invalid — there is no `key=` parameter in `pd.merge()`.

---

## MSQ — Multiple Correct Answers

---

**Question 7** *(Moderate)*

A team member asks: *"Which of these approaches correctly renames the column `'Units'` to `'Quantity'` in DataFrame `df`?"*

Which of the following options **correctly rename the column** and ensure the change is reflected in `df`? **Select ALL that apply.**

A) `df.rename(columns={"Units": "Quantity"})`
B) `df.rename(columns={"Units": "Quantity"}, inplace=True)`
C) `df = df.rename(columns={"Units": "Quantity"})`
D) `df.columns = ["Quantity" if col == "Units" else col for col in df.columns]`

**Correct Answers:** B, C, D

**Answer Explanation:**
- **A (Incorrect):** `rename()` without `inplace=True` returns a **new DataFrame** and does not change `df`. Since the result is not stored, the change is lost.
- **B (Correct):** `inplace=True` tells pandas to apply the rename **directly to `df`**, so the change persists.
- **C (Correct):** Storing the returned DataFrame back into `df` achieves the same result as `inplace=True`.
- **D (Correct):** Reassigning `df.columns` with a conditional list updates only the exact `"Units"` column name (not partial matches), and the change is applied directly to `df`.

---

**Question 8** *(Moderate)*

Priya wants to remove the `"Discount"` column from a DataFrame `df`. Which of the following lines of code **successfully remove the column**? **Select ALL that apply.**

A) `df.drop("Discount")`
B) `df.drop(columns=["Discount"], inplace=True)`
C) `df.drop("Discount", axis=1, inplace=True)`
D) `df = df.drop(columns=["Discount"])`

**Correct Answers:** B, C, D

**Answer Explanation:**
- **A (Incorrect):** `df.drop("Discount")` interprets "Discount" as a **row label** (axis=0 by default) and raises a `KeyError` since no row has that label. It does NOT remove the column.
- **B (Correct):** `inplace=True` applies the column drop directly to `df`.
- **C (Correct):** This is the `axis=1` form with `inplace=True`, so `df` is modified directly.
- **D (Correct):** Reassigning `df = df.drop(columns=["Discount"])` stores the updated DataFrame back into `df`, so the column is actually removed from `df`.

---

**Question 9** *(Hard)*

A data analyst writes the following pipeline to generate a regional revenue summary:

```python
result = (
    pd.merge(orders, customers, on="CustomerID", how="left")
      .groupby("City")
      .agg(Total_Revenue=("Amount", "sum"), Order_Count=("OrderID", "count"))
      .reset_index()
      .sort_values(by="Total_Revenue", ascending=False)
)
```

Assume `orders` has 5 rows and `customers` has 7 rows. Two customers have never placed an order. Which of the following statements about this pipeline are **correct**? **Select ALL that apply.**

A) Since a left join is used, all 5 rows from `orders` are guaranteed to appear in the merged result
B) The 2 customers with no orders will appear in the merged result with NaN in the `Amount` and `OrderID` columns
C) `.reset_index()` converts the `City` group-by index back into a regular column so the result has a clean integer index
D) Removing `.reset_index()` would cause `.sort_values()` to raise an error

**Correct Answers:** A, C

**Answer Explanation:**
- **A (Correct):** A **left join** keeps every row from the left DataFrame (`orders`). All 5 orders are guaranteed to appear. Unmatched right-side (customer) columns fill with NaN.
- **B (Incorrect):** In a **left join**, the **left DataFrame** (`orders`) drives the result. Customers with no orders are in the right DataFrame — they are **not included** since there is no matching order row on the left. NaN would only appear for orders whose `CustomerID` is missing from `customers`.
- **C (Correct):** After `.groupby("City").agg(...)`, `City` becomes the DataFrame's **index**. `.reset_index()` demotes it back to a regular column, giving the result a default 0, 1, 2… integer index.
- **D (Incorrect):** `.sort_values()` works on DataFrames regardless of whether the index is a named column or the default integer range. Removing `.reset_index()` does not cause `.sort_values()` to fail — it would still sort correctly.

---

**Question 10** *(Hard)*

Consider the following two DataFrames:

- `df1` (Orders): CustomerIDs are `["C01", "C02", "C01", "C04"]` — 4 rows total
- `df2` (Customers): CustomerIDs are `["C01", "C02", "C03", "C04"]` — 4 rows total

C03 (Charlie) appears only in `df2` and has no orders. C01 (Alice) appears twice in `df1` because she placed 2 orders.

Which of the following statements are **correct**? **Select ALL that apply.**

A) An **inner join** on `CustomerID` produces exactly 4 rows (C01 contributes 2 rows, C02 contributes 1, C04 contributes 1)
B) A **right join** on `CustomerID` produces 5 rows — 4 matched rows plus Charlie (C03) with NaN in order-related columns
C) An **outer join** on `CustomerID` produces the same number of rows as an inner join because all CustomerIDs in `df1` exist in `df2`
D) A **left join** on `CustomerID` produces at least as many rows as an inner join for the same data

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A (Correct):** Inner join includes only rows where the key exists in both DataFrames. All 4 orders (C01, C02, C01, C04) have matches in `df2`. Alice (C01) appears **twice** since she placed 2 orders. Total = 4 rows.
- **B (Correct):** A right join keeps all 4 rows from `df2`. Charlie (C03) has no matching order in `df1`, so `OrderID` and `Amount` are **NaN** for that row. The result: 4 matched rows + 1 Charlie row = **5 rows**.
- **C (Incorrect):** The outer join result is **not** the same as the inner join here. Outer join keeps all rows from both sides. Charlie (C03) is in `df2` only — so the outer join includes him with NaN on the order columns, producing **5 rows** — more than the inner join's 4.
- **D (Correct):** Left join keeps **all rows from the left DataFrame** (`df1`). Since every order already has a matching customer, the left join here produces 4 rows — equal to the inner join. In general, a left join always produces ≥ as many rows as an inner join because it never drops left-side rows.
