# Lecture Notes QC Report — Session 64 (Buffer & Submission)

## Iteration 1

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 4 | Checklist/README/stretch/review present; length short |
| Creativity | 5 | Passport file vs shopping bag; stretch doors vs vault |
| Structural Adherence | 4 | Partner activity used a clock duration |
| No Logical Mistakes | False | Stretch A `/ingest` with empty chunks would fail closed — now stated as correct |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |

**Fixes applied:** seed script never inserts `99INVALID`; stretch only after G01–G03; cache GST not `ready_to_pay`; README cold-start without a time limit; exam defence table; SUBMISSION.md checklist.

## Iteration 2

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Checklist, README, one stretch A/B/C, cross-team review, course wrap |
| Creativity | 5 | |
| Structural Adherence | 5 | No session numbers; no duration; support hours as upcoming not a second product |
| No Logical Mistakes | True | Same graph for hatch; human stamp cannot self-approve |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |

Expected QC result achieved.

## Iteration 3 — Logic, flow, taught-stack only

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Checklist, README, one stretch, cross-team review |
| Creativity | 5 | |
| Structural Adherence | 5 | Stretch uses Groq JSON / LangGraph checkpoint / cache — not a new API stack |
| No Logical Mistakes | True | No `/ingest` with empty fake chunks; labelled G01–G03 still the submit bar |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |
| Taught-stack only | True | Removed FastAPI, Pydantic, uvicorn, chromadb from `requirements.txt` |

**Stretch A** is now Groq messy extract (`json` + env key). **Not** FastAPI/Pydantic/SQLAlchemy.

