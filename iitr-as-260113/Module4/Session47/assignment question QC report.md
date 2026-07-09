# Assignment Question QC Report

**Session:** Building Your First n8n Workflow with Forms, Google Sheets, and Conditional Logic

**Files reviewed:** `assignment-objective.md`, `assignment-subjective.md`

**QC standard:** `Command Center/prompts/OS_Assignment_Questions_GenerationPrompt.md`

**Review date:** 2026-07-09

**Iteration:** 3 (subjective rewrite — GreenMart multi-product + Get Order Status)

---

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1–Q10 | Objective | Unchanged from iteration 2. All correct options verified. Relevancy: **Yes**. |
| Q1 | Subjective (Practical, Medium) | **GreenMart** two-workflow build: (1) Form → Switch/IF → 3 Append tabs by product; (2) Manual trigger → 3 Get rows → Code (count/sum) → Order Summary. **11 nodes** total specified with visual maps, field tables, expression for order_value, copy-paste Code template, test data with expected 3/2/730. Plan B for IF fallback. Google Doc submission (case b). Relevancy: **Yes**. |

---

## Structural Compliance Check

| Requirement | Objective | Subjective |
| --- | --- | --- |
| Total Qs | 10 ✓ | 1 ✓ |
| Difficulty | Easy → Moderate → Hard ✓ | Medium ✓ |
| Answer explanation | Per question ✓ | Walkthrough + grading checklist + Plan B ✓ |
| In-syllabus + reasonable extension | ✓ | Core: form, OAuth, append, IF/Switch, expressions. Extension: Get rows + Code for sums (documented with template). No LLM. ✓ |
| Clear submission instructions | ✓ | Google Doc, public link, screenshot list ✓ |
| Node count / build guidance | N/A | **11 nodes** enumerated; step-by-step per node ✓ |
| Test data / expected outputs | N/A | 3 orders + summary 3/2/730 specified ✓ |

---

## Overall QC Ratings

| QC Parameter | Rating / Status | Notes |
| --- | --- | --- |
| **Content Coverage** | **5 / 5** | Covers multi-tab routing, Switch/IF, expressions, read rows, simple aggregation, manual trigger, OAuth, pin/unpin reminder. |
| **Creativity** | **5 / 5** | Realistic grocery order + status dashboard; stronger than single feedback form. |
| **Structural Adherence** | **5 / 5** | One practical task, medium difficulty, complete ideal solution, common mistakes table, Plan B fallback. |
| **No Logical Mistakes** | **True** | Math 160+120+450=730; pending count 2; tab routing logic consistent. |
| **No Presentation Mistakes** | **True** | Clear node maps, tables, no session-reference phrasing, no ambiguous product names. |

---

## Final QC Decision

Expected result met:
- Content Coverage, Creativity, Structural Adherence: all **>= 5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**

Outcome: **PASS** on iteration 3.

---

## Iteration 4 — `assignment.csv` for Assess platform

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) ✓ |
| `tagRelationships` on all rows | `6a4f16baf91319cf8969db90` ✓ |
| CSV parse QC | Passed — Python `csv.DictReader` no errors ✓ |
| Content alignment | Matches `assignment-objective.md` and `assignment-subjective.md` ✓ |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) ✓ |
| Question bodies | No Q-number/difficulty prefix on objective rows; options without A/B/C labels ✓ |
| Difficulty levels | Easy MCQ `0`; Moderate MCQ/MSQ `0.5`; Hard MSQ `1`; Subjective `0.5` ✓ |
| Markdown preserved | `contentType` = markdown on all rows ✓ |
| MCSC answers | 1, 3, 2, 2, 1, 2 ✓ |
| MCMC answers | 1, 2, 3 on Q7–Q10 ✓ |

**Outcome:** CSV **PASSED** QC on iteration 4.
