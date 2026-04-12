# Pre-Read: Python - Working with Files

## What You’ll Learn
In this pre-read, you’ll discover:
- Why programs need to **read from and write to files**  
- How Python **opens and closes files** safely  
- Why **with blocks** are preferred over manual file handling  
- How to **read text files** and **write simple logs**  


![s9 preread](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4001141b-5e24-486d-ad5d-379f720d77ee/iFMzLqAOZcQlHTFH.png)

---

## Introduction: Why Programs Need Files
Imagine restarting your computer and losing everything you worked on.

That’s what happens if a program only uses memory.

Files allow programs to:
- **Save information permanently**  
- **Reuse data later**  
- **Share results with humans and other programs**  

Files are how programs remember.

---

## Why File Handling Matters
Working with files lets your programs:
1. **Persist data** beyond a single run  
2. **Process real-world information** like text files and logs  
3. **Record activity** for debugging and tracking  

Almost every serious application reads or writes files.

---

## From Known to New: Memory → Files
### What You Already Know
So far, data lives in:
- Variables  
- Lists  
- Dictionaries  

But once the program ends, everything disappears.

### The File-Based Way
Files store data on disk, so:
- Data survives program restarts  
- Information can be shared  
- Programs can grow beyond toy examples  

---

## Core File-Handling Concepts
### 1. Opening and Closing Files
Before using a file, Python must **open** it.

- Opening tells Python how you want to use the file  
- Closing frees system resources  

Forgetting to close files can cause bugs and data loss.

---

### 2. Using `with` Blocks
A **with block** manages files safely.

- Automatically closes the file  
- Prevents common mistakes  
- Makes code cleaner  

*Think of it as “open, use, and clean up—automatically.”*

---

### 3. Reading Text Files
Reading files allows programs to:
- Load data  
- Analyze content  
- Process instructions  

Text files are the simplest and most common format.

---

### 4. Writing Simple Logs
Writing to files lets programs:
- Save outputs  
- Record events  
- Track errors or activity  

Logs are written step by step as the program runs.

---

## Putting It All Together
A typical file workflow:
1. Open a file safely  
2. Read or write data  
3. Let Python close the file automatically  
4. Use saved data later  

This turns programs into long-term tools instead of one-time runs.

---

## Quick Practice (Think Before the Lecture)
1. Why is saving data in a file better than printing it?  
2. What could go wrong if a file is never closed?  
3. Where might logs be useful in a real application?

---

### Final Thought
Files give your programs **memory beyond execution**.  
Once you master file handling, your code starts interacting with the real world.
