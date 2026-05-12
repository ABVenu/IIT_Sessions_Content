# Subjective Assignment — Introduction to Databases for AI Systems

## Instructions
- This assignment has **1 practical task**.
- Read all parts of the question carefully before you begin.
- Follow the submission instructions provided at the end.

---

### Question 1 *(Medium | Practical Task — SQL Schema Design & Implementation in Supabase)*

**Context:**

You have joined a small startup building **"BookMind"** — an AI-powered book recommendation platform. The platform needs a database to track its book catalog, registered readers, and each reader's reading history. This reading history will eventually be used to power personalised recommendations using semantic search.

Your task is to design and implement this database from scratch inside your Supabase project.

---

**Part 1 — Create the Database Schema**

Write and execute `CREATE TABLE` statements in the Supabase SQL Editor to create the following three tables. Apply appropriate data types and constraints as described:

**Table 1: `books`** — stores the platform's book catalog

| Column | Type | Constraints / Notes |
|---|---|---|
| `book_id` | `SERIAL` | Primary Key — auto-assigned |
| `title` | `VARCHAR(200)` | NOT NULL |
| `author` | `VARCHAR(100)` | NOT NULL |
| `genre` | `VARCHAR(50)` | NOT NULL |
| `published_year` | `INT` | CHECK: must be greater than 1800 |
| `is_available` | `BOOLEAN` | DEFAULT TRUE |

**Table 2: `readers`** — stores reader profiles

| Column | Type | Constraints / Notes |
|---|---|---|
| `reader_id` | `SERIAL` | Primary Key — auto-assigned |
| `full_name` | `VARCHAR(100)` | NOT NULL |
| `email` | `VARCHAR(150)` | UNIQUE, NOT NULL |
| `joined_on` | `DATE` | DEFAULT CURRENT_DATE |

**Table 3: `reading_history`** — tracks which reader read which book

| Column | Type | Constraints / Notes |
|---|---|---|
| `reader_id` | `INT` | Part of Composite Primary Key |
| `book_id` | `INT` | Part of Composite Primary Key |
| `read_on` | `DATE` | DEFAULT CURRENT_DATE |
| `rating` | `INT` | CHECK: must be between 1 and 5 (inclusive) |

> **Note:** `reading_history` must use a **composite primary key** on `(reader_id, book_id)` — this ensures one reader can only have one history entry per book.

---

**Part 2 — Insert Sample Data**

Write and execute `INSERT INTO` statements to populate the tables:

1. Insert at least **4 books** into the `books` table (use real or fictional book titles with realistic data)
2. Insert at least **2 readers** into the `readers` table
3. Insert at least **3 entries** into the `reading_history` table, linking your readers to books they have "read" with a rating between 1 and 5

**Constraint Violation Test:**
- Attempt to insert one entry into `reading_history` with a `rating` value of **`6`**
- Observe the error message returned by Supabase — this confirms your `CHECK` constraint is working

---

**Submission Instructions:**

- Open your **Supabase project** → go to the **SQL Editor**
- Write all your SQL queries (all `CREATE TABLE` statements, all `INSERT INTO` statements, and the failed constraint violation insert)
- Run each query and verify the tables are created and populated correctly
- Once verified, copy **all your SQL queries** and paste them into the **answer box** in the LMS
- Make sure your submission includes all three parts: the CREATE TABLE statements, the INSERT INTO statements, and the constraint violation attempt

---

## Answer Explanation / Ideal Solution

### Part 1 — Ideal `CREATE TABLE` Statements

```sql
-- Table 1: books catalog
CREATE TABLE books (
    book_id        SERIAL PRIMARY KEY,
    title          VARCHAR(200) NOT NULL,
    author         VARCHAR(100) NOT NULL,
    genre          VARCHAR(50)  NOT NULL,
    published_year INT          CHECK (published_year > 1800),
    is_available   BOOLEAN      DEFAULT TRUE
);

-- Table 2: reader profiles
CREATE TABLE readers (
    reader_id  SERIAL PRIMARY KEY,
    full_name  VARCHAR(100) NOT NULL,
    email      VARCHAR(150) UNIQUE NOT NULL,
    joined_on  DATE DEFAULT CURRENT_DATE
);

-- Table 3: reading history with composite primary key
CREATE TABLE reading_history (
    reader_id INT,
    book_id   INT,
    read_on   DATE DEFAULT CURRENT_DATE,
    rating    INT  CHECK (rating >= 1 AND rating <= 5),
    PRIMARY KEY (reader_id, book_id)
);
```

**Walkthrough:**
- `books` uses `SERIAL PRIMARY KEY` so `book_id` is auto-assigned (1, 2, 3…). `published_year` has a `CHECK` to block impossible years. `is_available` defaults to `TRUE` — no need to specify it when inserting most books.
- `readers` uses `UNIQUE NOT NULL` on `email` — every reader must have one and no two readers can share an email address.
- `reading_history` has **no auto-generated ID** — instead, the combination of `reader_id` and `book_id` together forms the primary key. This means the same reader cannot have two history entries for the same book. The `CHECK` on `rating` blocks any value outside 1–5.

---

### Part 2 — Ideal `INSERT INTO` Statements

```sql
-- Insert books
INSERT INTO books (title, author, genre, published_year)
VALUES
    ('Atomic Habits',        'James Clear',       'Self-Help',       2018),
    ('The Alchemist',        'Paulo Coelho',       'Fiction',         1988),
    ('Deep Work',            'Cal Newport',        'Productivity',    2016),
    ('Educated',             'Tara Westover',      'Memoir',          2018),
    ('Sapiens',              'Yuval Noah Harari',  'Non-Fiction',     2011);

-- Insert readers
INSERT INTO readers (full_name, email)
VALUES
    ('Ananya Sharma', 'ananya@example.com'),
    ('Rohan Mehta',   'rohan@example.com');

-- Insert reading history (reader 1 read books 1, 2, 3 | reader 2 read book 1)
INSERT INTO reading_history (reader_id, book_id, rating)
VALUES
    (1, 1, 5),
    (1, 2, 4),
    (1, 3, 3),
    (2, 1, 4);

-- Constraint violation test — this INSERT should FAIL
INSERT INTO reading_history (reader_id, book_id, rating)
VALUES (2, 2, 6);
-- Expected error: new row for relation "reading_history" violates check constraint "reading_history_rating_check"
```

**Walkthrough:**
- `book_id`, `reader_id` are not specified during insert — `SERIAL` assigns them automatically (1, 2, 3…).
- `joined_on` and `read_on` are not specified — their `DEFAULT CURRENT_DATE` fills in today's date automatically.
- `is_available` is not specified — it defaults to `TRUE` for all books.
- The final insert with `rating = 6` violates `CHECK (rating >= 1 AND rating <= 5)`, so Supabase rejects the row entirely and returns a constraint violation error. No partial data is stored.

---

### Alternative Approaches

- **UUID instead of SERIAL:** For a production BookMind platform operating at global scale (or merging data across multiple regional servers), `book_id` and `reader_id` should be `UUID DEFAULT gen_random_uuid()` instead of `SERIAL`. This prevents ID collisions if records are created on different servers and later merged.

- **Foreign keys in `reading_history`:** In a production schema, the `reader_id` and `book_id` columns in `reading_history` should have `FOREIGN KEY` references to `readers(reader_id)` and `books(book_id)` respectively. This ensures you cannot insert a reading history entry for a reader or book that doesn't exist. Foreign keys were introduced in the session but not applied here to keep the task at medium difficulty.

- **BETWEEN shorthand for rating CHECK:** The constraint `CHECK (rating BETWEEN 1 AND 5)` is equivalent to `CHECK (rating >= 1 AND rating <= 5)` and is slightly more readable. Both are valid.

- **Inserting multiple rows in one statement:** All four `reading_history` inserts above use a single `INSERT INTO ... VALUES (row1), (row2), ...` — this is more efficient than four separate `INSERT` statements and is considered better practice.
