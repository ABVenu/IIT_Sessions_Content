# Assignment Question QC Report: Database Fundamentals & SQL (Part II)

**Cohort:** iitp-sdai-2606 / Module3 / Session32  
**Aligned to:** `Lecture Notes.md`

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **C**. Relevancy: **Yes**. `WHERE` on `SELECT` filters the answer and leaves the other rows stored. |
| 2 | Objective MCQ - Easy | Correct option: **B**. Relevancy: **Yes**. Text match is case-sensitive and uses single quotes; `IS NULL` is the wrong test for a filled city. |
| 3 | Objective MCQ - Easy | Correct option: **D**. Relevancy: **Yes**. `marks < 80` keeps Rahul (76) and Imran (64) only. |
| 4 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. `SET` plus `WHERE id = 1` changes one column on one row. |
| 5 | Objective MCQ - Moderate | Correct option: **C**. Relevancy: **Yes**. `CHECK` rejects marks 150 on `UPDATE`; the old value stays. |
| 6 | Objective MCQ - Moderate | Correct option: **D**. Relevancy: **Yes**. Deleting a hostel that students still reference is refused; an unused hostel delete and a valid `hostel_id` update are allowed. |
| 7 | Objective MSQ - Moderate | Correct options: **B, D, E**. Relevancy: **Yes**. `IS NULL`, text `'Not given'`, and filter-does-not-delete. A and C are wrong. |
| 8 | Objective MSQ - Moderate | Correct options: **A, C, D, E**. Relevancy: **Yes**. `UPDATE`/`DELETE` without `WHERE`, comma in `SET`, and `RETURNING`. B is wrong. |
| 9 | Objective MSQ - Hard | Correct options: **A, C, D**. Relevancy: **Yes**. One-to-many, deleting one enrolment pair, and duplicate pair primary key. B and E are wrong. |
| 10 | Objective MSQ - Hard | Correct options: **B, C**. Relevancy: **Yes**. Identity is not reused, and a wide `DELETE` should be previewed with `SELECT`. A, D, and E are wrong. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (single `club_register.sql`, run in a PostgreSQL SQL Editor, paste into the LMS answer box). Dataset needed: **No** (all rows are written in the question). Covers `WHERE` (`AND`, `OR`, `IS NULL`), `UPDATE`/`SET`/`RETURNING`, `DELETE` with `WHERE`, one-to-many `room_id`, and a `signups` link table. |

---

## Overall Assignment QC — Iteration 2

Iteration 1 drafted the full set. Iteration 2 rechecked option counts so MSQs are not all the same size, stated that `id` is identity before claiming id 5 is not reused, and aligned the subjective script with Parts A–F.

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers `WHERE`, comparison text, `AND`/`OR`, `IS NULL` versus `= NULL` and versus `'Not given'`, `UPDATE`/`SET`/`WHERE`/`RETURNING`, a missing comma in `SET`, check and unique failure leaving the old value, `DELETE` versus dropping the table, foreign keys, one-to-many, a shared `hostel_id`, link-table many-to-many, pair primary key, child-before-parent drop order, and identity not reused. `ALTER TABLE ... ADD COLUMN` is practiced in the subjective script. Stays inside the lecture notes. |
| Creativity | 5 | Clinic visits, a marks list, a hostel office, a city register, and a coding-club lab register. The subjective task applies the same ideas to rooms, members, and workshop signups. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: one medium SQL script with exact expected grids, single-file submission, full walkthrough, and complete code. |
| No Logical Mistakes | True | Filter results, refused hostel delete, null tests, and the club script’s ids and remaining signup pairs were checked against the seeded rows. Correct options match the statements. |
| No Presentation Mistakes | True | No session-reference phrasing. Each objective item explains the correct choice and why the others are wrong. Expected inputs and outputs are stated. |

**Expected result:** All criteria met — **QC passed**. No further modification required.

---

## Scope Guardrails Applied

| Outside this session’s notes | Assignment treatment |
|---|---|
| Joining two tables so a name and a related title appear on one result line | Not asked. Every read uses one table. |
| Mixing `AND` and `OR` without a worked grouping example | Not asked as an operator-precedence puzzle. |
| Triggering check, unique, or foreign-key errors inside the submitted script | Not required. Those failures are tested in the objective questions. The script is a successful run. |
