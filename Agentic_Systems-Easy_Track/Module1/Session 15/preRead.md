# Pre-Read: Pandas - Cleaning & Grouping

## What You’ll Learn
In this pre-read, you’ll discover:
- Why real-world datasets are often **messy**  
- How to handle **missing values** properly  
- How **GroupBy** helps summarize data  
- How to use basic aggregations like **sum, mean, and count**  
- How **rename** and **drop** improve dataset clarity  

---

## Introduction: Real Data Is Never Perfect
Imagine downloading a sales report.

You notice:
- Some prices are missing  
- Column names are unclear  
- Data looks inconsistent  

That’s normal.

In real projects, **cleaning data** is often more important than analyzing it.

---

## Why Cleaning & Grouping Matter
Before building models or reports, you must:

1. **Fix missing or inconsistent values**  
2. **Organize data clearly**  
3. **Summarize patterns across groups**  

Without cleaning, results can be misleading.

---

## From Known to New: Raw Table → Clean Insight
### What You Already Know
You can:
- Load data into a DataFrame  
- Inspect rows and columns  

But raw data rarely gives immediate answers.

### The Pandas Way
You:
- Handle missing values  
- Group related rows  
- Apply summary statistics  

This transforms chaos into clarity.

---

## Core Cleaning & Grouping Concepts
### 1. Handling Missing Values
Missing values appear as empty or null entries.

You can:
- Remove rows with missing values  
- Fill them with defaults  
- Replace them strategically  

Ignoring missing data can distort analysis.

---

### 2. GroupBy Operations
**GroupBy** allows you to:
- Split data into categories  
- Apply operations to each category  
- Combine results  

*Think: “Group first, calculate second.”*

---

### 3. Basic Aggregations
After grouping, you can compute:

- **Sum** → total values  
- **Mean** → average  
- **Count** → number of entries  

These provide quick summaries.

---

### 4. Rename and Drop
Sometimes datasets need structural cleanup.

- **Rename** makes column names clearer  
- **Drop** removes unnecessary columns or rows  

Clean structure improves readability and reduces confusion.

---

## Putting It All Together
A common workflow:
1. Load dataset  
2. Identify and handle missing values  
3. Group by a category  
4. Apply aggregations  
5. Rename or drop columns for clarity  

This prepares data for modeling or reporting.

---

## Quick Practice (Think Before the Lecture)
1. Why might removing missing values be risky?  
2. When would grouping be more useful than filtering?  
3. Why is clear column naming important?

---

### Final Thought
Cleaning makes data trustworthy.  
Grouping makes data meaningful.  
Together, they turn messy tables into powerful insights.