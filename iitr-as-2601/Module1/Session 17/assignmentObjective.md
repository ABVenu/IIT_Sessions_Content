# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

What is the primary purpose of the `SELECT` statement in SQL?

A) To delete rows from a table
B) To retrieve specific columns from a table
C) To create a new table
D) To modify existing data

**Correct answer:** B

**Explanation:**
`SELECT` is used to retrieve data from one or more tables. It specifies which columns should appear in the result set and is the foundation of all data retrieval operations in SQL.

---

### **2. (MCQ)**

What does the following query return?

```sql
SELECT *
FROM users;
```

A) Only the primary key
B) All columns from the `users` table
C) All tables in the database
D) Only unique rows

**Correct answer:** B

**Explanation:**
The `*` wildcard retrieves all columns from the specified table. While useful for exploration, it is discouraged in production environments because it may retrieve unnecessary data.

---

### **3. (MCQ)**

Which clause is used to filter rows based on a condition?

A) `ORDER BY`
B) `DISTINCT`
C) `WHERE`
D) `LIMIT`

**Correct answer:** C

**Explanation:**
The `WHERE` clause filters rows according to specified conditions. Without `WHERE`, all rows in the table are returned.

---

### **4. (MCQ)**

What is the correct way to retrieve students who scored above 85 and passed?

A)

```sql
SELECT name FROM students WHERE score > 85 OR passed = TRUE;
```

B)

```sql
SELECT name FROM students WHERE score > 85 AND passed = TRUE;
```

C)

```sql
SELECT name FROM students AND score > 85;
```

D)

```sql
SELECT name FROM students WHERE score > 85, passed = TRUE;
```

**Correct answer:** B

**Explanation:**
To ensure both conditions are satisfied, the `AND` operator must be used. `OR` would return rows meeting either condition, not necessarily both.

---

### **5. (MCQ)**

What does the `DISTINCT` keyword do?

A) Sorts the results
B) Removes duplicate rows in the result set
C) Deletes duplicate records from the table
D) Limits the number of rows returned

**Correct answer:** B

**Explanation:**
`DISTINCT` ensures that only unique combinations of selected columns are returned. It does not modify the underlying table—only the query output.

---

### **6. (MCQ)**

By default, how does `ORDER BY` sort results?

A) Descending
B) Randomly
C) Ascending
D) By primary key only

**Correct answer:** C

**Explanation:**
If no sorting direction is specified, `ORDER BY` sorts results in ascending order. To sort descending, `DESC` must be explicitly included.

---

### **7. (MCQ)**

What is the purpose of the `LIMIT` clause?

A) To restrict the number of columns returned
B) To restrict the number of rows returned
C) To filter based on numeric conditions
D) To remove duplicates

**Correct answer:** B

**Explanation:**
`LIMIT` restricts how many rows appear in the output. It is commonly used to preview datasets or retrieve top-ranked results.

---

### **8. (MCQ)**

What is the function of an alias in SQL?

A) Permanently renames a column in the table
B) Deletes a column
C) Temporarily renames a column or table in a query
D) Creates a new table

**Correct answer:** C

**Explanation:**
Aliases rename columns or tables within the context of a query using `AS`. They improve readability and make outputs clearer without changing the underlying database structure.