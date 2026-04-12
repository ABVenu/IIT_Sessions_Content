# Pre-Read: SQL - Thinking in Tables

## What You’ll Learn
In this pre-read, you’ll discover:
- How to think in terms of **tables instead of files**  
- The difference between **relational and non-relational databases**  
- Why **primary keys** are essential  
- What a **database schema** represents  

![Session 16](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/da6fed21-cd3d-44ce-8501-9da40aaea40d/aFRGMTlAOvZ03ktH.png)

---

## Introduction: From Files to Tables
Imagine storing student data in separate Excel files:
- One file for names  
- One file for marks  
- One file for attendance  

Soon, it becomes messy and inconsistent.

Now imagine storing everything in structured tables that connect logically.

That structured system is a **relational database**.

---

## Why Thinking in Tables Matters
Databases power:
- Banking systems  
- E-commerce websites  
- Social media platforms  
- AI data pipelines  

Understanding tables helps you:
1. **Organize data logically**  
2. **Avoid duplication**  
3. **Maintain consistency**  

Before writing SQL queries, you must understand the structure.

---

## From Known to New: Spreadsheets → Databases
### What You Already Know
You’ve worked with:
- Rows  
- Columns  
- Tables in Pandas  

### The Database Perspective
A relational database stores:
- Data in tables  
- Tables connected through relationships  
- Structured, consistent records  

But unlike Excel, relationships are enforced formally.

---

## Core Database Concepts
### 1. Tables and Rows
A **table** stores related information.

- Columns define categories (like name, age, salary)  
- Rows represent individual records  

Each row is one complete entry.

---

### 2. Primary Keys
A **primary key** uniquely identifies each row.

- No duplicates allowed  
- Cannot be null  
- Acts like a unique ID  

Without a primary key, records can become ambiguous.

---

### 3. Relational vs Non-Relational Databases
**Relational databases:**
- Use structured tables  
- Enforce schemas  
- Ideal for structured, consistent data  

**Non-relational databases:**
- More flexible structure  
- Often store data like JSON  
- Better for rapidly changing or unstructured data  

Both have uses—but relational databases rely on table thinking.

---

### 4. Database Schema Basics
A **schema** is the blueprint of the database.

It defines:
- Tables  
- Columns  
- Data types  
- Relationships  

Think of it as the architectural plan before building.

---

## Putting It All Together
A relational system works like this:
1. Design a schema  
2. Create tables  
3. Assign primary keys  
4. Link tables logically  

Once the structure is strong, querying becomes powerful.

---

## Quick Practice (Think Before the Lecture)
1. Why is a primary key necessary?  
2. What problems arise if data is duplicated across tables?  
3. When might a non-relational database be better?

---

### Final Thought
SQL starts with structure.  
If you think clearly in tables, queries become intuitive.