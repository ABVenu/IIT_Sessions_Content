# Assignment — Objective (Session 15)

**Instructions:** Answer all questions. For multiple-select questions, choose every option that correctly completes the statement.

---

## Section A — Multiple choice (single correct)

### Q1 (Easy)

A product catalog column `sku` stores codes like `AI-100`, `AI-200`, and `HR-50`. You want every SKU that **starts with** `AI-`. Which `WHERE` clause is correct?

- A) `WHERE sku = 'AI-'`
- B) `WHERE sku LIKE 'AI-%'`
- C) `WHERE sku LIKE '%AI-'`
- D) `WHERE sku LIKE 'AI_'`

---

### Q2 (Easy)

You need the **newest** rows first using a column `created_at`. Which clause does that?

- A) `ORDER BY created_at ASC`
- B) `ORDER BY created_at DESC`
- C) `ORDER BY created_at`
- D) `SORT BY created_at NEWEST`

---

### Q3 (Easy)

A table lists 10,000 support threads. You only want the **first 20** rows after sorting. Which clause caps the result size?

- A) `OFFSET 20`
- B) `LIMIT 20`
- C) `TOP 20` (standard in all SQL engines)
- D) `CAP 20`

---

### Q4 (Easy)

Table `events` has stable numeric `event_id` values. Page size is **4**, and you want **page 3** (1-based), using `ORDER BY event_id ASC`, `LIMIT 4`. What `OFFSET` value completes the pagination pattern?

- A) `3`
- B) `8`
- C) `12`
- D) `2`

---

### Q5 (Moderate)

You paginate with `ORDER BY id ASC`, `LIMIT 5`, and `OFFSET`. Which `OFFSET` value returns rows whose **1-based positions** in that ordering are **11 through 15** (inclusive)?

- A) `OFFSET 5`
- B) `OFFSET 10`
- C) `OFFSET 11`
- D) `OFFSET 15`

---

### Q6 (Moderate)

You model **learners** and **skills** where each learner may list many skills and each skill tag may apply to many learners. Which design best matches a **many-to-many** relationship?

- A) Store a comma-separated `skills` text column on `learners`
- B) Add `learner_id` as a column on `skills` only (one FK total)
- C) Add a `learner_skills` table with `(learner_id, skill_id)` pairs
- D) Duplicate one full row per learner inside `skills` for every match

---

## Section B — Multiple choice (multiple correct)

### Q7 (Moderate) — Select all that apply

Which statements about **normalization** (as described for relational design) are **true**?

- A) It aims to reduce repeating the same fact across many rows
- B) It guarantees every query will run faster than a single wide table
- C) It often means splitting one wide design into smaller tables linked by identifiers
- D) It removes the need for joins when reading reports

---

### Q8 (Moderate) — Select all that apply

Consider: `SELECT * FROM shipments ORDER BY shipment_id ASC LIMIT 10 OFFSET 20;`  
Which statements are **true**?

- A) At most ten rows can appear in the result
- B) The first twenty rows in the chosen ordering are skipped before the limit is applied
- C) This always returns “page 2” if page size is 10 (using 1-based page numbering)
- D) PostgreSQL supports `OFFSET` in this pattern

---

### Q9 (Hard) — Select all that apply

You run a **cross join** between `customers` (200 rows) and `promo_codes` (50 rows) with **no** `ON` filter between them. Which statements are **true**?

- A) The result has at most 250 rows
- B) The result can contain pairs that do not represent a real customer–promo association
- C) The row count is multiplicative in the two table sizes (before any further filtering)
- D) This pattern is usually the safest default for production “lookup” screens

---

### Q10 (Hard) — Select all that apply

Which statements about **foreign keys** and **inner joins** are **true**?

- A) A child row’s foreign key column stores an identifier that references a parent row
- B) An `INNER JOIN ... ON parent.id = child.parent_id` keeps rows where that match holds in both tables
- C) An inner join between parent and child always includes parent rows that have **zero** matching child rows
- D) Table aliases (for example `FROM orders o`) are mainly useful to shorten names and resolve ambiguous column references

---

## Answer key (for facilitators / LMS “Answer Explanation”)

### Q1

- **Correct:** B  
- **Why:** In SQL `LIKE`, `%` matches **any sequence of characters (including empty)** after the literal prefix `AI-`.  
- **Why others are wrong:** A is exact equality. C matches strings that **end** with `AI-`, not necessarily start with `AI-`. D uses `_` which matches **exactly one** character, not “any length suffix.”

### Q2

- **Correct:** B  
- **Why:** `DESC` sorts from largest/latest to smallest/earliest for typical timestamps.  
- **Why others are wrong:** A/C sort oldest/lowest first (ASC default). D is not valid SQL in this form.

### Q3

- **Correct:** B  
- **Why:** `LIMIT` caps how many rows are returned.  
- **Why others are wrong:** `OFFSET` skips rows; it does not cap size. `TOP` is engine-specific (not universal). `CAP` is not standard SQL.

### Q4

- **Correct:** B  
- **Why:** 1-based page \(p\) with page size \(n\): `OFFSET = (p - 1) * n`. Here \((3 - 1) * 4 = 8\).  
- **Why others are wrong:** A/D are common off-by-one mistakes; C would correspond to page 4 for size 4.

### Q5

- **Correct:** B  
- **Why:** Positions 11–15 are the **third** page when the page size is 5, and pages start at offset \((page - 1) \times page\_size = (3 - 1) \times 5 = 10\).  
- **Why others are wrong:** A would target positions 6–10; C/D misalign the skip count with the intended 1-based slice.

### Q6

- **Correct:** C  
- **Why:** Many-to-many is typically modeled with a **junction/bridge** table holding pairs of foreign keys.  
- **Why others are wrong:** A is denormalized string packing. B is not sufficient alone for many-to-many. D is redundant row explosion, not a normalized bridge.

### Q7

- **Correct:** A, C  
- **Why:** Normalization reduces repeated facts and commonly splits tables linked by IDs.  
- **Why others are wrong:** B is false (not a performance guarantee). D is false (normalized designs often **use joins** when reading).

### Q8

- **Correct:** A, B, D  
- **Why:** `LIMIT 10` caps output; `OFFSET 20` skips 20 ordered rows; PostgreSQL supports `OFFSET` with `LIMIT` as described in the session notes.  
- **Why C is wrong:** With page size 10, `OFFSET 20` corresponds to **page 3**, not page 2.

### Q9

- **Correct:** B, C  
- **Why:** Cross join forms a Cartesian product (multiplicative size) and most pairs are not meaningful associations without a constraint.  
- **Why others are wrong:** A is false (200 × 50 = 10,000). D is false (usually not a safe UI default).

### Q10

- **Correct:** A, B, D  
- **Why:** FK stores parent identifiers; inner join keeps matched pairs; aliases help readability/ambiguity.  
- **Why C is wrong:** Inner join **drops** parent rows with **no** matching child rows.

---

## QC note

Per process requirements, a separate file `assignment question QC report.md` records per-question QC and aggregate ratings.
