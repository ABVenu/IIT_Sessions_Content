# Introduction to Databases for AI Systems

## Context of This Session

In the previous session, we went deep into how AI agents handle memory — both short-term memory that lives within a conversation, and long-term memory that persists across sessions. We explored strategies like Buffer Memory, Window Memory, and Summary Memory for managing short-term context, and we understood the three types of long-term memory: Episodic, Semantic, and Procedural. Towards the end, we touched on the idea that long-term memory must be stored somewhere — a file, a database, or a vector store.

That "somewhere" is exactly what this session is all about. Think of the previous session as understanding *why* agents need to remember things over time. This session answers *where* and *how* that data is actually stored, organised, and retrieved — which is the foundation of every intelligent AI system.

**In this session, you will:**

- Understand why simple file-based storage (like CSV or Excel) breaks down at scale and why databases were invented
- Explore the four main types of databases and when each is used in AI systems
- Understand how embeddings and semantic similarity power AI memory and RAG systems
- Learn core SQL vocabulary — tables, rows, columns, keys, schemas, constraints, and data types — including UUIDs and composite primary keys
- Set up and explore **Supabase**, a browser-based database tool that requires zero installation
- Write your first SQL queries to create tables and insert data
- Understand the difference between structured and unstructured data and why it matters for AI

---

## Why Data Storage Matters — The Problem with Files

Every AI system, at its core, works with data. Whether it is a chatbot remembering user preferences, a recommendation engine suggesting products, or an agent recalling past decisions — all of it needs to be stored somewhere and retrieved quickly.

Most beginners start storing data in Excel files or CSVs. This feels natural because everyone has used a spreadsheet. But as the system grows, file-based storage starts causing very serious problems.

### The Breakdown of File-Based Storage

- **Official Definition:** **File-based storage** refers to saving data in flat files such as `.csv`, `.xlsx`, or plain text files on a computer or server — without any built-in mechanism for querying, enforcing structure, or handling simultaneous access.
- **In Simple Words:** You are basically saving your data the same way you save a Word document. It works fine when you are alone, but falls apart when many people or systems try to use it at the same time.
- **Real-Life Example:** Imagine a school that keeps all student records in a single Excel file. One teacher opens it, another tries to edit it at the same time — the file gets corrupted. Now imagine 10,000 students across 100 schools. The file becomes unmanageable.

**Problems that file-based storage cannot solve:**

- **Scalability** — A CSV file with 10 million rows becomes extremely slow to open, search, or update.
- **Consistency** — Two people editing the same file at the same time can overwrite each other's changes.
- **Concurrent Access** — Files are not designed to be accessed by multiple systems or users simultaneously.
- **Queryability** — Finding "all students who scored above 80 in Mathematics" in a CSV requires reading the whole file line by line — there is no built-in way to filter smartly.
- **Relationships** — If student data is in one file and marks data is in another, linking them is messy and error-prone.

![File-based spreadsheets versus a managed database — scale, clashes, and why teams outgrow CSV and Excel alone](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session14/session14-01-file-vs-database.png)

### What a Database Solves

- **Official Definition:** A **database** is an organised collection of structured data, managed by a software called a **Database Management System (DBMS)**, which provides tools to store, retrieve, update, and delete data efficiently and reliably.
- **In Simple Words:** A database is like a very intelligent filing cabinet with a trained librarian who can find any record in seconds, let multiple people access it at once, and make sure no one's data gets overwritten by accident.
- **Real-Life Example:** Think of a bank. Thousands of customers are checking balances, making transfers, and withdrawing cash — all at the same time. This only works because a database is handling every transaction with precision, not an Excel sheet.

**What databases give you:**

- **Speed** — Databases use special internal structures (called indexes) to find records instantly, even in millions of rows.
- **Concurrent Access** — Multiple users and systems can read and write data at the same time without conflicts.
- **Data Integrity** — Rules can be enforced — for example, a student's age cannot be stored as "apple."
- **Relationships** — Data across multiple tables can be linked, so you do not duplicate information.
- **Security** — Access can be controlled — some users can only read, others can write.

---

## Types of Databases — Choosing the Right Tool for AI

Not all databases are the same. Just like you would not use a hammer to cut wood, different types of databases are built for different problems. In AI systems, you will encounter four major types.

### Relational Databases (SQL)

- **Official Definition:** A **relational database** stores data in structured **tables** made up of rows and columns. Tables can be linked to each other using **keys**. You interact with them using **SQL** (Structured Query Language).
- **In Simple Words:** Think of it like a very organised set of spreadsheets where all the sheets are connected. You define strict rules about what kind of data goes where, and SQL lets you ask questions across all the sheets at once.
- **Real-Life Example:** A hospital database — one table for patients, another for doctors, another for appointments. They are all linked so you can ask "Show me all appointments for Dr. Sharma next week."
- **When used in AI:** Storing structured training data, logging model outputs, managing user records in AI-powered apps, transaction history for financial AI systems.
- **Examples:** MySQL, PostgreSQL, Supabase (PostgreSQL-based), SQLite.

### NoSQL Databases (Document / Key-Value)

- **Official Definition:** **NoSQL databases** store data in formats other than relational tables — such as JSON documents, key-value pairs, graphs, or wide columns. They are flexible and do not require a fixed schema.
- **In Simple Words:** If a relational database is a filing cabinet with strict labelled folders, a NoSQL database is a box where you can throw in papers of any shape or size. It is more flexible but harder to keep organised.
- **Real-Life Example:** Think of a user profile in an app. One user has a phone number, another doesn't. One has 3 addresses, another has none. NoSQL can handle this irregular structure easily.
- **When used in AI:** Storing user conversation histories, session logs, flexible agent memory, product catalogs in e-commerce AI.
- **Examples:** MongoDB (document), Redis (key-value), DynamoDB (AWS).

### Vector Databases

- **Official Definition:** A **vector database** stores data as **mathematical vectors** — numerical representations of content like text, images, or audio — and is optimised to find similar items quickly using mathematical distance calculations.
- **In Simple Words:** When an AI reads a sentence, it converts it into a long list of numbers (a vector). A vector database stores these number lists and can instantly find "which stored sentence is most similar to this new query?" This is the engine behind AI memory retrieval and semantic search.
- **Real-Life Example:** Imagine you hum a tune and an app identifies the song. The hummed tune is converted to a vector, compared against millions of stored song vectors, and the nearest match is returned. That is vector search.
- **When used in AI:** Long-term memory for agents (retrieving relevant past conversations), semantic search, recommendation engines, RAG (Retrieval Augmented Generation) systems.
- **Examples:** Pinecone, Weaviate, ChromaDB, pgvector (inside PostgreSQL/Supabase).

### Time-Series Databases

- **Official Definition:** A **time-series database** is optimised to store and query data that is indexed by time — where every record has a timestamp and queries typically involve ranges of time.
- **In Simple Words:** These databases are designed for data that changes constantly over time — like a heart rate monitor or a stock price ticker. They make it very fast to ask "show me all readings from the last 30 minutes."
- **Real-Life Example:** Think of a smartwatch that records your heart rate every second. A regular database would struggle to store and retrieve 86,400 entries per day per user efficiently. A time-series database handles this without breaking a sweat.
- **When used in AI:** Monitoring AI model performance over time, IoT sensor data in industrial AI, financial market analysis, anomaly detection systems.
- **Examples:** InfluxDB, TimescaleDB, Amazon Timestream.

| Database Type | Format | Best For in AI | Example Tools |
|---|---|---|---|
| **Relational (SQL)** | Tables with rows & columns | Structured data, logs, user records | MySQL, PostgreSQL, Supabase |
| **NoSQL** | Documents, key-value, graphs | Flexible data, chat histories | MongoDB, Redis |
| **Vector** | Numerical vectors | Semantic search, agent memory | Pinecone, ChromaDB |
| **Time-Series** | Time-stamped records | Monitoring, sensor data, anomaly detection | InfluxDB, TimescaleDB |

![The four database families used in AI — relational tables, flexible NoSQL, vector search, and time-stamped streams](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session14/session14-02-four-database-types.png)

---

## Embeddings, Semantic Similarity, and RAG — How AI Actually Searches Memory

We briefly introduced vector databases as one of the four types. But vector databases deserve a deeper look — because they are the key to how AI agents remember things and retrieve relevant information intelligently. Before a vector database can be useful, you first need to understand **embeddings**.

### What Are Embeddings?

- **Official Definition:** An **embedding** is a numerical representation of a piece of content — text, image, or audio — expressed as a list (vector) of decimal numbers. It is produced by a trained AI model and captures the *meaning* of the content, not just its characters.
- **In Simple Words:** When you read "I love pizza," your brain understands the meaning — happiness, food, preference. An embedding does the same thing for a computer — it converts the sentence into a long list of numbers that mathematically represents its meaning.
- **Real-Life Example:** Think of a map. Every city has coordinates — (latitude, longitude). Two cities that are geographically close have similar coordinates. Embeddings work the same way — two sentences with similar *meaning* will have similar number-coordinates (vectors), even if the actual words are different.

**Key insight:** The sentence "I enjoy eating pizza" and "I love pizza" will produce embeddings that are very *close* to each other mathematically — because they mean nearly the same thing. The sentence "I hate mathematics" will produce an embedding that is far away. This closeness is what we call **semantic similarity**.

### Semantic Similarity — Searching by Meaning

- **Official Definition:** **Semantic similarity** is a measure of how alike two pieces of content are in *meaning*, computed by comparing their embeddings using mathematical distance metrics (like cosine similarity or dot product).
- **In Simple Words:** Instead of asking "do these two sentences share the same words?", semantic similarity asks "do these two sentences mean the same thing?" Two sentences can share zero words and still be semantically very similar.
- **Real-Life Example:** Imagine you search for "good restaurants near me" in an app, but the database stores listings tagged as "top-rated eateries in your area." A keyword search would find nothing — the words don't match. A semantic search (using embeddings) finds it immediately because the meaning is the same.

**How it works:**
- Every piece of content is converted to a vector (list of numbers) by an embedding model.
- When you search, your query is also converted to a vector.
- The vector database finds all stored vectors that are *closest* to your query vector.
- "Closest" = most similar in meaning — this is semantic search.

### RAG — Retrieval Augmented Generation

- **Official Definition:** **RAG (Retrieval Augmented Generation)** is an AI architecture pattern where a language model's response is augmented by first retrieving relevant information from an external knowledge source (typically a vector database) and providing that retrieved context to the model before it generates an answer.
- **In Simple Words:** Imagine an AI assistant that, before answering your question, quickly searches a library of notes and pulls out the 3 most relevant pages — then answers using those pages as context. That is RAG. The AI does not rely only on what it was trained on; it retrieves fresh, specific information first.
- **Real-Life Example:** You ask an AI customer support bot "What is the refund policy for orders above ₹5000?" Instead of guessing, the bot converts your question into an embedding, searches the company's policy documents (stored as embeddings in a vector database), retrieves the exact policy paragraph, and then generates an accurate answer using that retrieved text.

**Why RAG matters for AI agents:**
- Agents have limited memory within a conversation. RAG gives them access to a large external knowledge base.
- The retrieved information is always up-to-date — you can update the vector store without retraining the model.
- It dramatically reduces hallucinations — the model answers from retrieved facts, not guesses.

| Concept | What It Does | Where It Fits |
|---|---|---|
| **Embedding** | Converts content into a vector of numbers capturing meaning | Model output; stored in vector DB |
| **Semantic Similarity** | Measures closeness between two vectors = closeness in meaning | Used during search/retrieval |
| **Vector Database** | Stores embeddings and finds nearest ones to a query | The storage layer for RAG |
| **RAG** | Retrieve relevant context first, then generate an answer | End-to-end AI memory architecture |

---

## Core SQL Terminologies — The Vocabulary You Must Know

Now that you know relational databases are the foundation of most AI-powered applications, let's learn the language they speak. Before writing a single query, you need to understand the building blocks.

Think of a relational database as a well-organised **office building**. The building is the database, each **floor is a table**, each **row is one employee's file**, and each **column is a field** on that form (name, ID, department, etc.).

![Office-building analogy — database as the building, tables as floors, rows as records, and columns as labelled fields](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session14/session14-03-sql-office-building.png)

### Table

- **Official Definition:** A **table** is the primary structure in a relational database where data is stored in a grid of rows and columns, similar to a spreadsheet tab.
- **In Simple Words:** One table = one category of data. You have a `students` table, a `courses` table, an `orders` table — each dedicated to one type of thing.
- **Real-Life Example:** In a school, the attendance register is a table — one row per student per day, with columns for date, name, and present/absent.

### Row (Record)

- **Official Definition:** A **row** (also called a **record** or **tuple**) represents a single entry in a table — one complete set of information about one item.
- **In Simple Words:** One row = one thing. In a `students` table, each row is one student.
- **Real-Life Example:** In a hospital patient table, each row is one patient — their ID, name, age, and blood group.

### Column (Field / Attribute)

- **Official Definition:** A **column** (also called a **field** or **attribute**) represents one specific property or characteristic of the data stored in a table. All values in a column must be of the same data type.
- **In Simple Words:** Columns are the "categories" of information. In a `students` table, you might have columns: `student_id`, `name`, `age`, `email`.
- **Real-Life Example:** On an Aadhaar card form, each box you fill (name, DOB, address) is a column in the database table.

### Schema

- **Official Definition:** A **schema** is the formal structure or blueprint of a database — it defines all the tables, what columns each table has, the data types of those columns, and the relationships between tables.
- **In Simple Words:** A schema is like the architecture plan of a building — before construction starts, it defines where every room goes, how big each room is, and how the rooms are connected.
- **Real-Life Example:** Before building a hotel booking app, you define: "We will have a `hotels` table, a `rooms` table, and a `bookings` table, and here is exactly what each table looks like." That plan is the schema.

### Primary Key

- **Official Definition:** A **primary key** is a column (or combination of columns) in a table whose value is **unique for every row** and **cannot be null**. It is used to uniquely identify each record.
- **In Simple Words:** The primary key is the unique ID for every row — no two rows can have the same primary key value. It is how the database knows exactly which record you are talking about.
- **Real-Life Example:** Your **Aadhaar number** is a primary key in the government's database. Every Indian citizen has a different one, and no one is allowed to have the same number. The system uses it to pull up your exact record.
- **Common mistake to avoid:** Never use a person's name as a primary key — two students can have the same name. Always use a unique ID.

**Composite Primary Key — When One Column Is Not Enough:**

Sometimes, no single column is unique on its own, but a *combination* of two columns together is always unique. This is called a **composite primary key**.

- **Example:** In a `student_course_enrollment` table, one student can enroll in many courses, and one course can have many students. Neither `student_id` alone nor `course_id` alone is unique. But the *pair* `(student_id, course_id)` is unique — a specific student enrolling in a specific course happens only once.

```sql
-- Composite primary key: the combination of both columns must be unique
CREATE TABLE student_course_enrollment (
    student_id INT,                          -- Student identifier
    course_id INT,                           -- Course identifier
    enrolled_on DATE DEFAULT CURRENT_DATE,   -- Enrollment date
    PRIMARY KEY (student_id, course_id)      -- Composite PK = both columns together
);
```

**How the code works:**
- `PRIMARY KEY (student_id, course_id)` — The combination of both columns acts as the identifier. The same student cannot enroll in the same course twice, but can enroll in different courses.

### Foreign Key

- **Official Definition:** A **foreign key** is a column in one table that **references the primary key** of another table. It is used to establish and enforce a link (relationship) between two tables.
- **In Simple Words:** A foreign key is how tables talk to each other. It says "this value in my table corresponds to a row in another table."
- **Real-Life Example:** In a school database, the `marks` table has a column `student_id`. That `student_id` is a foreign key — it points to the `student_id` (primary key) in the `students` table. This connection tells you whose marks they are without repeating all student details.

![Primary keys uniquely identify a row in one table; foreign keys safely reference rows in another table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session14/session14-04-primary-foreign-keys.png)

### Constraints

- **Official Definition:** **Constraints** are rules applied to columns to control what kind of data can be entered. They enforce data integrity at the database level.
- **In Simple Words:** Constraints are like the validation rules on a form — they prevent bad data from entering the database.
- **Common constraints:**
  - `NOT NULL` — The column cannot be left empty. Example: `name NOT NULL` means every student must have a name.
  - `UNIQUE` — Every value in this column must be different. Example: email addresses.
  - `PRIMARY KEY` — Combines NOT NULL + UNIQUE for the identifier column.
  - `FOREIGN KEY` — Ensures the value exists in the referenced table.
  - `DEFAULT` — Sets a default value if none is provided.
  - `CHECK` — Validates that a value meets a condition. Example: `age > 0`.

### Data Types

- **Official Definition:** A **data type** defines the kind of value a column can store — numbers, text, dates, booleans, etc. The database enforces that only the correct type of data is inserted.
- **In Simple Words:** Data types are like labels on jars in a kitchen — the jar labelled "Sugar" should only contain sugar. If you try to put salt in it, the system rejects it.
- **Commonly used data types in SQL:**

| Data Type | What It Stores | Example |
|---|---|---|
| `INT` / `INTEGER` | Whole numbers | 1, 42, 1000 |
| `FLOAT` / `DECIMAL` | Numbers with decimals | 3.14, 99.99 |
| `VARCHAR(n)` | Variable-length text up to n characters | "Rahul", "Delhi" |
| `TEXT` | Long text with no size limit | Paragraph, descriptions |
| `BOOLEAN` | True or False | TRUE, FALSE |
| `DATE` | Date only | 2024-01-15 |
| `TIMESTAMP` | Date + Time | 2024-01-15 10:30:00 |
| `SERIAL` | Auto-incrementing integer | 1, 2, 3… (good for small systems) |
| `UUID` | Globally unique identifier | `a3f2c1d4-...` (safe at any scale) |

**SERIAL vs UUID — Which Should You Use?**

- `SERIAL` gives you simple numbers (1, 2, 3…). It is easy to read and works fine for small systems.
- `UUID` (Universally Unique Identifier) generates a long random string like `a3f2c1d4-89bc-4e1f-b720-3c9a1e0f7d82`. It is guaranteed to be unique even across different databases, servers, or countries.
- **Why UUID at scale:** If you have multiple databases merging data (like a global app with servers in India and the US), two records can accidentally get `SERIAL` ID = 1 from different servers. UUID prevents this clash entirely — the probability of two UUIDs being identical is astronomically small.
- **Rule of thumb:** Use `SERIAL` for simple learning projects. Use `UUID` for production systems that need to scale or merge data across servers.

---

## Where SQL Can Be Written — MySQL vs Supabase

You now know the vocabulary. Before writing queries, let us understand *where* you write them. There are several platforms available.

### MySQL (Traditional Setup)

- **Official Definition:** **MySQL** is one of the most widely used open-source relational database systems. It requires installation on your computer or server and is managed through a local interface or terminal.
- **In Simple Words:** MySQL is powerful and widely used in production systems, but it requires you to install software, configure settings, and manage the database locally.
- **Limitation for beginners:** The setup process can be tricky — port conflicts, permission issues, and command-line usage can be a barrier for those new to tech.

### Supabase — Our Go-To Tool

- **Official Definition:** **Supabase** is an open-source Backend-as-a-Service (BaaS) platform built on top of **PostgreSQL** (one of the most powerful SQL databases). It provides a browser-based dashboard, a SQL editor, and auto-generated APIs — all without any installation.
- **In Simple Words:** Supabase is like having a full-featured database that runs in your browser. You go to the website, create a project, and immediately start writing SQL — no installation, no configuration, no terminal commands.
- **Why Supabase for this course:**
  - **Zero installation** — works entirely in the browser
  - **Visual table UI** — you can see your data in a clean spreadsheet-like view
  - **Built-in SQL editor** — write and run queries directly in the browser
  - **Future-ready** — Supabase connects directly to AI systems, Python backends, and automation tools we will use in upcoming sessions
  - **Free tier available** — no cost to get started

> **Note:** Both MySQL and Supabase speak the same SQL language — the queries you write are essentially identical. The difference is only in how you set up and access the database.

---

## Setting Up and Exploring Supabase

Let's walk through setting up your Supabase workspace step by step.

### Step 1 — Create a Supabase Account

- Go to [https://supabase.com](https://supabase.com) and click **Start your project**
- Sign in with your GitHub account (recommended) or email
- Once logged in, you will land on the **Supabase Dashboard**

### Step 2 — Create a New Project

- Click **New Project**
- Choose your **organisation** (Supabase creates one by default with your account name)
- Give your project a name — for example: `ai_systems_db`
- Set a **Database Password** — save this somewhere; you will need it later
- Choose a **Region** closest to you (e.g., Southeast Asia — Singapore)
- Click **Create New Project** and wait about 60 seconds for setup

### Step 3 — Explore the Dashboard

Once your project is ready, familiarise yourself with the left sidebar:

| Section | What It Does |
|---|---|
| **Table Editor** | View and manage your tables visually — like a spreadsheet |
| **SQL Editor** | Write and run SQL queries directly |
| **Database** | View table schemas, functions, and extensions |
| **Authentication** | Manage users and login methods |
| **Storage** | Store files (images, PDFs, etc.) |
| **Edge Functions** | Run server-side code |
| **API Docs** | Auto-generated API documentation for your tables |

**For this session, you will primarily use:** the **Table Editor** and the **SQL Editor**.

> **Important:** When creating tables in Supabase for practice, disable Row Level Security (RLS) so your queries run without permission errors. You will learn about RLS when we connect Supabase to AI systems in upcoming sessions.

---

## Creating Tables and Inserting Data — CREATE & INSERT

Now that Supabase is ready, let's create our first table. We will use a relatable real-world example: a **student management system** for an AI course.

### The CREATE TABLE Statement

- **Official Definition:** `CREATE TABLE` is a SQL command used to define and create a new table in the database, specifying its columns, data types, and constraints.
- **In Simple Words:** `CREATE TABLE` is like designing a new registration form — you decide what fields exist, what type of data goes in each field, and what rules apply.

**Full Code — Creating the `students` Table:**

```sql
-- Create a table called 'students' to store student information
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,      -- Auto-incrementing unique ID for each student
    full_name VARCHAR(100) NOT NULL,     -- Student's full name; cannot be empty
    email VARCHAR(150) UNIQUE NOT NULL,  -- Email must be unique and cannot be empty
    course VARCHAR(100) NOT NULL,        -- The course the student is enrolled in
    city VARCHAR(50),                    -- City where the student is from (optional)
    enrollment_date DATE DEFAULT CURRENT_DATE,  -- Defaults to today's date if not provided
    is_active BOOLEAN DEFAULT TRUE       -- Whether the student is currently enrolled
);
```

**How the code works:**

- `SERIAL PRIMARY KEY` — `SERIAL` means the database automatically assigns the next number (1, 2, 3...) to `student_id` for every new row. `PRIMARY KEY` means it uniquely identifies each student.
- `VARCHAR(100) NOT NULL` — Stores text up to 100 characters; the field cannot be left blank.
- `UNIQUE NOT NULL` on `email` — Every student must have an email, and no two students can share the same email.
- `DEFAULT CURRENT_DATE` — If you do not provide an enrollment date, today's date is filled in automatically.
- `BOOLEAN DEFAULT TRUE` — The `is_active` column starts as `TRUE` for every new student unless you say otherwise.

### The INSERT INTO Statement

- **Official Definition:** `INSERT INTO` is a SQL command used to add new rows (records) of data into an existing table.
- **In Simple Words:** `INSERT INTO` is like filling in a registration form and submitting it. Each `INSERT` adds one (or more) complete records to the table.

**Full Code — Inserting Multiple Students:**

```sql
-- Insert the first student record
INSERT INTO students (full_name, email, course, city)
VALUES ('Ananya Sharma', 'ananya@example.com', 'Agentic Systems and Design', 'Bangalore');

-- Insert a second student
INSERT INTO students (full_name, email, course, city)
VALUES ('Rohan Mehta', 'rohan@example.com', 'Agentic Systems and Design', 'Mumbai');

-- Insert a third student with no city provided
INSERT INTO students (full_name, email, course)
VALUES ('Priya Nair', 'priya@example.com', 'Agentic Systems and Design');

-- Insert multiple students in a single INSERT statement
INSERT INTO students (full_name, email, course, city)
VALUES 
    ('Karan Patel', 'karan@example.com', 'Agentic Systems and Design', 'Ahmedabad'),
    ('Sana Mirza', 'sana@example.com', 'Agentic Systems and Design', 'Hyderabad'),
    ('Dev Joshi', 'dev@example.com', 'Agentic Systems and Design', 'Pune');
```

**How the code works:**

- `INSERT INTO students (column1, column2, ...)` — You name which columns you are providing values for.
- `VALUES (...)` — You provide the actual data in the same order as the column names listed above.
- `student_id` is not mentioned because `SERIAL` fills it automatically — the database handles it.
- `enrollment_date` and `is_active` are also not mentioned because they have `DEFAULT` values.
- Priya's row has no `city` — that column allows `NULL` (no `NOT NULL` constraint), so it is stored as empty.

---

## Structured vs Unstructured Data — What It Means for AI

We have been working with **structured data** — data that fits neatly into rows and columns with defined types. But most of the world's data is actually **unstructured**. Understanding this difference is essential for anyone building AI systems.

### Structured Data

- **Official Definition:** **Structured data** is data that is organised into a predefined format — typically rows and columns with specific data types — that can be easily stored, searched, and analysed using SQL.
- **In Simple Words:** Structured data is data that fits into a table. Every value knows exactly which box it belongs in.
- **Examples in AI:** Student records, transaction histories, sensor readings, user click logs, product inventory.
- **Stored in:** Relational databases (MySQL, PostgreSQL, Supabase), spreadsheets.

### Unstructured Data

- **Official Definition:** **Unstructured data** is data that does not have a predefined format or schema. It includes text documents, images, audio files, videos, emails, and social media posts.
- **In Simple Words:** Unstructured data is anything that cannot naturally fit into a neat table. A WhatsApp message, a photo, a voice recording — these are unstructured.
- **Examples in AI:** Training data for language models (raw text), images for computer vision, audio for speech recognition, customer reviews for sentiment analysis.
- **Stored in:** File systems, object storage (like AWS S3), NoSQL databases, or converted into vectors and stored in vector databases.

![Structured data fits cleanly into relational tables queried with SQL; rich media and free text stay unstructured until models or embeddings reshape them](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session14/session14-06-structured-vs-unstructured.png)

### Why This Distinction Matters in AI

| Aspect | Structured Data | Unstructured Data |
|---|---|---|
| **Format** | Tables, rows, columns | Text, images, audio, video |
| **Query Method** | SQL | AI models, NLP, Computer Vision |
| **Storage** | Relational databases | File systems, NoSQL, Vector DBs |
| **Volume** | Typically smaller, well-defined | Huge — 80%+ of all data in the world |
| **AI Use** | Feature engineering, logs, rules | Training data, embeddings, inputs |

- When an AI agent retrieves a user's past purchase history — that is **structured data** from a relational database.
- When an AI reads a customer review and decides the sentiment is "positive" — that is processing **unstructured text**.
- When an AI searches its memory for "what did this user talk about 3 sessions ago?" — it converts the old conversations (unstructured) into vectors and searches a **vector database** using semantic similarity (as we covered in the Embeddings & RAG section).

Understanding which type of data you are working with directly determines which database type to use — and this is why we started this session by learning all four database types.

---

## Key Takeaways

- **Databases solve real problems** that file-based storage cannot handle at scale — concurrent access, speed, data integrity, and queryability. For any AI system that handles real users and real data, a database is non-negotiable.
- **Four database types serve four different needs:** Relational (SQL) for structured records, NoSQL for flexible data, Vector databases for AI memory and semantic search, and Time-Series for timestamped data streams.
- **Embeddings are how AI converts meaning into numbers.** Semantic similarity lets vector databases find "close in meaning" content — and RAG uses this to give AI agents access to external knowledge, dramatically reducing hallucinations.
- **SQL is the language of relational databases.** You learned the core vocabulary: `CREATE TABLE` to define structure and `INSERT INTO` to add data — with constraints like `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` keeping your data clean.
- **UUID vs SERIAL:** For small projects, `SERIAL` auto-incrementing IDs are fine. For production systems merging data across servers at scale, `UUID` prevents ID collisions entirely. Composite primary keys solve cases where no single column is unique, but a combination of columns is.
- **Structured data lives in tables; unstructured data lives everywhere else.** In the next session, we will pick up from here — reading data with `SELECT`, filtering with `WHERE`, and updating/deleting records — before connecting this database knowledge to Python and AI workflows.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `CREATE TABLE` | SQL Command | Defines and creates a new table with columns and constraints |
| `INSERT INTO` | SQL Command | Adds new rows of data into a table |
| `PRIMARY KEY` | Constraint | Unique, non-null identifier for each row in a table |
| `FOREIGN KEY` | Constraint | Links a column to the primary key of another table |
| `NOT NULL` | Constraint | Column must always have a value; cannot be empty |
| `UNIQUE` | Constraint | All values in the column must be different |
| `DEFAULT` | Constraint | Sets an automatic value if no value is provided |
| `CHECK` | Constraint | Validates that a value meets a given condition |
| `SERIAL` | Data Type | Auto-incrementing integer, commonly used for primary keys in small systems |
| `UUID` | Data Type | Globally unique identifier; collision-safe at any scale or across multiple servers |
| `VARCHAR(n)` | Data Type | Variable-length text with a maximum of n characters |
| `BOOLEAN` | Data Type | Stores TRUE or FALSE |
| `TIMESTAMP` | Data Type | Stores both date and time |
| **Composite Primary Key** | Concept | A primary key made of two or more columns whose combined values are unique |
| **Relational Database** | Concept | Database that stores data in structured tables linked by keys |
| **NoSQL Database** | Concept | Database for flexible, non-tabular data formats |
| **Vector Database** | Concept | Database optimised for storing and searching mathematical embeddings |
| **Time-Series Database** | Concept | Database optimised for time-stamped sequential data |
| **Schema** | Concept | The structural blueprint of a database — tables, columns, types, and relationships |
| **Structured Data** | Concept | Data organised in tables with a fixed format and data types |
| **Unstructured Data** | Concept | Data without a fixed format — text, images, audio, video |
| **Embedding** | Concept | A numerical vector (list of numbers) representing the meaning of content |
| **Semantic Similarity** | Concept | Measure of how close two embeddings are — i.e., how similar in meaning two pieces of content are |
| **RAG** | Concept | Retrieval Augmented Generation — retrieve relevant context from a vector DB before generating a response |
| **Supabase** | Tool | Browser-based PostgreSQL database with a visual interface and SQL editor |
| **MySQL** | Tool | Widely-used open-source relational database system |
| **PostgreSQL** | Tool | Powerful open-source SQL database; the engine behind Supabase |
| **SQL** | Language | Structured Query Language — used to interact with relational databases |
| **DBMS** | Concept | Database Management System — software that manages a database |
