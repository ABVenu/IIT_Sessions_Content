# Objective Assignment — Introduction to Databases for AI Systems

## Instructions
- This assignment has **10 questions**: 6 Multiple Choice Questions (Single Correct) and 4 Multiple Select Questions (Multiple Correct).
- Questions are ordered progressively from Easy to Hard.
- Read each question carefully before selecting your answer(s).
- Submit via the LMS platform.

---

### Question 1 *(Easy | MCQ — Single Correct)*

A growing e-commerce startup stores all its order records in a single shared Excel file on a cloud drive. During a big sale event, three employees try to update different orders at the same time — and the file gets corrupted, causing permanent data loss.

Which specific limitation of file-based storage does this scenario most directly illustrate?

A) Lack of visual appeal in presenting data
B) Inability to handle concurrent access by multiple users
C) High infrastructure and licensing costs
D) Absence of automatic data backup features

**Answer:** B

**Explanation:** The scenario directly demonstrates the **concurrent access** problem — multiple users editing the same file simultaneously caused data corruption. Databases solve this using transaction management and locking mechanisms that prevent one user's changes from overwriting another's. Options A, C, and D describe issues that are unrelated to what the scenario shows.

---

### Question 2 *(Easy | MCQ — Single Correct)*

A developer creates a `products` table in Supabase with the following definition:

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL
);
```

After running three separate `INSERT INTO` statements — without specifying `product_id` — what values will the database automatically assign to `product_id` for the three rows?

A) Three randomly generated UUID strings
B) Three `NULL` values, since the field was not provided
C) The integers `1`, `2`, and `3` respectively
D) Three copies of the value `0`

**Answer:** C

**Explanation:** `SERIAL` is an **auto-incrementing integer** type. The database automatically assigns sequential values starting from 1 each time a new row is inserted. Since `student_id` is not provided in the INSERT, the database fills it with 1, 2, 3, and so on. `UUID` produces random strings — that is a different data type. `NULL` is prevented by `PRIMARY KEY`. `0` is never used with `SERIAL`.

---

### Question 3 *(Easy | MCQ — Single Correct)*

An AI travel assistant needs to answer questions like: *"Which of my past trips were most similar to a beach holiday in Goa?"* It must search through hundreds of stored trip summaries and return the ones closest in meaning — even if the exact words are completely different.

Which type of database is most appropriate for storing and querying these trip summaries?

A) Relational Database (SQL)
B) Time-Series Database
C) Vector Database
D) NoSQL Document Database

**Answer:** C

**Explanation:** **Vector databases** store embeddings (numerical representations of meaning) and can find content that is closest in meaning using semantic similarity. Two trip summaries can use entirely different words but still be mathematically close if they describe similar experiences. Relational databases use SQL which matches exact values, not meaning. Time-series databases handle timestamped sequential data. NoSQL handles flexible formats but cannot do meaning-based retrieval.

---

### Question 4 *(Easy | MCQ — Single Correct)*

A developer defines a column in a Supabase table as:

```sql
age INT CHECK (age > 0)
```

A data entry operator attempts to insert a new row with `age = -5`. What will the database do?

A) Insert the row and store `-5` as-is
B) Automatically convert the value to `0` before storing
C) Reject the row because the `CHECK` constraint is violated
D) Insert the row but store the `age` column as `NULL`

**Answer:** C

**Explanation:** The `CHECK` constraint validates every incoming value against the defined condition. Since `-5 > 0` is false, the `INSERT` statement fails entirely — the row is not added to the table. The database never silently changes or nullifies values; it simply rejects the operation, protecting data integrity.

---

### Question 5 *(Moderate | MCQ — Single Correct)*

A logistics company's AI fleet monitoring system records the GPS coordinates and speed of 2,000 delivery vehicles every 5 seconds, around the clock. The system must efficiently answer queries like: *"Show all vehicles that exceeded 80 km/h in the last 10 minutes."*

Which type of database is most suited for this use case?

A) Relational Database (SQL)
B) NoSQL Document Database
C) Vector Database
D) Time-Series Database

**Answer:** D

**Explanation:** **Time-series databases** are specifically optimised for data that is indexed by time and queried in time ranges. They handle extremely high-frequency timestamped data (one reading every 5 seconds from 2,000 vehicles = 24,000 writes/minute) far more efficiently than general-purpose databases. Relational databases could store this data but are not optimised for this volume and query pattern. NoSQL and Vector databases serve entirely different purposes.

---

### Question 6 *(Moderate | MCQ — Single Correct)*

Priya is designing a global AI-powered HR system that will run on independent servers in India, the US, and Germany. Employee records can be created on any regional server and must later be merged into a single central database. She needs a primary key strategy that guarantees no two records — created on different servers — will ever have the same ID.

Which data type should she use for the primary key?

A) `SERIAL`, because it auto-increments and is easy to manage
B) `INTEGER`, because databases can synchronise integer counters across servers
C) `VARCHAR(50)`, because adding a country prefix makes the ID unique
D) `UUID`, because it generates a globally unique identifier regardless of which server creates the record

**Answer:** D

**Explanation:** `UUID` (Universally Unique Identifier) generates a mathematically near-impossible-to-duplicate identifier independently on any server, making it the correct choice for multi-server architectures. `SERIAL` would produce ID = 1 on all three regional servers independently — causing collisions during the central merge. `INTEGER` has the same collision problem. Using `VARCHAR` with a custom country prefix is an error-prone manual workaround with no guarantee of uniqueness.

---

### Question 7 *(Moderate | MSQ — Multiple Correct)*

A developer is designing a `users` table for an AI chatbot platform. She wants to enforce data quality rules on the table's columns using SQL constraints.

Which of the following are valid SQL constraints that can be applied to columns in a `CREATE TABLE` statement? *(Select all that apply)*

A) `NOT NULL`
B) `UNIQUE`
C) `JOIN`
D) `DEFAULT`
E) `CHECK`
F) `FETCH`

**Answer:** A, B, D, E

**Explanation:**
- `NOT NULL` — Prevents a column from storing empty values. ✓
- `UNIQUE` — Ensures every value in the column is different across all rows. ✓
- `JOIN` — This is a **query clause** used to combine tables in a `SELECT` statement, not a table constraint. ✗
- `DEFAULT` — Automatically sets a value when none is provided during insert. ✓
- `CHECK` — Validates that inserted values satisfy a specified condition. ✓
- `FETCH` — This is a cursor navigation command, not a column constraint. ✗

---

### Question 8 *(Moderate | MSQ — Multiple Correct)*

A regional school chain transitions from storing all student data in Excel files to a PostgreSQL-based relational database (hosted on Supabase). Which of the following improvements will they directly experience as a result of this migration? *(Select all that apply)*

A) Multiple teachers across different branches can update student records simultaneously without overwriting each other's changes
B) The database will automatically generate attendance graphs and performance dashboards
C) A query to find "all students with fees pending for more than 30 days" can be executed instantly using SQL
D) Constraints like `age INT CHECK (age > 5)` will prevent invalid entries at the database level
E) The school will no longer need internet connectivity since databases function entirely offline

**Answer:** A, C, D

**Explanation:**
- A: Correct — databases handle concurrent access safely using transaction management. ✓
- B: Incorrect — databases store and query data; dashboards require separate BI tools like Tableau or Metabase. ✗
- C: Correct — SQL allows fast, indexed queries across large datasets that would require full file scans in Excel. ✓
- D: Correct — `CHECK` and `NOT NULL` constraints enforce data integrity directly at the database level. ✓
- E: Incorrect — Cloud-hosted databases (like Supabase) require internet; local installations need software setup. ✗

---

### Question 9 *(Hard | MSQ — Multiple Correct)*

A developer is designing an `event_registrations` table for a conference management platform. The table tracks which attendee registered for which event. One attendee can register for multiple different events, and each event can have many attendees.

Which of the following statements about this table design are correct? *(Select all that apply)*

A) `attendee_id` alone cannot serve as the primary key because the same attendee can appear in multiple rows (one per event)
B) A composite primary key of `(attendee_id, event_id)` ensures the same attendee cannot register for the same event twice
C) `event_id` alone can serve as the primary key because event IDs are unique across the events catalog
D) A composite primary key enforces both NOT NULL and UNIQUE behavior on the *combined values* of both columns together
E) Adding a separate `SERIAL` column as primary key is a structurally valid alternative, though it would not automatically prevent the same attendee from registering for the same event twice

**Answer:** A, B, D, E

**Explanation:**
- A: Correct — `attendee_id` repeats because one attendee registers for many events, so it cannot be a standalone primary key. ✓
- B: Correct — the composite key `(attendee_id, event_id)` means the exact same pair cannot appear twice, preventing duplicate registrations. ✓
- C: Incorrect — `event_id` also repeats because many different attendees register for the same event. ✗
- D: Correct — a composite primary key applies the combined NOT NULL + UNIQUE constraint to the pair of values as a unit. ✓
- E: Correct — a `SERIAL` ID column is structurally valid as a primary key, but it only guarantees uniqueness for that auto-generated ID. Preventing duplicate `(attendee_id, event_id)` pairs would require an additional `UNIQUE` constraint on that combination. ✓

---

### Question 10 *(Hard | MSQ — Multiple Correct)*

An AI customer support system uses RAG (Retrieval Augmented Generation) to answer user questions about a company's product policies. When a user asks *"What is the return policy for electronics purchased above ₹10,000?"*, the system follows a specific multi-step process to generate its response.

Which of the following statements correctly describe how this RAG system works? *(Select all that apply)*

A) The user's question is first converted into a numerical vector (embedding) before searching the policy knowledge base
B) The language model directly scans the policy documents by searching for matching keywords in the text
C) The vector database returns the policy document(s) whose embeddings are mathematically closest to the question's embedding
D) The retrieved policy content is provided to the language model as context before it generates its final answer
E) RAG reduces hallucinations because the model generates its answer grounded in retrieved factual content, rather than relying purely on its training
F) RAG works by retraining the language model every time a new policy document is added to the knowledge base

**Answer:** A, C, D, E

**Explanation:**
- A: Correct — the query is passed through an embedding model to produce a vector before the similarity search. ✓
- B: Incorrect — RAG uses semantic (embedding-based) similarity search, not keyword matching. ✗
- C: Correct — the vector database finds stored embeddings that are mathematically nearest to the query embedding. ✓
- D: Correct — the retrieved document text is injected into the model's prompt as context before response generation. ✓
- E: Correct — since the model generates from retrieved facts, it is less likely to fabricate information. ✓
- F: Incorrect — RAG does not retrain the model. The knowledge base (vector store) is updated independently, without touching the model. ✗
