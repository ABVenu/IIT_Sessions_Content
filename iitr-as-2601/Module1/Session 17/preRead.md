# Pre-Read: SQL - Core Querying

## What You’ll Learn
In this pre-read, you’ll discover:
- How **SELECT** retrieves data from tables  
- How **WHERE** filters records  
- Why **DISTINCT** removes duplicates  
- How **ORDER BY**, **LIMIT**, and **aliases** refine results  

---

## Introduction: Asking Questions from a Database
Imagine you manage a bookstore database with 50,000 books.

You don’t want all the data.  
You want answers like:
- Show books under ₹500  
- List unique authors  
- Display the top 10 highest-rated books  

SQL is the language you use to ask these questions.

---

## Why Core Querying Matters
Databases store massive amounts of information.

Core querying helps you:
1. **Extract exactly what you need**  
2. **Filter irrelevant records**  
3. **Organize results clearly**  

Without querying, data just sits there unused.

---

## From Known to New: Filtering in Pandas → SQL Queries
### What You Already Know
In Pandas, you:
- Select columns  
- Apply conditions  
- Sort values  

### The SQL Way
In SQL, you:
- Use **SELECT** to choose columns  
- Use **WHERE** to filter rows  
- Use **ORDER BY** to sort  

The mental model is similar—but the syntax is different.

---

## Core SQL Query Concepts
### 1. SELECT and WHERE
- **SELECT** specifies which columns to retrieve  
- **WHERE** applies conditions to filter rows  

Together, they answer targeted questions.

---

### 2. DISTINCT
Sometimes tables contain repeated values.

**DISTINCT** ensures:
- Only unique values are returned  
- Duplicate entries are removed  

Useful when analyzing categories or groups.

---

### 3. ORDER BY
Sorting helps reveal patterns.

- Ascending (smallest to largest)  
- Descending (largest to smallest)  

Sorting makes reports readable and meaningful.

---

### 4. LIMIT and Aliases
**LIMIT** restricts the number of rows returned.

- Useful for previews  
- Improves performance  

**Aliases** rename columns in results.

- Makes output clearer  
- Improves readability in reports  

---

## Putting It All Together
A typical query might:
1. Select specific columns  
2. Filter rows with conditions  
3. Remove duplicates  
4. Sort results  
5. Limit output to top entries  

This transforms raw tables into useful answers.

---

## Quick Practice (Think Before the Lecture)
1. Why is filtering essential in large databases?  
2. When would DISTINCT be important?  
3. Why might you limit results instead of fetching everything?

---

### Final Thought
SQL querying is about asking precise questions.  
Once you master the basics, data starts responding clearly.