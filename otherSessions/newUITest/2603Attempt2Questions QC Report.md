# QC Report — 2603Attempt2Questions.md

**Assignment:** IITR-AS-2603 | Module 1 — Objective Questions (Attempt 2)
**Type:** Objective Only (10 Questions)
**QC Date:** 07 May 2026

---

## Part 1 — Per-Question QC

| Q# | Type | Difficulty | Correct Answer(s) | Correct Answer Relevant to Question? | Remarks |
|----|------|------------|-------------------|--------------------------------------|---------|
| Q1 | MCQ | Easy | C — `<class 'int'>` | Yes | Both operands are integer literals; subtraction preserves `int` type. All distractors are plausible but clearly wrong. |
| Q2 | MCQ | Easy | D — `Senior Discount` | Yes | `elif age <= 59` is False for 65; falls to `else`. Step-by-step trace verified. |
| Q3 | MCQ | Easy | B — `392` | Yes | Manual sum: 72+85+90+68+77 = 392. Distractors 390 (arithmetic slip), 77 (last element), 0 (uninitialized assumption) are all plausible traps. |
| Q4 | MCQ | Easy | A — `77.0` | Yes | `temps_c[1]` = 25; (25 × 9/5) + 32 = 77.0. Other options map correctly to indices 0 and 2, making them strong distractors. |
| Q5 | MCQ | Moderate | C — `git push origin main` | Yes | Add → Commit → Push workflow. Pull, clone, and merge are all meaningful distractors testing understanding of what each Git command does. |
| Q6 | MCQ | Moderate | C — `(3, 4)` | Yes | 12-element array reshaped to `(3, 4)`; 3×4=12 ✓. Distractors test reversed shape and pre-reshape shape confusion. |
| Q7 | MSQ | Moderate | A, B, C, E | Yes | All four are verified: `upper()` → "AISHA" ✓; `.get()` → None ✓; `len()` → 4 ✓; `["score"]` → KeyError ✓. D is a deliberate false option (op4 is True, not False). |
| Q8 | MSQ | Moderate | A, D, E | Yes | A and D are logically equivalent (AND is commutative). E adds ORDER BY which changes sort but not filter. B wrong (SELECT *), C wrong (OR logic). |
| Q9 | MSQ | Hard | A, B, C | Yes | All three correctly filter FIRST then aggregate. D filters after aggregation (different semantics). E computes `.mean()` on both columns, violating the sum requirement for units_sold. |
| Q10 | MSQ | Hard | A, C, E | Yes | A: INNER JOIN + HAVING ✓. C: LEFT JOIN + HAVING ✓. E: Reversed FROM/JOIN + standard `HAVING SUM(o.amount)` ✓ *(fixed from alias usage)*. B: WHERE with aggregate ✗. D: COUNT instead of SUM ✗. |

---

## Part 2 — Issues Found & Fixes Applied

| Issue # | Question | Issue Description | Fix Applied |
|---------|----------|-------------------|-------------|
| 1 | Q10 Option E | Used `HAVING total_amount > 100000` — referencing a SELECT alias in HAVING is **non-standard SQL** and fails in PostgreSQL and other ANSI-compliant engines. | Changed to `HAVING SUM(o.amount) > 100000`. Updated explanation to remove dialect-specific caveats. |

---

## Part 3 — Overall Assignment QC Scorecard

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Content Coverage | **5 / 5** | All 11 topics from the Module 1 syllabus covered across 10 questions (Python Basics, Conditional Statements, Loops, Lists & Functions, Version Control, NumPy, Strings/Dictionaries, SQL SELECT/WHERE, Pandas Aggregation, SQL Aggregation & Joins). |
| Creativity | **5 / 5** | Every question is scenario-based with a named character and a real-world context (budget tracking, ticket booking, temperature converter, sales analysis, e-commerce database, etc.). No abstract or dry "what does X do?" style questions. |
| Structural Adherence | **5 / 5** | Exactly 6 MCQs (4 Easy + 2 Moderate) and 4 MSQs (2 Moderate + 2 Hard). Questions ordered progressively Easy → Moderate → Hard. Full answer explanations provided for every question including reasoning for wrong options. |
| No Logical Mistakes | **True** | All correct answers mathematically and programmatically verified. One SQL non-standard alias issue in Q10 was identified and corrected. Post-fix, zero logical errors remain. |
| No Presentation Mistakes | **True** | No spelling or grammar errors. Code blocks are properly formatted. All options clearly labelled A–E. Correct answers and explanations are consistent with each other throughout. |

---

## Part 4 — QC Verdict

> **PASSED** — All five criteria meet the required threshold.
> Content Coverage ≥ 5 ✓ | Creativity ≥ 5 ✓ | Structural Adherence ≥ 5 ✓ | No Logical Mistakes ✓ | No Presentation Mistakes ✓

The assignment is ready for upload to the platform.
