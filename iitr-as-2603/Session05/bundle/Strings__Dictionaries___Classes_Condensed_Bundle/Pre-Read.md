## What are Strings?
**Strings** are text data – any characters enclosed in quotes.

```python
name = "Alice"
message = 'Hello, World!'
```
Single `'` or double `"` quotes both work!

### Why Strings Are Different
Computers only understand numbers. When you write "Hello", it sees numbers (via character encoding). This is why the text character `"5"` is different from the number `5`.

### Simple Analogy
Think of a string like a **necklace**:
- Each character is a bead.
- Beads are strung together in a specific order.
- "Hello" is 5 beads: H-e-l-l-o.

### Why Order Matters
Unlike numbers, string order matters because they represent language:
- "cat" ≠ "act"

## String Operations

### Concatenation (Combining)
```python
first = "Hello"
second = "World"
combined = first + " " + second # "Hello World"
```

### Repetition
```python
laugh = "ha" * 3 # "hahaha"
```

### Length
```python
name = "Alice"
print(len(name)) # 5
```

## Special Characters
```python
# Use opposite quotes inside
message = "He said, 'Hello!'"
# Or escape quotes
message = "He said, \"Hello!\""
```

## When to Use Strings
✅ Names, messages, text, emails, URLs, addresses.

## Try It
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)
```

---

## Creating and Initializing Dictionaries

---

## What Are Dictionaries?

Dictionaries are Python's "smart label maker" — they store data as **key-value pairs**, giving data **meaning** instead of just a position. Instead of remembering `student[2]` is 'grade', you use `student['grade']`.

### Simple Analogy

Think of dictionaries like your **phone's contact list**:
-   **Key**: Person's name ("Mom")
-   **Value**: Phone number, email
-   **Lookup**: Tap "Mom" → instant info! No need to remember Mom is contact #47.

### Why This Changes Everything

**The "magic position" problem** (lists):
```python
student = ['Alice', 22, 'A']
# To get grade, you MUST remember that index 2 is 'A'. Fragile!
```

**The "labeled data" solution** (dicts):
```python
student = {
    'name': 'Alice',
    'age': 22,
    'grade': 'A'
}
print(student['grade']) # Crystal clear! No memorization needed.
```

### The Real-World Connection

**Everything digital uses dictionaries**:
-   **JSON** (internet data format)
-   **Databases** (key-value stores)
-   **Web APIs**
-   **Configuration files**

Even Python internally uses dictionaries to map **variable names** to their values (e.g., `'my_variable'` to `10`).

---

### Quick Example

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
print(student['name'])   # Alice
print(student['grade'])  # A
```

### Why Not Just Use Lists?

Dictionaries provide **self-documenting data**.
```python
# With a list — ambiguous what index 2 means:
student = ['Alice', 22, 'A']
print(student[2])

# With a dict — clear and descriptive:
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
print(student['grade'])
```

---

### Creating Dictionaries

```python
# Method 1: Curly braces (most common)
person = {'name': 'Alice', 'age': 25}

# Method 2: dict() constructor (using keyword arguments)
person = dict(name='Alice', age=25)

# Method 3: Empty dictionary
empty = {}
```

---

### Try This

```python
# Create a dictionary for your favorite book
book = {
    'title': 'Your Book Title',
    'author': 'Author Name',
    'year': 2024,
    'rating': 4.5
}
print(book)
print(book['title'])
```

---

### What to Expect

In the session, you'll delve deeper into creating dictionaries, dictionary comprehensions, rules for keys and values, and more practical applications.

---

## Accessing Dictionary Values

---

## What's the Difference Between `[]` and `.get()`?

Python's **"crash vs. continue"** methods.

### Simple Analogy

-   **`[]` like strict password system**: Wrong password -> "ERROR! Access denied!" (crash).
-   **`.get()` like voice assistant**: Asks for unknown -> "I don't have that. Want the default?" (continue).

### The "Missing Key" Problem

**Using `[]` (crashes!):**
```python
settings = {'theme': 'dark'}
# font_size = settings['font_size']  # KeyError! 💥 Program dies!
```

**Using `.get()` (safe!):**
```python
settings = {'theme': 'dark'}
theme = settings.get('theme', 'light')      # 'dark'
font_size = settings.get('font_size', 14)   # 14 (default!)
# No crashes! Program continues!
```

### When to Use Which?

-   **Use `[]` when**: Key is **guaranteed** to exist. Missing key = bug. (e.g., `required_config['database_url']`)
-   **Use `.get()` when**: Key **might not** exist. Missing key = normal. (e.g., `user_prefs.get('language', 'en')`)

---

### Two Ways to Access Values

```python
student = {'name': 'Alice'}
print(student['name'])  # Alice
print(student.get('name'))    # Alice
print(student.get('email'))   # None (no error!)
print(student.get('email', 'N/A'))  # N/A (custom default)
```

---

### The Problem with `[]`

```python
data = {'x': 10}
# print(data['y'])  # KeyError: 'y' — CRASH!
```

---

### The Solution: `.get()`

```python
data = {'x': 10}
print(data.get('y', 0))  # 0 — safe!
```

---

### Quick Exercise

```python
config = {'port': 8080}

# What does each print?
print(config.get('port', 3000))     # ?
print(config.get('host', 'localhost'))  # ?
```

**Answers:** `8080`, `localhost`

---

## Adding and Modifying Dictionary Entries

### What Does Add/Modify Mean?
Dictionaries use `dict[key] = value` to automatically add a new entry if the key doesn't exist, or update an existing one if it does. This is **one syntax for two operations**.

### Simple Analogy
**Like phone contacts**: Saving "Mom" creates a new contact if she's not there, or updates her existing number if she is. Your phone doesn't require a special "add mode" vs. "update mode". Dicts work identically.

### The "No Error" Magic
Dictionaries are forgiving! Assigning to a non-existent key adds it; assigning to an existing key updates it, **without errors**.
```python
person = {}  # Empty dict
person['name'] = 'Alice' # Add - works!
person['name'] = 'Alice B.' # Modify - works!
# Compare to lists: items[0] = 'x' would raise IndexError if list is empty.
```

### Adding & Modifying
```python
person = {'name': 'Alice'}
person['age'] = 25        # Add new key
person['name'] = 'Alice B.'  # Modify existing key
```

### Multiple Updates
Use `dict.update()` to add or modify several entries at once:
```python
person.update({'city': 'Mumbai', 'email': 'alice@mail.com'})
```

### Safe Setting with `setdefault()`
`setdefault()` only sets a value if the key is not already present. It's useful for providing default values.
```python
config = {'port': 8080}
config.setdefault('port', 3000)      # No change — key exists
config.setdefault('host', 'localhost')  # Added — key was new
print(config) # {'port': 8080, 'host': 'localhost'}
```

### Common Pattern: Counting
This pattern uses `dict.get(key, default_value)` to safely increment counts or accumulate totals.
```python
counts = {}
for item in ['a', 'b', 'a', 'c', 'a']:
    counts[item] = counts.get(item, 0) + 1
print(counts) # {'a': 3, 'b': 1, 'c': 1}
```

### Try This
```python
cart = {}
cart['apple'] = 3
cart['banana'] = 5
cart['apple'] = 10  # What happens?
print(cart)
```
**Answer:** `{'apple': 10, 'banana': 5}` — the value for 'apple' is overwritten.

---

## Removing Dictionary Entries

### Four Ways to Remove
```python
d = {'a': 1, 'b': 2, 'c': 3}

# del — remove by key
del d['a']       # d = {'b': 2, 'c': 3}

# pop() — remove and return value
val = d.pop('b') # val = 2, d = {'c': 3}

# popitem() — remove last inserted pair (LIFO)
pair = d.popitem()  # pair = ('c', 3), d = {}

# clear() — remove all entries
d = {'x': 1, 'y': 2}
d.clear()  # d = {}
```

### Safe Removal
*   `del d[key]` and `d.pop(key)` (without default) raise `KeyError` if the key is missing.
*   Use `d.pop(key, default_value)` for safe removal.
    ```python
d = {'a': 1}
val = d.pop('z', None)  # val = None, no crash
    ```

---

## Checking for Key Existence

**Duration:** 5 minutes

---

### The `in` Keyword
```python
data = {'name': 'Alice', 'age': 25}

print('name' in data)   # True — key exists
print('email' in data)  # False — key doesn't exist
```

---

### Keys vs Values
```python
# 'in' checks KEYS, not values
print('Alice' in data)          # False — Alice is a value
print('Alice' in data.values()) # True — check values explicitly
```

---

### Why It Matters
```python
data = {'x': 10}

# Without checking:
# print(data['y'])  # KeyError — crash!

# With checking:
if 'y' in data:
    print(data['y'])
else:
    print("Not found")
```

---

### Try This
```python
config = {'debug': True, 'port': 8080}
print('debug' in config)    # ?
print(True in config)       # ?
print('host' not in config) # ?
```

**Answers:** `True`, `False`, `True`

---

## Iterating Through Dictionaries

### Three Iteration Methods
```python
d = {'name': 'Alice', 'age': 25}
# Keys
for key in d: print(key)
# Values
for val in d.values(): print(val)
# Both (Key-Value pairs)
for key, val in d.items(): print(key, val)
```

### Most Useful: .items()
Often, you need both the key and its corresponding value:
```python
scores = {'Alice': 90, 'Bob': 80}
for name, score in scores.items():
    print(f"{name} scored {score}")
```

### Try Before Class
```python
prices = {'apple': 1.5, 'banana': 0.75, 'cherry': 3.0}
# What does this print?
for item, price in prices.items():
    if price > 1:
        print(item)
```
**Answer:** `apple` and `cherry`

---

## Merging Dictionaries

### Why Merge Dictionaries?
To combine data from multiple sources, where new data should override old data:
```python
defaults = {'color': 'blue', 'size': 'medium'}
user_choice = {'color': 'red'}
# User choice overrides defaults
final = {**defaults, **user_choice}
print(final) # {'color': 'red', 'size': 'medium'}
```

### Two Main Methods
1.  **`update()` — modifies in place:**
    ```python
    d1 = {'a': 1}
    d1.update({'b': 2})
    print(d1) # {'a': 1, 'b': 2}
    ```
2.  **`{**d1, **d2}` — creates a new dict:**
    ```python
    d1 = {'a': 1}
    d2 = {'b': 2}
    merged = {**d1, **d2} # d1 unchanged
    print(merged) # {'a': 1, 'b': 2}
    ```

### The Rule: Last One Wins
When keys overlap, the value from the last dictionary in the merge operation takes precedence.
```python
d1 = {'x': 1}
d2 = {'x': 99}
print({**d1, **d2}) # {'x': 99} (d2 wins)
print({**d2, **d1}) # {'x': 1} (d1 wins)
```

### Try This
```python
base = {'a': 1, 'b': 2}
override = {'b': 20, 'c': 30}
result = {**base, **override}
print(result)
```
**Answer:** `{'a': 1, 'b': 20, 'c': 30}`

---

# Define Classes

## What is a Class?
A class is a blueprint for creating objects. Think of it as a template or recipe.
```python
class Dog:
    pass

my_dog = Dog()
```

## Why Use Classes?
1. **Organization**: Group related data and functions.
2. **Reusability**: Create multiple objects from one template.
3. **Real-world modeling**: Represent real-world entities.

## Basic Example
```python
class Car:
    def start(self):
        print("Engine started")
    
my_car = Car()
my_car.start()
```

## Class vs Object
- **Class**: The blueprint (`Dog` class).
- **Object**: The actual instance (`my_dog`, `your_dog`).
One class, many objects!
```python
class Dog:
    pass

my_dog = Dog()
your_dog = Dog()
```

---

## Create Objects from Class Definitions

### Creating Objects
To create an object (or instance) from a class, you call the class using function-like syntax. This process is called instantiation. Each call creates a new, independent object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Each call creates a new, independent object
d1 = Dog("Rex", "Lab")
d2 = Dog("Max", "Poodle")
print(f"{d1.name} is a {d1.breed}") # Rex is a Lab
print(f"{d2.name} is a {d2.breed}") # Max is a Poodle
```

### Objects Are Independent
Once created, objects have their own separate state. Changing an attribute on one object does not affect other objects, even if they are from the same class.

```python
d1.name = "Buddy" # Changes only d1's name
print(d1.name)    # Buddy
print(d2.name)    # Max (unchanged)
```

### Type Checking
You can verify an object's type or if it's an instance of a specific class.

```python
print(type(d1))            # <class '__main__.Dog'>
print(isinstance(d1, Dog)) # True
print(isinstance("hello", Dog)) # False
```

### Storing Objects in Collections
Objects can be stored and manipulated within Python's collection types like lists, dictionaries, or sets.

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [Item("Pen", 1.5), Item("Book", 12.0), Item("Bag", 25.0)]
for item in items:
    print(f"{item.name}: ${item.price}")

# Output:
# Pen: $1.5
# Book: $12.0
# Bag: $25.0
```

---

# Implement the __init__ Constructor

## What is __init__?
`__init__` is a special method that runs automatically when you create an object:
```python
class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Created dog named {name}")

my_dog = Dog("Buddy")  # Created dog named Buddy
print(my_dog.name)      # Buddy
```

## Why Use __init__?
1.  **Initialize data**: Set up object with starting values.
2.  **Automatic**: Runs automatically when creating object.
3.  **Customization**: Each object gets different data.

## The self Parameter
`self` refers to the object being created. It's the first parameter of `__init__` and allows you to store data directly on *that specific object*.
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Store name in THIS object
        self.age = age    # Store age in THIS object

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob
```

## With and Without __init__
```python
# Without __init__ (manual assignment)
class Dog:
    pass
dog = Dog()
dog.name = "Buddy"

# With __init__ (automatic assignment)
class Dog:
    def __init__(self, name):
        self.name = name
dog = Dog("Buddy")
print(dog.name) # Buddy
```