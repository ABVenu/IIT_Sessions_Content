# SQL: Joining Data

## What You’ll Learn

In this lesson, you’ll learn how to combine information stored across multiple tables using SQL joins. You’ll understand how `INNER JOIN` and `LEFT JOIN` work, why joins are central to relational database design, and how to build a strong mental model for combining tables correctly. You’ll also compare SQL joins to Pandas’ `merge()` to connect database thinking with Python workflows used in AI systems.

![Session 18](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/3c1c1bab-5b39-4e6a-8874-1552d6b2ceab/GyqdUHY1EWSLmSEi.png)


---

## 1. Why Joining Data Is Essential

Relational databases are designed around **separation of concerns**. Instead of storing everything in one large table, data is split into multiple related tables.

For example:

**users**

| user_id | name   |
|----------|--------|
| 1        | Alice  |
| 2        | Bob    |

**orders**

| order_id | user_id | amount |
|-----------|----------|--------|
| 101       | 1        | 250    |
| 102       | 1        | 100    |
| 103       | 2        | 300    |

The `orders` table does not repeat user names. Instead, it references the `users` table through `user_id`.

This design:
- Avoids duplication
- Preserves consistency
- Supports scalability

But to answer real questions—like “How much did Alice spend?”—you must combine tables.

That is the purpose of a JOIN.

---

## 2. The Mental Model of a JOIN

A JOIN combines rows from two tables based on a related column.

Conceptually:
1. Identify a common key
2. Match rows where the key aligns
3. Construct a new result table

Think of it as lining up rows from two tables where the keys match.

In relational systems, joins are how relationships become useful.

---

## 3. INNER JOIN: Matching Rows Only

An `INNER JOIN` returns only rows where there is a match in both tables.

### Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.key = table2.key;
````

### Example

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;
```

Result:

| name  | amount |
| ----- | ------ |
| Alice | 250    |
| Alice | 100    |
| Bob   | 300    |

Only matching records appear. If a user has no orders, they will not appear in the result.

---

### When to Use INNER JOIN

Use `INNER JOIN` when:

* You only care about matched records
* Both tables must have valid relationships
* Missing matches are irrelevant

In AI pipelines, this is common when:

* Merging feature tables
* Joining events to known users
* Combining datasets with guaranteed overlap

---

## 4. LEFT JOIN: Preserving the Left Table

A `LEFT JOIN` (or `LEFT OUTER JOIN`) returns all rows from the left table and matching rows from the right table.

If no match exists, the right-side columns contain `NULL`.

### Syntax

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.key = table2.key;
```

### Example

```sql
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;
```

If a user has no orders, they still appear:

| name    | amount |
| ------- | ------ |
| Alice   | 250    |
| Alice   | 100    |
| Bob     | 300    |
| Charlie | NULL   |

This ensures no records from the left table are lost.

---

### When to Use LEFT JOIN

Use `LEFT JOIN` when:

* You need all records from one table
* Missing matches are meaningful
* You want to identify gaps

Example in AI:

* Find users with no transactions
* Detect missing metadata
* Identify incomplete feature records

---

## 5. The Power of JOIN in AI Workflows

Joins allow you to:

* Combine user profiles with transaction history
* Merge labels with features
* Integrate metadata with predictions
* Enrich datasets before modeling

Without joins, relational data remains fragmented.

The strength of SQL lies not just in selecting rows—but in combining structured information intelligently.

---

## 6. SQL JOIN vs Pandas `merge()`

If you’ve worked with Pandas, joins will feel familiar.

In Pandas:

```python
merged = pd.merge(users_df, orders_df, on="user_id", how="inner")
```

This corresponds to:

```sql
SELECT *
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id;
```

Similarly:

```python
merged = pd.merge(users_df, orders_df, on="user_id", how="left")
```

Corresponds to:

```sql
SELECT *
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id;
```

---

### Key Mental Differences

SQL:

* Operates inside a database
* Works declaratively (you state what you want)
* Scales to massive datasets

Pandas:

* Operates in memory
* Works programmatically
* Best for local analysis and ML preprocessing

The conceptual model is the same:

> Identify keys → choose join type → combine tables

---

## 7. Common Join Mistakes

* Joining on the wrong column
* Forgetting the `ON` condition
* Confusing INNER and LEFT joins
* Accidentally creating duplicate rows
* Ignoring NULL values

Understanding join behavior is more important than memorizing syntax.

---

## 8. A Practical AI Example

Imagine:

**users**

* user_id
* signup_date

**activity**

* user_id
* login_count

To prepare features:

```sql
SELECT users.user_id,
       users.signup_date,
       activity.login_count
FROM users
LEFT JOIN activity
ON users.user_id = activity.user_id;
```

This ensures all users are included—even those with no recorded activity.

This pattern is extremely common in ML feature engineering.

---

## Key Takeaways

Joins combine data across relational tables using shared keys. `INNER JOIN` returns only matching rows, while `LEFT JOIN` preserves all rows from the left table. Joins are central to relational database design and AI data preparation. The SQL JOIN mental model closely matches Pandas’ `merge()` function, though SQL operates at database scale.

**Mental model:**
Tables separate data.
Keys connect tables.
INNER JOIN matches.
LEFT JOIN preserves.
JOIN turns structure into insight.

---

## Additional Reading

* PostgreSQL JOIN Tutorial:
  [https://www.postgresql.org/docs/current/tutorial-join.html](https://www.postgresql.org/docs/current/tutorial-join.html)

* MySQL JOIN Documentation:
  [https://dev.mysql.com/doc/refman/en/join.html](https://dev.mysql.com/doc/refman/en/join.html)

* Pandas `merge()` Documentation:
  [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)