## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-sql-assignment`).

3. Write **separate Python files** for each question inside this folder.

4. For each program:

   * Run the code in the **terminal**
   * Verify the **output**

5. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

6. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repo).

---

### **Question: AI Feature Engineering with SQL Joins**

**Task:**
You are building features for a machine learning model using relational data.

You are given three conceptual tables:

**users**

* user_id (primary key)
* name
* signup_date

**orders**

* order_id (primary key)
* user_id (foreign key)
* amount

**activity**

* user_id (foreign key)
* login_count

Write SQL queries that accomplish the following:

1. Retrieve each user’s name and total order amount (using `INNER JOIN` and aggregation).
2. Retrieve all users and their login counts, including users with no recorded activity (using `LEFT JOIN`).
3. Identify users who have never placed an order.
4. Combine all three tables to produce:

   * user_id
   * total order amount
   * login count
5. Explain briefly why `LEFT JOIN` is often preferred in AI feature preparation pipelines.

**Requirements:**

* Use correct JOIN syntax
* Include proper `ON` conditions
* Use aggregation where necessary
* Avoid accidental Cartesian products
* Write clean, properly formatted SQL

**Example format (illustrative only):**

```sql
SELECT u.user_id, SUM(o.amount) AS total_spent
FROM users u
INNER JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id;
```