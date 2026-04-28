# Assignment – Objective Questions
## Session 10: SQL – Querying Data with SELECT and WHERE

---

### Q1 (MCQ | Easy)

Priya is a junior data analyst at a logistics company. She has just been given access to the company's `employees` database and wants to see **every column and every row** of the table to understand its structure before starting any analysis. Which SQL query should she run?

**Options:**
- A) `SELECT ALL FROM employees;`
- B) `SELECT employees FROM *;`
- C) `SELECT * FROM employees;`
- D) `FROM employees SELECT *;`

**Answer:** C

**Explanation:**
`SELECT * FROM employees;` is the correct syntax. `SELECT *` means "give me all columns", and `FROM employees` tells the database which table to read from. Option A (`SELECT ALL`) is not valid SQL syntax. Option B has the table and wildcard positions swapped. Option D reverses the required keyword order — SQL always starts with `SELECT`, then `FROM`.

---

### Q2 (MCQ | Easy)

Rajan, an HR manager at a manufacturing firm, needs to pull records of all employees who joined his company **on or after the year 2020** to plan a batch appraisal cycle. The table is `employees` and the column is `JoiningYear`. Which SQL clause correctly filters those records?

**Options:**
- A) `HAVING JoiningYear >= 2020`
- B) `ORDER BY JoiningYear >= 2020`
- C) `LIMIT JoiningYear >= 2020`
- D) `WHERE JoiningYear >= 2020`

**Answer:** D

**Explanation:**
`WHERE` is the SQL clause used to filter rows based on a condition. `WHERE JoiningYear >= 2020` checks each row and keeps only those where the joining year is 2020 or later. `HAVING` is used with GROUP BY for aggregate filtering (not covered yet). `ORDER BY` sorts rows — it does not filter. `LIMIT` restricts how many rows are returned — it does not filter by condition.

---

### Q3 (MCQ | Easy)

A sales director at ShopBridge asks her analyst to find out **which unique cities** their employees are based in — she only wants each city name listed once, with no repetitions. The analyst runs this query on the `employees` table from the lecture:

```sql
SELECT DISTINCT City FROM employees;
```

How many rows will the result contain, and which cities will appear?

**Options:**
- A) 10 rows – all city names including repetitions
- B) 4 rows – Sales, HR, IT, Finance
- C) 1 row – showing a count of distinct cities
- D) 3 rows – Delhi, Mumbai, Bengaluru

**Answer:** D

**Explanation:**
`DISTINCT` removes duplicate values and returns each unique entry only once. Looking at the `employees` table from the lecture, the City column contains: Delhi (×4), Mumbai (×3), Bengaluru (×3). `DISTINCT` collapses these into 3 unique values: Delhi, Mumbai, Bengaluru. Option A (10 rows) would be the result without DISTINCT. Option B lists departments, not cities. Option C would require a COUNT() function, not DISTINCT alone.

---

### Q4 (MCQ | Easy)

A data engineer at a fintech startup is working with a `transactions` table that has over 10 lakh rows. Before writing a complex query, she wants to quickly **preview just the first 5 rows** to check the column names and data format. Which keyword should she add to her `SELECT` query to do this in MySQL?

**Options:**
- A) `TOP 5`
- B) `FETCH 5`
- C) `ROWS 5`
- D) `LIMIT 5`

**Answer:** D

**Explanation:**
`LIMIT 5` is the correct keyword in MySQL, PostgreSQL, and SQLite to restrict output to the first N rows. `TOP 5` is used in Microsoft SQL Server — not MySQL. `FETCH` and `ROWS` are not valid standalone SQL keywords for this purpose. Adding `LIMIT 5` at the end of any SELECT query ensures only 5 rows are returned, which is very useful for quick previews.

---

### Q5 (MCQ | Moderate)

Arjun, a data analyst at a retail company, runs the following query on the `employees` table from the lecture to find the company's top IT earners:

```sql
SELECT Name, Salary
FROM employees
WHERE Department = 'IT'
ORDER BY Salary DESC
LIMIT 2;
```

Referring to the `employees` dataset in the lecture, which two employees will appear in the result?

**Options:**
- A) Aarav (₹40,000) and Diya (₹55,000)
- B) Meera (₹75,000) and Rohan (₹90,000)
- C) Riya (₹95,000) and Rohan (₹90,000)
- D) Riya (₹95,000) and Meera (₹75,000)

**Answer:** C

**Explanation:**
The IT department has 3 employees: Meera (₹75,000), Rohan (₹90,000), and Riya (₹95,000). `ORDER BY Salary DESC` sorts them highest first: Riya → Rohan → Meera. `LIMIT 2` then returns only the top 2: **Riya (₹95,000)** and **Rohan (₹90,000)**. Option B and D are incorrect because Meera at ₹75,000 ranks third — she is cut off by the LIMIT. Option A lists Sales and HR employees who don't satisfy `WHERE Department = 'IT'`.

---

### Q6 (MCQ | Moderate)

Sana, a new SQL learner, writes the following query after coming from a Python background. She gets a syntax error when she runs it:

```sql
SELECT Name, Department
FROM employees
WHERE Department == 'Sales';
```

What is the mistake, and what is the correct fix?

**Options:**
- A) `Department` should be wrapped in quotes: `'Department' == 'Sales'`
- B) `WHERE` should be replaced with `HAVING` for text comparisons
- C) `==` should be replaced with `=` — SQL uses a single equal sign for comparison
- D) The query is correct; `==` and `=` are both accepted in SQL

**Answer:** C

**Explanation:**
In Python (and JavaScript), `==` is used for equality checks, which is why Sana made this mistake. However, in SQL, equality comparison always uses a **single `=`** sign. Writing `==` causes a syntax error in all major SQL databases. Column names are never wrapped in quotes (that's for text values). `HAVING` is used with GROUP BY aggregations, not simple row filtering. The correct query is `WHERE Department = 'Sales'`.

---

### Q7 (MSQ | Moderate)

Kavitha is a data analyst at a healthcare company. She wants to retrieve all employees from the `employees` table who **either work in the IT department OR earn more than ₹80,000** (or both). Which of the following SQL queries will give her the correct result? *(Select all that apply)*

**Options:**
- A) `SELECT * FROM employees WHERE Department = 'IT' OR Salary > 80000;`
- B) `SELECT * FROM employees WHERE Department = 'IT' AND Salary > 80000;`
- C) `SELECT * FROM employees WHERE Salary > 80000 OR Department = 'IT';`
- D) `SELECT * FROM employees WHERE NOT (Department != 'IT' AND Salary <= 80000);`

**Answer:** A, C, D

**Explanation:**
- **A:** Correct — directly uses `OR` to match IT employees or high earners.
- **B:** Incorrect — `AND` requires **both** conditions to be true simultaneously, which would return only IT employees who also earn more than ₹80,000. This is a much narrower result.
- **C:** Correct — identical logic to A; `OR` is commutative so swapping the conditions gives the same result.
- **D:** Correct — applying De Morgan's Law: `NOT (Department != 'IT' AND Salary <= 80000)` simplifies to `(Department = 'IT' OR Salary > 80000)` — exactly what Kavitha wants.

---

### Q8 (MSQ | Moderate)

A company's database administrator is onboarding a new intern and explains how SQL handles missing data differently from Excel or Python. Based on what was covered in the lecture, which of the following statements about **NULL** in SQL are correct? *(Select all that apply)*

**Options:**
- A) NULL means "no value entered" or "unknown" — it is NOT the same as 0 or an empty string
- B) You can find rows with missing values using `WHERE City = NULL`
- C) `IS NULL` is the correct syntax to find rows where a column has no value recorded
- D) `IS NOT NULL` returns only rows where the column has an actual value stored

**Answer:** A, C, D

**Explanation:**
- **A:** Correct — NULL represents the **absence of any value**. It is fundamentally different from 0 (a valid number) or `''` (an empty string).
- **B:** Incorrect — `= NULL` does **not** work in SQL. Because NULL represents the unknown, it cannot be compared using `=`. The result of any `= NULL` comparison is always NULL (neither TRUE nor FALSE). You must use `IS NULL`.
- **C:** Correct — `IS NULL` is the proper SQL syntax for checking missing values.
- **D:** Correct — `IS NOT NULL` is the inverse, returning rows where data is present.

---

### Q9 (MSQ | Hard)

A senior analyst at a logistics company runs the following query on the `employees` table from the lecture to identify mid-to-high earners in the Finance and IT departments:

```sql
SELECT Name, Department, Salary
FROM employees
WHERE Department IN ('Finance', 'IT')
  AND Salary BETWEEN 70000 AND 90000;
```

Referring to the dataset in the lecture, which employees will appear in the result? *(Select all that apply)*

**Options:**
- A) Vihaan (Finance, ₹70,000)
- B) Riya (IT, ₹95,000)
- C) Ishaan (Finance, ₹85,000)
- D) Meera (IT, ₹75,000)
- E) Rohan (IT, ₹90,000)

**Answer:** A, C, D, E

**Explanation:**
First, `IN ('Finance', 'IT')` keeps only Finance and IT employees:
- Finance: Vihaan (₹70,000), Ishaan (₹85,000)
- IT: Meera (₹75,000), Rohan (₹90,000), Riya (₹95,000)

Then `BETWEEN 70000 AND 90000` (both ends **inclusive**) filters further:
- Vihaan ₹70,000 ✓ (equals lower bound)
- Ishaan ₹85,000 ✓
- Meera ₹75,000 ✓
- Rohan ₹90,000 ✓ (equals upper bound)
- Riya ₹95,000 ✗ (exceeds 90,000 — excluded)

So **Riya is the only one excluded**, because ₹95,000 is above the upper limit.

---

### Q10 (MSQ | Hard)

Neha, a Python developer at a data consulting firm, is migrating her team's pandas analysis scripts into SQL queries so they can be run directly against the company's MySQL database. She has the `employees` DataFrame `df` (same data as in the lecture). Which of the following **pandas → SQL translations** are correct? *(Select all that apply)*

**Options:**
- A) `df["Department"].unique()` → `SELECT DISTINCT Department FROM employees;`
- B) `df.sort_values("Salary", ascending=True).head(5)` → `SELECT * FROM employees ORDER BY Salary DESC LIMIT 5;`
- C) `df[(df["City"] == "Delhi") & (df["Salary"] >= 70000)]` → `SELECT * FROM employees WHERE City = 'Delhi' AND Salary >= 70000;`
- D) `df[df["City"].isna()]` → `SELECT * FROM employees WHERE City IS NULL;`

**Answer:** A, C, D

**Explanation:**
- **A:** Correct — `.unique()` removes duplicates in pandas, exactly as `DISTINCT` does in SQL.
- **B:** Incorrect — `ascending=True` means sorting **low to high (ASC)**, but the SQL says `ORDER BY Salary DESC` which sorts **high to low**. The correct SQL equivalent would be `ORDER BY Salary ASC LIMIT 5`.
- **C:** Correct — `&` in pandas corresponds to `AND` in SQL. The double-equals `==` in pandas matches single `=` in SQL. The logic is identical.
- **D:** Correct — `.isna()` in pandas checks for missing values, which maps to `IS NULL` in SQL. Both return rows where the column has no recorded value.
