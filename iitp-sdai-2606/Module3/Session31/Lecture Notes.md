# Database Fundamentals & SQL (Part I)

You book a train ticket tonight. Tomorrow morning the same PNR is still on the screen.

The phone did not memorise that ticket. A program on a server stored the booking in an organised store, then read it back when you asked again.

In the previous session you decided which web pages may call your API, accepted an uploaded file, and let a small task run after the response was sent. Those tools move messages and files. They do not give you a grid of records that stays organised after the program stops.

This session adds that store. You will see why a backend uses a **relational database**, how to **design one table**, how to **add rows**, and how to **read those rows** back.

## What you will learn in this session

- Why a **relational database** belongs in the backend, beside the API you already run
- How a **table**, a **row**, a **column**, a **primary key**, and **constraints** fit together
- How to write **CREATE TABLE** so the database itself enforces the rules
- How to write **INSERT** to add records, and **SELECT** to retrieve them

You will work in **SQLite**, a small relational database that stores everything in one file on your computer. The same table ideas appear in larger products such as PostgreSQL and MySQL.

## Why the backend uses a relational database

Your earlier APIs kept notices in a Python list. Stop the program and that list is gone. An uploaded file keeps the bytes, but it has no columns and no uniqueness rule.

A spreadsheet on a laptop has columns. The API still cannot open that laptop when a student checks a result at midnight.

- **Database**
  - *Official Definition:* An organised store of data that programs can read and write.
  - *In Simple Words:* A structured notebook the backend keeps, instead of loose papers or a list that vanishes.
  - *Real-Life Example:* The attendance register in a college office. The pages stay in the cupboard after the clerk goes home.
- **Relational database**
  - *Official Definition:* A database that stores data in relations — tables of rows and columns — and answers questions written in a query language.
  - *In Simple Words:* The notebook is a set of grids. One grid holds one kind of fact. You ask for rows using fixed commands.
  - *Real-Life Example:* One grid lists students. Each line is one student. The columns are name, email, city, and marks. The word “relational” points at that grid (a relation). Connecting several grids comes in an upcoming session.
- **RDBMS (Relational Database Management System)**
  - *Official Definition:* The software that stores relational tables and runs the commands you send.
  - *In Simple Words:* The clerk who owns the cupboard, checks the rules, and fetches the page you asked for.
  - *Real-Life Example:* **SQLite** is the RDBMS you will use today. Large public sites often use PostgreSQL or MySQL. Your SQL sentences stay in the same family.
- **SQL (Structured Query Language)**
  - *Official Definition:* The standard language for defining tables and reading or writing their rows in a relational database.
  - *In Simple Words:* Short, formal sentences the database understands: make this grid, add this line, show these columns.
  - *Real-Life Example:* A bank withdrawal slip. The printed headings stay fixed. You fill the boxes. You do not rewrite the printed form as a free-form essay.

| Place the data lives | Still there after restart? | Can the API use it? | Can the store enforce “this email must be unique”? |
| --- | --- | --- | --- |
| Python list in memory | No | Only while that one process is running | Only if your Python code remembers every check |
| Uploaded file or plain text file | Yes | Yes, but you invent the reading rules yourself | No built-in columns or uniqueness |
| Relational database | Yes | Yes. The API sends SQL and gets rows back | Yes. You declare the rules on the table |

Need: A backend that shows the same students tomorrow must keep rows **outside** the request that created them.

Logic: The API stays the door. The database is the cupboard behind the door. A request arrives, SQL runs, rows come back, and the API can turn those rows into a reply.

Common doubt: “Is the database the same thing as the API?” The API listens for HTTP. SQLite stores tables.

They work as a pair. Today you practise the SQL the API would send.

Common error: Treating a JSON example on the screen as saved data. JSON in a response is a message. The database is the saved grid.

Connecting idea: Once the data lives in a grid, the next step is to name the parts of that grid.

## How a table is organised

Picture one admission form that the office reprints for every student. The blank form is the design. Each filled form is one student.

- **Table**
  - *Official Definition:* A named collection of data arranged in columns and rows inside a relational database.
  - *In Simple Words:* One grid for one kind of thing.
  - *Real-Life Example:* A sheet titled `students`. It is the student list, not the whole college.
- **Column**
  - *Official Definition:* A named field that stores one kind of value for every row in the table.
  - *In Simple Words:* One labelled box on the form, repeated down the page.
  - *Real-Life Example:* The box `email` holds an email on every line.
- **Row** (also called a **record**)
  - *Official Definition:* One complete entry in a table, with a single value for each column.
  - *In Simple Words:* One filled form. One student.
  - *Real-Life Example:* The line for Asha Rao is one row. Rahul Mehta is a different row.
- **Schema**
  - *Official Definition:* The structure of the database: which tables exist, which columns they have, and which rules apply.
  - *In Simple Words:* The blank form and its rules, before anyone has written a name.
  - *Real-Life Example:* The office prints boxes and instructions such as “email cannot be left blank.” The ink a clerk adds later is the data.
- **NULL**
  - *Official Definition:* A marker meaning “no value is stored.” It is different from zero and from an empty word.
  - *In Simple Words:* The box was left untouched.
  - *Real-Life Example:* A city box with nothing written is NULL. The number 0 would mean “zero marks.” A typed empty word `''` is still a value.
- **Data type**
  - *Official Definition:* The kind of value a column is allowed to store, such as a whole number or text.
  - *In Simple Words:* The instruction on the box: numbers only, or words only.
  - *Real-Life Example:* Marks are a whole number. A name is text.

| SQL type in this session | What you store | Everyday example |
| --- | --- | --- |
| `INTEGER` | Whole numbers | Marks `88`, copies of a book `3` |
| `TEXT` | Words and sentences | Name `Asha Rao`, email, city |
| `REAL` | Numbers that can include a fraction | Price `249.50` |

SQLite can be loose about types unless you ask it to be strict. You will add **STRICT** so a word cannot be stored in a marks column.

Text uses single quotes. Numbers do not. Values must follow the column order you list, or a city can land in the marks box.

Connecting idea: A grid can still accept two students with the same email, or marks of 500. Those guards are **constraints**, and the identity of each row is the **primary key**.

## Primary keys and constraints

- **Primary key**
  - *Official Definition:* A column, or a set of columns, whose value is unique for every row and identifies that row.
  - *In Simple Words:* The roll number on the form. Two students never share it.
  - *Real-Life Example:* `id` 1 means Asha’s row in this practice table, even if another student is also named Asha.
- **Constraint**
  - *Official Definition:* A rule declared on a table or column that the database refuses to break.
  - *In Simple Words:* A printed instruction the clerk will not ignore.
  - *Real-Life Example:* “This box cannot be empty,” or “this email cannot appear twice.”

| Constraint | Meaning on a column | A save the database refuses |
| --- | --- | --- |
| `PRIMARY KEY` | Unique identity for the row. Here that column is `id` | A second row that tries to reuse `id` 1 |
| `NOT NULL` | A value must be present | An insert that leaves out `full_name` |
| `UNIQUE` | The same value cannot appear on two rows | A second student with Asha’s email |
| `DEFAULT` | The value used when that column is left out of the insert | City stored as `Not given` |
| `CHECK` | A condition the new value must pass | Marks `120` when the rule allows only 0 to 100 |

When the column is `INTEGER PRIMARY KEY` and you leave `id` out of the insert, SQLite fills the next number. Email stays `UNIQUE`, so it cannot repeat, while `id` remains the stable identity of the row. Leave `id` out of `INSERT` so you do not collide with a number already stored.

`CHECK` runs when a row is saved. Reading only the rows that match a condition comes in the next session.

Connecting idea: You have the design words. Next you open SQLite and turn that design into a real file.

## SQLite, the file, and the SQL prompt

- **SQLite**
  - *Official Definition:* A relational database engine that keeps one database in a single file and runs from a terminal command or from inside a program.
  - *In Simple Words:* There is no separate database server to install for today’s practice. One file, `campus.db`, is the whole database.
  - *Real-Life Example:* A register that is one notebook in a drawer. You still write formal sentences in it.
- **Statement**
  - *Official Definition:* One complete SQL instruction, ended with a semicolon.
  - *In Simple Words:* One full sentence to the database.
  - *Real-Life Example:* “Create the students grid” is one statement. “Add Asha” is the next statement.
- **Keyword**
  - *Official Definition:* A word SQL reserves for its grammar, such as `CREATE`, `TABLE`, `SELECT`, or `INSERT`.
  - *In Simple Words:* A printed word on the form. Names you invent, such as `students` or `email`, are your own.
  - *Real-Life Example:* These notes write keywords in CAPITALS so your eye can find them. SQL also accepts `select` in lowercase.

The database file appears in the folder where you run the command. Stay in one project folder so you do not create two different `campus.db` files by accident.

Open a terminal in that folder and start the SQLite prompt:

```bash
sqlite3 campus.db   # Open campus.db, or create that file if it is not there yet
```

You are now inside SQLite. **Dot commands** talk to the SQLite program. They are not SQL, and they do not end with a semicolon.

Opening the file only creates a place to work. An empty `.tables` reply is normal before `CREATE TABLE`.

| Dot command | What you get |
| --- | --- |
| `.headers on` | Column names above the results |
| `.mode column` | Results aligned as a grid |
| `.tables` | Names of tables in this file |
| `.schema students` | The `CREATE` statement of `students` |
| `.quit` | Back to the terminal |

Common error: A semicolon after `.quit`, or a missing semicolon after SQL. Dot commands reject the semicolon. SQL statements need it.

The `sqlite3` command and the `campus.db` file both stay on your machine.

Connecting idea: Next you design the columns, then run a script that builds `students`, adds four rows, and reads them.

## Design of the students table

Decide the schema before you type. One row means one student. This session uses a single table.

| Column | Type | Rules | Why this rule |
| --- | --- | --- | --- |
| `id` | `INTEGER` | `PRIMARY KEY` | Identifies the row. SQLite fills it when you omit it |
| `full_name` | `TEXT` | `NOT NULL` | A student row without a name cannot be used |
| `email` | `TEXT` | `NOT NULL` and `UNIQUE` | Required, and two rows cannot share it |
| `city` | `TEXT` | `DEFAULT 'Not given'` | If you omit city, this text is stored |
| `marks` | `INTEGER` | `NOT NULL` and `CHECK` from 0 to 100 | Required, and out-of-range marks are rejected |

Use letters, numbers, and underscores in names. `full_name` stays one word to SQL. A space in a name forces extra quoting and is a common slip.

### Student activity: design a books table on paper

Write this on paper before you read the sample script later in these notes. One row means one book.

Include `id` as the primary key, required text for title and author, and a price that cannot be negative. If copies are omitted, store `0`. Beside each name, write the type and the rule.

## Create the table and add the first rows

Save the following as `campus.sql` in the same folder where you run `sqlite3`. The script is complete: it rebuilds `students`, inserts four rows, and reads them back.

```sql
DROP TABLE IF EXISTS students; -- Remove a previous practice table so this script can start clean
CREATE TABLE students ( -- Define a new table named students
    id INTEGER PRIMARY KEY, -- Identity number; SQLite assigns it when INSERT omits id
    full_name TEXT NOT NULL, -- Name is text and must be present
    email TEXT NOT NULL UNIQUE, -- Email is text, required, and cannot repeat
    city TEXT DEFAULT 'Not given', -- If city is omitted, store this text
    marks INTEGER NOT NULL CHECK (marks >= 0 AND marks <= 100) -- Whole number from 0 to 100
) STRICT; -- Reject a value that does not match the declared type
INSERT INTO students (full_name, email, city, marks) -- Fill these columns; id is intentionally absent
VALUES ('Asha Rao', 'asha@example.com', 'Pune', 88); -- First row; text uses single quotes, marks does not
INSERT INTO students (full_name, email, marks) -- City is omitted on purpose so DEFAULT can run
VALUES ('Rahul Mehta', 'rahul@example.com', 76); -- Second row; city becomes Not given
INSERT INTO students (full_name, email, city, marks) -- Same column list for the next two rows
VALUES -- Start a list of rows inside this one statement
    ('Meera Iyer', 'meera@example.com', 'Chennai', 91), -- Third row
    ('Imran Khan', 'imran@example.com', 'Lucknow', 64); -- Fourth row; comma between rows, semicolon at the end
SELECT id, full_name, email, city, marks -- Ask for these columns, in this order
FROM students; -- Read them from students; every saved row comes back
```

From the terminal, in that same folder, run:

```bash
sqlite3 -header -column campus.db < campus.sql   # Print headings in a grid and run campus.sql
```

How the code works:

- `-header -column` changes only the printed layout. It does not change the data.
- `DROP TABLE IF EXISTS students` removes the **whole table**, both design and rows, so practice can start again. `IF EXISTS` means the first run still succeeds when the table is absent.
- `CREATE TABLE students` writes the schema. There is **no comma after the `marks` line**, because it is the last column.
- `STRICT` tells SQLite to honour the types. The word `eighty` in `marks` is rejected.
- Each `INSERT` lists columns, then `VALUES` in that same order. Single quotes wrap text. The number `88` has no quotes.
- Rahul’s insert omits `city`, so `DEFAULT` stores `Not given`. If you explicitly store `NULL`, you get NULL. Omit the column when you want the default.
- The third insert adds two rows in one statement. A comma sits between the two parenthesised groups. The semicolon ends the statement.
- `SELECT` reads columns from `students`. It does not change stored rows. Every row returns, because this query does not narrow the list.

You should see four rows. Ids are 1 to 4. Rahul’s city is `Not given`.

| id | full_name | email | city | marks |
| --- | --- | --- | --- | --- |
| 1 | Asha Rao | asha@example.com | Pune | 88 |
| 2 | Rahul Mehta | rahul@example.com | Not given | 76 |
| 3 | Meera Iyer | meera@example.com | Chennai | 91 |
| 4 | Imran Khan | imran@example.com | Lucknow | 64 |

Re-running the script rebuilds these four rows, because `DROP TABLE` removes that table inside `campus.db` and the inserts run again. Removing one student and keeping the table comes in the next session.

Common error: A comma after the last column, a missing comma, or a missing semicolon. SQLite may say `near ")": syntax error`, or it may wait. Text values use **single** quotes.

Connecting idea: The script shows the path that succeeds. The next statements are ones SQLite should refuse.

## Inserts the database should reject

Run these only after `campus.sql` has succeeded. Each statement is complete. Each one should fail, and the four good rows should remain.

Run **one statement at a time**. A failure stops the rest of a script.

```sql
INSERT INTO students (email, city, marks) -- full_name is required, and it is not in this column list
VALUES ('new@example.com', 'Pune', 70); -- Rejected because full_name is NOT NULL
INSERT INTO students (full_name, email, city, marks) -- Every required column is listed
VALUES ('Asha Rao', 'asha@example.com', 'Pune', 70); -- Email is already on row 1, so UNIQUE fails
INSERT INTO students (full_name, email, city, marks) -- The column list matches the values
VALUES ('Neha Shah', 'neha@example.com', 'Delhi', 120); -- 120 fails CHECK, which allows only 0 to 100
INSERT INTO students (full_name, email, city, marks) -- marks is declared INTEGER
VALUES ('Neha Shah', 'neha@example.com', 'Delhi', 'eighty'); -- STRICT refuses TEXT in an INTEGER column
```

How the code works:

- A refused `INSERT` does not leave a half-written row. The message names the rule, such as `UNIQUE constraint failed: students.email`.
- The same person-name may appear on two rows. The same email may not.
- `CHECK` rejects marks outside 0 to 100. `STRICT` rejects the word `eighty` in an integer column.

### Student activity: insert one valid row of your own

1. Open the file with `sqlite3 campus.db`.
2. If headings are hidden, type `.headers on` and `.mode column`.
3. Insert one new student: your name, a fresh email, a city, and marks from 0 to 100. Omit `id`.
4. Run `SELECT id, full_name, email, city, marks FROM students;` and confirm your row appears with the next `id`.
5. Repeat the insert with that same email and confirm SQLite rejects it.
6. Type `.quit` when you finish.

If you later re-run `campus.sql`, your extra row disappears, because that script drops and rebuilds the table. During practice, that reset is expected.

## SELECT — retrieve what is stored

`INSERT` writes. `SELECT` reads. A read does not remove rows, and it does not change marks.

- **Query**
  - *Official Definition:* A request you send to the database as a SQL statement. In this session that request is a `SELECT`.
  - *In Simple Words:* A formal ask to see part of the stored grid.
  - *Real-Life Example:* Asking the clerk to read out names and marks while the register stays in the cupboard.
- **Result set**
  - *Official Definition:* The rows and columns returned by a query.
  - *In Simple Words:* The answer table. It can show fewer columns than the stored table.
  - *Real-Life Example:* A photocopy of two columns, not the original register.
- **Alias**
  - *Official Definition:* A temporary name for a column in one query, written with `AS`.
  - *In Simple Words:* A heading used only on this answer sheet.
  - *Real-Life Example:* The stored column is `full_name`. Today’s notice prints the heading `student_name`.

`SELECT *` asks for every column. The result follows the order of the table design.

```sql
SELECT * -- Every column, in table order: id, full_name, email, city, marks
FROM students; -- Source table; every saved row is included
```

Name the columns when you need a shorter answer. The left-to-right order you write is the order you receive.

```sql
SELECT full_name, marks, city -- Three columns, in this order
FROM students; -- Every row; fewer columns is different from fewer rows
```

An alias changes the heading of the result only.

```sql
SELECT full_name AS student_name, marks AS score -- Headings for this result alone
FROM students; -- Stored names remain full_name and marks
```

`ORDER BY` arranges the **result**. `ASC` is smallest first. `DESC` is largest first.

If you write neither word, the order is ascending. The stored rows stay in place.

`LIMIT` stops the answer after a fixed number of rows. Put it after `ORDER BY` when the order matters. It shortens the answer, and it leaves every stored row in place.

```sql
SELECT full_name, marks -- Columns for a short list
FROM students -- Every saved student is a candidate
ORDER BY marks DESC -- Largest marks at the top of this answer
LIMIT 2; -- Keep the first two lines of that sorted answer
```

With the four sample rows, that statement returns Meera Iyer with 91, then Asha Rao with 88.

`DISTINCT` shows each different value once in the result. It is an answer-sheet tool. It is separate from a `UNIQUE` rule on the table.

```sql
SELECT DISTINCT city -- Each different city once
FROM students -- Read city from every row
ORDER BY city; -- Sort those city names in ascending order
```

Those four rows produce `Chennai`, `Lucknow`, `Not given`, and `Pune`.

How the code works:

- `FROM students` names the only table in this session. `AS` changes the heading on the answer, and `.schema students` still shows `full_name`.
- `ORDER BY` sorts the answer only. Read `id` again and the numbers are still 1, 2, 3, and 4.
- Zero rows returns an empty result. `no such table: students` means `CREATE` has not run in this file.
- `SELECT full_name marks` with no comma treats `marks` as an alias, so one column comes back. The real column is `full_name`, so `name` raises `no such column`.

Keeping only the rows that match a condition comes in the next session.

### Student activity: read the table in four ways

1. In `sqlite3 campus.db`, show every column of every row.
2. Show only `full_name` and `city`, with headings `student_name` and `home_city`.
3. Show `full_name` and `marks`, smallest marks first, with `ORDER BY marks ASC`.
4. Show each different city once, in ascending order.

## How a backend program runs the same SQL

The terminal is the right place to learn the sentences. A running API does not type into the `sqlite3` prompt. It uses a library, sends the statement, and reads the rows.

- **Parameterised query**
  - *Official Definition:* A SQL statement that contains placeholders, with the real values supplied separately by the program.
  - *In Simple Words:* The sentence stays fixed. Names and numbers travel beside it, in a list.
  - *Real-Life Example:* The withdrawal slip keeps its printed lines. The amount goes in the box. The customer does not rewrite the printed lines.

In Python’s `sqlite3` library the placeholder is `?`. You also call `commit()` so inserts are written into the file.

The interactive tool saved each statement as you entered it. A Python script has to ask for that save.

Save the program below as `read_students.py`. It uses a different file, `practice.db`, so it does not rebuild the `campus.db` from your activities.

```python
import sqlite3  # Use Python's built-in SQLite library
connection = sqlite3.connect("practice.db")  # Open or create practice.db in this folder
cursor = connection.cursor()  # Make a helper that can run SQL statements
cursor.execute("DROP TABLE IF EXISTS students")  # Clear an older practice table in this file
create_students = (  # Hold the CREATE statement in one string
    "CREATE TABLE students ("  # Define the students table
    "id INTEGER PRIMARY KEY, "  # Identity number filled when id is omitted
    "full_name TEXT NOT NULL, "  # Name is required text
    "email TEXT NOT NULL UNIQUE, "  # Email is required and cannot repeat
    "city TEXT DEFAULT 'Not given', "  # Stored when city is omitted
    "marks INTEGER NOT NULL CHECK (marks >= 0 AND marks <= 100) "  # Whole number from 0 to 100
    ") STRICT"  # Enforce the declared types
)  # End of the CREATE string
cursor.execute(create_students)  # Create the table inside practice.db
rows_to_add = [  # Rows to insert; id is left out on purpose
    ("Asha Rao", "asha@example.com", "Pune", 88),  # First student
    ("Rahul Mehta", "rahul@example.com", "Jaipur", 76),  # Second student, with a real city
]  # End of the row list
insert_sql = "INSERT INTO students (full_name, email, city, marks) VALUES (?, ?, ?, ?)"  # Fixed sentence with four placeholders
cursor.executemany(insert_sql, rows_to_add)  # Run that insert once for each tuple
connection.commit()  # Save the inserts into practice.db
cursor.execute("SELECT id, full_name, email, city, marks FROM students")  # Read every student column
all_students = cursor.fetchall()  # Copy the result into a Python list of tuples
for student in all_students:  # Take one tuple at a time
    print(student)  # Show id, name, email, city, and marks
connection.close()  # Close the database file
```

Run it from the terminal, in the folder that contains the file:

```bash
python3 read_students.py   # Create practice.db, insert two students, and print both rows
```

How the code works:

- `connect` opens `practice.db`. `execute` sends one statement. `executemany` repeats the insert once per tuple.
- Four `?` marks line up with four values. A name such as `O'Brien` stays data. Gluing that name into the sentence with quotes can break the statement.
- `commit` writes the inserts. Skip it and a later open can show no rows. `fetchall` returns tuples such as `(1, 'Asha Rao', 'asha@example.com', 'Pune', 88)`.
- An API you have already run would call this kind of code on a request, then place the tuples in a JSON reply. `campus.sql` writes `campus.db`. This program writes `practice.db`.

### Student activity: build the books table

Compare your paper design with this sample. Save it as `books.sql`. From the terminal run `sqlite3 -header -column library.db < books.sql`.

```sql
DROP TABLE IF EXISTS books; -- Reset this practice table only
CREATE TABLE books ( -- One row means one book
    id INTEGER PRIMARY KEY, -- Identity filled by SQLite when omitted
    title TEXT NOT NULL, -- Title must be present
    author TEXT NOT NULL, -- Author must be present
    price REAL NOT NULL CHECK (price >= 0), -- Rupees and paise; negative price is refused
    copies INTEGER NOT NULL DEFAULT 0 CHECK (copies >= 0) -- Shelf count; omit it to store 0
) STRICT; -- Keep the declared types
INSERT INTO books (title, author, price, copies) -- Leave id out
VALUES ('The Blue Umbrella', 'Ruskin Bond', 199.00, 4); -- Four copies of this title
INSERT INTO books (title, author, price) -- copies is omitted, so DEFAULT 0 is used
VALUES ('Malgudi Days', 'R. K. Narayan', 249.50); -- REAL allows the paise in 249.50
SELECT id, title, author, price, copies -- Read the catalogue columns
FROM books -- Read them from the books table
ORDER BY title ASC; -- Alphabetical titles in this result only
```

How the code works:

- SQLite may print `199.0` and `249.5`. Those are the amounts you inserted.
- Malgudi Days shows `0` copies because `copies` was omitted. Title order prints it before The Blue Umbrella.
- The `id` values stay 1 and 2. `library.db` is separate from `campus.db` and `practice.db`.

## If something breaks — check this list

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `.tables` prints nothing | `CREATE TABLE` has not run in this file | Run `sqlite3 campus.db < campus.sql` |
| `no such table: students` | Wrong file, or the script never ran | Stay in the project folder and open `campus.db` |
| `near ")": syntax error` | Comma after the last column, or a comma missing | Commas between columns only, none after the last column |
| SQLite sits with no reply | The semicolon is missing | Type `;` and press Enter |
| `UNIQUE constraint failed: students.email` | That email is already stored | Use another email. The rule is working |
| `NOT NULL constraint failed: students.full_name` | The name was left out | Include `full_name` in the column list and in `VALUES` |
| `CHECK constraint failed` | Marks, price, or copies broke the range | Marks from 0 to 100. Price or copies of 0 or more |
| `cannot store TEXT value in INTEGER column` | A word was sent to a number column | Send a number, without quotes |
| City is blank instead of `Not given` | NULL or `''` was written in | Omit `city` from the column list |
| Python later shows no rows | `commit()` was skipped | Call `commit()` before `close()` |
| Your extra student vanished | `campus.sql` ran again | Insert your row after the rebuild |

Connecting idea: `CREATE TABLE` sets the rules, `INSERT` adds rows those rules accept, and `SELECT` reads columns back while the stored table stays in place.

## Key Takeaways

- A **relational database** keeps tables of rows and columns on disk, so the backend still has the records after the program stops. SQLite stores that database in one file, such as `campus.db`.
- **CREATE TABLE** names the columns and their types, then adds a **primary key** and the constraints `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK`. `STRICT` makes those types hold.
- **INSERT** adds rows. Leave an `INTEGER PRIMARY KEY` out of the column list so SQLite can number the row, and omit a column when you want its default. A broken rule cancels that statement and keeps the older rows.
- **SELECT** retrieves data. You choose columns, rename headings with `AS`, sort the answer with `ORDER BY`, shorten it with `LIMIT`, and collapse repeated values with `DISTINCT`.
- In the next session you will change values already stored in a row, remove a row while keeping the table, and read only the rows that match a condition.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
| --- | --- |
| Relational database | Tables of rows and columns on disk |
| RDBMS / SQLite | Software that stores the tables; today’s engine is one file |
| SQL | Language of `CREATE`, `INSERT`, and `SELECT` |
| `campus.db` / `practice.db` / `library.db` | Students script, Python program, and books script |
| `sqlite3 campus.db` | Open the SQLite prompt |
| `sqlite3 -header -column campus.db < campus.sql` | Print a grid and run a script file |
| `.headers on` / `.mode column` | Show names and align a grid |
| `.tables` / `.schema students` / `.quit` | List tables, show the design, leave |
| `NULL` | No value stored; different from `0` and from `''` |
| `INTEGER` / `TEXT` / `REAL` | Whole number, words, number that may include a fraction |
| `PRIMARY KEY` | Unique row identity; here, `id` |
| `INTEGER PRIMARY KEY` | SQLite fills `id` when the insert omits it |
| `NOT NULL` / `UNIQUE` | Required value, or a value that cannot repeat |
| `DEFAULT` | Used when that column is omitted from `INSERT` |
| `CHECK` / `STRICT` | Save-time rule, and real type checking |
| `DROP TABLE IF EXISTS` | Remove a practice table so a script can rebuild it |
| `INSERT INTO ... VALUES` | Add one row or several rows |
| `SELECT` / `FROM` / `SELECT *` | Read chosen columns, or every column |
| `AS` | Heading for this result only |
| `ORDER BY` / `ASC` / `DESC` | Sort the result, smallest first or largest first |
| `LIMIT` / `DISTINCT` | Shorter answer, or each different value once |
| `?` / `commit()` / `fetchall()` | Placeholder, save from Python, copy rows into a list |
