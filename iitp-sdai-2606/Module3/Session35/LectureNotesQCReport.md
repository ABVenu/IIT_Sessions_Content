# Lecture Notes QC Report: SQLAlchemy ORM Fundamentals

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Topics present: ORM and why it is used with FastAPI, model definition, INSERT/SELECT/UPDATE/DELETE through a session, one-to-many `relationship`.
- Next-session overlap was avoided in the body (no FastAPI routes, no `Depends`/`get_db`, no mini app). The takeaways still named an AI query lab, which belongs to a later session.
- Structural Adherence dropped because the first complete draft was **478** lines. The required length is **480–500**. One opening paragraph ran to four sentences.
- Logical mistake: the INSERT analogy said “two hostel forms” while the sample creates four hostels.
- Presentation: instructor-facing “Do not turn today’s scripts into an API yet,” and the table-list comment promised an extra SQLite catalogue table that this script does not create.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Recap now starts from the previous session (aggregates), without session numbers. Upcoming FastAPI wiring is mentioned only as a connecting sentence.
- Removed the AI-lab line from Key Takeaways. Softened the “do not build an API yet” instruction.
- Corrected the INSERT analogy to four hostels and five students. Named `list_tables.py`. Corrected the expected table list. Replaced the inaccurate `LIMIT 1` mapping.
- Split the four-sentence opening. Length is **490** lines. Sample scripts were executed: five students, Pune House has two names, Neha’s hostel is `None`, update to 75, Guest House delete, relationship `append` all match the notes.

Expected QC result achieved.

## QC Iteration 3

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 3:

- Previous-session recap now matches the previous lecture: `campus-sql` SQL Editor, **COUNT / SUM / AVG / MIN / MAX**, **GROUP BY** (one number per hostel), **HAVING**, and “stored rows did not change.”
- Same five students and marks (90, 80, 91, 70, 85; class total 416, average 83.2) are named as that sample. Practice is local `campus.db`, not a repeat of the SQL Editor.
- Length is **491** lines. No session numbers. No FastAPI route wiring.

Expected QC result achieved.
