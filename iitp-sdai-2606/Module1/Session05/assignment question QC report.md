# Assignment Question QC Report

## Objective Questions QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ - Easy | Correct option: C. Relevancy: Yes. Tests dictionary selection for contact-style key-value data. Incorrect options are clearly non-suitable data types/structures. |
| Q2 | MCQ - Easy | Correct option: C. Relevancy: Yes. Tests direct access using `dict[key]`. Output `88` is logically correct. |
| Q3 | MCQ - Easy | Correct option: B. Relevancy: Yes. Tests empty dictionary syntax. Distractors represent list, tuple, and string. |
| Q4 | MCQ - Easy | Correct option: B. Relevancy: Yes. Tests `get()` behavior for a missing key without default. `None` is correct and no `KeyError` occurs. |
| Q5 | MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests sorting dictionary values using `sorted(prices.values())`. Other options test keys, views, or pairs. |
| Q6 | MCQ - Moderate | Correct option: C. Relevancy: Yes. Tests duplicate-key overwrite behavior. Latest value is correctly retained. |
| Q7 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests `keys()`, `values()`, `items()`, and `get(key, default)` behavior. |
| Q8 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests character-count pattern using dictionary and `get(char, 0)`. |
| Q9 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests `len()`, `sorted()` on keys, `max()` on values, and rejects invalid `sum()` on string keys. |
| Q10 | MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Tests dictionary/hashmap intuition and hashable key rules. |

## Subjective Question QC

| Question Number | Type | Remarks |
|---|---|---|
| SQ1 | Subjective Coding - Medium | Difficulty: Medium. Relevancy: Yes. The task asks for a single-file Python implementation using dictionaries, `get()`, `keys()`, `values()`, `items()`, `len()`, `sorted()`, `max()`, `min()`, and `sum()`. Submission instructions match Session01 format: OneCompiler Python link, Save/Share workflow, and LMS link submission. Input/output format and constraints are included. No external dataset is needed. |

## Overall QC Ratings

| Criteria | Rating / Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

## Final QC Summary

- Objective assignment has exactly 10 questions: 6 MCQs and 4 MSQs.
- Objective questions are ordered progressively: Easy, Moderate, then Hard.
- Subjective assignment has exactly 1 practical implementation task of medium difficulty.
- All questions are within the scope of dictionaries, hashmaps, dictionary methods, built-in functions, hashable keys, and character counting.
- Every question includes a complete answer explanation with correct answer(s) and reasoning.
- No question uses informal references such as "as taught in the session".
- QC status: **PASSED**.
