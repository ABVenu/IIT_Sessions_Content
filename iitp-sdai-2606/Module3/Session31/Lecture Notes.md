# Database Fundamentals & SQL (Part I)

You book a train ticket tonight. Tomorrow morning the same PNR is still on the screen.

The phone did not memorise that ticket. A program on a server stored the booking in an organised store, then read it back when you asked again.

In the previous session you decided which web pages may call your API, accepted an uploaded file, and let a small task run after the response was sent. Those tools move messages and files. They do not give you a grid of records that stays organised after the program stops.

This session adds that store. You will see why a backend uses a **relational database**, how to **design one table**, how to **add rows**, and how to **read those rows** back.

![A Python list disappears when the program stops; PostgreSQL inside Supabase still holds the student rows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session31/session31-01-list-vanishes-database-stays.png?v=20260928)

## What you will learn in this session

- Why a **relational database** belongs in the backend, beside the API you already run
- How a **table**, a **row**, a **column**, a **primary key**, and **constraints** fit together
- How to write **CREATE TABLE** so the database itself enforces the rules
- How to write **INSERT** to add records, and **SELECT** to retrieve them

You will work in a **Supabase** project. Supabase hosts a **PostgreSQL** database, and you will type SQL in its **SQL Editor**.

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
  - *Real-Life Example:* **PostgreSQL** is the RDBMS inside your Supabase project. You write the SQL. PostgreSQL stores the rows and checks the rules.
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

Common doubt: “Is the database the same thing as the API?” The API listens for HTTP. PostgreSQL, inside Supabase, stores the tables.

They work as a pair. Today you practise the SQL in the Supabase SQL Editor.

Common error: Treating a JSON example on the screen as saved data. JSON in a response is a message. The database is the saved grid.

Connecting idea: Once the data lives in a grid, the next step is to name the parts of that grid.

## How a table is organised

Picture one admission form that the office reprints for every student. The blank form is the design. Each filled form is one student.

![The students table: a column is one labelled box, a row is one student, id is the primary key, and an empty city cell is NULL](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session31/session31-02-students-table-anatomy.png?v=20260928)

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
| `NUMERIC` | An exact number that can include a fraction | Price `249.50` |

PostgreSQL rejects a value of the wrong type. The word `eighty` cannot be stored in an `INTEGER` column.

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

![Five constraints — primary key, not null, unique, default, and check — and the inserts they accept or reject](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session31/session31-03-constraints-database-enforces.png?v=20260928)

`id` is `INTEGER GENERATED BY DEFAULT AS IDENTITY`. Leave it out of `INSERT`, and PostgreSQL fills the next number. Email stays `UNIQUE`, so it cannot repeat, while `id` remains the stable identity of the row.

`CHECK` runs when a row is saved. Reading only the rows that match a condition comes in the next session.

Connecting idea: You have the design words. Next you open Supabase and turn that design into a real table.

## Supabase and the SQL Editor

- **PostgreSQL**
  - *Official Definition:* An open-source relational database system that stores tables and runs SQL.
  - *In Simple Words:* The software that keeps the grids and refuses rows that break the rules.
  - *Real-Life Example:* The register system in a college office. You do not install it. Supabase runs it for you.
- **Supabase**
  - *Official Definition:* A hosted platform that gives each project a PostgreSQL database and a browser tool for SQL.
  - *In Simple Words:* A login that opens your database. You type SQL in the browser and click Run.
  - *Real-Life Example:* The college keeps the attendance register online. You sign in from any computer. The register is not a file sitting on your laptop.
- **SQL Editor**
  - *Official Definition:* The Supabase page that sends your SQL to the project database and shows the rows that come back.
  - *In Simple Words:* A text box, a Run button, and a result grid under the box.
  - *Real-Life Example:* The clerk’s counter. You pass a slip. The reply appears on the same screen.
- **Statement**
  - *Official Definition:* One complete SQL instruction, ended with a semicolon.
  - *In Simple Words:* One full sentence to the database.
  - *Real-Life Example:* “Create the students grid” is one statement. “Add Asha” is the next statement.
- **Keyword**
  - *Official Definition:* A word SQL reserves for its grammar, such as `CREATE`, `TABLE`, `SELECT`, or `INSERT`.
  - *In Simple Words:* A printed word on the form. Names you invent, such as `students` or `email`, are your own.
  - *Real-Life Example:* These notes write keywords in CAPITALS so your eye can find them. SQL also accepts `select` in lowercase.

Create one project and reuse it for every exercise on this page.

1. Sign in at [supabase.com](https://supabase.com) and create a project named `campus-sql`.
2. Save the database password in a private note. Choose a region close to you, such as Mumbai if it is listed.
3. Wait until the project is ready. The editor cannot run SQL while the project is still starting.
4. Open **SQL Editor**. Use **New query** when you want a blank box.
5. Paste the script. Click once in an empty part of the box so that no lines stay highlighted.
6. Click **Run**. Read the grid under the editor.

Highlighted lines are the only lines Run will send. A highlight on the first statement leaves the rest unsent.

Open **Table Editor** after a successful run and choose `students`. That screen is the same table, drawn as a sheet. Queries still belong in the SQL Editor.

Common error: A missing semicolon. PostgreSQL reports `syntax error at or near` the next word. Each statement in these notes ends with `;`.

Common doubt: “Do I need a secret API key today?” No. The SQL Editor is already connected because you are signed in to the project.

Connecting idea: Next you design the columns, then Run a script that builds `students`, adds four rows, and reads them.

## Design of the students table

Decide the schema before you type. One row means one student. This session uses a single table.

| Column | Type | Rules | Why this rule |
| --- | --- | --- | --- |
| `id` | `INTEGER` | `GENERATED BY DEFAULT AS IDENTITY` and `PRIMARY KEY` | Identifies the row. PostgreSQL fills it when you omit it |
| `full_name` | `TEXT` | `NOT NULL` | A student row without a name cannot be used |
| `email` | `TEXT` | `NOT NULL` and `UNIQUE` | Required, and two rows cannot share it |
| `city` | `TEXT` | `DEFAULT 'Not given'` | If you omit city, this text is stored |
| `marks` | `INTEGER` | `NOT NULL` and `CHECK` from 0 to 100 | Required, and out-of-range marks are rejected |

Use letters, numbers, and underscores in names. `full_name` stays one word to SQL. A space in a name forces extra quoting and is a common slip.

### Student activity: design a books table on paper

Write this on paper before you read the sample script later in these notes. One row means one book.

Include `id` as the primary key, required text for title and author, and a price that cannot be negative. If copies are omitted, store `0`. Beside each name, write the type and the rule.

## Create the table and add the first rows

Paste the following into the Supabase **SQL Editor** and click **Run**. The script is complete: it rebuilds `students`, inserts four rows, and reads them back.

```sql
DROP TABLE IF EXISTS students; -- Remove a previous practice table so this script can start clean
CREATE TABLE students ( -- Define a new table named students
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, -- Identity number; omit it on INSERT and PostgreSQL assigns it
    full_name TEXT NOT NULL, -- Name is text and must be present
    email TEXT NOT NULL UNIQUE, -- Email is text, required, and cannot repeat
    city TEXT DEFAULT 'Not given', -- If city is omitted, store this text
    marks INTEGER NOT NULL CHECK (marks >= 0 AND marks <= 100) -- Whole number from 0 to 100
); -- End of the column list; no comma after the marks line
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

How the code works:

- `DROP TABLE IF EXISTS students` removes the **whole table**, both design and rows, so practice can start again. `IF EXISTS` means the first run still succeeds when the table is absent.
- `CREATE TABLE students` writes the schema in the `public` area of this Supabase project. There is **no comma after the `marks` line**.
- `GENERATED BY DEFAULT AS IDENTITY` numbers the row when `id` is left out. PostgreSQL also rejects the word `eighty` in `marks`, because that column is `INTEGER`.
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

![One script does three jobs: CREATE TABLE students, INSERT four rows, then SELECT them back](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session31/session31-04-create-insert-select.png?v=20260928)

## What appears under Run

The students script ends with `SELECT`, so the grid under **Run** is that answer.

| Last statement that ran | What you see |
| --- | --- |
| `DROP TABLE` or `CREATE TABLE` | Success. The design changed. There is no row grid |
| `INSERT` | Success. The row is saved even when the grid is empty |
| `SELECT` | The result rows |

An empty grid after `INSERT` does not mean the row is missing. Run a `SELECT`, or open **Table Editor**, to see the stored line.

Supabase shows the statement that just finished. A long script shows the **last** statement. That is why the students script ends with `SELECT`.

Common error: Only the `CREATE` line was highlighted, so the inserts never ran. Clear the highlight and Run the whole script.

- **`public` schema**
  - *Official Definition:* The default namespace in a Supabase database. Tables you create in the SQL Editor are stored there.
  - *In Simple Words:* The drawer labelled public. Both `students` and `books` land in it.
  - *Real-Life Example:* Table Editor lists `students` under `public`. In SQL the name `students` is enough.

`GENERATED BY DEFAULT AS IDENTITY` starts at 1 on a new table. The next successful insert that omits `id` receives the next number. After `DROP TABLE` and `CREATE TABLE`, numbering starts at 1 again.

Leave `id` out of `INSERT`. If you type an `id` that is already stored, the primary key rejects that row.

### Student activity: confirm the sheet and the query

1. Open **Table Editor** and select `students`.
2. Check that four rows are listed and that Rahul Mehta’s city is `Not given`.
3. Return to the SQL Editor and run the statement below.

```sql
SELECT id, full_name -- Identity and name only
FROM students -- The table you just built
ORDER BY id ASC; -- Smallest id first
```

How the code works:

- The grid lists Asha Rao, Rahul Mehta, Meera Iyer, and Imran Khan. The ids read 1, 2, 3, and 4.
- Table Editor shows the same people, including email, city, and marks.

Re-running the script rebuilds these four rows, because `DROP TABLE` removes `students` in this project and the inserts run again. Removing one student and keeping the table comes in the next session.

Common error: A comma after the last column, or a missing comma. PostgreSQL says `syntax error at or near ")"`. Text values use **single** quotes.

Connecting idea: The script shows the path that succeeds. The next statements are ones PostgreSQL should refuse.

## Inserts the database should reject

Run these in the SQL Editor only after the students script has succeeded. Highlight **one** statement, then click **Run**. Each one should fail, and the four good rows should remain.

```sql
INSERT INTO students (email, city, marks) -- full_name is required, and it is not in this column list
VALUES ('new@example.com', 'Pune', 70); -- Rejected because full_name is NOT NULL
INSERT INTO students (full_name, email, city, marks) -- Every required column is listed
VALUES ('Asha Rao', 'asha@example.com', 'Pune', 70); -- Email is already on row 1, so UNIQUE fails
INSERT INTO students (full_name, email, city, marks) -- The column list matches the values
VALUES ('Neha Shah', 'neha@example.com', 'Delhi', 120); -- 120 fails CHECK, which allows only 0 to 100
INSERT INTO students (full_name, email, city, marks) -- marks is declared INTEGER
VALUES ('Neha Shah', 'neha@example.com', 'Delhi', 'eighty'); -- PostgreSQL refuses text in an INTEGER column
```

How the code works:

- A refused `INSERT` does not leave a half-written row. The message names the rule, such as `students_email_key` or `students_marks_check`.
- The same person-name may appear on two rows. The same email may not.
- `CHECK` rejects marks outside 0 to 100. An integer column rejects the word `eighty`.

### Student activity: insert one valid row of your own

1. In the SQL Editor, click **New query**.
2. Insert one new student: your name, a fresh email, a city, and marks from 0 to 100. Omit `id`.
3. Run `SELECT id, full_name, email, city, marks FROM students;` and confirm your row appears with the next `id`.
4. Repeat the insert with that same email and confirm PostgreSQL rejects it.
5. Open **Table Editor**, select `students`, and confirm the new row is on the sheet.

If you later Run the full students script again, your extra row disappears, because that script drops and rebuilds the table. During practice, that reset is expected.

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

![SELECT builds a shorter answer sheet with aliases, order, limit, and distinct cities while the stored table stays unchanged](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session31/session31-05-select-reads-only.png?v=20260928)

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

- `FROM students` names the only table in this session. `AS` changes the heading on the answer. The stored column is still `full_name`.
- `ORDER BY` sorts the answer only. Read `id` again and the numbers are still 1, 2, 3, and 4.
- Zero rows returns an empty grid. `relation "students" does not exist` means `CREATE` has not run in this project.
- `SELECT full_name marks` with no comma treats `marks` as an alias, so one column comes back. The real column is `full_name`, so `name` raises `column "name" does not exist`.

Keeping only the rows that match a condition comes in the next session.

### Student activity: read the table in four ways

1. In a new SQL Editor query, show every column of every row.
2. Show only `full_name` and `city`, with headings `student_name` and `home_city`.
3. Show `full_name` and `marks`, smallest marks first, with `ORDER BY marks ASC`.
4. Show each different city once, in ascending order.

## Where this database sits in the backend

The SQL Editor is the practice counter. The API you have already built does not click Run. When a request arrives, that API can send the same `INSERT` or `SELECT` to this Supabase database and place the rows in a JSON reply.

- **Parameterised query**
  - *Official Definition:* A SQL statement kept fixed in a program, with the real values supplied separately.
  - *In Simple Words:* The sentence stays printed. Names and numbers travel beside it.
  - *Real-Life Example:* The withdrawal slip keeps its printed lines. The amount goes in the box. The customer does not rewrite the printed lines.

In the SQL Editor you type each value yourself, inside single quotes. That is the right way to learn the sentence.

A program that later sends a user’s name, such as `O'Brien`, should not glue that name into the sentence. The quote inside the name can break the SQL. The program passes the name beside a fixed statement.

You do not need the project URL or the secret keys for these exercises. Those values let a program connect. The SQL Editor is already connected, because you are signed in.

Common doubt: “Should I paste the database password into the SQL script?” No. The password protects the project. It is not a column and it is not part of `INSERT`.

### Student activity: build the books table

Compare your paper design with this sample. Paste it into a **new** SQL Editor query in the same `campus-sql` project, then click **Run**.

```sql
DROP TABLE IF EXISTS books; -- Reset this practice table only
CREATE TABLE books ( -- One row means one book
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, -- Identity filled by PostgreSQL when omitted
    title TEXT NOT NULL, -- Title must be present
    author TEXT NOT NULL, -- Author must be present
    price NUMERIC(6, 2) NOT NULL CHECK (price >= 0), -- Rupees and paise; negative price is refused
    copies INTEGER NOT NULL DEFAULT 0 CHECK (copies >= 0) -- Shelf count; omit it to store 0
); -- End of the column list
INSERT INTO books (title, author, price, copies) -- Leave id out
VALUES ('The Blue Umbrella', 'Ruskin Bond', 199.00, 4); -- Four copies of this title
INSERT INTO books (title, author, price) -- copies is omitted, so DEFAULT 0 is used
VALUES ('Malgudi Days', 'R. K. Narayan', 249.50); -- NUMERIC keeps the paise in 249.50
SELECT id, title, author, price, copies -- Read the catalogue columns
FROM books -- Read them from the books table
ORDER BY title ASC; -- Alphabetical titles in this result only
```

How the code works:

- `price` is `NUMERIC(6, 2)`, so two digits after the decimal stay exact. `copies` is `INTEGER`.
- The grid should show `199.00` and `249.50`. Malgudi Days shows `0` copies because `copies` was omitted.
- Title order prints Malgudi Days before The Blue Umbrella. The `id` values stay 1 and 2. `books` lives in the same project as `students`.

## If something breaks — check this list

| What you see | Likely cause | What to do |
| --- | --- | --- |
| SQL Editor will not run | The project is still starting | Wait until the project is ready, then click **Run** again |
| Only the first statement ran | Some lines were highlighted | Click a blank spot in the editor so nothing is selected, then **Run** |
| `relation "students" does not exist` | `CREATE TABLE` has not succeeded in this project | Run the full students script in this project |
| `syntax error at or near ")"` | Comma after the last column, or a comma missing | Commas between columns only, none after `marks` |
| `null value in column "full_name"` | The name was left out | Include `full_name` in the column list and in `VALUES` |
| `students_email_key` | That email is already stored | Use another email. The unique rule is working |
| `students_marks_check` or a price check | Marks, price, or copies broke the range | Marks from 0 to 100. Price or copies of 0 or more |
| `invalid input syntax for type integer` | A word was sent to a number column | Send a number, without quotes |
| City is blank instead of `Not given` | NULL or `''` was written in | Omit `city` from the column list |
| Table Editor looks empty | The sheet is stale, or you are in another project | Refresh Table Editor. Confirm the project name is `campus-sql` |
| Your extra student vanished | The full students script was run again | `DROP TABLE` rebuilds the four sample rows. Insert your row after that |

Connecting idea: `CREATE TABLE` sets the rules, `INSERT` adds rows those rules accept, and `SELECT` reads columns back while the stored table stays in place.

## Key Takeaways

- A **relational database** keeps tables of rows and columns so the backend still has the records after the program stops. In this session that database is **PostgreSQL**, opened through a **Supabase** project and its **SQL Editor**.
- **CREATE TABLE** names the columns and their types, then adds a **primary key**, `GENERATED BY DEFAULT AS IDENTITY`, and the constraints `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK`.
- **INSERT** adds rows. Leave `id` out of the column list so PostgreSQL can number the row, and omit a column when you want its default. A broken rule cancels that statement and keeps the older rows.
- **SELECT** retrieves data. You choose columns, rename headings with `AS`, sort the answer with `ORDER BY`, shorten it with `LIMIT`, and collapse repeated values with `DISTINCT`. Table Editor shows the same stored rows.
- In the next session you will change values already stored in a row, remove a row while keeping the table, and read only the rows that match a condition.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
| --- | --- |
| Relational database | Tables of rows and columns |
| PostgreSQL | The database engine inside the Supabase project |
| Supabase | The site where you sign in and open that database |
| SQL Editor | Browser box where you paste SQL and click **Run** |
| Table Editor | The same tables drawn as a sheet |
| `campus-sql` | The practice project for these exercises |
| `public` | The default place Supabase stores your tables |
| SQL | Language of `CREATE`, `INSERT`, and `SELECT` |
| Run | Sends the script, or only the highlighted lines |
| `NULL` | No value stored; different from `0` and from `''` |
| `INTEGER` / `TEXT` / `NUMERIC` | Whole number, words, exact number with a fraction |
| `NUMERIC(6, 2)` | Price with two digits after the decimal |
| `PRIMARY KEY` | Unique row identity; here, `id` |
| `GENERATED BY DEFAULT AS IDENTITY` | PostgreSQL fills `id` when the insert omits it |
| `NOT NULL` / `UNIQUE` | Required value, or a value that cannot repeat |
| `DEFAULT` | Used when that column is omitted from `INSERT` |
| `CHECK` | A rule checked when a row is saved |
| `DROP TABLE IF EXISTS` | Remove a practice table so a script can rebuild it |
| `INSERT INTO ... VALUES` | Add one row or several rows |
| `SELECT` / `FROM` / `SELECT *` | Read chosen columns, or every column |
| `AS` | Heading for this result only |
| `ORDER BY` / `ASC` / `DESC` | Sort the result, smallest first or largest first |
| `LIMIT` / `DISTINCT` | Shorter answer, or each different value once |
| `students_email_key` | The unique rule PostgreSQL creates for `email` |
| Parameterised query | A fixed SQL sentence, with values passed beside it |
