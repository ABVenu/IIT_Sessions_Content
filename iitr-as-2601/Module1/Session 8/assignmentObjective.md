# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

Which of the following best describes a Python **list**?

A) Ordered and immutable
B) Unordered and mutable
C) Ordered and mutable
D) Unordered and immutable

**Correct answer:** C

**Explanation:**
A list maintains the order of elements and allows modification after creation (adding, removing, or updating items). This makes lists suitable for sequential data that changes over time, such as datasets or accumulated results.

---

### **2. (MCQ)**

What will the following code output?

```python
scores = [72, 85, 90, 66]
print(scores[2])
```

A) 72
B) 85
C) 90
D) 66

**Correct answer:** C

**Explanation:**
Python lists use **zero-based indexing**. Index `2` refers to the third element in the list, which is `90`.

---

### **3. (MCQ)**

Which operation modifies a list **in place**?

A) `scores[0:2]`
B) `scores.append(78)`
C) `scores + [78]`
D) `list(scores)`

**Correct answer:** B

**Explanation:**
`append()` directly changes the existing list by adding an element to it. Slicing and list concatenation return new lists instead of modifying the original.

---

### **4. (MCQ)**

Which statement about **list slicing** is true?

A) Slicing changes the original list
B) Slicing always returns a tuple
C) Slicing returns a new list
D) Slicing only works from index 0

**Correct answer:** C

**Explanation:**
List slicing creates and returns a **new list** containing the selected elements. The original list remains unchanged, which is important when working with subsets like train-test splits.

---

### **5. (MCQ)**

What is the defining characteristic of a **dictionary**?

A) Items are stored by index
B) Items are stored as key–value pairs
C) Items are stored in sorted order
D) Items cannot be modified

**Correct answer:** B

**Explanation:**
Dictionaries store data as **key–value pairs**, allowing access by meaningful labels instead of positions. This makes them ideal for structured and labeled data such as configurations or metadata.

---

### **6. (MCQ)**

Why are **tuples** often used instead of lists?

A) They are faster to iterate over
B) They allow duplicate removal
C) They prevent accidental modification
D) They support key–value access

**Correct answer:** C

**Explanation:**
Tuples are **immutable**, meaning their contents cannot be changed after creation. This immutability provides safety and makes intent explicit when data should remain fixed.

---

### **7. (MCQ)**

What is guaranteed by a Python **set**?

A) Items remain in insertion order
B) Items are indexed
C) Items are unique
D) Items are immutable

**Correct answer:** C

**Explanation:**
Sets automatically enforce **uniqueness**. Duplicate values are removed, and order is not preserved. This makes sets useful for deduplication and fast membership checks.

---

### **8. (MCQ)**

Which data structure is the **best choice** for mapping feature names to values in an AI model?

A) List
B) Tuple
C) Set
D) Dictionary

**Correct answer:** D

**Explanation:**
Dictionaries allow explicit labeling of values using keys, which improves clarity and correctness when handling structured data like features, configurations, or metadata.

---
