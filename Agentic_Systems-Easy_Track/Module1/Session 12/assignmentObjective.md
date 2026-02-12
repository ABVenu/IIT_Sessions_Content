# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

Why is JSON widely used as the standard format for APIs and agent communication?

A) It supports executable code
B) It is lightweight, structured, and language-agnostic
C) It is faster than binary formats in all cases
D) It is only compatible with JavaScript

**Correct answer:** B

**Explanation:**
JSON is human-readable, machine-parseable, lightweight, and independent of any programming language. These properties make it ideal for communication between services, APIs, agents, and platforms in AI systems.

---

### **2. (MCQ)**

Which JSON structure corresponds most closely to a Python dictionary?

A) JSON array
B) JSON string
C) JSON object
D) JSON number

**Correct answer:** C

**Explanation:**
A JSON object consists of key–value pairs enclosed in `{}` and maps directly to a Python dictionary. This intentional similarity makes Python a natural choice for API and AI work.

---

### **3. (MCQ)**

Which of the following is **valid JSON**?

A)

```json
{ name: "Alice", age: 30 }
```

B)

```json
{ "name": "Alice", "age": 30 }
```

C)

```json
{ "name": "Alice", "age": True }
```

D)

```json
{ "name": "Alice", "age": None }
```

**Correct answer:** B

**Explanation:**
In JSON, keys must be strings enclosed in double quotes, and boolean values must be lowercase (`true`/`false`). `None` is not valid in JSON; `null` is used instead.

---

### **4. (MCQ)**

What is the primary difference between `json.dumps()` and `json.dump()` in Python?

A) One parses JSON, the other validates it
B) One writes to a file, the other returns a JSON string
C) One works with arrays, the other with objects
D) One handles nested JSON, the other does not

**Correct answer:** B

**Explanation:**
`json.dumps()` converts Python objects into a JSON-formatted **string**, while `json.dump()` writes JSON directly to a file object.

---

### **5. (MCQ)**

What does `json.loads()` do?

A) Converts a Python dictionary into JSON
B) Writes JSON to disk
C) Parses a JSON string into Python objects
D) Validates JSON schema

**Correct answer:** C

**Explanation:**
`json.loads()` takes a JSON-formatted string and parses it into equivalent Python objects (typically dictionaries and lists).

---

### **6. (MCQ)**

Given the following parsed JSON, how do you access the value `"Alice"`?

```python
data = {
  "user": {
    "profile": {
      "name": "Alice"
    }
  }
}
```

A) `data["name"]`
B) `data["user"]["name"]`
C) `data["profile"]["name"]`
D) `data["user"]["profile"]["name"]`

**Correct answer:** D

**Explanation:**
Nested JSON objects must be accessed step by step, following the hierarchy exactly. Each level corresponds to another dictionary lookup in Python.

---

### **7. (MCQ)**

Why is nested JSON common in real-world APIs?

A) It reduces file size
B) It improves execution speed
C) It represents complex, hierarchical relationships
D) It avoids using arrays

**Correct answer:** C

**Explanation:**
Real-world data often contains hierarchical relationships (users → profiles → roles). Nested JSON mirrors this structure cleanly and understandably.

---

### **8. (MCQ)**

Why is blindly accessing deeply nested JSON keys risky in production systems?

A) It slows down the program
B) JSON parsing may fail silently
C) Keys may be missing or structured differently
D) JSON does not support nesting

**Correct answer:** C

**Explanation:**
API responses and agent messages may vary. Assuming all keys always exist can cause runtime errors. Robust systems validate or check JSON structures before accessing deeply nested values.

---

