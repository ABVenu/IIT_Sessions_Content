# Objective Assignment: Advanced SQL – JOINs

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A library keeps members and branches in two tables. A member’s `branch_id` points at `branches.id`. Store Room is branch 4, and nobody points at it.

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

The desk runs:

```sql
SELECT m.full_name, br.branch_name
FROM members AS m
INNER JOIN branches AS br
ON m.branch_id = br.id;
```

Which statement is true?

A. Anil Joshi is left out because two members share Central Branch  
B. Bina Kapoor is left out because a shared branch can match only one member  
C. Esha Roy is left out because her `branch_id` matches no branch row  
D. Store Room is returned with a blank member name  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because an inner join keeps a row only when `ON` finds a match. Esha’s `branch_id` is empty, so she matches nothing and is left out of this answer.

A is incorrect because Anil’s `branch_id` 1 matches Central Branch, so he stays. B is incorrect because one branch may match many members. Anil and Bina both appear with Central Branch, on two result rows. D is incorrect because Store Room is on the right and no member points at it, so an inner join from members does not return it.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

Bina Kapoor is member 2, and her `branch_id` is 1. Central Branch is branch 1. North Branch is branch 2.

The desk wants Bina on the same result row as Central Branch. Which `ON` does that?

A. `ON m.id = br.id`  
B. `ON m.branch_id = br.id`  
C. `ON m.full_name = br.branch_name`  
D. `ON m.id = br.branch_name`  

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the stored link is the foreign key: the member’s `branch_id` equals the branch’s own `id`. Bina’s `branch_id` 1 matches Central Branch.

A is incorrect because `m.id` and `br.id` are both identity numbers, not the link. Bina’s id is 2, so that rule pairs her with North Branch. C is incorrect because a person’s name is not equal to a branch name. D is incorrect because an id and a branch name are not the same kind of value, and they are not the stored link.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

The register is:

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

The desk runs:

```sql
SELECT m.full_name, br.branch_name
FROM members AS m
LEFT JOIN branches AS br
ON m.branch_id = br.id;
```

Which statement is true?

A. Store Room appears beside a blank member name  
B. Esha Roy is dropped, in the same way an inner join drops her  
C. `branch_name` is copied into the stored `members` table  
D. Esha Roy appears, and `branch_name` on her result row is NULL  

**Correct Answer:** D

**Answer Explanation:**  
D is correct because the left table is `members`, the table after `FROM`. A left join keeps every member. Esha has no matching branch, so `branch_name` comes back NULL. A blank cell in the grid is that NULL, not the word “empty”.

A is incorrect because Store Room sits on the right. A left join from members does not keep an unmatched branch. B is incorrect because a left join does not drop the left table. C is incorrect because a join only builds an answer. The stored `members` rows stay as they are.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

Both `members` and `branches` have a column named `id`. This statement is run:

```sql
SELECT id, m.full_name
FROM members AS m
INNER JOIN branches AS br
ON m.branch_id = br.id;
```

What happens?

A. PostgreSQL reports that the column reference `id` is ambiguous  
B. The bare `id` is taken from `members`, because that table is written after `FROM`  
C. The bare `id` is taken from `branches`, because that table is joined second  
D. `AS m` permanently renames the stored table, so later queries must say `m`  

**Correct Answer:** A

**Answer Explanation:**  
A is correct because both tables have `id`. After the join, a bare `id` could mean either table, so PostgreSQL refuses it. The fix is a prefixed column, such as `m.id` or `br.id`.

B is incorrect because the left table is not the automatic choice when both sides have the same column name. C is incorrect because join order does not pick the bare name either. D is incorrect because `AS m` is a nickname for this query only. The stored table is still named `members`.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

Clubs live in `clubs`. Pairs of `member_id` and `club_id` live in `memberships`. The register is:

| member id | full_name | Clubs in `memberships` |
| --- | --- | --- |
| 1 | Anil Joshi | Fiction Club, Poetry Club |
| 2 | Bina Kapoor | Fiction Club |
| 3 | Charu Sen | Fiction Club |
| 4 | Dev Malik | Poetry Club |
| 5 | Esha Roy | none |

Chess Club exists in `clubs`. No pair points at it.

The desk runs:

```sql
SELECT m.full_name, c.club_name
FROM members AS m
LEFT JOIN memberships AS ms
ON m.id = ms.member_id
LEFT JOIN clubs AS c
ON ms.club_id = c.id
WHERE c.club_name = 'Poetry Club';
```

Who appears?

A. Bina Kapoor and Charu Sen only  
B. Esha Roy and Dev Malik only  
C. Anil Joshi and Dev Malik only  
D. All five members, with Poetry Club filled in only for Anil and Dev  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because `WHERE c.club_name = 'Poetry Club'` keeps only finished rows whose club title is Poetry Club. Anil and Dev have that club. Each appears once.

A is incorrect because Bina and Charu are in Fiction Club only, so their rows fail this test. B is incorrect because Esha has no Poetry Club row. Her club name is NULL, and NULL fails `= 'Poetry Club'`. D is incorrect because this test is in `WHERE`, so it throws away rows that are not Poetry Club. The word `LEFT` stays in the statement, but the other members do not.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

The register is:

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

Which query returns one row, and that row’s branch name is Store Room?

A.

```sql
SELECT br.branch_name
FROM members AS m
INNER JOIN branches AS br
ON m.branch_id = br.id
WHERE br.branch_name = 'Store Room';
```

B.

```sql
SELECT m.full_name
FROM members AS m
LEFT JOIN branches AS br
ON m.branch_id = br.id
WHERE br.id IS NULL;
```

C.

```sql
SELECT br.branch_name
FROM members AS m
LEFT JOIN branches AS br
ON m.branch_id = br.id
WHERE br.branch_name = 'Store Room';
```

D.

```sql
SELECT br.branch_name
FROM branches AS br
LEFT JOIN members AS m
ON m.branch_id = br.id
WHERE m.id IS NULL;
```

**Correct Answer:** D

**Answer Explanation:**  
D is correct because Store Room has to stay in the result, so `branches` is written after `FROM`. The left join keeps every branch. `WHERE m.id IS NULL` then keeps only the branch whose member side never matched. That branch is Store Room.

A is incorrect because an inner join has already dropped Store Room. The name test has no Store Room row left to keep, so the result is empty. B is incorrect because members are on the left, so `br.id IS NULL` returns Esha Roy, not Store Room. C is incorrect because a `WHERE` test on the right table drops the empty branch rows, and no member actually has Store Room, so the result is empty.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

The pairs are:

| member id | full_name | Clubs in `memberships` |
| --- | --- | --- |
| 1 | Anil Joshi | Fiction Club, Poetry Club |
| 2 | Bina Kapoor | Fiction Club |
| 3 | Charu Sen | Fiction Club |
| 4 | Dev Malik | Poetry Club |
| 5 | Esha Roy | none |

Chess Club exists in `clubs`. No pair points at it.

The desk runs:

```sql
SELECT m.full_name, c.club_name
FROM members AS m
INNER JOIN memberships AS ms
ON m.id = ms.member_id
INNER JOIN clubs AS c
ON ms.club_id = c.id;
```

Which statements are correct?

A. Anil Joshi appears on two result rows, one for Fiction Club and one for Poetry Club  
B. Esha Roy appears once, with `club_name` NULL  
C. Chess Club does not appear  
D. A second copy of Anil Joshi is inserted into the stored `members` table  
E. Each `JOIN` needs its own `ON`  

**Correct Answers:** A, C, E

**Answer Explanation:**  
A is correct because one member with two pairs becomes two result rows. The stored member is still one row. C is correct because no pair points at Chess Club, so both inner joins leave it out. E is correct because each hop has its own match rule. A missing second `ON` is a syntax error.

B is incorrect because Esha has no row in `memberships`. The inner joins drop her. There is no NULL club row to show. D is incorrect because a join only builds an answer. It does not insert a row into `members`.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

The register is:

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

The desk runs:

```sql
SELECT br.branch_name, m.full_name
FROM branches AS br
LEFT JOIN members AS m
ON m.branch_id = br.id;
```

Which statements are correct?

A. Esha Roy appears with a NULL `branch_name`  
B. Store Room appears once, and `full_name` on that row is NULL  
C. Central Branch appears as one row with both Anil Joshi and Bina Kapoor in the same cell  
D. North Branch appears with Charu Sen  
E. Adding `ORDER BY br.id` brings Esha Roy into this result  

**Correct Answers:** B, D

**Answer Explanation:**  
B is correct because branches are on the left, so Store Room is kept. No member points at it, so `full_name` is NULL. D is correct because Charu’s `branch_id` is 2, and North Branch is id 2, so that pair is one result row.

A is incorrect because Esha is on the right and her `branch_id` matches nothing. A left join from branches does not keep her. C is incorrect because two matches become two rows, not one cell that holds a list of names. Central Branch appears once with Anil and once with Bina. E is incorrect because `ORDER BY` only sorts the rows already included. It does not add Esha.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

Poetry Club is club id 2. Members and branches are:

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

The club pairs are:

| member id | full_name | Clubs in `memberships` |
| --- | --- | --- |
| 1 | Anil Joshi | Fiction Club, Poetry Club |
| 2 | Bina Kapoor | Fiction Club |
| 3 | Charu Sen | Fiction Club |
| 4 | Dev Malik | Poetry Club |
| 5 | Esha Roy | none |

Which statements are correct?

A. After left joins from `members` through `memberships` to `clubs`, `WHERE c.club_name = 'Poetry Club'` drops every result row that is not Poetry Club, including Esha Roy  
B. `LEFT JOIN memberships AS ms ON m.id = ms.member_id AND ms.club_id = 2`, then a left join to `clubs`, keeps all five members, and the club name is Poetry Club only for Anil Joshi and Dev Malik  
C. An inner join from `members` to `branches`, followed by `WHERE br.id IS NULL`, returns Esha Roy  
D. A left join from `members` to `branches` on `m.branch_id = br.id`, followed by `WHERE br.id IS NULL`, returns Esha Roy  
E. `AS m` renames the stored `members` table, so the next query must use `m`  

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because a `WHERE` test on the right table filters the finished answer. Esha’s club name is NULL, and Bina and Charu are in Fiction Club, so those rows fail `= 'Poetry Club'`. Anil and Dev remain.

B is correct because `ms.club_id = 2` sits inside `ON`. It chooses which pair may stick. It does not delete members who have no Poetry Club pair. Anil and Dev show Poetry Club. Bina, Charu, and Esha stay, with a NULL club name.

D is correct because the left join keeps Esha with an empty branch, and `br.id IS NULL` keeps that unmatched left row.

C is incorrect because the inner join has already thrown Esha away. No empty branch row remains, so the result is empty. E is incorrect because a table alias lasts for one query. The stored name stays `members`.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

The register is:

| id | full_name | branch_id |
| --- | --- | --- |
| 1 | Anil Joshi | 1 |
| 2 | Bina Kapoor | 1 |
| 3 | Charu Sen | 2 |
| 4 | Dev Malik | 3 |
| 5 | Esha Roy | NULL |

| id | branch_name |
| --- | --- |
| 1 | Central Branch |
| 2 | North Branch |
| 3 | East Branch |
| 4 | Store Room |

Which statements are correct?

A. `SELECT m.id, br.id` is legal on a join of `members` and `branches`, because each `id` names its table  
B. An `INNER JOIN` written with no `ON` is a syntax error  
C. This inner join pairs Dev Malik with Store Room:

```sql
SELECT m.full_name, br.branch_name
FROM members AS m
INNER JOIN branches AS br
ON m.id = br.id;
```

D. A left join from `members` to `branches` on `m.branch_id = br.id`, then `WHERE br.branch_name = 'Central Branch'`, returns only Anil Joshi and Bina Kapoor  
E. That Central Branch join writes a branch id into Esha Roy’s stored `branch_id`  

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A is correct because a prefixed column tells PostgreSQL which table’s `id` to read. The bare name `id` would be ambiguous. Both tables have `id`.

B is correct because every join needs its own `ON`. Without it, PostgreSQL reports a syntax error at the join.

C is correct because `ON m.id = br.id` matches identity numbers, not `branch_id`. Dev’s id is 4 and Store Room’s id is 4, so this result puts those two together even though his allotted branch is East Branch. The same rule also pairs Bina (id 2) with North Branch, not with Central Branch.

D is correct because `WHERE br.branch_name = 'Central Branch'` filters the finished answer. Anil and Bina match Central Branch. Charu, Dev, and Esha do not remain. Esha’s NULL branch name fails the test, so this left join behaves like an inner join for that filter.

E is incorrect because a join does not change stored rows. A later read of `members` still shows Esha’s `branch_id` empty.
