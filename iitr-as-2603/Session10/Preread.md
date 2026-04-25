# Pre-read: SQL: Querying Data with SELECT and WHERE

## The hook
You already shuffle rows and columns in **pandas** when you work with a CSV on your laptop — a solid first step. The moment a company needs one shared number for train seats, canteen stock, or payroll, the data cannot live only in your notebook’s temporary memory. Picture IRCTC or a busy Swiggy kitchen screen: many people need the same rows at the same time, and nothing should vanish when someone closes a file. **Databases** hold that kind of data for good, and we step into how you **ask** for answers from one today.

## The problem
**What if** you had to list “everyone in Sales in Delhi, joined after 2020, top three by salary” from a sheet with ten thousand names? Scrolling, manual filters, and re-sorting every day is slow. **What if** two people email two different “final” Excel files, and no one knows which one is the truth? You need a single, trusted store and a **repeatable instruction** the machine can run again and again. The pain is not “math is hard” — the pain is scale, sharing, and trust in the source.

## The solution preview
**SQL** (Structured Query Language) is the common way to **read** data stored as **tables** (rows and columns) inside a relational **database**; in this session you will use it to **select** the columns you need, **filter** rows, **sort** the result, and **cap** how many lines come back — the same story you know from **DataFrames**, but where the data lives in a proper, shared system. The live class will show you the order of the words, how to run a query in a real tool, and one running **employees** table so every new keyword has a clear before-and-after.

## A simple analogy
Think of a **library** with lakhs of books. You do not search every shelf yourself. You walk to the desk and say, in effect: “From this catalogue, show me only these details, only books that match this rule, in this order, and stop after a few results.” The librarian is the **database**; your clear sentence is the **query** — the same **library** picture we use in the lecture notes.

## Key terms
- **Table:** A named grid in the database: each **row** is one record, each **column** is one type of field (name, salary, city).
- **SQL:** The usual language to ask a relational **database** for data; the basics repeat across many products.
- **SELECT:** "Show me these **columns**" — the part of a query that lists what you want to see.
- **WHERE:** "Keep only **rows** that pass this test" — your filter, like a rule at the gate.
- **DISTINCT:** "Show each different value only once" — useful for unique names or cities without repeats.
- **ORDER BY** and **LIMIT:** Sort the answer (e.g. salary high to low) and return only the first few rows when you do not need the full list.

## Questions we will answer in the session
1. Why does a **database** beat a lone **pandas** session or a private spreadsheet when data must be **permanent**, **shared**, and **reliable** for many people at once?
2. How do you put "which **columns**, which **table**, which **rows**, which **order**, how many **rows**" into one well-formed **SQL** question the system understands?
3. How does the **same** filter-and-sort job you would do in **pandas** line up, step by step, with **SQL** so you do not juggle two unrelated mental models?

## What you will be able to do after the session
- Explain **why** data often lives in **databases** and what **SQL** is for, in plain words tied to real apps you already use.
- Read data using **SELECT**, narrow it with **WHERE** (with common tests and combinations), and use **DISTINCT**, **ORDER BY**, and **LIMIT** where they fit.
- Map **DataFrame** selection and filtering to the **SQL** version of the same job so toolbars and interview questions look familiar.
- Run ideas against one consistent **employees** table in class so you see exactly how each keyword changes the **output**.
