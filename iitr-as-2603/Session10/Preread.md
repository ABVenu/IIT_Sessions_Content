# Pre-read: From Excel Brain to Database Brain — Your First SQL Queries

Imagine lakhs of people trying to book a train seat at the same second. If every booking lived only in one person’s laptop file, seats would clash, data would vanish when the laptop shut down, and nobody could trust the system. Companies do not run on lone spreadsheets — they run on **databases**: permanent, shared, fast stores of truth. This session is your first step into that world.

**What if** you had to answer “Who are our top three highest-paid people in Delhi?” from a table with thousands of employees — and you had to do it again tomorrow, and the day after, without opening every row by hand? Doing it manually does not scale. You need a way to **ask the computer in clear language** and get only the rows you care about, in the order you want.

That “language” for talking to relational databases is **SQL** (Structured Query Language). We will use it to **read** data with `SELECT`, **narrow** it with `WHERE`, **sort** with `ORDER BY`, and **cap** long lists with `LIMIT` — the same mental steps you already know from pandas, but where the data lives in a proper database table.

**Think of it like a library.** The database is the librarian with lakhs of books in the back. You do not run through every shelf. You simply say, in effect: “Show me only these columns, only rows that match this rule, sorted this way, and stop after the first few.” SQL is that polite, precise sentence to the librarian.

**SQL** is just the standard way we **request** information from tables (rows and columns, like a serious Excel sheet stored safely on disk). **SELECT** means “show me these fields.” **WHERE** means “only rows that pass this test” — like a guard at a gate who lets in only visitors who match your rule. You will see how these pieces fit in one fixed order: what to show, which table, which rows, how to sort, how many to return.

**Interesting questions** we will crack in the live session:

- How is a database different from pandas or Excel when data must last forever and serve many users at once — and why does that matter for jobs in data and analytics?
- How do you write one short SQL query to get “top N” answers (for example, highest salaries in a city) instead of scrolling and sorting by hand?
- How does the **same** question look in SQL versus pandas — so you can switch between them without learning two different ways of thinking?

**After this session, you will be able to:**

- Explain in plain words **why** databases exist and what **SQL** is for.
- Read from a table using **`SELECT`**, pick columns, use **`DISTINCT`**, and filter with **`WHERE`** (including **AND**, **OR**, **BETWEEN**, **IN**, **LIKE**, and missing values).
- Sort results with **`ORDER BY`** and take only the first few rows with **`LIMIT`**, and relate these steps to the pandas you already know.

Come curious — we start from “why databases,” end with queries you can run in tools like MySQL Workbench, and use one **`employees`** table all through so cause and effect stay crystal clear.
