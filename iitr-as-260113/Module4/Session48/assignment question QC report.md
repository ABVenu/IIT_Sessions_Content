# Assignment Question QC Report

**Session:** Building End-to-End AI Automation Pipelines with n8n

**Files reviewed:** `assignment-objective.md`, `assignment-subjective.md`

**QC standard:** `Command Center/prompts/OS_Assignment_Questions_GenerationPrompt.md`

**Review date:** 2026-07-11

**Iteration:** 1

---

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | MCQ, Easy | Correct: **A** (`localhost:5678`). Relevancy: **Yes** — local n8n access from lecture notes. |
| Q2 | MCQ, Easy | Correct: **B** (Gmail on message received). Relevancy: **Yes** — automatic trigger vs manual form. |
| Q3 | MCQ, Easy | Correct: **B** (system prompt role). Relevancy: **Yes** — Basic LLM chain prompts from notes. |
| Q4 | MCQ, Easy | Correct: **B** (unpin before final run). Relevancy: **Yes** — pin/unpin testing practice. |
| Q5 | MCQ, Moderate | Correct: **A** (Gmail API). Relevancy: **Yes** — Google Cloud OAuth setup for Gmail. |
| Q6 | MCQ, Moderate | Correct: **B** (Merge node). Relevancy: **Yes** — parallel LLM synchronization. |
| Q7 | MSQ, Moderate | Correct: **A, B, D**. Relevancy: **Yes** — sender filter, event type, poll time. |
| Q8 | MSQ, Moderate | Correct: **A, B, D**. Relevancy: **Yes** — Define below, OpenAI credential, node naming. |
| Q9 | MSQ, Hard | Correct: **A, B, C, D**. Relevancy: **Yes** — full pipeline wiring from notes; all four statements accurate. |
| Q10 | MSQ, Hard | Correct: **A, B, C**. Relevancy: **Yes** — fetch test event, JSON export handoff, OpenAI failure; D correctly excluded (no public credential sharing). |
| Q1 | Subjective (Practical, Medium) | **CodeBridge Solutions** single-workflow build: Gmail trigger → parallel summarizer + commentator → Merge → Aggregate → Gmail send (**6 nodes**). Mirrors Session 47 structure: big-picture table, ASCII visual map, Parts A–H, sample Python email body, exact prompts, pin/unpin, 3-test checklist (happy/failure/edge), optional HTML bonus, JSON export, Google Doc submission (case b), common mistakes + grading checklist. Relevancy: **Yes**. |

---

## Structural Compliance Check

| Requirement | Objective | Subjective |
| --- | --- | --- |
| Total Qs | 10 ✓ | 1 ✓ |
| MCQ / MSQ split | 6 MCQ + 4 MSQ ✓ | N/A |
| Difficulty flow | 4 Easy MCQ → 2 Moderate MCQ → 2 Moderate MSQ → 2 Hard MSQ ✓ | Medium ✓ |
| Answer explanation | Per question ✓ | Walkthrough + grading checklist + alternatives ✓ |
| In-syllabus only | ✓ | Gmail trigger, LLM chain, merge, aggregate, send, OAuth, pin/unpin, testing, export — all from lecture notes ✓ |
| No session-reference phrasing | ✓ | ✓ |
| Submission instructions | N/A | Google Doc, public link, screenshot list ✓ |
| Node count / build guidance | N/A | **6 nodes** enumerated; step-by-step per node ✓ |
| Test data / expected outputs | N/A | Sample script, T1/T2/T3 table, reply email criteria ✓ |
| Similar to Session 47 format | N/A | Company scenario, visual map, parts A–H, Plan-style tables, common mistakes ✓ |

---

## Overall QC Ratings

| QC Parameter | Rating / Status | Notes |
| --- | --- | --- |
| **Content Coverage** | **5 / 5** | Covers automatic Gmail trigger, Basic LLM chain, parallel branches, merge/aggregate, Gmail send, OAuth, OpenAI credentials, pin/unpin, pipeline testing, JSON handoff. |
| **Creativity** | **5 / 5** | CodeBridge contractor code-review scenario; applied pipeline build aligned with Session 48 demo use case. |
| **Structural Adherence** | **5 / 5** | 10 objective + 1 subjective; difficulty ordering; complete answer explanations; Session 47-style subjective scaffolding. |
| **No Logical Mistakes** | **True** | Pipeline order, parallel wiring, merge-before-aggregate logic, and test criteria are internally consistent. |
| **No Presentation Mistakes** | **True** | Clear tables, ASCII map, no ambiguous wording, no forbidden session-reference phrasing. |

---

## Final QC Decision

Expected result met:
- Content Coverage, Creativity, Structural Adherence: all **>= 5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**

Outcome: **PASS** on iteration 1.

---

## Iteration 2 — `assignment.csv` for Assess platform

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) ✓ |
| `tagRelationships` on all rows | `6a51e3ee9ff4faa8f8777dea` ✓ |
| CSV parse QC | Passed — Python `csv.DictReader` no errors ✓ |
| Content alignment | Matches `assignment-objective.md` and `assignment-subjective.md` ✓ |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) ✓ |
| Question bodies | No Q-number/difficulty prefix on objective rows; options without A/B/C labels ✓ |
| Difficulty levels | Easy MCQ `0`; Moderate MCQ/MSQ `0.5`; Hard MSQ `1`; Subjective `0.5` ✓ |
| Markdown preserved | `contentType` = markdown on all rows ✓ |
| MCSC answers | 1, 2, 2, 2, 1, 2 ✓ |
| MCMC answers | 1,2,4 / 1,2,4 / 1,2,3,4 / 1,2,3 ✓ |
| Grading rubrics excluded | No evaluator checklist in subjective `answerExplanation` ✓ |

**Outcome:** CSV **PASSED** QC on iteration 2.
