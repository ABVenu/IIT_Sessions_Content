# Assignment Question QC Report

## Session 10: SQL – Querying Data with SELECT and WHERE

---

## Objective Questions

| Q No. | Type           | Correct Option                            | Correct Option Relevancy to Question | Remarks                                                                                                                                                                                                                                           |
| ----- | -------------- | ----------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1    | MCQ – Easy     | C) `SELECT * FROM employees;`             | Yes                                  | Tests basic SELECT \* syntax in a practical analyst scenario. Correct option is the only syntactically valid query. All distractors break SQL keyword order or use invalid syntax.                                                                |
| Q2    | MCQ – Easy     | D) `WHERE JoiningYear >= 2020`            | Yes                                  | Correctly identifies WHERE as the row-filtering clause. Distractors (HAVING, ORDER BY, LIMIT) are all real SQL keywords but serve entirely different purposes — good plausible traps.                                                             |
| Q3    | MCQ – Easy     | D) 3 rows – Delhi, Mumbai, Bengaluru      | Yes                                  | Directly tests DISTINCT on the lecture dataset. Answer is verifiable against the exact data in the notes. Distractor B (departments) is a plausible confusion trap for learners who mix up column names.                                          |
| Q4    | MCQ – Easy     | D) `LIMIT 5`                              | Yes                                  | Tests knowledge of the MySQL LIMIT keyword. TOP 5 (SQL Server) is a strong, realistic distractor for learners who may have seen other databases. FETCH and ROWS are plausible but invalid.                                                        |
| Q5    | MCQ – Moderate | C) Riya (₹95,000) and Rohan (₹90,000)     | Yes                                  | Requires applying WHERE + ORDER BY DESC + LIMIT 2 together on the lecture dataset. Answer is fully verifiable. Options A (wrong department), B and D (wrong salary rank) are well-constructed distractors.                                        |
| Q6    | MCQ – Moderate | C) Replace `==` with `=`                  | Yes                                  | Classic Python-to-SQL migration mistake. Answer is accurate and relevant. Distractors A and B are implausible but test attention to detail. Distractor D tests whether learners know `==` is invalid in SQL.                                      |
| Q7    | MSQ – Moderate | A, C, D                                   | Yes                                  | A and C are correct OR queries (order doesn't matter). D correctly applies De Morgan's Law — a genuine hard-check for logical thinking. B (AND) is the most common wrong answer. Question, scenario, and all options are within session scope.    |
| Q8    | MSQ – Moderate | A, C, D                                   | Yes                                  | Tests three distinct aspects of NULL handling covered in the lecture. B (`= NULL`) is the most common beginner mistake and a deliberate trap. All correct options are directly supported by the lecture content.                                  |
| Q9    | MSQ – Hard     | A, C, D, E (Vihaan, Ishaan, Meera, Rohan) | Yes                                  | Requires manually tracing IN + BETWEEN logic across the full 10-row dataset. Riya (₹95,000) is the only distractor — she's in IT (passes IN check) but fails the BETWEEN check (95,000 > 90,000). Multi-step reasoning makes this genuinely hard. |
| Q10   | MSQ – Hard     | A, C, D                                   | Yes                                  | Tests pandas ↔ SQL translation covered in the Pandas vs SQL section. B is the trap: `ascending=True` maps to ASC not DESC. A, C, D have accurate translations directly from the lecture's side-by-side mapping table.                             |

---

## Subjective Question

| Q No. | Type                        | Difficulty | Submission Instructions Clear | Dataset / Setup Mentioned                                                                       | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | --------------------------- | ---------- | ----------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1    | Practical Coding Task (SQL) | Medium     | Yes                           | Yes — learner is told to use the exact CREATE TABLE and INSERT INTO statements from the lecture | 5-part query task covering CREATE, INSERT, WHERE, DISTINCT, OR/AND, ORDER BY DESC, LIMIT, LIKE — spans the full scope of Session 10. Framed as a real business scenario (TalentBridge HR analyst) to make it engaging and applied. No out-of-scope concepts used. Submission is via code/answer box (Case C — single .sql file). Each query is independently verifiable. Difficulty is medium: requires combining multiple clauses but all are taught in the session. |

---

## Overall QC Summary

| Check                                                      | Status |
| ---------------------------------------------------------- | ------ |
| Total objective questions: 10 (6 MCQ + 4 MSQ)              | ✅     |
| MCQ split: 4 Easy + 2 Moderate                             | ✅     |
| MSQ split: 2 Moderate + 2 Hard                             | ✅     |
| Questions ordered progressively (Easy → Moderate → Hard)   | ✅     |
| All questions within session scope                         | ✅     |
| All questions scenario/application based (not rote recall) | ✅     |
| Correct options verified against lecture dataset           | ✅     |
| All distractors are plausible and relevant                 | ✅     |
| Subjective question: 1 practical coding task               | ✅     |
| Subjective difficulty: Medium                              | ✅     |
| Subjective submission instructions: Clear (Case C)         | ✅     |
| Dataset/setup instructions mentioned in subjective         | ✅     |
| No grammatical or spelling errors                          | ✅     |
