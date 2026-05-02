# Assignment Question QC Report
## Session: Self-Reflection and Feedback Loops | Module 2 — Session 11

---

## Objective Assignment QC

| Question # | Type | Correct Option | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|
| Q1 | MCQ — Easy | C — Self-reflection | Yes | Correct and unambiguous. The chatbot scenario (first-draft acceptance, no self-check) maps directly to the session definition of self-reflection. All three distractors are plausible but clearly wrong: A (chain-of-thought) addresses reasoning, not output review; B (one-shot) is the cause of the problem; D (user feedback loop) requires human input, which is a different mechanism. |
| Q2 | MCQ — Easy | D — Generate → Critique → Rewrite | Yes | Correct. The three-stage order is explicitly defined in the lecture notes. The distractors all disrupt the logical sequence (e.g., critiquing before generating anything is impossible). No ambiguity. |
| Q3 | MCQ — Easy | D — Exactness | Yes | Correct. The EVAL Exactness criterion ("Did the AI answer exactly what was asked?") is the precise failure when half the question is skipped. Distractors (Validity, Adequacy, Layout) each address a different dimension and are clearly non-applicable to this scenario. |
| Q4 | MCQ — Easy | D — Hallucination | Yes | Correct. Wrong specific facts (wrong founders) stated with full confidence and detail is the textbook definition of hallucination from the session. Distractors (Vagueness, Wrong Format, Incomplete Coverage) are factually distinct failure types and clearly inapplicable. |
| Q5 | MCQ — Moderate | B — Acknowledge what works; target only the second paragraph | Yes | Correct. Option B applies both iterative prompting best practices: acknowledge working elements + fix one specific thing at a time. Options A, C, and D each represent explicit anti-patterns from the session (full rewrite, multi-target vague instructions, vague correction). |
| Q6 | MCQ — Moderate | C — Reflection-based prompting | Yes | Correct. High-volume autonomous deployment with measurable criteria is the precise use case for reflection-based prompting as described in the comparison table in the session. One-shot provides no quality check; iterative requires human presence; user feedback loops are reactive post-delivery. |
| Q7 | MSQ — Moderate | A, B, D | Yes | Correct. A (max cycles), B (measurable criterion), and D (reusable template) are all Principles 1–3 from the "Four Principles for Efficient Feedback Loops" section. C ("engaging and on-brand") is explicitly identified in the notes as a subjective criterion that breaks self-evaluation. E (loop until "feels right") is the exact anti-pattern the max-cycles principle prevents. |
| Q8 | MSQ — Moderate | A, C, D | Yes | Correct. Role controls tone consistency; Output Format controls structural consistency; Reflection Criteria catches quality variability. B (Task) varies intentionally by design and is not a source of inconsistency. E (chain-of-thought) addresses single-response reasoning, not cross-run consistency — correctly excluded. |
| Q9 | MSQ — Hard | A, B, D, E | Yes | Correct. A (specific feature inclusion), B (word count), D (no unverified audience claims), and E (concluding recommendation) are all measurable and binary. C ("good review") is explicitly the weak-criteria anti-pattern. F ("positive and enthusiastic") is subjective without further definition — as covered under Principle 1, only measurable criteria allow accurate self-evaluation. |
| Q10 | MSQ — Hard | A, C, D | Yes | Correct. A (paragraph when list asked = Wrong Format), C (only pros when pros+cons asked = Incomplete Coverage), D (evidence contradicts conclusion = Logical Contradiction) are all correctly matched. B is misidentified as Vagueness — wrong specific facts with confidence is Hallucination, not Vagueness. E is misidentified as Hallucination — a true-but-useless answer is Vagueness, not Hallucination. The distractors test whether students can distinguish between similar-sounding failure types. |

---

## Subjective Assignment QC

| Question # | Type | Remarks |
|---|---|---|
| Q1 | Subjective — Practical Task (Google Doc submission) | Medium difficulty ✓. Scenario is creative and original — the coaching institute context is not directly lifted from session examples, requiring the student to apply concepts to a new domain ✓. Requires applied design of all four agent prompt flow components (Role, Task, Reflection Criteria, Output Format) plus a loop instruction ✓. The Design Note requirement tests deeper reasoning about why each design choice matters ✓. Submission instructions are clearly stated with folder path suggestion, sharing settings, and submission format ✓. No dataset required — student generates the prompt design from the scenario ✓. Question difficulty is genuinely medium: the concepts needed are all taught, but applying them to a new scenario requires synthesis, not recall ✓. |

---

## Overall Assignment Quality Ratings

| Metric | Objective Assignment | Subjective Assignment |
|---|---|---|
| Content Coverage | 5 / 5 | 5 / 5 |
| Creativity | 5 / 5 | 5 / 5 |
| Structural Adherence | 5 / 5 | 5 / 5 |
| No Logical Mistakes | True | True |
| No Presentation Mistakes | True | True |

---

## Content Coverage Notes

The 10 objective questions together cover the following topics from the session:

| Session Topic | Covered By |
|---|---|
| Self-reflection — definition and purpose | Q1 |
| Self-correction prompts — three-stage structure | Q2 |
| EVAL framework | Q3 |
| Five types of bad AI responses (Hallucination, Vagueness, Wrong Format, Incomplete Coverage, Logical Contradiction) | Q4, Q10 |
| Iterative prompting — best practices | Q5 |
| Comparing prompting strategies (one-shot vs iterative vs reflection-based) | Q6 |
| Feedback loop design — four efficiency principles | Q7 |
| Agent prompt flow — four components | Q8 |
| Internal feedback loop — measurable criteria design | Q9 |

The subjective question covers the capstone skill of the session — building a complete four-component agent prompt flow — applied to a novel scenario.

---

## QC Verdict

All ratings meet or exceed the expected standard (Content Coverage ≥ 5, Creativity ≥ 5, Structural Adherence ≥ 5, No Logical Mistakes, No Presentation Mistakes). No revision pass required. Both assignments are ready for platform upload.
