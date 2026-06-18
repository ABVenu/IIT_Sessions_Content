# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. System vs user roles via college admission helpdesk scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. JSON schema and guardrails belong in system prompt (medical-notes extractor). |
| Q3 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Translation with no examples = zero-shot. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Proprietary error codes need few-shot demonstrations. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Few-shot fails on diagnosis — symptom→many diseases; needs CoT reasoning. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. Token usage ordering: zero-shot < few-shot < chain-of-thought. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C, E, F. Relevancy: Yes. All five template building blocks; API key is distractor only. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Hallucination guardrails for meeting summarizer. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C, E. Relevancy: Yes. Task→technique matching (translation, internal labels, career compare, JSON extraction). |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D, F. Relevancy: Yes. Sound beginner agent design; rejects 15 few-shot examples and unnecessary CoT on simple extraction. |
| Q1 | Subjective (Applied, Medium) | Medium difficulty: Yes. Creative CampusShelf library scenario. Submission case b (Google Doc + public link + screenshots): Yes. Groq Playground testing required; no Python/API (aligned with session — Playground only). Six-part rubric covers system/user split, five blocks, technique justification, hallucination guardrail, token awareness. Sample solution in answer explanation. |

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

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective applied task (prompt design + Groq Playground validation; Google Doc submission).
- Complete answer explanations for every objective and subjective question.
- No “as taught in session” / “mentioned in lecture” phrasing in learner-facing questions.
- Subjective scope: system/user prompts, zero-shot/few-shot/CoT choice, five building blocks, hallucination guardrails, token awareness — all within released lecture notes; no Python implementation required (deferred in live session).
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## Coverage Checklist (released lecture notes)

| Concept in notes | Objective / Subjective coverage |
| --- | --- |
| System vs user prompts | Q1, Q2; Subjective Part 1–2 |
| Bounded system prompt | Q2; Subjective Part 1 |
| Zero-shot vs few-shot | Q3, Q4, Q9; Subjective Part 4 |
| Chain-of-thought | Q5, Q6, Q9, Q10; Subjective Part 4 |
| Five building blocks | Q7; Subjective Part 3 |
| Hallucination guardrails | Q8; Subjective Part 1 |
| Technique selection / token cost | Q6, Q9, Q10; Subjective Part 6 |
| Groq Playground hands-on | Subjective Part 5 |
| Beginner single-agent workflow | Q10; Subjective overall scenario |
