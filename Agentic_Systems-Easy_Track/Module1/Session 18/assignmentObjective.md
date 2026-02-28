# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

What is the primary purpose of a SQL JOIN?

A) To delete duplicate rows
B) To combine rows from multiple tables based on a related column
C) To sort data
D) To rename columns

**Correct answer:** B

**Explanation:**
A JOIN combines rows from two (or more) tables using a shared key. This allows related data stored separately (such as users and orders) to be analyzed together.

---

### **2. (MCQ)**

What does an `INNER JOIN` return?

A) All rows from both tables
B) Only rows that exist in the left table
C) Only rows where matching keys exist in both tables
D) All rows from the right table

**Correct answer:** C

**Explanation:**
`INNER JOIN` returns only rows where the join condition matches in both tables. If a row in one table has no corresponding match in the other, it is excluded from the result.

---

### **3. (MCQ)**

What happens when using a `LEFT JOIN` and no matching row exists in the right table?

A) The row is removed
B) The query fails
C) The right-side columns return NULL values
D) The row is duplicated

**Correct answer:** C

**Explanation:**
A `LEFT JOIN` preserves all rows from the left table. If no match exists in the right table, the right-side columns are filled with `NULL`.

---

### **4. (MCQ)**

In the following query, what is the join condition?

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;
```

A) `users.name = orders.amount`
B) `users.user_id = orders.user_id`
C) `INNER JOIN orders`
D) `SELECT users.name`

**Correct answer:** B

**Explanation:**
The `ON` clause defines the join condition. It specifies how rows from the two tables are matched — here, matching `user_id` values.

---

### **5. (MCQ)**

When should you prefer a `LEFT JOIN` over an `INNER JOIN`?

A) When only matched records matter
B) When missing matches are meaningful and must be preserved
C) When both tables have identical data
D) When sorting is required

**Correct answer:** B

**Explanation:**
Use `LEFT JOIN` when you need all records from the left table, even if no matching record exists in the right table. This is common when identifying missing data or incomplete feature records.

---

### **6. (MCQ)**

What is a common mistake when writing JOIN queries?

A) Using SELECT before FROM
B) Joining tables without specifying an ON condition
C) Using WHERE after ORDER BY
D) Using aliases

**Correct answer:** B

**Explanation:**
Forgetting the `ON` condition can create unintended Cartesian products (every row joined with every other row), leading to incorrect and extremely large result sets.

---

### **7. (MCQ)**

Which Pandas function corresponds conceptually to a SQL JOIN?

A) `groupby()`
B) `concat()`
C) `merge()`
D) `sort_values()`

**Correct answer:** C

**Explanation:**
`pd.merge()` performs table joins in Pandas, similar to SQL JOIN operations. The `how` parameter (`inner`, `left`) mirrors SQL join types.

---

### **8. (MCQ)**

What is the result of joining two tables where one user has multiple matching rows in the second table?

A) Only one row is returned
B) The database removes duplicates automatically
C) Multiple rows are returned — one for each match
D) The query fails

**Correct answer:** C

**Explanation:**
If a row in the left table matches multiple rows in the right table, the result includes multiple rows — one for each matching pair. This is expected join behavior and a common source of unintended duplication.
