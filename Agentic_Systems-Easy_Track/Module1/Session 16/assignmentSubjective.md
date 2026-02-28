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

### **Question: Designing a Relational Schema for an AI Application**

**Task:**
Design a relational database schema for an AI-powered e-commerce analytics system.

Your system must include at least the following entities:

* Users
* Orders
* Products

You must:

1. Define each table clearly.
2. Specify:

   * Table name
   * Column names
   * Data types
   * Primary key
3. Define relationships between tables (including foreign keys).
4. Explain why your chosen primary keys are appropriate.
5. Write at least two example SQL queries:

   * One that joins two tables
   * One that aggregates data (e.g., total spending per user)

**Requirements:**

* Follow relational design principles
* Ensure primary keys are unique and non-null
* Clearly explain relationships
* Use proper SQL syntax in your example queries
* Keep the design normalized (avoid unnecessary duplication)

**Example Query (format example only):**

```sql
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id;
```