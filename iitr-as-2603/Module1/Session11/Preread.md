# Pre-read: SQL: Aggregation and Joining Tables

Imagine you are the manager of a grocery chain with stores across five cities in India. Every day, thousands of transactions happen — customers buying rice, pulses, snacks, and vegetables. At the end of the month, your boss walks in and asks: *"Which city made the most revenue this month? Which product category is underperforming? Are there customers who shopped more than five times but never crossed ₹500 in total spend?"*

You have the raw data — millions of rows sitting in a database. But raw data is just noise until you summarise it. That summary is where real decisions get made.

---

Now take it one step further. Your grocery chain keeps data in separate files — one for customer details (name, city, phone), another for transactions (date, amount, product), and a third for product information (category, price, supplier). None of these files alone can answer your boss's question. You need to *connect* them and *summarise* them at the same time.

Doing this manually in Excel would take hours. With SQL, it takes a few lines.

---

The two superpowers you pick up in this session are **aggregation** and **joins** — and together, they transform you from someone who can *fetch* data into someone who can *analyse* data.

Think of aggregation like your school report card. Your school did not hand you 365 daily attendance entries — it handed you one number: 89% attendance. That single number was produced by *collapsing* 365 rows into one summary. SQL does the exact same thing using functions like COUNT, SUM, AVG, MAX, and MIN.

Joins work differently. Think of your Aadhaar number. The government stores your name and address in one file, and your financial records in a completely separate file. Your Aadhaar number is the link that connects both files whenever needed. A SQL JOIN does precisely this — it uses a shared column (called a **key**) to stitch two tables together so you can ask questions that span both.

---

**In this pre-read, you'll discover:**

- How aggregate functions like COUNT, SUM, AVG, MAX, and MIN collapse many rows into one meaningful number
- How GROUP BY lets you break that summary down by category — total revenue *per city*, or average order value *per customer*
- How HAVING acts as a filter for groups, because regular WHERE cannot filter on summarised results
- How INNER JOIN and LEFT JOIN connect two tables using a shared key column — and what the difference between the two means in practice

---

Here is where most beginners get stuck — and why this session matters.

Fetching data is straightforward: *"Show me all orders from Mumbai."* But real business questions are never that simple. They sound like: *"Show me only customers from Mumbai who placed more than three orders and spent over ₹20,000 in total."* To answer that, you need to join two tables, filter rows, group by customer, calculate totals, and then filter on those calculated totals — all in one query.

None of that is possible with just SELECT and WHERE. GROUP BY, HAVING, and JOIN need to work together — which is exactly what this session is about.

---

There is one more thing that surprises almost every beginner: **SQL does not execute your query in the order you write it.** You write SELECT first, but SQL actually runs FROM first, then WHERE, then GROUP BY, then HAVING, then SELECT, and finally ORDER BY.

This matters more than it sounds. It explains *why* you cannot use WHERE to filter on a number you just calculated with SUM or COUNT — because WHERE runs *before* the grouping even happens. HAVING, on the other hand, runs *after* grouping. Knowing this one rule saves hours of debugging and is a favourite topic in data analyst interviews.

---

If you have used Python's pandas library before, there is good news: you already understand the logic. SQL's GROUP BY maps directly to pandas' `groupby()`, and SQL's JOIN maps directly to pandas' `merge()`. The concepts are identical — only the syntax changes. By the end of this session, you will be able to move between the two comfortably.

---

**After this session, you'll be able to:**

- Write queries that count, sum, and average data across thousands of rows instantly
- Use GROUP BY to produce per-category summaries — by city, by product, by customer
- Filter aggregated results with HAVING — a skill that appears in almost every SQL interview
- Connect two or more tables using INNER JOIN and LEFT JOIN, and know when to use which
- Build multi-step queries that answer real business questions end to end

---

Before you walk into the session, sit with these for a few minutes:

1. A supermarket wants to find all product categories where total sales this quarter were *below ₹1,00,000*. Which SQL clauses would you need — and can you figure out the order they should run in?

2. An HR team has two tables: one with all employee details, and one with performance review scores. Some employees never received a review. If you want a list of *all* employees with their score shown (and a blank for those without a review) — which type of JOIN would you use, and why not the other type?

3. You write a query using WHERE to keep only customers whose total orders exceed 5, but SQL throws an error. What is the most likely reason — and which clause would fix it?

These are the exact questions the session will unpack step by step, with real examples and code you can run yourself. Come ready to think in summaries and connections.
