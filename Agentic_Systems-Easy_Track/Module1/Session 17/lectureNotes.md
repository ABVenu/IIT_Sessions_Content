# SQL: Core Querying

## What You’ll Learn

In this lesson, you’ll learn the foundational SQL commands used to retrieve data from relational databases. You’ll understand how to use `SELECT` to fetch columns, `WHERE` to filter rows, `DISTINCT` to remove duplicates, `ORDER BY` to sort results, and `LIMIT` and aliases to control output clarity. These tools form the core vocabulary of SQL and are used daily in data analysis, backend engineering, and AI data preparation workflows.


![Session 17](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/09c9ea99-98a5-4776-afe6-337e7bc16759/VlwwpQUQEXuqAgmg.png)

---

## 1. Why Querying Matters in AI Systems

AI systems depend on high-quality, structured data. Before training a model, generating features, or analyzing performance, engineers must retrieve the correct data from databases.

SQL querying allows you to:

- Extract specific subsets of data  
- Filter records based on conditions  
- Rank and sort results  
- Reduce noise and duplication  
- Prepare structured outputs for downstream systems  

In production environments, SQL is often the first step in any AI pipeline.

---

## 2. SELECT: Choosing What to Retrieve

The `SELECT` statement tells the database which columns to return.

Basic syntax:

```sql
SELECT column_name
FROM table_name;
````

Example:

```sql
SELECT name
FROM users;
```

This retrieves only the `name` column from the `users` table.

To retrieve multiple columns:

```sql
SELECT name, email
FROM users;
```

To retrieve all columns:

```sql
SELECT *
FROM users;
```

Using `SELECT *` is convenient for exploration but discouraged in production systems, where explicit column selection improves clarity and performance.

---

## 3. WHERE: Filtering Rows

The `WHERE` clause restricts which rows are returned.

Example:

```sql
SELECT name, score
FROM students
WHERE score > 85;
```

This returns only students with scores above 85.

Common comparison operators:

* `=`  (equal)
* `!=` (not equal)
* `>`  (greater than)
* `<`  (less than)
* `>=`
* `<=`

You can combine conditions:

```sql
SELECT name
FROM students
WHERE score > 85 AND passed = TRUE;
```

Logical operators include:

* `AND`
* `OR`
* `NOT`

Filtering is essential in AI workflows to:

* Select training subsets
* Remove invalid records
* Segment users
* Define experimental cohorts

---

## 4. DISTINCT: Removing Duplicates

Sometimes a column contains repeated values. The `DISTINCT` keyword ensures unique results.

Example:

```sql
SELECT DISTINCT city
FROM users;
```

This returns each city only once.

Without `DISTINCT`, duplicate entries would appear multiple times.

`DISTINCT` is commonly used when:

* Counting unique categories
* Identifying unique labels
* Exploring dataset diversity

---

## 5. ORDER BY: Sorting Results

Sorting makes patterns visible and supports ranking.

Basic syntax:

```sql
SELECT name, score
FROM students
ORDER BY score;
```

By default, sorting is ascending.

For descending order:

```sql
SELECT name, score
FROM students
ORDER BY score DESC;
```

You can sort by multiple columns:

```sql
SELECT name, score, class
FROM students
ORDER BY class ASC, score DESC;
```

Sorting is critical in AI workflows when:

* Identifying top predictions
* Ranking performance metrics
* Finding extreme values

---

## 6. LIMIT: Controlling Result Size

The `LIMIT` clause restricts how many rows are returned.

Example:

```sql
SELECT *
FROM students
LIMIT 5;
```

This is useful for:

* Previewing data
* Testing queries safely
* Reducing load on large datasets

In production systems, limiting results improves efficiency and reduces unnecessary data transfer.

---

## 7. Aliases: Improving Readability

Aliases rename columns or tables temporarily within a query.

Column alias:

```sql
SELECT score AS exam_score
FROM students;
```

Table alias:

```sql
SELECT s.name
FROM students AS s;
```

Aliases improve clarity, especially in complex queries involving multiple tables.

They also help prepare clean output fields for downstream systems.

---

## 8. A Complete Example

```sql
SELECT name, score AS final_score
FROM students
WHERE score > 75
ORDER BY score DESC
LIMIT 10;
```

This query:

1. Selects specific columns
2. Renames one column
3. Filters rows
4. Sorts results
5. Returns only the top 10 entries

This is a typical pattern in analytics and AI feature preparation.

---

## 9. How These Commands Work Together

SQL queries follow a logical structure:

1. `SELECT` – What data do you want?
2. `FROM` – Where is the data?
3. `WHERE` – Which rows should be included?
4. `ORDER BY` – How should results be sorted?
5. `LIMIT` – How many results should be returned?

Understanding this order helps you write clean, predictable queries.

---

## 10. Common Beginner Mistakes

* Forgetting the `WHERE` clause and retrieving too much data
* Using `SELECT *` in production
* Confusing `AND` and `OR`
* Forgetting `DESC` when ranking high values
* Misplacing clauses in the wrong order

SQL has a strict structure. Learning its grammar is like learning a new language.

---

## Key Takeaways

`SELECT` retrieves columns.
`WHERE` filters rows.
`DISTINCT` removes duplicates.
`ORDER BY` sorts results.
`LIMIT` controls output size.
Aliases improve readability.

Together, these commands form the foundation of SQL querying. Mastering them enables efficient, precise data retrieval for analytics and AI systems.

---

## Additional Reading

* PostgreSQL SQL Tutorial:
  [https://www.postgresql.org/docs/current/tutorial-select.html](https://www.postgresql.org/docs/current/tutorial-select.html)

* SQL SELECT Documentation (MySQL):
  [https://dev.mysql.com/doc/refman/en/select.html](https://dev.mysql.com/doc/refman/en/select.html)

* Google Cloud SQL Query Basics:
  [https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)