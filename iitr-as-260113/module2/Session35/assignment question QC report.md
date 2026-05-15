# Assignment Question QC Report
**Session:** Session 35 — Tool Integration in AI Agents
**Course:** iitr-as-260113 | Module 2

---

## Section 1: Objective Assignment QC

| Q# | Type | Correct Option | Correct Option Relevant to Question? | Remarks |
|----|------|----------------|--------------------------------------|---------|
| Q1 | MCQ (Easy) | B) Weather API tool via agent runtime | Yes | Tests why agents need external tools for live data. Distractors target context window, manual HTML, and guessing. |
| Q2 | MCQ (Easy) | B) Agent runtime validates and executes | Yes | Tests LLM vs runtime responsibility split in function calling. Distractors cover direct LLM DB access and frontend-only access. |
| Q3 | MCQ (Easy) | C) JSON | Yes | Tests JSON as API wire format in a flight-search argument scenario. Distractors are CSV, XML-only, and binary-only. |
| Q4 | MCQ (Easy) | A) Microservices composed through APIs | Yes | Maps multi-tool agents to microservice-style API composition. Other options describe anti-patterns from the notes. |
| Q5 | MCQ (Moderate) | B) Pydantic returns structured validation error | Yes | Tests `ProductSearchInput` type validation before DB access. Distractors cover silent coercion, SQLite errors, and LLM rewrite. |
| Q6 | MCQ (Moderate) | B) SQLAlchemy is a Python toolkit, not the DB engine | Yes | Tests SQLAlchemy vs database engine distinction. Distractors confuse server role, JSON-only use, and Pydantic overlap. |
| Q7 | MSQ (Moderate) | A, B, D, E | Yes | Covers direct answer vs tool path, structured arguments, runtime execution, and tool metadata. Option C (model dials APIs directly) is the key false statement. |
| Q8 | MSQ (Moderate) | A, B, C, E | Yes | Maps HTTP verbs and status codes in tool/API contexts. Option D swaps **201** with client validation failure (**400**). |
| Q9 | MSQ (Hard) | A, B, C, D, F | Yes | Validates ORM query style, default `in_stock`, ORM result shape, re-seed duplication, and SQLite engine URL. Option E (`max_price: 0`) conflicts with `gt=0`. |
| Q10 | MSQ (Hard) | A, B, C, E, F | Yes | End-to-end agent stack: routing, Pydantic, ORM read, JSON APIs, production auth. Option D (LLM writes SQLite) is false. |

---

## Section 2: Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Mentioned | Dataset / Input Provided | Remarks |
|----|------|------------|-----------------------------------|--------------------------|---------|
| Q1 | Practical Coding — GadgetMart product search tool (3 tasks) | Medium | Yes (Case C — single `gadgetmart_search_tool.py`, run and verify, submit in LMS) | Yes — six-row seed table, hard-coded agent arguments, invalid-input check, and expected print lines in one prompt | One medium question with three tasks (catalog, validated tool, simulated agent run); shorter than the prior seven-step version. Pydantic boundary, ORM `select().where()`, structured errors, and three in-stock mobiles under ₹50,000 verified. |

---

## Section 3: Overall Assignment Quality Ratings

### Objective Assignment

| Criteria | Rating (1–5) | Notes |
|----------|-------------|-------|
| Content Coverage | 5 | Covers tools vs chat-only models, function calling, runtime execution, JSON wire format, microservices analogy, Pydantic validation, SQLAlchemy role, ORM queries, tool metadata, HTTP methods/status codes, and production auth. |
| Creativity | 5 | Scenario-based prompts (helpdesk weather, GadgetMart, flight JSON, campus/e-commerce services). No session-reference phrasing. |
| Structural Adherence | 5 | Exactly 10 questions: 6 MCQs (4 Easy + 2 Moderate) + 4 MSQs (2 Moderate + 2 Hard). Ordered Easy → Moderate → Hard. Full answer explanations with incorrect-option reasoning. |
| No Logical Mistakes | True | Correct answers and distractors checked against lecture notes and demo constraints (`max_price` > 0, runtime vs LLM roles, status-code families). |
| No Presentation Mistakes | True | Consistent headings, tables, and option formatting; grammar and spelling reviewed. |

### Subjective Assignment

| Criteria | Rating (1–5) | Notes |
|----------|-------------|-------|
| Content Coverage | 5 | One question with three tasks covers ORM setup and idempotent seeding, Pydantic validation and ORM search, and simulated agent flow with CLI output. |
| Creativity | 5 | GadgetMart storyline with a leaner task list than the seven-step draft; applied tool-boundary framing without session-reference phrasing. |
| Structural Adherence | 5 | One medium practical question; three tasks max; Case C submission; embedded dataset; ideal solution and alternative approach in explanation. |
| No Logical Mistakes | True | Empty-table seed guard, three-product filter under ₹50,000 in stock, invalid `category` type returns `success: False` without querying, and expected print lines verified by execution. |
| No Presentation Mistakes | True | Task labels, expected output, and code blocks are clear and consistent. |

---

## QC Summary

All ratings meet the required threshold (5/5). No logical or presentation mistakes detected.
Both assignments are approved and ready for platform upload.
