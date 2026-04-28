# Lecture Script: SQL — Querying Data with SELECT and WHERE

**Session Duration:** 2 hours 15 minutes (≈ 130 min of blocks + one 5–8 min break)  
**Audience:** Absolute Beginners (Indian students, no prior tech background assumed); comfortable with pandas DataFrames from recent sessions — we will finish today with a pandas ↔ SQL bridge.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the Lecture Notes. Use it to manage pacing, screen-sharing, room circulation, live-coding, and quick engagement checks. Keep the Lecture Notes open on a second tab for definitions, full code blocks, and analogies.

---

## Break rule

After **60–75 minutes** of instruction and live coding, take **one** pause of **5–8 minutes**. Do not schedule the break as a numbered teaching block; resume with the next block's bridge sentence. A natural break point is suggested inside Block 9.

---

## Environment setup (before class)

- Have **MySQL Workbench** (most recommended) or **DBeaver** installed, connected to a local database, and open on the main screen.
- Have the **employees** CREATE + INSERT script (from Lecture Notes) **pre-saved** so you can paste it in one shot — do not waste live time typing 10 INSERTs.
- Keep an **online SQL compiler** (SQLiteOnline / DB Fiddle / OneCompiler) open as a **backup only**, in case Workbench fails on the projector — and remind students this is the *not recommended* path because work cannot be saved.
- Keep **VS Code** open with a Python file ready (pandas imported + `df` dict pre-saved) for the final pandas↔SQL block. Students only know **VS Code** — do not mention Jupyter or Colab.

---

# PART A — Why Databases, What is SQL & Where to Write It (26 minutes)

---

## 1. Opener — Why do we even need databases? (8 minutes)

- **Screen-share:** Write the word **DATABASE** on one line. Below it, write **pandas / Excel / CSV**. Ask: *"What is different?"*
- **Relatable hook:** IRCTC — *"Lakhs of people book tickets in the same second. Your seat is saved forever, and nobody else can grab it. Can Excel do this? No. Only a database can."*
- **Say it crisply:** *"Pandas is a **calculator** for data. A database is the **bank vault** that holds it."*
- **Screen-share the 7 failures of pandas/Excel** (from Lecture Notes) — one line each, 20 seconds per bullet:
  - Not permanent (RAM only) → survives restarts.
  - Single user → thousands concurrent.
  - Size limits (10 lakh row Excel crash) → billions of rows.
  - No safety rules → data types + validation.
  - Slow searches → indexes.
  - No security → logins + permissions.
  - No history → transaction logs, rollback.
- **Cold-call:** *"Why can't Flipkart run on a giant Excel file?"* (Multi-user, size, safety.)
- **Check:** **Thumbs up** — *"Clear that a database is not just a bigger Excel?"*

**Bridge sentence:** *"Databases are not all the same — let us see the main **types** you will hear about on the job."*

---

## 2. Types of databases + real-world use cases (8 minutes)

- **Screen-share:** The two big families — **Relational (SQL)** vs **Non-Relational (NoSQL)**.
- **Analogy (30 sec):** SQL = **set of connected Excel sheets**. NoSQL = **a box of JSON-shaped sticky notes**.
- **Live narrate the comparison table** from the Lecture Notes (Relational / Document / Key-Value / Graph / Data Warehouse). Spend 10 seconds per row — **just recognition**, not memorisation.
- **Name-drop (say out loud, no code):** MySQL, PostgreSQL, Oracle, SQL Server, SQLite (SQL); MongoDB, Redis, Cassandra, Neo4j (NoSQL); Snowflake, BigQuery (Warehouse).
- **Real-world use cases — rapid fire (1 min):** IRCTC → SQL. Instagram feed → NoSQL. HDFC Bank → SQL. WhatsApp chats → NoSQL. Swiggy orders → SQL + NoSQL mix.
- **Cold-call:** *"Your college attendance system — which type?"* (Relational.)
- **Check:** **Thumbs up** — *"Clear that SQL = tables, NoSQL = flexible shapes?"*

**Bridge sentence:** *"Out of all these, the **relational database** is the industry default — and the language to talk to it is **SQL**. Let us meet it."*

---

## 3. Introduction to SQL — what it is & why it matters (6 minutes)

- **Screen-share:** The full form — **S**tructured **Q**uery **L**anguage.
- **Say it plainly:** *"SQL is the **language** we use to talk to a relational database, just like English is the language we use to talk to a shopkeeper."*
- **Library analogy (30 sec):** *"You don't search the shelves yourself. You say, 'Give me all books by APJ Abdul Kalam after 2010.' That sentence is your SQL query."*
- **Why learn SQL (4 one-liners):** universal language / top-3 interview skill / 3 lines vs 20 lines of Python / works on crores of rows without RAM.
- **Screen-share the 4 command families** (name only — no code today for most of them):
  - **DDL** → `CREATE`, `ALTER`, `DROP` (build structure).
  - **DML** → `INSERT`, `UPDATE`, `DELETE` (change data).
  - **DQL** → `SELECT` ← **today's focus**, underline it.
  - **DCL** → `GRANT`, `REVOKE` (permissions).
- **Check:** **Thumbs up** — *"Today we live inside the `SELECT` family — agreed?"*

**Bridge sentence:** *"Before we write our first `SELECT`, a very natural question — **'Sir, where do we actually write SQL?'** Let us answer that first."*

---

## 3B. Where to write and practice SQL (4 minutes)

- **Say it plainly:** *"Unlike Python, SQL does **not** run inside VS Code directly. It runs inside a **database tool** that talks to a database."*
- **Screen-share the 3 options — one line each:**
  - **MySQL Workbench (Most Recommended):** Official free tool from MySQL. Proper editor + result viewer + table view. *"This is what we will use in class, and it is what you will see in real companies."* Download from the **official MySQL website**.
  - **DBeaver (Great Alternative):** Free, universal tool — works with MySQL, PostgreSQL, SQLite, and more. *"Lighter on the laptop than Workbench. Pick this if Workbench feels heavy."*
  - **Online SQL Compilers (NOT Recommended):** SQLiteOnline / OneCompiler / Programiz SQL / DB Fiddle. *"Runs in the browser — no install — but your work is **NOT saved**, and the database **resets** when you close the tab. Use only for a quick throwaway query."*
- **Shout the clear instruction:** *"Homework before the next session — **install MySQL Workbench (or DBeaver)** on your laptop. Do NOT rely on online compilers for practice."*
- **Live-show (30 sec):** Flip to the Workbench window you already have open. Point to the query editor, the Run button, and the result grid. *"This is where every SQL code block from today's notes will run. Paste → hit Run → see the result below."*
- **Check:** **Thumbs up** — *"Everyone clear that by next class, Workbench or DBeaver is installed?"*

**Bridge sentence:** *"Tool sorted. Now let us meet the place where the data actually lives — **tables**."*

---

# PART B — SQL Basics & SELECT (26 minutes)

---

## 4. Tables, rows, columns + our running `employees` dataset (9 minutes)

- **Screen-share:** The three words — **Table, Row, Column** — with the school attendance register analogy.
  - **Table** = full Excel sheet.
  - **Column (Field)** = one type of info (Name, Salary). Has a fixed **data type**.
  - **Row (Record)** = one full entry (one employee).
  - **Primary Key** = unique ID per row. Analogy: **Aadhaar number**.
- **Live-setup (paste, don't type):** Open SQL playground, **paste the pre-saved script**:
  - `CREATE TABLE employees (...)` with 6 columns.
  - **10 `INSERT INTO` rows** — Aarav, Diya, Kabir, Meera, Rohan, Sneha, Vihaan, Ishaan, Anaya, Riya.
- **Narrate while pasting (30 sec total):**
  - `INT PRIMARY KEY` → unique EmployeeID.
  - `VARCHAR(50)` → text up to 50 chars.
  - Order of VALUES **must match** order of columns.
- **Say loudly:** *"This **one `employees` table** is our **single source of truth** for the whole session. Every query today runs on this."*
- **Students do:** Run the script in their own playground; verify 10 rows loaded with a quick `SELECT * FROM employees;`.
- **Check:** **Thumbs up** — *"Everyone sees 10 rows, 6 columns?"*

**Bridge sentence:** *"Table is alive. Now the most used word in all of SQL — `SELECT`."*

---

## 5. `SELECT *` and specific columns (7 minutes)

- **Screen-share the structure:** `SELECT column1, column2 FROM table_name;`
- **Analogy (15 sec):** *"`SELECT` = **'show me'**. You tell the waiter which dishes from the menu."*
- **Live-code in sequence:**
  1. `SELECT * FROM employees;` — all 10 rows, all 6 columns.
  2. `SELECT Name, Salary FROM employees;` — two columns only.
  3. `SELECT Name, Department, City FROM employees;` — three columns, in a chosen order.
- **Say it sharply (best practice):** *"In real company projects, **avoid `SELECT *`**. List only the columns you need — it is faster and safer."*
- **Shout the semicolon rule:** *"`;` at the end is your **full stop**. Many tools need it."*
- **Students do:** Run all three queries. Then fire their own: `SELECT EmployeeID, JoiningYear FROM employees;`.
- **Cold-call:** *"If I write `SELECT Salary, Name` instead of `SELECT Name, Salary` — does the data change or only the display?"* (Only the display order.)

**Bridge sentence:** *"Column names are often ugly — `sal_$`, `emp_name`. Let us make them report-friendly with `AS`."*

---

## 6. Renaming output columns with `AS` (4 minutes)

- **Screen-share:** `SELECT Name AS "Employee Name", Salary AS "Monthly Pay", Department AS Team FROM employees;`
- **Say clearly:**
  - Quotes around alias **if it has a space** (`"Employee Name"`).
  - **No quotes** for single-word alias (`Team`).
  - The **actual column in the table is NOT changed** — only the **output label**.
- **Real-world hook (1 line):** *"This is exactly what you will do before exporting to Excel for a manager."*
- **Students do:** Rename `JoiningYear` to `"Year of Joining"` in a SELECT.
- **Check:** **Thumbs up** — *"Clean header in the output?"*

**Bridge sentence:** *"Sometimes we want only the **unique** values of a column — like a **list of all departments**. Meet `DISTINCT`."*

---

## 7. `DISTINCT` — unique values only (6 minutes)

- **Screen-share:** The word **DISTINCT** = *"show me one of each kind"*.
- **Analogy (15 sec):** *"WhatsApp contacts — 5 friends from Delhi, `DISTINCT` says 'Delhi' just once."*
- **Live-code in sequence:**
  1. `SELECT DISTINCT Department FROM employees;` → 4 rows (Sales, HR, IT, Finance).
  2. `SELECT DISTINCT City FROM employees;` → 3 rows (Delhi, Mumbai, Bengaluru).
  3. `SELECT DISTINCT Department, City FROM employees;` → unique **combinations**, not unique per column.
- **Say it twice:** *"When you list multiple columns with `DISTINCT`, the **whole combination** is what must be unique. `Sales, Delhi` is different from `Sales, Bengaluru`."*
- **Students do:** Compute `DISTINCT JoiningYear`.
- **Cold-call:** *"`DISTINCT City` — how many rows?"* (3.) *"And `DISTINCT Department, City`?"* (Count from the table — 9 unique pairs.)

**Bridge sentence:** *"Reading **all** rows is rarely useful. Managers always ask 'only the ones where…'. That is **`WHERE`**."*

---

# PART C — Filtering with WHERE (38 minutes)

---

## 8. `WHERE` with comparison operators (10 minutes)

- **Screen-share the structure:**

```
SELECT columns
FROM table_name
WHERE condition;
```

- **Analogy (20 sec):** *"`WHERE` is the **security guard at the mall gate** — only rows with a valid pass get through."*
- **Screen-share the 6 comparison operators** — read each aloud: `=`, `<>` / `!=`, `>`, `<`, `>=`, `<=`.
- **Shout the #1 beginner trap:** *"**Single `=`** in SQL, NOT `==`. Python brain → SQL fingers is a very common bug."*
- **Live-code in sequence (narrate each result row-count):**
  1. `WHERE Department = 'Sales'` → 3 rows.
  2. `WHERE Salary > 60000` → 5 rows.
  3. `WHERE Department <> 'IT'` → 7 rows.
  4. `WHERE JoiningYear >= 2020` → 4 rows.
- **Say it clearly:**
  - **Text values** → **single quotes**: `'Sales'`.
  - **Numbers** → **no quotes**: `60000`.
- **Students do:** Write a query for *"Employees earning less than 50000"*.
- **Cold-call:** *"`WHERE Department == 'Sales'` — does this run?"* (No, use single `=`.)
- **Check:** **Thumbs up** — *"Row counts matching ours?"*

**Bridge sentence:** *"Real questions have **more than one** condition — 'Sales AND more than 50000'. For that: `AND`, `OR`, `NOT`."*

---

## 9. Logical operators — `AND`, `OR`, `NOT` (10 minutes)

- **Screen-share the 3 logicals with a Venn diagram:**
  - `AND` → **intersection** (both true).
  - `OR` → **union** (at least one true).
  - `NOT` → **flip** the condition.
- **Live-code in sequence:**
  1. `WHERE Department = 'Sales' AND Salary > 50000` → 1 row (Kabir).
  2. `WHERE City = 'Delhi' OR City = 'Mumbai'` → 7 rows.
  3. `WHERE NOT City = 'Bengaluru'` → 7 rows (same logic as `<>`).
  4. Combined: `WHERE Department = 'IT' AND City = 'Bengaluru' AND Salary >= 80000` → 1 row (Rohan).
- **Shout the rule:** *"When you **mix `AND` with `OR`**, use **parentheses**. Just like BODMAS in maths."*
- **Pair-share (60 sec):** *"Write a query: Employees from Mumbai **OR** Bengaluru who earn more than 70000."* Expect parentheses around the OR.
- **Cold-call:** One pair to share. Expected:

```sql
WHERE (City = 'Mumbai' OR City = 'Bengaluru') AND Salary > 70000
```

- **Check:** **Thumbs up** — *"Parentheses habit locked in?"*

> **[BREAK RULE]** We are around ~65–70 minutes in. Take the **5–8 minute pause** now. Resume at Block 10.

**Bridge sentence (after break):** *"`AND`/`OR` work, but long `OR` chains become ugly. SQL gives us three shortcuts — `BETWEEN`, `IN`, `LIKE`."*

---

## 10. Shortcuts — `BETWEEN`, `IN`, `LIKE` (12 minutes)

- **Screen-share the 3 shortcuts with one-liners:**
  - `BETWEEN a AND b` → range (**both ends included**).
  - `IN (a, b, c)` → match any from a list.
  - `LIKE 'pattern'` → text pattern (`%` = any chars, `_` = exactly one char).
- **Live-code each:**
  1. `WHERE Salary BETWEEN 50000 AND 80000` — equivalent to `>= 50000 AND <= 80000`. Narrate: *"Both boundaries included."*
  2. `WHERE City IN ('Delhi', 'Mumbai', 'Bengaluru')` — cleaner than 3 `OR`s. Narrate: *"Database runs this **faster** too."*
  3. `WHERE Name LIKE 'A%'` → names starting with A (Aarav, Anaya).
  4. `WHERE Name LIKE '%a'` → names ending with a (Diya, Meera, Sneha, Anaya, Riya).
  5. **Bonus one-liner:** `WHERE Name LIKE '_i%'` → second letter is 'i' (Diya, Vihaan, Riya, Ishaan).
- **Say it clearly:** *"`%` = **any number of characters** including zero. `_` = **exactly one** character."*
- **Students do:** Write *"Employees whose city name starts with 'B'"* using `LIKE`.
- **Cold-call:** *"`BETWEEN 50000 AND 80000` — is Meera (75000) included? Is Sneha (50000) included?"* (Yes and yes — inclusive.)

**Bridge sentence:** *"One more WHERE case — **missing data**. Databases have a special value for 'we don't know'. It is `NULL`."*

---

## 11. `IS NULL` / `IS NOT NULL` (6 minutes)

- **Screen-share the golden rule:** *"`NULL` = **unknown**. NOT zero. NOT empty string."*
- **Shout it:** *"**`City = NULL` DOES NOT WORK** in SQL. Always `IS NULL` or `IS NOT NULL`."*
- **Live-demo the trap:**
  1. Run `SELECT * FROM employees WHERE City = NULL;` → **0 rows, no error** — misleading!
  2. Fix with `SELECT * FROM employees WHERE City IS NULL;` → correct (in our clean data, 0 rows; but the right query).
  3. Opposite: `WHERE City IS NOT NULL` → all 10 rows.
- **Why this matters in the real world (1 line):** *"Newly joined employees, missing phone numbers, blank address fields — every real dataset has NULLs."*
- **Students do:** Run both queries on our table. Discuss why both queries give different answers only when data actually has NULLs.
- **Check:** **Thumbs up** — *"Will you ever use `= NULL` again?"* (Expect a loud 'No'.)

**Bridge sentence:** *"Filtered data is good. But managers also ask 'sorted by salary, top 3'. That is **`ORDER BY` + `LIMIT`**."*

---

# PART D — Sorting, Limiting & The Full Query Pattern (22 minutes)

---

## 12. `ORDER BY` — ascending, descending, multi-column (8 minutes)

- **Screen-share:** `ORDER BY column [ASC|DESC]`.
- **Analogy (15 sec):** *"Flipkart → 'Sort by price: low to high'. Same data, better view."*
- **Live-code in sequence:**
  1. `ORDER BY Salary` → ascending (default).
  2. `ORDER BY Salary ASC` → same result; **`ASC` is optional**.
  3. `ORDER BY Salary DESC` → highest first.
  4. **Multi-column:** `ORDER BY Department ASC, Salary DESC` → A–Z by Department, within each department highest salary first. **This is the report format managers love.**
- **Say it twice:** *"For **text** columns, ASC = **A→Z**, DESC = **Z→A**. For **numbers**, ASC = **small→big**."*
- **Students do:** Sort employees by `City ASC, JoiningYear DESC`.
- **Cold-call:** *"Within Sales, who comes first on `ORDER BY Department ASC, Salary DESC`?"* (Kabir — highest Sales salary.)

**Bridge sentence:** *"Sorted — great. But the boss only wants **top 3**. That is `LIMIT`."*

---

## 13. `LIMIT` and the Top-N pattern (6 minutes)

- **Screen-share:** `LIMIT n` = return at most **n** rows.
- **Analogy (15 sec):** *"Google shows you the first 10 results, not all 10 crore."*
- **Live-code the Top-N pattern (**this is interview gold**):**
  1. `SELECT * FROM employees LIMIT 3;` — first 3 rows in stored order (**not meaningful**).
  2. `... ORDER BY Salary DESC LIMIT 3;` — **top 3 highest paid**.
  3. `... ORDER BY Salary ASC LIMIT 5;` — **bottom 5**.
  4. `WHERE Department = 'IT' ORDER BY Salary DESC LIMIT 2;` — top 2 IT employees.
- **Say it twice:** *"`LIMIT` without `ORDER BY` is almost always a mistake — you get **random** rows."*
- **One-liner caveat:** *"MySQL/PostgreSQL/SQLite → `LIMIT`. SQL Server → `TOP n`. Same idea, different word."*
- **Students do:** *"Top 3 highest-paid Delhi employees"* — full pattern.
- **Cold-call:** *"What is the answer?"* (Riya 95000, Vihaan 70000, Kabir 60000.)

**Bridge sentence:** *"We have four tools now — `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`. They always appear in **one fixed order**. Let us lock it in."*

---

## 14. The full query order — the SQL backbone (8 minutes)

- **Screen-share this skeleton and make students read it aloud:**

```
SELECT    columns       -- what to show
FROM      table_name    -- which table
WHERE     condition     -- which rows to keep
ORDER BY  column DESC   -- how to arrange
LIMIT     n;            -- how many
```

- **Say it like a mantra:** *"**Select, From, Where, Order By, Limit.** Changing the order is a syntax error."*
- **Live-code the flagship example:** *"Top 3 highest-paid Delhi employees"*:

```sql
SELECT Name, City, Salary
FROM employees
WHERE City = 'Delhi'
ORDER BY Salary DESC
LIMIT 3;
```

- **Walk the execution story (slow, 60 sec):**
  1. `FROM` loads the table.
  2. `WHERE` filters Delhi rows (4 rows).
  3. `ORDER BY Salary DESC` sorts them highest first.
  4. `LIMIT 3` slices the top 3.
  5. `SELECT` finally picks the columns to show.
- **Students do:** Build *"Top 2 most experienced (lowest JoiningYear) non-IT employees"*.
- **Pair-share (60 sec):** Each pair writes one business question; neighbour writes the SQL.
- **Cold-call:** One pair to share.

**Bridge sentence:** *"You now speak SQL. But many of you came in speaking **pandas**. Let us show that they are the **same idea in two languages**."*

---

# PART E — Pandas ↔ SQL Bridge & Close (22 minutes)

---

## 15. Why pandas vs SQL, and setting up the same `df` (3 minutes)

- **Screen-share the one-liner:** *"Pandas runs inside Python on DataFrames. SQL runs inside a database on tables. **Same thinking, different syntax.**"*
- **Analogy (15 sec):** *"Google Maps and Apple Maps show the same roads — different buttons."*
- **Live-code in VS Code:** Open the pre-saved Python file and paste the **same 10-row `df`** (copy-paste from Lecture Notes — dict of 6 lists, `pd.DataFrame(...)`). Run it and print `df` to confirm the same 10 rows.
- **Say it clearly:** *"From now, `employees` in SQL = `df` in pandas — exactly the same 10 rows."*

**Bridge sentence:** *"Let us run **8 side-by-side comparisons** on the same data."*

---

## 16. Side-by-side mappings — 8 key operations (14 minutes)

- **Screen-share (split screen: SQL left, pandas right).** Live-run each pair back-to-back. **Narrate the pattern, not the syntax** — the goal is that students see the *translation* is mechanical.

**Run in this sequence (~90 sec each):**

1. **All rows, all columns** → `SELECT * FROM employees;` ↔ `df`
2. **Specific columns** → `SELECT Name, Salary …` ↔ `df[["Name","Salary"]]`
3. **DISTINCT** → `SELECT DISTINCT Department …` ↔ `df["Department"].unique()`
4. **WHERE single** → `WHERE Salary > 60000` ↔ `df[df["Salary"] > 60000]`
5. **WHERE AND** → `WHERE Dept='Sales' AND Salary>50000` ↔ `df[(df["Department"]=="Sales") & (df["Salary"]>50000)]` — **shout: parentheses are mandatory, and `&` not `and`**.
6. **IN** → `WHERE City IN ('Delhi','Mumbai')` ↔ `df[df["City"].isin(["Delhi","Mumbai"])]`
7. **ORDER BY DESC** → `ORDER BY Salary DESC` ↔ `df.sort_values("Salary", ascending=False)`
8. **LIMIT Top-N** → `... LIMIT 3` ↔ `.head(3)`

- **Finale — the flagship example in both (45 sec):** *"Top 3 highest-paid Delhi employees."*
  - SQL: 5-line query.
  - Pandas: `df[df["City"]=="Delhi"].sort_values("Salary", ascending=False).head(3)[["Name","City","Salary"]]`
  - **Say it loud:** *"**Thinking order is identical** — filter → sort → limit → pick. Only the syntax changes."*
- **Screen-share the one-page mapping table** from the Lecture Notes; bookmark it for the assignment.
- **Check:** **Thumbs up** — *"Any row in the mapping table feel unfamiliar?"*

**Bridge sentence:** *"You can now translate between pandas and SQL both ways. Let us close with the **traps** to avoid."*

---

## 17. Common doubts, cheat sheet & exit (5 minutes)

- **Screen-share the 8-item 'common mistakes' list** (from Lecture Notes) — **15 sec per bullet**:
  - `==` vs `=` (single equal in SQL).
  - Quotes around text only.
  - `IS NULL`, never `= NULL`.
  - Keyword order: SELECT → FROM → WHERE → ORDER BY → LIMIT.
  - Avoid `SELECT *` in production.
  - SQL keywords **not** case-sensitive; **string values ARE**.
  - Semicolon at end.
  - Parentheses when mixing `AND`/`OR`.
- **Screen-share the one-page commands table** — the full cheat sheet.
- **Students do:** Write **one query they will reuse this week**. Drop it in the chat. Instructor picks 2 at random and reads aloud.
- **Closing line:** *"You just learnt the **first half** of SQL — reading data. Next session, same `employees` table, we learn to **modify and combine** data with `UPDATE`, `DELETE`, and `JOIN`."*

---

## Timing flex — if you are running late

- **Cut first from PART A (Why & Types):**
  - Block 2 (Types): skip the Quick Comparison table walkthrough; just name-drop SQL vs NoSQL in 2 minutes.
  - Block 3 (SQL intro): skip the 4 command families list; keep only `SELECT` mention.
- **Cut first from PART C (WHERE):**
  - Block 10 (`BETWEEN`/`IN`/`LIKE`): demo **`IN` and `LIKE 'A%'` only**; mention `BETWEEN` as a one-liner.
  - Block 11 (`IS NULL`): demo once with the trap; skip the opposite `IS NOT NULL` run.
- **Cut first from PART E (Pandas bridge):**
  - Block 16: live-run only **4 mappings** — specific columns, WHERE AND, ORDER BY, LIMIT. Put the rest on-screen as a **reference table** for self-study.
- **Demo-only:** Block 6 (`AS` aliases) — show once, assign variants as homework.
- **Minimum viable session:**
  - Why DB (Block 1, 5 min).
  - Employees table setup + `SELECT *`/specific (Blocks 4+5 combined, 10 min).
  - `DISTINCT` (Block 7, 4 min).
  - `WHERE` with comparison + AND/OR (Blocks 8+9 combined, 15 min).
  - `IN` and `LIKE 'A%'` only (5 min from Block 10).
  - `ORDER BY DESC` + `LIMIT` + full Top-N pattern (Blocks 12+13+14 combined, 15 min).
  - Pandas bridge — 4 mappings + flagship example (10 min from Blocks 15+16).
  - Exit cheat sheet (Block 17, 3 min).
- **If ahead of schedule:**
  - Add a **live debugging** round (10 min): deliberately write `==`, `= NULL`, `ORDER BY` **before** `WHERE`, and a missing `'` around `'Sales'`. Let students spot the 4 errors.
  - Show **`LIKE '_i%'`** and **wildcard escaping** in `LIKE`.
  - Introduce `COUNT(*)` in a single line as a teaser for the next session's aggregation topic.
  - Run the **Top 3 highest-paid Delhi employees** query in both **SQL and pandas back-to-back** a second time, emphasising execution order (FROM → WHERE → ORDER BY → LIMIT → SELECT) because freshers confuse writing order with execution order.
