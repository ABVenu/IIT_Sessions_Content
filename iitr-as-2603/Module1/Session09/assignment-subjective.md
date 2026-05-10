# Subjective assignment — Pandas: NGO project tracker

## Problem statement

You volunteer with a small **NGO** that runs community projects in three cities. The coordinator exported a messy spreadsheet-style table: it has useful columns plus a few columns nobody needs for the **quarterly summary**.

Your job is to write a **single Python script** (or notebook cell sequence saved as one `.py` file) that:

1. Builds the data in pandas (you may use `pd.DataFrame({...})`; **do not** rely on `merge` or joins).  
2. **Drops** junk columns.  
3. Produces a **management report**: **one row per `City`**, with **headcount** (number of projects), **total** `Budget_Lakh`, and **average** `Volunteers`—using **`groupby`** and **named aggregation** (`Name=("col", "func")` style).

Build the solution using: a pandas **DataFrame**, **`drop` with `axis=1`** for column removal, optional row **filtering**, **`groupby`**, and **`agg`** with **named output columns**. Stick to these building blocks; do not introduce unrelated pandas APIs beyond what the tasks require.

---

## Starter data (use exactly this)

```python
import pandas as pd

projects = pd.DataFrame({
    "ProjectID":   ["P01", "P02", "P03", "P04", "P05", "P06"],
    "City":        ["Pune", "Pune", "Mumbai", "Mumbai", "Mumbai", "Nashik"],
    "ProjectName": ["Water", "Lights", "Clinic", "School", "Garden", "Skills"],
    "Budget_Lakh": [12.5, 8.0, 25.0, 18.5, 6.0, 9.5],
    "Volunteers":  [10, 14, 22, 30, 8, 12],
    "internal_only": ["x", "x", "x", "x", "x", "x"],   # junk — remove
    "legacy_flag":   [0, 0, 0, 0, 0, 0],                 # junk — remove
})
```

---

## Tasks

1. **Import** pandas as `pd`.  
2. Create `projects` exactly as above.  
3. **Drop** columns `internal_only` and `legacy_flag` using **`axis=1`**, and assign the result back so the working DataFrame has **no** junk columns.  
4. Build **`report`** with:

   ```text
   projects.groupby("City").agg(
       Num_Projects=("ProjectID", "count"),
       Total_Budget_Lakh=("Budget_Lakh", "sum"),
       Avg_Volunteers=("Volunteers", "mean"),
   )
   ```

   Use these **exact** output names: `Num_Projects`, `Total_Budget_Lakh`, `Avg_Volunteers`.

5. **Print** a short banner line (e.g. `NGO summary by city`) and **print** `report` so a human can read the table in the console.  
6. **(Stretch, optional)** Call **`.reset_index()`** on a copy of the report and print it once, so `City` appears as a normal column. If you skip this, ensure task 5 still works.

---

## Expected output shape

After cleanup and aggregation, the grouped summary should look like this (row order may follow default group order; numeric formatting may show more decimals):

| City   | Num_Projects | Total_Budget_Lakh | Avg_Volunteers |
|--------|-------------:|------------------:|---------------:|
| Mumbai | 3            | 49.5              | 20.0           |
| Nashik | 1            | 9.5               | 12.0           |
| Pune   | 2            | 20.5              | 12.0           |

*If your console prints the City as the index without a column header, that is acceptable as long as the numbers match.*

---

## Submission instructions

1. Use **VS Code** or any IDE; ensure `pandas` is installed (`pip install pandas`).  
2. Run the script end-to-end with **no errors**.  
3. Paste the **full** `.py` source into the assessment **answer** box.  
4. At the **top** (as comments), note your Python version, the `pip install` line you used, and how to run the file (e.g. `python ngo_report.py`).

---

## Answer Explanation (for Assess)

### Ideal walkthrough

1. **Load data:** The starter `DataFrame` holds one row per project with `City` as the grouping key.  
2. **Cleanup:** `projects = projects.drop(["internal_only", "legacy_flag"], axis=1)` removes useless columns while keeping analysis columns. A single `drop` with a list is fine; two separate `drop` calls are also acceptable.  
3. **Group and summarise:** `groupby("City")` splits rows by city. Named `agg` maps each output column to one input column and one function: counting `ProjectID` gives project counts, summing `Budget_Lakh` gives total budget in lakhs, mean of `Volunteers` gives average team size.  
4. **Print:** Printing the report shows the index (`City`) and three summary columns—exactly the “split → apply → combine” pattern.

### Reference solution (complete code)

```python
# Python 3.10+ recommended
# pip install pandas
# Run: python ngo_report.py

import pandas as pd

projects = pd.DataFrame({
    "ProjectID":   ["P01", "P02", "P03", "P04", "P05", "P06"],
    "City":        ["Pune", "Pune", "Mumbai", "Mumbai", "Mumbai", "Nashik"],
    "ProjectName": ["Water", "Lights", "Clinic", "School", "Garden", "Skills"],
    "Budget_Lakh": [12.5, 8.0, 25.0, 18.5, 6.0, 9.5],
    "Volunteers":  [10, 14, 22, 30, 8, 12],
    "internal_only": ["x", "x", "x", "x", "x", "x"],
    "legacy_flag":   [0, 0, 0, 0, 0, 0],
})

projects = projects.drop(["internal_only", "legacy_flag"], axis=1)

report = projects.groupby("City").agg(
    Num_Projects=("ProjectID", "count"),
    Total_Budget_Lakh=("Budget_Lakh", "sum"),
    Avg_Volunteers=("Volunteers", "mean"),
)

print("NGO summary by city")
print(report)

# Optional stretch: City as a column
report_flat = report.reset_index()
print("\nWith City as column:")
print(report_flat)
```

### Alternative approaches (also valid if results match)

- Drop junk columns with two calls: `projects = projects.drop("internal_only", axis=1)` then `projects = projects.drop("legacy_flag", axis=1)`.  
- Use `inplace=True` instead of reassignment for drops (less common in teaching flow, but valid).  
- For headcount, **`Name=("ProjectName", "count")`** instead of `ProjectID` gives the same counts if there are no null names.  
- Stretch only: `reset_index()` for an export-friendly layout; after `groupby`, this exposes the grouping key as a normal column.

### Common mistakes to catch when grading

- Forgetting **`axis=1`** when dropping columns.  
- Forgetting to **assign** `projects = projects.drop(...)` and then aggregating on the old frame (junk columns still present).  
- Using **`merge`** or file joins—outside the stated requirements.  
- Typos in **named aggregation** output keys (platform may check for exact names if auto-graded).

---


