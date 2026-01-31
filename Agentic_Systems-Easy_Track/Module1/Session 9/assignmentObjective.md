# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

Why is file handling essential in real-world Python and AI systems?

A) It improves execution speed
B) It allows data to persist beyond a single program run
C) It replaces the need for databases
D) It prevents syntax errors

**Correct answer:** B

**Explanation:**
Files allow programs to read input data, store outputs, and record logs that persist even after the program exits. AI systems rely heavily on this persistence for datasets, results, and debugging information.

---

### **2. (MCQ)**

What does the `open()` function return when a file is opened successfully?

A) The file contents
B) The file path
C) A file handle (file object)
D) A Boolean value

**Correct answer:** C

**Explanation:**
`open()` returns a **file handle**, which represents an active connection between the program and the file. All reading and writing operations are performed through this handle.

---

### **3. (MCQ)**

Which file mode opens a file for writing **and overwrites existing content**?

A) `"r"`
B) `"a"`
C) `"r+"`
D) `"w"`

**Correct answer:** D

**Explanation:**
The `"w"` mode creates a new file if it doesn’t exist and **overwrites** the file if it already exists. This behavior is intentional but potentially dangerous if used carelessly.

---

### **4. (MCQ)**

Why is explicitly calling `file.close()` important when not using `with`?

A) It increases file size
B) It flushes data and releases system resources
C) It improves readability
D) It prevents Python from crashing

**Correct answer:** B

**Explanation:**
Closing a file ensures that buffered data is written to disk and system resources are released. Failing to close files can cause data corruption or resource leaks.

---

### **5. (MCQ)**

What is the primary advantage of using the `with` statement when working with files?

A) It allows faster reading
B) It avoids syntax errors
C) It automatically closes the file even if an error occurs
D) It reads the file line by line

**Correct answer:** C

**Explanation:**
The `with` statement uses a context manager to guarantee that files are closed properly, even if an exception is raised. This makes file handling safer and more reliable.

---

### **6. (MCQ)**

Which approach is most memory-efficient when processing very large text files?

A) `file.read()`
B) `file.readlines()`
C) Iterating over the file line by line
D) Copying the file into a list

**Correct answer:** C

**Explanation:**
Iterating line by line reads only one line into memory at a time, making it ideal for large files commonly used in data processing and AI pipelines.

---

### **7. (MCQ)**

What is the key difference between `"w"` and `"a"` file modes?

A) `"w"` reads, `"a"` writes
B) `"w"` appends, `"a"` overwrites
C) `"w"` overwrites, `"a"` preserves existing content
D) `"w"` works only with text files

**Correct answer:** C

**Explanation:**
`"w"` clears existing content before writing, while `"a"` appends new content to the end of the file. Appending is especially useful for logs.

---

### **8. (MCQ)**

Why are logs commonly written using append mode (`"a"`)?

A) Logs must be immutable
B) Logs are usually small
C) Logs should record events chronologically over time
D) Append mode is faster

**Correct answer:** C

**Explanation:**
Logs are meant to accumulate information across multiple program runs. Using append mode ensures previous log entries are preserved and new events are added sequentially.

---
