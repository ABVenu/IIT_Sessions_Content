# Lecture Script: Using SQL Databases with AI Applications

**Session duration:** 2 Hours 15 Minutes (instruction-focused; excludes the one structured pause below)  
**Audience:** Absolute beginners — Indian learners, minimal prior tech exposure; hands-on Supabase SQL Editor

**Break rule:** After roughly 60–75 minutes of instruction (recommended: after completing the block on normalization, relationships, and referential integrity, or immediately before the heavy Supabase live-build if the cohort needs energy earlier), take **one** pause of **5–8 minutes**. Do **not** treat the break as a numbered teaching block — resume with the bridge sentence into the next block.

**How to use this document:** This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Use it to manage flow, screen sharing, room checks, and engagement; keep the detailed definitions and SQL examples on the notes or in the editor.

---

## 1. Opening, outcomes, and CRUD recap (8 minutes)

- **You:** Welcome; state the session title and the three big ideas: control how rows come back (`ORDER BY` / `LIMIT` / `OFFSET`), understand **why** data splits across tables, then **join** and maintain **referential integrity** with foreign keys.
- **You:** Quick table walk — `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `WHERE` — one line each; stress the golden rule: always pair `WHERE` with `UPDATE` and `DELETE`.
- **Students:** In chat or verbally, one example each of a filter they remember from last session (`LIKE`, `BETWEEN`, or `IN`); cold-call 2–3 volunteers.
- **You:** Bridge from “one table” to “today we connect tables and sort/page results.”
- **Room action:** Share screen on speaker notes or Supabase home; glance at a few student screens to confirm they can open the SQL Editor.

**Bridge sentence:** “We already read and filter one table — next we control *order and volume* of what comes back before we tackle multiple tables.”

---

## 2. ORDER BY, LIMIT, and OFFSET — live queries (22 minutes)

- **You:** Explain `ORDER BY` with the streaming-app analogy; live-code `ASC` / `DESC` and multi-column sort on `students` (or your cohort table).
- **Students:** Type the same queries; **check for thumbs up** once basic sort runs.
- **You:** Introduce `LIMIT` as “top N”; combine `ORDER BY` + `LIMIT` for “most recent enrollment” pattern.
- **You:** Introduce `OFFSET` with Flipkart paging; live-code page 1 / page 2 / page 3 with `LIMIT 3 OFFSET 0`, `OFFSET 3`, `OFFSET 6`; write the formula `OFFSET = (page − 1) × page_size` on the board or slide.
- **Students:** **Pair-share (2 minutes):** One partner says a real app feature (“show latest message”), the other names which clause (`ORDER BY` / `LIMIT` / `OFFSET`) fits.
- **Room action:** Walk the room; fix typos and comma order (`ORDER BY` before `LIMIT`/`OFFSET` in PostgreSQL style you’re using).

**Bridge sentence:** “Sorted, capped, paged results are table stakes in apps — now let’s ask why we don’t stuff everything into one giant table.”

---

## 3. Normalization, redundancy, relationship types, and referential integrity (20 minutes)

- **You:** Use the university / teacher-phone example — **data redundancy** and update pain; define **normalization** in plain language (“don’t repeat yourself; one fact, one place”).
- **Students:** **Cold-call:** “Customer → orders — one-to-one, one-to-many, or many-to-many?” (one-to-many). Second cold-call: “Students ↔ courses?” (many-to-many → junction table).
- **You:** Cover one-to-one (Aadhaar), one-to-many (customer/orders), many-to-many (enrollments); show the summary table from the lecture notes if projected.
- **You:** Define **referential integrity** — foreign key must point to a real parent; connect to AI context (sessions linked to users, no “ghost” IDs).
- **Room action:** Stay at the front for definitions; use the session diagrams (normalization, relationship types, referential integrity) if available — quick pass, not a read-aloud.

**Bridge sentence:** “Theory only matters if the database enforces it — we’ll build `customers` and `orders` in Supabase and let the constraint do the policing.”

---

## 4. Supabase — create `customers` and `orders` with a foreign key (22 minutes)

- **You:** Screen-share Supabase → SQL Editor; create `customers` first (parent); narrate `SERIAL`, `UNIQUE`, `DEFAULT NOW()` briefly.
- **Students:** Run the same script; **thumbs up** when `customers` exists with no errors.
- **You:** Create `orders` with named `CONSTRAINT fk_customer`, `FOREIGN KEY … REFERENCES customers(customer_id)`, **`ON DELETE CASCADE`**; explain what breaks without FK (phantom `customer_id`).
- **You:** Open **Database → Tables** and **Table Editor**; point at the visible link / FK in the inspector — “this is the same relationship in the UI.”
- **Room action:** Circle the room; catch students who run `orders` before `customers`; help with copy-paste and semicolons.

**Bridge sentence:** “Parent rows must exist before children — we’ll insert customers first, then orders, in that strict order.”

---

## 5. Inserts across related tables (10 minutes)

- **You:** Run `INSERT INTO customers …` batch; then `INSERT INTO orders …` with matching `customer_id` values; highlight Ananya/Priya having multiple orders (the “many” side).
- **Students:** Mirror inserts; verify row counts in Table Editor.
- **You:** Optional quick **cold-call:** “What happens if I insert `customer_id = 99`?” — let them predict, then show the FK error **if time** (or tease block 8).
- **Room action:** Confirm no one skipped the customer insert sequence.

**Bridge sentence:** “We have split data and we’ve enforced links — now we need one query that *stitches* name and order lines together.”

---

## 6. INNER JOIN — anatomy, aliases, and WHERE on joined data (22 minutes)

- **You:** “Two spreadsheets merged on a shared ID” analogy; show the generic pattern `FROM … INNER JOIN … ON …`.
- **You:** Live-code full-name query from `orders` `INNER JOIN` `customers` on `customer_id`; prefix columns with table names.
- **Students:** Run the join; **pair-share:** compare row count to raw `orders` count (should align for INNER).
- **You:** Rewrite with aliases `o` / `c`; add `ORDER BY c.full_name`.
- **You:** Add `WHERE c.city = 'Mumbai'` and `WHERE o.amount > 1000` examples; stress filtering *after* the join on either table’s columns.
- **Room action:** Watch for missing `ON` clause or wrong key; live-debug one common mistake on screen (with consent from the class).

**Bridge sentence:** “Writes are trickier when tables depend on each other — updates, deletes, and CASCADE are where integrity shows up.”

---

## 7. CRUD on related data, CASCADE, and breaking integrity (16 minutes)

- **You:** `UPDATE orders` with `WHERE order_id` **and** `AND customer_id` as a safety habit; `UPDATE customers` email and tie back to normalization (“ID is stable, display data changes”).
- **You:** `DELETE` one order vs `DELETE` customer with **ON DELETE CASCADE**; run verification `SELECT * FROM orders WHERE customer_id = 4`.
- **Students:** Execute the safe updates/deletes on their copy or watch and run a variant — **check for thumbs up** after CASCADE demo.
- **You:** Optionally run (or show) failing `INSERT` with bad FK and failing `DELETE` on parent while children exist — read the error message together; map to “agent memory can’t corrupt silently.”
- **Room action:** Remind everyone to use `WHERE` on every mutating statement; spot anyone running global `DELETE`.

**Bridge sentence:** “This isn’t academic — pagination, joins, and FKs are exactly how agents, dashboards, and Supabase-backed apps behave in production.”

---

## 8. AI applications, takeaways, and next session hook (9 minutes)

- **You:** Rapid-fire map: recent conversation = `ORDER BY … LIMIT 1`; top recommendations = `ORDER BY score DESC LIMIT 5`; activity feed = `LIMIT`/`OFFSET` pages; user ↔ sessions = one-to-many; JOIN for “name + session summary.”
- **You:** Read or paraphrase **Key Takeaways** from the lecture notes; preview next session — **Python (or application code) talking to Supabase**.
- **Students:** One-minute **exit ticket** in chat: “Name one clause and one relationship type you used today.”
- **You:** Field 2–3 questions; point to the terminology table in the notes for self-study.

**Bridge sentence:** (Session close — none required.)

---

## Timing flex — if the session is running long

- **Cut first (save ~10–18 min):** Shorten the failing `INSERT`/`DELETE` error demos to a spoken “the database returns an error like…” without running; reduce pair-share in block 2 to 1 minute; summarize relationship diagrams verbally instead of displaying all three images.
- **Cut second (~8–12 min):** Combine blocks 5 and 6 slightly: one join query with aliases only, skip the second `WHERE` example or assign it as homework reading in the notes.
- **Never skip:** Foreign key creation with `REFERENCES` and at least one successful `INNER JOIN` and one `ON DELETE CASCADE` observation — these are the session’s competency anchors.
- **If ahead of schedule (~10 min buffer):** Deepen block 8 with a whiteboard sketch of an agent reading `sessions` JOIN `users`; or let students draft a junction table for `students`/`courses` on paper.
