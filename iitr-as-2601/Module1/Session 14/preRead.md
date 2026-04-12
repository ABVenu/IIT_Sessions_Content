# Pre-Read: Pandas — Selection & Filtering

## What You’ll Learn
In this pre-read, you’ll discover:
- How to **select specific columns** from a DataFrame  
- How to use **row indexing** to access particular records  
- How **Boolean filtering** helps answer specific questions  
- How to **sort DataFrames** to reveal patterns  

---

## Introduction: Asking Questions from Data
Imagine opening a large Excel sheet with 50,000 rows.

You don’t read everything.

You ask:
- Show only students who scored above 90  
- Sort products by highest price  
- Display only names and email columns  

That process of asking targeted questions is called **selection and filtering**.

---

## Why Selection & Filtering Matter
Raw data is rarely useful as-is.

You need to:
1. **Focus on relevant information**  
2. **Extract specific insights**  
3. **Remove noise from large datasets**  

Selection and filtering are how you turn data into answers.

---

## From Known to New: Full Table → Targeted View
### What You Already Know
You’ve learned:
- DataFrames store rows and columns  
- CSV files load into structured tables  

But viewing everything at once can be overwhelming.

### The Pandas Way
Instead of scanning manually, you:
- Select only needed columns  
- Filter rows using conditions  
- Sort data to see patterns clearly  

This makes analysis intentional.

---

## Core Concepts of Selection & Filtering
### 1. Selecting Columns
You can extract:
- A single column  
- Multiple columns  
- Subsets of the table  

This is useful when only certain variables matter.

---

### 2. Row Indexing
Every row has an **index**.

Row indexing lets you:
- Access specific rows  
- Slice ranges of rows  
- Select based on position or label  

This is similar to list slicing but applied to tables.

---

### 3. Boolean Filtering
Boolean filtering uses conditions that return **True or False**.

For example:
- Salary > 50000  
- Age < 30  
- Score == 100  

Only rows where the condition is true are returned.

This is how you answer data-driven questions.

---

### 4. Sorting DataFrames
Sorting rearranges rows based on column values.

You can:
- Sort ascending or descending  
- Sort by one column or multiple columns  

Sorting reveals trends and extremes quickly.

---

## Putting It All Together
A typical analysis flow:
1. Load a dataset  
2. Select relevant columns  
3. Filter rows based on conditions  
4. Sort results to understand patterns  

This transforms raw tables into meaningful insights.

---

## Quick Practice (Think Before the Lecture)
1. Why is selecting fewer columns often better than viewing all?  
2. What real-life question could Boolean filtering answer?  
3. How can sorting help identify top or bottom performers?

---

### Final Thought
Selection and filtering turn Pandas into a **question-answering tool**.  
Once you master them, data starts responding to your curiosity.
