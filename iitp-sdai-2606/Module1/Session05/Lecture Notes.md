# DSA: Dictionaries & HashMaps – Built-in Functions

## What You Will Learn in This Lesson

You have already learned how to store **many values in order** using **lists** and how to work with **text** using **strings**. You accessed items by **position** (index 0, 1, 2…) and used built-in functions like **`len()`** and **`sorted()`** to measure and organise data.

In this lesson, you will learn **dictionaries** — a way to store data as **key–value pairs** instead of numbered positions. You will create dictionaries, read and update values using **keys**, use methods like **`get()`**, **`keys()`**, **`values()`**, and **`items()`**, and understand why dictionaries behave like **hashmaps** for fast lookups.

By the end, you will be able to build contact books, product price maps, student mark records, and word counters — the same kind of labelled data that real apps use every day.

---

## Why Do Programs Need Dictionaries?

- **Official Definition:** A **dictionary** in Python is a collection of **key–value pairs**, where each **key** maps to exactly one **value**. Keys must be **unique** and **hashable**.
- **In Simple Words:** A dictionary is like a **labelled storage box** — you find things by **name** (the key), not by **position number** (like in a list).
- **Real-Life Example:** Your **phone contacts app** — you search **"Maa"** and instantly get her number. You do not scroll to "contact number 47" in a long list.

- **E-commerce apps** map **product ID → price** — look up one item without scanning every product.
- **Exam result portals** map **roll number → marks** — fetch one student's score directly.
- **Language translation tools** map **English word → Hindi word** — `"water" → "paani"`.

Without dictionaries, you would keep **two parallel lists** — one for names and one for values — and search by index every time. That works for small data but becomes slow and error-prone when lists grow. Dictionaries are built for **fast lookup by label**.

| Feature | List | Dictionary |
|---------|------|------------|
| Access by | **Index** (0, 1, 2…) | **Key** ("name", 101, "Delhi") |
| Order | Positions matter | Keys are unique labels |
| Best for | Ordered sequences — marks, cart items | Labelled data — contacts, prices, settings |
| Lookup style | "Give me item at position 3" | "Give me value for key 'Rahul'" |

![Dictionaries big picture — phone contacts search by name, list vs dictionary comparison with indexed boxes vs labelled key-value pairs, e-commerce product ID to price, exam roll number to marks, and translation word mapping](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-01-dictionaries-big-picture.png?v=20260620)

---

## Creating and Defining Dictionaries

- **Official Definition:** A **key–value pair** consists of a **key** (the lookup label) and a **value** (the stored data), written as `key: value` inside curly braces `{ }`. **Dictionary creation** uses `{key: value, ...}`, an empty `{}`, or the **`dict()`** constructor.
- **In Simple Words:** Each entry is a **tag** and what is stored under that tag — like a name tag on a locker and what is inside the locker.
- **Real-Life Example:** A **restaurant menu board** — dish name (key) and price (value): `"Dosa": 60`, `"Idli": 40`.

```python
# Simple dictionary — keys on the left, values on the right
student = {
    "name": "Anita",  # Key "name" maps to value "Anita"
    "age": 20,  # Key "age" maps to value 20
    "city": "Pune"  # Key "city" maps to value "Pune"
}
print(student)  # Output: {'name': 'Anita', 'age': 20, 'city': 'Pune'}
print(type(student))  # Output: <class 'dict'>

# Empty dictionary and menu with initial pairs
cart = {}  # No items yet — ready to fill later
menu = {"Dosa": 60, "Idli": 40, "Vada": 35, "Coffee": 25}
print(menu)  # Output: {'Dosa': 60, 'Idli': 40, 'Vada': 35, 'Coffee': 25}

# dict() constructor — another way to create
student = dict(name="Rohit", marks=88, city="Jaipur")
print(student)  # Output: {'name': 'Rohit', 'marks': 88, 'city': 'Jaipur'}

# Values can be any type — lists as values are allowed
profile = {"username": "deepa_22", "followers": 150, "scores": [78, 85, 92]}
print(profile)  # Output: {'username': 'deepa_22', 'followers': 150, 'scores': [78, 85, 92]}
```

**How the code works:**

- Curly braces **`{ }`** tell Python "this is a dictionary." Each pair uses **`key: value`** with a **colon** between them.
- **`{}`** creates an empty dictionary — useful when you will add pairs later (like a shopping cart filling up).
- Keys are usually **strings** or **integers**; **values** can be any type — numbers, strings, lists, even other dictionaries.
- **Common mistake:** Using **`[ ]`** instead of **`{ }`** — square brackets create a **list**, not a dictionary.

Lists and strings use **position**; dictionaries use **meaningful labels**. That shift is what makes dictionaries powerful for real-world data.

---

## Accessing and Modifying Key-Value Pairs

- **Official Definition:** **Dictionary access** retrieves a value using its key: `dictionary[key]`. **Modification** updates an existing value or adds a new pair: `dictionary[key] = new_value`.
- **In Simple Words:** Ask for data by **label** with **`dict["label"]`**. Change a value or add a new label with **`=`**.
- **Real-Life Example:** At a **railway reservation counter**, you give your **PNR number** (key) and get your **seat details** (value). If your seat changes, the same PNR now maps to a new seat.

```python
contacts = {
    "Maa": "9876543210",
    "Papa": "9876543211",
    "Bhai": "9876543212"
}

print(contacts["Maa"])  # Output: 9876543210 — access by key

contacts["Bhai"] = "9999888877"  # Modify existing value
contacts["Didi"] = "9123456789"  # Add new key-value pair
print(contacts)  # Output: {'Maa': '9876543210', 'Papa': '9876543211', 'Bhai': '9999888877', 'Didi': '9123456789'}

del contacts["Papa"]  # Delete a pair entirely
print(contacts)  # Output: {'Maa': '9876543210', 'Bhai': '9999888877', 'Didi': '9123456789'}
```

**How the code works:**

- **`contacts["Maa"]`** looks up the key and returns its value — fast, direct access.
- **`contacts["Didi"] = "9123456789"`** creates a **new** key because `"Didi"` was not present before.
- **`del contacts["Papa"]`** removes the entire key–value pair for **`"Papa"`**.
- **Common mistake:** Accessing a missing key — `contacts["Uncle"]` raises **`KeyError`**. Use **`get()`** (next section) for safe access.

| Operation | Syntax | What Happens |
|-----------|--------|--------------|
| **Read** | `dict[key]` | Returns value or **`KeyError`** if missing |
| **Update** | `dict[key] = value` | Changes value if key exists |
| **Add** | `dict[new_key] = value` | Inserts new pair |
| **Delete** | `del dict[key]` | Removes the pair entirely |

![Key-value access diagram — curly brace dictionary structure with name age city pairs, read update add delete operations, railway PNR key to seat value analogy, and contacts phone book example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-02-key-value-access.png?v=20260620)

### Quick Activity: Update a Product Price Map

Start with two products and prices. Change one price, add a new product, and print the updated dictionary.

```python
prices = {"Notebook": 45, "Pen": 10}
prices["Pen"] = 12  # Price increased
prices["Eraser"] = 5  # New product added
print(prices)  # Output: {'Notebook': 45, 'Pen': 12, 'Eraser': 5}
```

Accessing by key is the core skill — dictionary **methods** make this safer and more flexible.

---

## Dictionary Methods — `get()`, `keys()`, `values()`, and `items()`

- **Official Definition:** A **dictionary method** is a function called on a dictionary using dot notation. **`get(key, default)`** returns a value safely; **`keys()`**, **`values()`**, and **`items()`** return **view objects** listing keys, values, or key–value pairs.
- **In Simple Words:** Methods are **built-in actions** — safe lookup, list all keys, list all values, or list all pairs together.
- **Real-Life Example:** A **hotel reception desk** — `get()` is "Do you have a booking under Sharma? If not, here is a default room." `items()` is name + room number together.

### Using `get()` — Safe Lookup Without Crashes

```python
marks = {"Anita": 88, "Rohit": 72, "Priya": 95}

print(marks["Anita"])  # Output: 88 — works when key exists
print(marks.get("Karan"))  # Output: None — no crash when key missing
print(marks.get("Karan", 0))  # Output: 0 — default used because Karan not in dict
print(marks.get("Priya", 0))  # Output: 95 — real value returned; default ignored
# print(marks["Karan"])  # KeyError: 'Karan' — bracket access would crash
```

**How the code works:**

- **`marks.get("Karan")`** returns **`None`** instead of crashing when the key is missing.
- **`marks.get("Karan", 0)`** returns **`0`** (the default) when the key is missing.
- **When to use `get()`:** User input, file data, or any situation where a key might not exist.

### Using `keys()`, `values()`, and `items()`

```python
inventory = {"Rice": 50, "Dal": 30, "Oil": 20, "Sugar": 15}

print(inventory.keys())  # Output: dict_keys(['Rice', 'Dal', 'Oil', 'Sugar'])
print(list(inventory.keys()))  # Output: ['Rice', 'Dal', 'Oil', 'Sugar'] — as a list
print(sum(inventory.values()))  # Output: 115 — total stock units

# Loop through items — most common pattern
print("--- Stock Report ---")
for product, qty in inventory.items():
    print(f"{product}: {qty} kg")
```

**How the code works:**

- **`keys()`** returns a **view** of all keys — wrap with **`list()`** if you need a real list.
- **`values()`** returns all values — useful with **`sum()`** when values are numbers.
- **`items()`** returns **`(key, value)` tuples** — perfect for **`for` loops** that need both parts.
- **Common mistake:** Expecting **`keys()`** to return a list directly — use **`list(dict.keys())`** when you need a list.

| Method | Returns | Best Use |
|--------|---------|----------|
| **`get(key, default)`** | Value or default | Safe lookup when key may be missing |
| **`keys()`** | All keys | Check what labels exist |
| **`values()`** | All values | Totals, averages, searching by value |
| **`items()`** | `(key, value)` pairs | Looping over the whole dictionary |

![Dictionary methods diagram — get() safe lookup with default fallback, keys() values() items() panels, hotel reception desk analogy, and student marks method comparison table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-03-dictionary-methods.png?v=20260620)

### Quick Activity: Safe Lookup and Menu Report

Look up present and absent student names using **`get()`**, then loop through a menu with **`items()`**.

```python
scores = {"Amit": 78, "Sneha": 91, "Rahul": 85}
print(scores.get("Sneha", "Not found"))  # Output: 91
print(scores.get("Kiran", "Not found"))  # Output: Not found

menu = {"Dosa": 60, "Idli": 40, "Vada": 35}
for dish, price in menu.items():
    print(f"{dish} — Rs.{price}")
```

---

## HashMaps — Why Dictionaries Are Fast

- **Official Definition:** A **hashmap** (or **hash table**) is a data structure that maps keys to values using a **hash function** to compute a storage location, enabling fast lookup, insertion, and deletion.
- **In Simple Words:** A hashmap is a smart filing system — instead of searching every file, it uses a formula to jump directly to the right drawer.
- **Real-Life Example:** A **bank locker** — your account number (key) is processed by a rule (hash function) that tells the clerk exactly which locker (slot) to open.

In Python, the built-in **`dict`** type **is** a hashmap. When instructors say "dictionary" and "hashmap," they usually mean the **same thing** in Python.

- **List lookup:** To find `"Mango"` in a list of 10,000 fruits, Python may check **every item** — slow for large data.
- **Dictionary lookup:** To find the price of `"Mango"`, Python uses the key's **hash** to jump to the right slot — fast even with millions of entries.

```python
# List — must scan every item
fruits_list = ["apple", "banana", "mango", "grapes", "orange"]
found = "mango" in fruits_list  # Checks each item one by one
print("Found in list:", found)  # Output: Found in list: True

# Dictionary — direct key access, no manual loop
fruit_prices = {"apple": 120, "banana": 40, "mango": 80, "grapes": 90, "orange": 60}
print("Mango price:", fruit_prices["mango"])  # Output: Mango price: 80
print("Is mango a key?", "mango" in fruit_prices)  # Output: Is mango a key? True
```

**How the code works:**

- The **dictionary** uses **`fruit_prices["mango"]`** — direct access by key without a manual loop.
- **`"mango" in fruit_prices`** checks whether a key exists — returns **`True`** or **`False`** safely.
- **Common mistake:** `"mango" in fruit_prices` checks **keys**, not values.

### Hashable Keys — What Can Be a Dictionary Key?

- **Official Definition:** A **hashable** object has a fixed hash value and can be used as a dictionary key. **Strings**, **integers**, **floats**, **booleans**, and **tuples of hashable items** are hashable. **Lists** and **dictionaries** are **not** hashable.
- **In Simple Words:** Keys must be **stable labels** — things that do not change shape. A list can grow or shrink, so Python will not trust it as a key.
- **Real-Life Example:** An **Aadhaar number** (fixed string) works as an ID key. A **shopping list on a sticky note** that you keep editing cannot serve as a permanent locker key.

```python
valid_dict = {
    "name": "Rahul",  # String key
    101: "Room A",  # Integer key
    ("Math", "Science"): "Group A"  # Tuple key — all elements must be hashable
}
print(valid_dict[101])  # Output: Room A

# Invalid — TypeError: unhashable type
# bad_dict = {[1, 2]: "value"}  # List as key — not allowed
# bad_dict2 = {{"a": 1}: "value"}  # Dict as key — not allowed
```

**How the code works:**

- **Strings** and **integers** are the most common key types in beginner programs.
- **Lists and dicts as keys** fail because their contents can change — Python raises **`TypeError: unhashable type`**.
- **Values** can be lists or dicts freely — only **keys** must be hashable.

| Type | Hashable? | Can Be a Key? |
|------|-----------|---------------|
| **String / Integer / Float / Boolean** | Yes | Yes |
| **Tuple** (hashable elements) | Yes | Yes |
| **List / Dictionary** | No | No |

![Hashmap fast lookup diagram — list scan vs dictionary direct key access, hash function jumping to mango price slot, bank locker analogy, and hashable vs unhashable key types table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-04-hashmap-fast-lookup.png?v=20260620)

### Quick Activity: Check Keys Before Access

Create a dictionary of three cities and their state codes. Use **`in`** to check if a city exists before printing its code.

```python
city_state = {"Pune": "MH", "Jaipur": "RJ", "Kochi": "KL"}
city = "Pune"
if city in city_state:
    print(f"{city} is in state {city_state[city]}")
else:
    print(f"{city} not in dictionary")
```

Understanding hashmaps explains **why** dictionaries exist — built-in functions help you **measure and sort** dictionary data next.

---

## Built-in Functions — `len()` and `sorted()` on Dictionaries

- **Official Definition:** **`len(d)`** returns the number of key–value pairs in dictionary **`d`**. **`sorted(iterable)`** returns a new sorted list; when applied to a dictionary directly, it sorts the **keys**.
- **In Simple Words:** **`len()`** counts how many entries exist. **`sorted()`** arranges keys (or values) in order without changing the original dictionary.
- **Real-Life Example:** **`len()`** is counting how many dishes are on the menu. **`sorted()`** is arranging dish names alphabetically for display — the kitchen recipe book stays unchanged.

```python
marks = {"Anita": 88, "Rohit": 72, "Priya": 95, "Karan": 64}

print(len(marks))  # Output: 4 — counts key-value pairs
print(sorted(marks))  # Output: ['Anita', 'Karan', 'Priya', 'Rohit'] — sorts KEYS
print(sorted(marks.values()))  # Output: [64, 72, 88, 95] — sorts values
print(sorted(marks.values(), reverse=True))  # Output: [95, 88, 72, 64] — highest first
print(marks)  # Original unchanged — sorted() returns a NEW list
```

**How the code works:**

- **`len(marks)`** counts **pairs** — 4 students means **`len` is 4**.
- **`sorted(marks)`** sorts **keys** alphabetically — it does **not** sort by values.
- **`reverse=True`** flips sort order — useful for rank lists and leaderboards.
- **Common mistake:** Expecting **`sorted(marks)`** to sort by **values** — pass **`marks.values()`** instead.

### Sorting by Value — A Practical Pattern

When you need "who scored highest," sort **`items()`** by value using a **key function**:

```python
marks = {"Anita": 88, "Rohit": 72, "Priya": 95, "Karan": 64}

top_first = sorted(marks.items(), key=lambda pair: pair[1], reverse=True)
print(top_first)  # Output: [('Priya', 95), ('Anita', 88), ('Rohit', 72), ('Karan', 64)]

print("--- Leaderboard ---")
for name, score in top_first:
    print(f"{name}: {score}")
```

**How the code works:**

- **`marks.items()`** gives **`(name, score)` tuples** — **`pair[1]`** is the score.
- **`key=lambda pair: pair[1]`** tells **`sorted()`** to compare by the **second element** (the mark).
- The **original dictionary is not changed** — same rule as **`sorted()`** on lists.

| Expression | What Gets Sorted | Original Dict Changed? |
|------------|------------------|------------------------|
| **`sorted(d)`** | Keys | No |
| **`sorted(d.values())`** | Values | No |
| **`sorted(d.items(), key=...)`** | Pairs by custom rule | No |

![len and sorted on dictionaries diagram — len counts four student pairs, sorted keys alphabetically vs sorted values ascending, leaderboard Priya first with trophy, word counter example, and original dict unchanged note](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-05-len-sorted-builtin.png?v=20260620)

### Quick Activity: Analyse Dictionary Size and Sorted Keys

Create a dictionary of four friends and their ages. Print the count, alphabetically sorted names, and youngest-to-oldest ages.

```python
ages = {"Amit": 22, "Sneha": 20, "Rahul": 24, "Priya": 21}
print("Friends:", len(ages))
print("Names A-Z:", sorted(ages))
print("Ages ascending:", sorted(ages.values()))
```

---

## Putting It Together — A Word Counter Program

Real programs combine creation, access, methods, and built-in functions in one flow. A **word counter** is a classic dictionary use case.

```python
text = "Python is fun and Python is powerful"
words = text.split()
print("Words:", words)  # Output: ['Python', 'is', 'fun', 'and', 'Python', 'is', 'powerful']

word_count = {}  # Empty dictionary for counts
for word in words:
    word_count[word] = word_count.get(word, 0) + 1  # Increment count safely

print("--- Word Count ---")
for word, count in word_count.items():
    print(f"{word}: {count}")

print("Unique words:", len(word_count))  # Output: Unique words: 5
print("Sorted words:", sorted(word_count))  # Output: ['Python', 'and', 'fun', 'is', 'powerful']
```

**How the code works:**

- **`text.split()`** breaks the string into a **list of words**.
- **`word_count.get(word, 0) + 1`** is the standard counting pattern — if the word is new, start at 0 then add 1; if it exists, increment.
- **`len(word_count)`** tells how many **unique** words appeared; **`sorted(word_count)`** lists them alphabetically.

---

## Practice Programs — Beginner Dictionary Exercises

### Exercise 1: Contact Book and Inventory Report

Build a contact dictionary and look up names with **`get()`**. Then print a stock report with totals.

```python
contacts = {"Maa": "9876543210", "Papa": "9876543211", "Friend": "9123456789"}
print(contacts.get("Maa", "Not found"))  # Output: 9876543210
print(contacts.get("Uncle", "Not found"))  # Output: Not found

stock = {"Rice": 50, "Dal": 30, "Oil": 20}
for item, qty in stock.items():
    print(f"{item}: {qty} kg")
print("Total units:", sum(stock.values()))
print("Product count:", len(stock))
```

### Exercise 2: Student Marks Summary

Store four students' marks. Print sorted names, highest mark, and a leaderboard sorted by score (highest first).

```python
marks = {"Anita": 88, "Rohit": 72, "Priya": 95, "Karan": 64}
print("Students:", sorted(marks))
print("Highest mark:", max(marks.values()))
leaderboard = sorted(marks.items(), key=lambda pair: pair[1], reverse=True)
for name, score in leaderboard:
    print(f"{name}: {score}")
```

### Exercise 3: Check Before You Access

Given a dictionary of PIN codes, hard-code a city name in a variable. Print the PIN if the city exists; otherwise print a friendly message.

```python
pin_codes = {"Pune": 411001, "Delhi": 110001, "Mumbai": 400001}
city = "Pune"
if city in pin_codes:
    print(f"PIN for {city}: {pin_codes[city]}")
else:
    print(f"No PIN stored for {city}")
```

---

## Debugging Dictionaries

- **Print the dictionary** after each add or update — especially when building from loops or user input.
- **Use `get()` instead of `[ ]`** when a key might be missing — avoids unexpected **`KeyError`** crashes.
- **Check key type:** `"101"` (string) and **`101`** (integer) are **different keys**.
- **Verify hashable keys:** Lists and dicts cannot be keys — use a **string** or **tuple** label instead.
- **Remember `sorted(dict)` sorts keys:** To rank by values, use **`sorted(dict.items(), key=...)`**.
- **Trace with small examples:** Test on 3-key dictionaries before large datasets.

```python
sample = {"a": 1, "b": 2}
print("Keys:", list(sample.keys()))  # Output: Keys: ['a', 'b']
print("Safe read:", sample.get("c", "missing"))  # Output: Safe read: missing
print("Count:", len(sample))  # Output: Count: 2
```

---

## Key Takeaways

- **Dictionaries** store **key–value pairs** — access data by **meaningful label** instead of numeric index, ideal for contacts, prices, settings, and records.
- **Methods** — **`get()`** for safe lookup, **`keys()`**, **`values()`**, and **`items()`** for listing and looping — are the everyday tools for reading dictionary data.
- Python's **`dict`** is a **hashmap** — keys must be **hashable** (strings, numbers, tuples), which enables **fast direct lookup** even in large datasets.
- **Built-in functions** — **`len()`** counts entries; **`sorted()`** orders keys or values without changing the original dictionary.
- These skills connect directly to **functions, file handling, and data processing** — where dictionaries carry labelled information your programs look up, update, and analyse.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **Dictionary `{key: value}`** | Collection of unique keys mapped to values |
| **Key–value pair** | One label (key) and its stored data (value) |
| **`dict[key]`** | Access or assign value for a key; raises **`KeyError`** if missing |
| **`get(key, default)`** | Safe access — returns default instead of crashing |
| **`keys()`** | Returns a view of all keys in the dictionary |
| **`values()`** | Returns a view of all values in the dictionary |
| **`items()`** | Returns `(key, value)` pairs — best for loops |
| **`del dict[key]`** | Removes a key–value pair from the dictionary |
| **`in` (with dict)** | Checks whether a key exists — `"key" in dict` |
| **Hashmap / Hash table** | Data structure for fast key-based lookup; Python `dict` is one |
| **Hashable** | Object that can be used as a dictionary key (str, int, tuple, etc.) |
| **`KeyError`** | Raised when accessing a missing key with `[ ]` |
| **`TypeError` (unhashable)** | Raised when using a list or dict as a key |
| **`len(dict)`** | Returns number of key–value pairs |
| **`sorted(dict)`** | Returns a new list of keys sorted alphabetically |
| **`sorted(dict.values())`** | Returns values sorted in ascending order |
| **`sorted(dict.items(), key=...)`** | Sorts pairs by a custom rule — e.g. by value |
