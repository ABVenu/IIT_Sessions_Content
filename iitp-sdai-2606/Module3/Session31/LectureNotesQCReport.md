# Lecture Notes QC Report: Database Fundamentals & SQL (Part I)

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Four curriculum topics are present: why a relational database sits behind a backend, `CREATE TABLE` with a primary key and constraints, `INSERT`, and `SELECT`.
- Later topics are not taught: no `UPDATE`, `DELETE`, `WHERE`, relationships, joins, or aggregate functions.
- Structural Adherence dropped because the first complete draft was **614** lines. The required length is **480–500**.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Trimmed the notes to **494** lines. Full `campus.sql`, rejected inserts, `SELECT` forms, `read_students.py`, and `books.sql` remain, each with a comment on every code line.
- Split paragraphs that ran past three sentences. Renamed the read activity to four steps so the heading matches the list.
- Checked the scripts: four student rows, four rejected inserts, `LIMIT 2` returns Meera then Asha, `DISTINCT city` returns four cities, the books script prints Malgudi Days then The Blue Umbrella, and `read_students.py` prints two tuples.
- No session numbers. Forward links say “next” or “upcoming” only. No duration, audience, or internal instruction wording in the student notes.

Expected QC result achieved.
