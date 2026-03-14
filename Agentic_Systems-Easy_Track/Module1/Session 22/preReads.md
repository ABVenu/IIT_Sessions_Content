# Pre-Read: APIs — The Agent’s Hands

## What You’ll Learn
In this pre-read, you’ll discover:
- What an **API** is and why it allows programs to access web services  
- How the **Requests** library helps Python communicate with APIs  
- The difference between **GET** and **POST** requests  
- Why **status codes** matter when handling responses  
- How to read and understand **API documentation**

---

## Introduction: How Programs Reach the Web
Imagine asking a restaurant kitchen directly for food.

You wouldn’t walk into the kitchen.  
You would talk to the **waiter**, who carries your request and returns the result.

In software, that “waiter” is an **API (Application Programming Interface)**.

An API allows one program to **request information or actions from another system**.

---

## Why APIs Matter
APIs power most modern applications.

They allow programs to:
1. **Fetch live data** from the internet  
2. **Send requests to external services**  
3. **Integrate different systems together**

Many AI agents rely on APIs to interact with real-world information.

---

## From Known to New: Files → Web Data
### What You Already Know
You’ve worked with:
- Local files  
- CSV datasets  
- JSON data  

But these datasets are static.

### The API Approach
APIs allow your program to:
- Request fresh data  
- Receive responses instantly  
- Work with constantly updating information

This turns programs into dynamic systems.

---

## Core API Concepts
### 1. The Requests Library
Python’s **requests** library simplifies communication with web APIs.

It allows you to:
- Send requests to servers  
- Receive responses  
- Work with returned data easily

This library is the most common way to interact with APIs in Python.

---

### 2. GET vs POST
Different types of requests perform different actions.

**GET requests**
- Retrieve information  
- Do not change data  
- Used for fetching results

**POST requests**
- Send new data to a server  
- Often create or update resources

Understanding this difference is essential when working with APIs.

---

### 3. Handling Status Codes
When an API responds, it includes a **status code**.

These codes indicate whether the request succeeded or failed.

Examples include:
- Success responses  
- Client errors (invalid requests)  
- Server errors

Checking status codes ensures your program handles responses safely.

---

### 4. Reading API Documentation
Every API comes with documentation explaining:

- Available endpoints  
- Required parameters  
- Authentication requirements  
- Example responses

Reading documentation is often the most important step in using an API correctly.

---

## Putting It All Together
A typical API workflow:
1. Read the API documentation  
2. Send a request using the Requests library  
3. Check the status code  
4. Parse the response data  

This allows programs to interact with external services.

---

## Quick Practice (Think Before the Lecture)
1. Why might a program prefer API data over local files?  
2. When would a POST request be required instead of a GET request?  
3. Why is checking status codes important?

---

### Final Thought
APIs extend what your program can do.  
Instead of relying only on local data, your code can reach the entire web.