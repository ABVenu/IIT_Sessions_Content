# SQLAlchemy ORM Fundamentals

A parent still asks, “How did Pune House do?” In the previous session you answered with **AVG** and **GROUP BY**: one number per hostel, not five mark sheets.

You also used **COUNT**, **SUM**, **MIN**, **MAX**, and **HAVING**. Those sentences ran in the Supabase project `campus-sql`, in the **SQL Editor**. The stored student rows did not change; only the answer was short.

A FastAPI function cannot press **Run** in that editor. It is Python. Restart the older notices API and the Python list is empty again, even though `campus-sql` still holds Asha, Rahul, Meera, Imran, and Neha.

The backend needs a Python way to create, read, change, and remove those same kinds of rows. That Python way is an **ORM**.

Today you map the campus tables to SQLAlchemy models, run **CRUD** through a session, and walk the hostel-to-student link as an attribute. Connecting those calls to HTTP routes is upcoming work. This session stays in Python.

Work in a new folder `campus_orm` with a virtual environment activated, the same habit you used for FastAPI.

```bash
mkdir campus_orm  # New folder for today's Python files
cd campus_orm  # Enter that folder
python3 -m venv .venv  # Isolated packages, same habit as FastAPI setup
source .venv/bin/activate  # Turn the virtual environment on
pip install sqlalchemy  # Install the ORM library
```

## What you will learn in this session

- What an **ORM** is, and why FastAPI work uses one instead of raw SQL strings
- How a **SQLAlchemy model** maps a Python class to a database table
- How to **INSERT**, **SELECT**, **UPDATE**, and **DELETE** through a **session**
- How a **one-to-many** foreign key becomes `hostel.students` and `student.hostel`

## Why an ORM is used with FastAPI

- **ORM (Object-Relational Mapper)**
  - *Official Definition:* A library that maps Python classes and objects to relational tables and rows, and translates object operations into SQL.
  - *In Simple Words:* A translator. You speak Python. The database still speaks SQL. The ORM writes the SQL for you.
  - *Real-Life Example:* You fill a college admission form in English. The office clerk copies it into the official register in the office’s format. You did not rewrite the register by hand.
- **SQLAlchemy**
  - *Official Definition:* A Python SQL toolkit and ORM used to define models, open a database connection, and run queries.
  - *In Simple Words:* The ORM library you install with `pip` for this course.
  - *Real-Life Example:* The clerk’s rulebook. It knows how to turn “add Asha” into an **INSERT**, and “find Asha” into a **SELECT**.

Need: FastAPI handlers already work with Python objects, such as the Pydantic models you used for request bodies. A database row is not a Pydantic model. Someone has to convert between Python and SQL.

Logic: If every route writes its own `INSERT INTO ...` string, one spelling mistake in a column name fails at run time, and a join is copied in many files. An ORM keeps the table shape in one class, and the route (later) asks for `Student` objects.

Common doubt: “Did we already learn CRUD?” Yes, in two other places. SQL CRUD was typed in the SQL Editor. FastAPI CRUD stored notices in a list.

Neither of those is ORM CRUD. Today the third version writes to a database file from Python.

Common error: Putting SQL strings inside a FastAPI route and calling that “the backend database layer.” That still works for a tiny script. It does not give you `hostel.students` as a Python list, and it repeats table names everywhere.

| Approach | What you write | What the database receives | Stays after restart? |
| --- | --- | --- | --- |
| Python list in a FastAPI route | `notices.append(...)` | Nothing. There is no table | No |
| Raw SQL in the SQL Editor | `INSERT INTO students ...` | That exact SQL | Yes |
| Raw SQL inside Python | A string such as `"SELECT * FROM students"` | That string, if you send it | Yes |
| SQLAlchemy ORM | `session.add(asha)` then `session.commit()` | SQLAlchemy’s **INSERT** | Yes |

Connecting idea: The ORM does not replace the database. PostgreSQL and SQLite still store tables. The ORM is the Python door to those tables.

![Clerk translates an English student form into the official database register — the ORM](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session35/session35-01-orm-translator-clerk.png?v=20261009)

This session uses **SQLite**, not the `campus-sql` SQL Editor. SQLite stores the whole database in one file on your laptop, named `campus.db`. The tables, keys, and foreign keys are the same ideas you used with PostgreSQL in Supabase, and only the engine URL changes if you later point the same models at another database.

## Engine, session, and Base

Three SQLAlchemy names sit under every model and query.

- **Engine**
  - *Official Definition:* The SQLAlchemy object that holds the database URL and creates connections.
  - *In Simple Words:* The address of the cupboard, plus the driver that opens it.
  - *Real-Life Example:* `sqlite:///campus.db` means “the file `campus.db` in this folder.”
- **Session**
  - *Official Definition:* The working unit that tracks objects, sends SQL on **commit**, and rolls work back on failure.
  - *In Simple Words:* The tray of forms you are editing before the clerk stamps them into the register.
  - *Real-Life Example:* `session.add(asha)` places Asha on the tray. `session.commit()` writes her into `campus.db`. Close without commit, and the tray is discarded.
- **Base**
  - *Official Definition:* The declarative base class that SQLAlchemy models inherit from so they can be mapped to tables.
  - *In Simple Words:* The common parent of every model class in this project.
  - *Real-Life Example:* Every campus form is printed on the same office pad. `Base` is that pad.

`DeclarativeBase` is the modern parent class. `create_engine` builds the engine. `Session(engine)` opens a session bound to that engine.

Save this as `models.py`. Run it once. It only creates empty tables.

```python
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine  # Types, link, and engine
from sqlalchemy.orm import DeclarativeBase, relationship  # Parent class and one-to-many helper

engine = create_engine("sqlite:///campus.db", echo=True)  # File database; echo prints the SQL SQLAlchemy sends


class Base(DeclarativeBase):  # All models in this folder inherit from this class
    pass  # No extra columns on the parent itself


class Hostel(Base):  # One row in the hostels table
    __tablename__ = "hostels"  # Exact table name in campus.db
    id = Column(Integer, primary_key=True)  # Primary key; SQLite fills this on insert
    hostel_name = Column(String, unique=True, nullable=False)  # Building name, required, cannot repeat
    students = relationship("Student", back_populates="hostel")  # Python list of Student objects for this hostel

    def __repr__(self):  # How the object prints in the terminal
        return f"<Hostel id={self.id} name={self.hostel_name}>"  # Short label for checks


class Student(Base):  # One row in the students table
    __tablename__ = "students"  # Exact table name in campus.db
    id = Column(Integer, primary_key=True)  # Primary key; SQLite fills this on insert
    full_name = Column(String, nullable=False)  # Required name
    email = Column(String, unique=True, nullable=False)  # Required, and unique like the SQL UNIQUE rule
    city = Column(String, nullable=False)  # Required city
    marks = Column(Integer, nullable=False)  # Whole number marks
    hostel_id = Column(Integer, ForeignKey("hostels.id"), nullable=True)  # Optional link to hostels.id
    hostel = relationship("Hostel", back_populates="students")  # The one Hostel object, or None

    def __repr__(self):  # How the object prints in the terminal
        return f"<Student id={self.id} name={self.full_name}>"  # Short label for checks


Base.metadata.create_all(engine)  # CREATE TABLE for every model that does not already exist
```

How the code works:

- `echo=True` prints the generated SQL in the terminal. That is how you confirm the ORM still talks SQL. Set it to `False` when the noise is not useful.
- `__tablename__` is the table name. It should match the name you would have used in `CREATE TABLE`.
- `Column(Integer, primary_key=True)` is the same idea as a primary key `id` in SQL. SQLite numbers the row when you omit `id`.
- `nullable=False` is `NOT NULL`. `unique=True` is `UNIQUE`. `ForeignKey("hostels.id")` is the same link as `hostel_id INTEGER REFERENCES hostels(id)`.
- `relationship` does not add a third column. It teaches SQLAlchemy to load the other side of the foreign key as a Python attribute.
- `create_all` issues `CREATE TABLE` only when the table is missing. It does not rebuild sample rows. Delete `campus.db` if you need a clean file.

Pydantic `BaseModel` and SQLAlchemy `Base` are different parents. A Pydantic class validates a JSON body. A SQLAlchemy class maps a table.

Do not inherit a table model from `BaseModel`. You already use Pydantic on FastAPI request bodies. That job stays on the HTTP side.

| Kind of class | Parent | Job | Example field |
| --- | --- | --- | --- |
| Pydantic schema | `BaseModel` | Check JSON keys and types | `email: str` on a request body |
| SQLAlchemy model | `Base` | Map a table row | `email = Column(String, unique=True)` |

Connecting idea: The classes are the blank forms. The next step is to fill forms and commit them.

![Student class fields map to columns on the students table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session35/session35-02-class-maps-to-table.png?v=20261009)

## Define the models, then confirm the file

After `python3 models.py`, the folder contains `campus.db`. The terminal shows `CREATE TABLE` for `hostels` and `students`.

Save as `list_tables.py` if you want to see the empty tables in SQL, from the same folder:

```python
from sqlalchemy import text  # Lets you send one raw SQL sentence through the engine
from models import engine  # Reuse the same campus.db connection

with engine.connect() as connection:  # Open one connection
    hostels = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))  # List tables
    print(hostels.fetchall())  # Expect hostels and students
```

How the code works:

- This check is not ORM CRUD. It only proves the file and tables exist.
- `sqlite_master` is SQLite’s own catalogue. You do not create it.
- Everyday work uses models, not `text("SELECT ...")`. Raw SQL is a torch, not the default tool.

Activity: In `campus_orm`, run `python3 models.py`. Confirm `campus.db` appears, then run `python3 list_tables.py`. You should see `hostels` and `students` in the printed list.

## INSERT — create rows with the ORM

- **INSERT with the ORM**
  - *Official Definition:* Creating model instances, registering them with `session.add` or `session.add_all`, then calling `session.commit()` so SQLAlchemy emits **INSERT**.
  - *In Simple Words:* Make Python objects, put them on the session tray, then stamp the tray.
  - *Real-Life Example:* You fill four hostel forms and five student forms, then hand the stack to the clerk at once.

Hostels must exist before a student can point at `hostel_id`, the same order you used in SQL. Neha’s `hostel_id` stays empty.

Save as `insert_rows.py` and run it once.

```python
from sqlalchemy.orm import Session  # Working tray for objects
from models import Hostel, Student, engine  # Tables and the campus.db engine

with Session(engine) as session:  # Open a session; it closes at the end of this block
    pune = Hostel(hostel_name="Pune House")  # Hostel row, id filled on commit
    chennai = Hostel(hostel_name="Chennai House")  # Second building
    lucknow = Hostel(hostel_name="Lucknow House")  # Third building
    guest = Hostel(hostel_name="Guest House")  # Building with no students later
    session.add_all([pune, chennai, lucknow, guest])  # Place hostels on the tray
    session.flush()  # Send INSERT now so hostel ids exist, without finishing the transaction
    asha = Student(  # Student row linked to Pune House
        full_name="Asha Rao",  # Name
        email="asha@example.com",  # Unique email
        city="Pune",  # City
        marks=90,  # Marks used in later reads
        hostel_id=pune.id,  # Foreign key after flush
    )  # End of Asha
    rahul = Student(  # Second student in Pune House
        full_name="Rahul Mehta",  # Name
        email="rahul@example.com",  # Unique email
        city="Jaipur",  # City
        marks=80,  # Marks
        hostel_id=pune.id,  # Same hostel id as Asha
    )  # End of Rahul
    meera = Student(  # Chennai House
        full_name="Meera Iyer",  # Name
        email="meera@example.com",  # Unique email
        city="Chennai",  # City
        marks=91,  # Marks
        hostel_id=chennai.id,  # Foreign key
    )  # End of Meera
    imran = Student(  # Lucknow House
        full_name="Imran Khan",  # Name
        email="imran@example.com",  # Unique email
        city="Lucknow",  # City
        marks=70,  # Marks
        hostel_id=lucknow.id,  # Foreign key
    )  # End of Imran
    neha = Student(  # No hostel
        full_name="Neha Shah",  # Name
        email="neha@example.com",  # Unique email
        city="Delhi",  # City
        marks=85,  # Marks
        hostel_id=None,  # Empty foreign key
    )  # End of Neha
    session.add_all([asha, rahul, meera, imran, neha])  # Place students on the tray
    session.commit()  # Write every new row into campus.db
    print(pune.id, asha.id, neha.hostel_id)  # Expect 1, 1, None on a fresh file
```

How the code works:

- `with Session(engine) as session` opens and later closes the session. Closing without `commit` drops uncommitted work.
- `flush()` sends SQL early so `pune.id` is no longer `None`. `commit()` then finishes the transaction.
- You may assign `hostel=pune` instead of `hostel_id=pune.id`. The relationship fills the foreign key. Both styles are valid. Pick one in a file and keep it.
- The marks are 90, 80, 91, 70, and 85. That is the same five-student sample whose class total was 416 and average 83.2 in the previous summaries.
- Running this script twice on the same file raises a unique error on `hostel_name` or `email`. Delete `campus.db`, run `models.py`, then run `insert_rows.py` again.

Common error: Calling `add` and then reading the database in another program without `commit`. The other program still sees empty tables.

![Session tray of student cards, commit stamp, then the campus.db file](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session35/session35-03-session-tray-commit.png?v=20261009)

Activity: Run `insert_rows.py` on a fresh `campus.db`. The last print should show a hostel id, Asha’s id, and `None` for Neha.

## SELECT — read rows with the ORM

- **SELECT with the ORM**
  - *Official Definition:* Building a `select()` statement against a model class, executing it on the session, and receiving model objects or column values.
  - *In Simple Words:* Ask the session for `Student` objects, not for a handwritten SQL grid.
  - *Real-Life Example:* “Give me every student form,” or “give me the form whose email is asha@example.com.”

`select(Student)` is “all columns of that table,” as objects. `.where(...)` is the **WHERE** you already know. `session.scalars(...)` returns the objects themselves.

Save as `read_rows.py`.

```python
from sqlalchemy import select  # The SELECT builder
from sqlalchemy.orm import Session  # Working tray
from models import Hostel, Student, engine  # Models and engine

with Session(engine) as session:  # Read-only work still uses a session
    all_students = session.scalars(select(Student).order_by(Student.id)).all()  # Every student, by id
    for student in all_students:  # Walk the list of objects
        print(student.id, student.full_name, student.marks, student.hostel_id)  # Fields are attributes
    asha = session.scalars(  # One row, or None
        select(Student).where(Student.email == "asha@example.com")  # WHERE email = ...
    ).first()  # First match, not a list
    print(asha.full_name, asha.city)  # Asha Rao, Pune
    high_marks = session.scalars(  # Filtered list
        select(Student).where(Student.marks >= 85).order_by(Student.marks.desc())  # WHERE and ORDER BY
    ).all()  # All matches
    for student in high_marks:  # Meera 91, Asha 90, Neha 85
        print(student.full_name, student.marks)  # Name and marks
    pune = session.scalars(select(Hostel).where(Hostel.hostel_name == "Pune House")).one()  # Exactly one hostel
    print(pune.id, pune.hostel_name)  # 1, Pune House
```

How the code works:

- `session.scalars(select(Student))` yields `Student` instances. You read `student.full_name`, not `row[1]`.
- `.all()` returns a list. `.first()` returns one object or `None`. `.one()` returns one object and raises an error if the count is not exactly one.
- `Student.marks >= 85` is a condition on the class, not a string of SQL. SQLAlchemy turns it into SQL, which `echo=True` will show.
- `order_by(Student.marks.desc())` is `ORDER BY marks DESC`. Highest marks print first: 91, 90, 85.

| SQL you already wrote | SQLAlchemy read |
| --- | --- |
| `SELECT * FROM students` | `select(Student)` |
| `WHERE email = 'asha@example.com'` | `Student.email == "asha@example.com"` |
| `WHERE marks >= 85` | `Student.marks >= 85` |
| `ORDER BY marks DESC` | `order_by(Student.marks.desc())` |
| First matching row | `.first()` (object or `None`) |

Common doubt: “Is `select(Student)` the same as `SELECT *`?” It selects the mapped columns of that class, then builds objects. You do not unpack tuples unless you select individual columns on purpose.

Activity: Run `read_rows.py`. Confirm five students print, Asha’s city is Pune, and the high-marks list is Meera, Asha, Neha.

## UPDATE — change a stored object

- **UPDATE with the ORM**
  - *Official Definition:* Loading an object, assigning new attribute values, then committing so SQLAlchemy emits **UPDATE**.
  - *In Simple Words:* Find the form, correct one box, stamp the tray.
  - *Real-Life Example:* Imran’s marks were 70. The office corrects them to 75. The same `id` stays.

You do not write `UPDATE students SET marks = 75`. You change `imran.marks` and commit.

Save as `update_row.py`.

```python
from sqlalchemy import select  # Lookup by email
from sqlalchemy.orm import Session  # Working tray
from models import Student, engine  # Student table and engine

with Session(engine) as session:  # One transaction
    imran = session.scalars(  # Load the stored object
        select(Student).where(Student.email == "imran@example.com")  # Unique email
    ).one()  # Must exist after insert_rows.py
    print("before", imran.marks)  # 70 on the sample
    imran.marks = 75  # Change the attribute; SQLAlchemy marks the object as dirty
    session.commit()  # Emit UPDATE and save
    print("after", imran.marks)  # 75
```

How the code works:

- After commit, a new session should also see 75. The change is in `campus.db`, not only in memory.
- Changing `imran.marks` without `commit` is only a tray edit. Closing the `with` block discards it.
- If a commit fails, SQLAlchemy rolls the transaction back. The stored marks stay at the old value until a later commit succeeds.
- The primary key does not change. You still find Imran by email or by `id`.

Common error: Updating with a copied number in your head, such as `Student(id=4, marks=75)`, and adding it as a new row. That tries a second insert. Load first, then assign.

Activity: Run `update_row.py`. Then run a short read of Imran’s marks. You should see 75. If you need the original sample again, delete `campus.db`, run `models.py`, then `insert_rows.py`.

## DELETE — remove a stored object

- **DELETE with the ORM**
  - *Official Definition:* Loading an object, calling `session.delete(obj)`, then committing so SQLAlchemy emits **DELETE**.
  - *In Simple Words:* Take one form off the register, not the whole register.
  - *Real-Life Example:* Guest House is unused in a drill. You remove that hostel row if no student points at it.

`session.delete` needs the object. It is not enough to know the name as a string.

Save as `delete_row.py`. Use it only after you understand that the row is gone from `campus.db`.

```python
from sqlalchemy import select  # Lookup by name
from sqlalchemy.orm import Session  # Working tray
from models import Hostel, engine  # Hostel table and engine

with Session(engine) as session:  # One transaction
    guest = session.scalars(  # Load Guest House
        select(Hostel).where(Hostel.hostel_name == "Guest House")  # Unique name
    ).one()  # Must exist after insert_rows.py
    session.delete(guest)  # Mark the row for deletion
    session.commit()  # Emit DELETE
    gone = session.scalars(select(Hostel).where(Hostel.hostel_name == "Guest House")).first()  # Look again
    print(gone)  # None
```

How the code works:

- After commit, `Guest House` is not in the table. The other hostels remain.
- If a student still had `hostel_id` pointing at Guest House, SQLite may reject the delete, or leave a broken link, depending on foreign-key enforcement. In this sample, no student uses Guest House, so the delete is safe.
- `Base.metadata.create_all` does not restore the deleted row. Only a fresh insert does.

Common error: Deleting a hostel that students still reference, then wondering why a later `student.hostel` is empty. Remove or reassign children first, the same caution you used with SQL **DELETE**.

Activity: Run `delete_row.py` once. Print all hostel names after that. You should see three names, not four. Rebuild `campus.db` before the relationship practice below so Guest House exists again.

## One-to-many relationships in the ORM

You already stored one-to-many in SQL: one hostel id on many student rows. A **JOIN** then printed the building name beside the student name.

The ORM still stores that foreign key. `relationship` adds a Python shortcut so you can write `pune.students` and `asha.hostel` instead of a join sentence every time.

![Pune House lists Asha and Rahul; Neha has no hostel; Guest House has zero students](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session35/session35-04-one-to-many-hostel.png?v=20261009)

- **One-to-many relationship (ORM)**
  - *Official Definition:* A mapping where one parent row links to many child rows through a foreign key, exposed as a collection attribute on the parent and a scalar attribute on the child.
  - *In Simple Words:* One hostel object holds a list of student objects. Each student object holds one hostel object, or none.
  - *Real-Life Example:* Pune House’s register lists Asha and Rahul. Asha’s form lists Pune House. Neha’s form lists no hostel.
- **`back_populates`**
  - *Official Definition:* A `relationship` argument that names the attribute on the other class, so both sides stay in sync in Python.
  - *In Simple Words:* The two arrows are a pair: `students` on `Hostel`, `hostel` on `Student`.
  - *Real-Life Example:* The hostel register points at the residents. Each resident form points back at the building.

Rebuild a clean file, then save `read_relationships.py`.

```python
from sqlalchemy import select  # Lookups
from sqlalchemy.orm import Session  # Working tray
from models import Hostel, Student, engine  # Both models

with Session(engine) as session:  # One session so related objects load together
    pune = session.scalars(select(Hostel).where(Hostel.hostel_name == "Pune House")).one()  # Parent
    print(pune.hostel_name)  # Pune House
    for student in pune.students:  # Collection: Asha and Rahul
        print(student.full_name, student.marks)  # Names from the child table
    asha = session.scalars(select(Student).where(Student.email == "asha@example.com")).one()  # Child
    print(asha.hostel.hostel_name)  # Pune House, from the parent object
    neha = session.scalars(select(Student).where(Student.email == "neha@example.com")).one()  # No hostel
    print(neha.hostel)  # None, because hostel_id is empty
    guest = session.scalars(select(Hostel).where(Hostel.hostel_name == "Guest House")).one()  # Empty parent
    print(len(guest.students))  # 0
```

How the code works:

- `pune.students` runs the child lookup for you. You did not write `JOIN` in this file. SQLAlchemy does.
- `asha.hostel` is one `Hostel` object. `asha.hostel.hostel_name` is the building name.
- `neha.hostel` is `None`. That is the ORM form of a `LEFT JOIN` that finds no building.
- `guest.students` is an empty list, not `None`. The hostel exists. It has no children.
- Access related objects while the session is still open. After the `with` block, lazy loading may fail because the connection is closed.

You can also create the link from the parent side when inserting:

```python
from sqlalchemy.orm import Session  # Working tray
from models import Hostel, Student, engine  # Both models

with Session(engine) as session:  # Demo only: run on a throwaway copy of campus.db
    demo_hostel = Hostel(hostel_name="Demo House")  # New parent
    demo_student = Student(  # New child with no hostel_id typed by hand
        full_name="Kiran Shah",  # Name
        email="kiran@example.com",  # Unique email
        city="Pune",  # City
        marks=88,  # Marks
    )  # hostel_id still empty
    demo_hostel.students.append(demo_student)  # Relationship fills hostel_id on commit
    session.add(demo_hostel)  # Adding the parent can cascade the new child
    session.commit()  # INSERT hostel and student
    print(demo_student.hostel_id, demo_student.hostel.hostel_name)  # New id, Demo House
```

How the code works:

- `append` on `students` sets the foreign key. You do not have to assign `hostel_id` yourself.
- Skip this demo if you want the five-student sample untouched. Unique email `kiran@example.com` will fail on a second run.

Common error: Forgetting `back_populates` on one side. SQLAlchemy then cannot keep `pune.students` and `asha.hostel` as a pair.

Common doubt: “Do I still need `hostel_id` if I have `hostel`?” Yes. `hostel_id` is the column in the table. `hostel` is the object shortcut. The column is what the database stores.

Activity: Rebuild `campus.db` with `models.py` and `insert_rows.py`. Run `read_relationships.py`. Pune House should list two names, Asha should show Pune House, Neha should show `None`, and Guest House should show length 0.

Connecting idea: CRUD and this relationship stay inside Python. Upcoming work places the same session calls behind FastAPI routes so a client can persist data over HTTP.

## If something breaks — check this list

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `No module named 'sqlalchemy'` | venv is off, or `pip install` was skipped | Activate `.venv`, then `pip install sqlalchemy` |
| `campus.db` is missing | `models.py` was not run in this folder | `cd campus_orm`, run `python3 models.py` |
| `no such table: students` | Queries ran before `create_all` | Run `models.py` first |
| Unique error on email or hostel name | `insert_rows.py` ran twice on the same file | Delete `campus.db`, recreate tables, insert once |
| `asha` is `None` | Insert never committed, or a different folder’s db | Commit, and check you are in `campus_orm` |
| `imran.marks` still 70 after an update file | Forgot `session.commit()` | Assign, then commit, then read in a new session |
| `Guest House` still prints after delete | Delete script was not run, or you rebuilt the file | Run `delete_row.py`, or accept that a rebuild restored it |
| `NoneType` has no `hostel_name` | You used `neha.hostel.hostel_name` | Check `neha.hostel is None` first |
| Related list is empty when it should not be | Session closed, or you queried a different hostel | Read `pune.students` inside the same `with Session` block |
| Pydantic error on a model file | Table class inherited from `BaseModel` | Inherit from SQLAlchemy `Base` only |
| SQL in the terminal looks unfamiliar | `echo=True` is on | That print is the ORM’s SQL. It is expected |

## Key Takeaways

- An **ORM** maps Python classes to tables so FastAPI-facing code can work with objects while the database still stores rows. **SQLAlchemy** is that mapper in this course.
- A model names `__tablename__`, **columns**, and constraints. `create_all` creates missing tables. This is not a Pydantic schema.
- **CRUD** in the ORM is `add`/`commit` (insert), `select` (read), attribute change/`commit` (update), and `delete`/`commit` (delete). A session that never commits does not change `campus.db`.
- A **one-to-many** foreign key stays on the child as `hostel_id`. `relationship` exposes `hostel.students` and `student.hostel`, including empty lists and `None`.
- These scripts are the persistence layer. Upcoming work connects the same models to FastAPI routes so HTTP clients can store and read rows.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
| --- | --- |
| ORM | Maps objects to tables and writes SQL for you |
| SQLAlchemy | The Python ORM library installed with `pip` |
| SQLite / `campus.db` | Local file database used for today’s practice |
| Engine | Connection factory built by `create_engine` |
| `echo=True` | Prints the SQL SQLAlchemy sends |
| Session | Tracks objects; `commit()` saves; close discards uncommitted work |
| `Base` / `DeclarativeBase` | Parent of table model classes |
| Model | Python class mapped to one table, such as `Student` |
| `__tablename__` | Table name in the database file |
| `Column` | Mapped field: type, `primary_key`, `nullable`, `unique` |
| `ForeignKey("hostels.id")` | Child column that points at a parent id |
| `relationship` / `back_populates` | Python link between parent collection and child object |
| `create_all` | `CREATE TABLE` for missing models |
| `session.add` / `session.add_all` | Register new objects for **INSERT** |
| `session.flush` | Send SQL before the final commit so ids exist |
| `session.commit` | Write the transaction to `campus.db` |
| `session.delete` | Register an object for **DELETE** |
| `select(Student)` | ORM **SELECT** of that model |
| `session.scalars(...).all()` | List of model objects |
| `.first()` / `.one()` | One object or `None`; or exactly one object |
| `.where(...)` | Filter, the ORM form of **WHERE** |
| Pydantic `BaseModel` | Request/response schema; not a table model |
| `pune.students` | One-to-many collection |
| `asha.hostel` | Many-to-one parent object |
| `neha.hostel` | `None` when `hostel_id` is empty |
