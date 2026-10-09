# Objective Assignment: Database Fundamentals & SQL (Part II)

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A clinic keeps four rows in `visits`. The receptionist runs:

```sql
SELECT visit_id, patient_name
FROM visits
WHERE city = 'Pune';
```

The grid shows one row. What is true about the other three visits?

A. They are deleted because they failed the city test  
B. The `visits` table is dropped, and only the Pune row is saved in a new table  
C. They stay stored in `visits`; this query only leaves them out of the answer  
D. Their city values are rewritten to an empty box  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because `WHERE` only filters this result. Rows that fail the test remain in the table.

A is incorrect because a `SELECT` does not remove rows. B is incorrect because this statement does not drop the table. D is incorrect because a filter does not write new city values.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

One stored city is the text `Chennai`. Which condition keeps that row in the result?

A. `WHERE city = 'chennai'`  
B. `WHERE city = 'Chennai'`  
C. `WHERE city = Chennai`  
D. `WHERE city IS NULL`  

**Correct Answer:** B

**Answer Explanation:**  
B is correct because text must match the stored capitals, and text in a condition uses single quotes.

A is incorrect because `chennai` and `Chennai` are different, so the result is empty. C is incorrect because missing quotes make PostgreSQL look for a column named Chennai. D is incorrect because this city is filled; `IS NULL` looks for an empty box.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

`students` holds these marks:

| full_name | marks |
| --- | --- |
| Asha Rao | 88 |
| Rahul Mehta | 76 |
| Meera Iyer | 91 |
| Imran Khan | 64 |

This query is run:

```sql
SELECT full_name
FROM students
WHERE marks < 80;
```

Who appears?

A. Asha Rao and Meera Iyer  
B. Meera Iyer only  
C. All four students  
D. Rahul Mehta and Imran Khan  

**Correct Answer:** D

**Answer Explanation:**  
D is correct because 76 and 64 are less than 80. Rahul and Imran pass the test.

A is incorrect because 88 and 91 fail `marks < 80`. B is incorrect because Meera’s 91 does not pass, and Rahul also passes. C is incorrect because Asha and Meera fail the test and are left out of this answer. They remain stored.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

Asha Rao is `id` 1. Her email is `asha@example.com` and her city is `Pune`. This statement succeeds:

```sql
UPDATE students
SET marks = 90
WHERE id = 1;
```

What is true afterwards?

A. Only Asha’s marks become 90; her email and city stay as they were  
B. Every student’s marks become 90  
C. Asha’s `id` becomes 90  
D. Asha’s row is removed and a new row is inserted for her  

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `SET` names the new marks, `WHERE id = 1` limits the change to Asha, and the other columns on her row stay.

B is incorrect because the condition stops the change from reaching every row. C is incorrect because `id` is not in `SET`. D is incorrect because `UPDATE` edits the existing row; it does not delete and insert.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

`marks` must stay from 0 to 100 (`CHECK (marks >= 0 AND marks <= 100)`). Asha’s marks are 90. This statement is run:

```sql
UPDATE students
SET marks = 150
WHERE id = 1;
```

What happens?

A. Marks become 150, because the check applies only when a row is first inserted  
B. Marks become 100, and the extra 50 is ignored  
C. The statement is cancelled, and Asha’s marks stay 90  
D. The `students` table is dropped because 150 is illegal  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because the check still applies on `UPDATE`. The statement is cancelled, and a failed update does not half-save the row.

A is incorrect because the same rule rejects 150 on update. B is incorrect because PostgreSQL does not clamp the value to 100. D is incorrect because a failed update leaves the table in place.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

`hostels` contains id 1 (`Pune House`) and id 4 (`Guest House`). Student 3 exists, and `students.hostel_id` references `hostels`. Two students still store `hostel_id` 1. No student stores `hostel_id` 4.

Which statement is refused?

A. `SELECT hostel_name FROM hostels WHERE id = 4`  
B. `DELETE FROM hostels WHERE id = 4`  
C. `UPDATE students SET hostel_id = 1 WHERE id = 3`  
D. `DELETE FROM hostels WHERE id = 1`  

**Correct Answer:** D

**Answer Explanation:**  
D is correct because a foreign key will not leave students pointing at a hostel that no longer exists. Pune House stays while those students still use id 1.

A is incorrect because reading Guest House is allowed. B is incorrect because Guest House has no student pointing at it, so that delete removes only hostel 4. C is incorrect because hostel 1 exists, so storing `hostel_id` 1 is allowed.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A city column has three kinds of rows: one stores `Pune`, one stores `Not given`, and one was never filled (empty).

Which statements are correct?

A. `WHERE city = NULL` returns the row whose city was never filled  
B. `WHERE city IS NULL` returns the row whose city was never filled  
C. A row that fails the city test is deleted by that `SELECT`  
D. `WHERE city = 'Not given'` returns the row that stores those words  
E. `WHERE city = 'Pune'` returns the Pune row and leaves the other rows stored  

**Correct Answers:** B, D, E

**Answer Explanation:**  
B is correct because an empty box is tested with `IS NULL`. D is correct because `Not given` is real text, found with `=`. E is correct because `WHERE` filters the answer and does not remove the other rows.

A is incorrect because `= NULL` does not find an empty box. C is incorrect because this `SELECT` does not delete rows.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

Which statements are correct?

A. `UPDATE students SET city = 'Pune'` with no `WHERE` rewrites every city  
B. `INSERT` needs a `WHERE` clause so the new row can be tested before it is added  
C. Two `SET` assignments must be separated by a comma; without it, the statement fails and no column changes  
D. `DELETE FROM students` with no `WHERE` removes every row and leaves the table in place  
E. `RETURNING` can show the row an `UPDATE` or `DELETE` just touched  

**Correct Answers:** A, C, D, E

**Answer Explanation:**  
A is correct because a missing `WHERE` on `UPDATE` changes every row. C is correct because a missing comma between `SET` assignments is a syntax error, and no column changes. D is correct because `DELETE` without `WHERE` empties the rows and keeps the columns; that is different from `DROP TABLE`. E is correct because `RETURNING` shows the row that was changed or removed.

B is incorrect because `INSERT` has no `WHERE`; the row is not there yet to test.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

Use this stored state:

- Students 1 and 2 both store `hostel_id` 1. Each of those rows has only one hostel id.
- `enrolments` holds pairs `(student_id, course_id)`: `(1, 1)`, `(1, 2)`, and `(3, 1)`.
- The primary key of `enrolments` is `(student_id, course_id)`.
- Course names live only in `courses`. Pair rows store ids.

Which statements are correct?

A. Two students sharing hostel id 1 is a one-to-many link: one hostel, many students  
B. Student 1’s two courses should both be saved in that student’s single `hostel_id` column  
C. `DELETE FROM enrolments WHERE student_id = 1 AND course_id = 2` removes that pair only; student 1 and the course row remain  
D. Inserting `(3, 1)` again is rejected because that pair is already stored  
E. `SELECT student_id, course_id FROM enrolments WHERE student_id = 1` returns course names such as `Databases`  

**Correct Answers:** A, C, D

**Answer Explanation:**  
A is correct because many child rows may store the same parent id, while each student still has one hostel value. C is correct because deleting one enrolment removes the link, not the student and not the course. D is correct because the pair primary key blocks a second copy of `(3, 1)`.

B is incorrect because one column cannot hold two course ids; those pairs belong in a link table. E is incorrect because `enrolments` returns ids, not the course name from `courses`.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

`students.id` is generated by default as identity, and inserts omit `id`. Rows 1, 2, 3, and 4 are already stored. A practice row is inserted and receives id 5, then removed with `DELETE FROM students WHERE email = 'practice@example.com'`. `enrolments` stores pairs that reference `students`. `hostels` is the parent of `hostel_id`.

Which statements are correct?

A. `DROP TABLE students` is the safe first step while `enrolments` still references `students`  
B. The next insert that omits `id` does not receive id 5  
C. If `DELETE FROM students WHERE marks < 90` would match two people, run that same `WHERE` in a `SELECT` before deleting  
D. When a new email breaks the unique rule, the new email is saved and only the other columns roll back  
E. A foreign key on `hostel_id` means two students cannot store the same hostel id  

**Correct Answers:** B, C

**Answer Explanation:**  
B is correct because identity keeps counting forward. Deleting the row that used id 5 does not give 5 to the next insert that omits `id`. C is correct because a condition can match more rows than you expect, so the same `WHERE` should be read with `SELECT` first.

A is incorrect because link rows that point at students have to go first. Dropping `students` while `enrolments` still references it is not the safe first step. D is incorrect because a failed update is cancelled. The old email stays, and the row is not half-saved. E is incorrect because the foreign key only demands that the hostel id exist. Many students may store the same `hostel_id`.
