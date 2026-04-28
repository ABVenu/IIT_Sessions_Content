# Assignment – Subjective Question
## Session 10: SQL – Querying Data with SELECT and WHERE

---

### Q1 (Practical Task | Medium)

**The TalentBridge Employee Intelligence Report**

Arjun has just joined as a junior data analyst at **TalentBridge**, a mid-sized HR consulting firm. On his very first week, his manager drops a task on his desk: *"Set up a small employee database, run a few queries, and send me the results — I need them before the team meeting this afternoon."*

Using the `employees` table structure from today's lecture, Arjun must build the database from scratch and write a series of SQL queries to answer real business questions.

---

**Your Task**

Complete all the steps below in a single `.sql` file, in order:

**Step 1 — Build the Database**

Create the `employees` table with the following columns and insert all 10 records exactly as provided in the lecture:

| Column | Data Type |
|---|---|
| EmployeeID | INT (Primary Key) |
| Name | VARCHAR(50) |
| Department | VARCHAR(30) |
| Salary | INT |
| City | VARCHAR(30) |
| JoiningYear | INT |

*(Use the exact CREATE TABLE and INSERT INTO statements from the lecture.)*

---

**Step 2 — Answer the Business Questions**

Write one SQL query for each question below. Add a comment above each query indicating which question number it answers.

**Query 1 — High Earners List:**
The finance team needs a list of all employees earning **strictly above ₹60,000**. Show their **Name, Department, and Salary**, sorted from the **highest salary to the lowest**.

**Query 2 — Department Directory:**
HR wants to know **which unique departments** exist in the company — each department name listed exactly once, with no duplicates.

**Query 3 — Delhi & Mumbai Pre-2021 Joiners:**
The company is running a 5-year loyalty recognition programme. Find all employees who are based in **Delhi or Mumbai** AND who joined **before 2021**. Show their **Name, City, and JoiningYear**.

**Query 4 — Top 3 Earners:**
The CEO wants to see the **top 3 highest-paid employees** across all departments. Show their **Name, Department, and Salary**.

**Query 5 — Name Pattern Search:**
The admin team is looking for employees whose name **starts with the letter 'R'**. Show their **Name and Department**.

---

**Submission Instructions:**
- Open **MySQL Workbench** (or DBeaver / any SQL tool you have set up).
- Write all SQL statements — the CREATE TABLE, all 10 INSERTs, and all 5 queries — in a **single `.sql` file**, one after another.
- Run the entire file and verify that each query returns the expected result.
- Copy-paste all your SQL query into the **answer/code box** below and submit.
