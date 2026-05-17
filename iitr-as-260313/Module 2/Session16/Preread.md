# Pre-read: Embeddings and Semantic Representation

Imagine you work on support for a popular online learning platform. A student messages: *"I forgot my login password — how do I get back in?"*

Your help centre already has an article titled **"Steps to reset your account password."** But the search box only looks for the **exact words** the student typed. It hunts for "forgot" and "login" — and returns nothing useful. The student waits. The chatbot guesses — and might make something up.

A smarter platform surfaces the right article instantly — even though the student's words and the article's title barely overlap. That difference is about understanding **meaning**, not just **matching words**.

---

## Two Walls Every AI Builder Hits

You have started storing data in **related tables** — users in one, orders in another, linked by IDs. Two challenges still feel manual:

> **Wall 1 — Structured data:** *"Which customer placed which order, and from which city?"*  
> Matching IDs across two reports by hand is slow and error-prone at scale.

> **Wall 2 — Unstructured text:** *"Find policy text that answers what this user is really asking."*  
> Normal search is **Ctrl+F** at scale. If the user says "refund my money" and the policy says "payment reversal," keyword search often misses it — even though a human would not.

Today's session fixes **both**: how to **stitch related tables** in one database query, and how **embeddings** turn text into numbers so a computer can say *"these two sentences mean almost the same thing."*

---

## From Registers to a Meaning Map

Picture two office registers.

- **Register A** — every order: product, amount, **customer ID**.  
- **Register B** — every customer: ID, name, city, email.

When the manager asks for *"all Mumbai orders with the buyer's name,"* you match each order's ID to the right customer row — you do not retype names on every slip. A database **JOIN** does that in one step.

Now picture a **room of balloons** — one per FAQ line or PDF paragraph. Balloons about **passwords** cluster together; balloons about **food delivery** sit in another corner; **weather** stays far away. A new question floats in; the system finds the **nearest** balloons — those are the best matches. That room is **vector space**; each position is an **embedding** — numbers that capture *what the text is about*.

---

## In this pre-read, you'll discover:

- How **INNER JOIN** links `users` and `orders` to answer *"who bought what?"* — and why the **parent** row must exist before the **child**
- How **insert, update, and delete** work on linked tables — including **cascade** when a user is removed
- Why **keyword search** fails for real AI cases — and how **semantic search** finds content when words differ
- What **vectors** and **embeddings** are, how **tokenization** turns text into numbers, and the **semantic search workflow** behind chatbots and **RAG**

---

## Ideas Worth Knowing Before We Go Live

**INNER JOIN** — Merges two tables where a shared ID matches on **both** sides, so each order row shows the buyer's name and city in one result.

**Foreign key & referential integrity** — Every order must point to a real user. Invalid IDs are **rejected** — so AI systems do not store broken links.

**ON DELETE CASCADE** — Deleting a user can auto-delete their orders when child rows only make sense with the parent. Sometimes deletion is **blocked** instead — for audit records you must keep.

**Vector** — An ordered list of numbers marking a position on an abstract map (like GPS, but with hundreds of dimensions).

**Embedding** — A vector from text where **similar meaning → nearby position** — same logic as a music app matching a hummed tune to the closest stored song.

**Tokenization** — Text split into **tokens** the model reads as numbers. Longer text costs more tokens; long PDFs are often **chunked** before embedding.

**Same model for docs and queries** — Indexing and searching must use the **same embedding model**, or similarity scores become meaningless.

**SQL vs semantic search** — Partners, not rivals. *"Pending Mumbai orders over ₹1,000"* → **SQL**. *"Refund policy for cancelled flights?"* → **semantic** retrieval, then optionally an LLM drafts an answer from those passages (**RAG**).

---

## Questions We Will Answer in the Live Session

1. **The JOIN puzzle:** Ananya has two orders; Rohan has one. Starting from `orders`, how many JOIN rows appear — and what happens to a user with **no** orders?

2. **The delete dilemma:** You delete a user who still has five orders. With **CASCADE** vs **RESTRICT**, what happens — and when would you choose each?

3. **The search showdown:** A student searches *"unable to sign in"*; the FAQ says *"account recovery."* Would `LIKE '%sign in%'` find it? How would **embeddings** treat the two phrases — and why must documents and queries use the **same** embedding model?

---

## After This Session, You Will Be Able To

- Write an **INNER JOIN** on two tables and explain it before you type the query  
- Run **CRUD** on linked tables without breaking **referential integrity**  
- Explain **embeddings** and **semantic similarity** in everyday language  
- Choose **keyword/SQL** vs **semantic search** for the right kind of question  
- Describe how **RAG**, recommendations, and **agent memory** retrieve context by **meaning**  
- See why **vector databases** — coming next — matter when you have millions of chunks

See you in class. The step from *"who bought what in SQL"* to *"what does this user actually mean?"* is one of the most important on your path to trustworthy AI systems.
