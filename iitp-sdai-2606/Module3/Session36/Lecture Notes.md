# Hands-on Backend – Mini End-to-End Application

A hostel office is not one window. The desk takes a slip, a stamp goes on every visit, a page on another port may call, a file is filed, and the register in the cupboard must still be there tomorrow.

You have already practised each of those jobs in isolation: FastAPI, Pydantic, **Depends**, middleware, CORS, background tasks, files, SQL summaries, and SQLAlchemy models in `campus_orm`. Today you **assemble** them into one `campus_api` app. Upcoming work uses an AI assistant on this same app; today you type and run it yourself.

![HTTP desk and campus.db cupboard join as one campus_api office](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session36/session36-01-desk-and-cupboard.png?v=20261009)

## Flow of this session

Follow this order. Do not POST a student before the files and hostels exist.

1. Read the **ideal features** and the **route table** so you know what “done” looks like.
2. Create the `campus_api` folder, venv, `.env`, and the three Python files.
3. Define **models** and **`get_db`**, then the **Pydantic** schemas.
4. Assemble **main.py**: health, CORS, middleware, hostels, student CRUD, summary, files.
5. Start Uvicorn and walk **every route** in `/docs` (or Postman), including a restart that keeps the rows.

## Ideal features of the campus backend

The product is a small campus API. A page on port **5500** may call it. Student rows live in **`campus.db`**, must survive a Uvicorn restart, and must not fall back to the old notices list.

**Features the finished app must have**

- Health check that reads **`.env`**
- Hostel list so POST can use a real `hostel_id`
- Student **CRUD** with Pydantic bodies; JSON includes **`hostel_name`** from the relationship
- Optional **`?city=`** filter on the student list
- **GET `/hostels/summary`**: COUNT and AVG per hostel; Guest House stays with count 0
- Middleware stamp on every reply; **CORS** for port 5500
- Background line in **`campus.log`** after create
- **Upload** and **download** a file

**Routes to build**

| Method | Path | Request | Success |
| --- | --- | --- | --- |
| GET | `/health` | none | `status`, `app` from `.env` |
| GET | `/hostels` | none | list of `{id, hostel_name}` |
| GET | `/hostels/summary` | none | `{hostel_name, student_count, average_marks}` |
| GET | `/students` | optional `?city=` | list of `StudentOut` |
| GET | `/students/{student_id}` | path id | one `StudentOut`, or **404** |
| POST | `/students` | `StudentCreate` JSON | **201** `StudentOut`; then `campus.log` |
| PUT | `/students/{student_id}` | full `StudentCreate` | updated `StudentOut`, or **404** |
| DELETE | `/students/{student_id}` | path id | `{detail: ...}`, or **404** |
| POST | `/upload` | multipart file | `{filename, bytes}` |
| GET | `/download/{name}` | path file name | file body, or JSON **404** |

`StudentOut` fields: `id`, `full_name`, `email`, `city`, `marks`, `hostel_id`, `hostel_name`. `StudentCreate` has no `id` and no `hostel_name`. A missing email on POST is **422**, before any INSERT.

Connecting idea: The notes below implement this table, skill by skill. If a route is missing at the end, the assemble is not finished.

![Campus office counters for health, hostels, students, summary, and files](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session36/session36-03-campus-api-counters.png?v=20261009)

## What you will learn while building it

- How those routes share **one** request path: schema → `Depends(get_db)` → ORM → `campus.db`
- How query params, middleware, CORS, background tasks, and files sit on the same `app`
- How to prove persistence with a restart in `/docs`

Work in a new folder. Activate a venv. Install the packages this app actually imports.

```bash
mkdir campus_api  # One project for the assembled backend
cd campus_api  # Enter it
python3 -m venv .venv  # Same kit as the first FastAPI setup
source .venv/bin/activate  # Turn the venv on
pip install fastapi uvicorn sqlalchemy python-dotenv  # API, server, ORM, .env loader
```

```
campus_api/
  .env             # APP_NAME and CORS origin; not committed
  .gitignore       # Ignores .venv, .env, campus.db, uploads
  models.py        # Engine, Hostel, Student, get_db
  schemas.py       # Pydantic contracts
  main.py          # Routes, middleware, CORS, files, summary
  uploads/         # Created on first upload
  campus.db        # Created on first Uvicorn start
```

Save `.env`:

```
APP_NAME=Campus API
CORS_ORIGIN=http://127.0.0.1:5500
```

Save `.gitignore` with `.venv/`, `.env`, `campus.db`, and `uploads/`. Do not copy `campus.db` from `campus_orm`. This app owns its own file.

## Models and a session for each request

Two FastAPI-only changes sit on the models you already wrote: `check_same_thread=False`, and **`get_db`**. `hostel_name` is a Python shortcut over the relationship — the ORM form of reading the hostel table beside the student.

Save as `models.py`.

```python
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine  # Types and engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker  # Base, link, factory

engine = create_engine(  # SQLite beside main.py
    "sqlite:///campus.db",  # App-owned file
    connect_args={"check_same_thread": False},  # Server thread may use SQLite
)  # End engine
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)  # One tray per request


class Base(DeclarativeBase):  # Parent of table classes
    pass  # No extra columns


class Hostel(Base):  # Parent table
    __tablename__ = "hostels"  # Table name
    id = Column(Integer, primary_key=True)  # Primary key
    hostel_name = Column(String, unique=True, nullable=False)  # Building name
    students = relationship("Student", back_populates="hostel")  # One-to-many


class Student(Base):  # Child table for CRUD
    __tablename__ = "students"  # Table name
    id = Column(Integer, primary_key=True)  # Primary key
    full_name = Column(String, nullable=False)  # Name
    email = Column(String, unique=True, nullable=False)  # Unique email
    city = Column(String, nullable=False)  # Used as a query filter
    marks = Column(Integer, nullable=False)  # Used in the hostel summary
    hostel_id = Column(Integer, ForeignKey("hostels.id"), nullable=True)  # Optional parent
    hostel = relationship("Hostel", back_populates="students")  # JOIN as an attribute

    @property  # Not a stored column
    def hostel_name(self):  # For StudentOut
        return self.hostel.hostel_name if self.hostel is not None else None  # Empty for Neha


def get_db():  # Depends target
    db = SessionLocal()  # Open
    try:  # Route runs here
        yield db  # Injected Session
    finally:  # After the response
        db.close()  # Always close
```

How the code works:

- `commit` is still your job. `get_db` only opens and closes.
- `student.hostel_name` uses the relationship while the session is open. After `get_db` closes, do not lazy-load. Return `StudentOut` inside the route.

## Pydantic contracts

Save as `schemas.py`.

```python
from typing import Optional  # hostel fields may be empty
from pydantic import BaseModel, ConfigDict  # Schemas


class StudentCreate(BaseModel):  # POST and PUT body
    full_name: str  # Required
    email: str  # Required
    city: str  # Required; also a query on GET list
    marks: int  # Required
    hostel_id: Optional[int] = None  # Optional parent id


class StudentOut(BaseModel):  # JSON out
    model_config = ConfigDict(from_attributes=True)  # Read ORM attributes
    id: int  # Database id
    full_name: str  # Name
    email: str  # Email
    city: str  # City
    marks: int  # Marks
    hostel_id: Optional[int]  # May be null
    hostel_name: Optional[str]  # From the relationship, not a student column


class HostelOut(BaseModel):  # GET /hostels
    model_config = ConfigDict(from_attributes=True)  # ORM objects
    id: int  # Id used as hostel_id
    hostel_name: str  # Building


class HostelSummary(BaseModel):  # GET /hostels/summary
    hostel_name: str  # Group label
    student_count: int  # COUNT of students
    average_marks: Optional[float]  # AVG, or null when the hostel is empty
```

How the code works:

- `StudentCreate` has no `id` and no `hostel_name`. The client does not invent those.
- `hostel_name` on output is the JOIN you used to print Pune House beside Asha. It is not a second stored name on `students`.

## Assemble the application in main.py

This file is the desk: settings, CORS, a stamp on every reply, CRUD, a summary, a background log, and files. You already know each tool. Here they share one `app`.

![One POST of Asha walks HTTP, Pydantic, session, ORM model, then campus.db](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session36/session36-02-request-layers.png?v=20261009)

Save as `main.py`.

```python
import os  # .env values and file paths
import time  # Middleware clock
from fastapi import BackgroundTasks, Depends, FastAPI, File, HTTPException, Query, Request, UploadFile  # Web tools
from fastapi.middleware.cors import CORSMiddleware  # Browser guest list
from fastapi.responses import FileResponse, JSONResponse  # File bytes and JSON errors
from sqlalchemy import func, select  # SELECT, COUNT, AVG
from sqlalchemy.orm import Session  # Injected session type
from dotenv import load_dotenv  # Load .env
from models import Base, Hostel, Student, SessionLocal, engine, get_db  # Persistence
from schemas import HostelOut, HostelSummary, StudentCreate, StudentOut  # Contracts

load_dotenv()  # Read APP_NAME and CORS_ORIGIN
UPLOAD_DIR = "uploads"  # Folder for POST /upload
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Safe if it already exists

app = FastAPI(  # Uvicorn serves this object
    title=os.getenv("APP_NAME", "Campus API"),  # From .env
    description="Campus mini app: persistent students, summary, files",  # /docs subtitle
    version="1.0.0",  # OpenAPI version
)  # End FastAPI()
app.add_middleware(  # CORS for a page on another port
    CORSMiddleware,  # Same class as before
    allow_origins=[os.getenv("CORS_ORIGIN", "http://127.0.0.1:5500"), "http://localhost:5500"],  # Exact origins
    allow_credentials=False,  # No cookies today
    allow_methods=["*"],  # GET, POST, OPTIONS, ...
    allow_headers=["*"],  # Headers the page may send
)  # End CORS


def get_settings():  # Shared Depends, same idea as before
    return {"app": os.getenv("APP_NAME", "Campus API")}  # Health and welcome


def append_log(line: str):  # Background callable; not a route
    with open("campus.log", "a", encoding="utf-8") as log_file:  # Append
        log_file.write(line + "\n")  # One line after the response


@app.middleware("http")  # Stamp every visit, including /docs
async def stamp_response(request: Request, call_next):  # Must await the chain
    started = time.perf_counter()  # Clock in
    response = await call_next(request)  # Route + get_db + handler
    elapsed_ms = (time.perf_counter() - started) * 1000  # Clock out
    response.headers["X-Process-Time-Ms"] = str(round(elapsed_ms, 2))  # Timing
    response.headers["X-Campus"] = "campus-api"  # Label
    return response  # Always return it


@app.on_event("startup")  # Once per process
def on_startup():  # Tables then hostels
    Base.metadata.create_all(bind=engine)  # CREATE TABLE if missing
    db = SessionLocal()  # Seed session
    try:  # Insert buildings once
        if db.scalars(select(Hostel)).first() is None:  # Empty table
            db.add_all([  # Campus sample names
                Hostel(hostel_name="Pune House"),  # Id 1
                Hostel(hostel_name="Chennai House"),  # Id 2
                Hostel(hostel_name="Lucknow House"),  # Id 3
                Hostel(hostel_name="Guest House"),  # Id 4, no students
            ])  # End list
            db.commit()  # Save hostels
    finally:  # Close seed
        db.close()  # Return connection


@app.get("/health")  # First GET, from the setup lesson
def health(settings: dict = Depends(get_settings)):  # Shared settings
    return {"status": "ok", "app": settings["app"]}  # Proves .env loaded


@app.get("/hostels", response_model=list[HostelOut])  # Parent ids for POST
def list_hostels(db: Session = Depends(get_db)):  # Session
    return db.scalars(select(Hostel).order_by(Hostel.id)).all()  # Four buildings


@app.get("/hostels/summary", response_model=list[HostelSummary])  # COUNT and AVG per hostel
def hostel_summary(db: Session = Depends(get_db)):  # Session
    rows = db.execute(  # Join then group, same idea as SQL summaries
        select(  # One row per hostel
            Hostel.hostel_name,  # Group label
            func.count(Student.id),  # 0 for Guest House
            func.avg(Student.marks),  # None when count is 0
        )  # End select list
        .select_from(Hostel)  # Keep empty hostels
        .outerjoin(Student, Student.hostel_id == Hostel.id)  # LEFT JOIN
        .group_by(Hostel.hostel_name)  # One pile per building
        .order_by(Hostel.hostel_name)  # Stable order
    ).all()  # Tuples
    return [  # Map to HostelSummary
        HostelSummary(  # One JSON object
            hostel_name=name,  # Building
            student_count=count,  # COUNT
            average_marks=None if avg is None else round(float(avg), 1),  # One decimal
        )  # End row
        for name, count, avg in rows  # Unpack
    ]  # End list


@app.get("/students", response_model=list[StudentOut])  # List; optional city query
def list_students(city: str | None = Query(default=None), db: Session = Depends(get_db)):  # Query + session
    stmt = select(Student).order_by(Student.id)  # Base list
    if city is not None:  # Filter when the query is sent
        stmt = stmt.where(Student.city == city)  # WHERE city = ...
    return db.scalars(stmt).all()  # StudentOut, including hostel_name


@app.get("/students/{student_id}", response_model=StudentOut)  # Path parameter
def read_student(student_id: int, db: Session = Depends(get_db)):  # Id + session
    student = db.get(Student, student_id)  # Primary key
    if student is None:  # Missing
        raise HTTPException(status_code=404, detail="Student not found")  # JSON 404
    return student  # hostel_name from the property


@app.post("/students", response_model=StudentOut, status_code=201)  # Create + log after reply
def create_student(payload: StudentCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):  # Body, task, session
    student = Student(  # Table object
        full_name=payload.full_name,  # Copy
        email=payload.email,  # Unique
        city=payload.city,  # City
        marks=payload.marks,  # Marks
        hostel_id=payload.hostel_id,  # May be None
    )  # End Student()
    db.add(student)  # INSERT
    db.commit()  # Persist
    db.refresh(student)  # Load id
    background_tasks.add_task(append_log, "created:" + student.email)  # After JSON
    return student  # 201


@app.put("/students/{student_id}", response_model=StudentOut)  # Replace fields
def update_student(student_id: int, payload: StudentCreate, db: Session = Depends(get_db)):  # Id, body, session
    student = db.get(Student, student_id)  # Load first
    if student is None:  # Missing
        raise HTTPException(status_code=404, detail="Student not found")  # 404
    student.full_name = payload.full_name  # Overwrite
    student.email = payload.email  # Overwrite
    student.city = payload.city  # Overwrite
    student.marks = payload.marks  # Overwrite
    student.hostel_id = payload.hostel_id  # Overwrite
    db.commit()  # UPDATE
    db.refresh(student)  # Reload
    return student  # StudentOut


@app.delete("/students/{student_id}")  # Remove row
def delete_student(student_id: int, db: Session = Depends(get_db)):  # Id + session
    student = db.get(Student, student_id)  # Load
    if student is None:  # Missing
        raise HTTPException(status_code=404, detail="Student not found")  # 404
    db.delete(student)  # DELETE
    db.commit()  # Persist
    return {"detail": "Student deleted"}  # Confirmation


@app.post("/upload")  # Multipart file, same pattern as before
def upload_file(file: UploadFile = File(...)):  # Picker in /docs
    raw = file.file.read()  # Bytes
    safe_name = os.path.basename(file.filename or "unnamed")  # No folders
    if safe_name == "":  # Empty
        return JSONResponse(status_code=400, content={"detail": "filename required"})  # 400
    path = os.path.join(UPLOAD_DIR, safe_name)  # uploads/<name>
    with open(path, "wb") as out:  # Binary write
        out.write(raw)  # Save
    return {"filename": safe_name, "bytes": len(raw)}  # Receipt


@app.get("/download/{name}")  # FileResponse
def download_file(name: str):  # Path is the file name
    safe_name = os.path.basename(name)  # Strip ../
    path = os.path.join(UPLOAD_DIR, safe_name)  # Look in uploads/
    if name != safe_name or not os.path.isfile(path):  # Unsafe or missing
        return JSONResponse(status_code=404, content={"detail": "File not found"})  # JSON 404
    return FileResponse(path, filename=safe_name)  # File body
```

How the code works:

- **GET `/health`** proves `.env` and **Depends(`get_settings`)**. It does not touch the database.
- **CORS** is for a page on port **5500**. `/docs` on 8000 is same-origin and does not prove CORS.
- Middleware adds **X-Campus** and **X-Process-Time-Ms** on every reply, including `/docs`.
- **GET `/students?city=Pune`** is a query filter. Omit `city` to list everyone.
- **`hostel_name`** on a student is the relationship (JOIN). Neha’s value is `null`.
- **GET `/hostels/summary`** is **LEFT JOIN** + **GROUP BY** + **COUNT** / **AVG**. Guest House stays with count 0.
- POST returns JSON first. Then **`campus.log`** gains `created:asha@example.com`. Open the file; do not look for that line in the 201 body.
- Upload and download are the same file pair you already ran, now sitting beside student CRUD.

Common error: Forgetting `db.commit()` on POST. The 201 looks fine until GET after restart is empty.

Common doubt: “Why both middleware and CORSMiddleware?” One stamps headers you wrote. The other is the browser guest list. They are different jobs.

Walk the route table from the start of the notes, in `/docs` or Postman.

## Walk the assembled app

Start the server from `campus_api`:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000  # Serve the mini app
```

Use **`/docs`**. You may send the same JSON from **Postman** (method, URL, body). Do not stop at the first 201. If `/docs` shows 201 and Postman shows 404, you are hitting a different port or folder.

1. **GET `/health`**. `app` should be `Campus API` from `.env`. In the response headers, **X-Campus** should be `campus-api`.
2. **GET `/hostels`**. Pune House is id 1. **GET `/hostels/summary`**. Guest House count is 0 and average is `null` before any POST.
3. **POST `/students`** with this body. You should see **201**, `"id": 1`, `"hostel_name": "Pune House"`. Open `campus.log` and find `created:asha@example.com`.

```json
{
  "full_name": "Asha Rao",
  "email": "asha@example.com",
  "city": "Pune",
  "marks": 90,
  "hostel_id": 1
}
```
4. POST Rahul (Pune, 80, hostel 1), Meera (Chennai, 91, hostel 2), Imran (Lucknow, 70, hostel 3), Neha (Delhi, 85, `hostel_id` null). **GET `/students`**. Five rows. Neha’s `hostel_name` is `null`.
5. **GET `/students?city=Pune`**. Asha and Rahul only. **GET `/students/99`**. **404**.
6. **Stop Uvicorn** and start it again. **GET `/students`**. Five rows remain. That is persistence.

![After restart, GET still returns Asha — the row lived in campus.db](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session36/session36-04-restart-still-asha.png?v=20261009)
7. **PUT `/students/4`** with Imran’s full body and `marks` 75. **GET `/hostels/summary`**. Lucknow House average should now use 75.
8. **POST `/upload`** a small text file, then **GET `/download/{name}`**. The file body should match. **GET `/download/missing.txt`** is JSON 404.

Connecting idea: Every click should match the route table at the top. If a row in that table was not exercised, go back to it.

Activity: After step 6, GET `/hostels/summary`. Pune House count 2, average 85.0 (90 and 80). Guest House still 0. That is the same campus arithmetic as the SQL summaries, now behind HTTP.

A summary row looks like this after the five POSTs (Imran still 70 until step 7):

```json
{
  "hostel_name": "Pune House",
  "student_count": 2,
  "average_marks": 85.0
}
```

Asha’s GET body includes `"hostel_name": "Pune House"` even though that string is not a column on `students`. If that key is missing, the property did not run inside an open session.

## If something breaks — check this list

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `No module named 'dotenv'` | pip missed python-dotenv | `pip install python-dotenv` |
| Health `app` is not Campus API | `.env` missing or venv off | File beside `main.py`; activate venv |
| Empty students after POST | No `commit`, or wrong folder | Commit; run Uvicorn from `campus_api` |
| Rows vanish after restart | Still on the notices list app | This `main.py` must import `Student` |
| `hostel_name` missing / error | Property read after session close | Return `StudentOut` inside the route |
| Summary has no Guest House | Inner join instead of outerjoin | Keep `select_from(Hostel).outerjoin` |
| `by-city` 422 on int | Not this app; city is a **query** | Use `/students?city=Pune` |
| No line in `campus.log` | Looked in the JSON 201 | Open the file after the response |
| CORS confusion on `/docs` | Same origin | CORS is for port 5500, not Swagger |
| Upload JSON 404 | `../` in the name, or wrong folder | `basename` only; file in `uploads/` |
| `from_attributes` error | `StudentOut` missing ConfigDict | Keep `from_attributes=True` |
| Unique error on email | Asha posted twice | New email, or DELETE first |
| Health 200 but no X-Campus | Middleware not registered | Confirm `@app.middleware("http")` is in `main.py` |

## Key Takeaways

- This session **assembles** the backend you already learnt: FastAPI, Pydantic, Depends, middleware, CORS, background tasks, files, SQL ideas, and ORM persistence.
- **`Depends(get_db)`** plus **`commit`** is what makes CRUD survive a Uvicorn restart. A Python list never did.
- **Query `city`**, **`hostel_name`**, and **`/hostels/summary`** reuse WHERE, JOIN, and COUNT/AVG on the same campus sample.
- Middleware stamps every reply. CORS, the background log, and upload/download sit on this app without replacing the student table.
- Upcoming work uses an AI assistant on **this same `campus_api`**. Do not start a blank project. The running app is the source of truth.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
| --- | --- |
| `campus_api` | Assembled mini backend |
| `.env` / `APP_NAME` / `CORS_ORIGIN` | Local settings |
| `get_settings` / `get_db` | Depends: config and session |
| `CORSMiddleware` | Guest list for port 5500 |
| HTTP middleware | X-Campus and timing headers |
| `BackgroundTasks` / `campus.log` | Work after POST JSON |
| `UploadFile` / `FileResponse` | `/upload` and `/download` |
| `StudentCreate` / `StudentOut` | Pydantic in and out |
| `hostel_name` property | JOIN as an attribute |
| `?city=` | Query filter |
| `/hostels/summary` | COUNT and AVG per hostel |
| `func.count` / `func.avg` / `outerjoin` | ORM form of the SQL summaries |
| `db.add` / `commit` / `refresh` | Persistent insert |
| Persistence | GET works after restart |
| `/docs` or Postman | Walk the full app |
| `X-Campus` | Middleware stamp on every response |
| `campus.log` | Background line after POST |
| `func.count(Student.id)` | 0 on Guest House with outer join |
| `python-dotenv` | Loads `.env` for APP_NAME and CORS |
| `check_same_thread=False` | Lets FastAPI use SQLite |
