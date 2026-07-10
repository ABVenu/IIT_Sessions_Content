# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Local development defined via student moving from online compiler to laptop workspace. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `python3 --version` for verifying Python 3 installation. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `.py` extension identifies Python source files. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `python3 hello_local.py` runs a saved local Python file from Terminal. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Logic-building framework: Input, Output, Conditions, Steps. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. `dictionary.get(key, 0)` returns default `0` when key is missing. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. VS Code play-button troubleshooting; C distractor (`.txt` extension) correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. DSA definition, dictionary, and `mkdir`; D distractor (dry run = cloud execution) correctly excluded. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Frequency map and duplicate detection on `[1, 2, 3, 2, 4, 1]`; D distractor (`.items()` hides values) correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Two-pointer merge approach; C distractor (`sorted(a+b)` only way) correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via VS Code + Terminal run + paste code and output in LMS answer box: Yes — per instructor request. No external dataset needed — fixed score list and exact output format provided. Tests find-max without `max()`, frequency dictionary with `.get()`, duplicate detection with `.items()` and `append()`. |

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
- 1 medium subjective coding task with VS Code + Terminal submission instructions.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to local development, Python/VS Code/Terminal setup, logic building, DSA basics, find-max without `max()`, character/score frequency with `.get()`, duplicate detection with `.items()`, and two-pointer merge concepts from released lecture notes.
- Merge leftover-elements edge case referenced only at objective level (Q10); not required in subjective implementation.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## QC Iteration 2 (Confirmation)

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

### Observations

- Second review confirms practical scenarios (coding club, hackathon, local setup) with no session-reference phrasing.
- Subjective combines two taught patterns (find maximum + find duplicates) in one cohesive applied task at medium difficulty.
- Reference solution verified: highest score `91`, duplicate scores `[89, 45]`, exact three-line output format.
- Submission instructions match instructor request: code in VS Code, run in Terminal, paste code and output in answer box.

### Action Taken

- QC passed. Assignments ready for platform upload.

---

## AssignmentCreation.csv QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | mcsc | Correct option: 2 (B). Relevancy: Yes. Markdown body; options without A/B/C prefixes. |
| Q2 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q3 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q4 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q5 | mcsc | Correct option: 2 (B). Relevancy: Yes. difficultyLevel: 0.5. |
| Q6 | mcsc | Correct option: 2 (B). Relevancy: Yes. Code block preserved in markdown. difficultyLevel: 0.5. |
| Q7 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 0.5. |
| Q8 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 0.5. |
| Q9 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 1. |
| Q10 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 1. |
| Q1 | subjective | Solution in answerExplanation only (not subjectiveAnswer). VS Code + Terminal submission steps included. Reference code with proper indentation. difficultyLevel: 0.5. |

| CSV QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |
| CSV Parsing (11 rows, no errors) | Pass |
| tagRelationships (`6a50962149a3582e9a072e67` on all rows) | Pass |

**CSV QC iteration:** 1 — passed.
