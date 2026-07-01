# Assignment Question QC Report

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | Objective MCQ (Easy) | Correct option: B. Relevancy: Yes. Tests input vs output sanitization with a practical support-bot scenario. |
| Q2 | Objective MCQ (Easy) | Correct option: B. Relevancy: Yes. Tests PII definition from released notes. |
| Q3 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests prompt-injection pattern recognition. |
| Q4 | Objective MCQ (Easy) | Correct option: A. Relevancy: Yes. Tests core guardrail purpose. |
| Q5 | Objective MCQ (Moderate) | Correct option: B. Relevancy: Yes. Applied scenario — internal refund checks leak = data leakage. |
| Q6 | Objective MCQ (Moderate) | Correct option: A. Relevancy: Yes. Tests injection refusal template from lab. |
| Q7 | Objective MSQ (Moderate) | Correct options: A, B. Relevancy: Yes. Distinguishes input vs output sanitization layers. |
| Q8 | Objective MSQ (Moderate) | Correct options: A, B, C. Relevancy: Yes. Tests unguarded-bot failure types (PII, leakage, scope). |
| Q9 | Objective MSQ (Hard) | Correct options: A, B, C. Relevancy: Yes. Tests LLM Guard capabilities taught at overview level. |
| Q10 | Objective MSQ (Hard) | Correct options: A, B, C. Relevancy: Yes. Tests correct guarded pipeline order; D and E are clearly wrong distractors. |
| Subjective | Practical coding (single file) | Medium difficulty: Yes. Clear submission instructions (case c): Yes. Dataset needed: No — rule lists and mock replies provided in question. Scope: input/output guardrails, refusal templates, PII mask, bias refusal — all from released notes. No LLM API or heavy frameworks required. |

## Overall QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers guardrails, PII, data leakage, prompt injection, input/output sanitization, refusal templates, LLM Guard overview, and pipeline order. |
| Creativity | 5 | QuickKart support scenario; applied MCQs; offline rule-based guardrail implementation mirrors lab without out-of-scope APIs. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: 1 practical task with submission instructions and full answer explanation. |
| No Logical Mistakes | True | All correct options verified against released notes; subjective expected outputs match reference solution logic. |
| No Presentation Mistakes | True | Self-contained questions; no session references; grammar and formatting consistent. |

## Final Result

QC passed. No modifications required.
