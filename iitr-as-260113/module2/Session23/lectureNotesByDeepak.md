## What is the Role of Data in AI Systems?

AI systems are built on data.  
Without data, AI cannot learn patterns, make predictions, or support decision-making.

### Why data is important in AI

AI systems use data in three major stages:

**Training**

During training, the model learns from historical data.

**Example:**  
If we want to build a spam email detector, we train the model on thousands of emails labeled as:

* spam  
* not spam

The model studies patterns in the data and learns how to classify future emails.

**Inference**

Inference means using a trained model on new incoming data.

**Example:**  
A user receives a new email. The AI model checks that email and predicts whether it is spam or not.

**Decision-making**

AI systems often support or automate decisions.

**Example:**

* A shopping app recommends products  
* A bank flags suspicious transactions  
* A hospital system helps identify risky patients

In all of these, data is the foundation.

## Why is Efficient Storage Critical?

If data is not stored properly, AI systems become slow, unreliable, and difficult to manage.

**Problems with poor storage**

* data may be duplicated  
* data may be missing  
* searching data may become slow  
* updating data may cause inconsistency  
* large-scale systems may fail to handle growing volume

**Why efficient storage matters**

Efficient storage helps with:

* storing large amounts of data  
* retrieving data quickly  
* keeping data accurate  
* managing relationships between different entities  
* supporting AI pipelines smoothly

**Example:**  
Imagine an AI-powered e-commerce app:

* user data is stored  
* product data is stored  
* order history is stored  
* recommendation logs are stored

If this information is scattered across random files, it becomes hard to build reliable AI features.  
A proper database makes this organized and searchable.

## What is a Database?

A database is an organized system for storing, managing, and retrieving data.

Instead of keeping information in loose files, a database stores it in a structured way so that applications can easily access and update it.

### Simple definition

A database is a centralized and structured collection of data that can be:

* stored  
* updated  
* searched  
* managed efficiently

## Database vs File-Based Storage (CSV / Excel)

**File-based storage**

This means storing data in files such as:

* `.csv`  
* `.xlsx`  
* `.json`  
* `.txt`

**Example of CSV:**

| student_id | name | course | marks |
|------------|------|--------|-------|
| 1 | Rahul | Python | 85 |
| 2 | Neha | SQL | 91 |

This looks fine for a small class, but problems start when the system grows.

**Problems with file-based storage**

**Poor scalability**

As data grows into lakhs or crores of records, files become hard to manage.

**Data inconsistency**

Multiple copies of the same file may exist. One file may be updated while another is outdated.

**Difficult querying**

Finding “all students with marks > 90 in SQL” is not as efficient or flexible as in a database.

**No strong relationships**

It is hard to properly connect students, courses, teachers, and attendance using plain files.

**Concurrency issues**

If multiple users edit the same Excel file, conflicts can happen.

**Advantages of databases over files**

**Better scalability**

Databases can handle large volumes of data more effectively.

**Better consistency**

Rules can be applied to maintain correct and clean data.

**Powerful querying**

You can search, filter, sort, and combine data easily.

**Safer updates**

Multiple users and applications can work with the same database more reliably.

**Better structure**

Related data can be connected through keys and relationships.

## Real-life example of file based storage vs database storage

**File-based approach**

Suppose a small shop stores:

* customers in one Excel file  
* products in another Excel file  
* orders in another file

Now imagine:

* customer name changes  
* product price changes  
* order details need to be analyzed

This becomes messy very quickly.

**Database approach**

A database can store:

* customers table  
* products table  
* orders table  
* order_items table

Now everything is connected and easy to query.

## What is a Relational Database?

A relational database stores data in the form of tables. Each table represents a specific entity, and relationships between tables are maintained using keys.

Popular relational databases:

* MySQL  
* PostgreSQL  
* Oracle  
* SQL Server  
* SQLite

**Table-based structure**  
A table looks similar to an Excel sheet, but it is much more powerful.

**Example: Students table**

| student_id | name | age | course |
|------------|------|-----|--------|
| 1 | Asha | 21 | Python |
| 2 | Ravi | 22 | SQL |
| 3 | Meena | 20 | AI |

**Important terms**

* Table: collection of related data  
* Row: one record  
* Column: one attribute or field

**Rows and Columns**

**Row**  
A row represents one complete record.

**Example:**  
This row: `1 | Asha | 21 | Python`

means:

* student_id = 1  
* name = Asha  
* age = 21  
* course = Python

**Column**  
A column represents one property of the entity.

In the Students table:

* student_id  
* name  
* age  
* course

are columns.

## Tables and Basic Data Modeling

Data modeling means deciding how to represent real-world objects in tables.

In real life, we deal with entities such as:

* users  
* products  
* students  
* teachers  
* employees  
* orders

Each entity becomes a table.

**Example 1: User table**

| user_id | name | email | city |
|---------|------|-------|------|
| 101 | Deepak | deepak@gmail.com | Jaipur |
| 102 | Abhishek | abhishek@gmail.com | Delhi |

Here:

* entity = User  
* attributes = user_id, name, email, city

### Why does data modeling matters?

Good data modeling helps us:

* avoid duplicate data  
* keep data clean  
* represent real-world systems properly  
* build scalable applications

**Keys in Databases**  
Keys are used to uniquely identify records and connect tables.

The two most important keys are:

* Primary Key  
* Foreign Key

### Primary Key

A primary key is a column that uniquely identifies each row in a table.

Properties of primary key:

* must be unique  
* cannot be null  
* one table typically has one primary key

**Example: Students table**

| student_id | name | course |
|------------|------|--------|
| 1 | Rahul | Python |
| 2 | Neha | SQL |

Here, `student_id` is the primary key.

**Why?**  
Because each student has a unique ID.  
Even if two students have the same name, their `student_id` will still be different.

**Foreign Key**  
A foreign key is a column in one table that refers to the primary key of another table.

This is how tables are connected.

**Students table:**

| student_id | name |
|------------|------|
| 1 | Rahul |
| 2 | Neha |

**Courses table:**

| course_id | course_name |
|-----------|-------------|
| 101 | Python |
| 102 | SQL |

**Enrollments table:**

| enrollment_id | student_id | course_id |
|----------------|------------|-----------|
| 1 | 1 | 101 |
| 2 | 2 | 102 |

Here:

* student_id in Enrollments refers to Students table  
* course_id in Enrollments refers to Courses table

These are foreign keys.

## Relationships Between Tables

Relationships show how data in one table is connected to data in another.

### One-to-One

One record in table A is linked to one record in table B.

**Example:**  
One user has one passport.

### One-to-Many

One record in table A is linked to many records in table B.

**Example:**  
One customer can place many orders.

**Customer table:**

| customer_id | name |
|-------------|------|
| 1 | Deepak |

**Orders table:**

| order_id | customer_id | amount |
|----------|-------------|--------|
| 101 | 1 | 500 |
| 102 | 1 | 700 |

One customer → many orders.

**Many-to-Many**  
Many records in table A can relate to many records in table B.

**Example:**  
Many students can enroll in many courses.

To represent this, we use a third table called a **mapping table** or **junction table**.

## SQL as a Database Language

SQL stands for Structured Query Language.

It is the standard language used to interact with relational databases.

Using SQL, we can:

* create tables  
* insert data  
* read data  
* update data  
* delete data  
* filter and sort data

Think of SQL as the language through which we “talk” to the database.

## SQL Operations (CRUD)

CRUD stands for:

* Create  
* Read  
* Update  
* Delete

These are the most basic operations in any database system.

### CREATE / INSERT

Used to add new data.

```sql
INSERT INTO students (student_id, name, course, marks)
VALUES (1, 'Rahul', 'Python', 85);
```

This adds one new row into the students table.

### READ / SELECT

Used to retrieve data.

```sql
SELECT * FROM students;
```

This fetches all records from the students table.

### UPDATE

Used to modify existing data.

```sql
UPDATE students
SET marks = 90
WHERE student_id = 1;
```

This updates Rahul’s marks to 90.

### DELETE

Used to remove data.

```sql
DELETE FROM students
WHERE student_id = 1;
```

This deletes the student whose ID is 1.

## Basic Queries with Filtering and Sorting

After reading data, we often want only specific records.

For that, SQL provides clauses like:

* WHERE  
* ORDER BY

### WHERE clause

Used to filter rows based on a condition.

```sql
SELECT * FROM students
WHERE course = 'Python';
```

This returns only students enrolled in Python.

```sql
SELECT * FROM students
WHERE marks > 80;
```

This returns students who scored more than 80.

### ORDER BY clause

Used to sort the results.

```sql
SELECT * FROM students
ORDER BY marks ASC;
```

Sorts students by marks in ascending order.

**Descending order**

```sql
SELECT * FROM students
ORDER BY marks DESC;
```

Shows highest marks first.

### Combining WHERE and ORDER BY

```sql
SELECT * FROM students
WHERE course = 'Python'
ORDER BY marks DESC;
```

This means:  
first find students from Python course  
then sort them by highest marks first

## Structured vs Unstructured Data

AI systems work with different types of data.

Broadly, data can be divided into:

* structured data  
* unstructured data

**Structured Data**  
Structured data is organized in a predefined format, usually in rows and columns.

**Examples**

* customer records  
* product price tables  
* bank transaction logs  
* employee salary data

This data is easy to store in relational databases.

**Unstructured Data**  
Unstructured data does not fit neatly into rows and columns.

**Examples**

* text documents  
* emails  
* chat messages  
* images  
* audio recordings  
* videos  
* PDFs

Further examples:

* a customer review paragraph  
* a scanned invoice image  
* a voice recording  
* a YouTube video transcript

**Semi-structured data**  
Sometimes data is partly organized, but not in strict table format.

**Examples**

* JSON  
* XML

This is called semi-structured data.

## How Databases Fit into AI Pipelines?

A database is not the AI model itself, but it plays a crucial role in the overall AI pipeline.

A simple AI pipeline often looks like this:

Storage → Preprocessing → Model Usage → Output

Let us understand each part.

**Step 1: Data Storage**  
Raw data is stored in a database or storage system.

**Example**

An e-learning platform stores:

* student details  
* course details  
* quiz attempts  
* performance history

This data sits in the database.

**Step 2: Data Retrieval**  
The required data is fetched from the database.

**Example:**  
To predict which students may fail the exam, the system retrieves:

* attendance  
* quiz scores  
* assignment completion  
* previous marks

**Step 3: Preprocessing**  
Data is cleaned and prepared before sending it to the model.

This may include:

* handling missing values  
* removing duplicates  
* converting text into numbers  
* selecting useful columns

**Example**

Convert:

* “Yes/No” into 1/0  
* missing marks into average values  
* dates into useful features

**Step 4: Model Usage**  
The prepared data is sent to the AI model.

**Example:**  
A machine learning model predicts:

* pass / fail  
* fraud / not fraud  
* recommended / not recommended

**Step 5: Output or Decision**  
The prediction is used by the application.

**Example**

The system may:

* alert the teacher about at-risk students  
* recommend revision material  
* send personalized notifications
