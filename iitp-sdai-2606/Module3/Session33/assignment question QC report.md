# Assignment Question QC Report: Advanced SQL – JOINs

**Cohort:** iitp-sdai-2606 / Module3 / Session33  
**Aligned to:** `Lecture Notes.md`

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **C**. Relevancy: **Yes**. Inner join on `branch_id` drops Esha because NULL matches no branch. Anil and Bina both stay with Central Branch. Store Room is not returned. |
| 2 | Objective MCQ - Easy | Correct option: **B**. Relevancy: **Yes**. The link is `branch_id = branches.id`. `m.id = br.id` pairs Bina (id 2) with North Branch, not Central Branch. |
| 3 | Objective MCQ - Easy | Correct option: **D**. Relevancy: **Yes**. Left join from members keeps Esha with NULL `branch_name`. Store Room stays out. The stored table is unchanged. |
| 4 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. Bare `id` is ambiguous. `AS m` does not rename the stored table. |
| 5 | Objective MCQ - Moderate | Correct option: **C**. Relevancy: **Yes**. `WHERE c.club_name = 'Poetry Club'` after the left joins keeps only Anil Joshi and Dev Malik. |
| 6 | Objective MCQ - Moderate | Correct option: **D**. Relevancy: **Yes**. Store Room is found by a left join from branches plus `m.id IS NULL`. A and C return no rows. B returns Esha Roy. |
| 7 | Objective MSQ - Moderate | Correct options: **A, C, E**. Relevancy: **Yes**. Two pairs make two result rows, Chess Club is unmatched, and each join needs `ON`. B and D are wrong. |
| 8 | Objective MSQ - Moderate | Correct options: **B, D**. Relevancy: **Yes**. Store Room comes back with NULL `full_name`, and North Branch comes back with Charu Sen. A, C, and E are wrong. |
| 9 | Objective MSQ - Hard | Correct options: **A, B, D**. Relevancy: **Yes**. `WHERE` on the club name drops non-matches, the same test inside `ON` keeps all five members, and left-join `IS NULL` returns Esha. C and E are wrong. |
| 10 | Objective MSQ - Hard | Correct options: **A, B, C, D**. Relevancy: **Yes**. Prefixed ids are legal, a missing `ON` is a syntax error, `m.id = br.id` pairs Dev with Store Room, and a `WHERE` on Central Branch keeps only Anil and Bina. E is wrong. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (practice in the Supabase SQL Editor, then paste the working queries into the answer box). Dataset needed: **No** (the setup script in the question inserts the rows). Four queries: inner join on `room_id`, left join that keeps Rhea, two-hop join through `bookings`, and the Chords test kept inside `ON`. |

---

## Subjective QC — Iteration 4

The practical task is now one setup script plus four queries. City and score filters, the unused-room query, the unused-skill query, and the final stored-row check were removed. Objective questions were not changed. Unmatched `IS NULL`, including an unused room or skill, remains covered by the objective questions.

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | The script still applies an inner join, a left join, a foreign-key `ON`, aliases, a two-hop link table, and a right-side test kept inside `ON`. |
| Creativity | 5 | The weekend music school register is unchanged. The learner writes the four reads against a given setup. |
| Structural Adherence | 5 | One medium SQL task, exact expected grids, Supabase practice, paste-into-answer-box submission, short walkthrough, and complete code. |
| No Logical Mistakes | True | The four grids were checked against the seeded rows: Kabir and Lata with Practice Room A, Rhea with NULL, Kabir on two skill rows, and Chords only for Kabir when the test is in `ON`. |
| No Presentation Mistakes | True | The setup is given once. Each query states the join, the order, and the expected grid. `(NULL)` is defined once. |

**Expected result:** Subjective criteria met — **QC passed**.

---

## Subjective QC — Iteration 3

Submission text now tells the learner to practice the script in the Supabase SQL Editor and, once every grid matches, paste the queries into the answer box. Objective questions were not changed.

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Same join coverage as Iteration 2. The task still builds the register and reads the connected rows. |
| Creativity | 5 | Weekend music school register is unchanged. |
| Structural Adherence | 5 | One medium SQL script, exact expected grids, Supabase practice, paste-into-answer-box submission, full walkthrough, and complete code. |
| No Logical Mistakes | True | Expected grids are unchanged and still match the seeded rows. |
| No Presentation Mistakes | True | The task line and the submission block describe the same Supabase-then-answer-box path. |

**Expected result:** Subjective criteria met — **QC passed**.

---

## Overall Assignment QC — Iteration 2

Iteration 1 drafted the full set and checked every result grid against the seeded rows. Iteration 2 copied the register into each objective question, gave Question 5 two short wrong options beside the short correct option, and stated the city-filter columns and the meaning of `(NULL)` in the subjective task.

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers why a join is required, `INNER JOIN`, `LEFT JOIN`, left versus right table, `ON` with the foreign key, table aliases, ambiguous `id`, a missing `ON`, `NULL` after a left join, `WHERE ... IS NULL` for an unmatched side, `WHERE` removing unmatched left rows, the same test moved into `ON`, a link table with two hops, one stored row becoming two result rows, and a join leaving stored rows unchanged. Stays inside the lecture notes. |
| Creativity | 5 | A library desk (members, branches, clubs) and a weekend music school (rooms, trainees, skills). The questions apply the join rules to those registers. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: one medium SQL script with exact expected grids, single-file submission, full walkthrough, and complete code. |
| No Logical Mistakes | True | Join grids, unmatched `IS NULL` results, the Poetry Club `WHERE` versus `ON` split, and the wrong `id = id` pairing were executed against the seeded rows. Correct options match those results. |
| No Presentation Mistakes | True | No session-reference phrasing. Each question carries the rows it needs. Each objective item explains the correct choice and why the others are wrong. Expected inputs and outputs are stated. |

**Expected result:** All criteria met — **QC passed**. No further modification required.

---

## Scope Guardrails Applied

| Outside this session’s notes | Assignment treatment |
|---|---|
| Totals, averages, or `GROUP BY` | Not asked. Every result is the joined rows themselves. |
| `RIGHT JOIN`, `FULL JOIN`, `CROSS JOIN`, `NATURAL JOIN`, or `USING` | Not asked. |
| Changing stored rows with `UPDATE` or `DELETE` inside the submitted script | Not required. Part G only reads Rhea’s stored `room_id` to show the joins did not write it. |
