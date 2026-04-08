# Introduction to Databases for AI Systems

## 1. Data is not optional in AI

Modern systems such as ChatGPT, Claude, or Gemini are useful only because they sit on top of **large, curated bodies of data** and continuous new input. The instructor’s point was blunt: **without data, there is nothing to learn from and nothing meaningful to return** when a user asks a question.

Two phases matter everywhere in the pipeline:

**Training** is the phase where a model absorbs examples (text, labels, structured records—depending on the system) and builds the internal patterns that later drive behavior. If the underlying storage is messy, duplicated, or wrong, those patterns inherit the same defects.

**Inference** is what happens when you send a **query** to an already trained model and receive a **response**. Even though we do not retrain in that moment, inference still relies on **data**: at minimum the prompt, and often retrieved context, user history, or feature vectors pulled from storage. So training and inference are not independent stories; both need trustworthy, reachable information.

For anyone building or operating AI products, this means **data management is part of the product**, not a separate afterthought.

![Training and inference both depend on stored, reachable data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session23/session23-ai-training-inference-data.png)

---

## 2. Why “throwing data on disk” fails: organization, speed, and trust

It is tempting to imagine that storage is solved as soon as bytes are written somewhere. That breaks down for real systems.

**Reliability** (in the sense used in class) is linked to whether the system can **dependably locate and use** the right information when needed. If nothing is organized, you may “know” the data exists but still fail to retrieve it on time—or retrieve the wrong copy.

The **house / wardrobe analogy** is useful: if tools, documents, and clothes are randomly scattered, finding a screwdriver takes forever. If each class of item has a place, you walk straight to it. **Organization improves both reliability and latency.**

**Scale** sharpens the problem. Consumer-facing AI services accumulate enormous volumes; new interaction and media are added constantly. At that size, ad hoc file sprawl does not just slow queries—it makes **governance** (who may see what) and **maintenance** (schema changes, cleanup) realistically unmanageable.

When storage is poor, typical symptoms include **missing values**, **uncontrolled duplication**, **slow searches**, **security weaknesses**, and **inconsistent answers** depending on which copy of a “fact” a component reads.

![Ad hoc files vs a structured database as system of record](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session23/session23-files-vs-database.png)

### Duplicate identities and enforced rules

Consider student sign-ups recorded by appending rows to a plain text file. The file format itself does not stop two users from registering the same **email address**. A relational database, by contrast, can declare that email must be **unique** and **non-null** (when business rules require it). Those are **constraints**—something files do not give you for free.

### Inconsistency when one fact lives in many places

If the same user profile is replicated in many systems or files, and you change—for example—the email from _X_ to _Y_, you must update **every** copy. If you miss one, some teams still see _X_ and others _Y_. That situation is **inconsistency**: the world no longer agrees on a single truth for one entity. Good design tries to store each fact in **one authoritative place** and refer to it elsewhere through **keys**, which limits this class of error.

### Relationships are part of correctness (example: users and chats)

**Users** and **chat transcripts** are related: each conversation belongs to an account. You should see **only your** threads, not everyone’s. Achieving that requires not only access control but a clear **data model** that ties conversations to user identifiers. Dumping all chats into an unscoped blob fails both privacy and query patterns.

---

## 3. A deeper look at “consistency” (beyond the buzzword)

Class discussion touched on themes that often confuse beginners: **backups and replicas** are not the same problem as **duplicate inconsistent business records**.

Financial systems illustrate **strong consistency** expectations: two withdrawal channels should not both believe a full balance is still available and together pay out more than exists. The system **coordinates** concurrent access so balance updates are ordered sensibly.

By contrast, some global products allow a profile photo change to **propagate slowly** across services; you may see a notice that updates can take **24–48 hours**. That is a deliberate trade-off: not every attribute needs instant global agreement if the product can tolerate temporary mismatch between surfaces.

**CAP** (Consistency, Availability, Partition tolerance) was named as the classic summary of tensions in distributed systems. You do not need to master the theorem for day-one AI engineering, but you should remember that **real systems choose trade-offs**; “always consistent everywhere instantly” is not free.

**Disaster recovery**: cloud operators store **many copies** across machines, data centers, and **regions** so one destroyed site does not wipe customer data. That is engineered redundancy with process behind it—not the same as ten people maintaining ten different Excel versions of “the customer list.” How long **old** data (e.g. photos) is kept depends on **policy** and product.

---

## 4. What we mean by “database”

Etymology helped in lecture: just as an **air base** is where aircraft are kept and operated, a **database** is a **base for data**—a place intended for storing and working with information systematically.

More formally, a **database** is an organized collection whose access is usually managed by software called a **Database Management System (DBMS)**. The DBMS handles persistence, concurrent access, security hooks, and efficient retrieval so applications do not reinvent those problems from scratch.

---

## 5. CRUD — the four verbs of data work

Almost all day-to-day operations are variations of:

|                | Meaning                | Typical example                                           |
| -------------- | ---------------------- | --------------------------------------------------------- |
| **C** — Create | Insert a new row       | New account registration                                  |
| **R** — Read   | Retrieve data          | Dashboard load, search                                    |
| **U** — Update | Change existing values | Problem-solving percentage after submitting an assignment |
| **D** — Delete | Remove a row           | Account closure                                           |

“Analyze” or “export” still decompose into **reads** and sometimes **writes** of derived results.

![The four CRUD operations on data held in a database](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session23/session23-crud-operations.png)

---

## 6. File-based storage versus databases

Humans stored data in **files** (text, PDF, **CSV**, Excel) long before databases were ubiquitous. CSV means **comma-separated values**: a row per record, fields separated by commas. Files remain excellent for **small extracts**, **human sharing**, and **one-off analytics**. They are a weak **system of record** for large concurrent applications.

### Limitations at scale

**Scalability.** Searching one specific fact inside a gigantic static document can be impractical. AI-scale corpora magnify this: you need structures and indexes, not only bytes.

**Enforcement.** Files do not automatically enforce **unique emails**, **foreign key** validity, or typed columns. Databases can, when you declare rules.

**Retrieval.** Without schema and indexes, answering precise questions over many large files devolves into repeated full scans.

**Concurrency.** _Concurrent_ means many operations overlapping in time—two payments, two editors, two services. The lecture used a **bank balance** story: if **ATM** and **UPI** both read the balance before either deducts, both might authorize spends that together exceed funds unless something **serializes** or **locks** critical steps. General-purpose files do not give you the transaction semantics databases are built around (for example, **locks** held briefly so one update completes before another reads stale state).

Databases therefore aim to improve **scale**, **consistency mechanisms**, **query power** (SQL in the next lecture), and **safe concurrency** for contested data.

**Caveat:** full **distributed systems design** is its own deep subject. As an AI engineer you may not implement locking internals—but you should recognize **why** Excel alone is rarely the backbone of a high-traffic production stack.

---

## 7. Relational versus non-relational (the high-level split)

At the broadest taxonomy, people separate:

- **Relational databases** — data organized in **tables** (relations); relationships expressed with **keys**; queried heavily with **SQL**. Examples from class: **MySQL**, **PostgreSQL**, **SQLite**, **Microsoft SQL Server (MSSQL)**.
- **Non-relational databases** — everything else purposely grouped under one umbrella: **document** stores, **key-value** systems, **wide-column** designs, **graph** databases, products such as **MongoDB** or **DynamoDB**, and more.

Non-relational is not one thing; it is **many** paradigms. Relational is comparatively uniform in concept: **if it is not relational, it falls into the non-relational bucket** for this coarse classification.

The memorable one-liner from class: **relational databases store relations, and relations are tables.** Each table normally represents one **entity type** (users, courses, videos, questions, …) rather than mixing unrelated realities in one wide grab bag.

![Example tables with primary keys, foreign keys, and a junction table for enrollments](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session23/session23-relational-pk-fk-junction.png)

---

## 8. Reading a table: rows, columns, entities

- A **row** is one **record** (one student, one course offering, one scheduled class).
- A **column** is an **attribute** (name, email, duration, title).
- A **table** groups records of the same kind.

### Modeling rule: one entity, one table

**Students** and **batches** (or **courses**) are different concepts with different fields. A batch has batch id, start date, track, and so on—fields that do not belong pasted onto every student row as if they were personal attributes. **Different entity ⇒ separate table.** That keeps columns meaningful and avoids redundant, wide rows that are hard to maintain.

### Naming columns

Two **different** tables may both use a column named `id` or `instructor_id`—the table name provides context. Within a **single** table, column names must remain distinct.

---

## 9. Primary keys

**Definition.** A **primary key (PK)** is a column or minimal set of columns that **uniquely identifies** each row in that table, and that must not be **NULL**.

**Uniqueness** is obvious in intent: if two users shared primary key values, you could no longer point to exactly one person.

**Why not NULL?** A null primary key would mean “this row has no stable identity,” which defeats the purpose of referencing it elsewhere.

### Natural keys versus surrogate keys

**Email** or **phone** might be unique in a closed system and could theoretically serve as PK **if** they are always **present** and **immutable** enough for your architecture.

Real tensions:

- If email is PK but some legitimate account lacks email (NULL), the row violates PK rules.
- If email is PK and is **referenced** across placements, instructors, billing, and tooling, and the human **changes** email, you must cascade updates everywhere or break references. Some products forbid email changes; others allow them for UX—making email a weak PK.

**Common professional pattern:** add a **surrogate key** — an internal **`user_id`** (often integer **auto-increment**) generated by the database. The user may never see it. Public attributes can change; internal id stays fixed. Other tables reference **`user_id`**, not the email string.

There is **one primary key** per table (possibly **composite**, i.e. multiple columns together). Auto-increment is a convenience, not a theoretical requirement.

---

## 10. Foreign keys

**Definition.** A **foreign key (FK)** is a column in a **child** table that stores values matching the **primary key** of a **parent** table. “Foreign” signals that the value’s **meaning** is defined in another table—it encodes a **relationship**.

**Referential integrity** (when enabled) means you cannot insert a foreign key value that does not exist as a primary key in the parent, avoiding **dangling** references.

### Repetition is allowed on the child side

Many **class** rows may list the **same** `instructor_id` if the same person teaches many sessions. The FK value **repeats** in the child table. It must **not** repeat as a PK in the parent table—each instructor has exactly one PK row.

---

## 11. Cardinality — deciding 1:1, 1:N, M:N

Cardinality describes **how many** rows on one side match **how many** on the other. Class gave a repeatable way to think:

1. Pick two entity types and label them left and right.
2. Ask: for **one** row on the left, how many matching rows can exist on the right—**one** or **many**? (“Many” here means more than one in the informal sense used in lecture.)
3. Ask the same **in the reverse direction**.
4. **Both one** ⇒ **one-to-one (1:1)**.  
   **One versus many** ⇒ **one-to-many** from the “many” side’s perspective—or **many-to-one** if you reverse the wording.  
   **Both many** ⇒ **many-to-many (M:N)**.

Worked examples:

- **Student** and **course enrollment:** one student, many courses; one course, many students ⇒ **M:N**.
- **Citizen** and **Aadhaar** (idealized): one citizen, one Aadhaar card; one Aadhaar, one citizen ⇒ **1:1**.
- **Scheduled class** and **instructor:** one class session has one instructor; one instructor teaches many sessions ⇒ **many-to-one** from class to instructor (equivalently **one-to-many** from instructor to classes).

![Cardinality patterns: one-to-one, one-to-many, and many-to-many with a junction](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session23/session23-cardinality-1-1-1-n-m-n.png)

---

## 12. Implementing relationships in relational schemas

### Many-to-one and one-to-many

**Rule:** place the **primary key of the “one” side** as a **foreign key** on the **“many” side**.

Example: **classes** are **many**; each has **one** **instructor**. Store **`instructor_id`** on **`classes`**. To learn the instructor’s name, **join** (next lecture) to the **instructors** table using that FK.

**Why not** store a list of class ids inside the instructor row? Relational modeling traditionally avoids stuffing **lists** into a single cell for arbitrarily growing collections; an instructor with thousands of classes creates an unmaintainable blob. Modern engines sometimes offer array types, but the **clear pattern** remains: use rows, not comma-packed strings, for repeating associations.

### One-to-one

Either table may hold the other’s PK as FK: **citizen** row stores **aadhaar_id**, or **aadhaar** row stores **citizen_id**. Choose based on privacy, query paths, and institutional rules.

Merging two 1:1 tables into one **wide** table is usually **not** the first choice: the entities have different lifecycles, regulation, and width. At very large scale (hundreds of millions of rows per side), a single merged table can become harder to evolve than two focused ones.

### Many-to-many

Neither entity table should absorb arbitrary-length lists of the other. Introduce a **junction** (or **mapping**) table—e.g. **`student_courses`**—whose rows are pairs of foreign keys (`student_id`, `course_id`). Each enrollment is one row; the same student appears on many rows; the same course appears on many rows.

---

## 13. What comes next in the course

The next session is set to add **SQL**—how you **create** schema, **insert** and **update** rows, **select** and **filter**, and **join** tables—plus a clearer contrast between **structured** data (rows and columns, natural fit for relational models) and **unstructured** data (text, audio, images), often stored with structured **metadata** nearby.

Together, this lecture (why databases and how tables relate) and the next (how to query them) form the foundation for talking later about **which database style** suits which AI application pattern.

---

## Key terms (for revision)

**Training · Inference · DBMS · CRUD · CSV · Scalability · Concurrency · Lock · Relational / non-relational · Table · Row · Column · Entity · Primary key · Foreign key · Referential integrity · Surrogate key · Cardinality (1:1, 1:N, M:N) · Junction table**
