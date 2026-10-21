# Databases, Embeddings, and Retrieval-Augmented Generation

You already know that a model only continues text, and that memory has to live somewhere real. This session is about those stores. A table answers an exact question.

A vector store answers a meaning question.

An agent should fetch a fact instead of inventing one. Structured facts live in tables and are fetched with SQL. Unstructured text is split, turned into vectors, and fetched by meaning.

Retrieval-augmented generation places the fetched text into the prompt so the model answers from that text. The useful skill is to say which stage failed when the answer is wrong.

## 1. Two stores, two questions

| Question | Store | Lookup |
|---|---|---|
| What is the status of order 1842? | Relational table | Exact key, filters, joins |
| What is our written policy on damaged items? | Vector store of document chunks | Similarity to the question |

A language model is a poor database. It has a knowledge cutoff, it was not trained on your private handbook, and it will complete a plausible sentence when the fact is missing. Retrieval is how you hand it the fact at answer time.

![Two stores — relational table for exact order status lookup versus vector store for policy meaning search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/final-course-revision/session03/revision03-01-two-stores.png)

CSV and spreadsheet files are fine for a small, single-user extract. They become the wrong system when many people, or an agent, read and write the same records at once.

They do not enforce “this id may appear only once”, and they do not give you a query language with predictable structure. A database does.

## 2. Relational databases

A relational database stores data in tables. A table is rows and columns. A row is one record.

A column is one attribute. The schema is the definition of those columns: names, types, and rules.

Typical types: `INTEGER`, `FLOAT`, `VARCHAR` for bounded text, `TEXT` for long text, `BOOLEAN`, `DATE`, `TIMESTAMP`, and `UUID` when you need an identifier that stays unique at large scale.

### 2.1 Keys and constraints

A **primary key** identifies one row. It is unique and not null. A **foreign key** stores the primary key of a row in another table, which is how “this order belongs to that customer” stays a real link rather than a copied name.

Constraints you should be able to name:

| Constraint | What it refuses |
|---|---|
| `NOT NULL` | A missing value in that column |
| `UNIQUE` | A second row with the same value |
| `PRIMARY KEY` | A missing or duplicate identifier |
| `DEFAULT` | Nothing, if you omit the column; it fills a known value |
| `CHECK` | A value outside a rule, such as a negative price |

Without these, the application discovers bad data at the worst moment: two customers with the same id, or an order whose customer id points at nobody.

### 2.2 Relationships and normalisation

- **One-to-one:** one person, one government id record.
- **One-to-many:** one customer, many orders. The “many” table holds the foreign key.
- **Many-to-many:** students and courses. A junction table holds pairs of keys, because neither side can store a single foreign key without repeating or dropping data.

![Keys and joins — primary and foreign keys, one-to-many and junction table, danger of UPDATE or DELETE without WHERE](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/final-course-revision/session03/revision03-02-keys-joins.png)

Normalisation splits a wide, repetitive table into smaller tables so each fact is stored once. Repeating a teacher’s phone number on every class row means one correction must be edited in many places, and some copies will be missed. A teachers table plus a foreign key removes that repetition.

Normalise far enough that a fact has one home. Do not split so far that every simple screen needs a dozen joins you cannot explain. The practical test is: if this fact changes, how many rows must change?

### 2.3 Why an agent meets a database

An agent reads profiles, orders, and preferences, and sometimes writes a new memory or a ticket. Reads dominate in question-answering. Writes are the dangerous ones, because a bad statement changes the record for everyone.

Later notes treat “only read unless a person approves the write” as a safety rule. The database concept underneath it is simply that `SELECT` and `DELETE` are different powers.

**Edge cases**

- A foreign key with no matching parent is an integrity failure. Joins will drop or null that row depending on the join type.
- A default value can hide a bug: every omitted city becomes `"unknown"` and your report looks complete.
- Names are poor primary keys. Two people can share one, and a person can change it.

**Recall:** schema, primary key, foreign key, junction table, normalisation.

## 3. SQL that you can reason about

SQL is the language for these tables. Keyword case does not matter. Text literals use quotes.

Whether `'Asha'` matches `'asha'` depends on the database collation. Do not assume a match. Store and search categories in one chosen case.

### 3.1 The core statements

| Statement | Job | Edge |
|---|---|---|
| `CREATE TABLE` | Define columns and constraints | A later insert that breaks a constraint is rejected |
| `INSERT` | Add rows | A duplicate primary key is rejected |
| `SELECT` | Read columns | `SELECT *` pulls columns you may not have meant to show a user |
| `UPDATE` | Change rows | Without `WHERE`, it changes every row |
| `DELETE` | Remove rows | Without `WHERE`, it empties the table |

`UPDATE` and `DELETE` without a `WHERE` clause are the catastrophic edge cases. Read the statement twice and prefer a `SELECT` with the same `WHERE` first, so you can see which rows match.

### 3.2 Filtering, matching, sorting, paging

`WHERE` keeps rows. Combine tests with `AND`, `OR`, and `NOT`. `AND` binds more tightly than `OR`, so use parentheses when a condition mixes them.

The same precedence surprise you saw in Python appears here.

Useful predicates:

- Comparisons: `=`, `<>` or `!=`, `>`, `<`.
- `IN ( ... )` for a fixed set of allowed values.
- `BETWEEN` for an inclusive range.
- `LIKE 'J%'` where `%` means any run of characters and `_` means one character.

`ORDER BY column ASC` or `DESC` sorts the rows that survived the filter. Sorting is not a filter. `LIMIT 5` returns at most five rows.

`OFFSET 10` skips ten rows first. `LIMIT` plus `OFFSET` is pagination. Offset pagination gets slower and can skip or repeat rows if the underlying data changes between pages.

It is still the right concept for “page 3 of a report”.

A table alias (`customers AS c`) shortens a name inside one query. It does not rename the table in the database.

### 3.3 Joins

A join builds a wider row from two tables using a matching key.

| Join | Rows you get |
|---|---|
| Inner join | Only pairs that match |
| Left join | Every left row, with nulls on the right when nothing matches |
| Cross join | Every combination, the Cartesian product, rows-on-the-left times rows-on-the-right |

The Cartesian product is what you get when you list two tables and forget the match condition. It looks like a successful query and the numbers are nonsense. Always state the `ON` condition.

An inner join silently drops a customer who has no orders, or an order whose customer id is unknown. A left join keeps that customer and shows null order columns. Choosing the join is choosing which absence you are willing to see.

Nulls do not equal null. A filter `WHERE phone = NULL` does not find missing phones. The test for absence is `IS NULL`.

### 3.4 How to read a query

The engine does not run clauses in the order you type them.

The usual order is `FROM` and `JOIN`, then `WHERE`, then `GROUP BY`, then `HAVING`, then `SELECT`, then `ORDER BY`, then `LIMIT` and `OFFSET`.

![SQL clause execution order — FROM and JOIN through WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT and OFFSET](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/final-course-revision/session03/revision03-04-sql-clause-order.png)

`WHERE` drops rows before any total exists. `HAVING` drops groups after `COUNT`, `SUM`, or `AVG` has been computed. Using `WHERE` to drop “small groups” answers a different question.

`COUNT(*)` counts rows. `COUNT` of a column skips nulls in that column.

### 3.5 Patterns an agent actually uses

- **Lookup:** one row by primary key. Fast and exact.
- **Conditional retrieval:** many rows by status, date, or owner.
- **Batch:** a set of ids, not one query per id in a loop, when the set is known.
- **Write:** an insert of a new ticket or memory, with the constraints left in place so a bad write fails loudly.

Latency matters because the user is waiting on a model call plus this query. Selecting every column of every historical row “just in case” makes both the database and the later prompt slower. Fetch the columns the next step needs.

**Edge cases**

- `LIKE '%smith'` cannot use a simple left-anchored index strategy the way `LIKE 'smith%'` can. Leading wildcards are more expensive.
- An alias used in `WHERE` under another name is a typo that fails the query, not a second table.
- `SELECT *` in an agent prompt pastes internal columns, including notes never meant for the user.
- A successful query can still be the wrong query. “Zero rows” might mean the filter was too strict, the join dropped the parent, or the data is genuinely absent. Those three causes need different fixes.

**Recall:** `WHERE` versus a missing `WHERE` on writes, `IS NULL`, inner versus left versus cross join, `LIMIT`/`OFFSET`, fetch only what the next step needs.

## 4. Embeddings

Keyword search finds the words you typed. It misses “send it back” when the document says “returns window”. An embedding is a list of numbers that stands for the meaning of a piece of text.

Similar meanings land near each other. Unrelated meanings land far apart.

The intuition is geometric. “Paris” is to “France” in something like the way “Rome” is to “Italy”: the relationship is a direction in the space. You do not need the training math to use the consequence.

You need to know that the space is only as good as the model that built it, and that two sentences about the same topic in very different words can still be neighbours.

Text is split into chunks first. Each chunk is passed through an embedding model. The same model must embed the user’s question later.

Mixing two embedding models in one store puts vectors in incompatible spaces. Nearness then means nothing.

### 4.1 Similarity

Cosine similarity uses the angle between two vectors. For text, it is the usual choice because it cares about direction (the meaning) more than about the length of the vector. Euclidean distance measures straight-line distance and is more sensitive to magnitude.

A smaller angle means a closer meaning when the score is cosine similarity.

A score is not a proof. A high score means “closest among what you stored”, not “this passage answers the question”. If the store does not contain the answer, the nearest chunk is still returned, and it is the wrong chunk.

### 4.2 Exact search and approximate search

Brute-force search compares the query with every stored vector. It is accurate and it gets slow as the collection grows, because the work scales with the number of vectors.

Approximate nearest neighbour search organises vectors into a structure (clusters or a graph) so the lookup can jump toward the right neighbourhood. It is much faster at large scale and can miss a slightly better neighbour. That miss is a real edge case: the right policy paragraph exists and the approximate index did not surface it.

Raising the candidate pool, or rebuilding the index, is the systems response. Blaming the language model is the wrong response.

**Recall:** same embedding model for documents and queries, cosine for text, nearest is not the same as relevant, approximate search can miss.

## 5. Chunking

A chunk is the piece you embed and the piece you might hand to the model. The whole document as one chunk is too coarse: the vector averages the entire policy manual, and a question about returns retrieves a blur. A chunk of a few words is too fine: the vector has no subject, and the model receives a fragment with no condition attached.

### 5.1 Strategies

| Strategy | How it cuts | Watch for |
|---|---|---|
| Fixed size | Every N characters or tokens | Splits mid-sentence and mid-rule |
| Paragraph | On natural breaks | A huge paragraph becomes a huge chunk |
| Recursive | Tries large separators, then smaller ones | Still needs a size cap |
| Semantic | Groups sentences whose embeddings are close | Slower to build, often cleaner neighbours |

Overlap repeats a slice of the previous chunk at the start of the next, often on the order of ten to fifteen percent, or a small fixed number of characters. Overlap exists so a rule that crosses the cut still appears whole in at least one chunk. Too much overlap stores the same sentence many times and can fill the top results with duplicates.

Too little overlap loses the sentence that contained the exception.

### 5.2 Size is a retrieval decision

Too small: the answer’s condition and its exception land in different chunks, and you retrieve only one. Too large: several topics share a vector, so a question retrieves a passage that is half relevant and half noise. The model then has more chance to quote the wrong half.

There is no universal character count. A short FAQ can use small chunks. A contract with long definitions needs larger chunks or semantic grouping.

Change size only with a before-and-after check on questions you already know the answers to.

### 5.3 Metadata

Each chunk should carry source, page or section, a stable id, and a category when you have one. Metadata does three jobs:

- **Traceability:** the answer can cite the document.
- **Filtering:** a returns question can search only the returns category.
- **Deletion:** when a policy is retired, you can remove its chunks.

Category tags must be normalised. `"Returns"` and `"returns"` are different filters and you will “lose” half the manual. Decide the lowercase form when you ingest, not when you debug a demo.

**Edge cases**

- Overlap creates duplicate passages. A top-k of five can be three copies of one paragraph plus two useful chunks. Deduplicate by source position if you see this.
- Headers that are not repeated inside the chunk leave a chunk that says “14 days” without saying 14 days of what. Include the heading in the chunk.
- Tables and multi-column pages split badly under naive character cuts. A row separated from its column titles is a false fact waiting to be quoted.

**Recall:** too small versus too large, overlap, metadata for filter and citation, normalise tags.

## 6. The vector store

A vector database stores embeddings, the original chunk text, and the metadata, and it answers “which items are nearest to this query vector?”

Three jobs:

1. **Storage** of the vector, the text, and the metadata.
2. **Indexing** so the nearest-neighbour lookup does not scan blindly.
3. **Retrieval** of the top k neighbours.

A collection is the named container, analogous to a table. An upsert inserts or replaces by id. Re-ingesting a document under the same ids updates it.

Ingesting it under new ids duplicates it, and retrieval starts returning two generations of the policy.

Useful operations to recognise, without treating them as a build exercise:

| Operation | Meaning |
|---|---|
| Create or open a collection | The container you will query |
| Upsert | Insert or replace chunks |
| Count | How many chunks are stored |
| Peek or get | Inspect a known id |
| Query | Similarity search returning top k and distances |

Distances need a consistent reading. Some libraries return “smaller means closer”. Do not assume a high number is a high similarity until you check that library’s definition.

A threshold copied from a blog and applied to the wrong direction will either accept everything or accept nothing.

Common systems you will hear named: Chroma for local and lab use, a managed service such as Pinecone, FAISS as a similarity library, and a Postgres extension when vectors live beside relational data. The concepts above are the same. The product changes the operational details.

**Edge cases**

- An empty collection returns nothing. The model, if still called, will answer from its own prior knowledge unless the prompt forbids that.
- A persistent client writes to a folder. A purely in-memory client forgets the index when the process stops. Same surprise as in-memory chat history.
- Updating the source PDF and not the index leaves stale embeddings. The store does not watch the file for you.

**Recall:** collection, upsert versus duplicate insert, top k, distance direction, persistent versus in-memory.

## 7. Retrieval-augmented generation

RAG is three moves:

1. **Retrieve** the chunks whose embeddings are nearest to the question, optionally after a metadata filter.
2. **Augment** the prompt by placing those chunks in a clearly marked context block.
3. **Generate** an answer conditioned on that block.

![RAG pipeline — offline ingest chunk and embed; online retrieve, augment prompt, generate; name retrieval versus generation failure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/final-course-revision/session03/revision03-03-rag-pipeline.png)

Think of an open-book test. The model is the person answering. The retriever is the librarian.

The chunks are the pages that were actually handed over. Pages that stayed on the shelf do not exist for this answer.

### 7.1 Offline path and online path

**Offline, or ingestion.** Collect the sources (files, pages, exports). Clean them. Chunk. Embed with the chosen model. Upsert into the collection. Repeat on a schedule when the source changes. Prices, policies, and stock levels go stale if this path never runs again.

**Online, or the question.** Embed the user question with the same model. Retrieve top k. Build a prompt that contains the instruction, the context, and the question. Generate. Optionally check that the answer stays inside the context. Reply, with a citation when you have metadata.

Keep the two paths separate in your head. Ingestion can be slow. The question path has to be fast.

Doing chunking and embedding of a whole corpus on every user message is a design error.

### 7.2 Grounding

Grounding means the claims in the answer are supported by the retrieved text. The system instruction should say that the context is the only source, that missing information becomes a refusal or a clarifying question, and that the model must not fill gaps from general knowledge.

Delimiters keep the model from treating the document as a new set of instructions. A clear pattern is a context block, then a question block. If a retrieved page says “ignore previous rules”, those words arrived as data.

The instruction should say that text inside the context is evidence, not a command. That is the retrieval form of prompt injection.

### 7.3 Top k

A small k is fast and can miss the second paragraph that held the exception. A large k raises the chance the answer is somewhere in the pile, and it also raises cost, latency, and the chance the model attends to a distractor. Start from the smallest k that answers your known questions, then raise it when you see misses that are present just outside the cut.

Metadata filtering narrows the pile before similarity runs. A shipping question searched only inside shipping chunks is more precise. It fails when the true answer spans two categories and you allowed only one.

Multi-category questions need a wider filter or no filter plus a better ranker.

### 7.4 Two failures that need two fixes

| Symptom | Diagnosis | Useful response |
|---|---|---|
| The right fact is not in the retrieved chunks | Retrieval failure | Chunking, overlap, metadata, k, the embedding, or the index |
| The right fact is in the chunks and the answer ignores or contradicts it | Generation failure | Instruction, delimiters, temperature, or the model |

Always look at the retrieved text before you blame the model. Most bad RAG answers are retrieval failures. Changing the model does not insert a paragraph that was never retrieved.

Other misses:

- The fact was never ingested.
- The fact was ingested and then superseded, and both versions are still in the index.
- The right chunk was retrieved and then truncated because the prompt ran out of window.

### 7.5 Improvements, and what they cost

| Technique | Effect | Cost |
|---|---|---|
| Stricter instruction and an explicit refusal | Fewer invented policies | More “I don’t know” on borderline questions |
| Metadata filter | Cleaner neighbours | Misses cross-category answers if the filter is narrow |
| Larger k | Higher chance the fact is present | More noise and tokens |
| Query expansion | Several phrasings of a vague question, better recall | Extra model call |
| Re-ranking | A second model reorders a wide candidate list | Latency, usually better precision than stuffing every candidate into the prompt |
| Compression | A smaller model shortens the chunks before the answer | Can delete the one sentence that mattered |
| Semantic cache | A repeated or near-repeated question skips the pipeline | Must expire, or it serves a stale policy |

Re-ranking is preferred when you need both a wide net and a short final context. Compression is preferred when you are paying for a huge context and can tolerate some loss. They solve different problems.

A retrieval system does not reach a meaningful “always correct”. Sources change, questions are ambiguous, and approximate search has a miss rate. Plan for a person or a refusal on the residue, and plan to delete stale chunks.

**Edge cases**

- Two chunks disagree because ingestion ran twice. The model may quote either, or blend them. Ids and deletion of the old document are the fix.
- A refusal rule that is too strong says “I don’t know” even when the chunk contains the answer in different words. That is a generation failure caused by the instruction, or a retrieval score so weak the instruction dominated.
- Citations that name a document the model did not receive are themselves hallucinations. Cite only ids that were in the context.
- Personal data inside a knowledge base will be quoted if it is retrieved. Do not ingest it, or filter it out, before you celebrate grounding.

**Recall:** ingest offline, answer online, delimit context from the question, retrieval failure versus generation failure, k and filters as trade-offs.

## 8. A full pass on one question

Use this as a spoken drill.

A user asks, “Can I return headphones after 20 days?”

1. The orders table can say whether this user bought headphones and when. That is SQL, exact, and per person.
2. The policy collection can say whether the written window is 14 or 30 days. That is embeddings, and it is not personal.
3. Retrieval should surface the returns chunk, not the warranty chunk. Category metadata makes that likely.
4. The prompt contains the chunk and the purchase date, and the instruction says to apply the written window.
5. If the chunk is missing, the correct behaviour is to refuse, not to invent “most stores allow 30 days”.
6. If the chunk says 14 days and the answer says 30, the generation ignored the context. Look at temperature, the instruction, and whether a second chunk contradicted the first.

The agent did two different kinds of lookup. Collapsing both into “just ask the model” loses the order date and the policy. Collapsing both into one vector store loses exact filters on a customer id.

## 9. SQL patterns, spoken as results

Walk each pattern by naming the rows that remain.

**One customer’s open orders.** Filter orders by that customer id and by an open status. Sort by newest first. Limit to a page. If you forget the customer id, you have leaked every customer’s orders into the prompt. That is a correct SQL result and a serious product failure.

**Customers with and without orders.** An inner join lists only customers who have at least one order. A left join from customers lists everyone, and the order columns are null when there is no order. If a report of “customers we never sold to” uses an inner join, the report is empty for the wrong reason.

**A delete rehearsed as a select.** The rows you mean to delete are exactly the rows a `SELECT` with the same `WHERE` returns. Run that select, count them, then delete. “I meant one row” is not visible in a `DELETE` that already ran.

**A join that multiplies.** One order with two shipment rows, joined carelessly, appears twice. A later sum double-counts the order total. When a parent gains a second child, row counts jump. Check counts before and after a join when the next step is a total.

**Nulls in a filter.** “Phones that are missing” is `IS NULL`. “Phones that are blank” is an empty string. Some pipelines store one, some the other. A cleanup that looks for only one of them will report the column as complete.

**Case and pattern.** `LIKE` follows that same collation. Normalise case on the way in, or compare a lowercased expression, and use the same rule for vector category tags.

## 10. Chunk and retrieve drills

**Drill 1 — the exception on the boundary.** A rule says “14 days, except for headphones, which are 7”. A fixed cut lands between the two clauses. One chunk says 14 days. The other says headphones are 7, with no subject. Retrieval returns the 14-day chunk. Overlap or a heading repeated inside each chunk keeps the exception attached to the rule. This is a chunking bug even though the model “answered from the context”.

**Drill 2 — the duplicate generation.** The same policy is upserted under new ids after an edit. Top k returns the old 30-day window and the new 14-day window. The model blends them into “about two to four weeks”. Fix the ids, delete the retired source, and re-query. Do not add a sentence to the prompt asking the model to “use the latest” unless the chunks carry a date it can compare.

**Drill 3 — the confident neighbour.** The store has no headphone policy. The nearest chunk is about returning cables. The score is the best available and still wrong. A minimum similarity, plus the instruction to refuse when the context does not contain the product type, stops the cable policy from being applied to headphones. A threshold copied from another embedding model is meaningless. Set it by inspecting scores on questions you know.

**Drill 4 — the filter that was too clever.** Returns questions are filtered to the returns category. The user asks whether a return resets the warranty. The answer lives in two categories. A single-category filter retrieves half. Either detect multi-topic questions and widen the filter, or retrieve more widely and let a re-ranker demote the noise.

**Drill 5 — the window ate the context.** You retrieved eight chunks and also sent the full chat history. The context window kept the history and cut the chunks. The model answered from memory of the conversation. Reduce history, reduce k, or summarise before you retrieve. Then check the trace to see what the model actually received.

## 11. Ingestion hygiene

Ingestion is a data pipeline with a few states you should be able to name.

| State | What is true | What users experience |
|---|---|---|
| Never ingested | The fact exists only in a file on someone’s laptop | A fluent invention, or a refusal if you were strict |
| Ingested and current | Ids match the source version | Citations line up with the file |
| Stale | The file changed, the vectors did not | A grounded answer to the old policy |
| Duplicated | Old and new ids both present | Mixed numbers in one answer |
| Wrong space | A second embedding model wrote into the same collection | Similarities that look random |

Clean text before you embed it. Headers, footers, and page numbers repeated on every page become the most “similar” text in the store, because they appear everywhere. A question then retrieves the footer.

Strip boilerplate once, in ingestion, not in the prompt.

Schedulers exist because some facts move. A returns policy can be refreshed nightly. A stock level probably should not live in a vector store at all.

Put fast-changing exact facts in a table and keep the prose in the vector store.

**Edge cases**

- A failed ingestion halfway through leaves a collection with half the chapters. Count chunks per source after a run.
- Two writers upserting the same id at once can lose one update. Ingestion jobs should be one-at-a-time per document.
- Embedding a secret into the store makes retrieval a leak channel. Treat the collection as production data.

## 12. How to judge retrieval quality

You can judge a retriever before you judge a paragraph. For a handful of questions, write down the source you expect. Run retrieval.

Mark a hit if that source appears in the top k. A miss with the right source absent is a retrieval defect. A hit followed by a wrong sentence is a generation defect.

Keep those marks in two columns. Improving the model when the hit column is empty does not move the outcome.

When you do change chunk size, overlap, k, or a filter, change one of them and repeat the same questions. Two changes at once produce a better or worse score you cannot explain.

A ceiling exists. Some questions are ambiguous, some sources contradict, and approximate indexes miss. The honest system refuses, asks, or escalates the residue.

A demo that is perfect on five rehearsed questions has not measured that residue.

## 13. Connecting the table and the vectors in one design

Use the table when the question names an id, a date, a status, or a count. Use the vector store when the question names a meaning and the answer is prose. Use both when a decision needs a personal fact and a written rule, as in the headphone example.

Do not embed a row per order into the vector store to avoid learning SQL. You will lose exactness and spend a similarity search on a problem that was a primary-key lookup.

Do not try to answer a policy question with `LIKE '%return%'` alone once the wording varies. Keywords remain useful as a metadata filter and a cheap first pass. They are a weak substitute for embeddings when the user and the document share no words.

## 14. Distinctions to keep straight

- A spreadsheet is a file. A database is a system that can enforce uniqueness, links between tables, and many readers at once.
- A primary key identifies one row and cannot be empty or repeated. A foreign key points at a primary key in another table.
- One-to-many puts the foreign key on the “many” side. Many-to-many needs a junction table.
- Normalisation stores a fact once. A phone number copied onto every order will be wrong on some of those orders after the next edit.
- `SELECT` reads. `INSERT` adds. `UPDATE` changes. `DELETE` removes. The last two, without `WHERE`, apply to every row.
- `AND` binds before `OR`. Parentheses are part of the meaning when those mix.
- `BETWEEN` is inclusive. A range you meant to be open will include the endpoints.
- `LIKE '%x'` and `LIKE 'x%'` are different searches. A leading wildcard is the more expensive one.
- `LIMIT` caps rows. `OFFSET` skips rows. Neither replaces a filter.
- An alias exists inside one query. It does not rename the table on disk.
- An inner join keeps matches only. A left join keeps every left row and uses nulls when the right side is missing. A cross join with no match condition multiplies the tables.
- `NULL` is not equal to `NULL`. Missing values are found with `IS NULL`. An empty string is a different value.
- `COUNT(*)` counts rows. `COUNT` of a column skips nulls in that column.
- Row filters happen before a total exists. A test on a total is a later step. Using the row filter to drop “small groups” answers a different question.
- The nearest vector is the closest stored text, not a proof that the text answers the question.
- Cosine similarity cares about angle. A high score in one library may be a distance in another. Read the direction before you set a cutoff.
- Brute-force search compares the query with every vector. Approximate search is faster and can miss a better neighbour.
- The embedding model for the documents and the embedding model for the question must be the same. Two models do not share a space.
- Chunks that are too small split a rule from its exception. Chunks that are too large mix topics into one vector.
- Overlap keeps a boundary sentence in more than one chunk. Too much overlap fills top k with duplicates.
- Metadata supports filter, citation, and deletion. Tags that differ only by case will not match.
- Upsert on the same id replaces. A new id on the same document duplicates. Duplicates become blended answers.
- Ingestion is offline and may be slow. Answering is online and must stay fast. Re-embedding the corpus on every question couples the two.
- Grounding means the answer’s claims appear in the retrieved text. A citation to a document that was not retrieved is another hallucination.
- If the right chunk is absent, fix retrieval. If the right chunk is present and ignored, fix the instruction, the delimiters, or the temperature.
- A metadata filter raises precision and can hide a cross-topic answer.
- A larger k raises the chance the fact is in the pile and also raises noise, cost, and the chance the window cuts the pile back off.
- Query expansion helps a vague wording and spends another model call. Re-ranking reorders a wide list. Compression shortens context and can delete the one useful sentence.
- A semantic cache must expire when the source changes. A cache hit on a retired policy is a fast wrong answer.
- An empty store plus a model that is still allowed to “be helpful” produces an ungrounded answer. The refusal rule has to cover the empty case.
- Exact personal facts belong in tables. Written rules belong in the vector store. A decision often needs one lookup of each.
- Boilerplate that repeats on every page becomes a strong, useless neighbour. Strip it before you embed.

## 15. A question, named in order

1. Decide whether the fact is a row, a passage, or both.
2. If it is a row, write the filter first and include the owner id. Rehearse a write with a select.
3. If it is a passage, embed the question with the same model used at ingestion.
4. Apply a metadata filter only when you are sure the answer lives in one category.
5. Take top k and read the chunks yourself before you judge the model.
6. Place the chunks inside delimiters, then the question, with an instruction that the chunks are evidence and not commands.
7. Require a refusal when the chunks do not contain the fact.
8. If the answer is wrong, label it retrieval or generation before you change anything.
9. If you change chunk size, overlap, k, or the filter, change one and repeat the same questions.
10. When the source file changes, replace ids or delete the old chunks before users ask again.

## 16. Terms to define in one sentence

- **Schema:** the column names, types, and rules for a table.
- **Primary key:** the unique, non-empty identifier of one row.
- **Foreign key:** a column that stores another table’s primary key.
- **Junction table:** the table of pairs that represents a many-to-many link.
- **Constraint:** a rule the database enforces, such as not null, unique, or a check.
- **Normalisation:** storing each fact in one place so a change cannot leave stale copies.
- **Inner join:** a combined row only where both tables match.
- **Left join:** every left row, with nulls where the right table has no match.
- **Cross join:** every combination of the two tables when no match is required.
- **`IS NULL`:** the test for a missing value, which equality does not catch.
- **Embedding:** a numeric vector that places similar meanings near each other.
- **Cosine similarity:** a comparison by angle, the usual match score for text vectors.
- **Approximate nearest neighbour:** a faster lookup that may miss a slightly closer vector.
- **Chunk:** the passage you embed and the passage you may hand to the model.
- **Overlap:** the repeated edge between chunks so a cut does not drop a sentence.
- **Metadata:** source, location, and category stored beside a chunk for filter and citation.
- **Upsert:** insert or replace by id, as opposed to blindly adding a second copy.
- **Top k:** the number of nearest chunks returned for one question.
- **Ingestion:** the offline path that cleans, chunks, embeds, and stores.
- **Grounding:** an answer whose claims are supported by the retrieved text.
- **Retrieval failure:** the right passage never reached the prompt.
- **Generation failure:** the right passage was in the prompt and the answer still went wrong.
- **Re-ranking:** a second pass that reorders a wide candidate list before the answer is written.
- **Semantic cache:** a stored answer reused for a near-duplicate question, with an expiry.

## 17. Say the failure before you name the fix

- Two customers share one id. The primary key was missing or not unique.
- An order names a customer who does not exist. The foreign key was not enforced.
- A phone number is correct on one order and stale on another. The number was copied instead of normalised into one row.
- Every row changed. `UPDATE` or `DELETE` had no `WHERE`.
- A customer with no orders vanished from a report. The join was inner when it needed to be left.
- The report has thousands of rows and no business meaning. The join condition was omitted and the query cross-joined.
- Missing phones were not found. The test used `=` against null.
- “Headphones” did not find the returns rule written as “send the item back”. Keyword match was used where meaning match was required.
- The nearest chunk is about cables. The headphone rule was never stored, and no refusal threshold was set.
- The 14-day rule and the 7-day exception disagree inside one answer. The cut split them, or both versions are still in the index.
- Top results are the same paragraph three times. Overlap is high and duplicates were not removed.
- A returns question retrieves a warranty page. The category tag was missing, mistyped, or mixed case.
- The model answers well in a test and wrongly after a policy edit. Ingestion did not replace the old chunks.
- The model ignores a paragraph you can see in the trace. That is generation: instruction, delimiters, or temperature. Changing the embedding will not help.
- The model never received the paragraph. That is retrieval: chunking, filter, k, model mismatch, or an approximate-index miss.
- A fast repeated answer stays wrong after the policy edit. The semantic cache has no expiry tied to the source version.
- A stock count comes from a vector search. That fact belonged in a table lookup by id.

Name the stage, then change one setting and repeat the same questions.

## 18. Which store is this?

- Status of order 18 is a table lookup by key.
- “How long is the returns window?” is a passage in the vector store.
- “Can this order still be returned?” needs the table and the passage together.
- A count of open orders is SQL, not a similarity search.
- A paraphrased policy question is embeddings, not `LIKE` alone.
- A price that changes every minute stays in a table or a live API. Do not wait for a nightly re-embed.
- A retired PDF is a delete from the collection, not a note in the prompt.

## 19. Self-check

1. What does a primary key guarantee, and what does a foreign key point at?
2. What does `UPDATE` without `WHERE` do?
3. Why does an inner join drop a parent row that has no children?
4. Why must the query and the documents use the same embedding model?
5. Why is the nearest chunk sometimes still the wrong chunk?
6. What problem does overlap solve, and what problem does too much overlap create?
7. What is the difference between the ingestion path and the question path?
8. How do you tell a retrieval failure from a generation failure?
9. What does a metadata filter improve, and what question shape does it risk missing?
10. Why is a cross join without an `ON` condition a successful disaster?

When these answers are fluent, the last revision session can treat retrieval as one tool among others, and focus on calling tools safely, shaping their output, and running the system as an operation.

## Try this yourself

Write two questions a shop assistant might receive: “What is the status of order 18?” and “What is our written window for damaged items?” Next to each question, write the store you would use and the failure you would check first if the answer is wrong. For the order, name the `WHERE` test that keeps other customers’ rows out. For the policy, say whether a wrong answer with the right paragraph in the prompt is a retrieval failure or a generation failure.

## Key Takeaways

- A primary key identifies one row. A foreign key points at one. `UPDATE` and `DELETE` without `WHERE` change every row.
- The usual clause order is `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`, `LIMIT`. Inner, left, and cross joins keep different absences.
- Similar text lands near each other only when the same embedding model is used for documents and questions. Nearest does not mean “answers the question”.
- Ingestion is the slow path that stores chunks. Answering retrieves top k into a delimited prompt. Fix retrieval and generation separately.
- The next notes treat retrieval as one tool among others, with safety, evaluation, and cost around it.

## Important Commands, Libraries, Terminologies used

| Term | Meaning |
|---|---|
| Primary key / foreign key | Unique row id / a pointer at another table’s id |
| `WHERE` / `HAVING` | Filter rows before totals / filter groups after totals |
| `IS NULL` | The test for a missing value |
| Inner / left / cross join | Matches only / all left rows / every combination |
| Embedding / cosine similarity | A meaning vector / closeness by angle |
| Chunk / overlap / metadata | The stored passage / the repeated edge / source and category |
| Upsert / top k | Replace by id / how many neighbours to return |
| Ingestion / grounding | Offline store path / claims supported by retrieved text |
| Retrieval failure / generation failure | Right passage never arrived / right passage was ignored |
