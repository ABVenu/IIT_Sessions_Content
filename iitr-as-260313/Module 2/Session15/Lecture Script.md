# Lecture Script: Using SQL Databases with AI Applications

**Session Duration:** 2 hours 15 minutes (135 minutes)  
**Audience:** Absolute beginners — Indian students who may have no formal tech background; comfortable guiding them through Supabase UI and copying SQL safely.

---

**How to use this file**  
Use this script for **timing, room flow, and facilitation only**. It does not replace the detailed explanations in `Lecture Notes.md`; keep lecture notes open for definitions, full SQL snippets, and diagrams.

---

**Break rule**  
After roughly **60–75 minutes** of instruction (typically after completing the relationships + designing tables segments, before or immediately after heavy JOIN practice), pause for **one** break of **5–8 minutes**. Do **not** count the break inside the numbered blocks below — resume with the bridge for the next block.

---

## 1. Welcome, Agenda, CRUD recap (10 minutes)

- Briefly greet the cohort; remind them Sessions 13–14 set up SQL vocabulary, Supabase, and single-table CRUD (`CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE`).
- Screen-share the session outcomes from lecture notes — today moves from **one table** to **related tables** and **JOINs**.
- Flash the recap table (`CREATE TABLE` through `WHERE`); linger on the **golden rule**: always use `WHERE` with `UPDATE` and `DELETE`.
- **Check for thumbs-up:** “Thumbs up if you still have Session 14’s Supabase project open — if not, open it during the next exercise.”
- Circulate briefly; glance at student SQL editors for typo patterns.

**Bridge sentence:** “Single-table CRUD was the foundation — now we teach the database **how results are ordered**, **how many rows come back**, and **how pages of data work**, because every app-facing list uses that trio.”

---

## 2. ORDER BY, LIMIT, OFFSET — live control of result sets (22 minutes)

- Use the music-stream / Zomato / Google / Flipkart analogies from the notes to anchor intuition before SQL.
- **Live-code** in Supabase SQL Editor (or duplicate your screen onto theirs): sort `students` with `ASC` / `DESC`, then multi-column `ORDER BY`; add `LIMIT`, then **`ORDER BY` + `LIMIT`** for “top N.”
- Walk pagination: Page 1 / 2 / 3 with **`LIMIT … OFFSET`**; write the formula on the slide or board: offset = `(page − 1) × page_size`.
- Show the lecture diagram image (**session15-01-order-limit-offset**) if bandwidth allows — point at each clause’s role once.
- **Pair-share (90 seconds):** “With your neighbour, name one real screen (app or website) that is clearly using sort + cap or paging.”
- Pause for one **cold-call:** “Someone tell me offset for **page 4** if **page size is 3**.” *Answer: 9.*

**Bridge sentence:** “Sorting and paging control **presentation** — but production systems also split data across tables; next we motivate **why one giant table hurts**.”

---

## 3. Redundancy, normalization, relationships, referential integrity (22 minutes)

- Story: university AI system — repeat teacher rows → **data redundancy**; contrast “roll number references one address record.”
- Define **normalization** in plain language (“don’t repeat yourself” across rows); optional quick show of **session15-02** diagram.
- Teach **three relationship types** with Indian examples notes use (e.g., Aadhaar 1:1, customer→orders 1:many, student↔course + junction for many-many). Show relationship summary table / **session15-03** image.
- **Referential integrity:** ghost `customer_id` thought experiment; show **session15-04**.
- **Check for thumbs-up:** “Thumbs up if you can explain in one sentence why we need a **junction table** for many-to-many.”

**Bridge sentence:** “We have the vocabulary — time to **build** the classic parent-child pattern in Supabase: **customers** and **orders** linked by a **foreign key**.”

---

## 4. Design `customers` and `orders`; inspect FK in dashboard (18 minutes)

- **Live-code Step 1** — create `customers` (`SERIAL PRIMARY KEY`, `NOW()` default commentary).
- **Live-code Step 2** — create `orders` with named `fk_customer`, `DECIMAL(10,2)` for money, **`ON DELETE CASCADE`** — pause to ask *why* child rows might disappear when parent disappears.
- Instruct learners to **run the scripts** alongside you; **circulate**: check `NOT NULL`, comma errors, constraint name typos.
- Supabase UI: **Database → Tables**, open `orders`, show FK linkage / Table Editor hints as in notes.


**Bridge sentence:** “The schema exists — inserting data is now a **ordering problem**: parents first, children second, or the FK will reject you.”

---

## 5. Inserts across related tables; INNER JOIN and filters (33 minutes)

- **Students run** inserts: four customers then six orders; celebrate Ananya/Priya having two orders (1:many viscerally).
- **Deliberately bad insert (demo only):** `customer_id = 99` → read error aloud; emphasize **referential integrity** rejecting ghosts.
- **JOIN concept** before syntax: two spreadsheets stitched on shared ID; show **session15-05** INNER JOIN illustration.
- **Live-code** full INNER JOIN (“all orders + customer names”); rerun with **aliases** `o`/`c`; add `ORDER BY c.full_name`.
- Second demo: **`WHERE`** on joined result — Mumbai customers; then high `amount` orders with `ORDER BY o.amount DESC`.
- **Cold-call:** “Which table did we filter for Mumbai — **`c`** or **`o`**?”
- Pair desks to compare row counts vs expectations after each query.

**Bridge sentence:** “Reading across tables with JOIN is the daily bread of apps — writing **safely** (updates, deletes, cascades) is what keeps prod data trustworthy.”

---

## 6. CRUD on related data; CASCADE vs RESTRICT; intentional failures (17 minutes)

- **`UPDATE`** order status with extra `AND customer_id = …` safety; **`UPDATE`** customer email — tie back to normalization (IDs propagate).
- **`DELETE`** one order vs **`DELETE`** customer Karan (`customer_id = 4`) → **CASCADE** cleanup; **`SELECT`** verify zero orphan rows for that customer id.
- Contrast verbally: **`ON DELETE RESTRICT`** would block deleting a parent until children go away.
- Show the scripted **failed `INSERT`** and **`DELETE`** examples from notes — leave error text visible 10 seconds for slower typists to read.
- **Thumbs:** “If I delete parent with CASCADE children, thumbs up means you agree child rows should disappear; sideways if unsure.” Briefly acknowledge both.

**Bridge sentence:** “Patterns you used today are the same patterns **agents**, dashboards, and Supabase backends use — let me map jargon to YOUR job as builders.”

---

## 7. AI applications tie-in; takeaways; command cheat mentally; close (13 minutes)

- Rapid-fire map from notes: **ORDER BY … LIMIT …** for latest chat / top‑K recs / paged feeds; **1:many** user→sessions; **many-many** recommendations via junction; **`INNER JOIN`** for “who + summary in one round trip.”
- Optional flash **session15-06** “SQL in AI apps” composite image.
- Read **Key Takeaways** bullet list verbatim or paraphrase; point to glossary table for homework review.
- Tease **next session:** Python (or programmatic) connection to Supabase — running today’s queries from code.
- 2-minute **open mic** (“one question stripe”); acknowledge parking-lot topics.

**Bridge sentence:** *None — session ends.*

---

## Timing flex (running late — what to trim)

**Cut-first (save ~25–35 min total):**  
- Replace relationship deep-dive (Block 3) with **10-minute whistle-stop**: only 1:many + junction sketch; defer 1:1/`DECIMAL`/constraint naming detail to reading.  
- In Block 5, **one** INNER JOIN demo only (skip alias variant or skip second `WHERE` example).  
- In Block 6, demonstrate CASCADE delete **or** failed inserts — not both narratives in full.

**Sacrifice last if desperate:** shorten Block 7 to **five minutes**: one AI mapping example + takeaway bullets + “read glossary at home”; drop open mic.

**Never drop:** FK parent-first insert ordering, INNER JOIN **`ON`** condition, and the idea that **`WHERE`** still protects `UPDATE`/`DELETE`.

---
