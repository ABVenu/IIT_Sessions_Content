# Lecture Notes QC Report — Project Setup and Scaffolding

**File reviewed:** `Lecture Notes.md`  
**Batch / folder:** `iitr-as-260113/Module4/Session61`  
**Review date:** 2026-08-17

---

## Iteration 1

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | venv, gitignore, secrets, folders, Pydantic, SQLite schema, seed, FastAPI health/ingest/get, pipeline stub, samples, policy.md. |
| **Creativity** | **5 / 5** | Empty office opening day; health lamp; restart test as system-of-record proof. |
| **Structural Adherence** | **4 / 5** | Full files with per-line comments. **Gap:** `str \| None` is fine for 3.10+; startup event is the course FastAPI pattern. First ingest status `ingested` is honest but needed a clearer “do not call Ollama on boot” warning. |
| **No Logical Mistakes** | **False** | Need to keep insert **after** stub pipeline (already true) and forbid seeding `99INVALID` so BADGST can fail later. Seed section now states that. |
| **No Presentation Mistakes** | **True** | Activities student-facing; no session numbers. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

### Expected Result

- All ≥ 5 and flags True — **Not met**

**Outcome:** QC **failed** on iteration 1. Clarified seed must omit invalid GSTIN; done-checklist includes no payout file; line count **495**.

---

## Iteration 2

**Re-review after improvisation.** Line count: **495**. Four S3 images uploaded. SQL uses bound `?` parameters.

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Repository, env, scaffolding, initial implementation (health + ingest + fetch). |
| **Creativity** | **5 / 5** | Passport printer vs tokens; labelled slips as clerk typing. |
| **Structural Adherence** | **5 / 5** | Complete commented files; How the code works; restart activity; Key Takeaways; terminology. |
| **No Logical Mistakes** | **True** | Stub pipeline; SQLite survives restart; secrets gitignored; no NEFT file. |
| **No Presentation Mistakes** | **True** | Confirmed. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

### Expected Result

- All **≥ 5** and flags **True** — **Met**

**Outcome:** QC **passed** on iteration 2.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Initialise repo, venv, secrets | Repository, Environment, and Secrets |
| Scaffold folders | Folder Map on Disk |
| Pydantic, SQLite, FastAPI stubs | Config and Packet; SQLite Schema; FastAPI Doors |
| Seed vendors/POs and policy.md | Seed Function; Sample Policy |
| Prove ticket without a model | Restart Test; What Done Means Today |

---

## Iteration 3 — Logical correctness and pedagogical flow

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Repo, SQL connect, API stubs, seed, restart proof. |
| **Creativity** | **5 / 5** | Empty office / health lamp. |
| **Structural Adherence** | **5 / 5** | Offline-first; LangChain deferred; 496 lines. |
| **No Logical Mistakes** | **True** | Ingest packet allows `amount_inr = 0` and warns not to copy `ge=1`. `INSERT OR REPLACE` matches architecture idempotent ingest so eval/n8n retries do not hit PRIMARY KEY. |
| **No Presentation Mistakes** | **True** | Confirmed. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

**Pedagogical flow:** Keys and gitignore → rooms → packet/schema → samples → doors → restart test → seed. Model is banned on boot so a missing Ollama key cannot block opening day.

**Outcome:** QC **passed** on iteration 3.
