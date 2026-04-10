Q1: What will this query return?

SELECT * FROM orders;


A. Only the first row from orders
B. All rows and columns from orders
C. Only column names from orders
D. Deletes all rows from orders

Answer: B

Q2: Which query will fetch only the name and email columns from the users table?

A. SELECT (name, email) FROM users;
B. SELECT ALL name, email FROM users;
C. GET name, email FROM users;
D. SELECT name, email FROM users;

Answer: D

Q3: What will this query do?

SELECT * FROM orders
ORDER BY amount DESC;


A. Sort orders by amount from low to high
B. Sort orders by amount from high to low
C. Delete highest amount orders
D. Group orders by amount

Answer: B

Q4: What will this query return?

SELECT * FROM chat_history
LIMIT 3;


A. Last 3 rows only
B. 3 random rows 
C. Exactly 3 columns
D. First 3 rows from the result

Answer: D


Q5: Which query will fetch the most recent 5 messages for user_id = 10?

A.

SELECT * FROM chat_history
WHERE user_id = 10
LIMIT 5;


B.

SELECT * FROM chat_history
WHERE user_id = 10
ORDER BY created_at DESC
LIMIT 5;


C.

SELECT * FROM chat_history
ORDER BY created_at ASC
LIMIT 5;


D.

SELECT * FROM chat_history
WHERE created_at DESC
LIMIT 5;


Answer: B

Q6: Which query correctly inserts a new record into users(id, name, city)?

A.

INSERT users VALUES (1, 'Deepak', 'Bangalore');


B.

INSERT INTO users (id, name, city)
VALUES (1, 'Deepak', 'Bangalore');


C.

ADD INTO users (1, 'Deepak', 'Bangalore');


D.

CREATE INTO users VALUES (1, 'Deepak', 'Bangalore');


Answer: B

Q7: Which of the following is an example of structured data?

A. Customer complaint audio
B. Product image
C. orders table with columns like order_id, status, amount
D. PDF policy document

Answer: C

Q8: Why is LIMIT useful in AI systems?

A. It increases table size
B. It fetches only the required number of rows
C. It deletes extra records
D. It sorts the records automatically

Answer: B

Q9: You have a table called orders with the following columns:

order_id
user_id
product_name
status
amount

Write an SQL query to fetch the latest 5 orders of a user with user_id = 101, showing only the columns order_id, product_name, and amount.

The results should be sorted by the latest order first.








Answer: 

SELECT order_id, product_name, amount
FROM orders
WHERE user_id = 101
ORDER BY order_id DESC
LIMIT 5;


