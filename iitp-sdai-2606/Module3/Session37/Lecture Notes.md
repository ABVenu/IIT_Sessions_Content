# GenAI Coding Lab III

In the previous session you **assembled** `campus_api`: persistent student CRUD, `hostel_name`, `?city=`, `/hostels/summary`, middleware, CORS, `campus.log`, and upload/download. Restart still returned Asha.

Today you do not rebuild that project. You use **Claude** on **that same app**: one extra route, ORM query drafts, sample requests, and clearer `/docs`. Claude drafts; you read, run, and own every line.

![Claude drafts as a junior clerk; you stamp campus_api as the registrar](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session37/session37-01-junior-clerk-registrar.png?v=20261009)

## Flow of this session

Follow this order. Do not ask Claude to rewrite `main.py` from a blank file.

1. Start the **existing** `campus_api` and confirm the **ideal features** still work (health, students, summary, upload).
2. Lock the **prompt wrapper** so Claude cannot drop CORS, middleware, files, or summary.
3. Draft **GET `/students/high-marks`**, review it, paste it, test it in `/docs`.
4. Draft **ORM `select()`** queries (high marks, no hostel, summary join) and run them in `campus_api`.
5. Draft **request/response examples** and **docstrings** that match `StudentOut`.
6. Run the **checklist**. Reject anything that undoes persistence or strips a route from the table below.

## Ideal features of the campus backend (keep these)

This is the same product as the previous session. Claude may **add** one filter. Claude may **not** replace the office with a notices list.

**Must still work after every paste**

- GET `/health` reads `.env`
- Student CRUD in `campus.db` survives restart; JSON includes `hostel_name`
- GET `/students?city=` (do not add `/students/by-city`)
- GET `/hostels` and GET `/hostels/summary` (Guest House count 0, average `null`)
- Middleware headers, CORS for port 5500
- POST create still writes `campus.log`
- POST `/upload` and GET `/download/{name}`

**Routes already built (do not delete)**

| Method | Path | Role |
| --- | --- | --- |
| GET | `/health` | Liveness + app name |
| GET | `/hostels` | Parent ids |
| GET | `/hostels/summary` | COUNT and AVG |
| GET | `/students` | List; optional `?city=` |
| GET | `/students/{student_id}` | One row or 404 |
| POST | `/students` | Create + background log |
| PUT | `/students/{student_id}` | Full body replace |
| DELETE | `/students/{student_id}` | Remove row |
| POST | `/upload` | Multipart file |
| GET | `/download/{name}` | File body |

**Route this lab adds with Claude**

| Method | Path | Role |
| --- | --- | --- |
| GET | `/students/high-marks?min_marks=` | Students with marks ≥ that number; `StudentOut` list |

Connecting idea: If a keep-route disappears after a chat paste, restore `main.py` and ask for a **diff** only.

![Keep health, students, summary, and upload; add a High Marks Filter window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session37/session37-03-keep-routes-add-filter.png?v=20261009)

## What you will learn while using Claude

- An **AI-assisted workflow** on this backend, not a new project
- Prompts for a skeleton, ORM queries, examples, and `/docs` text
- How to reject drafts that undo the feature table

Keep the previous folder. Activate the same venv. Start Uvicorn.

```bash
cd campus_api  # Same assembled app
source .venv/bin/activate  # Same venv
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000  # Test drafts against the live API
```

## AI-assisted workflows for this app

![Five stations: Brief, Prompt, Review, Run in Docs, Refine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session37/session37-02-ai-workflow-stations.png?v=20261009)

- **AI-assisted workflow**
  - *Official Definition:* A repeatable loop of brief, prompt, review, run, and refine, where a language model drafts code or docs and a developer accepts only what matches the real application.
  - *In Simple Words:* You write the order slip. Claude types. You stamp only what still matches `campus_api`.
  - *Real-Life Example:* “Add GET `/students/high-marks?min_marks=85` using our Student model” is a workflow. “Write my backend” is not.
- **Claude**
  - *Official Definition:* An AI coding assistant you chat with in a browser. It generates text, including Python, from your prompt.
  - *In Simple Words:* A fast junior who has not opened your `campus.db` or your `.env`.
  - *Real-Life Example:* The clerk has never seen `hostel_name` as a **property**. If you omit that, the draft will add a fake column.

Need: The mini app already has CRUD, summary, files, and CORS. A fifth similar filter is faster to **review** than to invent, if the running app stays the source of truth.

Logic: Claude does not run Uvicorn. It cannot see **X-Campus**, `campus.log`, or a 404. A tidy function with no `commit` still fails persistence.

Common error: “Make it better” on the whole of `main.py`. Claude may drop CORS, middleware, or `/upload`. Ask for **one** extra piece.

Safe habit: never paste `.env` values, real student emails, or access keys into the chat. Use the Asha sample on this page.

| Step | What you do | Why it matters |
| --- | --- | --- |
| 1. Brief | Name path, method, and model | Stops a notices-list rewrite |
| 2. Prompt | Paste only the fields Claude needs | `Student` columns, `get_db`, `StudentOut` |
| 3. Review | Check commit, names, and existing routes | Catch a list in memory |
| 4. Run | Paste into `campus_api` and use `/docs` | Chat cannot prove restart |
| 5. Refine | Ask for a **diff**, not a new `main.py` | Keeps CORS, files, and summary |

Connecting idea: The frontend GenAI lab used this loop on a page. Today the loop targets the assembled FastAPI + ORM app. **What Claude cannot replace:** Uvicorn, `/docs`, `campus.db` after restart, and the feature table at the top.

## Prompt wrapper for campus_api

Lock the stack you already run. Replace only the TASK line.

```text
You are drafting code for the existing FastAPI app campus_api.
Do not replace main.py. Do not use an in-memory list.
Do not remove CORSMiddleware, the HTTP middleware, BackgroundTasks, /upload, /download, or /hostels/summary.
Use SQLAlchemy 2: select(), Session, db.scalars().
Inject the session with db: Session = Depends(get_db).
Student columns: id, full_name, email, city, marks, hostel_id.
hostel_name is a @property on Student from the Hostel relationship.
StudentCreate: full_name, email, city, marks, hostel_id optional.
StudentOut includes hostel_name.
GET /students already supports ?city=. Do not duplicate that filter.
TASK: <one sentence>
Return only the new function or query, with a comment on every line.
```

How the prompt works:

- The “do not remove” list protects the capstone. Claude likes to simplify a file down to CRUD only.
- `?city=` is already in the app. A new city path would clash with that query.

Activity: Save the wrapper. You will reuse it below. Do not add secrets to it.

## Generate a FastAPI endpoint skeleton

- **Endpoint skeleton**
  - *Official Definition:* A route function with the correct decorator, parameters, dependency, and return shape, before extra rules are added.
  - *In Simple Words:* One new counter window on the same office.
  - *Real-Life Example:* High-marks filter. It must still use `get_db` and `StudentOut`.

TASK:

```text
TASK: Write GET /students/high-marks with required query min_marks: int.
Return Student rows where marks >= min_marks, ordered by marks descending.
response_model=list[StudentOut], Depends(get_db).
Place the path so it does not clash with /students/{student_id}.
Do not rewrite POST, PUT, files, or summary.
```

A review-ready draft:

```python
from fastapi import Depends, Query  # Query reads ?min_marks=
from sqlalchemy import select  # SELECT
from sqlalchemy.orm import Session  # Session type
from models import Student, get_db  # Table and dependency
from schemas import StudentOut  # Response shape


@app.get("/students/high-marks", response_model=list[StudentOut])  # Static path, before {student_id}
def list_high_marks(  # Handler
    min_marks: int = Query(..., ge=0, le=100),  # Required query; marks range
    db: Session = Depends(get_db),  # Same session as CRUD
):  # End signature
    rows = db.scalars(  # Read only
        select(Student)  # Mapped columns
        .where(Student.marks >= min_marks)  # ORM WHERE
        .order_by(Student.marks.desc())  # Highest first
    ).all()  # Empty list is 200
    return rows  # StudentOut, including hostel_name
```

How the code works:

- Put this function **above** GET `/students/{student_id}`. If `high-marks` sits below that path, FastAPI may parse the word as an integer id and return **422**.
- This is not `?city=`. City already exists. This filter is **marks**, the same 85 cutoff you used in the ORM scripts (Meera, Asha, Neha).
- GET must not `commit` or `add`.

Activity: After the five campus POSTs, call GET `/students/high-marks?min_marks=85`. You should see Meera 91, Asha 90, Neha 85. Then try `min_marks=92`. `[]` and **200** is correct.

Asha’s object in that list should still include `"hostel_name": "Pune House"`. If Claude’s draft returns tuples `(name, marks)`, it skipped `StudentOut`. Reject it.

```json
{
  "id": 1,
  "full_name": "Asha Rao",
  "email": "asha@example.com",
  "city": "Pune",
  "marks": 90,
  "hostel_id": 1,
  "hostel_name": "Pune House"
}
```

Common error: Claude returns `students = []` and `append`. Reject it. Persistence already lives in `campus.db`.

Common doubt: “Should I delete GET `/students`?” No. The full list and `?city=` stay.

## Generate SQLAlchemy ORM queries

- **ORM query draft**
  - *Official Definition:* A `select()` produced from a plain-English filter, meant to run on your mapped classes.
  - *In Simple Words:* You say “marks at least 85.” Claude types the `where`.
  - *Real-Life Example:* The assembled app already has `/hostels/summary`. A query draft must use `Hostel` and `Student`, not `enrolments`.

TASK:

```text
TASK: Write one SQLAlchemy 2 query that returns Student rows with marks >= 85,
ordered by marks descending. Use SessionLocal and session.scalars.
Do not write FastAPI. Do not use session.query().
```

```python
from sqlalchemy import select  # SELECT builder
from models import Student, SessionLocal  # Same campus_api models


with SessionLocal() as session:  # Same campus.db as Uvicorn
    high_marks = session.scalars(  # Objects
        select(Student)  # Table
        .where(Student.marks >= 85)  # Filter
        .order_by(Student.marks.desc())  # 91, 90, 85
    ).all()  # List
    for student in high_marks:  # Meera, Asha, Neha on the sample
        print(student.full_name, student.marks, student.hostel_name)  # Property needs an open session
```

How the code works:

- Run this **inside** `campus_api` so `campus.db` is the API’s file, not `campus_orm`.
- `hostel_name` works here because the `with` block is still open. That is the same property the route uses.

Second TASK: students with no hostel.

```python
from sqlalchemy import select  # SELECT
from models import Student, SessionLocal  # Factory


with SessionLocal() as session:  # Same file
    no_hostel = session.scalars(  # Neha
        select(Student).where(Student.hostel_id.is_(None))  # IS NULL
    ).all()  # List
    print([student.full_name for student in no_hostel])  # ['Neha Shah'] after her POST
```

How the code works:

- `.is_(None)` is the column test. Prefer it over `Student.hostel == None` for this filter.
- If Claude joins `enrolments`, delete that join. This app has `Hostel` and `Student` only.

Activity: Run both scripts after the five POSTs. If both lists are empty, Uvicorn was started in another folder.

Connecting idea: The high-marks query is what the new route should execute. If they disagree, the skeleton is wrong.

You can also ask Claude to **restate** the summary query you already ship, not to invent a new table.

```text
TASK: Write SQLAlchemy 2 for GET /hostels/summary: from Hostel, outerjoin Student,
count Student.id, avg Student.marks, group by hostel_name.
Empty hostels must remain with count 0. Do not write FastAPI.
```

A pass matches the previous session: `select_from(Hostel).outerjoin(Student, ...)`, `func.count(Student.id)`, `func.avg(Student.marks)`. An inner join that drops Guest House is a fail. Do not paste a second summary route if `/hostels/summary` already works; use this TASK only to check that Claude understands the app.

Activity: Compare Claude’s summary SQL/ORM with `hostel_summary` in `main.py`. If the join type differs, keep your file. Tell Claude “outerjoin, keep Guest House.”

## Produce sample requests and responses

- **API example**
  - *Official Definition:* A pair of sample HTTP request JSON and response JSON for one route, used in docs or tests.
  - *In Simple Words:* A filled form and a filled receipt from **this** app.
  - *Real-Life Example:* POST Meera, including `hostel_name` on the 201 — because `StudentOut` has that key.

TASK:

```text
TASK: For POST /students, write valid JSON for Meera Iyer (marks 91, hostel_id 2)
and the 201 response assuming id 3, including hostel_name Chennai House.
Then the 422 shape if email is missing.
Do not add keys that are not on StudentOut. Do not invent JWT.
```

**Request (201 path)**

```json
{
  "full_name": "Meera Iyer",
  "email": "meera@example.com",
  "city": "Chennai",
  "marks": 91,
  "hostel_id": 2
}
```

**Response 201**

```json
{
  "id": 3,
  "full_name": "Meera Iyer",
  "email": "meera@example.com",
  "city": "Chennai",
  "marks": 91,
  "hostel_id": 2,
  "hostel_name": "Chennai House"
}
```

**Response 422** (email omitted) — you need `loc`, `msg`, and `type` inside `detail`.

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "email"],
      "msg": "Field required"
    }
  ]
}
```

How the examples work:

- Request has no `id` and no `hostel_name`. Response has both. That matches `StudentCreate` versus `StudentOut`.
- If Claude omits `hostel_name` on the 201, the example does not match the app you built in the previous session.
- 422 is Pydantic. No INSERT ran. `campus.log` should not gain a line.

Activity: Paste the Meera body into POST `/students` only if she is not already stored. Compare live 201 with the draft. Then POST `{"full_name": "X"}` and compare `loc`.

Ask Claude for GET `/students/99`: no body, **404** `{"detail": "Student not found"}` — your `HTTPException` string, not “Item not found.”

Ask for a PUT pair for Imran marks 75. The request must include **every** `StudentCreate` field. A body with only `"marks": 75` is **422** on this app.

Ask for an **upload** example: POST `/upload` is multipart, not JSON. If Claude writes `{"file": "..."}` as JSON, reject it. The previous session’s picker in `/docs` is the right client for that route.

**PUT `/students/4` request** (full body, not marks alone):

```json
{
  "full_name": "Imran Khan",
  "email": "imran@example.com",
  "city": "Lucknow",
  "marks": 75,
  "hostel_id": 3
}
```

**GET `/hostels/summary` Guest House** after the five POSTs, before anyone is assigned there:

```json
{
  "hostel_name": "Guest House",
  "student_count": 0,
  "average_marks": null
}
```

If Claude’s summary example uses `"average_marks": 0` for Guest House, it treated COUNT of an empty left join as an average of zero. Keep `null`.

Connecting idea: Examples are contracts. Documentation is those contracts written on `/docs` so the page describes the campus, not a blank “Items.”

## Improve API documentation with AI

FastAPI already builds Swagger from types. Claude can draft **docstrings** and the app `description`. You paste only what stays true of `campus_api`.

- **API documentation (assistant-aided)**
  - *Official Definition:* Human-readable route text generated or improved by an assistant, then checked against the running OpenAPI page.
  - *In Simple Words:* Labels on counters that already exist.
  - *Real-Life Example:* Mention SQLite, unique email, optional hostel, summary, files — not JWT.

TASK:

```text
TASK: Write a one-paragraph FastAPI description for campus_api and a docstring for create_student.
Mention campus.db, unique email, optional hostel_id, /hostels/summary, upload/download, and 404 on missing ids.
Do not claim JWT. Do not mention enrolments. Do not change Python logic.
```

```python
app = FastAPI(  # Same object
    title=os.getenv("APP_NAME", "Campus API"),  # Still from .env
    description=(  # Factual subtitle
        "Assembled campus backend. Students persist in SQLite (campus.db). "
        "POST /students requires full_name, email, city, and marks. email is unique. "
        "hostel_id is optional. GET /hostels/summary returns COUNT and AVG per hostel. "
        "POST /upload and GET /download/{name} handle files. Missing student ids return 404."
    ),  # End string
    version="1.0.0",  # Unchanged
)  # End FastAPI()
```

```python
@app.post("/students", response_model=StudentOut, status_code=201)  # Unchanged decorator
def create_student(payload: StudentCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):  # Unchanged signature
    """Create a student in campus.db and log the email after the response."""  # Shown in /docs
    student = Student(  # Unchanged mapping
        full_name=payload.full_name,  # Name
        email=payload.email,  # Email
        city=payload.city,  # City
        marks=payload.marks,  # Marks
        hostel_id=payload.hostel_id,  # Optional
    )  # End
    db.add(student)  # INSERT
    db.commit()  # Persist
    db.refresh(student)  # id
    background_tasks.add_task(append_log, "created:" + student.email)  # Keep the log
    return student  # StudentOut
```

How the code works:

- Only strings changed. CORS, middleware, and files stay. If Claude’s paste removes `BackgroundTasks`, reject it.
- Refresh `/docs`. The POST box should show the docstring. The top paragraph should mention summary and files.

Activity: Ask Claude for an OpenAPI example on GET `/hostels/summary` for Guest House (`student_count` 0, `average_marks` null). Paste only if that matches the previous session’s outer join.

Activity: In `/docs`, after you paste a docstring, confirm **POST `/upload`** still shows a file picker. If it became a JSON body, Claude overwrote the wrong function.

Common error: A “docs” reply that rewrites `create_student` without `commit`. Ask for **documentation only**.

## Refine what Claude returns

Ask for a **minimal diff**.

```text
Keep list_high_marks. Change only the default sort to full_name after marks.
Do not touch create_student, CORS, or /upload.
Show only the updated function, with a comment on every line.
```

Activity: Ask Claude, on purpose, “add JWT to create_student.” You should **not** paste the reply. The assembled app has no login. That fails the checklist.

Activity: Ask Claude, on purpose, “store students in a Python list.” Mark it as fail: it undoes persistence.

Activity: Ask Claude to “simplify main.py.” If the reply deletes `/hostels/summary` or `/upload`, it failed the keep-list in the wrapper. Keep your assembled file.

## Review checklist before you keep a draft

![Registrar stamps PASSED on get_db and commit; REJECTED on a memory list](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session37/session37-04-review-checklist-stamps.png?v=20261009)

| Check | Pass | Fail — reject or re-prompt |
| --- | --- | --- |
| Session | `Depends(get_db)` | New global session left open |
| Writes | `db.commit()` on POST/PUT/DELETE | JSON with no commit |
| GET | No `db.add` | GET that inserts |
| Model | `Student` from `models.py` | `class Student(BaseModel)` as a table |
| Columns | `full_name`, `marks`, `hostel_id` | `name`, `score` |
| `hostel_name` | Property / `StudentOut` | Extra stored column |
| Existing app | CORS, middleware, files, summary still there | Simplified CRUD-only `main.py` |
| City filter | Left as `?city=` | New duplicate `/students/by-city` |
| Path order | `/students/high-marks` above `{id}` | Word parsed as int |
| Examples | Keys on `StudentOut` | Missing `hostel_name`, or JWT |
| Docs | Facts about this app | Enrolments, PostgreSQL-only claims |
| Secrets | Asha sample only | Pasted `.env` |

Connecting idea: The checklist is the lab. Claude is the typist. The assembled app from the previous session is the register.

## If something breaks — check this list

| What you see | Likely cause | What to do |
| --- | --- | --- |
| Draft uses `session.query` | Old SQLAlchemy | Re-prompt `select()` / `scalars()` |
| Draft uses `students = []` | Notices-board pattern | Re-prompt: no in-memory list |
| CORS / upload vanished after paste | Whole-file rewrite | Restore `main.py`; ask for one function |
| `/docs` example missing `hostel_name` | Claude used Create schema | Match `StudentOut` |
| `high-marks` 422 about int | Route below `{student_id}` | Move it above the id route |
| Empty query script | Wrong folder’s `campus.db` | Run inside `campus_api` |
| Docstring mentions JWT | Extra story | Delete those sentences |
| `campus.log` silent after AI POST | `BackgroundTasks` dropped | Put `add_task` back |
| `.env` in the chat | Secret paste | Stop; use APP_NAME only in local files |
| Summary example average 0 | Empty hostel treated as zero | Keep `null` for Guest House |
| Two `create_engine` calls | Extra models file in the draft | One engine in `campus_api/models.py` |
| Health lost `Depends(get_settings)` | Claude rewrote `/health` | Restore `.env` app name in the body |

## Key Takeaways

- This lab uses **Claude on the same `campus_api`** you assembled: persistent CRUD, query filters, hostel summary, middleware, CORS, background log, and files.
- An **AI-assisted workflow** is brief → prompt → review → run in `/docs` → refine a **diff**. Claude does not replace Uvicorn or `campus.db`.
- **Skeletons** must reuse **`Depends(get_db)`** and **`StudentOut`**. A list in memory, or a rewrite that drops CORS and files, is a failed draft.
- **ORM drafts** use `select()` and the real columns. **Examples** and **docstrings** must match `hostel_name`, 404 text, and the summary.
- Keep this review habit when you extend the mini app. The stamped register is your running code, not the chat window.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
| --- | --- |
| `campus_api` | Assembled app from the previous session |
| Claude | Assistant for backend drafts |
| Prompt wrapper | Stack rules plus one TASK |
| Endpoint skeleton | One new route, not a new project |
| `GET /students/high-marks` | Example extra filter on marks |
| ORM query draft | `select()` + `where` on `Student` |
| `hostel_id.is_(None)` | Neha’s empty hostel |
| API example | Request + response for this `StudentOut` |
| Docstring / `description` | `/docs` text only |
| Review checklist | Session, commit, existing features, facts |
| Source of truth | Running `campus_api`, not the chat |
| Minimal diff | Follow-up that changes one function |
| No in-memory list | Blocks the old notices CRUD |
| Keep-list in the wrapper | CORS, middleware, files, summary must survive a paste |
