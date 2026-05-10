# Lecture Script: SQL: Aggregation and Joining Tables

**Session duration:** 2 hours 15 minutes  
**Audience:** Learners from diverse backgrounds; many may have limited prior tech experience (Indian classroom context)

**How to use this file:** This document is for *timing and facilitation only*. It is not a substitute for the detailed explanations and examples in the lecture notes. Use it to plan pacing, room moves, and engagement checks—then teach from your notes and live environment.

**Break rule:** After roughly 60–75 minutes of instruction, take **one** pause of about **5–8 minutes** (not counted as a numbered block). Do not fragment the session with multiple small breaks unless your programme requires it.

---

## 1. Opening, Recap, and the “Why” of Aggregation (8 minutes)

- Screen-share the session title and (briefly) the learning line: from *finding* rows to *summarising* and *combining* tables.
- In one minute, cold-call: *“In one line: what did we use `WHERE` for last time?”* Accept short answers; affirm.
- Set up the **tea-stall** metaphor from the notes—end-of-day questions without reading every row.
- Show the **aggregation** diagram (many rows → one number) if you have it in slides or notes; point, don’t read the slide.
- **Students do:** Thumbs up if they have SQL client / notebook open; quick scan to spot who needs help with environment.

**Bridge sentence:** *“We’ve said what aggregation is for—now we name the tools: the aggregate functions.”*

---

## 2. Aggregate Functions: COUNT, SUM, AVG, and MAX / MIN (12 minutes)

- Live-code or live-type: `COUNT(*)` vs `COUNT(column)` on a simple `orders`-style table; narrate the NULL behaviour as you go.
- Run `SUM` and `AVG` on one numeric column; add `MAX` / `MIN` in the same small example so they see the pattern.
- **Check for understanding:** *“Thumbs up if `COUNT(delivery_date)` can ever be larger than `COUNT(*)` for the same table.”* (Thumbs down = larger; discuss why that’s false.)
- **Pair-share (2 minutes):** Neighbour pairs—one person says *when* they’d use `COUNT(*)`, the other *when* they’d use `COUNT(column_name)`; then switch.
- Circulate: glance at 4–5 screens to confirm the queries run.

**Bridge sentence:** *“One big total is useful—but business questions are usually *per* customer, *per* city. That’s GROUP BY.”*

---

## 3. GROUP BY and the “Golden Rule” (14 minutes)

- Draw or screen the **buckets** image: groups first, then aggregate *inside* each group.
- State the **golden rule** clearly; write it on the board or show it in the editor as a comment.
- Live-code: `SELECT customer_id, SUM(order_amount) … GROUP BY customer_id`—intentionally show the **forgotten GROUP BY** error once, then fix it. Students remember the fix.
- Add `ORDER BY` on the grouped result (e.g. `avg_order_value DESC`) so they see a readable report.
- **Cold-call:** *“I have `customer_id` and `SUM(order_amount)` in SELECT—what must appear in GROUP BY?”*

**Bridge sentence:** *“We can filter *rows* with WHERE—next we filter *groups* after we’ve aggregated.”*

---

## 4. HAVING, WHERE vs HAVING, and SQL Execution Order (16 minutes)

- Contrast: WHERE = door check on rows; HAVING = check on the **result of grouping** (use a simple analogy: party / groups—keep the notes’ framing light).
- Live-code: `HAVING COUNT(*) > 3` and `HAVING SUM(order_amount) > …` on the same table they’ve been using.
- Then **combine** `WHERE` + `GROUP BY` + `HAVING` (e.g. year filter) in one short example.
- Walk through **execution order** (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT) slowly; show the **execution-order** image if available. Say explicitly: *“This is not the order you type—but the order the engine *thinks* in.”*
- **Engagement:** Quick **hand vote**: *“If I want to throw away rows *before* grouping, is that WHERE or HAVING?”* / *“If I want to keep only groups with average above X, is that WHERE or HAVING?”*

**Bridge sentence:** *“We’ve stayed on one table so far. Real data is split across tables—so we *join*.”*

---

*— Take the **single** 5–8 minute break here if you are at ~60–75 minutes. Reset screens; remind them what comes next: keys and JOINs. —*

---

## 5. Why Multiple Tables, Keys, and the Idea of a JOIN (12 minutes)

- Short story: `customers` vs `orders`—redundancy and inconsistency; introduce **primary key** and **foreign key** with the **bridge** image (keys linking tables).
- **Students do:** 30 seconds—think of *any* real ID that links two “lists” in life (Aadhaar, roll number, order ID); cold-call 2–3.
- Set expectation: next blocks are **INNER** vs **LEFT**—different questions, different results.

**Bridge sentence:** *“A JOIN is not magic—it’s *match the key*. Inner join: only when both sides match.”*

---

## 6. INNER JOIN and Table Aliases (14 minutes)

- Live-code the full `FROM orders INNER JOIN customers ON …` with **prefixed** column names, then refactor to `AS o` / `AS c`.
- Emphasize: the **ON** clause is the only place the relationship is stated; result is “wider” rows.
- **Pair-share:** *“In plain language: what does INNER join *drop*?”* (Rows that don’t have a match on both sides—neighbour check.)
- Circulate while they run a copy of the query; help with typos in `ON` and duplicate column names.

**Bridge sentence:** *“Sometimes you need *every* row on the left—even when the right has nothing. That’s LEFT JOIN.”*

---

## 7. LEFT JOIN, NULLs, and the “Never Ordered” Pattern (14 minutes)

- Live-code `LEFT JOIN` and point at **NULL** in right-hand columns.
- Then add `WHERE o.order_id IS NULL` and slow down: this is a **known interview pattern**—say it once, clearly.
- Show **INNER vs LEFT** diagram; one sentence: *“Same keys, different *keep* rules.”*
- **Thumbs up:** *“Thumbs up if you think a customer with two orders can appear in *two* rows in a left join to orders.”* (Clarify if needed.)

**Bridge sentence:** *“Real systems chain many tables—orders, line items, products. That’s the same join idea repeated.”*

---

## 8. Multi-Table JOINs and Aggregation + JOIN (12 minutes)

- Live-code a **three- or four-table** chain (customers → orders → order_items → products) at a pace they can type along or paste.
- Show **LEFT JOIN** + `GROUP BY` + aggregates for “per customer” totals (from notes); call out why **both** `customer_id` and `customer_name` are in `GROUP BY` if both are in `SELECT`.
- **Cold-call:** *“Why might we use LEFT here instead of INNER if the question is ‘spend per customer’?”* (E.g. include zero spenders—depends on business question; brief.)

**Bridge sentence:** *“If you know pandas, you’re not learning a new brain—just new spelling.”*

---

## 9. Pandas map: `groupby` and `merge` (10 minutes)

- Show the two summary tables (pandas vs SQL) from the notes—**do not** read every cell; highlight one row in each.
- Optional: run the small pandas snippet **or** the SQL version—your choice based on time; the point is *same story*.
- **Pair-share:** *“Name one thing that’s the *same* between `merge` and `JOIN`.”* (Matching on keys.)

**Bridge sentence:** *“We’ll put everything in one business-shaped query—Mumbai, totals, HAVING, sort.”*

---

## 10. Capstone Query, Key Takeaways, and Next Session Hook (15 minutes)

- Build or step through the **Mumbai + spend > 20000** query **line by line**: JOIN → WHERE → GROUP BY → HAVING → ORDER BY—tie back to **execution order**.
- Rapid **takeaways** from the notes (aggregates, GROUP BY rule, HAVING, INNER vs LEFT, pandas mapping)—bullet speed-round, not a second lecture.
- Tease next sessions: subqueries, window functions, SQL from Python—one sentence each.

**Bridge sentence:** *“We stop here for content—use the last minutes for questions and a quick self-check.”*

---

## 11. Q&A, Screen Checks, and Exit (8 minutes)

- Open floor; prioritise *misheard* topics: **GROUP BY list**, **WHERE vs HAVING**, **INNER vs LEFT**.
- If time remains: 2–3 **minute** on “one thing you will try on your data before next class” (think–pair–share, no need to report out).
- Remind them where the **lecture notes** and **term glossary** live; thank the room.

**Bridge sentence:** *N/A (final block).*

---

## Timing flex — if the session is running long

- **Shorten first:** Pandas block (9) to **5 minutes** (tables only, no live run—or SQL-only demo).  
- **Cut or trim:** second **pair-share** in block 2; capstone **narrated** from a slide instead of live-typed.  
- **Do not drop:** GROUP BY golden rule, WHERE vs HAVING, INNER vs LEFT, and one **chained** multi-table example—these are the non-negotiables for the learning objective.  
- If still over: end block 11 early and assign “read takeaways + run one HAVING example” as async follow-up.
