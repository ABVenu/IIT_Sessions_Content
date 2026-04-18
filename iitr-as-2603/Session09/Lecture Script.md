# Lecture Script: Pandas — CRUD Implementation (Catch-up) + Aggregation & Combining Data

**Session Duration:** 2 hours 15 minutes (30 min CRUD implementation catch-up + 1 hour 45 min on aggregation & combining)  
**Audience:** Absolute Beginners (Indian students); no prior tech background assumed; basic comfort with Python lists and DataFrames from the previous session helps.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the Lecture Notes. Use it to manage pacing, screen-sharing, room circulation, live-coding, and quick engagement checks. Keep the Lecture Notes open on a second tab for definitions, code, and analogies.

---

## Break rule

After **60–75 minutes** of instruction and live coding, take **one** pause of **5–8 minutes**. Do not schedule the break as a numbered teaching block; resume with the next block's bridge sentence.

---

# PART A — CRUD on DataFrames: Implementation Catch-up (30 minutes)

> **Why this part is here:** In the **previous session (Session 08)**, CRUD (Create / Read / Update / Delete) on a pandas DataFrame was **explained conceptually but never actually implemented in code** — the live-coding walkthrough was missed. Before moving to aggregation and joins, we close that gap today: every student must now **write the code** to create a DataFrame, read rows/columns from it, update cells, and delete rows/columns. Keep this tight — 30 minutes total, hands-on the whole way.

---

## 1. Framing the catch-up — “last class we spoke, today we type” (5 minutes)

- **Screen-share:** The word **CRUD** on one line — **C**reate, **R**ead, **U**pdate, **D**elete.
- **Say it plainly:** “Last class we **talked through** all four operations — today we will **actually write the code** for each one. The concept is already in your head; we are just giving your fingers the practice.”
- **Relatable hook:** WhatsApp contacts — **add** a contact (Create), **open** it (Read), **edit** name (Update), **delete** it (Delete). Same four actions, now on a DataFrame.
- **Set the plan:** 30 minutes of pure implementation on a small employee DataFrame, then we move to the main topics of today — summarising and combining.
- **Check:** **Thumbs up** — “Jupyter/Colab open with `import pandas as pd`?”

**Bridge sentence:** “Let us start with **Create** — how a DataFrame is born in code.”

---

## 2. **C**reate — building and adding to a DataFrame (8 minutes)

- **Screen-share (two ways to create):**
  1. From a **dictionary** — `pd.DataFrame({"Name":[...], "Salary":[...]})`.
  2. From a **list of lists** with `columns=[...]`.
- **Live-code:** Build a 3-row employee DataFrame (Name, Department, Salary). Print `df`.
- **Add a new column (Create a column):**
  - `df["Bonus"] = df["Salary"] * 0.10` — new column from a formula.
  - `df["Status"] = "Active"` — new column with a constant.
- **Add a new row (Create a row):**
  - `df.loc[len(df)] = ["Meera", "IT", 75000, 7500, "Active"]` — append by positional index.
  - One-liner mention: `pd.concat([df, new_row_df], ignore_index=True)` for adding **multiple** rows at once.
- **Students do:** Create their own 3-row DataFrame, then add one `Bonus` column and one new employee row.
- **Check:** **Thumbs up** — “Does your `df.shape` now show 4 rows and 5 columns?”

**Bridge sentence:** “A DataFrame exists. Now let us **read** from it — last class this was only described; today we type it.”

---

## 3. **R**ead — accessing rows, columns, cells (7 minutes)

- **Screen-share (code for everything we only discussed last time):**
  - Whole column: `df["Salary"]` → Series; `df[["Name","Salary"]]` → DataFrame.
  - Row by **label**: `df.loc[0]`, `df.loc[0:2]` (**inclusive** end).
  - Row by **position**: `df.iloc[0]`, `df.iloc[0:2]` (**exclusive** end).
  - Single cell: `df.at[0, "Salary"]` or `df.loc[0, "Salary"]`.
  - Boolean read: `df[df["Salary"] > 50000]`.
- **Live-code:** One example of each — column read, row read with `loc`, row read with `iloc`, one cell, one boolean filter. Keep each to 30 seconds.
- **Students do:** Read the salary of the 2nd employee using **both** `loc` and `iloc`.
- **Cold-call:** “`loc[0:2]` gives how many rows? And `iloc[0:2]`?” (3 vs 2.)

**Bridge sentence:** “Reading typed out — good. Now **updating** values in code, which we only heard about last class.”

---

## 4. **U**pdate — changing values in a DataFrame (6 minutes)

- **Screen-share:**
  - Update **one cell**: `df.loc[0, "Salary"] = 42000` or `df.at[0, "Salary"] = 42000`.
  - Update a **whole column**: `df["Bonus"] = df["Salary"] * 0.15` (rewrite).
  - **Conditional update** — the power move:
    - `df.loc[df["Department"] == "IT", "Salary"] = df["Salary"] * 1.10` (give IT a 10% raise).
    - `df["Status"] = df["Salary"].apply(lambda s: "High" if s > 60000 else "Normal")`.
  - **Rename a column value** (not the column itself): `df["Department"] = df["Department"].replace({"IT": "Tech"})`.
- **Live-code:** Demo the conditional update (IT department 10% raise) clearly — print `df` before and after so students see the change.
- **Students do:** Give everyone in HR a 5000 bonus addition using a conditional update.
- **Pitfall callout (one line):** **Avoid chained assignment** like `df[df["Salary"] > 50000]["Bonus"] = 1000` — use `df.loc[mask, "Bonus"] = 1000` instead. Pandas warns against the former.

**Bridge sentence:** “When a row or column no longer belongs, we **delete** it — the fourth CRUD, also finally in code today.”

---

## 5. **D**elete — removing rows and columns (4 minutes)

- **Screen-share:**
  - Delete a **column**: `df = df.drop("Bonus", axis=1)` or `del df["Bonus"]` (simpler syntax).
  - Delete a **row by label**: `df = df.drop(0)` (row at label 0) or `df = df.drop([0, 2])` for many.
  - Delete **by condition**: keep rows that do **not** match — `df = df[df["Department"] != "HR"]`.
- **Live-code:** Drop one column, then drop one row, then filter-drop by condition. Print `df.shape` after each.
- **Shout the rule:** “**`axis=1` for columns, `axis=0` (default) for rows.** We will repeat this rule in the Aggregation section.”
- **Students do:** Drop the `Status` column and remove any one employee row by their index.

**Bridge sentence:** “Create, Read, Update, Delete — now typed, not just spoken. The catch-up is done. Onward to today's core topics: **summarising** many rows into one number, and **combining** many tables into one view.”

---

# PART B — Aggregation & Combining Data (1 hour 45 minutes)

---

## 6. Why aggregate & combine? (3 minutes)

- **Screen-share:** Session objective — summarise datasets and combine multiple tables for analysis.
- **Say in one line:** “CRUD moves data around. **Aggregation** shrinks it into decisions. **Merge** pulls scattered tables together.”
- **Relatable hook:** Class teacher with 50 students' marks — principal only wants the **average**. That is aggregation.
- **Check:** **Thumbs up** — “Ready to move from single-row edits to whole-column summaries?”

**Bridge sentence:** “First, summarise a whole column in one line — that is basic aggregation.”

---

## 7. Basic Aggregation Functions (8 minutes)

- **Screen-share:** The five everyday functions — `sum()`, `mean()`, `count()`, `min()/max()`, `median()` — one line each, framed as total sales / average marks / headcount / top / bottom.
- **Live-code:** Reuse the employee DataFrame; run `.sum()`, `.mean()`, `.count()`, `.min()`, `.max()` on the Salary column. Narrate each output.
- **Students do:** Reproduce all five prints on their own DataFrame.
- **Under the hood (one line):** “Pandas ignores **NaN** by default in `sum`/`mean`/`count` — safe behaviour.”
- **Check:** **Thumbs up** — “Everyone saw total, mean, min, max print cleanly?”

**Bridge sentence:** “One number for the whole company is fine, but managers always ask **per department** — that is `groupby`.”

---

## 8. `groupby` — Split → Apply → Combine (5 minutes)

- **Screen-share:** The 3-word pattern: **Split, Apply, Combine**. Make students say it out loud.
- **Analogy (30 seconds):** Laundry — split by colour, wash each pile, fold back.
- **No coding yet** — just whiteboard the idea.
- **Cold-call:** “Give me one business question needing a groupby.” (sales per city, orders per customer, marks per class.)

**Bridge sentence:** “Now let us actually write it on the employee table.”

---

## 9. `groupby` with basic aggregations (10 minutes)

- **Screen-share:** The 6-row employee DataFrame from the notes (with Experience).
- **Live-code in sequence:**
  1. `grouped = df.groupby("Department")` — show nothing prints (**lazy**).
  2. `grouped["Salary"].mean()` — average salary per department.
  3. `df.groupby("Department")["Name"].count()` — headcount.
  4. `df.groupby("Department")["Salary"].sum()` — total cost.
  5. `df.groupby("Department")[["Salary","Experience"]].mean()` — two columns at once.
- **Point at output:** The group column becomes the **index**. Show `.reset_index()` in one line to flip back.
- **Students do:** Compute **headcount per department** and **total salary per department**.
- **Check:** **Thumbs up** — “Three rows in the output — HR, IT, Sales?”
- **Cold-call:** “Highest average salary?” (IT = 82,500.)

**Bridge sentence:** “One aggregation at a time is fine for learning, but real reports ask for sum + mean + count **together**. Meet `agg()`.”

---

## 10. `agg` — list, dictionary, and named (12 minutes)

- **Screen-share:** Combo-meal analogy — one order, many items.
- **Live-code all three forms back-to-back:**
  1. **List form:** `df.groupby("Department")["Salary"].agg(["sum","mean","count","min","max"])` — rich output, function names as strings.
  2. **Dict form:** `df.groupby("Department").agg({"Salary":"sum","Experience":"mean","Name":"count"})` — different function per column.
  3. **Named form:** `df.groupby("Department").agg(Total_Salary=("Salary","sum"), Average_Salary=("Salary","mean"), Headcount=("Name","count"), Avg_Experience=("Experience","mean"))` — **the production-quality form**, clean column names.
- **Say it clearly:** Named form syntax is `NewName=(existing_column, function)` — always a **tuple of two**. No quotes on the left.
- **Recommendation:** “For real reports, **always use named aggregation**.” Repeat this line.
- **Students do:** Build a report with **Total_Salary, Average_Salary, and Max_Salary** per department using the named form.
- **Check:** **Thumbs up** — “Output has 3 rows and 3 clean business-named columns?”

**Bridge sentence:** “We can summarise beautifully, but real raw data has messy column names — let us clean them.”

> **[BREAK RULE]** If we have crossed ~60–70 minutes of the total session here, take the **5–8 minute pause** now. Resume at Block 11.

---

## 11. Renaming columns (6 minutes)

- **Screen-share:** The messy DataFrame with `emp_id`, `EMP NAME`, `sal_$`.
- **Live-code:** `df = df.rename(columns={"emp_id":"EmployeeID", "EMP NAME":"EmployeeName", "sal_$":"Salary"})`. Also mention `inplace=True`.
- **Pitfall callout (live demo):** Run `rename` **without** reassignment; print columns; show unchanged; then fix. “Forgetting to reassign = nothing changes.”
- **Best practice (one line):** short, lowercase, underscore names (`employee_id`).
- **Students do:** Rename their own three messy columns.

**Bridge sentence:** “Some columns are not bad-named — they are just **useless**. We delete them with `drop`.”

---

## 12. Dropping columns (6 minutes)

- **Screen-share:** “Clean your WhatsApp” analogy.
- **Live-code:**
  1. `df.drop("Temp_Col", axis=1)` — single.
  2. `df.drop(["Old_Flag","Temp_Col"], axis=1)` — multiple.
- **Shout the rule (again):** “**`axis=1` means columns.** Forgetting it is the #1 beginner error.”
- **Live-demo the error:** Run `df.drop("Temp_Col")` without `axis=1`; show the `KeyError`; fix it.
- **Students do:** Drop one column and then drop two columns at once.

**Bridge sentence:** “Clean names, useful columns — good. Now we move from **one table** to **many tables**, which is how real companies store data.”

---

## 13. Introduction to Combining Data (3 minutes)

- **Screen-share:** Aadhaar + PAN = full person; Employees + Departments = full view. In SQL this is a JOIN; in pandas it is `merge` / `join`.
- **Whiteboard:** Two tables with a shared `DepartmentID`; arrow-match two rows. Rows line up **side-by-side on a key**.
- **Check:** **Thumbs up** — “Clear that merge = row-matching on a key?”

**Bridge sentence:** “Four kinds of joins cover 99% of real work.”

---

## 14. `merge` — inner join (10 minutes)

- **Screen-share:** Venn-diagram image of the 4 joins. Name each: **inner, left, right, outer**.
- **Set up data:** `employees` (4 rows, DeptID 1, 2, 1, 3) + `departments` (DeptID 1, 2, 4) — stress the *deliberate mismatch*.
- **Live-code inner join:** `pd.merge(employees, departments, on="DepartmentID", how="inner")`.
- **Narrate row-by-row:** Meera (Dept 3) **vanishes**; Finance (Dept 4) **vanishes**. Only matches survive.
- **Students do:** Build both tables and run the inner join. Expect 3 rows.
- **Pair-share (60 sec):** “Which join finds employees without a department?” (Left or outer.)

**Bridge sentence:** “Inner drops what does not match. In business we almost never want to lose our main table — that is what `left` is for.”

---

## 15. Left, right, and outer joins (8 minutes)

- **Live-code all three in sequence on the same data:**
  1. `how="left"` — all 4 employees kept; Meera's `DepartmentName` is **NaN**. “NaN here is **information**, not an error.”
  2. `how="right"` — all 3 departments kept; Finance's employee info is NaN.
  3. `how="outer"` — 5 rows total; NaNs on both sides where unmatched.
- **Say twice:** “`left` is the **most common** join in real projects.”
- **Students do:** Run all three; compare row counts (4 / 3 / 5).
- **Cold-call:** “Joining sales with a customer master, want every sale on the report — which join?” (Left.)

**Bridge sentence:** “So far key names matched. What if the key is `DeptID` on one side and `DepartmentID` on the other?”

---

## 16. `left_on` / `right_on` + quick intro to `.join()` (6 minutes)

- **Part 1 — `left_on` / `right_on` (live-code, ~4 min):**
  - **Set up the mismatch:** `employees2 = employees.rename(columns={"DepartmentID": "DeptID"})` — now the left key is `DeptID`, the right key is still `DepartmentID`.
  - **Live-code:** `pd.merge(employees2, departments, left_on="DeptID", right_on="DepartmentID", how="inner")`.
  - **Narrate:** Output carries **both** key columns side-by-side — drop one later with `.drop()` if you don't need it.
  - **One-liner:** *"`on="key"` works only when the column name is **identical** on both sides. The moment the name differs, switch to `left_on` + `right_on`."*
  - **Students do:** Reproduce the rename + merge; verify both `DeptID` and `DepartmentID` appear in the output.

- **Part 2 — Introduction to `.join()` (mention only, ~2 min — NO live-setup):**
  - **Screen-share the definition (from Lecture Notes):** *"`DataFrame.join()` combines two tables by **aligning them on their index** (row labels)."*
  - **Analogy (15 sec):** *"Two notebooks with the **same page numbers** — hold them together and every page of A pairs up with the same page of B."*
  - **Show the one-liner on screen (do NOT build the tables live):**

```python
# info and salary are two DataFrames, both indexed by EmployeeID
combined = info.join(salary)   # glues them side-by-side on the index
```

  - **Say it clearly and lock the distinction:**
    - **`merge`** → combine on a **column** (main tool, what we used today).
    - **`join`** → combine on the **index** (shortcut).
  - **Defer honestly:** *"We are **not going deep into `.join()` today**. Just remember it exists and it is for index-based combining. We will see detailed examples and `merge` vs `join` differences in the **upcoming SQL session**."*
  - **Check:** **Thumbs up** — *"Clear that `merge` = column, `join` = index, and deep-dive is next session?"*

**Bridge sentence:** “Every tool seen separately. Let us tie them together like a real Data Analyst.”

---

## 17. Mini Project — Clean → Combine → Aggregate (12 minutes)

- **Screen-share:** The 6-step workflow from the notes.
- **Live-code as a story:**
  1. Create raw Employees + Departments tables.
  2. `rename` bad columns, `drop` the junk `temp_flag`.
  3. `merge` on `dept_id` with `how="left"`.
  4. `groupby("dept_name").agg(...)` with **named aggregation** (Headcount, Total_Salary, Average_Salary).
  5. Print the final **FINAL MANAGEMENT REPORT**.
- **Say it twice:** “This three-step rhythm — **Clean → Combine → Aggregate** — is literally 80% of a Data Analyst's day job.”
- **Students do:** Reproduce end-to-end. Circulate fast; help only with typos.
- **Pair-share (90 sec):** “Change one thing to answer: which department has the **highest paid** employee?” (Replace `mean` with `max`.)
- **Cold-call:** One pair to share the change and the answer.

**Bridge sentence:** “You just did what junior analysts take a week to learn. Let us close with the mistakes to dodge.”

---

## 18. Common Doubts, Cheat Sheet & Exit (4 minutes)

- **Screen-share:** The “Common Doubts” bullets (15 seconds each):
  - Forgetting `axis=1` in `drop`.
  - Using `and`/`or` instead of `&`/`|`.
  - Not reassigning (`rename`/`drop`/`sort_values`).
  - `merge` (horizontal, on a key) vs `concat` (vertical stack).
  - NaN after left join is **information**, not a bug.
  - `reset_index()` after groupby.
- **Screen-share:** The one-page command table from the notes — bookmark it as the assignment cheat sheet.
- **Students do:** Write one command they will reuse this week.
- **Closing line:** “Keep today's notebook open — next class builds on the same **CRUD → clean → combine → aggregate** muscles.”

---

## Timing flex — if you are running late

- **Cut first from PART A (CRUD catch-up):**
  - Merge Blocks 3 + 4 (Read + Update) into one 8-minute demo; skip the `apply(lambda)` variant in Update; skip `replace()` unless students ask.
  - In Block 2 (Create), skip the list-of-lists form; show only the dictionary form.
  - Do **not** skip Part A entirely — the whole point of this session's opener is to close the implementation gap from last class.
- **Cut first from PART B (Aggregation & Combining):**
  - Block 10 (`agg`) — show **named aggregation only**; skip the list and dict forms (mention in one line).
  - Block 15 — demo **left + outer** only (outer covers the right case conceptually).
  - Block 16 — keep only Part 1 (`left_on`/`right_on` live demo); compress the `.join()` intro to a **single sentence** pointing students to the Lecture Notes and the upcoming SQL session.
  - Block 17 (mini-project) — give Steps 1–3 as **pre-written** code; live-code only Steps 4 and 5.
- **Demo-only:** Block 12 (`drop`) — show once, assign exercises for homework.
- **Minimum viable session:**
  - **CRUD catch-up (20 min):** Create via dict (Block 2 trimmed), quick Read implementation (Block 3 in 3 min), conditional Update (Block 4), Delete column + row (Block 5).
  - **Basic aggregation** on a column (Block 7).
  - **`groupby` with mean and count** (Block 9).
  - **Named aggregation** (Block 10, named form only).
  - **`rename`** (Block 11).
  - **`drop` with `axis=1`** (Block 12).
  - **`pd.merge` with inner + left only** (Blocks 14–15 merged).
  - **5-min mini-project recap** (Block 17).
- **If ahead of schedule:**
  - Extend Update in CRUD with a `df.apply(...)` row-wise example.
  - In the main part, add a 10-minute **live debugging** session — deliberately forget `axis=1`, forget parentheses in filters, forget to reassign after `rename`; students spot and fix.
  - Introduce `pd.concat` briefly as the **vertical** sibling of `merge` so the distinction sticks.
