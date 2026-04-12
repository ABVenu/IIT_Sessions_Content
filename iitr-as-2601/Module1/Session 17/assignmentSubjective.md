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

### **Question: AI Data Retrieval and Ranking Query Design**

**Task:**
Assume you are working with a relational database containing the following table:

**students**

| id | name | score | passed | class |
| -- | ---- | ----- | ------ | ----- |

Write SQL queries that accomplish the following:

1. Retrieve only the `name` and `score` columns.
2. Retrieve students who scored above 80.
3. Retrieve students who scored above 80 and passed.
4. Return a list of distinct classes.
5. Retrieve the top 5 highest-scoring students.
6. Retrieve students sorted first by `class` (ascending) and then by `score` (descending).
7. Use an alias to rename `score` as `final_score`.
8. Write one combined query that:

   * Selects `name` and `score`
   * Filters students who scored above 75
   * Sorts by score in descending order
   * Returns only the top 3 results

**Requirements:**

* Follow correct SQL clause order
* Use `SELECT`, `WHERE`, `DISTINCT`, `ORDER BY`, `LIMIT`, and aliases correctly
* Maintain proper SQL formatting
* Ensure logical correctness in conditions