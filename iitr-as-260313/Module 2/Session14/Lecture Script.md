# Lecture Script: Introduction to Databases for AI Systems

**Session Duration:** 2 hours 15 minutes (135 minutes)  
**Audience:** Absolute beginners — Indian students who may have no formal tech background; prioritize Supabase UI safety (password vaulting, avoiding destructive SQL without `WHERE`).

---

**How to use this file**  
Use this script for **timing, room flow, and facilitation only**. It does not replace the detailed explanations in `Lecture Notes.md`; keep lecture notes open for definitions, full SQL snippets, and diagrams.

---

**Break rule**  
After roughly **60–75 minutes** of instruction (typically after completing **SQL core vocabulary**, before diving into **`CREATE TABLE` / heavy hands-on SQL** — or halfway through Supabase setup if the cohort is slow), pause for **one** break of **5–8 minutes**. Do **not** count the break inside the numbered blocks below — resume with the bridge for the next block.

---

## 1. Welcome, arc from Session 13, files vs databases (12 minutes)

- One-line link to prior agent-memory session: long-term recall needs a **persistent store** — tonight we cover **where** that lives and **relational SQL** first.
- Screen-share outcomes from lecture notes (“this session you will…”).
- Run through **scalability / consistency / concurrency / queryability / relationships** as pain points with CSV–Excel metaphors (*school timetable collision*).
- Show **session14-01-file-vs-database**; narrate contrast in one pass.
- **Pair-share (90 seconds):** “Name something you’ve stored in Excel that would embarrass you if two people edited it at once.” Debrief briefly — normalize the struggle.

**Bridge sentence:** “If files are brittle at scale, we still need **the right *kind* of database** — AI stacks mix four familiar families.”

---

## 2. Four database types — picking tools for AI (18 minutes)

- Tour **relational, NoSQL, vector, time-series** with the course’s analogies (*filing cabinet vs flexible shoebox; song hum / embeddings; smartwatch ticker*).
- Walk the comparison table — tie each type to example tools (PostgreSQL **Supabase**, Mongo **Redis**, **Pinecone** / **pgvector**, **InfluxDB** etc.).
- **Cold-call:** “Which family would you use for semantic ‘find similar chats’ retrieval?” *(Vector.)*
- Flash **session14-02-four-database-types** as visual anchor.

**Bridge sentence:** “We’ll standardise on **relational SQL via Supabase** — but first everyone needs shared **vocabulary** so queries aren’t mystical symbols.”

---

## 3. Core SQL terminology — blueprint before code (26 minutes)

- **Office-building analogy** + **session14-03** image: database → floors (tables), rows → records, columns → fields.
- Define **schema** as blueprint; stress **why** duplication is bad precursor to FK (Session 15 goes deeper — don’t linger on joins here).
- **Primary key:** Aadhaar example; **cold-call mistake:** “Could two students share `full_name` as PK?” *(No.)*
- **Foreign key:** marks table referencing `students` — show **session14-04**.
- Constraints as form validation (`NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK` skim); skim **data types** table (`SERIAL`, `VARCHAR`, `BOOLEAN`, dates).
- **Thumbs:** “Thumbs up if you can explain PK vs FK in one sentence.”

**Bridge sentence:** “Vocabulary unlocked — **where we type SQL** matters; we steer you to browser **Supabase** so nobody fights installers tonight.”

---

## 4. MySQL contrast + Supabase project + dashboard map (14 minutes)

- Two-minute **why not local MySQL** for this cohort (*ports, friction*); hype **PostgreSQL-backed** Supabase: zero install, free tier.
- Walk **account → New Project** (name, password **saved**, region Singapore / closest); countdown **~60s** provision — poll chat for “loading” vs “green.”
- Sidebar map: **`Table Editor`**, **`SQL Editor`**, skim Auth/Storage/API as “later.”
- **Circulate:** password in password manager screenshots off; mistaken region uncommon but fixable later.

**Bridge sentence:** “Empty project is a blank blueprint — **`CREATE TABLE` is drafting the registration form.**”

---

## 5. `CREATE TABLE students` + `INSERT` drills (22 minutes)

- **Live-code** full `students` DDL from notes — narrate **`SERIAL PRIMARY KEY`**, **`NOT NULL` / `UNIQUE`**, **`DEFAULT`** for date and boolean.
- Learners **run identical script**; **circulate** for comma/`VARCHAR` typos.
- **`INSERT`** singles then **multi-row `VALUES`** chunk; emphasize column order parity; **`NULL` Optional `city`** for Priya row.
- Open **Table Editor** to sanity-check rows (visual reward).
- **Pair-share:** Compare row counts after multi-insert — should match expectation.

**Bridge sentence:** “Data exists — **`SELECT` is how we interrogate without opening the spreadsheet view every time.**”

---

## 6. `SELECT` anatomy — project columns, stare at grammar (13 minutes)

- Recall template `SELECT … FROM … WHERE …`; flash **session14-05-select-from-where-flow** (even if preview read next block).
- Demos: `SELECT *`, then **specific column lists** (“efficiency / clarity”).
- **Cold-call:** “What does `*` mean here?” *(All columns.)*

**Bridge sentence:** “Reading was safe — **writes are where careers end** if we omit filters — **always pair `WHERE` with `UPDATE` and `DELETE`.”**

---

## 7. `UPDATE` & `DELETE` — surgical writes (14 minutes)

- Live **`UPDATE` city**, **`is_active`**, multi-column with **`WHERE student_id = …`** (safest targeting story).
- **`DELETE`** one PK vs **`DELETE`** by condition (**inactive purge** demo if time).
- Dramatise **`UPDATE students SET …` sans `WHERE`** as table-wide catastrophe — **never run** deliberately in prod; optionally show in disposable scratch table if you maintain one.
- **Thumbs-up:** “Promise your neighbour you’ll glance at **`WHERE`** before pressing Run on any red text.”

**Bridge sentence:** “Same `WHERE` muscle powers **fine-grained reads** — comparison, logic, patterns, ranges, lists.”

---

## 8. `WHERE` mastery + structured vs unstructured + close (16 minutes)

- Rapid demos: **`=` `>` `<` `!=`**, **`AND OR NOT`**, **`LIKE`** with `%` / `_`, **`BETWEEN`**, **`IN` / `NOT IN`** — students mirror on `students`; **cold-call:** pattern for emails ending **`@example.com`**.
- If running short, collapse pattern demos to **two** archetypes (`LIKE`, `IN`) and assign rest as homework read.
- **Structured vs unstructured** section: table contrast + **session14-06**; tie back **vector retrieval** teaser from Block 2.
- Read **Key Takeaways** bullets; glossary table homework anchor.
- **Tease:** next module session extends SQL (**sorting / pagination / relational queries / JOINs** in Session 15 of this cohort) plus future **Python wiring** — keep exact label aligned to program calendar verbally.

**Bridge sentence:** *None — session ends.*

---

## Timing flex (running late — what to trim)

**Cut-first (save ~20–35 min total):**  
- Shorten Block 3: PK/FK story only + skip deep constraint/`CHECK` tour — assign dtypes table reading.  
- Block 8: Teach **comparison + `AND` + one `LIKE` example only** — push `BETWEEN`/`IN` to async practice.  
- Drop optional **inactive bulk `DELETE`** demo in Block 7.

**Never drop:** **`WHERE` with `UPDATE`/`DELETE`** warning, **`CREATE TABLE` basics**, first successful **`SELECT`**, and establishing a **live Supabase project** with at least **one authored table**.

**Running early:** Extended **poll** naming apps per database type (Block 2), extra **`DELETE` guarded practice** pairs, preview **relational teaser** linking FK to Session 15.

---
