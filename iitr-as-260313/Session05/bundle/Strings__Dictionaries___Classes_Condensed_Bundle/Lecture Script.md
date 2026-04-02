## LO–9.1.5: Implementing string data types for text (15 minutes)

### Implement String Data Types

### CS Theory Bite
> **Origin**: Text encoding evolved from **ASCII** (1963, 128 characters) to **Unicode** (1991, 150K+ characters). Python 3 strings are Unicode by default — supporting every human language.
>
> **Analogy**: A string is like a **necklace of letter beads** — each character is one bead, and you can slice, count, or rearrange them.
>
> **Why it matters**: Strings are everywhere — user input, file content, API responses, database records all flow as text.

### Hook
**Say**: "Every app you use has text - usernames, messages, posts. In Python, that's all strings!"
```python
username = "alice_2024"
message = "Hello World!"
```

### String Basics
**Say**: "Strings are text in quotes. Use single or double quotes - both work the same!"
```python
name = "Alice"
city = 'New York'
print(type(name)) # <class 'str'>
```
**Key Points**:
- Strings use "" or ''
- Must match opening and closing quotes
- Use opposite quotes inside: "She said 'Hi'"

**String Concatenation**:
**Say**: "Combine strings with the `+` operator."
```python
first = "John"
last = "Doe"
full_name = first + " " + last  # John Doe
print(full_name)
```

### String Methods
**Say**: "Strings have built-in methods to modify and check text. These are super useful for data cleaning!"
```python
name = "alice"
print(name.upper())      # ALICE

text = "  hello  "
print(text.strip())      # hello (removes spaces)

email = "USER@EXAMPLE.COM"
print(email.lower())     # user@example.com
```
**Say**: "Always lowercase emails before saving to a database!"

### Practice
**Say**: "Let's build an email address from parts."
```python
first = "john"
last = "doe"
domain = "example.com"

# Solution using concatenation
email = first + "." + last + "@" + domain
print(email)  # john.doe@example.com

# Better way with f-string
email = f"{first}.{last}@{domain}"
print(email)
```

---

## LO–9.2.18: Creating and initializing dictionaries for key value pairs (8 minutes)

## Creating and Initializing Dictionaries

---

### CS Theory Bite

> **Origin**: Dictionaries implement **hash maps** — the most important data structure in computing. They provide O(1) constant time access. **Python 3.7+** guarantees insertion order.
>
> **Analogy**: Like a **real dictionary** — look up a word (key) and instantly find its definition (value).

### Hook

Imagine storing student data: name, age, grade. With lists:

```python
student = ['Alice', 22, 'A', 'alice@mail.com']
# What is student[2]? Hard to remember!
```

With a dictionary, we give data **meaning** through labels:

```python
student = {
    'name': 'Alice',
    'age': 22,
    'grade': 'A',
    'email': 'alice@mail.com'
}
print(student['grade'])  # 'A' — clear and readable!
```

Dictionaries make your data self-documenting.

---

### Creating Dictionaries

**Curly Braces**
```python
person = {'name': 'Alice', 'age': 25}
medals = {1: 'Gold', 2: 'Silver'}
empty = {}
```

**`dict()` Constructor**

Use keyword arguments (keys must be valid variable names):
```python
person = dict(name='Alice', age=25)
```

Or from a list of tuples:
```python
person = dict([('name', 'Alice'), ('age', 25)])
```

---

### Comprehensions and fromkeys

**Dictionary Comprehension:** Quickly create dictionaries.
```python
# Numbers to their squares
squares = {n: n**2 for n in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**`fromkeys()`** for multiple keys with the same initial value:
```python
subjects = dict.fromkeys(['Math', 'Science', 'English'], 0)
# {'Math': 0, 'Science': 0, 'English': 0}
```

---

### Keys and Values Rules

**Keys must be unique:** If a key is repeated, the last value assigned to it wins.
```python
d = {'x': 1, 'y': 2, 'x': 3}
print(d)  # {'x': 3, 'y': 2} — 'x': 1 was overwritten
```

**Keys must be immutable:** This means they cannot change. Strings, numbers, and tuples are valid keys.
```python
ok = {'name': 1, 42: 2, (1,2): 3} # Valid
# bad = {[1,2]: 3} # TypeError: Lists are mutable, cannot be keys
```

**Values can be anything:** Lists, other dictionaries, numbers, booleans, etc.
```python
data = {
    'name': 'Alice',
    'scores': [85, 92, 78],
    'address': {'city': 'Mumbai'},
    'active': True
}
```

---

### Nested Dictionaries

Dictionaries can contain other dictionaries to store hierarchical data.

```python
company = {
    'engineering': {
        'Alice': {'role': 'Lead', 'salary': 120000},
    },
    'marketing': {
        'Charlie': {'role': 'Manager', 'salary': 100000}
    }
}

# Access a nested value
print(company['engineering']['Alice']['role'])  # 'Lead'
```

---

### Practical Uses

Dictionaries are perfect for counting items:

```python
text = "apple banana apple cherry banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

---

### Summary

1.  Dictionaries store **key-value pairs** for labeled, structured data.
2.  Create them with `{}`, `dict()`, comprehensions, or `fromkeys()`.
3.  Keys must be **unique** and **immutable**.
4.  Values can be **any type**, including lists and nested dicts.
5.  They are fundamental for structured data in Python, enabling clear, efficient lookups.

---

## LO–9.2.19: Accessing dictionary values using keys and get method (8 minutes)

## Accessing Dictionary Values

---

### CS Theory Bite

Key access uses **hash functions** for O(1) lookup. `get()` was added for **safe access** — returns a default instead of raising `KeyError`. This is the **LBYL** (Look Before You Leap) approach.

**Analogy**: Direct access `d[key]` is like **demanding a file** — crashes if it doesn't exist. `d.get(key)` is like **politely asking** — returns `None` if unavailable.

---

### Hook

Your app receives user data:

```python
user_data = {'name': 'Alice', 'age': 25}
email = user_data['email']  # CRASH! KeyError: 'email'
```

This stops your program. The solution is `.get()`:

```python
email = user_data.get('email', 'no-email@default.com')
# No crash, has a sensible default
```

---

### Section 1: Square Bracket Access

```python
student = {'name': 'Alice', 'age': 22}
print(student['name'])   # Alice
# print(student['email'])  # KeyError: 'email'
```
Use `[]` when you're **certain** the key exists.

---

### Section 2: The .get() Method

```python
student = {'name': 'Alice', 'age': 22}
print(student.get('name'))    # Alice
print(student.get('email'))   # None
print(student.get('email', 'N/A'))     # N/A
```

**Common pattern — counting:**
```python
counts = {}
words = ['apple', 'banana', 'apple']
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'apple': 2, 'banana': 1}
```

---

### Section 3: Checking Key Existence

```python
data = {'x': 10, 'y': 20}
print('x' in data)   # True
print(10 in data)    # False — checks keys, not values!

if 'z' in data:
    print(data['z'])
else:
    print("z not found")
```

---

### Section 4: keys(), values(), items()

```python
person = {'name': 'Alice', 'age': 25}

for key in person.keys():
    print(key)  # name, age

for val in person.values():
    print(val)  # Alice, 25

for key, val in person.items():
    print(f"{key}: {val}")
```

---

### Section 5: Nested Access

```python
data = {'user': {'name': 'Alice', 'settings': {'theme': 'dark'}}}

print(data['user']['settings']['theme'])  # dark

theme = data.get('user', {}).get('settings', {}).get('theme', 'light')
print(theme)  # dark
```

---

### Summary

1.  `dict[key]` — fast but crashes on missing keys
2.  `dict.get(key, default)` — safe, returns default for missing keys
3.  `key in dict` — checks key existence
4.  `.keys()`, `.values()`, `.items()` — iterate over contents
5.  Chain `.get()` for safe nested access

---

## LO–9.2.20: Adding and modifying dictionary entries (8 minutes)

## Adding and Modifying Dictionary Entries

### CS Theory Bite
Dict insertion and update are O(1) average. Python dicts use **dynamic resizing**: when the load factor exceeds ~2/3, the hash table doubles and rehashes all entries.

**Analogy**: Adding to a dict is like **filing a document**. Updating is like **replacing the document**. Dicts are mutable; build them incrementally.

### Hook
Imagine a user registration system where user data grows and changes:
```python
user = {}
user['name'] = 'Alice'          # Add
user['email'] = 'alice@mail.com'
user['plan'] = 'free'

user['plan'] = 'premium'        # Modify
```
Dictionaries evolve just like real data. Let's explore how to add and modify entries.

### Section 1: Basic Assignment
```python
d = {'a': 1}

# Add new key
d['b'] = 2
print(d)  # {'a': 1, 'b': 2}

# Modify existing key
d['a'] = 10
print(d)  # {'a': 10, 'b': 2}
```
The same `d[key] = value` syntax handles both adding new keys and modifying existing ones.

### Section 2: update()
Use `update()` to add or modify multiple entries at once:
```python
user = {'name': 'Alice'}

# Update with another dictionary
user.update({'age': 25, 'city': 'Mumbai', 'name': 'Alice B.'})
print(user)  # {'name': 'Alice B.', 'age': 25, 'city': 'Mumbai'}

# Or with keyword arguments
user.update(email='alice@mail.com')
```

### Section 3: setdefault()
`setdefault(key, value)` sets a value *only if* the key doesn't exist yet.
```python
config = {'port': 8080}

config.setdefault('port', 3000)    # Key exists — no change
config.setdefault('host', 'localhost')  # Key missing — sets it

print(config)  # {'port': 8080, 'host': 'localhost'}
```
**Killer use case — grouping data:**
```python
words = ['apple', 'ant', 'banana', 'avocado', 'berry']
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)
# {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'berry']}
```

### Section 4: Counter Pattern
The most common dict modification pattern for counting or accumulating:
```python
text = "the cat sat on the mat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
```

### Section 5: Merging Dicts
```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Unpacking (creates new dict; d2 overrides d1 for 'b')
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# |= operator (modifies d1 in place, Python 3.9+; d2 overrides d1)
d1 |= d2
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Summary
1.  `d[key] = value` — add or overwrite one entry.
2.  `d.update(...)` — add/overwrite multiple at once.
3.  `d.setdefault(key, val)` — set only if key is new.
4.  `.get(key, 0) + 1` — the counter pattern.
5.  `{**d1, **d2}` or `d1 |= d2` — merge dicts (last dictionary wins for duplicate keys).

---

## LO–9.2.21: Removing entries using pop popitem and del (8 minutes)

## Removing Dictionary Entries

### CS Theory Bite
`pop()` returns the removed value (useful for processing), `del` just removes (faster). `popitem()` removes the last inserted pair — useful for **stack-like** dict processing (LIFO since Python 3.7). Choose the right method based on whether you need the removed value.

### Hook
You're processing user data and need to remove sensitive fields:
```python
user = {'name': 'Alice', 'email': 'alice@mail.com', 'password': 'secret123', 'credit_card': '4111-1111-1111-1111'}
safe_user = user.copy()
safe_user.pop('password', None)
safe_user.pop('credit_card', None)
print(safe_user)  # {'name': 'Alice', 'email': 'alice@mail.com'}
```
Removing entries is as important as adding them. Let's learn every way.

### Section 1: del Statement
Use `del` to remove a specific key-value pair:
```python
d = {'a': 1, 'b': 2, 'c': 3}
del d['b']
print(d)  # {'a': 1, 'c': 3}
```
Attempting to delete a missing key raises `KeyError`. A safe pattern is `if 'z' in d: del d['z']`.

### Section 2: pop() Method
`pop()` removes a key-value pair and **returns** the removed value:
```python
d = {'a': 1, 'b': 2, 'c': 3}
val = d.pop('b')
print(val)  # 2
print(d)    # {'a': 1, 'c': 3}
```
Use a default value to prevent `KeyError` if the key is missing: `val = d.pop('z', -1)`. `pop()` is preferred when you need the removed value or want safe removal.

### Section 3: popitem()
`popitem()` removes and returns the **last** inserted key-value pair as a tuple:
```python
d = {'x': 10, 'y': 20, 'z': 30}
pair = d.popitem()
print(pair)  # ('z', 30)
print(d)     # {'x': 10, 'y': 20}
```
You can process all items in LIFO order using a `while d:` loop with `popitem()`.

### Section 4: clear()
`clear()` removes **all** entries from the dictionary, leaving it empty:
```python
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()
print(d)  # {}
```
The dictionary object still exists, it's just empty.

### Section 5: Practical Patterns
**Remove multiple keys safely:**
```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in ['b', 'd', 'f']:
    data.pop(key, None) # Ignores 'f' which is missing
print(data)  # {'a': 1, 'c': 3}
```
**Filter by condition (collect then remove):**
```python
scores = {'Alice': 90, 'Bob': 40, 'Charlie': 75}
failing = [k for k, v in scores.items() if v < 50]
for k in failing:
    del scores[k]
print(scores)  # {'Alice': 90, 'Charlie': 75}
```
**Never modify a dictionary while iterating directly:**
```python
# WRONG (RuntimeError): for k in d: if condition: del d[k]
# RIGHT: to_remove = [k for k in d if condition(k)]; for k in to_remove: del d[k]
```

### Summary
| Method | Use When |
|--------|----------|
| `del d[key]` | Simple removal, don't need the value, key must exist |
| `d.pop(key, default)` | Need the value or want safe removal |
| `d.popitem()` | Processing items one at a time (LIFO) |
| `d.clear()` | Reset the entire dictionary |

---

## LO–9.2.22: Checking for key existence using the in keyword (8 minutes)

## Checking for Key Existence

### CS Theory Bite
The `in` operator checks dict **keys** (not values) using O(1) hash lookup. It's like checking if a word exists in a dictionary's index – instant. Always check before accessing to avoid `KeyError` – or use `get()` for the same safety.

### Hook
Your app gets JSON data; sometimes fields are missing:
```python
response = {'status': 'ok', 'data': {'name': 'Alice'}}
# This crashes:
# print(response['error'])  # KeyError!
```
Data is messy. You need to check for keys before accessing them.

### Section 1: Basic Key Checking
```python
user = {'name': 'Alice', 'age': 25}

print('name' in user)   # True
print('email' in user)  # False

# NOT in
if 'email' not in user:
    print("No email on file")
```
Remember: `in` checks **keys only**, not values.

### Section 2: Keys vs Values
```python
scores = {'Alice': 90, 'Bob': 85}

# Key check
print('Alice' in scores)          # True

# Value check
print(90 in scores.values())      # True
print(90 in scores)               # False — 90 is not a key!
```

### Section 3: Patterns with `in`
**Conditional access:**
```python
if 'email' in user:
    send_notification(user['email'])
else:
    print("Email not found for user.")
```

### Section 4: `in` vs `get()`
```python
# Use 'in' when you need different logic paths
if 'role' in user:
    grant_access(user['role'])
else:
    deny_access()

# Use .get() when you just need a value with fallback
role = user.get('role', 'guest')
print(f"User role: {role}")
```

### Summary
1. `key in dict` — checks if key exists (O(1))
2. `val in dict.values()` — checks if value exists
3. Use `in` for conditional logic, `.get()` for fallback values
4. Always check before `del` or `[]` to prevent `KeyError`

---

## LO–9.2.23: Iterating through dictionary keys values and items (8 minutes)

Today, we'll master dictionary iteration. Python 3's `.keys()`, `.values()`, and `.items()` give you **view objects** — live windows that update with the dictionary. `.items()` is often most useful as it gives you both key and value.

Imagine you have student grades. To analyze them, like generating a report or calculating averages, you need to iterate:

```python
grades = {'Alice': 92, 'Bob': 78, 'Charlie': 85}
for name, score in grades.items():
    status = 'Pass' if score >= 80 else 'Needs work'
    print(f"{name}: {score} - {status}")
```
This shows the power of iterating through key-value pairs. Let's explore the three main ways.

First, **iterating keys**. This is the default when you loop over a dictionary directly, or use `.keys()`.
```python
data = {'a': 1, 'b': 2, 'c': 3}
for key in data: # Default
    print(key, data[key])
# Also: for key in data.keys(): ...
```

Next, **iterating values** using `.values()`. Useful for aggregations.
```python
prices = {'apple': 1.50, 'banana': 0.75, 'cherry': 3.00}
total = sum(prices.values())
print(f"Total price: ${total}")
```

Most powerful is **iterating items** with `.items()`. This gives you both the key and value simultaneously.
```python
user = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
for key, val in user.items():
    print(f"{key}: {val}")
```

You can also **sort** dictionaries by keys or values. For example, to print by sorted keys:
```python
data = {'b': 2, 'a': 1, 'c': 3}
for k in sorted(data):
    print(k, data[k])
```
And for **filtering**, dictionary comprehensions are very efficient.
```python
scores = {'Alice': 92, 'Bob': 78, 'Charlie': 85}
passing = {n: s for n, s in scores.items() if s >= 80}
print(f"Passing scores: {passing}")
```

To wrap up, remember:
1. `for key in dict` for keys.
2. `for val in dict.values()` for values.
3. `for k, v in dict.items()` for key-value pairs – this is often the most flexible.
4. Use `sorted()` for ordered iteration and comprehensions for quick filtering or transforming.

---

## LO–9.2.24: Merging dictionaries using the update method (8 minutes)

## Merging Dictionaries Using update()

### CS Theory Bite
> **Origin**: `update()` merges dicts — later values overwrite earlier ones. **Python 3.9+** added the `|` merge operator: `merged = dict1 | dict2`.
> **Analogy**: `update()` is like **merging two address books** — if both have "Alice", the newer entry wins.
> **Why it matters**: Dict merging is essential for combining configuration, API responses, and default + custom settings.

### Hook
Your app has layered configuration:

```python
defaults = {'debug': False, 'port': 3000, 'host': 'localhost'}
user = {'port': 8080, 'debug': True} # User wants port 8080 and debug on
config = {**defaults, **user}
print(config) # {'debug': True, 'port': 8080, 'host': 'localhost'}
```
User preferences win, defaults fill gaps. This is dictionary merging.

### Section 1: update() Basics
`update()` merges a dictionary's items into another, modifying it in place.

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}
d1.update(d2)
print(d1) # {'a': 1, 'b': 20, 'c': 30}
# d2 values override d1 for shared keys; d2 is unchanged.
```
`update()` can also take keyword arguments or a list of tuples.

### Section 2: Creating New Merged Dicts
To create a new dict without modifying originals:

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}

# Unpacking (Python 3.5+)
merged = {**d1, **d2}
print(merged) # {'a': 1, 'b': 20, 'c': 30}
print(d1)     # d1 is unchanged!

# | operator (Python 3.9+)
merged = d1 | d2 # Same result, cleaner syntax.
```

### Section 3: Merge Priority
Later dictionaries override earlier ones for shared keys.

```python
layer1 = {'x': 1, 'y': 2}
layer2 = {'y': 20, 'z': 30}
layer3 = {'z': 300}
result = {**layer1, **layer2, **layer3}
print(result) # {'x': 1, 'y': 20, 'z': 300}
```

### Section 4: Practical Applications
A key use is **configuration layering**:
```python
final = {**defaults, **env_config, **cli_args}
```
This applies user and environment settings over defaults.

### Section 5: Pitfalls
Merging is **shallow**: Nested dictionaries are replaced, not merged.

```python
d1 = {'settings': {'theme': 'dark', 'lang': 'en'}}
d2 = {'settings': {'theme': 'light'}}
merged = {**d1, **d2}
print(merged) # {'settings': {'theme': 'light'}}
# 'lang' is LOST! The 'settings' dict from d2 fully replaced d1's 'settings'.
```
For deep merging, a custom function or library is needed.

### Summary
1.  `d1.update(d2)`: merges in place, `d2` wins.
2.  `{**d1, **d2}` (or `d1 | d2`): creates new dict, last one wins.
3.  Merge priority: later dicts override earlier ones.
4.  Merging is **shallow**; nested dicts are replaced.
5.  Custom merge logic requires a specific function.

---

## LO–9.3.19: Define classes as object blueprints (10 minutes)

## Define Classes as Object Blueprints

### CS Theory Bite
**Origin**: Classes: **Simula 67** (1967) - first object-oriented language. **Smalltalk** (1972) - "everything is an object".
**Analogy**: A class is a **cookie cutter**; objects are unique cookies from that template.
**Why it matters**: Classes organize code around concepts, making systems manageable.

### Hook
Every Python value is an object. You'll now create your own types:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} says Woof!"

rex = Dog("Rex", "Labrador")
print(rex.bark())  # Rex says Woof!
```

### Section 1: What is a Class?
A class is a blueprint; an object is an instance:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
print(car1.make)   # Toyota
print(type(car1))  # <class '__main__.Car'>
```
Key points: `class` keyword defines the blueprint. `__init__` runs on instance creation. `self` refers to the current instance.

### Section 2: Adding Methods
Methods are functions belonging to a class:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def describe(self):
        return f"{self.width}x{self.height} rectangle"

r = Rectangle(5, 3)
print(r.area())        # 15
print(r.describe())    # 5x3 rectangle
```

### Section 3: Classes vs Dictionaries
Use classes when data needs behavior or validation, unlike dictionaries:
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
print(s.average())  # 87.5
```

### Summary
1. `class` defines a blueprint.
2. `__init__` initializes attributes.
3. `self` refers to the instance.
4. Methods define behavior.
5. Use classes for structured data with behavior.

---

## LO–9.3.20: Create objects from class definitions (10 minutes)

### CS Theory Bite
Object creation, or instantiation, allocates memory on the **heap** and initializes attributes. Python's **garbage collector** automatically frees objects when no longer needed. Think of it like baking a cookie from a cutter – the class defines the shape, each object is a unique cookie with its own toppings.

### Introduction to Instantiation
A class is just a blueprint. To use it, you create objects from it.
```python
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

pet1 = Pet("Buddy", "Dog") # This creates an object!
pet2 = Pet("Whiskers", "Cat")
print(pet1.name, pet2.name)
```
Each call to `Pet()` gives you a new, independent `Pet` object.

### Creating Objects
Calling a class like a function creates a new object, also called an instance.
```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

red = Color(255, 0, 0)
blue = Color(0, 0, 255)

print(red.r)   # 255 (red object's R value)
print(blue.r)  # 0   (blue object's R value, independent)
print(type(red)) # <class '__main__.Color'>
print(isinstance(red, Color)) # True, 'red' is an instance of 'Color'
```
Notice how `red` and `blue` are distinct, each holding its own color values.

### Objects in Collections
Objects seamlessly integrate with Python's data structures like lists and dictionaries.
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [
    Student("Alice", 92),
    Student("Bob", 85),
    Student("Carol", 95),
]

# Sort a list of student objects by their grade
ranked = sorted(students, key=lambda s: s.grade, reverse=True)
for s in ranked:
    print(f"{s.name}: {s.grade}")
```
Here, we have a list of `Student` objects, and we can easily sort them based on their attributes.

### Object Identity vs. Equality
When comparing objects, we consider their identity (are they the *exact same object* in memory?) and their equality (do they have the *same values*?).

By default, Python's `==` operator checks for *identity*, similar to the `is` operator.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2) # A new object, even with same values

print(f"p1 is p2: {p1 is p2}")  # False (they are distinct objects)
print(f"p1 == p2 (default behavior): {p1 == p2}") # False (default == also checks identity)
```
To define *value-based equality*, where objects with the same attribute values are considered equal, we override the `__eq__` method in our class:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Check if 'other' is also a Point and compare its x and y attributes
        if not isinstance(other, Point): # Important for robust comparison
            return NotImplemented
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2) # Still a new, distinct object

print(f"p1 is p2: {p1 is p2}")  # False (still distinct objects in memory)
print(f"p1 == p2 (with __eq__ override): {p1 == p2}") # True (now compares values)
```
So, `is` always checks memory identity, while `==` checks value equality *if* `__eq__` is defined, otherwise it defaults to identity.

### Summary
1.  **Create Objects**: Call a class like a function (`ClassName()`) to get a new instance.
2.  **Independent**: Each object has its own unique attributes.
3.  **Collections**: Objects work seamlessly in lists, dictionaries, and other data structures.
4.  **Identity vs. Equality**: `is` checks if objects are the *exact same object* in memory. `==` checks for *value equality*, which you can customize using the `__eq__` method.

---

## LO–9.3.21: Implement init constructor for initialization (10 minutes)

## Implement __init__ Constructor

### CS Theory Bite
Constructors were invented by **Simula 67** (1967). Python's `__init__` is technically an **initializer** — `__new__` creates the object, `__init__` sets it up. Analogy: `__init__` is like a **birth certificate** — automatically records essential details the moment an object is born. Why it matters: Guaranteed initialization prevents `AttributeError` bugs.

### Hook
The `__init__` method runs automatically when you create an object. It sets up everything the object needs:

```python
class Player:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = level * 100

p = Player("Alice", 5)
print(p.hp)  # 500
```

### Section 1: How __init__ Works
```python
class Dog:
    def __init__(self, name, breed):
        print(f"Creating dog: {name}")
        self.name = name
        self.breed = breed

d = Dog("Rex", "Lab")  # "Creating dog: Rex"
```
Key points:
- `__init__` is called automatically after the object is created.
- `self` is the new object being initialized.
- It should NOT return anything.
- It sets up the object's initial state.

### Section 2: Default Values and Validation
`__init__` can validate inputs and provide default values for parameters.

```python
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        self.area = math.pi * radius ** 2

c = Circle(5)
print(f"Area: {c.area:.2f}")  # Area: 78.54

# Circle(-1)  # ValueError: Radius must be positive
```

Default values make arguments optional:
```python
class Connection:
    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port

c1 = Connection()                        # All defaults
c2 = Connection("db.example.com", 3306)  # Custom host/port
```

### Section 3: Computed and Derived Attributes
`__init__` can compute values and derive attributes from inputs:

```python
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.full = f"{first} {last}"
        self.initials = f"{first[0]}.{last[0]}."

n = FullName("Alice", "Smith")
print(n.full)      # Alice Smith
print(n.initials)  # A.S.
```

### Summary
1. `__init__` initializes the object's state.
2. Use default values for optional parameters.
3. Validate inputs early, raising exceptions for bad data.
4. Compute derived attributes during initialization.
5. Never return a value from `__init__`.