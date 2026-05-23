# Assignment — Objective (Session 16)

**Instructions:** Answer all questions. For multiple-select questions, choose every option that correctly completes the statement.

---

## Section A — Multiple choice (single correct)

### Q1 (Easy)

A startup’s `customers` table has **4** rows and `orders` has **6** rows. You run a **cross join** with **no** matching condition. How many rows appear in the result?

- A) 10
- B) 24
- C) 4
- D) 6

---

### Q2 (Easy)

In a query you write `FROM customers AS c JOIN orders AS o`. What is the main purpose of **`c`** and **`o`** here?

- A) They permanently rename the tables in the database schema
- B) They are short **table aliases** for this query only, so columns can be written as `c.customer_id`
- C) They encrypt customer data before joining
- D) They are required only for `CROSS JOIN`, not for conditional joins

---

### Q3 (Easy)

A user searches a help portal for **“remote work policy”**. The best article title is **“Work from home rules”** and shares almost no words with the query. Which approach is designed for this situation?

- A) Keyword-only match on exact words in stored text
- B) Semantic search using embeddings
- C) `CROSS JOIN` without an `ON` condition
- D) Sorting FAQ rows with `ORDER BY` only

---

### Q4 (Easy)

In class, an **embedding** was described as:

- A) A SQL foreign key between two tables
- B) A sequence of numbers (a vector) representing the meaning of text
- C) A chunking strategy that splits PDFs every 500 characters
- D) A synonym dictionary maintained by hand

---

### Q5 (Moderate)

`customers` has `customer_id` **1, 2, 3**. `orders` has two rows linked to customers **1** and **2** only. Customer **3** has no orders. You run:

```sql
SELECT c.full_name, o.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```

How many rows should appear (only matching pairs are kept)?

- A) 3
- B) 2
- C) 6
- D) 0

---

### Q6 (Moderate)

FAQ **chunks** were embedded with **Model A**. Live user questions are embedded with **Model B** (different API, different vector length). What is the main risk?

- A) Similarity between query and stored chunks becomes unreliable because they are not in the same vector space
- B) PostgreSQL automatically converts Model B vectors to Model A
- C) Chunking is no longer required
- D) Keyword search and semantic search become identical

---

## Section B — Multiple choice (multiple correct)

### Q7 (Moderate) — Select all that apply

Which steps match the **semantic search workflow** described in class for a FAQ bot?

- A) Collect and clean source content (help pages, PDFs, etc.)
- B) Split long documents into **chunks** before embedding
- C) Embed the user query with the **same embedding model** used for stored chunks
- D) Retrain a full embedding model from scratch on every single user click
- E) Compare vectors and return the **closest** matches to the query

---

### Q8 (Moderate) — Select all that apply

Which statements about **chunking strategies** match what was taught?

- A) Fixed-size chunking (e.g. every N characters) was described as often **poor** because it can break meaning mid-thought
- B) Paragraph-based chunking can suit content where each paragraph is one complete idea
- C) Keeping related sub-points in the **same** chunk helps retrieval quality
- D) Recursive chunking can help nested documents (sections inside sections)

---

### Q9 (Hard) — Select all that apply

Which statements about **vectors**, **semantic similarity**, and **cosine similarity** match the session (concept level—no formula required)?

- A) Similar meanings tend to produce embeddings whose numbers are **closer** when compared
- B) **Cosine similarity** is used to find which stored vector is closest to the query vector
- C) Every developer must hand-code the full cosine formula before semantic search can work
- D) Mixing different embedding models for stored chunks vs live queries makes comparison unreliable

---

### Q10 (Hard) — Select all that apply

A support system must handle: (i) **“What is order_id 7’s status?”** and (ii) **“I want my payment back”** when policies use wording like **“refund eligibility.”** Which statements are **true**?

- A) Question (i) fits **structured SQL** on known columns and exact values
- B) Question (ii) fits **semantic retrieval** over embedded policy chunks
- C) The system can **retrieve** relevant chunks by similarity, then let an LLM answer using that text (RAG-style flow discussed in class)
- D) Semantic search should **replace** SQL for all inventory and status lookups

---

## Answer key (for facilitators / LMS “Answer Explanation”)

### Q1

- **Correct:** B
- **Why:** Cross join = Cartesian product: **4 × 6 = 24** rows (taught with customers × orders demo).
- **Why others are wrong:** A adds sizes; C/D are single-table counts.

### Q2

- **Correct:** B
- **Why:** **`c`** and **`o`** are **table aliases** for readability and qualified columns (`c.customer_id`), not schema renames.
- **Why others are wrong:** A is wrong (aliases are query-scoped). C/D are unrelated.

### Q3

- **Correct:** B
- **Why:** Class used **remote work** vs **work from home** to show keyword failure and **semantic** match by meaning.
- **Why others are wrong:** A is exact-word only. C/D do not search FAQ meaning.

### Q4

- **Correct:** B
- **Why:** Live teaching: embedding = **sequence of numbers** representing meaning; vector = that list.
- **Why others are wrong:** A is SQL design. C is preprocessing. D is the weak alternative the class argued against.

### Q5

- **Correct:** B
- **Why:** Join on `customer_id` keeps only real pairs—**two** orders → **two** rows; customer **3** excluded (demo: customer 5 with no orders).
- **Why others are wrong:** A includes customer without orders. C suggests cross join size. D means no matches.

### Q6

- **Correct:** A
- **Why:** Class stressed **same embedding model** for stored data and user query so comparisons are valid.
- **Why others are wrong:** B/C/D are false fixes or misconceptions.

### Q7

- **Correct:** A, B, C, E
- **Why:** Matches live workflow: collect/clean → chunk → embed with same model → compare → top matches (Swiggy/Zomato-style FAQ example).
- **Why D is wrong:** You **call** an embedding API/model; you do not retrain per click.

### Q8

- **Correct:** A, B, C, D
- **Why:** All four strategies were named; fixed-size called **useless** in class; paragraph, semantic, and recursive chunking discussed with nested/legal examples.
- **Why none are wrong:** Each option reflects taught content.

### Q9

- **Correct:** A, B, D
- **Why:** Class: closer numbers ≈ similar meaning; **cosine similarity** finds closest vectors; maths done by library later (“call one function”); same-model rule repeated.
- **Why C is wrong:** Instructor said not to worry about full maths now—production uses built-in functions / vector DB.

### Q10

- **Correct:** A, B, C
- **Why:** SQL for exact structured facts; semantic search for paraphrased policy intent; class described retrieve-then-answer flow (RAG preview) for password/refund-style Q&A.
- **Why D is wrong:** Class said production uses **both** SQL and semantic search, not one replacing the other.

---

## QC note

Per process requirements, a separate file `assignment question QC report.md` records per-question QC and aggregate ratings.
