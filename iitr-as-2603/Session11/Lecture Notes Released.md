# SQL: Aggregation and Joining Tables

## What We Covered So Far and What's Coming Next

In the previous session, we explored the foundations of SQL querying. We learned how to use **SELECT** to pick specific columns from a table, how to filter rows using **WHERE** with comparison and logical operators, and how to sort and limit results using **ORDER BY** and **LIMIT**. We also saw how SQL querying maps to pandas DataFrame operations.

Now that you know how to *find* data, it's time to learn how to *summarize* it and *combine* it from multiple tables. This session covers two of the most powerful skills in SQL:

- **Aggregation** — collapsing many rows into a single summary (e.g., "How many orders did each customer place?")
- **Joins** — connecting two or more tables together to answer bigger questions (e.g., "Which customers placed orders, and what did they buy?")

---

## Introduction to Aggregation — Summarising Your Data

Imagine you run a small tea stall. At the end of the day, you don't want to look at every single bill — you want answers like *"How much did I earn today?"* or *"Which item sold the most?"* That is exactly what **aggregation** does in SQL — it takes a large set of rows and summarises them into meaningful numbers.

- **Official Definition:** Aggregation in SQL is the process of performing a calculation across a set of rows and returning a single summary value.
- **In Simple Words:** Instead of looking at every row one by one, aggregation squishes many rows into one answer — like adding up all your marks to get a total score.
- **Real-Life Example:** Think of a classroom attendance register. You could look at each day's entry, or you could just count the total days a student was present. That count is an aggregation.

The SQL functions used for aggregation are called **aggregate functions**. The most common ones are:

| Function | What It Does |
|----------|-------------|
| `COUNT()` | Counts the number of rows |
| `SUM()` | Adds up all the values |
| `AVG()` | Calculates the average (mean) |
| `MAX()` | Finds the highest value |
| `MIN()` | Finds the lowest value |

![Many detailed rows in a table collapse into a single summary number when you use aggregate functions like COUNT, SUM, and AVG](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-aggregation-many-rows-to-one.png)

---

## The COUNT Function — How Many Rows Are There?

**COUNT** is the simplest aggregate function. It answers one question: *"How many?"*

- **Official Definition:** `COUNT()` returns the number of rows that match a specified condition or the total rows in a result set.
- **In Simple Words:** It is like counting how many students are sitting in a classroom.
- **Real-Life Example:** A hospital database might use `COUNT` to find out how many patients were admitted in a month.

There are two important forms of COUNT:

- `COUNT(*)` — counts every row, including rows that have NULL (empty) values in any column.
- `COUNT(column_name)` — counts only the rows where that specific column has a value (ignores NULLs).

**Common Doubt:** "When should I use `COUNT(*)` vs `COUNT(column_name)`?"
- Use `COUNT(*)` when you want the total number of rows.
- Use `COUNT(column_name)` when you only want to count rows where that column is not empty.

```sql
-- Count the total number of rows in the orders table
SELECT COUNT(*) AS total_orders
FROM orders;

-- Count only orders that have a delivery date filled in
SELECT COUNT(delivery_date) AS delivered_orders
FROM orders;
```

**How the code works:**
- `SELECT COUNT(*) AS total_orders` — asks SQL to count all rows and label the result `total_orders`
- `FROM orders` — tells SQL which table to look at
- `COUNT(delivery_date)` — counts only rows where `delivery_date` is not NULL

---

## The SUM and AVG Functions — Totals and Averages

Once you know how to count, you naturally want to go further — *"What is the total amount spent?"* or *"What is the average score?"* This is where **SUM** and **AVG** come in.

- **SUM — Official Definition:** Returns the total sum of a numeric column.
- **SUM — In Simple Words:** It adds up all the numbers in a column, just like a calculator.
- **SUM — Real-Life Example:** A company uses SUM to add up all employee salaries and get the total monthly payroll.

- **AVG — Official Definition:** Returns the arithmetic mean (average) of a numeric column.
- **AVG — In Simple Words:** It finds the middle ground — divide the total by the number of entries.
- **AVG — Real-Life Example:** Your school report card uses average marks to show your overall performance.

```sql
-- Find the total revenue from all orders
SELECT SUM(order_amount) AS total_revenue
FROM orders;

-- Find the average order value
SELECT AVG(order_amount) AS average_order_value
FROM orders;

-- Find the most expensive and cheapest order
SELECT MAX(order_amount) AS highest_order, MIN(order_amount) AS lowest_order
FROM orders;
```

**How the code works:**
- `SUM(order_amount)` — adds up every value in the `order_amount` column
- `AVG(order_amount)` — divides the total of `order_amount` by the count of rows
- `MAX(order_amount)` — scans the column and picks the largest number
- `MIN(order_amount)` — scans the column and picks the smallest number
- `AS highest_order` — renames the output column so the result is easy to read

---

## GROUP BY — Breaking Down Summaries by Category

Running a single SUM or COUNT across the whole table gives you one answer. But what if you want the total per customer, or the count per city? That is where **GROUP BY** becomes essential.

- **Official Definition:** `GROUP BY` groups rows that have the same value in one or more columns, and then applies an aggregate function to each group separately.
- **In Simple Words:** Imagine sorting your bills into separate envelopes — one per month. Then you add up each envelope separately. GROUP BY is that sorting step.
- **Real-Life Example:** A supermarket's billing system uses GROUP BY to calculate total sales per product category — so they know how much was sold in "Dairy," how much in "Snacks," etc.

**The Golden Rule of GROUP BY:**
> Any column in your SELECT that is NOT inside an aggregate function MUST appear in the GROUP BY clause.

![GROUP BY splits rows into separate groups (for example by city or customer), then each aggregate runs inside its own group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-group-by-buckets.png)

**Common Mistake:** Students often write `SELECT customer_id, SUM(order_amount) FROM orders` and forget to add `GROUP BY customer_id`. SQL will throw an error because it doesn't know which `customer_id` to display for the many rows being grouped.

```sql
-- Find the total order amount for each customer
SELECT customer_id, SUM(order_amount) AS total_spent
FROM orders
GROUP BY customer_id;

-- Count how many orders each customer has placed
SELECT customer_id, COUNT(*) AS number_of_orders
FROM orders
GROUP BY customer_id;

-- Find the average order value per city
SELECT city, AVG(order_amount) AS avg_order_value
FROM orders
GROUP BY city
ORDER BY avg_order_value DESC;
```

**How the code works:**
- `GROUP BY customer_id` — tells SQL to create a separate group for each unique `customer_id`
- `SUM(order_amount)` — adds up order amounts within each group (not across the whole table)
- `COUNT(*)` — counts the number of rows in each group (i.e., number of orders per customer)
- `ORDER BY avg_order_value DESC` — sorts the final result from highest to lowest average

---

## HAVING — Filtering Groups After Aggregation

You already know how to filter rows using **WHERE**. But here's an important limitation: **WHERE cannot filter on the result of an aggregate function**. For that, SQL gives us **HAVING**.

- **Official Definition:** `HAVING` is a clause used to filter groups after the `GROUP BY` operation has been applied. It works on aggregated results.
- **In Simple Words:** WHERE is like checking people at the entrance to a party. HAVING is like checking groups *after* they have already formed inside — and asking a group to leave if they don't meet some condition.
- **Real-Life Example:** You've grouped students by class. Now you want to keep only the classes where the average mark is above 70. That filter on the group result is HAVING.

**The Key Difference — WHERE vs HAVING:**

| | WHERE | HAVING |
|---|---|---|
| **When it filters** | Before grouping | After grouping |
| **Works on** | Individual rows | Groups / aggregated values |
| **Can use aggregate functions?** | No | Yes |

![WHERE filters individual rows before grouping; HAVING filters whole groups after aggregates are computed](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-where-vs-having.png)

```sql
-- Find only customers who have placed more than 3 orders
SELECT customer_id, COUNT(*) AS number_of_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 3;

-- Find cities where the total revenue is above 50,000
SELECT city, SUM(order_amount) AS total_revenue
FROM orders
GROUP BY city
HAVING SUM(order_amount) > 50000;

-- Combine WHERE and HAVING: only look at 2024 orders, then filter groups
SELECT customer_id, SUM(order_amount) AS total_spent
FROM orders
WHERE YEAR(order_date) = 2024
GROUP BY customer_id
HAVING SUM(order_amount) > 10000;
```

**How the code works:**
- `HAVING COUNT(*) > 3` — after grouping by customer, this keeps only groups (customers) with more than 3 rows
- `HAVING SUM(order_amount) > 50000` — filters out city groups whose total revenue is 50,000 or below
- `WHERE YEAR(order_date) = 2024` — first filters individual rows to only 2024 data, then GROUP BY and HAVING work on that filtered set

**SQL Execution Order (Very Important to Understand):**
SQL does not execute in the order you write it. The actual order is:
1. `FROM` — identify the table
2. `WHERE` — filter individual rows
3. `GROUP BY` — group the filtered rows
4. `HAVING` — filter the groups
5. `SELECT` — pick columns and apply functions
6. `ORDER BY` — sort the final result
7. `LIMIT` — trim the output

![SQL runs clauses in a fixed order: FROM, then WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT — not necessarily in the order you write them in the editor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-sql-execution-order.png)

---

## Joining Tables — Connecting Information Across Tables

So far, we have been working with a single table. But in real databases, information is spread across multiple tables to avoid repetition. For example, a shopping app might have a `customers` table, an `orders` table, and a `products` table — each storing different pieces of information.

- **Official Definition:** A **JOIN** in SQL is an operation that combines rows from two or more tables based on a related column between them.
- **In Simple Words:** A JOIN is like using a reference number on an invoice to look up the customer's full details from a separate contacts book.
- **Real-Life Example:** Think of your Aadhaar card number. The government has one file with your name and address, and another file with your financial records. The Aadhaar number is the link that connects both files — that's exactly how a JOIN works.

**Why Do We Have Multiple Tables?**
Keeping all data in one table causes problems:
- **Redundancy:** If 100 orders are placed by one customer, do you need to write the customer's name and address 100 times?
- **Inconsistency:** If the customer moves to a new city, you'd have to update 100 rows instead of just one.
- Splitting data into tables and connecting them with keys is called **normalisation** — a fundamental database design principle.

The connecting column is called a **key**:
- **Primary Key:** A unique identifier in a table (e.g., `customer_id` in the customers table)
- **Foreign Key:** A column in another table that references a primary key (e.g., `customer_id` in the orders table)

![A JOIN uses matching key columns — a primary key in one table and a foreign key in the other — to link related rows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-joins-keys-bridge.png)

---

## INNER JOIN — Find Only the Matching Records

**INNER JOIN** is the most commonly used type of join. It returns only the rows where there is a match in **both** tables.

- **Official Definition:** `INNER JOIN` returns rows that have matching values in both the left table and the right table based on the specified condition.
- **In Simple Words:** Think of two lists of names. INNER JOIN gives you only the names that appear on BOTH lists.
- **Real-Life Example:** You have a list of registered students and a list of students who submitted an assignment. INNER JOIN gives you only the students who are registered AND submitted — everyone else is excluded.

```sql
-- Get each order along with the customer's name and city
SELECT 
    orders.order_id,          -- order ID from the orders table
    orders.order_amount,       -- order amount from the orders table
    customers.customer_name,   -- customer name from the customers table
    customers.city             -- city from the customers table
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id;  -- match rows where customer_id is the same in both tables
```

**How the code works:**
- `FROM orders` — we start with the orders table as the "left" table
- `INNER JOIN customers` — we bring in the customers table as the "right" table
- `ON orders.customer_id = customers.customer_id` — this is the condition: only combine rows where the customer_id matches in both tables
- `orders.order_id` — because both tables are in the query, we prefix the column name with the table name to avoid confusion
- Result: only orders that have a matching customer record will appear; orphan orders with no customer info are excluded

**Using Table Aliases to Keep Code Clean:**
Writing `orders.column_name` every time is verbose. We can use **aliases** to shorten table names.

```sql
-- Same query using aliases for cleaner code
SELECT 
    o.order_id,           -- 'o' is the alias for orders
    o.order_amount,
    c.customer_name,      -- 'c' is the alias for customers
    c.city
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id;  -- join condition using aliases
```

**How the code works:**
- `FROM orders AS o` — gives the `orders` table a short nickname `o`
- `INNER JOIN customers AS c` — gives the `customers` table a short nickname `c`
- All column references now use the short alias — much easier to read in complex queries

---

## LEFT JOIN — Keep All Records from the Left Table

INNER JOIN drops records that don't have a match. But sometimes you *want* to keep all records from one side — even if there is no match on the other side. For this, we use **LEFT JOIN**.

- **Official Definition:** `LEFT JOIN` returns all rows from the left table, and the matching rows from the right table. If there is no match, the result will contain NULL for the right table's columns.
- **In Simple Words:** Imagine a teacher's roll call list (left table) and an attendance sheet (right table). LEFT JOIN gives you every student on the roll call, and marks "Absent" (NULL) for those who didn't sign the attendance sheet.
- **Real-Life Example:** An e-commerce company wants a list of all customers and whether or not they have placed any orders. Customers with no orders will show up with NULL in the order columns — LEFT JOIN makes this possible.

```sql
-- List all customers, and show their orders if they have any
-- Customers with no orders will still appear, with NULL in order columns
SELECT 
    c.customer_id,            -- customer ID from customers table
    c.customer_name,           -- customer name
    o.order_id,               -- order ID — will be NULL if no orders
    o.order_amount             -- order amount — will be NULL if no orders
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id;  -- match on customer ID
```

**How the code works:**
- `FROM customers AS c` — customers is the "left" table; ALL rows from here will appear in the result
- `LEFT JOIN orders AS o` — orders is the "right" table; only matching rows are brought in
- `ON c.customer_id = o.customer_id` — the join condition, same as INNER JOIN
- For a customer who has never ordered, `o.order_id` and `o.order_amount` will show as **NULL**

**Finding Customers Who Have NEVER Placed an Order (Using LEFT JOIN + IS NULL):**

```sql
-- Find all customers who have no orders at all
SELECT 
    c.customer_id,       -- customer's ID
    c.customer_name      -- customer's name
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id   -- attempt to match with orders
WHERE o.order_id IS NULL;              -- keep only rows where no match was found (no order)
```

**How the code works:**
- After the LEFT JOIN, customers with no matching orders have `o.order_id = NULL`
- `WHERE o.order_id IS NULL` — filters the result to keep only those non-matching rows
- This is a very common interview pattern — finding "records in one table that are absent from another"

![INNER JOIN keeps only rows that match in both tables; LEFT JOIN keeps every row from the left table and uses NULL when there is no match on the right](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-inner-vs-left-join.png)

---

## INNER JOIN vs LEFT JOIN — Key Comparison

| | INNER JOIN | LEFT JOIN |
|---|---|---|
| **Returns** | Only matching rows from both tables | All rows from left table + matching from right |
| **Non-matching rows** | Excluded | Kept (with NULLs for right table columns) |
| **Use when** | You only care about records with a match | You want all left records, regardless of match |
| **Example** | Orders with valid customers | All customers, whether or not they ordered |

---

## Multi-Table Queries — Joining More Than Two Tables

Real-world databases often require joining three or more tables. You simply chain multiple JOIN clauses one after the other.

- **Official Definition:** A multi-table query uses multiple JOIN clauses to combine data from three or more tables in a single SELECT statement.
- **In Simple Words:** It's like a chain — you connect Table A to Table B, and then connect Table B to Table C, forming one big connected result.
- **Real-Life Example:** An online store needs to show a customer's name, the products they ordered, and the category of each product — linking the `customers`, `orders`, `order_items`, and `products` tables.

```sql
-- Get customer name, order date, and product name for all orders
SELECT 
    c.customer_name,          -- customer name from customers table
    o.order_date,             -- order date from orders table
    p.product_name,           -- product name from products table
    oi.quantity               -- quantity from order_items table
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id          -- link customers to orders
INNER JOIN order_items AS oi
    ON o.order_id = oi.order_id               -- link orders to order_items
INNER JOIN products AS p
    ON oi.product_id = p.product_id;          -- link order_items to products
```

**How the code works:**
- We start with `customers`, then join `orders` on the shared `customer_id`
- We then join `order_items` to `orders` using the shared `order_id`
- Finally we join `products` to `order_items` using the shared `product_id`
- Each join adds more columns to the result, creating one combined view of the data

**Combining Aggregation with Joins:**

```sql
-- Find total amount spent by each customer, showing customer name
SELECT 
    c.customer_name,                    -- name from customers table
    COUNT(o.order_id) AS total_orders,  -- count of orders per customer
    SUM(o.order_amount) AS total_spent  -- sum of all order amounts per customer
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id    -- match customers with their orders
GROUP BY c.customer_id, c.customer_name -- group by customer
ORDER BY total_spent DESC;              -- show highest spenders first
```

**How the code works:**
- `LEFT JOIN` ensures all customers appear even if they have no orders
- `GROUP BY c.customer_id, c.customer_name` — groups rows by each unique customer
- `COUNT(o.order_id)` — counts the number of orders per customer (NULLs not counted)
- `SUM(o.order_amount)` — sums the order amounts for each customer
- `ORDER BY total_spent DESC` — ranks customers from highest to lowest total spend

---

## Pandas vs SQL — Mapping groupby and merge to SQL

If you have used **pandas** in Python, you already understand the logic behind GROUP BY and JOIN. This section maps familiar pandas operations directly to their SQL equivalents so you can switch between the two with confidence.

**GROUP BY in SQL ↔ groupby() in Pandas**

| Goal | Pandas | SQL |
|------|--------|-----|
| Count rows per group | `df.groupby('city').size()` | `SELECT city, COUNT(*) FROM ... GROUP BY city` |
| Sum values per group | `df.groupby('customer_id')['amount'].sum()` | `SELECT customer_id, SUM(amount) FROM ... GROUP BY customer_id` |
| Average per group | `df.groupby('dept')['salary'].mean()` | `SELECT dept, AVG(salary) FROM ... GROUP BY dept` |
| Filter groups | `df.groupby('city').filter(lambda x: x['amount'].sum() > 5000)` | `... GROUP BY city HAVING SUM(amount) > 5000` |

**JOIN in SQL ↔ merge() in Pandas**

| Goal | Pandas | SQL |
|------|--------|-----|
| Inner join | `pd.merge(df1, df2, on='id', how='inner')` | `FROM df1 INNER JOIN df2 ON df1.id = df2.id` |
| Left join | `pd.merge(df1, df2, on='id', how='left')` | `FROM df1 LEFT JOIN df2 ON df1.id = df2.id` |

**Key Insight:** Pandas `merge()` and SQL `JOIN` work on the exact same logic — find a matching key column between two DataFrames/tables and combine the rows. The difference is only syntax.

**Side-by-Side Example — Find total spend per customer with their name:**

```python
# Pandas version
import pandas as pd   # import the pandas library

# merge customers and orders on customer_id (inner join by default)
merged = pd.merge(customers_df, orders_df, on='customer_id', how='left')

# group by customer and calculate total spent
result = merged.groupby(['customer_id', 'customer_name'])['order_amount'].sum().reset_index()

# sort by total amount descending
result = result.sort_values('order_amount', ascending=False)

print(result)   # display the result
```

```sql
-- SQL version (equivalent logic)
SELECT 
    c.customer_id,                         -- customer identifier
    c.customer_name,                       -- customer's name
    SUM(o.order_amount) AS total_spent     -- total amount spent by each customer
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id       -- link customers and orders
GROUP BY c.customer_id, c.customer_name   -- group by customer
ORDER BY total_spent DESC;                 -- sort highest first
```

**How both work the same way:**
- Both start with a left join / merge to include all customers
- Both then group by customer and sum the order amounts
- Both sort the result in descending order
- The SQL version runs directly inside the database — no need to load data into Python first

---

## Putting It All Together — A Complete Real-World Query

Let's build a final query step-by-step that uses joins, aggregation, GROUP BY, and HAVING together.

**Business Question:** *"Which customers from Mumbai have spent more than ₹20,000 in total? Show their name, number of orders, and total spend, sorted by highest spenders first."*

```sql
-- Step 1: join customers and orders
-- Step 2: filter to only Mumbai customers
-- Step 3: group by customer and calculate totals
-- Step 4: keep only customers who spent more than 20000
-- Step 5: sort by total spend descending

SELECT 
    c.customer_name,                      -- customer's full name
    COUNT(o.order_id) AS total_orders,    -- how many orders they placed
    SUM(o.order_amount) AS total_spent    -- total money they spent
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id      -- link each order to the right customer
WHERE c.city = 'Mumbai'                   -- only include Mumbai customers (filters rows before grouping)
GROUP BY c.customer_id, c.customer_name  -- one group per customer
HAVING SUM(o.order_amount) > 20000       -- only keep groups where total spend exceeds 20000
ORDER BY total_spent DESC;               -- highest spender at the top
```

**How the code works:**
- `INNER JOIN` connects each order to its corresponding customer
- `WHERE c.city = 'Mumbai'` — filters individual rows first, keeping only Mumbai customers
- `GROUP BY c.customer_id, c.customer_name` — creates one group per customer
- `COUNT(o.order_id)` — counts how many orders each customer placed
- `SUM(o.order_amount)` — adds up all spending per customer
- `HAVING SUM(o.order_amount) > 20000` — drops groups (customers) who spent ₹20,000 or less
- `ORDER BY total_spent DESC` — puts the biggest spender at the top of the list

---

## Key Takeaways

- **Aggregate functions** like `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN` collapse many rows into a single summary value — essential for reporting and analysis.
- **GROUP BY** lets you apply aggregate functions per category (e.g., per customer, per city) instead of across the whole table. Every non-aggregated column in SELECT must be in GROUP BY.
- **HAVING** filters groups *after* aggregation — it is to GROUP BY what WHERE is to individual rows. They can be used together in the same query.
- **INNER JOIN** combines rows from two tables where a match exists on both sides; **LEFT JOIN** keeps all rows from the left table and fills NULLs for unmatched right-table columns.
- SQL's `GROUP BY` + aggregate functions map directly to pandas `groupby()`, and SQL `JOIN` maps directly to pandas `merge()` — the logic is identical, only the syntax differs.

In the next sessions, we will build on joins and aggregation to write subqueries (queries inside queries), explore window functions for running totals and rankings, and connect SQL queries to Python for automated data pipelines.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Description |
|---|---|
| `COUNT(*)` | Count all rows including NULLs |
| `COUNT(column)` | Count rows where column is not NULL |
| `SUM(column)` | Add up all values in a numeric column |
| `AVG(column)` | Calculate the mean of a numeric column |
| `MAX(column)` | Find the highest value in a column |
| `MIN(column)` | Find the lowest value in a column |
| `GROUP BY` | Group rows by one or more columns before aggregation |
| `HAVING` | Filter groups based on an aggregated condition |
| `INNER JOIN` | Return only rows that have a match in both tables |
| `LEFT JOIN` | Return all rows from the left table; NULLs for unmatched right rows |
| `ON` | Specifies the join condition (which columns to match) |
| `AS` | Creates an alias — a short nickname for a table or column |
| **Primary Key** | A unique identifier column in a table (e.g., `customer_id`) |
| **Foreign Key** | A column that references a primary key in another table |
| **NULL** | Represents a missing or unknown value in SQL |
| **Normalisation** | Designing a database with multiple related tables to reduce redundancy |
| `IS NULL` | Condition to check if a column has no value |
| `pd.merge()` | Pandas equivalent of SQL JOIN |
| `df.groupby()` | Pandas equivalent of SQL GROUP BY |
| SQL Execution Order | FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT |
