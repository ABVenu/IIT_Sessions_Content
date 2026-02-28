# Pre-Read: SQL - Joining Data

## What You’ll Learn
In this pre-read, you’ll discover:
- Why data is often split across **multiple tables**  
- How **INNER JOIN** and **LEFT JOIN** work  
- Why JOINs are one of the most powerful tools in SQL  
- How SQL JOINs compare to **Pandas merge()**  

---

## Introduction: Why Data Lives in Separate Tables
Imagine a school database.

You might have:
- A **Students** table (student_id, name, class)  
- A **Marks** table (student_id, subject, score)  

Why not store everything in one big table?

Because separating data:
- Reduces duplication  
- Improves organization  
- Maintains consistency  

To combine them when needed, we use a **JOIN**.

---

## Why JOINs Matter
In real systems:
- Customer info lives in one table  
- Orders in another  
- Payments in a third  

JOINs allow you to:
1. **Combine related data logically**  
2. **Avoid storing duplicate information**  
3. **Ask richer, cross-table questions**  

Without JOINs, relational databases lose their power.

---

## From Known to New: Pandas merge → SQL JOIN
### What You Already Know
In Pandas, you use:
- `merge()`  
- A common key column  

This connects two DataFrames.

### The SQL Way
In SQL, a **JOIN** connects tables using a shared column (often a primary key).

Same idea.  
Different syntax.  
Stronger enforcement of structure.

---

## Core JOIN Concepts
### 1. INNER JOIN
Returns only rows where matches exist in both tables.

- If no match → row is excluded  
- Useful when only complete relationships matter  

*Think: “Show only records that match.”*

---

### 2. LEFT JOIN
Returns:
- All rows from the left table  
- Matching rows from the right table  
- NULL where no match exists  

*Think: “Keep everything on the left, fill in what matches.”*

---

### 3. The Power of the JOIN
JOINs allow you to:
- Combine data without duplication  
- Build meaningful reports  
- Connect complex systems logically  

Most real-world SQL queries involve JOINs.

---

### 4. SQL Mental Model vs Pandas merge
Both:
- Combine data using common keys  
- Align rows based on relationships  

Difference:
- SQL works inside a structured database  
- Pandas works on in-memory DataFrames  

SQL enforces relationships more strictly.

---

## Putting It All Together
A common workflow:
1. Identify related tables  
2. Find the shared key  
3. Choose the correct join type  
4. Combine and filter results  

This is how databases answer complex questions.

---

## Quick Practice (Think Before the Lecture)
1. Why is storing everything in one table inefficient?  
2. When would a LEFT JOIN be better than an INNER JOIN?  
3. How is a primary key useful in joining tables?

---

### Final Thought
JOINs are where relational databases shine.  
Once you understand them, multi-table data becomes powerful and intuitive.