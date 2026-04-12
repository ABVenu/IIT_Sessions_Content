# Pre-Read: Python - Data Collections

## What You’ll Learn
In this pre-read, you’ll discover:
- Why programs need **collections** instead of many single variables  
- How **lists**, **dictionaries**, **tuples**, and **sets** differ  
- What **slicing** means and why it’s useful  
- How to choose the **right data structure** for a task  

![S8 preread](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/1cc8b75c-d902-4b40-bf6d-29acf2790277/OkbJTgXNjomEjo33.png)


---

## Introduction: Why Data Comes in Groups
Imagine storing your contacts.

You wouldn’t create one phone just for names, another just for numbers, and another for emails.  
You’d group related information together.

In Python, **data collections** do exactly that—they store **multiple values** in one structure.

---

## Why Data Collections Matter
Collections help you:
1. **Organize related information**  
2. **Process many values efficiently**  
3. **Write cleaner, more scalable code**  

Almost every real program works with groups of data.

---

## From Known to New: Many Variables → Collections
### The Clumsy Way
You might store values like this:
- score1  
- score2  
- score3  

This breaks down quickly as numbers grow.

### The Python Way
You store all related values **together** in a collection and work with them as a group.

This is simpler and more powerful.

---

## Core Types of Data Collections
### 1. Lists
A **list** stores ordered items.

- Items keep their position  
- Values can change  
- Supports slicing (taking parts of the list)  

*Think of a list as a row of boxes in order.*

---

### 2. List Slicing
**Slicing** lets you take a portion of a list.

- You can grab a range of items  
- Original list stays unchanged  

This is useful when working with subsets of data.

---

### 3. Dictionaries
A **dictionary** stores data as **key–value pairs**.

- You look up values using keys  
- Order is not the main focus  
- Very fast for searching  

*Think of a dictionary like a real dictionary—word → meaning.*

---

### 4. Tuples
A **tuple** is like a list, but **unchangeable**.

- Items are ordered  
- Values cannot be modified  
- Useful for fixed data  

*Think of a tuple as a sealed package.*

---

### 5. Sets
A **set** stores **unique** values only.

- No duplicates allowed  
- Order does not matter  
- Useful for removing repeats  

*Think of a set as a bag that rejects duplicates.*

---

## Choosing the Right Structure
Ask yourself:
- Does order matter? → List or Tuple  
- Do values need names? → Dictionary  
- Should values never change? → Tuple  
- Do I need uniqueness? → Set  

Choosing correctly makes your code simpler and faster.

---

## Putting It All Together
A program might:
1. Store values in a list  
2. Slice the needed portion  
3. Use a dictionary for fast lookups  
4. Use a set to remove duplicates  

Each structure has a purpose.

---

## Quick Practice (Think Before the Lecture)
1. What data in your life naturally comes as a group?  
2. When would changing data be dangerous?  
3. Why is a dictionary better than a list for lookups?

---

### Final Thought
Data collections are how programs **think in groups**.  
Once you master them, handling real-world data becomes natural.
