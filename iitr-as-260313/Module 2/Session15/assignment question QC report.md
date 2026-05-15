# Assignment question QC report — Session 15

## Per-question QC (Objective)

| Question | Type | Remarks |
| --- | --- | --- |
| Q1 | MCQ (Easy) | Correct: **B**; relevancy to `LIKE` wildcards: **Yes** |
| Q2 | MCQ (Easy) | Correct: **B**; relevancy to `ORDER BY` / `DESC`: **Yes** |
| Q3 | MCQ (Easy) | Correct: **B**; relevancy to `LIMIT`: **Yes** |
| Q4 | MCQ (Easy) | Correct: **B**; relevancy to pagination / `OFFSET` arithmetic: **Yes** |
| Q5 | MCQ (Moderate) | Correct: **B**; relevancy to `LIMIT` + `OFFSET` for a fixed 1-based row slice: **Yes** |
| Q6 | MCQ (Moderate) | Correct: **C**; relevancy to many-to-many + junction table: **Yes** |
| Q7 | MSQ (Moderate) | Correct: **A, C**; relevancy to normalization goals: **Yes** |
| Q8 | MSQ (Moderate) | Correct: **A, B, D**; relevancy to `LIMIT`/`OFFSET` semantics: **Yes** |
| Q9 | MSQ (Hard) | Correct: **B, C**; relevancy to cross join / Cartesian product intuition: **Yes** |
| Q10 | MSQ (Hard) | Correct: **A, B, D**; relevancy to foreign keys + inner join behavior + aliases: **Yes** |

## Per-question QC (Subjective)

| Question | Type | Remarks |
| --- | --- | --- |
| S1 | Practical SQL (Medium) | Difficulty: **Medium** (sort + pagination + `LIKE` + `INNER JOIN` + filters). Submission path: **case c** (single `.sql` file, run locally / Supabase, paste into LMS). Dataset: **Provided inline** (`CREATE`/`INSERT` included; no external download). Acceptance checks: **Stated** for self-verification. |

---

## Structural adherence check

| Rule (from generation prompt) | Status |
| --- | --- |
| Objective count = 10 | Met (6 MCQ + 4 MSQ) |
| MCQ mix: 4 Easy + 2 Moderate | Met (Q1–Q4 Easy; Q5–Q6 Moderate) |
| MSQ mix: 2 Moderate + 2 Hard | Met (Q7–Q8 Moderate; Q9–Q10 Hard) |
| Progressive ordering Easy → Moderate → Hard | Met |
| No “as taught in session” phrasing | Met |
| Subjective count = 1 | Met |
| Subjective avoids deep UI-only topics not live-taught (e.g., cascade setup as implementation) | Met |

---

## Aggregate QC ratings

| Criterion | Rating (1–5) | Notes |
| --- | ---: | --- |
| Content coverage | 5 | Aligns to released notes: `LIKE`, `ORDER BY`, `LIMIT`/`OFFSET`, redundancy/normalization framing, relationship shapes, FK idea, `CROSS JOIN` vs `INNER JOIN`, qualified columns/aliases, post-join `WHERE`. |
| Creativity | 5 | Scenario-led prompts (pagination math, device/event reporting, join semantics). |
| Structural adherence | 5 | Matches required counts, ordering, explanation blocks, and submission typing. |
| No logical mistakes | True | Keys and distractors re-verified after Q5 revision (removed edge-case-sensitive “empty child table” dependency). |
| No presentation mistakes | True | Grammar/spelling checked; tables and headings consistent. |

---

## Revision log

- **v1 → v2:** Replaced objective **Q5** to remove an edge case (empty `books` table) and avoid endorsing `CROSS JOIN` as a “guarantee” pattern; reran QC on objective set only.
