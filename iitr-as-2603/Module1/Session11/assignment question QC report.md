# Assignment Question QC Report
## Session 11 — SQL: Aggregation and Joining Tables

---

## Assignment: Objective — Question-Level QC

| Q No. | Type | Difficulty | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|---|
| Q1 | MCQ | Easy | B — `COUNT(*)` | Yes | Tests COUNT(*) vs COUNT(column) distinction; scenario is practical (delivery app with NULLs); all distractors are plausible and clearly wrong. |
| Q2 | MCQ | Easy | C — GROUP BY | Yes | Tests purpose of GROUP BY; scenario is concrete (retail city-wise sales); other options (WHERE, HAVING, ORDER BY) are legitimate SQL clauses that make good distractors. |
| Q3 | MCQ | Easy | B — LEFT JOIN | Yes | Tests when to use LEFT JOIN; university exam scenario is relatable; INNER JOIN distractor is the most common student mistake. |
| Q4 | MCQ | Easy | D — Foreign Key | Yes | Tests Primary Key vs Foreign Key distinction; e-commerce orders scenario directly maps to lecture content; distractors (Index Key, Super Key) are real terms that students may confuse. |
| Q5 | MCQ | Moderate | B — FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY | Yes | Tests SQL execution order, a key concept explicitly taught in session; logistics scenario is practical; all options are shuffled variations of the real clauses making it non-trivial. |
| Q6 | MCQ | Moderate | B — WHERE runs before grouping | Yes | Tests WHERE vs HAVING conceptual understanding; shows actual broken code for students to diagnose; distractors address common misconceptions (e.g., WHERE only for text columns). |
| Q7 | MSQ | Moderate | A, B, D | Yes — all three correct statements are accurate and directly tied to GROUP BY rules from session | Tests GROUP BY rules; one distractor (C — only one column) is a very common student misconception; practical sales scenario. |
| Q8 | MSQ | Moderate | A, C, D | Yes — all three are factually correct about INNER JOIN | Tests INNER JOIN behavior vs LEFT JOIN; option B (NULL for unmatched) is a classic mix-up with LEFT JOIN; HR recruitment scenario is relatable. |
| Q9 | MSQ | Hard | A, B, C | Yes — all three are correct and nuanced | Tests combined understanding of LEFT JOIN + GROUP BY + HAVING + COUNT(NULL) behavior; option D is a high-value distractor testing WHERE vs HAVING confusion with aggregates. |
| Q10 | MSQ | Hard | A, C | Yes — both are logically correct SQL queries | Tests ability to identify valid vs invalid query structures; option B has aggregate in WHERE (common error); option D has GROUP BY on non-unique column (subtle but important bug). |

---

## Assignment: Subjective — Question-Level QC

| Q No. | Type | Difficulty | Submission Instructions Clear? | Dataset Provided? | Remarks |
|---|---|---|---|---|---|
| Q1 (4 tasks) | Practical Coding (Python + SQLite) | Medium | Yes — Case C: single `.py` file, run in VS Code, submit via code editor in LMS | Yes — full schema + INSERT data provided as ready-to-run Python setup code | All 4 tasks test in-scope concepts: Task 1 (INNER JOIN + WHERE + GROUP BY + HAVING), Task 2 (LEFT JOIN + COALESCE), Task 3 (WHERE + GROUP BY + compound HAVING), Task 4 (3-table INNER JOIN + GROUP BY + HAVING). No concept asked that was taught only at surface level. Difficulty is medium — requires combining multiple clauses but no subqueries or window functions (not in scope). |

---

## Overall Assignment QC Ratings

### Objective Assignment

| Criteria | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | All major topics covered: COUNT/SUM/AVG/MAX/MIN, GROUP BY (golden rule), HAVING vs WHERE, SQL execution order, INNER JOIN, LEFT JOIN, table aliases, multi-table reasoning, NULL behavior. |
| Creativity | 5 | All questions use real-world scenarios (food delivery, logistics, telecom, university, HR, retail) instead of abstract table names. Code snippets are embedded in questions for hands-on context. |
| Structural Adherence | 5 | Exactly 10 questions: 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard). Ordered Easy → Moderate → Hard as required. All options have explanations covering why wrong options are wrong. |
| No Logical Mistakes | True | All correct answers verified against SQL semantics. WHERE vs HAVING, NULL behavior in COUNT and SUM, GROUP BY uniqueness requirements all checked. |
| No Presentation Mistakes | True | No grammatical or spelling errors. Code blocks formatted consistently. All questions are self-contained with sufficient context. |

### Subjective Assignment

| Criteria | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Covers JOIN (INNER and LEFT), GROUP BY, HAVING, WHERE, aggregate functions (COUNT, SUM), multi-table joins, and NULL handling (COALESCE) — all within session scope. |
| Creativity | 5 | FoodRush food delivery scenario is realistic and engaging. Tasks reflect real analyst work (revenue reports, customer activity, targeted campaigns, spend breakdowns). |
| Structural Adherence | 5 | Exactly 1 subjective question with 4 structured sub-tasks. Submission follows Case C (single .py file). Full ideal solution with alternative approaches provided in answer explanation. |
| No Logical Mistakes | True | All 4 SQL queries verified for correctness. GROUP BY includes both ID and name columns. COALESCE used correctly for NULL → 0 conversion. HAVING conditions correctly target aggregate results. |
| No Presentation Mistakes | True | Schema presented as clear table. Setup code is complete and runnable. Expected output columns stated for each task. Hints provided without giving away the answer. |

---

## QC Summary

All criteria across both assignments meet the required threshold of **5/5 ratings** with **no logical or presentation mistakes**. No re-run or improvisation required.
