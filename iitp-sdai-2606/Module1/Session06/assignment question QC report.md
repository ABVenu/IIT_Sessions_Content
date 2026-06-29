# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Nested conditional concept using metro ticket-and-bag scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Nested loop definition using school assembly analogy. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. 2D list access `hall[2][1]` returns `C2`. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Dictionary key lookup as O(1) example. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Nested loop iteration count `4 × 5 = 20`. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: C. Relevancy: Yes. Target at last position represents worst case. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Nested conditional behaviour and Python indentation; D correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, C. Relevancy: Yes. O(n) patterns with single loop and `if` inside loop; B and D correctly excluded. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. O(n²), O(n³), and worst-case focus; C correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Nested-loop execution, `continue`, and `break` behaviour; D correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via OneCompiler (save public + share link in LMS): Yes — matches Session 1 format with step images. No external dataset needed — seating grid hardcoded in prompt. Tests nested loops, conditional inside loop, 2D list access, and counter placement outside loops. Expected total open seats verified as 8. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria are satisfied:

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard).
- 1 medium subjective coding task with OneCompiler submission instructions matching Session 1.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to nested conditionals, nested loops, 2D lists, combinations, `continue`/`break`, best/average/worst case intuition, and O(1)/O(n)/O(n²)/O(n³) basics from released lecture notes.
- Surface-level concepts such as `enumerate()` and nested `while` loops are covered only through simple objective checks, not required in the subjective implementation.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.
