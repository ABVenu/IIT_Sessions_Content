Q1: Vector databases are mainly designed for:

A. Exact primary key lookups
B. Similarity-based retrieval
C. Only financial transactions
D. Replacing all relational databases

Answer: B

Q2: Which of the following are good examples of similarity search? (Multiple Correct)

A. Finding employee with ID = 101
B. Finding images visually similar to a given photo
C. Finding documents similar in meaning to a user query
D. Finding rows with salary > 50000

Answer: B, C

Q3: Why are traditional databases not ideal for large-scale vector search?

A. They cannot store numbers
B. They do not support tables
C. They only work with text
D. They are not optimized for high-dimensional similarity search

Answer: D

Q4: If two texts have similar meanings, their embeddings are usually:

A. Completely random
B. Very far from each other
C. Close to each other in vector space
D. Stored in different databases

Answer: C

Q5: What does "semantic search" mean?

A. Searching by file size
B. Searching by exact spelling only
C. Searching by table name
D. Searching based on meaning

Answer: D

Q6: Which of the following queries are best handled by a vector database? (Multiple Correct)

A. Find user with user_id = 5
B. Find songs that sound similar to a given audio clip
C. Find articles similar to "how to scale microservices"
D. Find all orders in March

Answer: B, C

Q7: ANN search is useful because: (Multiple Correct)

A. It requires no indexing at all
B. It is usually much faster than exact exhaustive search
C. It scales well to large high-dimensional datasets
D. It always returns worse results than exact search

Answer: B, C

Q8: Which of the following best describes similarity measurement conceptually?

A. Checking if two vectors have the same length
B. Matching vectors by document ID
C. Sorting vectors alphabetically
D. Measuring how close two vectors are in meaning

Answer: D

---

Q9: A company is building a **customer support chatbot** for its website. Users ask the **same question in different ways**, such as:

- *"How can I get my money back?"*
- *"I want a refund for my order"*
- *"How do I return a purchased item?"*

Explain why a **vector database** would be useful in this system instead of relying only on a **traditional database** or **exact keyword search**.

> 📝 **Submission Instruction:** Type your answer in the answer box below the question.

**Explanation:**

A **vector database** would be useful in this customer support chatbot because users often ask the same question in **different ways**. **Traditional databases** or **keyword search** depend heavily on exact words, so they may fail when the user's wording is different from the stored FAQ content.

For example, a support document may contain the term **"refund policy"**, but a user may ask *"How can I get my money back?"* Even though both mean the same thing, **keyword-based search** may not match them properly.

A **vector database** solves this problem by storing **embeddings** — numerical representations of **text meaning**. The support documents are converted into **embeddings** and stored in the vector database. When a user asks a question, that query is also converted into an **embedding**. The vector database then retrieves the documents whose embeddings are **closest** to the query embedding.

This allows the chatbot to return results based on **semantic similarity** rather than exact word matching. As a result, the chatbot becomes more **accurate**, more **flexible**, and more useful in real-life customer support scenarios.
