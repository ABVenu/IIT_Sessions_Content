# Subjective Assignment — Pandas: Data Cleanup & Combining DataFrames

---

## Practical Task: Build a City-Wise Revenue Report for FoodFly

### The Scenario

You have just joined **FoodFly**, a growing food delivery startup, as a junior data analyst. The operations manager wants a clean **city-wise revenue summary** to decide which cities to invest in next. She hands you two raw data sources — an orders table and a restaurant directory — and asks you to produce a final ranked report using Python and pandas.

Your job is to merge the data correctly, clean it up, and build the report using a single method-chaining pipeline.

---

### Dataset

Use exactly the following DataFrames in your code:

```python
import pandas as pd

orders = pd.DataFrame({
    "OrderID":        [101, 102, 103, 104, 105, 106],
    "RestaurantID":   ["R01", "R02", "R01", "R03", "R02", "R04"],
    "CustomerName":   ["Ananya", "Rohit", "Priya", "Dev", "Sara", "Meera"],
    "Amount":         [450, 320, 560, 180, 290, 720]
})

restaurants = pd.DataFrame({
    "RestaurantID":   ["R01", "R02", "R03", "R05"],
    "RestaurantName": ["Spice Garden", "The Grill House", "Curry Corner", "Pasta Palace"],
    "City":           ["Delhi", "Mumbai", "Delhi", "Bengaluru"]
})
```

> **Notice:** Order 106 is placed at `R04`, which does not exist in the `restaurants` table. `R05` (Pasta Palace) exists in `restaurants` but has received no orders. Keep these edge cases in mind when choosing your join type.

---

### What You Must Build

Complete all steps below in a single `.py` file or `.ipynb` notebook.

---

#### Step 1 — Merge the DataFrames

Merge `orders` and `restaurants` on `RestaurantID` using the join type that keeps **only orders that have a matching restaurant** (orders from unrecognised restaurants should be excluded, and restaurants with no orders should also be excluded).

Print the merged DataFrame and state in a comment which join type you used and why.

---

#### Step 2 — Clean the Merged Result

From the merged DataFrame produced in Step 1:

1. **Drop** the `RestaurantID` column (it is no longer needed after the merge)
2. **Rename** the following columns:
   - `"Amount"` → `"Revenue"`
   - `"RestaurantName"` → `"Restaurant"`

Print the cleaned DataFrame.

---

#### Step 3 — Build the City-Wise Report Using a Single Pipeline

Starting fresh from the original `orders` and `restaurants` DataFrames, write a **single method-chaining pipeline** (no intermediate variables) that:

1. Merges `orders` and `restaurants` on `RestaurantID` (same join type as Step 1)
2. Groups the merged result by `City`
3. Aggregates to produce:
   - `Total_Revenue` — the sum of `Amount` per city
   - `Order_Count` — the count of `OrderID` per city
4. Resets the index so `City` becomes a regular column
5. Sorts by `Total_Revenue` in **descending order** (highest revenue city first)

Store the final result in a variable called `city_report` and print it.

---

#### Step 4 — Interpret the Output

After printing `city_report`, answer the following in code comments (one sentence each):

1. Which city generated the highest total revenue, and what was the amount?
2. Why does Pasta Palace (R05, Bengaluru) not appear in the report?
3. Why does Order 106 (R04) not appear in the report?

---

### Submission Format

### Submission Format

- Code in a `.py` file in VS Code or `.ipynb` notebook. 
- paste the code directly in the answer box
- Your code must be clean, runnable from top to bottom without errors, and produce all the outputs described above.

---

### Answer Explanation (Complete Solution)

```python
import pandas as pd

# ── Dataset ────────────────────────────────────────────────────────────────────
orders = pd.DataFrame({
    "OrderID":        [101, 102, 103, 104, 105, 106],
    "RestaurantID":   ["R01", "R02", "R01", "R03", "R02", "R04"],
    "CustomerName":   ["Ananya", "Rohit", "Priya", "Dev", "Sara", "Meera"],
    "Amount":         [450, 320, 560, 180, 290, 720]
})

restaurants = pd.DataFrame({
    "RestaurantID":   ["R01", "R02", "R03", "R05"],
    "RestaurantName": ["Spice Garden", "The Grill House", "Curry Corner", "Pasta Palace"],
    "City":           ["Delhi", "Mumbai", "Delhi", "Bengaluru"]
})

# ── Step 1: Merge — Inner Join ─────────────────────────────────────────────────
# Inner join: keeps only rows where RestaurantID exists in BOTH DataFrames.
# - Order 106 (R04) is excluded: R04 has no entry in restaurants.
# - Pasta Palace (R05) is excluded: it has no matching order in orders.
merged = pd.merge(orders, restaurants, on="RestaurantID", how="inner")
print("Step 1 — Merged DataFrame:")
print(merged)

# ── Step 2: Drop RestaurantID, Rename columns ──────────────────────────────────
clean = merged.drop(columns=["RestaurantID"])
clean.rename(columns={"Amount": "Revenue", "RestaurantName": "Restaurant"}, inplace=True)
print("\nStep 2 — Cleaned DataFrame:")
print(clean)

# ── Step 3: City-Wise Report via Method Chaining ───────────────────────────────
city_report = (
    pd.merge(orders, restaurants, on="RestaurantID", how="inner")   # Step 1: merge
      .groupby("City")                                               # Step 2: group by city
      .agg(                                                          # Step 3: aggregate
          Total_Revenue=("Amount", "sum"),                           #   total revenue per city
          Order_Count=("OrderID", "count")                           #   number of orders per city
      )
      .reset_index()                                                 # Step 4: City → regular column
      .sort_values(by="Total_Revenue", ascending=False)              # Step 5: highest revenue first
)

print("\nStep 3 — City-Wise Revenue Report:")
print(city_report)

# ── Step 4: Interpretation ─────────────────────────────────────────────────────
# Q1: Delhi generated the highest total revenue (₹1,190 = Order 101: ₹450 + Order 103: ₹560 + Order 104: ₹180).
# Q2: Pasta Palace (R05, Bengaluru) has no matching orders in the orders table, so the inner join excludes it.
# Q3: Order 106 uses RestaurantID R04, which does not exist in the restaurants table; the inner join excludes it.
```

---

#### Walkthrough of the Solution

**Why Inner Join (Step 1)?**
The manager wants a revenue report — only completed, attributable orders matter. An order from an unrecognised restaurant (R04) cannot be city-tagged, and a restaurant with no orders contributes zero revenue. An inner join cleanly excludes both, giving us only the 5 orders that are fully matched and meaningful for the report.

**Why Drop `RestaurantID` (Step 2)?**
After the merge, `RestaurantID` has served its purpose — it was only the linking key. Keeping it in the final cleaned DataFrame adds noise without value. `drop(columns=["RestaurantID"])` removes it cleanly.

**Method Chaining Pipeline (Step 3):**
The pipeline mirrors a real analyst's thought process — merge the raw data, zoom into city-level, compute the numbers, clean the structure, and sort for readability. Wrapping the entire chain in parentheses `(...)` allows it to span multiple lines without backslashes, which is a clean Python idiom for long chains.

**`reset_index()` in the chain:**
After `.groupby("City").agg(...)`, `City` becomes the DataFrame's row index. Without `.reset_index()`, `City` is a special label, not a regular column — which makes downstream operations like renaming and sorting by City awkward. `.reset_index()` promotes it back to a normal column with a clean 0, 1, 2… integer index.

**Expected Output of `city_report`:**

| City   | Total_Revenue | Order_Count |
|--------|:-------------:|:-----------:|
| Delhi  | 1190          | 3           |
| Mumbai | 610           | 2           |

Delhi leads with ₹1,190 from 3 orders; Mumbai follows with ₹610 from 2 orders.
