## Implement String Data Types

---

<div align="center">

![Python String Character Indexing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.5.png)

*Strings are immutable sequences of characters — Python provides rich methods for slicing, searching, and transforming text*

</div>

---

## Understanding Strings

### Why "String"?
"String" means "string of characters" — like beads on a string. It's a **sequence** of characters:
"Hello" = ['H', 'e', 'l', 'l', 'o']

### From Numbers to Text
Each character is assigned a number (character encoding):
- **ASCII** (1960s): 128 characters (English, digits, symbols)
- **Unicode** (1991): 1 million+ characters (all languages, emoji) 😊
Python 3 uses Unicode by default, e.g., `message = "Hello 世界 🌍"`.

### Strings Are Immutable
Once created, strings cannot be changed. Any "modification" creates a **new** string:
```python
name = "Alice"
name = name.upper()  # Creates new string "ALICE"
```
**Why immutable?** Safety, efficiency, and allows use as dictionary keys.

## Creating Strings

### Using Quotes
```python
name = 'Alice'       # Single quotes
message = "Hello!"   # Double quotes
```

### Quotes Inside Strings
```python
text1 = "He said, 'Hello!'"
text2 = 'She said, "Hi!"'
text3 = "He said, \"Hello!\"" # Escape with backslash
```

### Multi-line Strings
```python
long_text = """This is a
multi-line string."""
```

---

## String Operations

### Concatenation (+)
```python
first = "Hello"
second = "World"
result = first + " " + second # "Hello World"

age = 25
message = "Age: " + str(age) # ✅ Convert number to string
```

### Repetition (*)
```python
laugh = "ha" * 3    # "hahaha"
line = "=" * 20   # "=================="
```

### Length
```python
name = "Alice"
length = len(name) # 5
```

---

## String Methods

### Case Conversion
```python
name = "Alice"
print(name.upper())  # "ALICE"
print(name.lower())  # "alice"
```

### Strip Whitespace
```python
text = "  hello  "
print(text.strip())  # "hello"
```

### Replace
```python
text = "Hello World"
new_text = text.replace("World", "Python") # "Hello Python"
```

### Check Contents
```python
email = "user@example.com"
print(email.startswith("user"))  # True
print("@" in email)              # True
```

---

## Practical Examples

### Example 1: Full Name
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name # "Alice Johnson"
```

### Example 2: Email Creation
```python
username = "alice"
domain = "example.com"
email = username + "@" + domain # "alice@example.com"
```

---

## Key Takeaways
1. Strings are text in quotes.
2. Use `+` to concatenate, `*` to repeat.
3. Convert numbers to strings (`str()`) before concatenating.
4. Many useful string methods (e.g., `upper()`, `lower()`, `strip()`, `replace()`).
5. Use `len()` to get length.

---

## Creating and Initializing Dictionaries for Key-Value Pairs

---

## Introduction

Dictionaries are Python's implementation of **hash maps** (or associative arrays) — a fundamental data structure for organizing data by **meaning** (keys) instead of position. They provide **O(1)** (constant time) average lookup speed.

---

<div align="center">

![Python Dictionary Key-Value Pairs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.18.png)

*Dictionaries are hash tables — keys are hashed to array indices for O(1) access to their associated values*

</div>

---

### Why Dictionaries Are Revolutionary

**Before dictionaries** (positional thinking):
```python
student = ['Alice', 22, 'A', 'alice@email.com']
# What's index 2? Grade or email? Fragile and error-prone!
```

**With dictionaries** (semantic thinking):
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A', 'email': 'alice@email.com'}
print(student['grade'])  # Crystal clear! Add/reorder fields without breaking code.
```

**Historical Context**: Concept from SNOBOL (1962), AWK (1977). Python's `dict` (1991) implemented as hash table. Guido van Rossum chose "dictionary" for its intuitive lookup analogy. Python 3.7+ guarantees insertion order.

**Real-World Analogy**: Like a **phonebook** where a person's name (key) instantly gives you their number (value). No need to scan page by page. This O(1) access is how databases and caches work internally.

**Hash Table Foundation**: Keys are **hashed** to an internal array index, allowing direct, constant-time retrieval of values. This is why keys must be immutable (hashable); a mutable key's hash could change, making the value unretrievable.

**Self-Documenting Power**: Dictionaries make code inherently clearer, explaining the purpose of each data piece without extra comments.
```python
config = {'debug': True, 'database': 'postgresql', 'port': 5432}
# Clearly understandable without comments.
```

---

### What Is a Dictionary?

A **dictionary** stores data as **key-value pairs**.

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
```

**Key Properties:**
1.  **Key-value pairs** — every entry has a key and a value.
2.  **Keys must be unique** — duplicate keys overwrite previous values.
3.  **Keys must be immutable** — strings, numbers, tuples are valid.
4.  **Values can be anything** — strings, lists, other dicts, etc.
5.  **Ordered** (Python 3.7+) — insertion order is preserved.

---

### Creating Dictionaries

**Method 1: Curly Braces (Most Common)**
```python
person = {'name': 'Alice', 'age': 25}
scores = {1: 'Gold', 2: 'Silver'}
```

**Method 2: `dict()` Constructor**
```python
person = dict(name='Alice', age=25) # Keyword arguments
person = dict([('name', 'Alice'), ('age', 25)]) # From list of tuples
```

**Method 3: Empty Dictionary**
```python
empty = {} or dict()
```

---

### Dictionary Comprehension

Create dictionaries with a compact expression:
```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### `dict.fromkeys()` — Same Value for Multiple Keys

```python
subjects = dict.fromkeys(['Math', 'Science', 'English'], 0)
# {'Math': 0, 'Science': 0, 'English': 0}
```

---

### Keys Must Be Unique

Using the same key twice overwrites the previous value:
```python
data = {'a': 1, 'b': 2, 'a': 3}
print(data)  # {'a': 3, 'b': 2}
```

---

### What Can Be Keys?

**Valid keys (immutable):** strings, ints, floats, tuples.
```python
d = {'name': 'Alice', 42: 'answer', (1, 2): 'coordinates'}
```

**Invalid keys (mutable):** lists, sets, other dictionaries.
```python
# d = {[1, 2]: 'list'} # TypeError
```

---

### Nested Dictionaries

Dictionaries can store other dictionaries as values, forming hierarchical structures.

```python
students = {
    'Alice': {'age': 22, 'grade': 'A'},
    'Bob': {'age': 24, 'grade': 'B'}
}

print(students['Alice']['grade'])      # 'A'
```

---

### Practical Examples

**Word Frequency Counter:**
```python
text = "the cat sat on the mat the cat"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```

---

### Quick Reference

| Method | Example | Result |
|--------|---------|--------|
| Literal | `{'a': 1, 'b': 2}` | Dict with 2 pairs |
| `dict()` | `dict(a=1, b=2)` | Same as above |
| From tuples | `dict([('a',1), ('b',2)])` | Same as above |
| Comprehension | `{x: x**2 for x in range(3)}` | `{0:0, 1:1, 2:4}` |
| `fromkeys()` | `dict.fromkeys(['a','b'], 0)` | `{'a':0, 'b':0}` |
| Empty | `{}` or `dict()` | Empty dict |

---

### Key Takeaways

1.  Dictionaries store **key-value pairs** for structured data.
2.  Multiple creation methods: `{}`, `dict()`, comprehensions, `fromkeys()`.
3.  Keys must be **unique** and **immutable**.
4.  Values can be **any type**.
5.  Order is **preserved** (Python 3.7+).
6.  Perfect for **structured data**, **lookups**, and **configurations**.

---

## Accessing Dictionary Values Using Keys and get() Method

---

## Introduction

`[]` vs `.get()` is about **fail-fast vs. fail-safe** error handling.

---

<div align="center">

![Python Dictionary get() Method Access](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.19.png)

*dict[key] and dict.get(key) both look up values by hashing the key — the difference is how they handle missing keys*

</div>

---

### Why Two Access Methods? Design Philosophy

**`dict[key]` = Fail-Fast:**
- Key **MUST** exist! Missing key → `KeyError`.
- Use during **development** to catch bugs immediately.

**`dict.get(key, default)` = Fail-Safe:**
- Key **might not** exist. Missing key → returns `default` value.
- Use in **production** for graceful degradation.

**Analogy**: `[]` is a **strict vending machine** (crashes if item missing). `.get()` is a **friendly assistant** (offers default if item missing).

### The Graceful Degradation Pattern

**Fragile code without `.get()`:**
```python
config = {'theme': 'dark'}
# font_size = config['font_size']  # KeyError!
if 'font_size' in config: font_size = config['font_size']
else: font_size = 14 # default
```

**Elegant code with `.get()`:**
```python
config = {'theme': 'dark'}
font_size = config.get('font_size', 14)
# One line! Missing key? Use 14.
```

### The Word Counting Pattern

```python
word_count = {}
words = ['apple', 'banana', 'apple']
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
# .get(word, 0) returns 0 if new word
```

---

### Accessing with Square Brackets `[]`

```python
student = {'name': 'Alice'}
print(student['name'])   # Alice
# print(student['email'])  # KeyError: 'email' (crashes!)
```

---

### Accessing with `.get()` — Safe Access

```python
student = {'name': 'Alice'}
print(student.get('name'))    # Alice
print(student.get('email'))   # None — no crash!
print(student.get('email', 'not set'))  # 'not set' — custom default
```

`get(key, default)` returns the value if key exists, `default` (or `None`) if not.

---

### When to Use `[]` vs `.get()`

| Situation | Use | Why |
|-----------|-----|-----|
| Key is guaranteed to exist | `dict[key]` | Clear, direct |
| Key might not exist | `dict.get(key, default)` | Avoids KeyError, handles defaults |

---

### Accessing All Keys, Values, and Items

```python
student = {'name': 'Alice', 'age': 22}
print(student.keys())    # dict_keys(['name', 'age'])
print(student.values())  # dict_values(['Alice', 22])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22)])
```

Convert to lists: `list(student.keys())`

---

### Checking if a Key Exists

```python
student = {'name': 'Alice'}
if 'name' in student: print(student['name'])

key = 'email'
if key in student: print(student[key])
else: print(f"'{key}' not found")
```
`in` checks **keys**, not values: `'Alice' in student` is `False`.

---

### Accessing Nested Dictionaries

```python
data = {'user': {'name': 'Alice', 'address': {'city': 'Mumbai'}}}

print(data['user']['name'])            # Alice

# Safe nested access:
city = data.get('user', {}).get('address', {}).get('city', 'Unknown')
print(city)  # Mumbai

phone = data.get('user', {}).get('phone', {}).get('number', 'N/A')
print(phone) # N/A (path doesn't exist)
```

---

### Practical Examples

**User Profile with Defaults:**
```python
profile = {'name': 'Alice', 'theme': 'dark'}
name = profile.get('name', 'Guest')
lang = profile.get('language', 'en')
print(f"Welcome {name}! Language: {lang}") # Welcome Alice! Language: en
```

---

### Key Takeaways

1.  `dict[key]` — direct access, raises `KeyError` if key missing
2.  `dict.get(key)` — safe access, returns `None` if key missing
3.  `dict.get(key, default)` — safe access with custom fallback
4.  Use `in` to check if a **key** exists
5.  `.keys()`, `.values()`, `.items()` give views of dictionary contents
6.  Chain `.get()` for safe nested dictionary access

---

## Adding and Modifying Dictionary Entries

Dictionary modification showcases **mutable mapping** design: `dict[key] = value` performs an **upsert** (update if key exists, insert if new), making it context-sensitive.

<div align="center">

![Python Dictionary Add Update Key Value Pair](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.20.png)

*`dict[key] = value` performs an upsert: if the key exists, its value is updated; if not, a new entry is inserted*

</div>

### Why Unified Add/Modify Syntax is Elegant
Python's `student['age'] = 23` is simple, clean, and requires no `if`-check. This is **"upsert"** (UPDATE or INSERT) behavior, common in databases.

### Real-World Analogy
**Dict modification is like updating contacts**: Your phone doesn't ask "add or update?" – it just saves the number under a name, adding if new, replacing if existing. Python dicts work the same way.

### The `setdefault()` Design Genius
**Problem**: Initialize a key if missing, otherwise keep its current value.
**Verbose approach**: `if 'count' not in data: data['count'] = 0`.
**Elegant solution**: `data.setdefault('count', 0)`.
**Why brilliant**: It combines **check + set + get** in one atomic, efficient operation. Crucial for grouping and accumulation patterns.

### Adding & Modifying Entries
Use `dict[key] = value`.
- **Adding**: Assign to a new key.
- **Modifying**: Assign to an existing key, overwriting its value.
```python
student = {'name': 'Alice', 'age': 22}
student['grade'] = 'A'  # Add new
student['age'] = 23      # Modify existing
print(student) # {'name': 'Alice', 'age': 23, 'grade': 'A'}
```

### The `update()` Method
Add or modify **multiple** entries at once. Existing keys are overwritten; new keys are added.
```python
student = {'name': 'Alice', 'age': 22}
student.update({'age': 23, 'grade': 'A', 'city': 'Mumbai'})
print(student) # {'name': 'Alice', 'age': 23, 'grade': 'A', 'city': 'Mumbai'}
```

### The `setdefault()` Method
Sets a value **only if the key doesn't already exist**.
```python
config = {'theme': 'dark'}
config.setdefault('theme', 'light')     # Key exists — no change
config.setdefault('language', 'en')   # Key doesn't exist — sets it
print(config) # {'theme': 'dark', 'language': 'en'}
```
**Useful for grouping:**
```python
word_groups = {}
words = ['apple', 'ant', 'banana']
for word in words:
    word_groups.setdefault(word[0], []).append(word)
print(word_groups) # {'a': ['apple', 'ant'], 'b': ['banana']}
```

### The `|=` Operator (Python 3.9+)
Merge another dictionary into the current one, modifying in place. Values from the right-hand dictionary override those from the left.
```python
defaults = {'theme': 'light', 'lang': 'en'}
user_prefs = {'theme': 'dark'}
defaults |= user_prefs
print(defaults)  # {'theme': 'dark', 'lang': 'en'}
```

### Incrementing Values (Counter Pattern)
Common for counters or accumulators using `dict.get()` with a default value.
```python
text = "hello"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Practical Examples
**1. Merging Configurations:**
```python
default_config = {'debug': False, 'port': 3000}
env_config = {'debug': True, 'port': 8080}
final = {**default_config, **env_config} # env overrides defaults
print(final) # {'debug': True, 'port': 8080}
```
**2. Accumulating Data:**
```python
sales = {}
transactions = [('Alice', 100), ('Bob', 200), ('Alice', 150)]
for name, amount in transactions:
    sales[name] = sales.get(name, 0) + amount
print(sales)  # {'Alice': 250, 'Bob': 200}
```

### Summary Table
| Method | Adds New? | Overwrites? | Multiple? |
|--------|-----------|-------------|-----------|
| `d[key] = val` | Yes | Yes | No |
| `d.update(...)` | Yes | Yes | Yes |
| `d.setdefault(key, val)` | Yes | **No** | No |
| `d \|= other` | Yes | Yes | Yes |

### Key Takeaways
1.  `dict[key] = value` — adds or overwrites a single entry.
2.  `dict.update()` — adds/overwrites multiple entries at once.
3.  `dict.setdefault()` — only sets if key is missing (safe initialization).
4.  Use `.get()` with increment for counting patterns.
5.  Use `{**d1, **d2}` or `|=` for merging dictionaries.

---

## Removing Entries Using pop(), popitem(), and del

<div align="center">

![Python Dictionary pop() Remove Entry](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.21.png)

*del removes by key, pop() removes and returns the value, popitem() removes the last inserted pair (LIFO)*

</div>

### Why Multiple Removal Methods?
*   `del` (statement): Low-level, permanent removal by key.
*   `pop()`: Removes and **returns** the value (retrieval + removal).
*   `popitem()`: Removes and returns the **last** inserted key-value pair (LIFO stack behavior).
*   `clear()`: Removes **all** entries, emptying the dictionary.
Each method serves a distinct purpose for different use cases.

### `del` Statement
Removes a specific key-value pair.
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
del student['grade']
print(student)  # {'name': 'Alice', 'age': 22}
```
*   Raises `KeyError` if the key doesn't exist.
*   `del student` removes the entire dictionary object.

### `pop()` Method
Removes and **returns** the value associated with a key.
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
removed_grade = student.pop('grade')
print(removed_grade)  # 'A'
print(student)        # {'name': 'Alice', 'age': 22}
```
*   `student.pop('email', 'not found')` returns `'not found'` if `'email'` is missing, preventing `KeyError`.
*   Without a default, `pop()` raises `KeyError` for missing keys.

### `popitem()` Method
Removes and returns the **last** inserted key-value pair as a tuple.
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
last = student.popitem() # Assuming 'grade' was last inserted
print(last)     # ('grade', 'A')
print(student)  # {'name': 'Alice', 'age': 22}
```
*   Raises `KeyError` if the dictionary is empty.

### `clear()` Method
Removes **all** entries, leaving the dictionary empty but still existing.
```python
student = {'name': 'Alice', 'age': 22}
student.clear()
print(student)  # {}
```

### Comparison Table
| Method | Returns Value? | Key Required? | Error if Missing? |
|--------|---------------|---------------|-------------------|
| `del d[key]` | No | Yes | Yes (KeyError) |
| `d.pop(key)` | Yes | Yes | Yes (unless default given) |
| `d.pop(key, default)` | Yes (or default) | Yes | No |
| `d.popitem()` | Yes (last pair) | No | Yes (if empty) |
| `d.clear()` | No | No | No |

### Safe Deletion Patterns
*   **Safe removal of multiple keys:** Iterate and use `pop(key, None)`.
    ```python
data = {'a': 1, 'b': 2, 'c': 3}
keys_to_remove = ['b', 'd']
for key in keys_to_remove:
    data.pop(key, None) # 'd' is ignored, no error
print(data) # {'a': 1, 'c': 3}
    ```
*   **Filter and remove:** Collect keys/items to remove first, then delete.
    ```python
scores = {'Alice': 92, 'Bob': 45}
failing = [name for name, score in scores.items() if score < 50]
for name in failing:
    del scores[name]
print(scores) # {'Alice': 92}
    ```
*   **Crucial:** Never modify a dictionary while iterating over its keys directly. Always collect keys/items to remove first.

### Key Takeaways
1.  `del d[key]` — simple, no return, errors on missing key.
2.  `pop(key)` — removes, returns value, can use default.
3.  `popitem()` — removes last pair (LIFO).
4.  `clear()` — empties the dictionary.
5.  Use `pop(key, None)` for safe removal without explicit `if` check.
6.  Never modify dict while iterating directly; collect keys first.

---

## Checking for Key Existence Using the 'in' Keyword

## Introduction
The `in` operator provides **O(1) membership testing** for dictionary keys, enabling **defensive programming** to prevent `KeyError` crashes. This is a "look before you leap" (LBYL) approach.

<div align="center">

![Python Dictionary Key Existence Check](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.22.jpg)

*The `in` keyword uses hash lookup — O(1) for dicts/sets vs O(n) for lists, making it ideal for membership checks*

</div>

### The `in` Operator for Dictionaries
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print('name' in student)    # True
print('email' in student)   # False
print('email' not in student)  # True
```
**Important:** `in` checks **keys**, not values.
```python
print('Alice' in student)  # False — 'Alice' is a value, not a key
print('name' in student)   # True — 'name' is a key
```

### Why Check for Keys?
Without checking, accessing a missing key crashes your program:
```python
data = {'x': 10}

# DANGEROUS
# print(data['y'])  # KeyError!

# SAFE — check first
if 'y' in data:
    print(data['y'])
else:
    print("Key 'y' not found")
```

### `in` vs `.get()` vs `try/except`
Three approaches to handle missing keys:

**Approach 1: `in` check**
```python
if 'email' in user:
    email = user['email']
else:
    email = 'N/A'
```

**Approach 2: `.get()` with default**
```python
email = user.get('email', 'N/A')
```

**Approach 3: `try/except`**
```python
try:
    email = user['email']
except KeyError:
    email = 'N/A'
```

**When to use which:**
- `in` — when you need different logic based on existence
- `.get()` — when you just need a value with a fallback
- `try/except` — when `KeyError` is rare (follows EAFP principle)

### Checking Keys in Nested Dicts
For cleaner checks in nested dictionaries, `.get()` is often preferred:
```python
data = {
    'user': {
        'name': 'Alice',
        'settings': {'theme': 'dark'}
    }
}
theme = data.get('user', {}).get('settings', {}).get('theme', 'light')
print(theme)  # 'dark'
```

### Checking Values (Not Keys)
To check if a **value** exists:
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print('Alice' in student.values())  # True
print(22 in student.values())       # True
```

### Common Patterns
**1. Conditional Update:**
```python
config = {'port': 8080}

if 'host' not in config:
    config['host'] = 'localhost'
print(config) # {'port': 8080, 'host': 'localhost'}
```

### Performance
Key lookup with `in` is **O(1)** on average due to dictionaries using hash tables internally.

### Key Takeaways
1. `key in dict` checks if a **key** exists — O(1) operation.
2. `in` does NOT check values — use `val in dict.values()` for that.
3. Use `in` when you need conditional logic based on key existence.
4. Use `.get()` when you just need a fallback value.
5. Always check before `del` or `[]` access to avoid `KeyError`.

---

## Iterating Through Dictionary Keys, Values, and Items

### Introduction
Dictionary iteration provides **three view objects**: `keys`, `values`, or `items` (key-value pairs). These are **live views** into the dictionary, not copies, and update automatically with dictionary changes.

<div align="center">

![Python Dictionary keys() values() items() Iteration](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.23.png)

*.keys() iterates over keys, .values() over values, .items() over (key, value) tuples — three views of the same data*

</div>

### Why Three Iteration Methods?
*   **Keys only** (`.keys()` or default): For identifiers.
*   **Values only** (`.values()`): For aggregating/analyzing data.
*   **Key-value pairs** (`.items()`): For context with each value.

### Dictionary Views Are Live!
Views update automatically:
```python
d = {'a': 1}
view = d.items()
d['b'] = 2  # View now includes 'b': 2
```

### Three Ways to Iterate
```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
```

**1. Iterate over keys (default):**
```python
for key in student:
    print(key)
```

**2. Iterate over values:**
```python
for value in student.values():
    print(value)
```

**3. Iterate over key-value pairs:**
```python
for key, value in student.items():
    print(f"{key}: {value}")
```

### `.keys()` — All Keys
`for key in dict` and `for key in dict.keys()` are identical.
```python
student = {'name': 'Alice', 'age': 22}
for key in student.keys():
    print(key, '->', student[key])
```

### `.values()` — All Values
```python
prices = {'apple': 1.50, 'banana': 0.75}
total = sum(prices.values()) # Total: $2.25
```

### `.items()` — Key-Value Pairs
```python
scores = {'Alice': 92, 'Bob': 78}
for name, score in scores.items():
    print(f"{name}: {score}")
```

### Iterating Over Nested Dictionaries
```python
grades = {'Alice': {'Math': 92}, 'Bob': {'Math': 78}}
for student, subjects in grades.items():
    print(f"\n{student}:")
    for subject, score in subjects.items():
        print(f"  {subject}: {score}")
```

### Building New Dicts While Iterating
*   **Filtering:**
    ```python
scores = {'Alice': 92, 'Bob': 45}
passing = {name: s for name, s in scores.items() if s >= 50}
    ```
*   **Inverting (swap keys/values):**
    ```python
original = {'a': 1, 'b': 2}
inverted = {v: k for k, v in original.items()}
    ```

### Sorted Iteration
Dictionaries preserve insertion order, but you can iterate in sorted order:
```python
data = {'banana': 3, 'apple': 5}
for key in sorted(data): # Sort by key
    print(f"{key}: {data[key]}")
for key in sorted(data, key=data.get): # Sort by value
    print(f"{key}: {data[key]}")
```

### Common Patterns
*   **Find Key with Max/Min Value:**
    ```python
scores = {'Alice': 92, 'Bob': 78}
top = max(scores, key=scores.get)
    ```
*   **Group Items by Value:**
    ```python
students = {'Alice': 'A', 'Bob': 'B'}
groups = {}
for name, grade in students.items():
    groups.setdefault(grade, []).append(name)
    ```

### Key Takeaways
1. `for key in dict` — iterates over keys
2. `for val in dict.values()` — iterates over values only
3. `for key, val in dict.items()` — iterates over pairs (most flexible)
4. Use comprehensions to filter/transform while iterating
5. Use `sorted()` for ordered iteration
6. Never modify a dict while iterating over it — build a new one instead

---

## Merging Dictionaries Using the update() Method

## Introduction
Dictionary merging, a fundamental software engineering pattern, enables **configuration layering**. This allows settings from sources like defaults, config files, environment variables, and command-line arguments to override each other, establishing precedence. This is how modern applications handle configuration.

<div align="center">

![Python Merge Dictionaries update() Method](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.24.png)

*update() merges two dictionaries — existing keys get overwritten by the new values, new keys are added*

</div>

### Why Merging is Fundamental
**The configuration problem**: Apps need settings from multiple sources with precedence (e.g., defaults < config files < environment variables < command-line args).
**Python's solution**: Layer dictionaries, with later ones overriding earlier ones:
```python
final = {**defaults, **config_file, **env_vars, **cli_args} # Last value wins
```
This pattern powers major Python frameworks.

### The Evolution of Dict Merging
**Python 3.5**: Introduced `{**d1, **d2}` unpacking for clean merging.
**Python 3.9**: Added the `|` operator, offering even cleaner syntax, inspired by set union.

### The `update()` Method
Merges another dictionary (or key-value pairs) into the current dictionary, modifying it in place.

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1) # {'a': 1, 'b': 3, 'c': 4}
```
**Behavior:**
- New keys are **added**.
- Existing keys are **overwritten** (last value wins).
- `d1` is modified in place; `d2` is unchanged.

### Different Ways to Call `update()`
1.  **With another dictionary:** `base.update({'port': 8080})`
2.  **With keyword arguments:** `config.update(font_size=14)`
3.  **With a list of tuples:** `data.update([('name', 'Alice')])`

### Merging Without Modifying Originals
**Using `{**d1, **d2}` unpacking (Python 3.5+):**
```python
defaults = {'theme': 'light', 'lang': 'en'}
user_prefs = {'theme': 'dark'}
merged = {**defaults, **user_prefs}
print(merged) # {'theme': 'dark', 'lang': 'en'}
print(defaults) # unchanged
```
**Using `|` operator (Python 3.9+):**
```python
merged = defaults | user_prefs # Same result
```
**Using `|=` for in-place merge (Python 3.9+):** `defaults |= user_prefs`

### Merge Priority (Who Wins?)
The **later** dictionary's values take priority:
```python
d1 = {'x': 1, 'y': 2}
d2 = {'y': 20, 'z': 30}
merged = {**d1, **d2}
print(merged) # {'x': 1, 'y': 20, 'z': 30}
```

### Merging Multiple Dictionaries
Multiple dictionaries can be merged, with the last one in the sequence determining the final value for shared keys.
```python
base = {'a': 1}
overrides1 = {'b': 2, 'a': 10}
overrides2 = {'c': 3, 'b': 20}
result = {**base, **overrides1, **overrides2}
print(result) # {'a': 10, 'b': 20, 'c': 3}
```

### Practical Examples
**Configuration Layering:**
```python
# Default < Environment < Command Line
default_config = {'debug': False, 'port': 3000}
env_config = {'port': 8080}
cli_config = {'debug': True}
final_config = {**default_config, **env_config, **cli_config}
print(final_config) # {'debug': True, 'port': 8080}
```

### Comparison Table
| Method | Modifies Original? | Python Version |
|--------|-------------------|----------------|
| `d1.update(d2)` | Yes | All |
| `{**d1, **d2}` | No (new dict) | 3.5+ |
| `d1 \| d2` | No (new dict) | 3.9+ |
| `d1 \|= d2` | Yes | 3.9+ |

### Key Takeaways
1.  `update()` merges a dict in place; later values overwrite earlier ones.
2.  `{**d1, **d2}` and `|` create new merged dicts, preserving originals.
3.  Order dictates priority: the last dict in sequence wins for shared keys.
4.  Merging is **shallow**: nested dicts are replaced entirely.
5.  For custom merge logic (e.g., combining lists, summing values), a dedicated function is required.

---

# Define Classes

## Classes in Python
A class is a blueprint for creating objects, defining their structure and behavior.

<div align="center">

![Python Class Blueprint OOP Concept](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.19.png)

*Classes serve as blueprints in Python's type hierarchy, defining the structure for creating objects*

</div>

## Introduction
Classes implement **object-oriented programming (OOP)**, organizing code around objects that combine data and behavior. Classes are **blueprints** that model real-world concepts. This is **abstraction**.

**With OOP** (classes): Data and behavior bundled together (**encapsulation**):
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy", 3)
buddy.bark()
```

### Historical Context
OOP invented by **Simula 67** (1967). **Smalltalk** (1972) popularized "everything is an object".

### Real-World Analogy
**Classes are like cookie cutters**:
- **Class**: Cookie cutter shape (blueprint)
- **Objects**: Actual cookies (instances)
One blueprint, many instances!

---
### Basic Syntax
```python
class ClassName:
    pass
```

### Naming Convention
- **PascalCase** (e.g., `BankAccount`)
- Descriptive names

## Creating a Simple Class
```python
class Dog:
    pass

my_dog = Dog()
print(my_dog)
```

## Adding Methods
```python
class Dog:
    def bark(self):
        print("Woof!")
    
my_dog = Dog()
my_dog.bark()
```

## Real-World Example: Book Class
```python
class Book:
    def open(self):
        print("Opening book...")
    def read_page(self, page_num):
        print(f"Reading page {page_num}")

book = Book()
book.open()
book.read_page(1)
```

## Key Takeaways
1. **`class` keyword**: Defines classes.
2. **PascalCase**: Naming convention.
3. **Blueprint**: Class is template, object is instance.
4. **Methods**: Functions inside classes.
5. **`self`**: First parameter of methods.

---

# Create Objects

## Creating Objects (Instances)
An object is a specific instance of a class. You create multiple objects from a single class definition.

<div align="center">
![Python Class Instantiation Object Creation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.20.png)
</div>

*Creating objects from classes works like a function machine: input parameters, output a new object*

## What is Instantiation?
**Instantiation** is the process of creating a concrete instance (object) from an abstract class blueprint. This defines the **class-instance relationship**.

### Why Instances Matter
Each object (instance) created from a class has:
-   **Unique identity**: A different memory address.
-   **Own state**: Independent data and attribute values.
-   **Shared behavior**: Methods defined by the class.
This ensures **instance independence**.

### Origin & Memory
**Simula 67** (1967) introduced object creation. Python uses `ClassName()` syntax (like a function call). Object creation allocates memory on the **heap**. Python's **garbage collector** automatically reclaims memory from unused objects (using reference counting and cycle detection).

### Analogy: Baking Cookies
-   **Class Cookie**: The recipe or cookie cutter (blueprint).
-   **cookie1, cookie2**: The actual cookies you bake (instances).
-   All follow the same recipe but are unique, individual cookies.

## Syntax
```python
object_name = ClassName(arguments_if_any)
```

## Basic Instantiation Example
```python
class Dog:
    pass

dog1 = Dog()
dog2 = Dog()

print(dog1) # <__main__.Dog object at 0x...>
print(dog2) # <__main__.Dog object at 0x...>
```
Each `Dog()` call returns a new object with a unique memory address.

## Objects Are Independent
Objects maintain their own state. Changing one object doesn't affect another.
```python
class Student:
    def __init__(self, name):
        self.name = name

alice = Student("Alice")
bob = Student("Bob")

alice.name = "Alicia" # Only affects the 'alice' object

print(alice.name) # Alicia
print(bob.name)   # Bob
```

## Objects with Methods
Objects created from a class share the same methods.
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc1 = Calculator()
calc2 = Calculator()

print(calc1.add(5, 3)) # 8
print(calc2.add(10, 2)) # 12
```

## Real-World Example: Bank Accounts
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)

alice_account.deposit(200)
bob_account.withdraw(100)
```

## Creating Objects in a Loop
```python
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1

counters = []
for i in range(3): # Reduced loop for brevity
    counter = Counter(i * 10)
    counters.append(counter)

for i, counter in enumerate(counters):
    counter.increment()
    print(f"Counter {i}: {counter.count}")
# Output:
# Counter 0: 1
# Counter 1: 11
# Counter 2: 21
```

## Storing Objects in Collections
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [
    Product("Laptop", 999),
    Product("Mouse", 25),
    Product("Keyboard", 75) # Reduced items for brevity
]

total_value = 0
for product in products:
    total_value += product.price
print(f"Total inventory value: ${total_value}")
```

## Key Takeaways
1.  **Multiple objects**: Create many instances from one class definition.
2.  **Independent**: Each object has its own unique data/state.
3.  **Same interface**: All objects from the same class share the same methods.
4.  **Memory**: Each object is stored in a separate memory location.
5.  **Collections**: Objects can be stored and managed within lists, dictionaries, etc.

---

# Implement the __init__ Constructor

## The __init__ Method
`__init__` is a special method (constructor) that automatically runs when you create an object.

<div align="center">

![Python __init__ Constructor Method Object](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.21.png)

*The __init__ constructor acts as a function machine, transforming input parameters into initialized object state*

</div>

## Introduction
`__init__` provides constructor functionality, ensuring automatic initialization when objects are created. It's the "object birth certificate", setting initial state before the object enters the world. This is fundamental to RAII (Resource Acquisition Is Initialization) and guaranteed initialization!

### Why __init__ is Revolutionary
**Problem without constructors**: Uninitialized objects are dangerous:
```python
# DANGER - forgot to initialize!
dog = Dog()
print(dog.name)  # AttributeError - name doesn't exist!
```
**Solution with __init__**: Guaranteed initialization:
```python
# SAFE - always initialized!
class Dog:
    def __init__(self, name):
        self.name = name  # Must provide name
dog = Dog("Buddy")  # Cannot create without name!
print(dog.name)  # Always works!
```
`__init__` ensures objects are born complete, never broken!

### Historical Context
Constructors were invented by **Simula 67** (1967). Python's `__init__` is technically an **initializer** (not a constructor) — `__new__` creates the object, `__init__` initializes it. This two-phase construction is invoked automatically when you create an object.

### Real-World Analogies
`__init__` is like a **birth certificate**: An object is created (`__new__`), then `__init__` records its initial data (name, etc.), giving it a complete identity.

### Constructor vs Regular Method
**Regular methods**: Called manually, e.g., `obj.setup()`. This can be forgotten.
**Constructor (`__init__`)**: Called automatically when the object is created, e.g., `obj = MyClass()`. This guarantees initialization.

### Syntax
```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value
```

## Why Use __init__?
1.  **Initialize attributes**: Set starting values for an object.
2.  **Automatic execution**: Runs when object is created.
3.  **Required data**: Ensure objects start with necessary data.

## Basic Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 25)
print(alice.name)  # Alice
print(alice.age)   # 25
```

## Without __init__ vs With __init__
```python
# Without __init__
class Dog:
    pass
dog = Dog()
dog.name = "Buddy"  # Must set attributes manually
dog.breed = "Labrador"

# With __init__
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
dog = Dog("Buddy", "Labrador") # Attributes set automatically
print(dog.name)   # Buddy
print(dog.breed)  # Labrador
```

## The self Parameter
`self` refers to the object being created:
```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand  # THIS object's brand
        self.year = year    # THIS object's year

car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2021)
print(car1.brand)  # Toyota (car1's brand)
print(car2.brand)  # Honda (car2's brand)
```

## Real-World Example: Bank Account
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        print(f"Account created for {owner} with balance ${balance}")

account = BankAccount("Alice", 1000)
# Output: Account created for Alice with balance $1000
print(account.owner)        # Alice
print(account.balance)      # 1000
```

## Validation in __init__
```python
class Person:
    def __init__(self, name, age):
        if age < 0:
            print("Age cannot be negative!")
            self.age = 0
        else:
            self.age = age
        
        if not name:
            print("Name cannot be empty!")
            self.name = "Unknown"
        else:
            self.name = name

person1 = Person("Alice", 25)
print(person1.name, person1.age)  # Alice 25
person2 = Person("Bob", -5)
# Output: Age cannot be negative!
print(person2.name, person2.age)  # Bob 0
```

## Computing Values in __init__
```python
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.salary = hourly_rate * hours_worked # Computed attribute
    
    def info(self):
        print(f"{self.name}: ${self.salary} ({self.hours_worked}hrs @ ${self.hourly_rate}/hr)")

emp = Employee("Alice", 25, 40)
emp.info()  # Alice: $1000 (40hrs @ $25/hr)
```

## __init__ with No Parameters
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

counter = Counter()
counter.increment()
print(counter.get_count())  # 1
```

## Common Mistakes

### Forgetting self in assignment
```python
# Wrong
class Dog:
    def __init__(self, name):
        name = name  # Doesn't save to object!
# Correct
class Dog:
    def __init__(self, name):
        self.name = name  # Saves to object
```

### Forgetting self parameter
```python
# Wrong
class Cat:
    def __init__(name):  # Missing self!
        self.name = name
# Correct
class Cat:
    def __init__(self, name):
        self.name = name
```

### Wrong indentation
```python
# Wrong
class Person:
def __init__(self, name): # Not indented!
    self.name = name
# Correct
class Person:
    def __init__(self, name):
        self.name = name
```

## Key Takeaways
1.  **`__init__`**: Constructor method, runs automatically.
2.  **`self`**: First parameter, refers to the object.
3.  **Initialize attributes**: Set starting values.
4.  **Automatic**: Called when creating object.
5.  **Required data**: Use parameters to require necessary data.
6.  **Default values**: Can provide default parameter values.
7.  **Validation**: Can validate data in `__init__`.