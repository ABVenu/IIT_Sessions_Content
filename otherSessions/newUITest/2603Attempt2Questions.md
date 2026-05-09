# IITR-AS-2603 | Module 1 — Objective Assignment Questions (Attempt 2)

**Course:** Certification in Agentic Systems and Design (IITRAS-2603)
**Module:** Module 1
**Type:** Objective Assignment
**Structure:** 6 MCQs (4 Easy · 2 Moderate) + 4 MSQs (2 Moderate · 2 Hard)
**Total Questions:** 10

> Questions are ordered progressively: Easy → Moderate → Hard

---

## MCQ — Easy (Single Correct Answer)

---

### Q1. MCQ | Easy | Topic: Python Basics — Variables, Data Types & Operators

Priya is writing her first Python script to track her monthly budget. She runs the following code:

```python
income = 50000
expenses = 18700
savings = income - expenses
print(type(savings))
```

What will be the output?

**A)** `<class 'float'>`
**B)** `<class 'str'>`
**C)** `<class 'int'>`
**D)** `<class 'number'>`

---

**Correct Answer:** C

**Explanation:**

`income` (50000) and `expenses` (18700) are both integer literals. Subtracting two integers in Python produces an integer. Therefore `type(savings)` returns `<class 'int'>`.

- **A is wrong:** Float is only produced when at least one operand has a decimal point (e.g., 50000.0).
- **B is wrong:** `str` is the string type. Arithmetic on integers never returns a string unless explicitly converted with `str()`.
- **D is wrong:** `'number'` is not a valid Python type name.

---

### Q2. MCQ | Easy | Topic: Operators & Conditional Statements

Rohan is building a ticket booking system. He writes the following code to determine the ticket price based on age:

```python
age = int(input("Enter age: "))

if age < 5:
    print("Free")
elif age <= 12:
    print("Half Price")
elif age <= 59:
    print("Full Price")
else:
    print("Senior Discount")
```

A user enters **65**. What will be printed?

**A)** `Full Price`
**B)** `Half Price`
**C)** `Free`
**D)** `Senior Discount`

---

**Correct Answer:** D

**Explanation:**

The value 65 is checked against each condition in order:
1. `65 < 5` → False
2. `65 <= 12` → False
3. `65 <= 59` → False
4. Falls through to `else` → prints `"Senior Discount"`

- **A is wrong:** `Full Price` requires `age` to be between 13 and 59 inclusive.
- **B is wrong:** `Half Price` requires `age` to be between 5 and 12 inclusive.
- **C is wrong:** `Free` requires `age` to be less than 5.

---

### Q3. MCQ | Easy | Topic: Loops & Iterations

Sneha needs to find the total marks scored by a student across 5 subjects. She uses a `while` loop:

```python
marks = [72, 85, 90, 68, 77]
total = 0
i = 0

while i < len(marks):
    total += marks[i]
    i += 1

print(total)
```

What will be the output?

**A)** `390`
**B)** `392`
**C)** `77`
**D)** `0`

---

**Correct Answer:** B

**Explanation:**

The loop adds each element of `marks`:
72 + 85 + 90 + 68 + 77 = **392**

- **A is wrong:** 390 is incorrect arithmetic — a common off-by-one slip.
- **C is wrong:** 77 is just the last element in the list, not the sum.
- **D is wrong:** `total` starts at 0 but gets accumulated through the loop; the loop runs 5 times before `i < 5` becomes False.

---

### Q4. MCQ | Easy | Topic: Lists & Functions

Arjun is building a temperature converter tool. He defines the following function and calls it:

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temps_c = [0, 25, 100]
result = celsius_to_fahrenheit(temps_c[1])
print(result)
```

What will be the output?

**A)** `77.0`
**B)** `32.0`
**C)** `212.0`
**D)** `25.0`

---

**Correct Answer:** A

**Explanation:**

`temps_c[1]` accesses index 1, which is `25`. Plugging into the formula:
(25 × 9/5) + 32 = 45 + 32 = **77.0**

- **B is wrong:** 32.0 is the result for 0°C (index 0).
- **C is wrong:** 212.0 is the result for 100°C (index 2).
- **D is wrong:** 25.0 is the raw Celsius value before conversion — the function would never return the input unchanged given this formula.

---

## MCQ — Moderate (Single Correct Answer)

---

### Q5. MCQ | Moderate | Topic: Version Control and GitHub Basics

Meera has been working on a data analysis project on her laptop. She cloned the repository two days ago, made changes to `analysis.py`, staged them using `git add analysis.py`, and committed with a meaningful message. Now her colleague cannot see her changes on GitHub.

Which command does Meera still need to run to make her changes visible on the remote repository?

**A)** `git pull origin main`
**B)** `git clone https://github.com/meera/data-project.git`
**C)** `git push origin main`
**D)** `git merge main`

---

**Correct Answer:** C

**Explanation:**

`git add` stages changes locally. `git commit` saves them to the local repository history. However, the remote repository (GitHub) is not updated until changes are explicitly **pushed** using `git push origin main`.

- **A is wrong:** `git pull` fetches and merges changes *from* the remote *into* the local branch — the opposite of what Meera needs.
- **B is wrong:** `git clone` creates a fresh local copy of a repository. Running it again would not upload Meera's changes.
- **D is wrong:** `git merge` combines branches in the local repository; it does not interact with the remote at all.

---

### Q6. MCQ | Moderate | Topic: NumPy — Numerical Foundations

Vikram is analyzing a dataset of 12 monthly sales figures. He stores them in a NumPy array and wants to reshape it into a 3-row, 4-column matrix for region-wise analysis:

```python
import numpy as np
sales = np.array([120, 150, 90, 200, 175, 135, 160, 110, 145, 180, 95, 165])
matrix = sales.reshape(3, 4)
print(matrix.shape)
```

What will be the output?

**A)** `(4, 3)`
**B)** `(12,)`
**C)** `(3, 4)`
**D)** `ValueError: cannot reshape`

---

**Correct Answer:** C

**Explanation:**

`reshape(3, 4)` reorganises the 12 elements into 3 rows and 4 columns. The total elements must match: 3 × 4 = 12 ✓. `matrix.shape` returns a tuple `(rows, columns)` → **(3, 4)**.

- **A is wrong:** `(4, 3)` would be the shape if `reshape(4, 3)` were called.
- **B is wrong:** `(12,)` is the shape of the original 1D array before reshaping.
- **D is wrong:** No error occurs because 3 × 4 = 12, which exactly matches the number of elements.

---

## MSQ — Moderate (Multiple Correct Answers)

---

### Q7. MSQ | Moderate | Topic: Strings, Dictionaries & Classes

Kiran is building a mini student portal. He creates a dictionary to store a student's profile and performs several operations:

```python
profile = {"name": "Aisha", "age": 21, "grade": "A", "city": "Pune"}

op1 = profile["name"].upper()
op2 = profile.get("email")
op3 = len(profile)
op4 = "grade" in profile
op5 = profile["score"]
```

Which of the following statements are **TRUE**? *(Select all that apply)*

**A)** `op1` evaluates to `"AISHA"`
**B)** `op2` evaluates to `None`
**C)** `op3` evaluates to `4`
**D)** `op4` evaluates to `False`
**E)** `op5` raises a `KeyError`

---

**Correct Answers:** A, B, C, E

**Explanation:**

- **A is correct:** `profile["name"]` → `"Aisha"`, and `.upper()` converts all characters to uppercase → `"AISHA"`.
- **B is correct:** `.get("email")` safely returns `None` when the key does not exist (unlike direct bracket access).
- **C is correct:** The dictionary has 4 key-value pairs: `name`, `age`, `grade`, `city` → `len()` returns `4`.
- **D is wrong:** `"grade"` *is* a key in the dictionary. The `in` operator checks for key existence, so `op4` evaluates to `True`, not `False`.
- **E is correct:** `profile["score"]` uses direct bracket access on a non-existent key, which always raises a `KeyError` in Python.

---

### Q8. MSQ | Moderate | Topic: SQL — Querying Data with SELECT and WHERE

Deepa is querying a company's `employees` table with columns: `emp_id`, `name`, `department`, `salary`, `city`. She wants to retrieve the **name and salary** of all employees in the `'HR'` department who earn **more than 45000**.

Which of the following SQL queries correctly return this result? *(Select all that apply)*

**A)**
```sql
SELECT name, salary FROM employees
WHERE department = 'HR' AND salary > 45000;
```

**B)**
```sql
SELECT * FROM employees
WHERE department = 'HR' AND salary > 45000;
```

**C)**
```sql
SELECT name, salary FROM employees
WHERE department = 'HR' OR salary > 45000;
```

**D)**
```sql
SELECT name, salary FROM employees
WHERE salary > 45000 AND department = 'HR';
```

**E)**
```sql
SELECT name, salary FROM employees
WHERE department = 'HR' AND salary > 45000
ORDER BY salary DESC;
```

---

**Correct Answers:** A, D, E

**Explanation:**

- **A is correct:** Selects exactly `name` and `salary`, with the correct AND condition.
- **B is wrong:** Uses `SELECT *` which returns all columns — the question specifies only `name` and `salary` should be retrieved.
- **C is wrong:** `OR` means a row is included if it is in `HR` *or* earns above 45000, not both. This returns more rows than intended.
- **D is correct:** SQL conditions with `AND` are commutative — swapping the order of conditions produces identical results.
- **E is correct:** Adding `ORDER BY salary DESC` does not change *which* rows are returned; the filter is unchanged. The query is still correct, just sorted.

---

## MSQ — Hard (Multiple Correct Answers)

---

### Q9. MSQ | Hard | Topic: Pandas — Indexing, Filtering & Aggregation

Rahul has a retail DataFrame `df` with columns: `store_id`, `region`, `product`, `units_sold`, `revenue`. He needs to:
1. Filter rows where `revenue` is greater than **10000**
2. Group the filtered data by `region`
3. Compute the **total units sold** and **average revenue** per region

Which of the following code snippets correctly complete all three steps? *(Select all that apply)*

**A)**
```python
filtered = df[df["revenue"] > 10000]
result = filtered.groupby("region").agg({"units_sold": "sum", "revenue": "mean"})
```

**B)**
```python
filtered = df.loc[df["revenue"] > 10000]
result = filtered.groupby("region").agg(
    total_units=("units_sold", "sum"),
    avg_revenue=("revenue", "mean")
)
```

**C)**
```python
result = (df[df["revenue"] > 10000]
          .groupby("region")
          .agg({"units_sold": "sum", "revenue": "mean"}))
```

**D)**
```python
result = df.groupby("region").agg({"units_sold": "sum", "revenue": "mean"})
result = result[result["revenue"] > 10000]
```

**E)**
```python
filtered = df[df["revenue"] > 10000]
result = filtered.groupby("region")[["units_sold", "revenue"]].mean()
```

---

**Correct Answers:** A, B, C

**Explanation:**

- **A is correct:** Boolean indexing filters rows first, then `groupby` + `agg` computes total `units_sold` (sum) and average `revenue` (mean) per region.
- **B is correct:** `df.loc[condition]` is equivalent to boolean indexing `df[condition]` for filtering. The named aggregation syntax `(col, func)` is an alternative to the dict form and produces the same grouped result.
- **C is correct:** Method chaining applies the filter and aggregation in one expression — semantically identical to A.
- **D is wrong:** Here the filter `result["revenue"] > 10000` is applied *after* aggregation, which means it filters regions whose **average revenue** exceeds 10000 — not rows where individual revenue exceeds 10000. This changes the semantics.
- **E is wrong:** Using `.mean()` computes the average of *both* `units_sold` and `revenue`. The question requires `sum` for `units_sold` and `mean` for `revenue` — so this does not satisfy the requirement.

---

### Q10. MSQ | Hard | Topic: SQL — Aggregation and Joining Tables

Nisha is analysing an e-commerce database with two tables:

- `orders` — columns: `order_id`, `customer_id`, `amount`, `status`
- `customers` — columns: `customer_id`, `name`, `city`

She wants to find the **total order amount per city**, but only include cities where the **total exceeds ₹100,000**.

Which of the following SQL queries correctly produce this result? *(Select all that apply)*

**A)**
```sql
SELECT c.city, SUM(o.amount) AS total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 100000;
```

**B)**
```sql
SELECT c.city, SUM(o.amount) AS total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE SUM(o.amount) > 100000
GROUP BY c.city;
```

**C)**
```sql
SELECT c.city, SUM(o.amount) AS total_amount
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 100000;
```

**D)**
```sql
SELECT c.city, COUNT(o.amount) AS total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
HAVING COUNT(o.amount) > 100000;
```

**E)**
```sql
SELECT c.city, SUM(o.amount) AS total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 100000;
```

---

**Correct Answers:** A, C, E

**Explanation:**

- **A is correct:** `INNER JOIN` pairs each order with its customer, `GROUP BY city` aggregates, and `HAVING SUM(o.amount) > 100000` filters groups by the aggregate total — exactly what is needed.
- **B is wrong:** `WHERE` is evaluated *before* grouping and **cannot** reference aggregate functions like `SUM()`. This query would throw a syntax/logic error. `HAVING` must always be used to filter on aggregated values.
- **C is correct:** `LEFT JOIN` keeps all orders even if a matching customer record is somehow missing. For valid transactional data, this produces the same result as INNER JOIN, and the `HAVING` filter correctly limits to cities with total > 100000.
- **D is wrong:** `COUNT(o.amount)` counts the *number of orders*, not the total monetary amount. The alias `total_amount` is misleading here. This query answers "cities with more than 100000 orders" — an entirely different question.
- **E is correct:** Flipping the table order in `FROM` and `JOIN` while keeping `INNER JOIN` produces the identical result set — INNER JOIN is symmetric. Using `SUM(o.amount)` directly in `HAVING` is standard SQL and works across all databases.

---

## Summary Table

| Q# | Type | Difficulty | Topic                                     | Correct Answer(s) |
|----|------|------------|-------------------------------------------|-------------------|
| 1  | MCQ  | Easy       | Python Basics — Variables & Operators     | C                 |
| 2  | MCQ  | Easy       | Conditional Statements (if/elif/else)     | D                 |
| 3  | MCQ  | Easy       | Loops & Iterations (while loop)           | B                 |
| 4  | MCQ  | Easy       | Lists & Functions                         | A                 |
| 5  | MCQ  | Moderate   | Version Control & GitHub                  | C                 |
| 6  | MCQ  | Moderate   | NumPy — Reshape & Shape                   | C                 |
| 7  | MSQ  | Moderate   | Strings, Dictionaries & Classes           | A, B, C, E        |
| 8  | MSQ  | Moderate   | SQL — SELECT & WHERE                      | A, D, E           |
| 9  | MSQ  | Hard       | Pandas — Indexing, Filtering & Aggregation| A, B, C           |
| 10 | MSQ  | Hard       | SQL — Aggregation & Joins                 | A, C, E           |
