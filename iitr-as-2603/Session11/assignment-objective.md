# Assignment — Objective: SQL Aggregation and Joining Tables

> **Total Questions:** 10 | **MCQs:** 6 (4 Easy + 2 Moderate) | **MSQs:** 4 (2 Moderate + 2 Hard)
> Ordered progressively: Easy → Moderate → Hard

---

## MCQ — Easy (Questions 1–4)

---

**Question 1**

QuickServe is a food delivery company. Their `orders` table records every order placed — but some orders have a missing `delivery_time` value (i.e., NULL) because the delivery has not yet been logged. The operations manager wants to know the **total number of orders** in the table, including those with missing delivery times.

Which query gives the correct count?

- A. `SELECT COUNT(delivery_time) AS total_orders FROM orders;`
- B. `SELECT COUNT(*) AS total_orders FROM orders;`
- C. `SELECT SUM(*) AS total_orders FROM orders;`
- D. `SELECT AVG(*) AS total_orders FROM orders;`

**Correct Answer:** B

**Answer Explanation:**
`COUNT(*)` counts every row in the table regardless of NULL values in any column — it simply counts how many rows exist. `COUNT(delivery_time)` would only count rows where `delivery_time` is not NULL, which would give a smaller number and miss unlogged orders. `SUM(*)` and `AVG(*)` are invalid SQL syntax — these functions require a specific column name, not `*`.

---

**Question 2**

Priya is a data analyst at a retail chain. She has a `sales` table with columns `city`, `product`, and `sale_amount`. She wants to calculate the **total sales amount for each city** separately. Which SQL clause should she use to separate the results by city before applying the aggregate function?

- A. WHERE
- B. HAVING
- C. GROUP BY
- D. ORDER BY

**Correct Answer:** C

**Answer Explanation:**
`GROUP BY` groups rows that share the same value in the specified column and applies an aggregate function (like `SUM`) independently to each group — exactly what Priya needs. `WHERE` filters individual rows before any grouping happens. `HAVING` filters groups after aggregation. `ORDER BY` only sorts the final result and does not create any grouping.

---

**Question 3**

A university database has two tables: `students` and `exam_results`. Not every student has appeared for the exam, so some students have no corresponding row in `exam_results`. You want to retrieve a list of **all students**, showing their exam marks where available and NULL for students who didn't appear.

Which join type should you use?

- A. INNER JOIN — returns only students who have exam records
- B. LEFT JOIN — returns all students; NULL for those with no exam records
- C. CROSS JOIN — pairs every student with every exam result
- D. INNER JOIN with a WHERE clause checking for NULL

**Correct Answer:** B

**Answer Explanation:**
`LEFT JOIN` keeps every row from the left table (`students`) and brings in the matching rows from the right table (`exam_results`). If a student has no exam record, the exam columns appear as NULL in the result. `INNER JOIN` would exclude students with no exam record entirely. `CROSS JOIN` creates a Cartesian product (every student paired with every exam row), which is not what's needed.

---

**Question 4**

An e-commerce platform has an `orders` table. Each row in `orders` contains a `customer_id` column that links the order to the matching row in the `customers` table. The `customer_id` in the `customers` table uniquely identifies each customer.

What is the `customer_id` column in the `orders` table called?

- A. Primary Key
- B. Index Key
- C. Super Key
- D. Foreign Key

**Correct Answer:** D

**Answer Explanation:**
A **Foreign Key** is a column in one table that references the Primary Key of another table, creating a link between the two. Here, `customer_id` in `orders` references `customer_id` in `customers` — it is a Foreign Key in `orders`. The `customer_id` in `customers` is the **Primary Key** because it uniquely identifies each customer. A Super Key is a broader concept from relational theory, and an Index Key is a database performance concept, not a relational key type.

---

## MCQ — Moderate (Questions 5–6)

---

**Question 5**

A logistics analyst runs this query on a delivery database:

```sql
SELECT city, COUNT(*) AS delivery_count
FROM deliveries
WHERE status = 'completed'
GROUP BY city
HAVING COUNT(*) > 100
ORDER BY delivery_count DESC;
```

In which order does SQL **actually execute** this query — regardless of the order it was written?

- A. SELECT → WHERE → GROUP BY → HAVING → ORDER BY
- B. FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- C. FROM → GROUP BY → WHERE → HAVING → SELECT → ORDER BY
- D. WHERE → FROM → GROUP BY → HAVING → ORDER BY → SELECT

**Correct Answer:** B

**Answer Explanation:**
SQL's internal execution order is fixed: **FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT**. The database first identifies the table (FROM), filters individual rows (WHERE), groups the filtered rows (GROUP BY), filters the groups (HAVING), then selects and formats the output (SELECT), and finally sorts the result (ORDER BY). This explains why you cannot use a SELECT alias in a HAVING clause in most databases — HAVING runs before SELECT.

---

**Question 6**

A junior analyst writes the following query to find customers who have spent more than ₹5,000 in total:

```sql
SELECT customer_id, SUM(order_amount) AS total_spent
FROM orders
WHERE SUM(order_amount) > 5000
GROUP BY customer_id;
```

Why will this query **fail with an error**?

- A. `WHERE` does not support the `>` operator
- B. `WHERE` runs before grouping, so `SUM(order_amount)` has not been computed yet when WHERE is evaluated
- C. `SUM` cannot be combined with `GROUP BY` in the same query
- D. `WHERE` can only filter text columns, not numeric ones

**Correct Answer:** B

**Answer Explanation:**
SQL processes clauses in a fixed order: `WHERE` runs **before** `GROUP BY`. At the WHERE stage, rows have not yet been grouped, so aggregate functions like `SUM()` have not been calculated — they don't exist yet at that point. This is exactly why SQL provides the `HAVING` clause: to filter on aggregated results **after** grouping. The correct version of this query uses `HAVING SUM(order_amount) > 5000` instead of `WHERE SUM(order_amount) > 5000`.

---

## MSQ — Moderate (Questions 7–8)

*Select all correct options.*

---

**Question 7**

A startup's database has a `sales` table with columns `department`, `employee_id`, and `sale_amount`. An analyst writes the following query:

```sql
SELECT department, SUM(sale_amount) AS total_sales, COUNT(*) AS num_sales
FROM sales
GROUP BY department;
```

Which of the following statements about this query are **correct**? *(Select all that apply)*

- A. `department` must appear in the `GROUP BY` clause because it is not inside an aggregate function
- B. `SUM(sale_amount)` computes the total separately for each department, not across the entire table
- C. `GROUP BY` can only be applied to a single column per query
- D. The final result will contain one row per unique `department` value

**Correct Answers:** A, B, D

**Answer Explanation:**
- **(A) Correct** — The Golden Rule of GROUP BY: every non-aggregated column in the SELECT clause must appear in GROUP BY. Since `department` is not wrapped in an aggregate function, it must be listed in GROUP BY.
- **(B) Correct** — GROUP BY creates separate groups (one per department), and `SUM` runs independently within each group.
- **(C) Incorrect** — GROUP BY can group by multiple columns simultaneously (e.g., `GROUP BY city, department`).
- **(D) Correct** — Each unique value in the grouping column becomes exactly one output row.

---

**Question 8**

An HR recruitment platform has a `candidates` table and an `interviews` table, linked by `candidate_id`. A recruiter runs an INNER JOIN between the two tables to build a report.

Which of the following statements correctly describe the behavior of this INNER JOIN? *(Select all that apply)*

- A. Only candidates who have at least one matching row in the `interviews` table will appear in the result
- B. Candidates with no interview records will appear in the result with NULL values in the interview columns
- C. The `ON` clause specifies which columns to match between the two tables
- D. Short table aliases (e.g., `AS c` for candidates, `AS i` for interviews) can be used to write cleaner column references

**Correct Answers:** A, C, D

**Answer Explanation:**
- **(A) Correct** — INNER JOIN returns only rows where a match exists in **both** tables. Candidates with no interview record are excluded entirely.
- **(B) Incorrect** — This describes LEFT JOIN behavior. In an INNER JOIN, unmatched rows do not appear at all — they are not included with NULLs.
- **(C) Correct** — The `ON` clause defines the join condition (e.g., `ON candidates.candidate_id = interviews.candidate_id`).
- **(D) Correct** — Table aliases are standard SQL practice. Using `AS c` and `AS i` lets you write `c.candidate_name` instead of `candidates.candidate_name`.

---

## MSQ — Hard (Questions 9–10)

*Select all correct options.*

---

**Question 9**

Meera is building a customer spending report for an e-commerce company. She writes the following query:

```sql
SELECT c.customer_name,
       COUNT(o.order_id)      AS order_count,
       SUM(o.order_amount)    AS total_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.order_amount) > 10000
ORDER BY total_spent DESC;
```

Which of the following statements about this query are **correct**? *(Select all that apply)*

- A. Customers who have never placed an order will NOT appear in the final output
- B. The LEFT JOIN ensures all customers are included in the intermediate result before HAVING filters them
- C. `COUNT(o.order_id)` correctly returns 0 for customers who have no orders, rather than NULL
- D. Replacing `HAVING SUM(o.order_amount) > 10000` with `WHERE o.order_amount > 10000` would produce the same result

**Correct Answers:** A, B, C

**Answer Explanation:**
- **(A) Correct** — After the LEFT JOIN, customers with no orders have `o.order_amount = NULL`. `SUM(NULL)` evaluates to NULL, and `NULL > 10000` is false, so those customers are filtered out by HAVING.
- **(B) Correct** — LEFT JOIN first brings all customers into the result set (with NULLs for missing order data). HAVING then filters based on the aggregated totals per group.
- **(C) Correct** — `COUNT(o.order_id)` counts non-NULL values. For a customer with no matching orders, `o.order_id` is NULL after the LEFT JOIN, so `COUNT` returns 0 — not NULL.
- **(D) Incorrect** — `WHERE o.order_amount > 10000` filters **individual rows** (only keeping orders larger than ₹10,000 per single order). This is fundamentally different from the HAVING clause, which filters the **total per customer**. A customer who placed twenty orders of ₹800 each (total ₹16,000) would be excluded by the WHERE version but included by the HAVING version.

---

**Question 10**

A telecom company wants to identify employees who have made **more than 100 calls** AND whose **average call duration exceeds 5 minutes**. They have an `employees` table and a `calls` table linked by `employee_id`. Which of the following queries correctly implement this requirement? *(Select all that apply)*

**Option A:**
```sql
SELECT e.employee_name,
       COUNT(c.call_id)  AS call_count,
       AVG(c.duration)   AS avg_duration
FROM employees AS e
INNER JOIN calls AS c ON e.employee_id = c.employee_id
GROUP BY e.employee_id, e.employee_name
HAVING COUNT(c.call_id) > 100 AND AVG(c.duration) > 5;
```

**Option B:**
```sql
SELECT e.employee_name,
       COUNT(c.call_id)  AS call_count,
       AVG(c.duration)   AS avg_duration
FROM employees AS e
INNER JOIN calls AS c ON e.employee_id = c.employee_id
WHERE COUNT(c.call_id) > 100 AND AVG(c.duration) > 5
GROUP BY e.employee_id, e.employee_name;
```

**Option C:**
```sql
SELECT e.employee_name,
       COUNT(c.call_id)  AS call_count,
       AVG(c.duration)   AS avg_duration
FROM employees AS e
LEFT JOIN calls AS c ON e.employee_id = c.employee_id
GROUP BY e.employee_id, e.employee_name
HAVING COUNT(c.call_id) > 100 AND AVG(c.duration) > 5;
```

**Option D:**
```sql
SELECT e.employee_name,
       COUNT(c.call_id)  AS call_count,
       AVG(c.duration)   AS avg_duration
FROM employees AS e
INNER JOIN calls AS c ON e.employee_id = c.employee_id
GROUP BY e.employee_name
HAVING COUNT(c.call_id) > 100 AND AVG(c.duration) > 5;
```

**Correct Answers:** A, C

**Answer Explanation:**
- **(A) Correct** — This is the standard correct approach: INNER JOIN to link employees with their calls, GROUP BY both `employee_id` and `employee_name` (to ensure uniqueness), and HAVING to apply both aggregate conditions.
- **(B) Incorrect** — Aggregate functions (`COUNT`, `AVG`) cannot be used inside a `WHERE` clause. WHERE runs before grouping, so aggregated values don't exist yet. This will throw a SQL error.
- **(C) Correct** — LEFT JOIN also works here. Employees with no calls will have `COUNT = 0` and `AVG = NULL`, both of which fail the HAVING conditions, so they are automatically excluded. The final result is identical to Option A.
- **(D) Incorrect** — `GROUP BY e.employee_name` alone is a logical error. If two employees share the same name (e.g., two people named "Rahul"), their call records would be merged into a single group, producing incorrect counts and averages. A unique identifier like `employee_id` must always be included in GROUP BY.
