# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A **Swiggy-style grocery app** builds a cart from scratch. A developer writes:

```python
cart = []
cart.append("Rice")
cart.append("Dal")
cart.append("Milk")
print(len(cart))
```

What is printed?

A. `0`  
B. `1`  
C. `3`  
D. `['Rice', 'Dal', 'Milk']`

**Correct Answer:** C

**Answer Explanation:**  
Each **`append()`** adds one item to the end of the list. After three appends, the list has **3 items**, and **`len(cart)`** returns **3**.

**Why other options are wrong:**  
- A and B: The list is not empty after three `append` calls.  
- D: `len()` returns a **number**, not the list itself.

---

## Q2 (MCQ, Easy)

A **festival countdown board** stores names in order:

```python
festivals = ["Holi", "Diwali", "Eid", "Christmas"]
print(festivals[0])
```

What is printed?

A. `Holi`  
B. `Diwali`  
C. `1`  
D. `IndexError`

**Correct Answer:** A

**Answer Explanation:**  
Python lists use **0-based indexing**. The **first** item is at index **`0`**, which is **`"Holi"`**.

**Why other options are wrong:**  
- B: `"Diwali"` is at index `1`.  
- C: Indexing returns the **item**, not its position number.  
- D: Index `0` is valid for a list of length 4.

---

## Q3 (MCQ, Easy)

A **typing tutor app** checks character positions in the word `"Python"`.

Which index correctly refers to the **last character** `'n'` using **positive** indexing?

A. `6`  
B. `5`  
C. `0`  
D. `-6`

**Correct Answer:** B

**Answer Explanation:**  
`"Python"` has **6 characters**, so valid positive indices are **`0` through `5`**. The last character **`'n'`** is at index **`5`** (`len(word) - 1`).

**Why other options are wrong:**  
- A: Index `6` is **out of range** and would raise `IndexError`.  
- C: Index `0` is the first character `'P'`.  
- D: `-6` is valid negative indexing for `'P'`, not the last character (`-1` would be `'n'`).

---

## Q4 (MCQ, Easy)

A beginner stores team names but accidentally uses the wrong brackets:

```python
team_a = (10, 20, 30)   # Line 1
team_b = [10, 20, 30]   # Line 2
```

Which statement is **correct**?

A. Both `team_a` and `team_b` are Python lists  
B. `team_a` is a list; `team_b` is a tuple  
C. `team_b` is a list; `team_a` is a tuple  
D. Both are tuples

**Correct Answer:** C

**Answer Explanation:**  
**Square brackets `[ ]`** create a **list**. **Parentheses `( )`** with comma-separated values create a **tuple** — not a list.

**Why other options are wrong:**  
- A: Parentheses do not create a list.  
- B: The bracket types are swapped.  
- D: Line 2 clearly uses `[ ]`, which is a list.

---

## Q5 (MCQ, Moderate)

A **weather dashboard** stores seven daily temperatures (in °C):

```python
temps = [32, 34, 31, 33, 35, 30, 29]
print(temps[2:5])
```

What is printed?

A. `[31, 33, 35]`  
B. `[34, 31, 33]`  
C. `[31, 33, 35, 30]`  
D. `[32, 34, 31]`

**Correct Answer:** A

**Answer Explanation:**  
Slicing **`[2:5]`** includes indices **2, 3, and 4** and **stops before 5**. Those values are **`31`, `33`, and `35`**.

**Why other options are wrong:**  
- B: Starts at index 1, not 2.  
- C: Includes index 5 (`30`), but `stop` is **exclusive**.  
- D: That slice would be `temps[:3]`.

---

## Q6 (MCQ, Moderate)

A **stationery shop** updates inventory after a sale:

```python
items = ["Pen", "Pencil", "Eraser", "Sharpener"]
removed = items.pop(1)
print(removed)
print(items)
```

What is printed (two lines)?

A. `Pencil` then `['Pen', 'Eraser', 'Sharpener']`  
B. `Pen` then `['Pencil', 'Eraser', 'Sharpener']`  
C. `Eraser` then `['Pen', 'Pencil', 'Sharpener']`  
D. `Pencil` then `['Pen', 'Pencil', 'Eraser', 'Sharpener']`

**Correct Answer:** A

**Answer Explanation:**  
**`pop(1)`** removes and returns the item at **index 1** — **`"Pencil"`**. The remaining list is **`['Pen', 'Eraser', 'Sharpener']`**.

**Why other options are wrong:**  
- B: Index 1 is not `"Pen"`.  
- C: Index 1 is not `"Eraser"`.  
- D: `pop` **removes** the item — the list cannot still contain `"Pencil"`.

---

## Q7 (MSQ, Moderate)

A **college attendance app** stores roll numbers in a Python list.

Which statements about **lists** are **correct**?

A. Lists are **mutable** — you can change an item after creation (e.g., `marks[2] = 95`)  
B. **`append(x)`** adds a single item to the **end** of the list  
C. Writing `grades = (90, 85, 88)` creates a mutable list  
D. An empty list `[]` is valid and can be grown later with `append`

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: Lists allow in-place updates by index.  
- B: `append` always adds at the **last position**.  
- D: Empty lists are a standard pattern before collecting data in a loop.  
- C is **false**: parentheses create a **tuple**, which is not the same as a mutable list.

**Why other options are wrong:**  
- C: `( )` does not create a list.

---

## Q8 (MSQ, Moderate)

A **campus ID card kiosk** builds a display line from a student's name and age:

```python
name = "Riya"
age = 20
line = "Student: " + name + " | Age: " + str(age)
```

Which statements about **strings and concatenation** are **correct**?

A. **`+`** joins strings end to end when both sides are strings  
B. **`str(age)`** converts the integer `20` to the string `"20"` so it can be joined with text  
C. **`"Age: " + age`** works without `str()` because Python auto-converts numbers in `+`  
D. Strings are **immutable** — you cannot change a single character in place like `name[0] = "r"`

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A and B: Concatenation requires **string operands**; numbers must be converted with **`str()`**.  
- D: Strings cannot be updated by index assignment.  
- C is **false**: `"Age: " + 20` raises **`TypeError`** — Python does not auto-convert for `+`.

**Why other options are wrong:**  
- C: Mixing `str` and `int` with `+` causes a type error.

---

## Q9 (MSQ, Hard)

A **exam marks portal** processes scores:

```python
marks = [78, 92, 64, 85]
backup = marks[:]
marks.sort(reverse=True)
```

Which statements are **correct**?

A. After `sort(reverse=True)`, `marks` becomes `[92, 85, 78, 64]`  
B. `backup` remains `[78, 92, 64, 85]` because slicing created a **new list**  
C. `marks.sort(reverse=True)` returns a new sorted list and leaves `marks` unchanged  
D. Calling `sort()` on a list that mixes integers and strings (e.g., `[1, "two"]`) can raise `TypeError`

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: Descending sort arranges from largest to smallest.  
- B: **`marks[:]`** copies into a separate list; `sort()` changes **`marks` only**.  
- D: Python cannot compare incompatible types during sorting.  
- C is **false**: **`sort()`** modifies the list **in place** and returns **`None`**, not a new list.

**Why other options are wrong:**  
- C: Confuses **`sort()`** (in-place method) with a non-mutating copy-returning pattern.

---

## Q10 (MSQ, Hard)

A **fitness tracker** stores five daily step counts:

```python
steps = [4500, 8200, 6100, 9800, 7200]
total = sum(steps)
count = len(steps)
average = total / count
peak = max(steps)
low = min(steps)
```

Which statements are **correct**?

A. `total` is `35800`  
B. `count` is `5`  
C. `sum(steps)` removes the largest value from the list before returning the total  
D. `peak` is `9800` and `low` is `4500`

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: `4500 + 8200 + 6100 + 9800 + 7200 = 35800`.  
- B: The list has **five** integers.  
- D: **`max()`** finds the highest; **`min()`** finds the lowest — neither changes the list.  
- C is **false**: **`sum()`** only **adds** values; it does **not** remove anything from the list.

**Why other options are wrong:**  
- C: Built-in `sum()` does not modify the original list.
