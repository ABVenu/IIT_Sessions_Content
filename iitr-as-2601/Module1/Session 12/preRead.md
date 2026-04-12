# Pre-Read: Introduction to JSON

## What You’ll Learn
In this pre-read, you’ll discover:
- What **JSON** is and why it’s the standard for APIs and agents  
- How Python **dictionaries map naturally to JSON**  
- How programs **parse API responses**  
- How to read and work with **nested JSON data**  

---

## Introduction: How Programs Talk to Each Other
Imagine two people who don’t share a language.

They need a **common format** to exchange information clearly.

In software, that common language is often **JSON**.

JSON is how:
- APIs send data  
- Agents exchange information  
- Systems stay language-independent  

---

## Why JSON Matters
JSON sits at the center of modern AI systems.

It helps because:
1. **Humans can read it** easily  
2. **Machines can parse it** reliably  
3. **Different systems** can communicate without confusion  

If you work with APIs or agents, you will work with JSON.

---

## From Known to New: Dictionaries → JSON
### What You Already Know
You’ve used Python dictionaries:
- Key–value pairs  
- Nested structures  
- Lists inside dictionaries  

### The JSON Connection
JSON uses the **same idea**:
- Keys map to values  
- Values can be numbers, text, lists, or objects  
- Structures can be nested  

Learning JSON is mostly learning how dictionaries travel outside Python.

---

## Core JSON Concepts
### 1. JSON Structure
A JSON object:
- Uses key–value pairs  
- Has a clear, strict format  
- Represents structured data  

*Think of JSON as a dictionary written for the outside world.*

---

### 2. Dictionaries to JSON
Python dictionaries can be:
- Converted into JSON  
- Sent over networks  
- Stored in files  

This is how Python programs communicate with APIs and agents.

---

### 3. Parsing API Responses
APIs usually return:
- JSON text  
- With nested data inside  

Your job is to:
- Convert JSON into Python structures  
- Extract the fields you need  
- Handle missing or unexpected data  

This step turns raw responses into usable information.

---

### 4. Handling Nested JSON
Real JSON is rarely flat.

It often contains:
- Dictionaries inside dictionaries  
- Lists of objects  
- Deeply nested values  

Understanding the structure is more important than memorizing syntax.

---

## Putting It All Together
A common workflow:
1. Receive JSON from an API  
2. Parse it into Python dictionaries  
3. Navigate nested structures  
4. Extract meaningful values  

This is the backbone of API-driven systems.

---

## Quick Practice (Think Before the Lecture)
1. Why is JSON better than plain text for data exchange?  
2. How is a nested dictionary similar to nested JSON?  
3. What could break if an API changes its JSON structure?

---

### Final Thought
JSON is the **bridge** between programs.  
Once you’re comfortable with it, APIs and agents stop feeling mysterious.
