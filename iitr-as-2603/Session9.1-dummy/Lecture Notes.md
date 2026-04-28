# SQL: Querying Data with SELECT and WHERE

In our last sessions, we used **pandas** to load, clean, and analyse data sitting inside CSV or Excel files. That works well for small datasets on a laptop, but it falls apart the moment the data becomes large, shared across many users, or needs to be **remembered permanently**. This is exactly where **databases** and **SQL** step in — and that is the world we will enter today.

## Why Do We Need Databases?

Before we jump into SQL, we must first understand **why databases exist at all**. Pandas, Excel, and CSV files feel enough when we are learning, but real companies need something much stronger.

- **Official Definition:** A **Database (DB)** is an organised collection of data stored electronically in a computer system, designed so that data can be added, read, updated, and deleted **safely and efficiently** by many users at the same time.
- **In Simple Words:** A database is a **smart digital godown** where data is **permanently stored, properly organised, and quickly searchable**.
- **Real-Life Example:** Think of **IRCTC (train ticket booking)**. Lakhs of people book tickets at the same second. The moment you pay, your booking is **saved forever**, your seat is **reserved instantly**, and nobody else can book the same seat. Excel or pandas can never do this — only a **database** can.

### Problems with Pandas / Excel / CSV Files

To truly feel the need for databases, let us see **where pandas and Excel fail** in real-world situations.

- **Not Permanent:** Pandas stores data in **RAM (temporary memory)**. The moment you close Python, your DataFrame is **gone forever**. A database stores data on **disk**, so it survives restarts and power cuts.
- **Single User Only:** Only one person can edit an Excel/CSV file at a time. A database lets **thousands of users read and write together** without conflicts.
- **Size Limits:** Excel crashes after around **10 lakh rows**, and pandas struggles when data goes beyond your laptop's RAM. Databases comfortably handle **billions of rows**.
- **No Safety Rules:** Nothing stops you from typing `"abcd"` in a salary column in Excel. Databases enforce **data types, unique IDs, and validation rules** automatically.
- **Slow Searches:** Searching in a giant CSV means scanning every row. Databases use **indexes** (like a book's index page) and return answers in **milliseconds**.
- **No Security:** Anyone who gets the Excel file can see everything. Databases support **usernames, passwords, and row-level permissions**.
- **No History / Backups:** If someone overwrites an Excel file, the old data is lost. Databases keep **transaction logs** and can **roll back** wrong changes.

In short, pandas is a **calculator for data**, but a database is the **bank vault that holds it**.

### What a Database Gives You (In One Line Each)

- **Persistence** → Data is stored **forever**, not just while the program runs.
- **Concurrency** → Many users can read and write **at the same time**.
- **Integrity** → **Rules and data types** keep bad data out.
- **Scalability** → Handles **crores of rows** without breaking a sweat.
- **Speed** → **Indexes** make searches very fast.
- **Security** → **Logins and permissions** protect sensitive data.
- **Recovery** → **Backups and transactions** protect against mistakes and crashes.

Now that we know **why** databases are needed, let us quickly look at the **different types** of databases you will hear about.

## Types of Databases

Not every database is the same. Different kinds of data need different kinds of databases, just like we use different vehicles for different journeys.

### 1. Relational Databases (SQL Databases)

- **Official Definition:** A **Relational Database** stores data in **tables** made of **rows and columns**, and uses **SQL** to interact with the data.
- **In Simple Words:** It is like a set of **connected Excel sheets** where every sheet has a fixed structure, and sheets can be **linked** using common IDs.
- **Real-Life Example:** A **bank's account system** — one table for customers, one for accounts, one for transactions, all connected by Customer ID.
- **Popular Examples:** **MySQL, PostgreSQL, Oracle, Microsoft SQL Server, SQLite**.
- **Best For:** Banking, inventory, bookings, HR, e-commerce — anywhere data has a **clear structure**.

### 2. Non-Relational Databases (NoSQL Databases)

- **Official Definition:** **NoSQL** databases store data in **flexible formats** like documents, key-value pairs, graphs, or wide columns instead of rigid tables.
- **In Simple Words:** They are used when data does **not fit neatly into rows and columns**, like social media posts or chat messages.
- **Real-Life Example:** Your **Instagram feed** — every post has different fields (photo, video, reel, story, caption, tags). Fixed columns would not work here.
- **Popular Examples:** **MongoDB** (document), **Redis** (key-value), **Cassandra** (wide-column), **Neo4j** (graph).
- **Best For:** Chat apps, social feeds, caching, recommendation engines, real-time analytics.

### 3. Other Common Types (Quick Overview)

You do not need to master these today, but you should at least **recognise the names**.

- **Cloud Databases:** Databases hosted on the internet, like **Amazon RDS, Google BigQuery, Snowflake**. You pay as you use.
- **Data Warehouses:** Special databases built for **analytics on huge historical data**, like **Snowflake, Redshift, BigQuery**.
- **In-Memory Databases:** Keep data in RAM for **lightning-fast access**, like **Redis** used in live dashboards and shopping carts.
- **Time-Series Databases:** Designed for sensor or stock-price data arriving every second, like **InfluxDB**.

### Quick Comparison

| Type | Data Shape | Example | Typical Use |
| :--- | :--- | :--- | :--- |
| Relational (SQL) | Tables (rows + columns) | MySQL, PostgreSQL | Banks, e-commerce, HR |
| Document (NoSQL) | JSON-like documents | MongoDB | Social media, user profiles |
| Key-Value (NoSQL) | Key → Value pairs | Redis | Caching, carts, sessions |
| Graph (NoSQL) | Nodes + connections | Neo4j | Friend networks, fraud detection |
| Data Warehouse | Huge analytical tables | Snowflake, BigQuery | Business reporting |

## Real-World Use Cases of Databases

To make things concrete, here are **everyday apps you already use** that run on databases.

- **IRCTC / MakeMyTrip:** Train and flight bookings, seat availability, payment history — relational databases.
- **Flipkart / Amazon:** Product catalog, orders, reviews, cart — a mix of SQL and NoSQL.
- **WhatsApp / Instagram:** Chats, stories, likes, follower lists — mostly NoSQL for scale.
- **Banks (HDFC, SBI, Paytm):** Account balances, transactions, loan records — strictly relational databases with strong safety rules.
- **Swiggy / Zomato:** Restaurants, menus, live orders, delivery tracking — relational for orders, NoSQL for live locations.
- **Hospitals (Apollo, AIIMS):** Patient records, prescriptions, reports — relational databases that keep data safe for years.
- **Schools and Universities:** Student info, attendance, marks, fees — classic relational database use case.

Every one of these apps needs **permanent, safe, shared, fast, and secure data** — and that is exactly what databases provide. Out of all these types, the **relational database** is the most common in the industry, and it uses one special language called **SQL**. That is where we go next.

## Introduction to SQL

Now that we know **what a database is** and **why we need one**, let us understand the language we use to **talk to relational databases**.

- **Official Definition:** **SQL** (Structured Query Language) is a standard language used to **store, read, update, and delete** data stored in relational databases.
- **In Simple Words:** SQL is the **language we use to talk to a database**, just like English is the language we use to talk to a shopkeeper.
- **Real-Life Example:** Think of a **library**. The librarian (database) has lakhs of books (data). You cannot go and search every shelf yourself. You simply say, *"Please give me all books by APJ Abdul Kalam published after 2010."* That sentence is your **SQL query**.

### Why Learn SQL?

- **Universal Language:** Almost every company in the world uses SQL. Whether it is MySQL, PostgreSQL, Oracle, or SQL Server — the **basic syntax is the same**.
- **Most In-Demand Skill:** SQL is consistently one of the **top 3 skills** asked in data, analyst, and backend job interviews.
- **Powerful with Very Little Code:** A question that takes **20 lines in Python** often takes **3 lines in SQL**.
- **Works on Huge Data:** SQL queries can handle **crores of rows** without loading everything into memory.

### Types of SQL Commands (Just the Names)

You do not need to memorise this today. Just know that SQL commands come in a few families; today we will focus on the **DQL** family (reading data).

- **DDL (Data Definition Language):** `CREATE`, `ALTER`, `DROP` — build and change table structure.
- **DML (Data Manipulation Language):** `INSERT`, `UPDATE`, `DELETE` — change the data inside tables.
- **DQL (Data Query Language):** `SELECT` — **read** data (our main focus today).
- **DCL (Data Control Language):** `GRANT`, `REVOKE` — manage user permissions.

Now that we know what SQL does and where it fits, a very natural question comes up: **"Sir, where do we actually write and run SQL?"** Let us answer that before we jump into our first query.

## Where to Write and Practice SQL

Unlike Python, SQL does **not** run inside VS Code directly — it runs inside a **database tool** that talks to a database. You have a few options, and you can pick any one based on your comfort. But remember, we **strongly recommend** downloading a proper workbench to match the setup you will see in real companies.

- **MySQL Workbench (Most Recommended):** This is the **official free tool** from MySQL. It gives you a proper query editor, a result viewer, and a visual view of your tables — exactly like the setup used in companies. Download and install it from the **official MySQL website**. This is the tool we will use for class demos.
- **DBeaver (Great Alternative):** DBeaver is a **free, universal database tool** that works with MySQL, PostgreSQL, SQLite, and many other databases. If MySQL Workbench feels a bit heavy on your laptop, DBeaver is a lighter and equally friendly option.
- **Online SQL Compilers (Not Recommended — only for quick practice):** Websites like **SQLiteOnline**, **OneCompiler**, **Programiz SQL**, or **DB Fiddle** let you run SQL queries directly in the browser **without installing anything**. They are fine if you just want to try out a small query, **but they usually do NOT let you save your work**, your database **resets when you close the tab**, and they do **not match a real company setup**. Use them only as a last option.

**Our clear recommendation:** Please go ahead and **download MySQL Workbench** (or DBeaver, if you prefer a lighter tool) on your laptop before you start practising. It is the closest to what you will see in real jobs and interviews, and your work is **saved permanently**. Use online compilers only when you are on a different machine and just want to try a quick query.

Once your tool is installed, open it, connect to a database, and you can simply paste every SQL code block from this lecture into it and hit **Run**. That is exactly how a data professional works every day.

## SQL Basics: Tables, Rows, and Columns

Every database is made of **tables**. And every table looks exactly like an Excel sheet — just stored on a computer in a more powerful form.

- **Official Definition:** A **table** is a collection of related data organised in **rows** (records) and **columns** (fields).
- **In Simple Words:** A table is just an **Excel sheet** sitting inside a database.
- **Real-Life Example:** An **attendance register** in school is a perfect table. Each **row** is one student, and each **column** is a piece of information (Name, Roll No, Class, Attendance %).

Let us break down the three main parts of any table.

- **Table:** The full Excel-like sheet (e.g., `employees`, `students`, `orders`).
- **Column (Field):** One **type of information**, like `Name` or `Salary`. Every column has a fixed **data type** (text, number, date).
- **Row (Record):** One **full entry**, like *one employee* with their Name, Salary, Department, City.
- **Primary Key:** A special column (like `EmployeeID`) whose value is **unique** for every row. It is like your Aadhaar number — no two people share it.

![Anatomy of a SQL table: columns, rows, primary key, and cell labelled on the employees table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session10/table_anatomy.png)

Before we start querying, let us set up **one single employees dataset** that we will use for the **entire lecture** — every SELECT, WHERE, ORDER BY, and LIMIT example will use this same table, so you can see the **cause and effect** clearly.

### Our Running Dataset: the `employees` Table

We first create the table structure, and then we insert 10 employee records into it. This is our **single source of truth** for the whole session.

```sql
-- Create a table called 'employees' with 6 columns
CREATE TABLE employees (
    EmployeeID   INT PRIMARY KEY,   -- Unique ID for each employee (like Aadhaar)
    Name         VARCHAR(50),       -- Employee's full name (text up to 50 letters)
    Department   VARCHAR(30),       -- Which team they belong to
    Salary       INT,               -- Monthly salary in rupees
    City         VARCHAR(30),       -- City where employee lives
    JoiningYear  INT                -- Year they joined the company
);

-- Insert 10 sample rows into the employees table
INSERT INTO employees VALUES (101, 'Aarav',  'Sales',       40000, 'Delhi',    2020);
INSERT INTO employees VALUES (102, 'Diya',   'HR',          55000, 'Mumbai',   2019);
INSERT INTO employees VALUES (103, 'Kabir',  'Sales',       60000, 'Delhi',    2021);
INSERT INTO employees VALUES (104, 'Meera',  'IT',          75000, 'Bengaluru',2018);
INSERT INTO employees VALUES (105, 'Rohan',  'IT',          90000, 'Bengaluru',2017);
INSERT INTO employees VALUES (106, 'Sneha',  'HR',          50000, 'Mumbai',   2022);
INSERT INTO employees VALUES (107, 'Vihaan', 'Finance',     70000, 'Delhi',    2019);
INSERT INTO employees VALUES (108, 'Ishaan', 'Finance',     85000, 'Mumbai',   2016);
INSERT INTO employees VALUES (109, 'Anaya',  'Sales',       45000, 'Bengaluru',2023);
INSERT INTO employees VALUES (110, 'Riya',   'IT',          95000, 'Delhi',    2015);
```

**How the code works:**

- `CREATE TABLE employees (...)` tells the database to make a **new empty table** with the given column names and **data types**.
- `PRIMARY KEY` on `EmployeeID` guarantees that **no two rows can have the same EmployeeID**, preventing duplicates.
- `VARCHAR(50)` means the column can store **up to 50 characters** of text.
- `INSERT INTO employees VALUES (...)` adds **one row** at a time. The **order of values** must match the **order of columns** in the CREATE TABLE.
- After running all 10 INSERTs, our `employees` table has **10 employees** spread across 4 departments and 3 cities. This table will be **used for every query** in the rest of the lecture.

Now that our data is loaded, let us learn how to **read** it using the most important keyword in SQL — `SELECT`.

## SELECT Queries: Reading Data

`SELECT` is the first word of **almost every SQL query you will ever write**. It simply tells the database, *"Give me some data from this table."*

- **Official Definition:** **`SELECT`** is the SQL statement used to **retrieve data** from one or more tables.
- **In Simple Words:** `SELECT` means *"show me"*. You tell the database **which columns** you want and **which table** to get them from.
- **Real-Life Example:** It is like asking the waiter, *"Please show me only the desserts from the menu."* You are not asking for everything — just what you need.

The basic structure of every SELECT query looks like this:

```sql
SELECT column1, column2, ...
FROM table_name;
```

Let us try this on our `employees` table.

### Select All Columns with `*`

The star `*` is a shortcut that means **"all columns"**. Use it when you want to see the **full table**.

```sql
-- Show ALL columns and ALL rows from the employees table
SELECT *
FROM employees;
```

**How the code works:**

- `SELECT *` asks the database for **every column** in the table.
- `FROM employees` tells the database **which table** to read from.
- The semicolon `;` at the end marks the **end of the SQL statement** (like a full stop in English).
- The output will be all **10 rows** and all **6 columns** of our employees table.

A small best practice: in **real company projects**, avoid `SELECT *` because it brings back huge amounts of data. Always mention only the columns you really need.

### Select Specific Columns

Most of the time, you only want **2 or 3 columns** out of a big table. Just list them with commas.

```sql
-- Show only the Name and Salary of every employee
SELECT Name, Salary
FROM employees;

-- Show three columns: Name, Department, and City
SELECT Name, Department, City
FROM employees;
```

**How the code works:**

- We list the **exact column names** after `SELECT`, separated by **commas**.
- The database returns a new table with **only those columns** for all 10 employees.
- The **order we write** (Name, Salary) is the **order we get back**, which is useful for reports.

### Renaming Columns in the Output with `AS`

Sometimes we want the output column name to look **friendlier** in a report. We use **`AS`** to give it an alias.

```sql
-- Rename 'Name' to 'Employee Name' and 'Salary' to 'Monthly Pay'
SELECT Name       AS "Employee Name",
       Salary     AS "Monthly Pay",
       Department AS Team
FROM employees;
```

**How the code works:**

- `AS "Employee Name"` renames the output column. Quotes are used because the alias has a **space** in it.
- For single-word aliases like `Team`, quotes are **not needed**.
- The **original table column is NOT changed** — only the **display name** in the result is changed.
- This is very useful when preparing data for dashboards or Excel exports.

### Getting Unique Values with `DISTINCT`

Our `employees` table has 10 rows but only **4 unique departments** (Sales, HR, IT, Finance). If we want to see each **unique value only once**, we use `DISTINCT`.

- **Official Definition:** **`DISTINCT`** removes duplicate values from the result and returns only **unique** entries.
- **In Simple Words:** It means *"show me one of each kind"*.
- **Real-Life Example:** In your WhatsApp contact list, if 5 different people are from **Delhi**, `DISTINCT` would just show "Delhi" **once** in a list of cities.

```sql
-- Show each Department name only ONCE (no duplicates)
SELECT DISTINCT Department
FROM employees;

-- Show each unique City
SELECT DISTINCT City
FROM employees;

-- Show each unique combination of Department AND City
SELECT DISTINCT Department, City
FROM employees;
```

**How the code works:**

- `SELECT DISTINCT Department` looks at the Department column and keeps **only one copy** of each value.
- With a single column, we get 4 rows back: **Sales, HR, IT, Finance**.
- With a single column `City`, we get 3 rows: **Delhi, Mumbai, Bengaluru**.
- When `DISTINCT` is used with **multiple columns**, the database treats the **whole combination** as one unit. So **`Sales, Delhi`** is different from **`Sales, Bengaluru`**.

A common doubt: *"What if I write `DISTINCT` after the first column only?"* Remember, `DISTINCT` always applies to **all columns after it** in the SELECT, not just one. There is no way to DISTINCT just one column while keeping others duplicated.

## Filtering Data with WHERE

Reading the **whole table** is rarely useful. In real work, we usually want to answer questions like *"Which employees earn more than 60000?"* or *"Which employees live in Delhi?"* For this, we use the **`WHERE`** clause.

- **Official Definition:** **`WHERE`** is the SQL clause used to **filter rows** based on a given condition, returning only the rows that match.
- **In Simple Words:** `WHERE` means *"only give me rows where this condition is true"*.
- **Real-Life Example:** It is like a **security guard at the mall gate**. Only visitors who meet the condition (*valid ticket*) are allowed inside. Others are turned away.

The basic structure is:

```sql
SELECT columns
FROM table_name
WHERE condition;
```

### Filtering with Comparison Operators

SQL gives us the same comparison operators that you use in math class.

- **`=`** → equal to (notice: **single** equal sign in SQL, not `==`)
- **`<>`** or **`!=`** → not equal to
- **`>`** → greater than
- **`<`** → less than
- **`>=`** → greater than or equal to
- **`<=`** → less than or equal to

Let us try them on our running `employees` table.

```sql
-- Employees who work in the Sales department
SELECT Name, Department, Salary
FROM employees
WHERE Department = 'Sales';

-- Employees earning MORE than 60000 per month
SELECT Name, Salary
FROM employees
WHERE Salary > 60000;

-- Employees who DO NOT belong to IT
SELECT Name, Department
FROM employees
WHERE Department <> 'IT';

-- Employees who joined ON OR AFTER 2020
SELECT Name, JoiningYear
FROM employees
WHERE JoiningYear >= 2020;
```

**How the code works:**

- In `WHERE Department = 'Sales'`, text values are always wrapped in **single quotes**.
- Numeric comparisons like `Salary > 60000` do **not** use quotes because numbers are not text.
- `<>` and `!=` both mean **"not equal"**. Most databases accept both, but `<>` is the official SQL standard.
- The database checks the condition **row by row** and keeps only the rows where the condition is **TRUE**.

A very common beginner mistake: writing `WHERE Department == 'Sales'` with **two** equal signs. That works in Python and JavaScript, but in SQL we use **only one** equal sign.

### Filtering with Logical Operators (AND, OR, NOT)

Real questions usually have **multiple conditions**. For example, *"Sales employees in Delhi earning more than 50000"*. We combine conditions using **`AND`**, **`OR`**, and **`NOT`**.

- **`AND`** → **Both** conditions must be true (like Venn diagram **intersection**).
- **`OR`** → **At least one** condition must be true (like Venn diagram **union**).
- **`NOT`** → **Reverses** the condition (true becomes false).

```sql
-- AND: Sales employees who earn more than 50000
SELECT Name, Department, Salary
FROM employees
WHERE Department = 'Sales'
  AND Salary > 50000;

-- OR: Employees from Delhi OR Mumbai
SELECT Name, City
FROM employees
WHERE City = 'Delhi'
   OR City = 'Mumbai';

-- NOT: Employees NOT from Bengaluru
SELECT Name, City
FROM employees
WHERE NOT City = 'Bengaluru';

-- Combining: IT employees in Bengaluru earning at least 80000
SELECT Name, Department, City, Salary
FROM employees
WHERE Department = 'IT'
  AND City = 'Bengaluru'
  AND Salary >= 80000;
```

**How the code works:**

- `AND` narrows the result. Each row must pass **every** condition to be included.
- `OR` widens the result. A row is kept if it matches **any** one of the conditions.
- `NOT` flips the truth value. `NOT City = 'Bengaluru'` is the same as `City <> 'Bengaluru'`.
- When mixing `AND` and `OR`, always use **parentheses** to control the order, just like in math.

### Helpful Shortcuts: BETWEEN, IN, and LIKE

SQL gives us three very handy shortcuts to avoid writing long `OR` or comparison chains.

- **`BETWEEN a AND b`** → Checks if a value is within a range (both ends included).
- **`IN (a, b, c)`** → Checks if a value matches any item in a list.
- **`LIKE 'pattern'`** → Checks if a text value matches a pattern (`%` = any characters, `_` = exactly one character).

```sql
-- BETWEEN: Employees earning between 50000 and 80000 (both inclusive)
SELECT Name, Salary
FROM employees
WHERE Salary BETWEEN 50000 AND 80000;

-- IN: Employees from Delhi, Mumbai, or Bengaluru (same as 3 ORs)
SELECT Name, City
FROM employees
WHERE City IN ('Delhi', 'Mumbai', 'Bengaluru');

-- LIKE: Employees whose Name starts with the letter 'A'
SELECT Name
FROM employees
WHERE Name LIKE 'A%';

-- LIKE: Employees whose Name ends with 'a'
SELECT Name
FROM employees
WHERE Name LIKE '%a';
```

**How the code works:**

- `BETWEEN 50000 AND 80000` is a cleaner way to write `Salary >= 50000 AND Salary <= 80000`. **Both boundaries are included**.
- `IN ('Delhi', 'Mumbai')` is a shorter, faster way to write many `OR` conditions.
- In `LIKE 'A%'`, the percent sign `%` means *"any number of characters (including zero)"*. So it matches Aarav, Anaya, Ananya, etc.
- `LIKE '%a'` finds names **ending with** the letter 'a', like Diya, Meera, Sneha, Anaya, Riya.

### Filtering for Missing Values: IS NULL

In real databases, some values are **missing** (NULL). For example, a new employee may not yet have a city recorded. We check for such rows using **`IS NULL`** (not `= NULL`).

```sql
-- (Suppose some employees have no City recorded)
-- Find all employees whose City is missing
SELECT Name
FROM employees
WHERE City IS NULL;

-- Find all employees whose City is filled in
SELECT Name, City
FROM employees
WHERE City IS NOT NULL;
```

**How the code works:**

- `NULL` means **"unknown" or "no value entered"** — it is **not** zero and **not** empty string.
- `City = NULL` does **not** work in SQL, because NULL cannot be compared using `=`.
- Always use `IS NULL` or `IS NOT NULL` to check missing data.

## Sorting and Limiting Results

After filtering, we often want results in a **specific order** — highest salary first, or names in alphabetical order. And sometimes we just want the **top 5 or top 10** rows. For this we use **`ORDER BY`** and **`LIMIT`**.

### Sorting with ORDER BY

- **Official Definition:** **`ORDER BY`** sorts the output rows based on one or more columns in ascending or descending order.
- **In Simple Words:** It means *"arrange the result in this order before showing it to me"*.
- **Real-Life Example:** It is like asking Flipkart *"Show me phones sorted by **price: low to high**"*. The data is the same, but the **order** helps you decide.

```sql
-- Sort all employees by Salary in ASCENDING order (low to high, default)
SELECT Name, Salary
FROM employees
ORDER BY Salary;

-- Explicit ASC keyword (same result as above)
SELECT Name, Salary
FROM employees
ORDER BY Salary ASC;

-- Sort by Salary in DESCENDING order (high to low)
SELECT Name, Salary
FROM employees
ORDER BY Salary DESC;

-- Sort by Department (A-Z), then by Salary (high to low) within each department
SELECT Name, Department, Salary
FROM employees
ORDER BY Department ASC, Salary DESC;
```

**How the code works:**

- **`ASC`** = Ascending (smallest first). This is the **default**, so you can omit it.
- **`DESC`** = Descending (largest first). You must write it if you want reverse order.
- When you sort by **multiple columns**, SQL sorts first by the **first column**, and uses the **second column as a tie-breaker**.
- For text columns, sorting is **alphabetical** (A to Z for ASC, Z to A for DESC).

### Limiting Rows with LIMIT

Sometimes we only care about the **top few rows** — like the *top 5 highest paid employees*. We use **`LIMIT`** for this.

- **Official Definition:** **`LIMIT n`** restricts the query output to the first **n** rows.
- **In Simple Words:** It means *"give me only this many rows, not everything"*.
- **Real-Life Example:** It is like Google Images showing you only the **first 50 results** instead of all 10,00,000 matches.

```sql
-- Show only the first 3 employees (in the order they are stored)
SELECT *
FROM employees
LIMIT 3;

-- TOP 3 highest paid employees (combine ORDER BY + LIMIT)
SELECT Name, Salary
FROM employees
ORDER BY Salary DESC
LIMIT 3;

-- LOWEST paid 5 employees
SELECT Name, Salary
FROM employees
ORDER BY Salary ASC
LIMIT 5;

-- Top 2 highest paid IT employees (combine WHERE + ORDER BY + LIMIT)
SELECT Name, Department, Salary
FROM employees
WHERE Department = 'IT'
ORDER BY Salary DESC
LIMIT 2;
```

**How the code works:**

- `LIMIT 3` tells the database to return **at most 3 rows**.
- **Combining `ORDER BY` with `LIMIT`** is the standard way to get a **"Top N"** report.
- Without `ORDER BY`, `LIMIT` just gives the first N rows in whatever order the database chooses — which may not be meaningful.
- Note: some databases (like Microsoft SQL Server) use `TOP 3` instead of `LIMIT 3`, but MySQL, PostgreSQL, and SQLite all use `LIMIT`.

### The Full Query Order

Once you learn `SELECT`, `WHERE`, `ORDER BY`, and `LIMIT`, the **order you write them in** is fixed. Remember this pattern — it is the **backbone of every SQL query**.

![SQL query pipeline showing written order SELECT → FROM → WHERE → ORDER BY → LIMIT vs execution order FROM → WHERE → ORDER BY → LIMIT → SELECT](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session10/sql_query_pipeline.png)

```sql
SELECT    columns          -- What to show
FROM      table_name       -- Which table to read
WHERE     condition        -- Which rows to keep
ORDER BY  column DESC      -- How to arrange them
LIMIT     n;               -- How many to return
```

For example, *"Show me the top 3 highest-paid Delhi employees"* becomes:

```sql
-- Top 3 highest-paid employees based in Delhi
SELECT Name, City, Salary
FROM employees
WHERE City = 'Delhi'
ORDER BY Salary DESC
LIMIT 3;
```

**How the code works:**

- First, `FROM employees` loads the table into memory.
- Then `WHERE City = 'Delhi'` keeps only Delhi-based rows.
- `ORDER BY Salary DESC` sorts those rows from **highest to lowest salary**.
- Finally, `LIMIT 3` returns only the **top 3 rows** of that sorted list.

## Pandas vs SQL — The Big Bridge

Many of you are coming from the last session where we used **pandas**. The good news: almost **every SQL idea has a pandas twin**. Once you see the pattern, switching between them becomes effortless.

- **Official Definition:** Both **pandas** and **SQL** are tools to query structured tabular data; one runs inside Python on DataFrames, the other runs inside databases on tables.
- **In Simple Words:** **Same question, two languages**. Like ordering *"one cup of tea"* in Hindi vs English — both get you tea.
- **Real-Life Example:** Google Maps and Apple Maps both show the same roads. Only the **buttons and words** are different; the destination is the same.

![Side-by-side mapping of SQL and pandas for the same top-3 highest-paid Delhi employees query, step by step: filter, sort, limit, pick columns](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session10/pandas_vs_sql_bridge.png)

Below is the side-by-side mapping using **our same `employees` table**. In pandas we assume the same data has been loaded into a DataFrame called `df`.

### Setup the Same Data in Pandas

```python
# Import pandas with its standard alias
import pandas as pd

# Create the SAME employees table as a pandas DataFrame
df = pd.DataFrame({
    "EmployeeID":  [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name":        ["Aarav","Diya","Kabir","Meera","Rohan",
                    "Sneha","Vihaan","Ishaan","Anaya","Riya"],
    "Department":  ["Sales","HR","Sales","IT","IT",
                    "HR","Finance","Finance","Sales","IT"],
    "Salary":      [40000, 55000, 60000, 75000, 90000,
                    50000, 70000, 85000, 45000, 95000],
    "City":        ["Delhi","Mumbai","Delhi","Bengaluru","Bengaluru",
                    "Mumbai","Delhi","Mumbai","Bengaluru","Delhi"],
    "JoiningYear": [2020, 2019, 2021, 2018, 2017,
                    2022, 2019, 2016, 2023, 2015]
})
```

**How the code works:**

- We create a pandas DataFrame with the **exact same 10 rows** we inserted in SQL.
- Each key in the dictionary becomes a **column**, and each list is that column's values.
- From now on, `df` in pandas is the **same thing** as the `employees` table in SQL.

### Side-by-Side Mapping

Let us take the most common operations and see them in **both languages**, on the same data.

#### 1. Select all rows and columns

```sql
-- SQL
SELECT * FROM employees;
```

```python
# Pandas
df
```

**How the code works:** `SELECT *` in SQL and just writing `df` in pandas both ask for the **full table**.

#### 2. Select specific columns

```sql
-- SQL
SELECT Name, Salary FROM employees;
```

```python
# Pandas
df[["Name", "Salary"]]
```

**How the code works:** In SQL we list column names after `SELECT`. In pandas, we pass a **list of column names** inside double brackets `[[ ]]` to get a sub-table.

#### 3. DISTINCT unique values

```sql
-- SQL
SELECT DISTINCT Department FROM employees;
```

```python
# Pandas
df["Department"].unique()
```

**How the code works:** `DISTINCT` in SQL and `.unique()` in pandas both remove duplicates and give you each unique value once.

#### 4. WHERE — single condition

```sql
-- SQL
SELECT Name, Salary
FROM employees
WHERE Salary > 60000;
```

```python
# Pandas
df[df["Salary"] > 60000][["Name", "Salary"]]
```

**How the code works:** In pandas, `df["Salary"] > 60000` creates a **Boolean mask** of True/False, and `df[mask]` keeps only the True rows. Then we pick the needed columns.

#### 5. WHERE with AND

```sql
-- SQL
SELECT Name, Department, Salary
FROM employees
WHERE Department = 'Sales'
  AND Salary > 50000;
```

```python
# Pandas (parentheses are REQUIRED around each condition)
df[(df["Department"] == "Sales") & (df["Salary"] > 50000)]
```

**How the code works:** SQL uses `AND`; pandas uses `&`. In pandas, each condition **must be in parentheses**, otherwise Python gets confused about operator order.

#### 6. WHERE with OR and IN

```sql
-- SQL
SELECT Name, City
FROM employees
WHERE City IN ('Delhi', 'Mumbai');
```

```python
# Pandas
df[df["City"].isin(["Delhi", "Mumbai"])][["Name", "City"]]
```

**How the code works:** SQL's `IN (...)` is the same as pandas' `.isin([...])`. Both give rows where the column value matches **any item** in the list.

#### 7. ORDER BY

```sql
-- SQL
SELECT Name, Salary
FROM employees
ORDER BY Salary DESC;
```

```python
# Pandas
df.sort_values(by="Salary", ascending=False)[["Name", "Salary"]]
```

**How the code works:** `ORDER BY ... DESC` in SQL matches `sort_values(by=..., ascending=False)` in pandas. Both arrange the data before returning it.

#### 8. LIMIT

```sql
-- SQL
SELECT Name, Salary
FROM employees
ORDER BY Salary DESC
LIMIT 3;
```

```python
# Pandas
df.sort_values(by="Salary", ascending=False).head(3)[["Name", "Salary"]]
```

**How the code works:** `LIMIT 3` is the same as pandas' `.head(3)`. Both return only the **first 3 rows** of the sorted result.

#### 9. The Full Query Example

*"Top 3 highest-paid Delhi employees"* — our earlier example — in both languages.

```sql
-- SQL
SELECT Name, City, Salary
FROM employees
WHERE City = 'Delhi'
ORDER BY Salary DESC
LIMIT 3;
```

```python
# Pandas
(
    df[df["City"] == "Delhi"]
      .sort_values(by="Salary", ascending=False)
      .head(3)[["Name", "City", "Salary"]]
)
```

**How the code works:** The **thinking order is identical** in both — filter → sort → limit → pick columns. Only the **syntax** changes. Once this click happens, you can easily move between SQL and pandas depending on where your data lives.

### Quick Mapping Table (Pandas ↔ SQL)

| Task | SQL | Pandas |
| :--- | :--- | :--- |
| All rows, all columns | `SELECT * FROM employees` | `df` |
| Specific columns | `SELECT Name, Salary FROM employees` | `df[["Name","Salary"]]` |
| Unique values | `SELECT DISTINCT Department FROM employees` | `df["Department"].unique()` |
| Filter — single | `WHERE Salary > 60000` | `df[df["Salary"] > 60000]` |
| Filter — AND | `WHERE A = x AND B > y` | `df[(df["A"]==x) & (df["B"]>y)]` |
| Filter — IN | `WHERE City IN ('Delhi','Mumbai')` | `df[df["City"].isin(["Delhi","Mumbai"])]` |
| Not equal | `WHERE City <> 'Delhi'` | `df[df["City"] != "Delhi"]` |
| Null check | `WHERE City IS NULL` | `df[df["City"].isna()]` |
| Sort | `ORDER BY Salary DESC` | `df.sort_values("Salary", ascending=False)` |
| Top N | `LIMIT 3` | `df.head(3)` |
| Rename column | `SELECT Name AS "Emp Name"` | `df.rename(columns={"Name":"Emp Name"})` |

## Common Doubts and Mistakes

Let us quickly go over the mistakes students make most often when starting SQL.

- **Using `==` instead of `=`:** In SQL, equality is a **single** equal sign, not double.
- **Forgetting quotes around text:** `WHERE Department = Sales` fails; it must be `WHERE Department = 'Sales'`.
- **Using `= NULL` instead of `IS NULL`:** NULL cannot be compared with `=`. Always use `IS NULL` or `IS NOT NULL`.
- **Wrong keyword order:** SQL is strict — `SELECT` first, then `FROM`, `WHERE`, `ORDER BY`, `LIMIT`. Changing the order is an error.
- **SELECT * in production:** It is fine while learning, but in real projects it slows things down and exposes unnecessary columns.
- **Uppercase vs lowercase:** SQL keywords are **not case-sensitive** (`SELECT` = `select`), but **string values are case-sensitive** (`'Sales'` is not `'sales'`).
- **Forgetting the semicolon:** Many tools require `;` at the end. Always finish your statement with one.
- **Mixing `AND`/`OR` without parentheses:** `A = 1 OR B = 2 AND C = 3` is not always what you think. Use parentheses to be safe.

## Important Commands & Keywords (Quick Revision)

Use this table as your one-page cheat sheet before assignments and interviews.

| Command / Keyword | What It Does | Simple Example |
| :--- | :--- | :--- |
| `CREATE TABLE` | Creates a new empty table | `CREATE TABLE employees (...)` |
| `INSERT INTO` | Adds a new row to a table | `INSERT INTO employees VALUES (101, 'Aarav', ...)` |
| `SELECT` | Reads columns from a table | `SELECT Name FROM employees` |
| `SELECT *` | Reads all columns | `SELECT * FROM employees` |
| `FROM` | Tells which table to read | `FROM employees` |
| `AS` | Renames a column in output | `SELECT Name AS "Emp Name"` |
| `DISTINCT` | Removes duplicates | `SELECT DISTINCT City FROM employees` |
| `WHERE` | Filters rows by a condition | `WHERE Salary > 50000` |
| `=`, `<>`, `>`, `<`, `>=`, `<=` | Comparison operators | `WHERE Salary >= 60000` |
| `AND`, `OR`, `NOT` | Combine multiple conditions | `WHERE A = 1 AND B > 2` |
| `BETWEEN ... AND ...` | Range filter (inclusive) | `WHERE Salary BETWEEN 50000 AND 80000` |
| `IN (...)` | Match any value in a list | `WHERE City IN ('Delhi','Mumbai')` |
| `LIKE`, `%`, `_` | Pattern match on text | `WHERE Name LIKE 'A%'` |
| `IS NULL` / `IS NOT NULL` | Check for missing values | `WHERE City IS NULL` |
| `ORDER BY ... ASC/DESC` | Sort result rows | `ORDER BY Salary DESC` |
| `LIMIT n` | Return first n rows | `LIMIT 5` |
| `;` | End of SQL statement | `SELECT * FROM employees;` |

With this, you can now **read, filter, sort, and limit** data from any SQL database confidently — which is the first and most important skill in handling real-world structured data. In the next session, we will use the **same `employees` table** to learn how to **modify and combine data** with UPDATE, DELETE, and JOINs.
