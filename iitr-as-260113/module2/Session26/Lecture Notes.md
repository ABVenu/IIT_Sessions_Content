### **Introduction to Vector Databases**

#### **What problem are we trying to solve?**

Modern AI applications do not only work with exact words or exact database values. They often need to understand the meaning.

For example:

* A user searches: “How do I reset my password?”  
* But the document says: “Steps to recover your account access”

A traditional database may not match these well because the words are different.

An AI system needs a way to understand that both sentences are about a similar intent. This is where embeddings and vector databases become important.

#### **Recall the Role of Embeddings in AI Systems**

**What is an embedding?**  
An embedding is a numerical representation of data such as text, image, or audio, in the form of a list of numbers.

**Example:**

"reset password" → \[0.12, \-0.44, 0.91, ...\]

This list of numbers is called a vector.

The main idea is:

* data with similar meaning  
* gets converted into vectors that are close to each other

So embeddings help AI systems move from:

* matching exact words

to

* matching meaning

**Why does embedding matter ?**  
Embeddings are useful because they capture semantic similarity.

**Example:**

* “cheap flights to Delhi”  
* “affordable air tickets for Delhi”

These phrases use different words, but their meaning is very similar. Their embeddings are likely to be close in vector space.

**Where embeddings are used ?**

Embeddings are commonly used in:

* semantic search  
* recommendation systems  
* question answering systems  
* chatbots  
* retrieval-augmented generation (RAG)  
* agent memory systems  
* fraud detection

![image1](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image1.png)

![image2](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image2.png)

#### **Why are Traditional Databases Limited for Vector Data ?**

Traditional relational databases like MySQL or PostgreSQL are excellent for structured data such as:

* employee\_id  
* order\_status  
* salary  
* date\_of\_joining

They are designed for operations like:

* exact lookup  
* filtering  
* sorting  
* joins  
* aggregation

**Example of traditional database strength**

You can easily ask:

| SELECT \* FROM employeesWHERE department \= 'Engineering'ORDER BY salary DESC; |
| :---- |

This works well because:

* values are structured  
* matching is exact  
* SQL operations are optimized for tabular data

But vector data is different.

An embedding may look like:

**`[0.82, -0.11, 0.54, 0.09, ... hundreds of dimensions ...]`**

Now imagine storing millions of such vectors and asking:

“Find the top 5 vectors most similar to this query vector”

Traditional databases were not originally designed for this kind of search.

### **What Is a Vector Database?**

A vector database is a database designed to store, manage, index, and search embeddings efficiently.

It is specialized for queries like:

* “Find the most similar documents”  
* “Find products similar to this item”  
* “Find past conversations related to this query”  
* “Retrieve memory relevant to the current user request”

**Simple definition**  
A vector database stores data as vectors and retrieves results based on similarity, not just exact matches.

**Core role of a vector database:**

A vector database helps AI systems:

* store embeddings  
* search similar vectors quickly  
* scale to large collections  
* support semantic retrieval

In many real-world systems, a vector database also stores:

* the vector itself  
* original text or metadata  
* document id  
* tags / category  
* source information

So it is not just storing numbers; it is storing vectors with useful context.

![image3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image3.png)

### **The relationship between vector databases and embeddings**

The vector database serves as a repository for the embeddings, enabling efficient storage and retrieval. However, its significance extends beyond storage. Vector databases play a crucial role in supporting various data-driven applications by providing a platform for leveraging embeddings. Applications utilize these embeddings stored in the vector database for tasks such as similarity search, recommendation, clustering, etc.

Assume the application is **`“Find Similar Images.”`** So, how will it find similar images? The process generally follows the following steps:

* **Generate embeddings:** Images are fed into an image embedding model, which converts them into high-dimensional numerical vectors, capturing various features and characteristics of the images. Each image is represented by a unique embedding vector.

* **Store embeddings:** These embedding vectors are stored in a vector database, which efficiently indexes and organizes them for quick retrieval.

* **Query processing:** When a user submits a query image, it undergoes the same embedding process to generate a query embedding vector.

* **Similarity search:** The vector database performs a similarity search by comparing the query embedding vector with the stored embedding vectors of all images. Various similarity metrics like Euclidean distance or cosine similarity can be used for this comparison.

* **Return results:** Images with embedding vectors most similar to the query embedding are retrieved from the database and returned to the user as similar images.

![image4](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image4.png)

***When a query is made, the same embedding model is used to create an embedding for the query. The vector database then searches for embeddings that are similar to the query embedding and sends the query’s matching results back to the client application.***

### **Similarity-Based Retrieval**

Instead of finding data that exactly matches the query, we find data that is semantically close to the query.

**Traditional retrieval vs similarity retrieval**

**Traditional retrieval asks:**

Does the text contain the exact keyword?

**Similarity retrieval asks:**

Which stored items are closest in meaning to the query?

**Query:**  
“How can I change my login password?”

**Stored documents:**

* “Password reset steps for registered users”  
* “How to update shipping address”  
* “Track your order status”

A similarity-based system should retrieve document 1, even though the wording is not identical.

That is the power of vector databases.

#### **Intuition for Similarity Search**

Students often understand this better through analogies.

**Analogy 1: Finding similar movies**  
Suppose you liked a movie that is:

* emotional  
* slow-paced  
* character-driven

A recommendation system does not only look for the same title.  
It tries to find movies with a similar pattern or feel.

That is similarity search.

**Analogy 2: Shopping recommendations**  
You view a running shoe.

The system may recommend:

* other lightweight sports shoes  
* shoes of similar style and use case

It does not require exact product names to match.

**Analogy 3: Finding similar notes in a notebook**  
Imagine all your notes are organized not alphabetically, but by meaning.  
When you write a new question, the system tries to find notes that “feel closest” in meaning.

That is how vector retrieval works.

**Analogy 4: Human memory**  
If someone says:  
“I need help booking a trip”

You may remember:

* flight booking sites  
* hotel options  
* previous travel discussions

Your brain does not search exact words only. It recalls related concepts. Vector databases try to do something similar computationally.

### **Understanding Similarity Measurement**

Each piece of content becomes a point in a multi-dimensional space.

* similar meaning → points are close  
* different meaning → points are far apart

**Example:** Suppose these queries are stored:

* “buy a laptop”  
* “purchase a notebook computer”  
* “book a doctor appointment”

The first two should be closer to each other than to the third one.

What similarity means here:

The system measures how `“close”` two vectors are.

* closer vectors \= more similar meaning  
* farther vectors \= less similar meaning

This closeness can be measured using methods like:

* cosine similarity

	![image5](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image5.png)

* Euclidean distance  
    
  ![image6](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session26/session26-image6.png)

Vector databases use mathematical methods to measure closeness between vectors and return the nearest ones.

### **Why is Scalable Search Needed ?**

**Small dataset case**  
If you have only 20 vectors, you can compare the query vector with all 20 and pick the closest.

That is manageable.

**Large dataset case**

Now imagine:

* 1 million product descriptions  
* 20 million documents  
* 100 million user interactions

Comparing the query vector against every vector one by one is expensive.

This is called brute-force search.

**Why is brute-force approach inefficient ?** 

Because for every query:

* the system calculates similarity with all stored vectors  
* this takes more time as data grows  
* latency becomes high  
* cost increases

For AI applications like chatbots, recommendation engines, and search systems, users expect very fast responses.

So we need smarter ways to search.

### **What Is Vector Indexing?**

A vector index is a data structure that helps the system search similar vectors faster.

Instead of checking every vector one by one, the index organizes vectors in a way that lets the system quickly narrow down the search area.

**Simple idea:** Think of an index like a shortcut mechanism.

**Without an index:**

search every item

**With an index:**

go to likely relevant regions first

**Traditional analogy**

In a book:

without an index, you read every page  
with an index, you jump near the topic quickly

Similarly, vector indexing helps the database avoid a full scan over all vectors.

**Vector indexing improves:**

* speed  
* scalability  
* query performance

This is critical in production systems.

### **Why Traditional Indexes Are Not Enough?**

Traditional database indexes such as:

* B-trees  
* hash indexes

works well for:

* exact match  
* sorted values  
* range queries

But vector search deals with:

* multi-dimensional numerical space  
* closeness, not equality  
* semantic retrieval

That is why vector databases use specialized indexing methods designed for similarity search.

Vector indexing is a special optimization layer built for fast nearest-neighbor retrieval in high-dimensional data.

### **What Is the Approximate Nearest Neighbor (ANN) Search?**

First, what is the nearest neighbor?

When a query vector comes in, the system wants to find the stored vectors that are closest to it.

**These closest vectors are called nearest neighbors.**

**Exact nearest neighbor search**

Exact search tries to find the absolutely best and most accurate nearest vectors.

But exact search can be expensive at large scale.

**Approximate nearest neighbor search**

**ANN** search finds vectors that are very close to the best answer, but much faster.

So the system accepts a small trade-off:

* slightly less perfect accuracy  
* much better speed and scalability

**Why is ANN useful ?**   
In real-world AI applications, returning a result in:

50 milliseconds

is often more useful than returning a mathematically perfect answer in:

5 seconds

**This is why ANN is widely used.**

**Analogy:**  Imagine you are looking for the nearest coffee shop in a huge city.

Exact method: check distance to every coffee shop  
ANN method: search nearby neighborhoods first and quickly choose one that is almost certainly among the best options

It may not always be the absolutely closest one, but it is usually close enough and much faster.

**Note:**   
ANN does not mean random guessing.  
It means using smart search structures to get near-optimal results efficiently.

### **How Similarity Search Works Step by Step**

This is one of the most important sections for students.

**Step 1: Convert data into embeddings**

Suppose we have documents:

* “How to reset password”  
* “Refund policy for orders”  
* “How to change email address”

Each document is converted into a vector using an embedding model.

**Step 2: Store embeddings in the vector database**

The system stores:

* vector  
* original text  
* metadata

**Example metadata:**

* document\_id  
* category  
* source  
* timestamp


**Step 3: Build an index**

The database creates a vector index so search can be fast.

**Step 4: User sends a query**

Example query:  
“I forgot my password, how can I log in again?”

**Step 5: Convert query into embedding**  
The query is also converted into a vector using the same embedding model.

**Step 6: Search for nearest vectors**  
The vector database compares the query vector against indexed vectors and retrieves the closest ones.

**Step 7: Return top matches**  
The system returns the most similar documents.

Likely result:  
“How to reset password”

**Step 8: Use in downstream AI system**  
These retrieved results may then be:

* shown to the user directly  
* used by a chatbot  
* provided as context to an LLM  
* used as memory for an agent

### **Exact Match vs Similarity Search**

| Aspect | Exact Match Search | Similarity Search |
| ----- | ----- | ----- |
| Goal | Find exact text/value match | Find semantically similar content |
| Works well for | IDs, status, names, filters | meaning-based retrieval |
| Query style | keyword / exact field match | embedding-based search |
| Example | find user\_id \= 101 | find documents similar to “reset account access” |
| Strength | precision for structured data | understanding intent and meaning |
| Weakness | misses synonyms/context | may return approximate rather than exact matches |

Query:  
“ways to recover account”

Traditional exact keyword search may fail if the document uses:

“password reset”  
“restore login access”

Similarity search can still retrieve these because it understands semantic closeness.

### **Vector Databases in AI Applications**

**Semantic Search**  
Instead of searching by exact keywords, the system retrieves content by meaning.

Example:  
A student asks:  
“How do I prepare for coding interviews?”

The system can retrieve:

* DSA preparation guide  
* interview roadmap  
* coding rounds strategy

even if the exact phrase does not appear.

**Question Answering Systems**  
A question is embedded, relevant documents are retrieved, and then an LLM answers using that context.

Example:  
A support bot answers questions from company documentation.

**Recommendation Systems**  
Products, movies, music, or articles can be recommended based on semantic similarity.

Example:  
If a user likes articles about:

* distributed systems  
* microservices  
* scalability

the system can recommend semantically related content.

**Conversational AI**  
A chatbot can retrieve relevant previous conversations, FAQs, or knowledge base documents.

**RAG Systems**  
In Retrieval-Augmented Generation:

* user query is embedded  
* relevant chunks are retrieved from vector database  
* retrieved text is passed to LLM  
* LLM generates grounded answer

This is one of the most common uses today.

### **Vector Databases in Agentic Systems**

An agentic system is an AI system that can:

* reason  
* plan  
* use tools  
* remember context  
* take actions

For such systems, memory and retrieval are critical.

How vector databases help agents ?

**Context retrieval**  
An agent may need relevant knowledge from past documents or conversations.

Example:  
A travel-planning agent receives:  
“Book a flight similar to my previous business trip preferences.”

The agent can retrieve:

* preferred airlines  
* budget range  
* past hotel choices  
* previous trip summaries

**Memory access**  
Agents often store important past interactions as embeddings.

When a new task comes, the agent retrieves memories that are semantically similar.

**Earlier memory:**

“User prefers vegetarian food and window seat”

**Later query:**

“Plan my trip for next month”

The agent can retrieve this memory even though the new query does not use the exact same words.

**Personalized assistance**  
Agents can use vector databases to maintain long-term user preferences.

**Task continuity**  
If an agent worked on a problem earlier, it can retrieve similar task history and continue intelligently.

For agentic systems, vector databases are often used as:

* semantic memory  
* contextual knowledge layer  
* retrieval system for relevant past information
