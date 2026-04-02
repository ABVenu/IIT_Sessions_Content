# Lecture Script: Session 05 — Strings, Dictionaries, Lists, and Classes

**Session duration:** 2 hours 15 minutes  


**How to use this file:** Each block states *what happens in the room* and its **duration in minutes**. This is timing and facilitation—definitions and figures live in Lecture Notes, slides, or the board. Use the code blocks as live-demo or screen-share prompts, not line-by-line reading.

**Break (only planned pause):** After roughly **60–75 minutes** of session clock time (after dictionary merging / before or early in the list segment), take **one** pause of **5–8 minutes**, then continue. Numbered sections below are teaching segments—not separate “break” rows.

---

## 1. Welcome and roadmap (2 minutes)

- Greet; confirm access to the environment you use (IDE, notebook, or PDF Notes).
- Name the four threads for the session: **strings** (text), **dictionaries** (labeled data), **lists** (built-ins and methods students will reuse everywhere), and **classes** / objects / **`__init__`**.
- Set expectation: Notes use **one or two examples per idea**—in class, stress **why** each pattern exists rather than multiplying variants; stay within **2 hours 15 minutes** by trimming optional asides (not by dropping the list block or **`__init__`**) if discussion runs long.

---

## 2. LO–9.1.5 — Implementing string data types for text (16 minutes)

### CS Theory Bite

**Say:** Python 3 strings are **Unicode** text. They are **immutable**: methods like `upper()` return *new* strings; the original stays unchanged. That safety matters for hashing and sharing data.

### Hook

**Say:** Everything users type — names, IDs, file paths — is string work.

```python
username = "alice_2024"
message = "He said, 'Hello!'"
```

### Quotes, concatenation, repetition, `len`

**Say:** Single or double quotes are equivalent; mix them to avoid escaping. Combine with `+`, repeat with `*`, and use `str(...)` before concatenating numbers.

```python
result = "Hello" + " " + "World"
message = "Age: " + str(25)
line = "=" * 20
len("Alice")  # 5
```

**Say:** Multi-line text uses triple quotes — see Lecture Notes if you show an example on screen.

### Common methods (one demo block)

**Say:** Normalise text with `strip`, case methods, `replace`, and prefix checks.

```python
name = "  alice  "
print(name.strip().title())
print("Hello World".replace("World", "Python"))
email = "user@example.com"
print(email.startswith("user"), "@" in email)
```

### Practice (single example)

**Say:** Build a display name from parts — reinforces `+` or an f-string.

```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
# or: f"{first_name} {last_name}"
```

### Summary (strings)

1. Strings are immutable sequences of characters.
2. Use `+`, `*`, `len`, `str()` for basic operations.
3. Prefer `strip` / case / `replace` / `startswith` / `in` for cleaning and checks.

---

## 3. LO–9.2.18 — Creating and initializing dictionaries (11 minutes)

### CS Theory Bite

**Say:** A dict is a **hash map**: average O(1) lookup by key. Python 3.7+ remembers insertion order.

### Hook

**Say:** Lists give position; dicts give **meaning**.

```python
student = ['Alice', 22, 'A', 'alice@mail.com']  # what is index 2?
student = {'name': 'Alice', 'age': 22, 'grade': 'A', 'email': 'alice@mail.com'}
print(student['grade'])
```

### Creating

**Say:** Literals, `dict(...)`, comprehensions, `fromkeys`, empty `{}`.

```python
person = {'name': 'Alice', 'age': 25}
person = dict(name='Alice', age=25)
squares = {x: x**2 for x in range(1, 6)}
subjects = dict.fromkeys(['Math', 'Science', 'English'], 0)
```

### Keys and values

**Say:** Keys unique and **immutable**; values any type. Show one invalid key in a comment.

```python
d = {'name': 'Alice', 42: 'answer'}
# d = {[1, 2]: 'x'}  # TypeError
```

### Nested dicts (compact)

```python
students = {
    'Alice': {'age': 22, 'grade': 'A'},
    'Bob': {'age': 24, 'grade': 'B'},
}
print(students['Alice']['grade'])
```

### Practical pattern — frequency

```python
text = "the cat sat on the mat the cat"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
```

### Summary

1. Dicts store key–value pairs; keys hashable and unique.
2. Create with `{}`, `dict`, comprehensions, `fromkeys`.
3. Nesting models structured data; `.get` + increment counts occurrences.

---

## 4. LO–9.2.19 — Accessing values (`[]` vs `.get()`) (11 minutes)

### CS Theory Bite

**Say:** `d[k]` is fail-fast; `d.get(k, default)` is fail-safe — design choice, not speed difference for the lookup itself.

### Hook

```python
user_data = {'name': 'Alice', 'age': 25}
# user_data['email']  # KeyError
email = user_data.get('email', 'no-email@default.com')
```

### Brackets vs `get`

```python
student = {'name': 'Alice'}
print(student['name'])
print(student.get('email', 'not set'))
```

**Say:** Word counting again: `counts[w] = counts.get(w, 0) + 1` — same pattern as the dict-creation section; do not re-type a long new story.

### `keys`, `values`, `items`

```python
person = {'name': 'Alice', 'age': 25}
for key, val in person.items():
    print(f"{key}: {val}")
```

### Nested — chained `get`

```python
data = {'user': {'name': 'Alice', 'address': {'city': 'Mumbai'}}}
city = data.get('user', {}).get('address', {}).get('city', 'Unknown')
```

### `in` on keys (preview)

**Say:** `'k' in d` tests **keys** only; full `in` lesson comes in the next dict block.

### Summary

1. `[]` when the key must exist; `get` when it might not.
2. `.items()` for loops; chain `.get(..., {})` for nested paths.
3. Combine with membership checks when you branch on existence.

---

## 5. LO–9.2.20 — Adding and modifying entries (11 minutes)

### CS Theory Bite

**Say:** `d[k] = v` is an **upsert**: insert or overwrite in one syntax.

### Hook

```python
user = {'name': 'Alice'}
user['email'] = 'alice@mail.com'
user['plan'] = 'premium'  # was 'free' in your story arc
```

### Assignment & `update`

```python
student = {'name': 'Alice', 'age': 22}
student['grade'] = 'A'
student.update({'age': 23, 'city': 'Mumbai'})
```

### `setdefault`

**Say:** Sets a key only if missing; returns the value. Skip the long “group by first letter” demo unless time allows.

```python
config = {'theme': 'dark'}
config.setdefault('language', 'en')
```

### Counter pattern

**Say:** Same line as before: `counts[k] = counts.get(k, 0) + 1`.

### Merge recap (light)

```python
defaults = {'theme': 'light', 'lang': 'en'}
user_prefs = {'theme': 'dark'}
defaults |= user_prefs  # in-place, 3.9+
```

### Summary

1. One syntax adds and updates: `d[k] = v`.
2. `update` / `|=` for batches; `setdefault` for “fill if absent”.
3. Counting and merging reappear — tie them to real config/state examples.

---

## 6. LO–9.2.21 — Removing entries (`del`, `pop`, `popitem`, `clear`) (9 minutes)

### CS Theory Bite

**Say:** Choose `del` for discard-only; `pop` when you need the value; `popitem` for LIFO processing; `clear` to reset.

### Hook — redacting fields

```python
user = {'name': 'Alice', 'email': 'a@x.com', 'password': 'secret'}
safe = user.copy()
safe.pop('password', None)
```

### Combined demo (matches condensed notes)

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
del student['grade']
student.pop('age')
student.popitem()
student.clear()

data = {'a': 1, 'b': 2, 'c': 3}
for key in ['b', 'd']:
    data.pop(key, None)
```

**Say:** Never delete keys while iterating the dict directly — collect keys first.

### Summary

- `del d[k]` — no return; errors if missing.
- `pop(k, default)` — safe multi-key cleanup.
- `popitem` / `clear` for stack-like or full reset.

---

## 7. LO–9.2.22 — Checking keys with `in` (7 minutes)

### CS Theory Bite

**Say:** `in` on dicts uses hash lookup on **keys**. Values need `.values()`.

### Hook

```python
response = {'status': 'ok'}
# response['error']  # KeyError
```

### Basics

```python
user = {'name': 'Alice', 'age': 25}
print('email' in user)

config = {'port': 8080}
if 'host' not in config:
    config['host'] = 'localhost'
```

**Say:** Contrast `in` (branching) vs `.get` (fallback) vs `try/except KeyError` (EAFP).

### Summary

1. `k in d` tests keys; `v in d.values()` tests values.
2. Pair checks with safe access patterns from earlier blocks.

---

## 8. LO–9.2.23 — Iterating keys, values, and items (9 minutes)

**Say:** Views are live; `for k in d` equals `for k in d.keys()`.

```python
student = {'name': 'Alice', 'age': 22}
for key, value in student.items():
    print(f"{key}: {value}")

prices = {'apple': 1.50, 'banana': 0.75}
total = sum(prices.values())
```

### Comprehensions and `max`

```python
scores = {'Alice': 92, 'Bob': 45}
passing = {name: s for name, s in scores.items() if s >= 50}
top_student = max(scores, key=scores.get)
```

**Say:** Use `sorted(d)` or `sorted(d, key=d.get)` when order matters — mention once, optional 30-second screen share.

### Summary

1. Prefer `.items()` when you need both key and value.
2. Comprehensions and `max(d, key=d.get)` are high-leverage idioms.
3. Do not mutate a dict while iterating it.

---

## 9. LO–9.2.24 — Merging dictionaries (9 minutes)

### CS Theory Bite

**Say:** Layered config is the mental model: defaults, then env, then CLI — **right-hand wins** on key clashes.

### Hook

```python
defaults = {'debug': False, 'port': 3000}
user = {'port': 8080, 'debug': True}
config = {**defaults, **user}
```

### `update` in place

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}
d1.update(d2)
```

### New dict without touching originals

**Say:** `{**a, **b}` or `a | b` (3.9+). Shallow merge only — nested dicts replace wholesale; show the one-line pitfall from the Notes if time remains.

### Practical stack

```python
default_config = {'debug': False, 'port': 3000}
env_config = {'port': 8080}
cli_config = {'debug': True}
final_config = {**default_config, **env_config, **cli_config}
```

### Summary

1. `update` mutates; unpacking and `|` produce new dicts.
2. Later layers override earlier for the same key.
3. Deep merge needs custom logic.

---

## 10. List essentials — built-ins and common methods (14 minutes)

**Say:** Lists are **mutable** sequences. Students will use these APIs with dicts and strings constantly — this block bridges dicts to classes.

### Built-in functions (any iterable; lists are the usual case)

**Say:** Name each: `len`, `sum`, `max`/`min`, `sorted` (new list), `reversed` (iterator), `enumerate`, `zip`.

```python
nums = [3, 1, 4]
print(len(nums), sum(nums), sorted(nums))
for i, x in enumerate(nums):
    print(i, x)
```

**Say:** Contrast **`sorted(x)`** (returns new list) vs **`x.sort()`** (in-place, returns `None`) — classic exam question.

### List methods

**Say:** `append` vs `extend`, `insert`, `pop`, `remove`, `sort`, `reverse`, `count`, `index`.

```python
items = [2, 3, 2]
items.append(5)
items.sort()
```

### Summary

1. Built-ins summarize and transform without mutating (except you assign back).
2. Methods mutate the list in place for `append`/`sort`/etc.
3. This section supports the next exercise: lists of objects.

---

## 11. LO–9.3.19 — Define classes as blueprints (11 minutes)

### CS Theory Bite

**Say:** Classes bundle state and behavior (**encapsulation**). Naming: **PascalCase**.

### Hook

**Say:** Start minimal — method only — then add state in the `__init__` lesson.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()
```

### Syntax

```python
class ClassName:
    pass
```

### Summary

1. `class` + PascalCase name.
2. Methods take `self` as the first parameter.
3. Class is blueprint; object is instance.

---

## LO–9.3.20: Create objects (instances) (11 minutes)

### CS Theory Bite

**Say:** `ClassName()` constructs an object on the heap; GC reclaims it when unreferenced.

### Independence

```python
class Student:
    def __init__(self, name):
        self.name = name

alice = Student("Alice")
bob = Student("Bob")
alice.name = "Alicia"
print(alice.name, bob.name)
```

### Realistic example — bank accounts

**Say:** Same narrative as Notes: two accounts, deposits and withdrawals stay separate.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)
```

### Objects in collections

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [Product("Laptop", 999), Product("Mouse", 25)]
total = sum(p.price for p in products)
```

### Identity vs equality (optional — 2 minutes max)

**Say:** `is` is same object in memory; `==` defaults to identity until you implement `__eq__`. Do **not** implement `__eq__` live unless the cohort is advanced — state that it exists for a later OOP session.

### Summary

1. Each call to the class constructor makes a new instance.
2. State changes on one instance do not touch siblings.
3. Objects live naturally in lists and dicts.

---

## 13. LO–9.3.21 — Implement `__init__` (11 minutes)

### CS Theory Bite

**Say:** `__new__` allocates; `__init__` initializes — what learners colloquially call the constructor.

### Why it exists

**Say:** Without `__init__`, attributes may never be set; with it, creation **forces** required fields.

### Pattern — with vs without

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Buddy", "Labrador")
```

### `self`

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
```

### Validation and derived attributes (one slide)

```python
class Person:
    def __init__(self, name, age):
        self.name = name or "Unknown"
        self.age = max(0, age)

class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.salary = hourly_rate * hours_worked
```

### No-argument `__init__`

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count)
```

### Common mistakes (verbal checklist)

**Say:** (1) assign with `self.attr`, not bare locals; (2) include `self` in the parameter list; (3) indent the class body.

### Summary

1. `__init__` runs automatically on construction.
2. Use it for required fields, validation, and derived values.
3. `self` is the instance being initialized.

---

## 14. Wrap-up and next steps (3 minutes)

- Tie the session together: strings and dicts cover most **data-shape** problems; lists are the usual **collection** workhorse; classes add **behavior** and invariants—point to matching sections in Lecture Notes and Pre-Read.
- One-minute **muddiest point** or two short questions; remind where to submit work or what prepares for the next session.
- Thank-you; dismiss.

---

### Timing flex

If you need time back in the first half, shorten **segment 8** (iteration—mention `sorted` only in speech) or **segment 9** (merge—demo `update` plus one of `{**a, **b}` or `|`, not both). If **segment 13** (`__init__`) finishes early, use spare minutes for **Q&A** on `is` vs `==` or shallow merges, without turning it into a new topic.
