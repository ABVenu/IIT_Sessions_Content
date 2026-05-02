# Assignment — Subjective: SQL Aggregation and Joining Tables

---

## Question 1 — FoodRush Operations Analytics

**Background:**

FoodRush is a growing food delivery startup operating across multiple Indian cities. Their engineering team has set up a relational database to track customers, restaurants, and orders. As a newly onboarded data analyst, your first task is to run a series of analytical SQL queries to help the operations team understand their business better.

The database schema is as follows:

| Table | Columns |
|---|---|
| `customers` | `customer_id` (PK), `customer_name`, `city` |
| `restaurants` | `restaurant_id` (PK), `restaurant_name`, `city`, `cuisine` |
| `orders` | `order_id` (PK), `customer_id` (FK), `restaurant_id` (FK), `order_amount`, `order_date`, `status` |

The `status` column in `orders` can be one of: `'delivered'`, `'cancelled'`, or `'pending'`.

**Setup — Use the following Python code to create the database and load sample data:**

```python
import sqlite3

conn = sqlite3.connect('foodrush.db')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT,
    city          TEXT
);

CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id   INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    city            TEXT,
    cuisine         TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id      INTEGER PRIMARY KEY,
    customer_id   INTEGER,
    restaurant_id INTEGER,
    order_amount  REAL,
    order_date    TEXT,
    status        TEXT,
    FOREIGN KEY (customer_id)   REFERENCES customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

INSERT OR IGNORE INTO customers VALUES
(1, 'Arjun Sharma',  'Delhi'),
(2, 'Priya Mehta',   'Mumbai'),
(3, 'Kiran Rao',     'Delhi'),
(4, 'Sneha Patel',   'Bangalore'),
(5, 'Rahul Nair',    'Mumbai'),
(6, 'Aisha Khan',    'Delhi');

INSERT OR IGNORE INTO restaurants VALUES
(1, 'Spice Garden', 'Delhi',     'Indian'),
(2, 'Burger Hub',   'Delhi',     'Fast Food'),
(3, 'Pizza Palace', 'Mumbai',    'Italian'),
(4, 'Dosa Corner',  'Bangalore', 'South Indian'),
(5, 'Wok Express',  'Delhi',     'Chinese');

INSERT OR IGNORE INTO orders VALUES
(1,  1, 1, 450.0, '2024-01-10', 'delivered'),
(2,  1, 2, 320.0, '2024-01-15', 'delivered'),
(3,  1, 5, 580.0, '2024-02-01', 'delivered'),
(4,  2, 3, 900.0, '2024-01-20', 'delivered'),
(5,  2, 3, 750.0, '2024-02-05', 'cancelled'),
(6,  3, 1, 400.0, '2024-01-25', 'delivered'),
(7,  3, 2, 280.0, '2024-02-10', 'delivered'),
(8,  3, 1, 500.0, '2024-02-15', 'delivered'),
(9,  4, 4, 350.0, '2024-01-30', 'delivered'),
(10, 5, 3, 620.0, '2024-02-20', 'pending'),
(11, 1, 1, 410.0, '2024-03-01', 'delivered'),
(12, 3, 5, 680.0, '2024-03-05', 'delivered');
""")

conn.commit()
print("Database setup complete.")
```

---

**Your Tasks:**

For each task below, write a SQL query, execute it using `cursor.execute()`, and print the results in a loop. Print a short heading before each output.

---

**Task 1 — Restaurant Revenue Report**

Write a SQL query to find, for each restaurant, the **total revenue** and the **number of delivered orders**. Only include restaurants that have **more than 2 delivered orders**. Sort by total revenue in descending order.

Expected output columns: `restaurant_name`, `delivered_orders`, `total_revenue`

---

**Task 2 — Full Customer Order Summary**

Write a SQL query to list **all customers** with their total number of orders and total spend. Customers who have **never placed an order** should still appear (showing 0 orders and 0.0 spend). Sort by total spend in descending order.

Expected output columns: `customer_name`, `city`, `total_orders`, `total_spent`

*Hint: Use a join type that keeps customers even if they have no matching orders.*

---

**Task 3 — Delhi High-Spenders**

Write a SQL query to find customers from **Delhi** who have placed **more than 1 order** and have a **total spend above ₹1,000**. Sort by total spend in descending order.

Expected output columns: `customer_name`, `total_orders`, `total_spent`

---

**Task 4 — Customer–Restaurant Spend Breakdown**

Write a SQL query joining all three tables to show, for each customer–restaurant pair, how many orders were placed and how much was spent in total. Include only pairs where the **total spend exceeds ₹500**. Sort by customer name ascending, then by total spend descending.

Expected output columns: `customer_name`, `restaurant_name`, `orders_at_restaurant`, `total_spent_at_restaurant`

---
**Submission Instructions:**

- Code all four tasks in **VS Code** in a single `.py` file (e.g., `foodrush_analytics.py`).
- Run the file and verify that all four query outputs appear correctly in the terminal.
- Once verified, **submit the code in the code editor / answer box** in the LMS.


---
**Answer Explanation (Ideal Solution):**

```python
import sqlite3

conn = sqlite3.connect('foodrush.db')
cursor = conn.cursor()

# Task 1: Restaurant Revenue Report
print("\n--- Task 1: Restaurant Revenue Report ---")
query1 = """
SELECT
    r.restaurant_name,
    COUNT(o.order_id)      AS delivered_orders,
    SUM(o.order_amount)    AS total_revenue
FROM restaurants AS r
INNER JOIN orders AS o ON r.restaurant_id = o.restaurant_id
WHERE o.status = 'delivered'
GROUP BY r.restaurant_id, r.restaurant_name
HAVING COUNT(o.order_id) > 2
ORDER BY total_revenue DESC;
"""
for row in cursor.execute(query1):
    print(row)

# Task 2: Full Customer Order Summary
print("\n--- Task 2: Full Customer Order Summary ---")
query2 = """
SELECT
    c.customer_name,
    c.city,
    COUNT(o.order_id)               AS total_orders,
    COALESCE(SUM(o.order_amount), 0) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.city
ORDER BY total_spent DESC;
"""
for row in cursor.execute(query2):
    print(row)

# Task 3: Delhi High-Spenders
print("\n--- Task 3: Delhi High-Spenders ---")
query3 = """
SELECT
    c.customer_name,
    COUNT(o.order_id)   AS total_orders,
    SUM(o.order_amount) AS total_spent
FROM customers AS c
INNER JOIN orders AS o ON c.customer_id = o.customer_id
WHERE c.city = 'Delhi'
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1 AND SUM(o.order_amount) > 1000
ORDER BY total_spent DESC;
"""
for row in cursor.execute(query3):
    print(row)

# Task 4: Customer–Restaurant Spend Breakdown
print("\n--- Task 4: Customer–Restaurant Spend Breakdown ---")
query4 = """
SELECT
    c.customer_name,
    r.restaurant_name,
    COUNT(o.order_id)   AS orders_at_restaurant,
    SUM(o.order_amount) AS total_spent_at_restaurant
FROM customers AS c
INNER JOIN orders AS o ON c.customer_id = o.customer_id
INNER JOIN restaurants AS r ON o.restaurant_id = r.restaurant_id
GROUP BY c.customer_id, c.customer_name, r.restaurant_id, r.restaurant_name
HAVING SUM(o.order_amount) > 500
ORDER BY c.customer_name ASC, total_spent_at_restaurant DESC;
"""
for row in cursor.execute(query4):
    print(row)

conn.close()
```

**Alternative approaches:**
- In Task 2, `IFNULL(SUM(o.order_amount), 0)` can be used instead of `COALESCE(...)` in SQLite.
- In Task 1, a `LEFT JOIN` filtered with `WHERE status = 'delivered'` works the same as `INNER JOIN` with the WHERE clause, since the filter effectively turns the LEFT into an INNER.
- In Task 4, adding `c.city` and `r.cuisine` to the SELECT and GROUP BY is a valid extension to make the output richer.

---


