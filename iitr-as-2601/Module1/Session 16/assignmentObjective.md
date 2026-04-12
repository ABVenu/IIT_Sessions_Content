# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

What is the core structural unit of a relational database?

A) Document
B) Table
C) JSON object
D) Graph

**Correct answer:** B

**Explanation:**
Relational databases organize data into **tables** composed of rows and columns. Each table represents a specific entity (e.g., users, orders, products). This structured, tabular format is the foundation of relational systems.

---

### **2. (MCQ)**

In a relational table, what does a row represent?

A) A data type
B) A schema definition
C) A single record or entity instance
D) A query

**Correct answer:** C

**Explanation:**
Each row in a relational table represents one complete record (for example, one user or one order). Columns define attributes, while rows represent actual data entries.

---

### **3. (MCQ)**

What is the primary purpose of a primary key?

A) To sort data automatically
B) To uniquely identify each row in a table
C) To store foreign data
D) To define column names

**Correct answer:** B

**Explanation:**
A primary key uniquely identifies each record in a table. It must be unique and non-null. Without a primary key, reliably referencing or joining records becomes difficult or impossible.

---

### **4. (MCQ)**

Which of the following is required for a valid primary key?

A) It can contain duplicate values
B) It can contain NULL values
C) It must be unique and non-null
D) It must be a string

**Correct answer:** C

**Explanation:**
Primary keys must uniquely identify rows and cannot contain NULL values. They ensure integrity and consistent referencing across tables.

---

### **5. (MCQ)**

What is a database schema?

A) A query language
B) A table containing metadata
C) A formal definition of tables, columns, and constraints
D) A backup copy of the database

**Correct answer:** C

**Explanation:**
A schema defines the structure of the database: table names, column names, data types, and constraints (such as primary keys). It acts as a blueprint for how data is organized.

---

### **6. (MCQ)**

Which statement best describes relational databases?

A) They store data as flexible documents
B) They use structured tables and enforce schemas
C) They avoid relationships between data
D) They do not support constraints

**Correct answer:** B

**Explanation:**
Relational databases store data in structured tables and enforce schemas and constraints. This ensures consistency, integrity, and clear relationships between entities.

---

### **7. (MCQ)**

How do relational databases typically connect related tables?

A) By embedding one table inside another
B) By duplicating data across tables
C) By using foreign keys referencing primary keys
D) By storing all data in one table

**Correct answer:** C

**Explanation:**
Relational systems connect tables through keys. A foreign key references a primary key in another table, enabling structured relationships and efficient joins.

---

### **8. (MCQ)**

What is the main conceptual difference between relational and non-relational databases?

A) Relational databases do not support queries
B) Non-relational databases enforce strict schemas
C) Relational databases normalize data into tables, while non-relational systems often embed related data
D) Non-relational databases cannot scale

**Correct answer:** C

**Explanation:**
Relational systems normalize data into separate tables linked by keys. Non-relational systems often denormalize and embed related data inside documents. The difference lies in structure and design philosophy, not capability.