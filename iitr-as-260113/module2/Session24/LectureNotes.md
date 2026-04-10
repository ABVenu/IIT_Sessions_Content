### **Introduction: Why Databases Matter in AI Systems**

AI systems do not work only because of models. They work because of data.

A model can generate answers, predictions, or decisions only when it has access to the right information. That information must be stored, organized, retrieved, and updated properly. This is where databases become important.

In traditional software, databases store user data, transactions, and business records.  
In AI systems, databases do even more:

* store user profiles  
* store chat history  
* store product or document metadata  
* store memory for AI agents  
* store application logs and feedback  
* provide context for model responses

So, in an AI application, the database is often the source of truth, while the AI model is the reasoning/generation engine.

![AI application: database as source of truth, model as reasoning engine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-module2-session24/ai_database_architecture.png)

### **Example of Database in AI Customer Support Assistant**

Imagine we are building an AI assistant for an e-commerce company.

This assistant can:

* answer customer questions  
* fetch customer order details  
* check ticket history  
* store conversation memory  
* recommend next actions to the support team

The system may use:

* structured data in a relational database. example: users, orders, tickets, payments  
* unstructured data. example: support emails, product manuals, policy documents, chat transcripts  
* AI processing. example: summarization, answer generation, intent detection, response drafting

![AI customer support assistant — structured data, unstructured data, and AI processing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-module2-session24/ai_support_assistant_flow.png)

### **SQL as a Database Language**

What is SQL?

SQL stands for Structured Query Language.

It is the standard language used to interact with relational databases such as:

* MySQL  
* PostgreSQL  
* SQLite  
* SQL Server  
* Oracle

SQL is used to:

* create tables  
* insert data  
* read data  
* update data  
* delete data  
* filter records  
* sort records  
* join tables  
* aggregate data

In simple words, SQL is the language through which applications talk to relational databases.

### **Why SQL is important for AI systems**

Even though AI systems often work with modern tools and APIs, SQL is still highly relevant because many important AI workflows depend on structured data stored in relational databases.

Examples:

* fetching customer details before generating a support reply  
* retrieving product price and stock before recommending an item  
* loading user interaction history for personalization  
* storing feedback on model outputs  
* tracking prompts, responses, and evaluation metrics

So, AI engineers must understand SQL not just as a database topic, but as a data access skill.

Example:  
Suppose we have a table called orders.

| order\_id | user\_id | product\_name | status | amount |
| ----- | ----- | ----- | ----- | ----- |
| 101 | 1 | Laptop | shipped | 55000 |
| 102 | 2 | Mouse | delivered | 1200 |
| 103 | 1 | Keyboard | pending | 2500 |

A simple SQL query:

| SELECT \* FROM orders; |
| :---- |

This means: fetch all rows and columns from the orders table.

### **Core SQL Operations (CRUD)**

CRUD stands for:

* Create  
* Read  
* Update  
* Delete

These are the most basic operations in any database-driven application.

![SQL CRUD: Create, Read, Update, Delete](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-module2-session24/sql_crud_operations.png)

### **CREATE / INSERT**

This is used to add new data.

Example

| INSERT INTO orders (order\_id, user\_id, product\_name, status, amount)VALUES (104, 3, 'Headphones', 'pending', 3000); |
| :---- |

This inserts a new order into the database.

**Example:** When a user starts a conversation with an AI assistant, the application may store the interaction in a table:

| INSERT INTO chat\_history (user\_id, user\_message, ai\_response)VALUES (1, 'Where is my order?', 'Your order has been shipped.'); |
| :---- |

So, INSERT is useful when AI systems need to store:

* user queries  
* model responses  
* feedback  
* memory  
* logs

### 

### **READ / SELECT**

This is used to fetch data.

Example

| SELECT \* FROM orders; |
| :---- |

Fetch only specific columns:

| SELECT product\_name, status FROM orders; |
| :---- |

**Example:** Before answering “Where is my order?”, the AI application may fetch the latest order:

| SELECT order\_id, statusFROM ordersWHERE user\_id \= 1ORDER BY order\_id DESCLIMIT 1; |
| :---- |

The result can then be passed to the AI model to generate a response like:

“Your most recent order is currently in shipped status.”

So, SELECT is extremely important because AI systems constantly retrieve data before generating output.

### **UPDATE**

This is used to modify existing data.

Example

| UPDATE ordersSET status \= 'delivered'WHERE order\_id \= 101; |
| :---- |

**Example:** Suppose the AI assistant summarizes a support ticket and the summary must be stored:

| UPDATE ticketsSET ai\_summary \= 'Customer is asking for refund due to damaged product.'WHERE ticket\_id \= 501; |
| :---- |

So, UPDATE is useful when AI systems need to:

* update memory  
* store new status  
* revise summaries  
* mark processed records  
* update evaluation results

### **DELETE**

This is used to remove data.

Example:

| DELETE FROM chat\_historyWHERE id \= 10; |
| :---- |

**Example:** Suppose temporary AI logs older than 30 days must be deleted:

| DELETE FROM ai\_logsWHERE created\_at \< '2026-03-01'; |
| :---- |

So, DELETE is useful for:

* removing stale logs  
* deleting temporary memory  
* cleaning outdated records  
* privacy-related data removal

### **Writing Queries with Filtering and Sorting**

Reading all data is rarely useful.  
AI systems usually need relevant data, not all data.

That is why filtering and sorting are very important.

### **WHERE Clause**

The WHERE clause filters rows.

Example

| SELECT \* FROM ordersWHERE status \= 'pending'; |
| :---- |

This fetches only pending orders.

**Example:** If the assistant needs all unresolved tickets:

| SELECT ticket\_id, issue\_type, created\_atFROM ticketsWHERE status \= 'open'; |
| :---- |

This helps the AI system focus only on relevant records.

### **ORDER BY Clause**

ORDER BY sorts the result.

Example: 

| SELECT \* FROM ordersORDER BY amount DESC; |
| :---- |

This fetches orders from highest amount to lowest.

Example: To get the latest conversation first:

| SELECT user\_message, ai\_response, created\_atFROM chat\_historyWHERE user\_id \= 1ORDER BY created\_at DESC; |
| :---- |

This is useful when the AI needs the most recent memory or interaction.

### **LIMIT Clause**

LIMIT restricts the number of rows returned.

Example:

| SELECT \* FROM ordersLIMIT 5; |
| :---- |

**Example:** If the assistant only needs the most recent 3 messages:

| SELECT user\_message, ai\_responseFROM chat\_historyWHERE user\_id \= 1ORDER BY created\_at DESCLIMIT 3; |
| :---- |

This avoids loading unnecessary data.

### **Combining WHERE, ORDER BY, and LIMIT**

Example: 

| SELECT order\_id, status, amountFROM ordersWHERE user\_id \= 1ORDER BY order\_id DESCLIMIT 1; |
| :---- |

* filter rows for a specific user  
* sort by newest order first  
* return only one row

This pattern appears very often in AI applications.

### **Structured vs Unstructured Data**

AI systems deal with many types of data, not just tables.

![Structured vs unstructured data in AI systems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-module2-session24/structured_vs_unstructured_data.png)

**Structured Data**  
Structured data is data organized in a fixed format, usually rows and columns.

Examples:

* users table  
* orders table  
* product inventory  
* support tickets  
* employee records

| user\_id | name | city | subscription |
| ----- | ----- | ----- | ----- |
| 1 | Asha | Delhi | Premium |
| 2 | Ravi | Pune | Basic |

This type of data is easy to query using SQL.

#### **Unstructured Data**

Unstructured data does not fit neatly into rows and columns.

Examples:

* emails  
* PDF documents  
* chat transcripts  
* images  
* audio recordings  
* videos  
* support call transcripts

**Example:** A customer complaint email:

**`“I received the wrong charger and the box was damaged.”`**

This is not naturally stored as clean columns like name, age, salary.  
It is free-form text.

**Why does this matter in AI ?** 

AI systems often combine both:

**Structured data**

* order\_id  
* order status  
* payment amount  
* customer tier

**Unstructured data**

* complaint text  
* product manual  
* delivery feedback  
* conversation transcript

**The AI model may use `unstructured text` for understanding, but use `structured data` for precise facts.**

Example: 

User asks:  
“Why was my refund delayed?”

The system may use:

**`structured data: refund status, transaction date, amount`**  
**`unstructured data: support notes, complaint text, internal policy explanation`**

So, strong AI systems often require both structured and unstructured retrieval.