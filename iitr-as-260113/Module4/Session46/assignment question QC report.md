# Assignment Question QC Report

**Session:** Introduction to n8n Workflow Automation

**Files reviewed:** `assignment-objective.md`, `assignment-subjective.md`

**QC standard:** `Command Center/prompts/OS_Assignment_Questions_GenerationPrompt.md`

**Review date:** 2026-07-02

**Iteration:** 1 (initial generation)

---

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option: **A**. Relevancy: **Yes**. Tests what n8n represents (workflow automation platform), not LLM/DB/UI. |
| Q2 | Objective (MCQ, Easy) | Correct option: **D**. Relevancy: **Yes**. Form submission starts the workflow. |
| Q3 | Objective (MCQ, Easy) | Correct option: **C**. Relevancy: **Yes**. Node = single step/action/decision. |
| Q4 | Objective (MCQ, Moderate) | Correct option: **B**. Relevancy: **Yes**. Expressions compute runtime dynamic values. |
| Q5 | Objective (MCQ, Moderate) | Correct option: **B**. Relevancy: **Yes**. Environment variables are used for secret/config in self-hosting patterns. |
| Q6 | Objective (MCQ, Moderate) | Correct option: **B**. Relevancy: **Yes**. Daily execution uses schedule trigger. |
| Q7 | Objective (MSQ, Moderate) | Correct options: **A, B, C**. Relevancy: **Yes**. Visual canvas, integrations, and observability are benefits; multi-agent is not mandatory. |
| Q8 | Objective (MSQ, Moderate) | Correct options: **A, B, C**. Relevancy: **Yes**. Credentials store auth data; OAuth2 grants scoped access; minimum permissions applies. |
| Q9 | Objective (MSQ, Hard) | Correct options: **A, B, C**. Relevancy: **Yes**. Image/container/volume definitions correct; D correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options: **A, B, C**. Relevancy: **Yes**. Observability and human-in-the-loop reduce debugging time and risk; D excluded because observability does not guarantee correctness. |
| Q1 | Subjective (Applied Theory, Medium) | Focus: automation + trigger vs workflow in an applied scenario. Submission fits theory-answer box style. Relevancy: **Yes**. |
| Q2 | Subjective (Applied Theory, Medium) | Focus: why visual tools help non-technical users and what still needs careful decisions (order/field mapping). Relevancy: **Yes**. |
| Q3 | Subjective (Applied Theory, Medium) | Focus: trigger choice plus roles of nodes and connections/data flow. Relevancy: **Yes**. |
| Q4 | Subjective (Applied Theory, Medium) | Focus: n8n vs Docker independence plus why Docker helps self-host learning. Relevancy: **Yes**. |
| Q5 | Subjective (Applied Theory, Medium) | Focus: image/container/volume meanings and which persists workflow data. Relevancy: **Yes**. |
| Q6 | Subjective (Applied Theory, Medium) | Focus: credentials, OAuth2 purpose, and one security best practice. Relevancy: **Yes**. |
| Q7 | Subjective (Applied Theory, Medium) | Focus: expressions for runtime dynamic computation. Relevancy: **Yes**. |
| Q8 | Subjective (Applied Theory, Medium) | Focus: observability debugging plus one human-in-the-loop gate scenario. Relevancy: **Yes**. |

---

## Structural Compliance Check

| Requirement | Objective | Subjective |
| --- | --- | --- |
| Total Qs | 10 ✓ | 8 ✓ |
| Difficulty Flow | Easy (Q1-Q3) -> Moderate (Q4-Q8) -> Hard (Q9-Q10) ✓ | Medium throughout ✓ |
| Question Types | 6 MCQ + 4 MSQ ✓ | Theory answers only, no code ✓ |
| Answer explanation | Included per question ✓ | Included ideal walkthrough ✓ |
| No session-number references / metadata leakage | ✓ | ✓ |
| In-syllabus only | ✓ | ✓ |

---

## Overall QC Ratings

| QC Parameter | Rating / Status | Notes |
| --- | --- | --- |
| **Content Coverage** | **5 / 5** | Covers n8n, triggers, nodes, connections/data flow, expressions, credentials, OAuth2, observability/human-in-loop, and Docker concepts (image/container/volume, self-host rationale, independence). |
| **Creativity** | **5 / 5** | Scenario-based questions with names (Ravi, HR coordinator, college club) and realistic automation contexts. |
| **Structural Adherence** | **5 / 5** | Matches objective/submission structure from nearby sessions and includes complete answer explanations. |
| **No Logical Mistakes** | **True** | CRUD/HTTP not tested here; all n8n/Docker definitions are consistent and logically correct. |
| **No Presentation Mistakes** | **True** | Grammar OK; no "as taught" phrasing; MCQ/MSQ correct options consistent. |

---

## Final QC Decision

Expected result met:
- Content Coverage, Creativity, Structural Adherence: all **>= 5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**

Outcome: **PASS** on iteration 1. No changes required.

---

## Iteration 2 — `assignment.csv` for Assess platform

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) ✓ |
| `tagRelationships` on all rows | `6a4611d7179257f379bafe94` ✓ |
| CSV parse QC | Passed — Python `csv.DictReader` no errors ✓ |
| Content alignment | Matches `assignment-objective.md` and `assignment-subjective.md` ✓ |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) ✓ |
| Question bodies | No Q-number/difficulty prefix on objective rows; options without A/B/C labels ✓ |
| Difficulty levels | Easy MCQ `0`; Moderate MCQ/MSQ `0.5`; Hard MSQ `1`; Subjective `0.5` ✓ |
| Markdown preserved | `contentType` = markdown on all rows ✓ |

**Outcome:** CSV **PASSED** QC on iteration 2.

