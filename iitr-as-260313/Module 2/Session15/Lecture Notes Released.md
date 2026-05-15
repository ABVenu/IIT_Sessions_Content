# Using SQL Databases with AI Applications

## Context of This Session

In the previous session, we built the foundation of working with databases. We explored why file-based storage fails at scale, met the main database families, learned core SQL vocabulary (tables, rows, columns, keys, constraints, data types), set up Supabase, and wrote first CRUD queries — `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`. We also used the `WHERE` clause with filters such as `LIKE`, `BETWEEN`, and `IN`.

That work stayed mostly on a *single table*. Real AI systems, though, spread data across **related tables** and need queries that **sort**, **page**, and **combine** those tables.

**In this session (live coverage), you:**

- Recap **SELECT**, **WHERE**, **UPDATE**, and **DELETE** on one table, and see how **`LIKE`** helps match patterns in text.
- Control how rows come back using **`ORDER BY`** (`ASC` / **`DESC`**), **`LIMIT`**, and **`OFFSET`** (pagination), including how some online compilers may not support **`OFFSET`** even though PostgreSQL does.
- See why designers split data to cut **redundancy**, and what **normalization** means in plain language.
- Learn the three relationship shapes — **one-to-one**, **one-to-many**, and **many-to-many** (with a **junction table** when both sides are “many”).
- Connect **foreign key columns** (same ID on two tables) as the practical “bridge” you match in queries.
- Understand **cross join** (every row × every row) as the wrong default, then **inner join** with an **`ON`** condition using **`customers`** and **`orders`**.

**Practice note:** Creating linked tables in the Supabase UI, multi-table **`INSERT`**, and **`ON DELETE CASCADE`** rules are in your course document for self-practice and later classes; they were **not** the focus of the live walk-through this day.

---

## Quick Recap — CRUD Operations from Session 14

Before we move forward, these commands stay the base for everything today.

| SQL Command | What It Does | Quick Example |
|---|---|---|
| `CREATE TABLE` | Defines a new table with columns and constraints | `CREATE TABLE students (...)` |
| `INSERT INTO` | Adds a new row of data | `INSERT INTO students VALUES (...)` |
| `SELECT` | Reads data from a table | `SELECT * FROM students` |
| `UPDATE` | Modifies existing rows | `UPDATE students SET city = 'Delhi' WHERE student_id = 1` |
| `DELETE` | Removes rows permanently | `DELETE FROM students WHERE student_id = 1` |
| `WHERE` | Filters which rows are affected | `WHERE city = 'Mumbai' AND is_active = TRUE` |

- **Golden rule:** Always use **`WHERE`** with **`UPDATE`** and **`DELETE`** unless you truly intend to touch every row.
- **Today’s build:** We extend **`SELECT`** with sorting, paging, and joins across tables that share an ID column.

### Filtering with `LIKE` — Pattern Matching (Recap Extension)

- **Official Definition:** **`LIKE`** is a **`WHERE`** operator that compares text to a **pattern**. **`%`** means “any characters (including none).” **`_`** means “exactly one character.”
- **In Simple Words:** Instead of spelling the full string, you say “anything that starts with J” or “anything that contains `ai`.”
- **Real-Life Example:** Searching your phone contacts for names that start with “Ra” is the same idea as `LIKE 'Ra%'`.

**Full Code — Names Starting With a Letter:**

```sql
-- Block 1: names that start with J
SELECT *                        -- return all columns for matching rows
FROM customers                  -- read from the customers table
WHERE name LIKE 'J%';           -- J then any characters (percent wildcard)

-- Block 2: names that contain 'a' anywhere
SELECT *                        -- return all columns
FROM customers                  -- source table
WHERE name LIKE '%a%';         -- any chars, then a, then any chars

-- Block 3: single-character wildcard between J and smith
SELECT *                        -- return all columns
FROM customers                  -- source table
WHERE name LIKE 'J_smith';      -- underscore = exactly one unknown character
```

**How the code works:**

- **`LIKE 'J%'`** — The **`%`** is a wildcard after **`J`**, so **`John`**, **`Jaya`**, and **`Jagdish`** match.
- **`LIKE '%a%'`** — **`%`** on both sides means “**`a`** can appear anywhere in the string.”
- **`LIKE 'J_smith'`** — Each **`_`** stands for exactly one character between **`J`** and **`smith`**.
- SQL keywords such as **`SELECT`** are usually **case-insensitive** in PostgreSQL-style engines; style is still important for team readability.

---

## Sorting, Limiting, and Pagination — ORDER BY, LIMIT, OFFSET

When you run `SELECT * FROM students`, the database may return rows in an **undefined** order. Large tables should not dump every row to the screen at once. **`ORDER BY`**, **`LIMIT`**, and **`OFFSET`** fix both problems.

Think of a music app: search, then **sort**, show **top N**, and **skip** to the next page.

### ORDER BY — Sorting Results

- **Official Definition:** **`ORDER BY`** sorts the result set by one or more columns, **ascending (`ASC`)** or **descending (`DESC`)**.
- **In Simple Words:** It is the “sort by” control — A→Z, 1→100, oldest→newest, or the reverse.
- **Real-Life Example:** Sorting Zomato listings by rating or delivery time maps to **`ORDER BY`**.

**Full Code — Sorting Students:**

```sql
-- Sort all students alphabetically by their full name (A to Z)
SELECT * FROM students          -- fetch all columns
ORDER BY full_name ASC;         -- ascending sort on full_name

-- Sort students by enrollment date, most recent first
SELECT * FROM students          -- fetch all columns
ORDER BY enrollment_date DESC; -- newest dates appear first

-- Sort by city, then by name inside each city
SELECT full_name, city, course FROM students  -- only these columns in the result
ORDER BY city ASC, full_name ASC;             -- city first, then name as tie-breaker
```

**How the code works:**

- **`ORDER BY col ASC`** — Ascending order (default if you omit **`ASC`** in many databases).
- **`ORDER BY col DESC`** — Reverses the sort.
- **Multiple columns** — Sort by the first; when two rows tie, the second column breaks the tie.

### LIMIT — Capping the Number of Results

- **Official Definition:** **`LIMIT`** caps how many rows the query returns.
- **In Simple Words:** “Show me only the first **N** rows.”
- **Real-Life Example:** Ten Google results per page ≈ **`LIMIT 10`** (plus **`OFFSET`** for page 2).

**Full Code — Limiting Results:**

```sql
SELECT * FROM students          -- fetch all columns
LIMIT 5;                        -- cap output to five rows

SELECT full_name, enrollment_date FROM students  -- only name and date columns
ORDER BY enrollment_date DESC    -- newest enrollments first
LIMIT 3;                        -- keep only three rows after sorting
```

**How the code works:**

- **`LIMIT 5`** — At most five rows.
- **`ORDER BY` + `LIMIT`** — Sort first, then take the “top” slice (e.g. top purchases).

### OFFSET — Skipping Rows for Pagination

- **Official Definition:** **`OFFSET`** skips **N** rows before **`LIMIT`** starts counting. Together they implement **pagination**.
- **In Simple Words:** “Skip the first 10, then show the next 5.”
- **Real-Life Example:** Flipkart page 2 = same page size, larger skip.

**Full Code — Implementing Pagination:**

```sql
-- Page 1: first 3 rows
SELECT full_name, city FROM students  -- columns to display
ORDER BY student_id ASC              -- stable order by id
LIMIT 3 OFFSET 0;                    -- show 3 rows, skip none

-- Page 2: next 3 rows
SELECT full_name, city FROM students  -- same projection
ORDER BY student_id ASC              -- same ordering
LIMIT 3 OFFSET 3;                    -- skip first 3, then show 3

-- Page 3: rows 7–9 in this ordering
SELECT full_name, city FROM students  -- same projection
ORDER BY student_id ASC              -- same ordering
LIMIT 3 OFFSET 6;                    -- skip first 6, then show 3
```

**How the code works:**

- **`OFFSET = (page_number - 1) × page_size`** for equal-sized pages.
- **Tooling note:** Some browser-based SQL playgrounds **do not** implement **`OFFSET`**. PostgreSQL and Supabase **do**. If **`OFFSET`** errors in a toy compiler, run the same pattern in PostgreSQL / Supabase or your course sandbox.

![ORDER BY sorts result rows, LIMIT caps how many rows you see, OFFSET skips ahead for paging through large slices of data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session15/session15-01-order-limit-offset.png)

---

## Understanding Database Relationships — Why Single Tables Are Not Enough

You may start from one **`students`** table. A real university stack also needs courses, teachers, and marks. One **wide** table repeats the same teacher name on every row — **data redundancy**.

- **Official Definition:** **Data redundancy** means storing the **same fact** in many places. Updates become risky: change the phone number once, miss one row, and reports disagree.
- **In Simple Words:** Write Rahul’s address **once**, point other rows at his **ID**.
- **Real-Life Example:** Exam papers carry a **roll number**, not a full duplicated address block.

### What Is Normalization?

- **Official Definition:** **Normalization** means splitting data into **smaller, focused tables** and linking them so each fact lives in **one logical home**.
- **In Simple Words:** “Don’t repeat yourself” for database columns.
- **Real-Life Example:** Hospital keeps **`doctors`** and **`appointments`**; an appointment row stores **`doctor_id`**, not a full bio every time.

![Heavy redundancy in one wide table versus normalized tables linked by IDs — fewer repeated facts and simpler updates across related records](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session15/session15-02-normalization-redundancy.png)

---

## Types of Relationships Between Tables

Three patterns cover most designs you will see — from banking to agent memory.

### One-to-One Relationship

- **Official Definition:** One row in **Table A** pairs with **at most one** row in **Table B**, and vice versa.
- **In Simple Words:** Strict 1:1 pairing.
- **Real-Life Example:** One citizen, one Aadhaar number (as a teaching analogy).
- **Used in AI:** Splitting sensitive profile fields from public profile fields.

### One-to-Many Relationship

- **Official Definition:** One row in **Table A** links to **many** rows in **Table B**; each **B** row links back to **one** **A** row.
- **In Simple Words:** One parent, many children; each child has one parent.
- **Real-Life Example:** One **customer**, many **orders**.
- **Used in AI:** One **user**, many **chat sessions**.

### Many-to-Many Relationship

- **Official Definition:** Rows on **both** sides can connect to **many** on the other side. You almost always add a **junction (bridge) table** holding pairs of IDs.
- **In Simple Words:** “Many students, many courses” needs an **`enrollments`**-style table in the middle.
- **Real-Life Example:** Students ↔ courses; products ↔ categories.
- **Used in AI:** Users ↔ roles, items ↔ tags.

| Relationship Type | Real-Life Example | Database Pattern |
|---|---|---|
| **One-to-One** | Citizen ↔ Aadhaar | One row in A, one row in B |
| **One-to-Many** | Customer → Orders | One row in A, many rows in B |
| **Many-to-Many** | Students ↔ Courses | Junction table required |

![One-to-one, one-to-many, and many-to-many patterns — including a junction table when both sides need many matches](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session15/session15-03-relationship-types.png)

### Foreign Keys — The Column You Match in Queries

- **Official Definition:** A **foreign key** is a column (or set of columns) in a **child** table that stores the **parent row’s identifier** — the value you must **join on** so combined rows make sense.
- **In Simple Words:** The **`customer_id`** on an **order** row “points back” to **one** row in **`customers`**.
- **Real-Life Example:** Every order line carries “which customer placed this,” not a duplicate copy of the whole customer record.

In class, **`customers.customer_id`** and **`orders.customer_id`** were the **shared bridge** used inside **`JOIN … ON`**.

---

## Querying Relational Data with JOINs

Two related tables raise one question: **how do I read both in one result?** A **JOIN** stitches rows where a **condition** is true — almost always “same ID on both sides.”

- **Official Definition:** A **JOIN** combines rows from two tables using a **related column** (here, **`customer_id`**).
- **In Simple Words:** Merge two spreadsheets on a **shared key column**.
- **Real-Life Example:** A report “customer name + each order line” needs **`customers`** and **`orders`** in one **`SELECT`**.

### Cross Join — Cartesian Product (Why We Avoid It Without a Condition)

The live session first showed what happens when you combine two tables **without** a matching rule: every row from table 1 pairs with **every** row from table 2.

- **Official Definition:** A **cross join** returns the **Cartesian product**: if table 1 has **M** rows and table 2 has **N** rows, you get **M × N** rows.
- **In Simple Words:** “Every customer × every order” — huge, mostly meaningless pairs.
- **Real-Life Example:** Five customers and five orders → **25** rows before any real link logic.

**Full Code — Cross Join (Illustrative):**

```sql
-- Cross join: all customers paired with all orders (M × N rows)
-- Teaching example — usually NOT what you want in production
SELECT *                        -- every column from both tables in the product
FROM customers                  -- left side of the Cartesian product
CROSS JOIN orders;              -- pair each customer row with each order row
```

**How the code works:**

- **`CROSS JOIN`** multiplies the two sets — good to **feel** why we need a **filter**.
- The live demo used a classroom SQL tool that let **`JOIN`** run **without** an **`ON`** clause and printed every combination — that is the **Cartesian** idea. In **PostgreSQL**, use **`CROSS JOIN`** (or the older comma form **`FROM a, b`**) for that product; a plain **`INNER JOIN`** must include **`ON`** (or **`USING`**). Always match syntax to the engine you run against.

### Inner Join — Only Rows That Match on Both Sides

After the cross join intuition, an **inner join** adds a **rule**: keep only rows where **`customers.customer_id = orders.customer_id`**.

- **Official Definition:** An **inner join** keeps rows where the **join condition** is true in **both** tables.
- **In Simple Words:** “Show pairs that actually belong together.” A customer with **no** orders disappears from the result (that is inner join behaviour).
- **Real-Life Example:** Two party guest lists — inner join = people who appear on **both** lists.

The class also tied this idea to a **banking-style** picture: combine **borrower** and **loan** tables on a shared loan key when data is split for normalization.

![INNER JOIN stitches rows where the matching key columns line up across two tables — only pairs that exist on both sides appear in the result](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session15/session15-05-inner-join.png)

### Anatomy of an Inner Join Query

```sql
SELECT columns_you_want                    -- list the columns you need in the result
FROM first_table                           -- start from the first table
INNER JOIN second_table                    -- attach rows from the second table
    ON first_table.shared_column = second_table.shared_column  -- only keep matching keys
WHERE optional_filter;                     -- optional extra filters on the joined row
```

**Full Code — Orders with Customer Names:**

```sql
-- Combine orders with customer details using INNER JOIN
SELECT 
    customers.full_name,          -- customer name from parent table
    customers.city,               -- customer city from parent table
    orders.product_name,          -- product from child table
    orders.amount,                -- order amount from child table
    orders.order_status,          -- lifecycle status from child table
    orders.ordered_at             -- timestamp from child table
FROM orders                       -- fact table: one row per order
INNER JOIN customers              -- bring in matching customer row
    ON orders.customer_id = customers.customer_id;  -- shared key must match
```

**How the code works:**

- **`FROM orders`** — Start from the **fact** table (orders).
- **`INNER JOIN customers ON …`** — For each order, attach the **one** customer row with the same **`customer_id`**.
- **Qualified names** — **`customers.full_name`** avoids ambiguity if both tables had similar column names.

**Full Code — Table Aliases:**

```sql
SELECT 
    c.full_name,                 -- customer name via alias c
    c.city,                      -- customer city via alias c
    o.product_name,             -- product via alias o
    o.amount,                   -- amount via alias o
    o.order_status              -- status via alias o
FROM orders o                   -- o is short for orders
INNER JOIN customers c         -- c is short for customers
    ON o.customer_id = c.customer_id  -- join on shared customer id
ORDER BY c.full_name ASC;      -- sort combined rows by customer name
```

**How the code works:**

- **`o`** and **`c`** are **aliases** — shorter names inside the query.
- **`ORDER BY`** after the join sorts the **combined** result.

**Full Code — Filter After the Join:**

```sql
SELECT 
    c.full_name,                 -- customer name
    c.city,                      -- customer city for the filter below
    o.product_name,             -- product on the order
    o.amount                    -- order amount
FROM orders o                   -- orders alias
INNER JOIN customers c         -- customers alias
    ON o.customer_id = c.customer_id  -- join keys must match
WHERE c.city = 'Mumbai';       -- keep only Mumbai customers after the join

SELECT 
    c.full_name,                 -- customer name
    o.product_name,             -- product name
    o.amount                    -- monetary amount
FROM orders o                   -- orders alias
INNER JOIN customers c         -- customers alias
    ON o.customer_id = c.customer_id  -- join keys must match
WHERE o.amount > 1000.00       -- filter expensive orders
ORDER BY o.amount DESC;       -- highest amounts first
```

**How the code works:**

- **`WHERE`** runs on the **joined** row — you can filter on **either** table’s columns.
- This pattern is how agents fetch “**high-value orders in a region**” in one round trip.

**What is next in SQL (not the focus of this live day):** Other join families (**LEFT**, **RIGHT**, **FULL**) appear in later material; the session stopped after a solid **inner join** plus **cross join** contrast.

---

## How This Applies to AI Applications

### Sorting and Pagination in AI Systems

- Latest thread first: **`ORDER BY started_at DESC LIMIT 1`**.
- Top recommendations: **`ORDER BY score DESC LIMIT 5`**.
- Paged logs: **`LIMIT 20 OFFSET 0`**, then **`OFFSET 20`**, and so on.

### Relationships in Agent Memory

- **One user → many sessions** mirrors **one customer → many orders**.
- **Many users ↔ many courses** still needs a **junction** table in the middle.

### JOINs in Agent Queries

- Pull **user name + session summary** together with **`INNER JOIN`** on **`user_id`**.
- Any “**which X belongs to which Y**” report is the same join pattern you practised with **`customers`** / **`orders`**.

![How sorting, paging, relational models, and JOIN queries show up behind agents, dashboards, and production Supabase backends](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session15/session15-06-sql-in-ai-apps.png)

---

## Key Takeaways

- **`ORDER BY`**, **`LIMIT`**, and **`OFFSET`** control **order**, **size**, and **pages** of a result set — everyday needs for dashboards and agents.
- **Redundancy** and **normalization** explain **why** real schemas split tables instead of one giant sheet.
- **One-to-one**, **one-to-many**, and **many-to-many** (with a **junction** table) describe **how** rows link; **foreign key columns** are what you **match** in **`ON`**.
- **Cross join** shows the **explosion** of meaningless pairs when you forget a condition; **inner join** with **`ON shared_id`** returns only **meaningful** pairs.
- **`LIKE`** with **`%`** / **`_`** extends **`WHERE`** for flexible text filters.
- **Next steps (course / upcoming classes):** Supabase table editor practice, **`INSERT`** order across parents and children, **`ON DELETE CASCADE`**, and **Python ↔ database** code paths follow in your roadmap and shared docs.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `ORDER BY` | SQL Clause | Sorts results; **`ASC`** = ascending, **`DESC`** = descending |
| `LIMIT` | SQL Clause | Caps how many rows are returned |
| `OFFSET` | SQL Clause | Skips rows before **`LIMIT`**; used for pagination |
| `LIKE` | SQL Operator | Pattern match in **`WHERE`**; **`%`** any substring, **`_`** one character |
| `CROSS JOIN` | SQL Join | Cartesian product — every left row × every right row |
| `INNER JOIN` | SQL Join | Keeps only rows that satisfy the **`ON`** condition in both tables |
| `ON` | SQL Keyword | Join condition between two tables |
| **Relationship** | Concept | Logical link between tables via shared identifiers |
| **One-to-One** | Relationship Type | One row in A ↔ one row in B |
| **One-to-Many** | Relationship Type | One row in A → many rows in B (most common) |
| **Many-to-Many** | Relationship Type | Many↔many; needs a **junction** table |
| **Junction Table** | Concept | Bridge table storing pairs of foreign keys |
| **Normalization** | Concept | Split tables to reduce repeated facts |
| **Data Redundancy** | Concept | Same data copied in many rows — risky on updates |
| **Foreign Key** | Concept | Child column storing the parent row’s ID for joins |
| **Alias** | SQL Concept | Short table nickname (`FROM orders o`) |
| **Pagination** | Concept | **`LIMIT` + `OFFSET`** (or equivalent) for pages |
