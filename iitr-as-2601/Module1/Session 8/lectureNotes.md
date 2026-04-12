# Python: Data Collections

## What You’ll Learn

In this lesson, you’ll learn how Python stores and manages **groups of information** using built-in data collections. You’ll understand how lists, dictionaries, tuples, and sets differ, how to access and manipulate their contents, and—most importantly—how to choose the right structure for a given problem. These concepts are foundational for AI systems, which routinely operate on datasets, features, predictions, and configurations at scale.

![S8 Notes](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/1d95f9a0-52a8-4964-9ac6-a6b336fddd81/oIJDuBEJJCryXdzb.png)

---

## 1. Why Data Collections Matter

Real programs rarely work with single values. They work with **collections**: lists of records, mappings from identifiers to values, sets of unique items, and fixed groups of related data. In AI and data-driven systems, collections appear everywhere—datasets, feature vectors, vocabularies, configuration objects, and results.

Choosing the right data structure affects:
- Clarity of code
- Performance
- Correctness
- Ease of maintenance

Python’s built-in collections are designed to cover the most common patterns engineers encounter, with clear semantics and predictable behavior.

---

## 2. Lists: Ordered, Changeable Sequences

### What Is a List?

A list is an **ordered, mutable collection** of items. “Ordered” means items have a position; “mutable” means the list can be changed after creation.

```python
scores = [72, 85, 90, 66]
````

Lists are the most commonly used collection in Python because they are flexible and intuitive.

You can access elements by index (starting at 0):

```python
scores[0]   # 72
scores[2]   # 90
```

---

### Modifying Lists

Because lists are mutable, you can change them in place:

```python
scores.append(78)      # Add an item
scores.remove(66)      # Remove an item
scores[1] = 88         # Update an item
```

This mutability is useful for:

* Accumulating results
* Building datasets incrementally
* Updating values during computation

---

### List Slicing: Working with Subsets

Slicing allows you to extract parts of a list using ranges.

```python
scores = [72, 85, 90, 66, 78]

scores[0:3]    # [72, 85, 90]
scores[2:]     # [90, 66, 78]
scores[:2]     # [72, 85]
```

Slicing does not modify the original list—it returns a new one. This is widely used in AI workflows, for example when splitting data into training and testing sets.

---

### When to Use Lists

Use lists when:

* Order matters
* Items may change
* You need to iterate sequentially

Lists are the default choice unless you have a specific reason to use another structure.

---

## 3. Dictionaries: Key–Value Data

### What Is a Dictionary?

A dictionary stores data as **key–value pairs**. Instead of accessing items by position, you access them by a meaningful key.

```python
user = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}
```

This structure mirrors how real-world data is often organized.

---

### Accessing and Modifying Dictionary Data

```python
user["name"]          # "Alice"
user["age"] = 31      # Update value
user["email"] = "a@example.com"  # Add new key
```

Keys must be unique and immutable (strings are commonly used).

---

### Why Dictionaries Are Critical in AI Systems

Dictionaries are ubiquitous in AI and system design:

* Configuration objects
* JSON-like data
* Model metadata
* Feature mappings
* API responses

They allow you to label data explicitly, making code more readable and robust.

---

### Iterating Over Dictionaries

```python
for key, value in user.items():
    print(key, value)
```

This pattern is common when inspecting model parameters or logging structured information.

---

## 4. Tuples: Fixed, Ordered Groups

### What Is a Tuple?

A tuple is an **ordered, immutable collection**. Once created, it cannot be changed.

```python
dimensions = (1920, 1080)
```

Tuples are often used to group related values that should not be modified independently.

---

### Why Immutability Matters

Immutability provides safety. When data should not change accidentally, tuples make intent explicit.

Examples:

* Coordinates
* Shape definitions
* Fixed configuration values

Because tuples cannot change, Python can optimize certain operations involving them.

---

### Tuple Unpacking

Tuples are commonly unpacked into variables:

```python
width, height = dimensions
```

This pattern is heavily used in Python and AI libraries.

---

## 5. Sets: Unique, Unordered Collections

### What Is a Set?

A set is an **unordered collection of unique items**.

```python
tags = {"ai", "python", "data"}
```

Sets automatically remove duplicates:

```python
unique_scores = {85, 90, 85, 72}
# Result: {72, 85, 90}
```

---

### Common Set Operations

Sets support mathematical operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b   # Union: {1, 2, 3, 4, 5}
a & b   # Intersection: {3}
a - b   # Difference: {1, 2}
```

These operations are useful when:

* Removing duplicates
* Comparing groups
* Tracking membership efficiently

---

### When to Use Sets

Use sets when:

* Order does not matter
* Uniqueness is required
* Fast membership checks are needed

Sets are commonly used for vocabularies, labels, and filtering operations in AI pipelines.

---

## 6. Choosing the Right Data Structure

Selecting the right collection is a design decision. A helpful way to decide is to ask:

* Do I care about order?
* Will the data change?
* Do I need labels (keys)?
* Do I need uniqueness?

### Quick Guide

* **List**: ordered, changeable, duplicates allowed
* **Dictionary**: labeled key–value data
* **Tuple**: fixed, ordered group
* **Set**: unique items, unordered

Professional code is not just about making something work—it’s about making intent clear through structure.

---

## 7. A Practical Example: Combining Structures

```python
users = [
    {"name": "Alice", "roles": {"admin", "editor"}},
    {"name": "Bob", "roles": {"viewer"}}
]

for user in users:
    if "admin" in user["roles"]:
        print(f"{user['name']} has admin access")
```

This example uses:

* Lists to store multiple users
* Dictionaries for structured user data
* Sets for unique role membership

This layered use of collections is common in real systems.

---

## 8. Common Beginner Mistakes

* Using lists when keys would be clearer
* Modifying tuples unintentionally (not allowed)
* Expecting sets to preserve order
* Overcomplicating structures instead of keeping them simple

These mistakes are normal and usually disappear as your mental model improves.

---

## Key Takeaways

Python offers multiple ways to store groups of information, each with a clear purpose. Lists handle ordered, changeable data. Dictionaries map keys to values. Tuples group fixed data safely. Sets enforce uniqueness. Choosing the right structure makes programs clearer, safer, and more scalable—especially in AI systems that manage large and complex data.

**Mental model:**
Lists sequence.
Dictionaries label.
Tuples protect.
Sets deduplicate.

---

## Additional Reading

* Python Data Structures (Official Tutorial):
  [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

* Choosing Data Structures in Python:
  [https://realpython.com/python-data-structures/](https://realpython.com/python-data-structures/)

* Google Python Style Guide (Collections):
  [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)
