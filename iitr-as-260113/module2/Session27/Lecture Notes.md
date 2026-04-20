# Implementing Vector Search Systems

Welcome to this session on **Vector Search Systems**. In our previous sessions, you learned what **embeddings** are and how they capture the "meaning" of text as numbers. Now, we will take the next big step — we will actually build a working system that can **store these embeddings** and **find the most similar ones** when you ask a question.

Think of it like this — earlier, you learned how to write words in a diary. Today, you will learn how to build a smart library that can find the right diary page the moment you describe what you are looking for.

---

## Introduction to Vector Search Systems

Before we start coding, let us first understand **what we are building and why**.

* **Official Definition:** A **Vector Search System** is a software pipeline that stores data as numerical vectors (embeddings) and retrieves the most semantically similar items for a given query vector.
* **In Simple Words:** It is a "meaning-based search engine." Instead of matching exact words, it matches the **idea** behind the words.
* **Real-Life Example:** Imagine you go to a Kirana store and ask the shopkeeper, *"Bhaiya, kuch thanda de do."* You did not say "Pepsi" or "Limca," but the shopkeeper understood your **intent** and gave you a cold drink. A vector search system works in exactly the same way — it understands the **meaning**, not just the exact word.

**Why do we need this?**

* Traditional keyword search (like Ctrl+F) fails when users type different words for the same meaning. For example, searching "mobile" will not find documents that only say "cell phone."
* Vector search solves this by comparing **meaning** using math (vectors).
* Every modern AI application — ChatGPT plugins, Google Search, Netflix recommendations, WhatsApp stickers suggestion — uses some form of vector search behind the scenes.

**Common Doubt:** *"Isn't this same as Google Search?"*

* Google uses a mix of keyword search AND vector search. The "meaning-based" part of Google is powered by vector search. So yes, you are basically building a mini-Google today.

---

## Defining the Objective of Our Vector Search System

Now that we know *what* a vector search system is, let us clearly define **what we want to build** in this session. Without a clear goal, we will get lost in the code.

**Our Goal for Today:**

* Build a small system where a user can type a **question in plain English**.
* The system will search through a list of stored sentences/documents.
* It will return the **top 3 most similar sentences**, even if the exact words do not match.

**Why define the objective first?**

* **Clarity:** Every engineer's first rule is — "Pehle problem samjho, phir code likho." (First understand the problem, then write code).
* **Avoids Confusion:** If we do not define the goal, we will keep adding unnecessary features and never finish.
* **Measurable Success:** We can clearly test — "Did the system return the right sentence? Yes or No?"

**Real-Life Example:** Think of planning a wedding. If you do not first decide "400 guests, veg menu, outdoor venue," the caterer and decorator will give you random options and your budget will explode. Defining the objective is the same — it keeps the whole project in control.

---

## Understanding the End-to-End Implementation Workflow

Before writing code, let us see the **complete journey** of data in our system. This is called the **pipeline**. Knowing the pipeline helps us understand where each piece of code fits.

**The 5-Step Pipeline:**

1.  **Data** — The raw text (sentences, documents, FAQs) that we want to search through.
2.  **Embeddings** — Convert this text into number-vectors using an AI model.
3.  **Storage** — Save these vectors into a **Vector Database** (like Chroma).
4.  **Query** — When the user types a question, convert that question also into a vector.
5.  **Retrieval** — Compare the query vector with stored vectors and return the closest matches.

**In Simple Words:**

* **Data** = Ingredients in the kitchen.
* **Embeddings** = Cutting and preparing the ingredients in a standard way.
* **Storage** = Keeping them neatly in labelled containers in the fridge.
* **Query** = You feel hungry and say "I want something spicy."
* **Retrieval** = The fridge smartly gives you the containers that match "spicy."

**Common Mistake Students Make:**

* They try to start coding directly without understanding this flow. Then they get stuck because they do not know "where" the error is coming from.
* **Golden Rule:** Always mentally trace these 5 steps when debugging.

---

## Setting Up the Development Environment

A cook cannot cook without a kitchen. Similarly, we need to set up our "coding kitchen" first. We will use **Python** with a beginner-friendly vector database called **Chroma**.

**Key Tools We Will Install:**

* **Python 3.10 or above:** The programming language we will use. It is simple and has many AI libraries.
* **ChromaDB:** 
    * **Official Definition:** Chroma is an open-source, embedded vector database designed for building AI applications with embeddings.
    * **In Simple Words:** It is a special kind of "database" that is built only for storing vectors and finding similar ones quickly.
    * **Real-Life Example:** A normal MySQL database is like a general store. ChromaDB is like a specialized shop that sells only shoes — but it is extremely fast and smart at it.
* **Sentence-Transformers:** A Python library that gives us **free, offline** AI models to generate embeddings. No API key, no internet needed after download.

**Step-by-Step Installation:**

* Open your terminal (Command Prompt on Windows, Terminal on Mac).
* Create a new folder for today's project, for example `vector_search_demo`.
* Install the required libraries by running the command below.

```bash
pip install chromadb sentence-transformers
```

**How this command works:**

* `pip` is Python's **package manager** — it downloads and installs libraries.
* `install` tells pip that we want to **add** something new.
* `chromadb` and `sentence-transformers` are the two libraries we need.

**Common Doubt:** *"Sir, do I need a GPU or paid account?"*

* **No.** Everything we do today runs on a normal laptop. No GPU, no credit card, no OpenAI key needed.
* If the install is slow, it is just downloading the AI model (~100 MB) once. After that, it is instant.

---

## Preparing Sample Data for Implementation

Every database needs **data**. Let us create a small but realistic dataset. We will use short sentences so you can easily see how the search works.

**Why start small?**

* **Easy to Test:** With 5-10 sentences, you can manually check if the search result makes sense.
* **Fast to Run:** Large datasets take time to embed. We want quick feedback while learning.
* **Scales Later:** The same code that works on 10 sentences will work on 10 lakh sentences — just slower.

**Our Sample Dataset (an Indian FAQ-style dataset):**

```python
documents = [
    "How to apply for an Aadhaar card in India",
    "What is the procedure to get a PAN card",
    "Best places to visit in Manali during winter",
    "How to book a train ticket on IRCTC website",
    "Healthy Indian breakfast recipes for weight loss",
    "How to pay electricity bill online through UPI",
    "Top engineering colleges in India after JEE",
    "Recipe for homemade masala chai",
]
```

**How this data works:**

* `documents` is a Python **list** — an ordered collection of items.
* Each item is a **string** (text inside quotes).
* These sentences are about totally different topics — government, travel, food, education. This variety will help us clearly see that search is based on **meaning**, not random chance.

---

## Generating Embeddings Using Pretrained Models

Now comes the **magic step** — converting text into numbers that capture meaning. We will not train our own model (that takes weeks and crores of rupees). Instead, we will use a **pretrained model** that is already trained by researchers.

* **Official Definition:** An **embedding model** is a neural network that maps text into a fixed-size vector of real numbers such that semantically similar texts produce closer vectors.
* **In Simple Words:** It is a "text-to-numbers converter" where similar meanings get similar numbers.
* **Real-Life Example:** Think of a **pin code system**. Two houses in the same colony have very similar pin codes (e.g., 560001 and 560002). Two houses in different cities have very different pin codes. Embeddings work like a "meaning pin code."

**The Model We Will Use: `all-MiniLM-L6-v2`**

* It is small (only ~80 MB), fast, and works well for general English text.
* It converts any sentence into a **384-dimensional vector** (384 numbers).

**Full Code to Generate Embeddings:**

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "How to apply for an Aadhaar card in India",
    "What is the procedure to get a PAN card",
    "Best places to visit in Manali during winter",
    "How to book a train ticket on IRCTC website",
    "Healthy Indian breakfast recipes for weight loss",
    "How to pay electricity bill online through UPI",
    "Top engineering colleges in India after JEE",
    "Recipe for homemade masala chai",
]

embeddings = model.encode(documents)

print("Number of documents:", len(documents))
print("Shape of embeddings:", embeddings.shape)
print("First vector (first 5 numbers):", embeddings[0][:5])
```

**How the code works:**

* **Import:** We bring in the `SentenceTransformer` class from the library.
* **Load Model:** `SentenceTransformer("all-MiniLM-L6-v2")` downloads and loads the model. The first time it takes ~1 minute; after that, it is cached.
* **Encode:** `model.encode(documents)` takes our list of sentences and returns a 2D array of vectors — one vector per sentence.
* **Verify:** We print the shape to confirm we got `(8, 384)` meaning 8 sentences, each with 384 numbers.

**Common Doubt:** *"Why 384 numbers? Why not 10 or 1000?"*

* The model was **designed** by researchers to use 384 dimensions as a balance between accuracy and speed. Bigger models (like OpenAI's) use 1536 dimensions — more accurate but slower.

---

## Initializing a Vector Database Collection

We now have embeddings in memory. But memory is lost when the program stops. We need to **store** them properly so we can reuse them. This is where our vector database, **Chroma**, comes in.

* **Official Definition:** A **collection** in Chroma is a logical grouping of embeddings along with their documents and metadata — similar to a table in SQL.
* **In Simple Words:** A collection is like a **folder** or a **named box** where we keep related vectors together.
* **Real-Life Example:** In your mother's kitchen, one dabba is labelled "Masala," another is "Dal," another is "Atta." Each dabba is a "collection" that holds related items. ChromaDB collections work the same way.

**Full Code to Initialize the Client and Collection:**

```python
import chromadb

client = chromadb.PersistentClient(path="./my_vector_db")

collection = client.get_or_create_collection(name="indian_faq")

print("Collection created successfully:", collection.name)
```

**How the code works:**

* **Import chromadb:** Load the ChromaDB library.
* **PersistentClient:** This creates a database that **saves to disk** at the folder `./my_vector_db`. Even if you close your laptop, the data stays safe.
* **get_or_create_collection:** This is a smart command — if a collection named `indian_faq` already exists, it opens it; otherwise, it creates a new one. This avoids errors on re-runs.
* **Print:** Just confirms everything worked.

**Why `PersistentClient` and not `Client`?**

* A normal `Client` stores data only in RAM (memory). Once the program closes, data is gone.
* `PersistentClient` saves it to the hard disk — so your "learning" is not wasted every time.

---

## Storing Embeddings in the Vector Database

Now we will actually **insert** our data into the collection. Along with the vector, we will also store the original text and some **metadata** (extra info like category).

**Why store metadata?**

* **Filtering Later:** We might want to search only "food" category or only "travel" category. Metadata makes this possible.
* **Human Readability:** Vectors are just numbers. Storing the original text helps us read the results.
* **Unique IDs:** Every record needs a unique ID to update or delete it later.

**Full Code to Add Documents:**

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="indian_faq")

documents = [
    "How to apply for an Aadhaar card in India",
    "What is the procedure to get a PAN card",
    "Best places to visit in Manali during winter",
    "How to book a train ticket on IRCTC website",
    "Healthy Indian breakfast recipes for weight loss",
    "How to pay electricity bill online through UPI",
    "Top engineering colleges in India after JEE",
    "Recipe for homemade masala chai",
]

categories = [
    "government", "government", "travel", "travel",
    "food", "finance", "education", "food"
]

ids = [f"doc_{i}" for i in range(len(documents))]

embeddings = model.encode(documents).tolist()

collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=documents,
    metadatas=[{"category": c} for c in categories]
)

print("Total items stored:", collection.count())
```

**How the code works:**

* **Load model & client:** Same as before — we need both to work.
* **Prepare categories:** A matching list telling which category each sentence belongs to.
* **Generate IDs:** `doc_0`, `doc_1`, ... `doc_7` — each sentence gets a unique name.
* **`.tolist()`:** Chroma expects a plain Python list, not a NumPy array. This conversion prevents errors.
* **`collection.add()`:** The main insert command. We pass four parallel lists — ids, embeddings, documents, metadatas. All four lists **must be the same length**, otherwise Chroma throws an error.
* **`collection.count()`:** Tells us how many items are now in the collection.

**Common Mistake:**

* Students often forget `.tolist()` and get a confusing error. Always remember — Chroma wants lists, not NumPy arrays.

---

## Verifying Stored Data

Before moving to searching, we must **verify** that our data actually went in correctly. A good engineer always double-checks.

**Why verify?**

* **Silent Failures:** Sometimes code runs without error but stores nothing (for example, if IDs are duplicate).
* **Peace of Mind:** Seeing your data makes debugging 10x easier later.

**Full Code to Peek Inside the Collection:**

```python
import chromadb

client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="indian_faq")

print("Total items:", collection.count())

sample = collection.peek(limit=3)

print("First 3 IDs:", sample["ids"])
print("First 3 documents:", sample["documents"])
print("First 3 metadatas:", sample["metadatas"])
```

**How the code works:**

* **`collection.count()`:** Returns the total number of stored items. Should say `8` for our example.
* **`collection.peek(limit=3)`:** Gives us a preview of the first 3 records — like opening a box and taking a small look.
* **Print fields:** We print IDs, original text, and metadata to confirm data is stored correctly.

**Real-Life Example:** It is like checking your Amazon order after the delivery boy has left. You open the box to confirm the right item is inside, even if the packaging looked fine.

---

## Converting Query Input into Embedding

Now the user will type a question. But we cannot directly compare text with vectors. We must first convert the **user's question** into a vector using the **same model** we used for storage.

**Golden Rule:** *Always use the same embedding model for storing and for querying.* Using different models is like trying to fit a 5-pin plug into a 3-pin socket — it simply will not work.

**Full Code to Embed a Query:**

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

user_query = "How do I get a new PAN card?"

query_embedding = model.encode([user_query]).tolist()

print("Query embedding length:", len(query_embedding[0]))
```

**How the code works:**

* **Same Model:** We load the exact same model (`all-MiniLM-L6-v2`) used during storage.
* **`[user_query]`:** We wrap the query in a list because `encode` expects a list of strings.
* **`.tolist()`:** Convert to plain list for Chroma compatibility.
* **Print length:** Should print `384`, confirming our query vector has the same dimensions as stored vectors.

**Common Doubt:** *"What if the user's query has spelling mistakes?"*

* Embedding models are quite **forgiving** — "PAN cad" will still mostly match "PAN card" because the meaning is captured, not exact spelling.

---

## Executing Similarity Search Queries

This is the moment of truth — let us actually **search** and see the magic happen.

* **Official Definition:** A **similarity search** finds the vectors in the database that are nearest to the query vector, typically using **cosine similarity** or **Euclidean distance**.
* **In Simple Words:** It compares the "meaning vector" of your question to every "meaning vector" in the database and returns the closest ones.
* **Real-Life Example:** Imagine 100 students standing in a field. You say "find the 3 students whose heights are closest to 5'6''." That is exactly what similarity search does — but in 384 dimensions instead of just height.

**Full Code for Similarity Search:**

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="indian_faq")

user_query = "How do I get a new PAN card?"

query_embedding = model.encode([user_query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

print("User asked:", user_query)
print("\nTop 3 matching results:")
for i, doc in enumerate(results["documents"][0]):
    print(f"{i+1}. {doc}")
```

**How the code works:**

* **Load everything:** Model, client, and collection.
* **Embed the query:** As explained above.
* **`collection.query()`:** The main search command. We pass the query vector and say we want 3 results.
* **`results["documents"][0]`:** The first `[0]` is because Chroma supports multiple queries at once — we only asked one, so we take the first set.
* **Loop & Print:** We neatly show the top 3 matches.

**Expected Output:**

* Top 1 will likely be the PAN card sentence (obvious match).
* Top 2 might be the Aadhaar card sentence (similar "government document" meaning).
* Top 3 might be something unrelated like IRCTC (still a "how to" sentence).

---

## Interpreting Query Results

Getting results is only half the job. A good developer must **understand** what Chroma returns. Let us inspect the full response.

**What Chroma Returns (Every Time):**

* `ids` — the unique IDs of matching documents.
* `documents` — the original text.
* `metadatas` — the extra info we stored (like category).
* `distances` — a **score** telling us how close the match is.

**Understanding "Distance":**

* **Smaller distance = more similar.** This is confusing for beginners.
* Distance `0.0` = identical meaning.
* Distance `0.5` = somewhat similar.
* Distance `1.5+` = very different.

**Full Code to See Full Results:**

```python
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

for i in range(len(results["ids"][0])):
    print("ID:", results["ids"][0][i])
    print("Document:", results["documents"][0][i])
    print("Category:", results["metadatas"][0][i]["category"])
    print("Distance:", round(results["distances"][0][i], 3))
    print("---")
```

**How the code works:**

* **Loop by Index:** We loop using `i` to access all four pieces (id, doc, metadata, distance) of the same item.
* **`round(..., 3)`:** Makes the distance number easier to read by keeping 3 decimal places.

**Real-Life Example:** Think of dating apps — they show "92% match," "85% match." Distance is the opposite — smaller is better. Internally, many apps use vector search on your preferences vector.

---

## Implementing Top-K Retrieval

**Top-K** simply means "give me the top K results." K is a number you decide.

* **K = 1:** Only the single best match. Good for "one correct answer" cases.
* **K = 3 to 5:** Good for most chatbots and search boxes.
* **K = 10+:** Good when you want to give the user many options to choose from.

**How to Choose K?**

* **Small K (1-3):** When accuracy matters more than variety (e.g., medical advice).
* **Medium K (5-10):** When the user will scan results (e.g., Google-like search).
* **Large K (20+):** When you will feed results into another AI system (this is called **RAG** — Retrieval Augmented Generation).

**Code Tweak for Different K Values:**

```python
for k in [1, 3, 5]:
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )
    print(f"\n--- Top {k} results ---")
    for doc in results["documents"][0]:
        print("-", doc)
```

**How the code works:**

* **Loop over K values:** We try K=1, 3, 5 one by one.
* **Same query:** We keep the query fixed and only change `n_results`.
* **Print each set:** This shows how the results list grows as K increases.

**Common Mistake:**

* Students set K = 1000 on a small database. Chroma will only return as many as exist. No error, but also no magic — if you have 8 items, K=1000 gives only 8.

---

## Applying Basic Metadata Filtering in Queries

Sometimes similarity alone is not enough. You may want to search **within a specific category**. This is called **metadata filtering**.

* **Real-Life Example:** On Zomato, you first filter "Pure Veg" or "Under ₹300," and **then** search for "pizza." Metadata filtering in vector DB works similarly — filter first, then find similar vectors.

**Full Code for Filtered Search:**

```python
user_query = "tasty breakfast ideas"

query_embedding = model.encode([user_query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
    where={"category": "food"}
)

print("Query:", user_query)
print("Filtered results (only food category):")
for doc in results["documents"][0]:
    print("-", doc)
```

**How the code works:**

* **`where={"category": "food"}`:** This is Chroma's filter syntax. It tells the database, *"Only consider items where category = food."*
* **Similarity after filter:** Chroma first shortlists food-category items, then ranks them by vector similarity.
* **Result:** You will only get food-related sentences, even if an unrelated sentence had a higher similarity.

**Why is this powerful?**

* **Speed:** Filtering first means fewer vectors to compare — faster results on large databases.
* **Relevance:** Prevents irrelevant cross-topic matches.
* **Business Rules:** In real companies, you often need rules like "only show products in stock" or "only Mumbai branch data."

---

## Updating the Vector Collection

A real-world application keeps growing — new FAQs, new products, new articles. Our vector DB must support adding and updating data.

**Two Main Operations:**

* **Add new items:** Keep inserting fresh data with new IDs.
* **Update existing items:** If information changes, update the same ID (the text and/or the embedding).

**Full Code to Add New Data:**

```python
new_documents = [
    "How to link Aadhaar with PAN card online",
    "Best street food places in Old Delhi",
]

new_categories = ["government", "food"]

existing_count = collection.count()
new_ids = [f"doc_{existing_count + i}" for i in range(len(new_documents))]

new_embeddings = model.encode(new_documents).tolist()

collection.add(
    ids=new_ids,
    embeddings=new_embeddings,
    documents=new_documents,
    metadatas=[{"category": c} for c in new_categories]
)

print("New total items:", collection.count())
```

**How the code works:**

* **New data prepared:** Two more sentences with categories.
* **Unique IDs:** We build `doc_8` and `doc_9` based on existing count, so IDs never clash.
* **Same pattern:** Same `collection.add()` as before.

**Updating Existing Items:**

```python
collection.update(
    ids=["doc_0"],
    documents=["How to apply for Aadhaar card online step by step"],
    embeddings=model.encode(["How to apply for Aadhaar card online step by step"]).tolist()
)
```

**How the code works:**

* **`collection.update()`:** Targets an existing ID and replaces its text and embedding.
* **Why update embedding too?:** Because the text has changed, the old vector is no longer accurate.

**Common Mistake:**

* Students update the text but forget to update the embedding. Then searches still use the old meaning — leading to wrong results.

---

## Building a Minimal End-to-End Vector Search Application

Finally, let us combine **everything** into one clean, runnable program. This is the complete mini-application you can show in your resume/portfolio.

**Full Complete Code:**

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="indian_faq_app")

documents = [
    "How to apply for an Aadhaar card in India",
    "What is the procedure to get a PAN card",
    "Best places to visit in Manali during winter",
    "How to book a train ticket on IRCTC website",
    "Healthy Indian breakfast recipes for weight loss",
    "How to pay electricity bill online through UPI",
    "Top engineering colleges in India after JEE",
    "Recipe for homemade masala chai",
]

categories = [
    "government", "government", "travel", "travel",
    "food", "finance", "education", "food"
]

if collection.count() == 0:
    ids = [f"doc_{i}" for i in range(len(documents))]
    embeddings = model.encode(documents).tolist()
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=[{"category": c} for c in categories]
    )
    print("Data inserted for the first time.")
else:
    print("Data already exists. Skipping insert.")

def search(query_text, top_k=3, category_filter=None):
    query_vector = model.encode([query_text]).tolist()
    where_clause = {"category": category_filter} if category_filter else None
    results = collection.query(
        query_embeddings=query_vector,
        n_results=top_k,
        where=where_clause
    )
    return results

while True:
    user_input = input("\nAsk a question (or type 'exit'): ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    results = search(user_input, top_k=3)
    print("\nTop matches:")
    for i, doc in enumerate(results["documents"][0]):
        dist = round(results["distances"][0][i], 3)
        print(f"{i+1}. {doc}  (distance: {dist})")
```

**How the code works:**

* **Load once:** Model and client are set up at the top.
* **Smart Insert:** `if collection.count() == 0` checks if data is already stored. This prevents duplicate inserts when you run the program again.
* **`search()` function:** A clean, reusable function — you give it a query, top_k, and optional category filter; it returns results.
* **`while True` loop:** Creates a simple chatbot-like interface where the user keeps asking questions.
* **`exit` keyword:** A graceful way to stop the program.
* **Output:** Shows the top 3 matches with distances, so the user sees how confident each match is.

**Congratulations!** You have now built a complete, working vector search application — the same core technology used by ChatGPT's memory, Perplexity's search, and e-commerce recommendation engines.

---

## Important Commands & Libraries — Quick Reference Table

| Category | Command / Tool | What It Does |
|---|---|---|
| **Install** | `pip install chromadb` | Installs the Chroma vector database. |
| **Install** | `pip install sentence-transformers` | Installs the embedding model library. |
| **Model Loading** | `SentenceTransformer("all-MiniLM-L6-v2")` | Loads a free, small, pretrained embedding model. |
| **Generate Vectors** | `model.encode(list_of_texts)` | Converts a list of sentences into a 2D NumPy array of embeddings. |
| **Convert to List** | `.tolist()` | Converts NumPy array to Python list (required by Chroma). |
| **Create Client** | `chromadb.PersistentClient(path="./my_db")` | Creates a database that saves to disk. |
| **Create/Open Collection** | `client.get_or_create_collection(name="xyz")` | Opens collection if it exists; creates a new one if not. |
| **Insert Data** | `collection.add(ids=, embeddings=, documents=, metadatas=)` | Adds new records to the collection. |
| **Count Items** | `collection.count()` | Returns total number of records stored. |
| **Preview Data** | `collection.peek(limit=N)` | Shows first N records for verification. |
| **Search** | `collection.query(query_embeddings=, n_results=K)` | Returns top-K most similar records. |
| **Filtered Search** | `where={"category": "food"}` | Applies metadata filter during search. |
| **Update Record** | `collection.update(ids=, documents=, embeddings=)` | Modifies an existing record by ID. |
| **Delete Record** | `collection.delete(ids=["doc_1"])` | Removes specific records by ID. |
| **Key Concept** | Embedding | Numerical vector representation of text meaning. |
| **Key Concept** | Cosine Similarity / Distance | Measure of how "close" two vectors are in meaning (smaller distance = more similar). |
| **Key Concept** | Top-K Retrieval | Returning the K most similar items to a query. |
| **Key Concept** | Metadata Filtering | Narrowing the search space using tags like category, date, author, etc. |

---

Keep practicing by trying new datasets — your own WhatsApp chats, song lyrics, or college notes. The more you experiment, the deeper your understanding of **semantic search** will become. You are now officially ready to build AI-powered search features in any real project!
