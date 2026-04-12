# Python: Working with Files

## What You’ll Learn

In this lesson, you’ll learn how Python programs interact with the local file system. You’ll understand how to open and close files safely, why the `with` statement is the preferred way to work with files, how to read data from text files, and how to write simple logs. These skills are essential for AI systems, which constantly read datasets, write results, and record execution details for debugging and auditing.


![S9 Notes](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/5fb372a1-0055-4588-b195-345293344efc/QbPxXfvReOXmRebs.png)

---

## 1. Why File Handling Matters in Real Systems

Most meaningful programs interact with data that exists **outside** the program itself. Models read training data from files. Scripts write predictions, metrics, and logs. Systems restart, but files persist.

File handling is how programs:
- Load input data
- Save outputs and results
- Record what happened during execution
- Communicate across runs and tools

In professional systems, file I/O is not an afterthought—it is part of the system’s reliability story. Code that reads and writes files correctly is code that can scale beyond a single session.

---

## 2. Files and the File System: A Mental Model

A file is a sequence of bytes stored on disk. When a Python program works with a file, it does not manipulate the file directly—it opens a **connection** to it.

This connection is called a **file handle**. While the handle is open:
- The program can read data from the file
- The program can write data to the file
- The operating system tracks the file’s state

Closing the file tells the operating system:
> “This program is done using this resource.”

Failing to close files can lead to data corruption, resource leaks, and subtle bugs.

---

## 3. Opening and Closing Files Explicitly

### Opening a File

Python uses the built-in `open()` function to open files.

```python
file = open("example.txt", "r")
````

The second argument specifies the **mode**:

* `"r"` → read
* `"w"` → write (overwrites existing file)
* `"a"` → append
* `"r+"` → read and write

Opening a file does not read it yet—it simply prepares it for interaction.

---

### Closing a File

When you are done, you must close the file:

```python
file.close()
```

This ensures:

* Data is flushed to disk
* System resources are released
* Other programs can safely access the file

While this approach works, it relies on the programmer remembering to close the file every time. In larger systems, this is risky.

---

## 4. The `with` Statement: Safe and Idiomatic File Handling

### Why `with` Exists

Python provides the `with` statement to manage resources safely. When used with files, it guarantees that the file is closed automatically—even if an error occurs.

This is the **recommended and professional way** to work with files.

---

### Using `with` to Open a File

```python
with open("example.txt", "r") as file:
    content = file.read()
```

When the block ends, Python automatically closes the file.

This pattern:

* Is safer
* Is cleaner
* Scales better in real systems

Google’s Python style guidance strongly encourages this approach because it reduces bugs related to resource management.

---

## 5. Reading Text Files

### Reading the Entire File

```python
with open("data.txt", "r") as file:
    text = file.read()
    print(text)
```

This reads the entire file into a single string. It is simple, but not ideal for very large files.

---

### Reading Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This approach:

* Is memory-efficient
* Preserves structure
* Is commonly used in data processing

In AI pipelines, reading line by line is common when processing logs, datasets, or streamed outputs.

---

### Reading All Lines into a List

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
```

Each line becomes an element in a list. This is useful when you need indexed access to lines.

---

## 6. Writing to Files

### Writing Text to a File

```python
with open("output.txt", "w") as file:
    file.write("Processing started\n")
```

Opening a file in `"w"` mode:

* Creates the file if it doesn’t exist
* Overwrites it if it does

This behavior is intentional but must be used carefully.

---

### Appending to a File

Appending preserves existing content:

```python
with open("output.txt", "a") as file:
    file.write("Processing completed\n")
```

Appending is especially useful for logging, where you want to record events over time.

---

## 7. Writing Simple Logs

### What Is a Log?

A log is a chronological record of events that occur during program execution. Logs help developers:

* Debug issues
* Understand system behavior
* Audit past runs

Even simple print-style logging written to a file can be incredibly valuable.

---

### A Simple Logging Example

```python
with open("app.log", "a") as log:
    log.write("Application started\n")
    log.write("Loading data\n")
    log.write("Application finished\n")
```

This creates a persistent record that survives program restarts.

In AI workflows, logs often capture:

* Start and end times
* Errors and warnings
* Model performance metrics
* Configuration details

---

## 8. A Complete Example: Reading Input, Writing Logs

```python
with open("numbers.txt", "r") as file:
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))

total = sum(numbers)

with open("results.log", "a") as log:
    log.write(f"Processed {len(numbers)} numbers\n")
    log.write(f"Total: {total}\n")
```

This example demonstrates:

* Reading structured data from a file
* Converting text to numbers
* Writing results to a log
* Separating data processing from persistence

This pattern appears frequently in data engineering and AI pipelines.

---

## 9. Common Beginner Mistakes

* Forgetting to close files
* Overwriting files unintentionally with `"w"` mode
* Reading large files entirely into memory
* Mixing file reading and writing logic in unclear ways

Using `with` blocks and keeping responsibilities separate prevents most of these issues.

---

## Key Takeaways

File handling allows programs to persist data beyond a single run. Python provides simple but powerful tools to open, read, write, and close files. The `with` statement ensures safety and clarity. Reading and writing files correctly is essential for building reliable AI systems that operate across time, data, and environments.

**Mental model:**
Files persist.
Open connects.
`with` protects.
Read consumes.
Write records.

---

## Additional Reading

* Python File I/O (Official Documentation):
  [https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

* Context Managers and `with`:
  [https://docs.python.org/3/reference/compound_stmts.html#the-with-statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

* Google Python Style Guide (File Handling):
  [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)
