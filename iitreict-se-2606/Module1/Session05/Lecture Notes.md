# Core Data Structures: Strings, Lists, Tuples, Dictionaries & Sets

## What You Will Learn in This Lesson

You have already learned how to wrap logic into **functions** using **`def`**, pass data with **parameters**, send results back with **`return`**, and understand **local vs global scope**. Your programs can reuse named blocks of code instead of repeating the same steps.

In this lesson, you will learn how to store and work with **many values in memory** using Python's core data structures:

- **Lists** and **strings** — ordered sequences with indexing, slicing, and methods
- **Tuples** — ordered, unchangeable collections for fixed data
- **Dictionaries** — labelled **key–value** storage for fast lookups
- **Sets** — unique unordered collections for membership checks
- **Built-in functions** — `len()`, `sorted()`, `min()`, `max()`, `sum()` on collections

By the end, you will choose the right structure for a problem and manipulate in-memory data with confidence.

---

## Why Do Programs Need Data Structures?

- **Official Definition:** A **data structure** is a way of organising and storing data so it can be accessed and updated efficiently.
- **In Simple Words:** Data structures are different kinds of containers — like a shopping bag, a sealed parcel, a labelled locker, or a unique ID list.
- **Real-Life Example:** A **Swiggy cart** is a list of items; a **phone contacts app** is a dictionary of names to numbers; a **locked exam roll sheet** is like a tuple (fixed once printed); a **unique coupon code list** is like a set.

Without collections, you would create separate variables for every mark or price — `mark1`, `mark2`, `mark3` — which becomes messy as data grows. Choosing the right container makes programs shorter, clearer, and safer.

| Structure | Written With | Ordered? | Changeable? | Best For |
|-----------|--------------|----------|-------------|----------|
| **List** | `[ ]` | Yes | Yes (mutable) | Shopping carts, marks, tasks |
| **String** | `' '` / `" "` | Yes | No (immutable) | Names, messages, text |
| **Tuple** | `( )` | Yes | No (immutable) | Fixed records — RGB colour, coordinates |
| **Dictionary** | `{key: value}` | Keys unique | Yes | Contacts, prices, settings |
| **Set** | `{ }` or `set()` | No | Yes | Unique IDs, duplicate removal |

![Lists and strings big picture — Swiggy cart as ordered list, exam marks list with student name string, UPI transaction history, tiffin box compartments analogy, and list vs single variable comparison](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-01-lists-strings-big-picture.png?v=20260614)

---

## Lists — Creating and Essential Methods

- **Official Definition:** A **list** is an ordered, mutable collection written with square brackets `[]`.
- **In Simple Words:** A list is a numbered row of boxes — you can add, remove, or change items.
- **Real-Life Example:** A **tiffin box with compartments** — rice, dal, sabzi — together form one lunch box.

```python
shopping_list = []  # Empty list — no items yet
fruits = ["apple", "banana", "mango"]  # Three string items in order
marks = [78, 85, 92, 64, 88]  # Five integer marks
mixed = ["Rahul", 22, True, 85.5]  # Different types allowed in one list

daily_tasks = []  # Start empty and grow
daily_tasks.append("Brush teeth")  # Add at the end
daily_tasks.append("Attend class")
print(daily_tasks)  # Output: ['Brush teeth', 'Attend class']
```

**How the code works:**

- Square brackets `[]` create a list; items are separated by commas; order is preserved.
- **Common mistake:** Using `( )` instead of `[ ]` — parentheses create a **tuple**, not a list.

### Essential List Methods — `append`, `pop`, and `sort`

```python
team = ["Virat", "Rohit", "Bumrah"]
team.append("Jadeja")  # Add at the end
print(team)  # Output: ['Virat', 'Rohit', 'Bumrah', 'Jadeja']

snacks = ["samosa", "pakora", "biscuit", "chai"]
removed = snacks.pop()  # Remove and return last item
print("Removed:", removed)  # Output: Removed: chai
print("Remaining:", snacks)  # Output: ['samosa', 'pakora', 'biscuit']

cities = ["Delhi", "Jaipur", "Goa", "Kerala"]
print(cities.pop(1))  # Output: Jaipur — remove at index 1

marks = [78, 92, 64, 85, 71]
marks.sort()  # Sort original list ascending
print(marks)  # Output: [64, 71, 78, 85, 92]
```

**How the code works:**

- **`append(x)`** adds at the end; **`pop()`** removes the last item; **`pop(i)`** removes at index `i`.
- **`sort()`** changes the original list — use `marks.sort(reverse=True)` for descending.
- Calling **`pop()`** on an empty list raises **`IndexError`**. Mixing numbers and strings then calling **`sort()`** raises **`TypeError`**.

| Method | What It Does | Changes Original? |
|--------|--------------|-------------------|
| **`append(x)`** | Adds `x` at the end | Yes |
| **`pop()` / `pop(i)`** | Removes last item / item at `i` | Yes |
| **`sort()`** | Arranges ascending | Yes |

![List methods diagram — append adds at end like train queue, pop removes last or indexed item, sort rearranges marks ascending, with method comparison table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-02-list-methods.png?v=20260614)

### Quick Activity: Build and Update a Shopping List

Create an empty list, add four grocery items with **`append`**, remove the last with **`pop`**, then print the list and its length.

```python
groceries = []
groceries.append("Rice")
groceries.append("Dal")
groceries.append("Milk")
groceries.append("Bread")
print("Before pop:", groceries)
groceries.pop()
print("After pop:", groceries)
print("Items to buy:", len(groceries))
```

---

## Indexing and Slicing on Lists

- **Official Definition:** **Indexing** accesses one element by position (first item is **0**). **Negative indexing** uses **-1** for the last item. **Slicing** extracts a portion with `list[start:stop:step]` where `stop` is exclusive.
- **In Simple Words:** Each item has a seat number. Slicing cuts a portion — like taking two idlis from a plate of five.
- **Real-Life Example:** From a **playlist of 10 songs**, playing songs 3 to 5 is a slice.

For `fruits = ["apple", "banana", "mango", "grapes"]`:

| Index | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| Item | apple | banana | mango | grapes |
| Negative | -4 | -3 | -2 | -1 |

```python
fruits = ["apple", "banana", "mango", "grapes"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: grapes
marks = [78, 85, 92, 64]
marks[2] = 95  # Lists are mutable — change index 2
print(marks)  # Output: [78, 85, 95, 64]

temps = [32, 34, 31, 33, 35, 30, 29]
print(temps[2:5])  # Output: [31, 33, 35] — stop is exclusive
print(temps[:3])  # Output: [32, 34, 31]
print(temps[-2:])  # Output: [30, 29]
print(temps[::-1])  # Output: reversed copy
```

**How the code works:**

- Valid indices for length 4 are **0–3**. Last index is **`len(list) - 1`**.
- Slicing creates a **new list**; the original stays unchanged.
- **Common mistake:** `fruits[4]` causes **`IndexError`**; expecting `stop` to be inclusive is wrong — `[0:3]` gives three items.

![List indexing diagram — positive indices 0 to 3 and negative indices -4 to -1 on fruits list, cricket overs analogy, mutable marks update, and IndexError warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-03-indexing.png?v=20260614)

![List slicing diagram — temps[2:5] with exclusive stop, shorthand slices [:3] [-2:] [::2] [::-1], idli plate analogy, and new list created warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-04-list-slicing.png?v=20260614)

---

## Strings — Indexing, Slicing, Concatenation, and f-Strings

- **Official Definition:** A **string** is an immutable sequence of characters. **Concatenation** joins with `+`; an **f-string** embeds expressions inside `{ }` with an `f` prefix.
- **In Simple Words:** A string is any text. You can glue pieces with `+`, or fill blanks in a sentence with f-strings.
- **Real-Life Example:** Your **name on an Aadhaar card** is a string; a **receipt template** is like an f-string.

```python
name = "Priya"
word = "PYTHON"
print(name[0])  # Output: P
print(name[-1])  # Output: a
print(word[1:4])  # Output: YTH
print(word[::-1])  # Output: NOHTYP

first_name = "Amit"
last_name = "Sharma"
print(first_name + " " + last_name)  # Output: Amit Sharma
print("-" * 30)  # Repeat a string

marks = 87
print(f"{name} scored {marks} marks.")  # Output: Priya scored 87 marks.
item, qty, price = "Notebook", 3, 45
print(f"Item: {item} | Qty: {qty} | Total: Rs.{qty * price}")
```

**How the code works:**

- Strings are **immutable** — `name[0] = "p"` is not allowed.
- Both sides of `+` must be strings — use `str(25)` or an f-string for numbers.
- **Common mistake:** Forgetting the `f` prefix — without it, `{name}` prints as literal text.

![Strings diagram — PYTHON character indexing and slicing, immutability garland analogy, concatenation Amit + Sharma, string repeat with asterisk, and Aadhaar name card example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-05-strings-concatenation.png?v=20260614)

![f-string formatting diagram — receipt template with curly brace placeholders, Deepa scored 87 example, bill with qty and total, :.2f decimal formatting, and missing f prefix mistake](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-06-fstrings.png?v=20260614)

Indexing and slicing work the same on lists and strings because both are ordered sequences. Next comes a sequence you **cannot** change after creation.

---

## Tuples — Ordered and Immutable

- **Official Definition:** A **tuple** is an ordered, immutable collection written with parentheses `( )`.
- **In Simple Words:** A tuple is like a sealed parcel — items stay in order, but you cannot add, remove, or replace them after packing.
- **Real-Life Example:** An **RGB colour** `(255, 128, 0)` or a **latitude–longitude** pair should not accidentally change mid-program.

```python
point = (10, 20)  # Two related numbers as one unit
rgb = (255, 128, 0)  # Fixed colour values
student = ("Anita", 20, "Pune")  # Fixed record fields
single = (42,)  # Trailing comma makes a one-item tuple
empty = ()  # Empty tuple

print(point[0])  # Output: 10 — indexing works
print(rgb[-1])  # Output: 0
print(student[1:3])  # Output: (20, 'Pune') — slicing works
print(len(rgb))  # Output: 3

# Unpacking — assign each item to its own variable
name, age, city = student
print(f"{name} is {age} years old in {city}")

# Tuple as a dictionary key (lists cannot be keys)
seat = {("A1", "Window"): "Rahul", ("B2", "Aisle"): "Priya"}
print(seat[("A1", "Window")])  # Output: Rahul
```

**How the code works:**

- Indexing and slicing work like lists; **`append`**, **`pop`**, and item assignment do **not**.
- A single-item tuple needs a **comma**: `(42,)` — without it, `(42)` is just an integer in parentheses.
- Tuples are **hashable** when their elements are hashable — useful as **dictionary keys**.
- **Common mistake:** Writing `point[0] = 99` raises **`TypeError: 'tuple' object does not support item assignment`**.

| Need | Prefer |
|------|--------|
| Grow, shrink, reorder | **List** |
| Fixed record / safe key | **Tuple** |

### Quick Activity: Unpack a Student Record

```python
record = ("Rohit", 88, "Jaipur")
name, marks, city = record
print(f"{name} from {city} scored {marks}")
```

When labels matter more than positions, use a **dictionary**.

---

## Dictionaries — Key–Value Storage

- **Official Definition:** A **dictionary** stores **key–value pairs**. Each key maps to one value. Keys must be **unique** and **hashable**.
- **In Simple Words:** Find data by **name/label**, not by seat number.
- **Real-Life Example:** Your **phone contacts** — search **"Maa"** and get her number instantly.

| Feature | List | Dictionary |
|---------|------|------------|
| Access by | Index (0, 1, 2…) | Key ("name", 101) |
| Best for | Ordered sequences | Labelled data — contacts, prices |

![Dictionaries big picture — phone contacts search by name, list vs dictionary comparison with indexed boxes vs labelled key-value pairs, e-commerce product ID to price, exam roll number to marks, and translation word mapping](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-01-dictionaries-big-picture.png?v=20260620)

```python
student = {"name": "Anita", "age": 20, "city": "Pune"}
menu = {"Dosa": 60, "Idli": 40, "Vada": 35}
cart = {}  # Empty dictionary
profile = {"username": "deepa_22", "scores": [78, 85, 92]}  # Values can be lists

contacts = {"Maa": "9876543210", "Papa": "9876543211", "Bhai": "9876543212"}
print(contacts["Maa"])  # Output: 9876543210
contacts["Bhai"] = "9999888877"  # Update existing
contacts["Didi"] = "9123456789"  # Add new pair
del contacts["Papa"]  # Delete a pair
print(contacts)
```

**How the code works:**

- Use `{key: value}` with a colon; **`{}`** starts empty.
- **`dict[key]`** reads; assignment updates or adds; **`del`** removes.
- Missing key with `[ ]` raises **`KeyError`** — prefer **`get()`** for safe access.
- **Common mistake:** Using `[ ]` instead of `{ }` creates a list, not a dictionary.

![Key-value access diagram — curly brace dictionary structure with name age city pairs, read update add delete operations, railway PNR key to seat value analogy, and contacts phone book example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-02-key-value-access.png?v=20260620)

### Dictionary Methods — `get()`, `keys()`, `values()`, `items()`

```python
marks = {"Anita": 88, "Rohit": 72, "Priya": 95}
print(marks.get("Karan"))  # Output: None — no crash
print(marks.get("Karan", 0))  # Output: 0 — default when missing

inventory = {"Rice": 50, "Dal": 30, "Oil": 20}
print(list(inventory.keys()))  # Output: ['Rice', 'Dal', 'Oil']
print(sum(inventory.values()))  # Output: 100
for product, qty in inventory.items():
    print(f"{product}: {qty} kg")
```

**How the code works:**

- **`get(key, default)`** returns the default instead of crashing.
- **`items()`** gives `(key, value)` pairs — best for loops.
- **`"mango" in fruit_prices`** checks **keys**, not values.

| Method | Best Use |
|--------|----------|
| **`get(key, default)`** | Safe lookup |
| **`keys()` / `values()`** | List labels / totals |
| **`items()`** | Loop over pairs |

![Dictionary methods diagram — get() safe lookup with default fallback, keys() values() items() panels, hotel reception desk analogy, and student marks method comparison table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-03-dictionary-methods.png?v=20260620)

Python dictionaries behave like **hashmaps** — lookup by key is fast because keys are hashed to a storage slot. Keys must be hashable (strings, numbers, tuples). Lists and dicts cannot be keys.

![Hashmap fast lookup diagram — list scan vs dictionary direct key access, hash function jumping to mango price slot, bank locker analogy, and hashable vs unhashable key types table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-04-hashmap-fast-lookup.png?v=20260620)

---

## Sets — Unique Items Only

- **Official Definition:** A **set** is an unordered collection of **unique** hashable items, written with `{ }` or created with **`set()`**.
- **In Simple Words:** A set is a bag that automatically throws away duplicates — each value appears at most once.
- **Real-Life Example:** A list of **coupon codes** or **registered mobile numbers** where repeats should not count twice.

```python
colors = {"red", "green", "blue", "red"}  # Duplicate "red" is kept only once
print(colors)  # Output order may vary — sets are unordered

unique_marks = set([78, 85, 78, 92, 85])  # Build from a list
print(sorted(unique_marks))  # Output: [78, 85, 92] — duplicates removed; sorted for stable display

empty_set = set()  # Correct empty set
# wrong = {}  # This creates an empty DICTIONARY, not a set

tags = {"python", "coding"}
tags.add("ai")  # Add one item
tags.discard("coding")  # Remove if present — no error if missing
print("python" in tags)  # Output: True — fast membership check

batch_a = {"Amit", "Sneha", "Rahul"}
batch_b = {"Sneha", "Priya", "Karan"}
print(batch_a | batch_b)  # Union — all names
print(batch_a & batch_b)  # Intersection — common names
print(batch_a - batch_b)  # Difference — only in A
```

**How the code works:**

- Duplicates disappear automatically; there is **no indexing** like `colors[0]`.
- Use **`set()`** for an empty set — **`{}`** is an empty **dictionary**.
- **`in`** on a set is a fast way to ask "is this already present?"
- **Common mistake:** Trying to store a **list** inside a set — lists are unhashable.

| Need | Prefer |
|------|--------|
| Ordered, allow duplicates, index access | **List** |
| Unique items, membership checks | **Set** |
| Label → value mapping | **Dictionary** |

### Quick Activity: Remove Duplicate Marks

```python
marks = [72, 88, 72, 91, 88, 65]
unique = set(marks)
print("Unique marks:", unique)
print("Count of unique:", len(unique))
```

---

## Built-in Functions on Collections

- **Official Definition:** Built-in functions like **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, and **`sum()`** work on many collections without importing libraries.
- **In Simple Words:** Ready-made tools to measure, sort, and summarise data.
- **Real-Life Example:** A **weighing scale at a ration shop** — one tool that totals weight without adding piece by piece.

```python
marks = [78, 92, 64, 85, 71]
word = "Python"
scores = {"Anita": 88, "Rohit": 72, "Priya": 95}

print(len(marks), len(word), len(scores))  # List items, characters, key-value pairs
print(sorted(marks))  # New sorted list — original unchanged
print(min(marks), max(marks), sum(marks))
print(f"Average: {sum(marks) / len(marks):.2f}")

print(sorted(scores))  # Sorts dictionary KEYS
print(sorted(scores.values()))  # Sorts values
print(max(scores.values()))  # Highest mark
```

**How the code works:**

- **`sorted(x)`** returns a **new list**; **`list.sort()`** changes the list in place and returns **`None`**.
- **`sum()`** needs numeric items; **`sorted(dict)`** sorts **keys**, not values.
- Methods change the object; most built-ins leave the original alone.

| Function | Typical Use |
|----------|-------------|
| **`len(x)`** | Count items / characters / pairs |
| **`sorted(x)`** | New sorted list |
| **`min(x)` / `max(x)`** | Smallest / largest |
| **`sum(x)`** | Total of numbers |

![Built-in functions diagram — len counts items, sorted returns new copy, min and max find extremes, sum totals marks with average formula, ration shop scale analogy, and sorted vs sort comparison](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-07-builtin-functions.png?v=20260614)

![len and sorted on dictionaries diagram — len counts four student pairs, sorted keys alphabetically vs sorted values ascending, leaderboard Priya first with trophy, word counter example, and original dict unchanged note](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-05-len-sorted-builtin.png?v=20260620)

---

## Choosing the Right Structure

Use this decision guide when solving a problem:

1. Need **ordered** items you will **change** often? → **List**
2. Need **text**? → **String**
3. Need a **fixed** ordered record (or a dict key)? → **Tuple**
4. Need **lookup by label**? → **Dictionary**
5. Need **unique** values only? → **Set**

```python
# Practical mix — class report using list + dict + set + builtins
students = ["Anita", "Rohit", "Priya", "Anita"]  # Names with a duplicate
marks = {"Anita": 88, "Rohit": 72, "Priya": 95}
unique_students = set(students)  # Remove duplicate name
top_score = max(marks.values())
print(f"Unique students: {len(unique_students)}")
print(f"Highest: {top_score}")
print(f"Sorted names: {sorted(marks)}")
print(f"Average: {sum(marks.values()) / len(marks):.2f}")
```

**How the code works:**

- The **list** holds ordered names; the **set** deduplicates; the **dictionary** maps name → mark; builtins answer summary questions.

### Practice Exercise: Mini Data Toolkit

```python
# 1) List + string
word = "AGENTIC"
print(word[0], word[-1], word[::-1])

# 2) Tuple unpack
city_info = ("Pune", "MH", 411001)
city, state, pin = city_info
print(f"{city}, {state} - {pin}")

# 3) Dictionary report
stock = {"Rice": 50, "Dal": 30, "Oil": 20}
for item, qty in stock.items():
    print(f"{item}: {qty} kg")
print("Total:", sum(stock.values()))

# 4) Set uniqueness
ids = [101, 102, 101, 103, 102]
print("Unique IDs:", set(ids))
```

---

## Key Takeaways

- **Lists** and **strings** support **indexing** and **slicing**; lists are mutable with methods like **`append`**, **`pop`**, and **`sort`**.
- **Tuples** are ordered and immutable — ideal for fixed records and as dictionary keys.
- **Dictionaries** store **key–value** pairs with methods like **`get()`**, **`keys()`**, **`values()`**, and **`items()`** for safe, labelled access.
- **Sets** keep **unique** items and support fast membership and set operations.
- Built-ins **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, and **`sum()`** work across collections — pick the structure that matches the problem, then process it with these tools as you build larger programs.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **List `[]`** | Ordered, mutable collection |
| **String** | Ordered, immutable text sequence |
| **Tuple `( )`** | Ordered, immutable collection |
| **Dictionary `{k: v}`** | Key–value mapping; keys unique and hashable |
| **Set `{ }` / `set()`** | Unordered unique items |
| **`append` / `pop` / `sort`** | Common list methods |
| **Indexing / Slicing** | Access one item / a portion (`stop` exclusive) |
| **f-string `f"..."`** | Formatted string with `{expression}` |
| **`get(key, default)`** | Safe dictionary lookup |
| **`keys()` / `values()` / `items()`** | Dictionary views for labels, values, pairs |
| **`add` / `discard`** | Set add / safe remove |
| **`len` / `sorted` / `min` / `max` / `sum`** | Built-in collection helpers |
| **Mutable / Immutable** | Can change after creation / cannot |
| **Hashable** | Can be used as a dict key or set item |
| **KeyError / IndexError** | Missing key / invalid index |
