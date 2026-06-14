# DSA: Lists & Strings – Built-in Functions

## What You Will Learn in This Lesson

You have already learned how to write Python programs using **variables**, **operators**, **input/output**, **conditional statements**, and **loops**. Your programs could make decisions and repeat actions — print tables, validate passwords, and process numbers one by one.

In this lesson, you will learn how to store **many values together** in **lists** and how to work with **text** using **strings**. You will access individual items through **indexing** and **slicing**, change lists with methods like **`append`**, **`pop`**, and **`sort`**, and use built-in functions such as **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, and **`sum()`** to process data quickly.

By the end, you will be able to manage shopping lists, student marks, product names, and formatted messages — the same kind of data handling that real apps use every day.

---

## Why Do Programs Need Lists and Strings?

- **Official Definition:** A **list** is an ordered, mutable collection of items in Python. A **string** is an ordered, immutable sequence of characters used to represent text.
- **In Simple Words:** A list is like a numbered row of boxes — each box holds one value and you can add, remove, or change items. A string is like a garland of letters — you read them in order, but you treat the whole garland as one piece of text.
- **Real-Life Example:** Your **Swiggy cart** is a list — item 1 is biryani, item 2 is raita, item 3 is cola. Your **WhatsApp status** is a string — a sequence of characters that form a message.

- **Exam portals** store all subject marks in a **list** and display the student name as a **string**.
- **Train booking apps** keep seat numbers in a **list** and show station names as **strings**.
- **UPI transaction history** is a list of amounts; each payee name is a string.

Without lists, you would create separate variables for every mark, price, or seat — `mark1`, `mark2`, `mark3` — which becomes messy when data grows. Without strings, you could not store names, messages, or formatted output. Lists and strings are the **building blocks of real data** in Python.

![Lists and strings big picture — Swiggy cart as ordered list, exam marks list with student name string, UPI transaction history, tiffin box compartments analogy, and list vs single variable comparison](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-01-lists-strings-big-picture.png?v=20260614)

---

## Understanding Lists — The Big Picture

- **Official Definition:** A **list** in Python is written with square brackets `[]` and can hold items of different types — numbers, strings, booleans, or even other lists.
- **In Simple Words:** A list is a single variable that holds many values in a fixed order.
- **Real-Life Example:** A **tiffin box with compartments** — each compartment has something different (rice, dal, sabzi), but together they form one lunch box.

| Feature | List | Single Variable |
|---------|------|-----------------|
| Holds multiple values | Yes | No — one value only |
| Order matters | Yes — first item stays first unless you change it | N/A |
| Can grow or shrink | Yes — using methods like `append` and `pop` | You replace the whole value |

Lists work naturally with **`for` loops** from your earlier learning — you can visit every item without knowing the count in advance.

---

## Creating and Defining Lists

- **Official Definition:** **List creation** means defining a list literal using square brackets with comma-separated values, or building a list programmatically using methods like `append`.
- **In Simple Words:** You write your items inside `[ ]`, separated by commas.
- **Real-Life Example:** Writing a **grocery list on paper** — "milk, bread, eggs" — each word is one item in order.

```python
# Create lists in different ways
shopping_list = []  # Empty list — no items yet
fruits = ["apple", "banana", "mango"]  # Three string items in order
marks = [78, 85, 92, 64, 88]  # Five integer marks
mixed = ["Rahul", 22, True, 85.5]  # Python allows different types in one list

print(shopping_list)  # Output: []
print(fruits)  # Output: ['apple', 'banana', 'mango']
print(marks)  # Output: [78, 85, 92, 64, 88]

# Start empty and grow with append
daily_tasks = []
daily_tasks.append("Brush teeth")
daily_tasks.append("Check emails")
daily_tasks.append("Attend class")
print(daily_tasks)  # Output: ['Brush teeth', 'Check emails', 'Attend class']
```

**How the code works:**

- Square brackets `[]` tell Python "this is a list." Items are separated by **commas**; order is preserved left to right.
- An empty list `[]` is valid — useful when you will add items later.
- **Common mistake:** Using `( )` instead of `[ ]` — parentheses create a **tuple**, not a list.

---

## Essential List Methods — `append`, `pop`, and `sort`

- **Official Definition:** A **list method** is a function attached to a list object that modifies or queries the list — called with dot notation like `my_list.append(item)`.
- **In Simple Words:** Methods are **actions** your list can do — add an item, remove an item, or arrange items in order.
- **Real-Life Example:** A **train queue** — `append` is someone joining at the back; `pop` is the last person leaving; `sort` is rearranging people by ticket number.

```python
# append — add at the end
team = ["Virat", "Rohit", "Bumrah"]
team.append("Jadeja")
team.append("Shami")
print(team)  # Output: ['Virat', 'Rohit', 'Bumrah', 'Jadeja', 'Shami']

# pop — remove and return an item
snacks = ["samosa", "pakora", "biscuit", "chai"]
removed = snacks.pop()  # Removes last item — chai
print("Removed:", removed)  # Output: Removed: chai
print("Remaining:", snacks)  # Output: ['samosa', 'pakora', 'biscuit']

cities = ["Delhi", "Jaipur", "Goa", "Kerala"]
removed_city = cities.pop(1)  # Index 1 is Jaipur — second item
print("Cancelled:", removed_city)  # Output: Cancelled: Jaipur
print("Updated:", cities)  # Output: ['Delhi', 'Goa', 'Kerala']

# sort — arrange in place
marks = [78, 92, 64, 85, 71]
marks.sort()  # Smallest to largest
print(marks)  # Output: [64, 71, 78, 85, 92]
```

**How the code works:**

- **`append(value)`** adds one item to the **last position**; the list name comes **before** the dot.
- **`pop()`** removes the **last** item; **`pop(i)`** removes the item at index `i`. Calling `pop()` on an **empty list** raises an `IndexError`.
- **`sort()`** changes the **original list** — for descending order use `marks.sort(reverse=True)`.
- **Common mistake:** Mixing numbers and strings in one list and calling `sort()` — Python raises a `TypeError`.

| Method | What It Does | Changes Original List? |
|--------|--------------|------------------------|
| **`append(x)`** | Adds `x` at the end | Yes |
| **`pop()`** | Removes and returns last item | Yes |
| **`pop(i)`** | Removes and returns item at index `i` | Yes |
| **`sort()`** | Arranges items in ascending order | Yes |

![List methods diagram — append adds at end like train queue, pop removes last or indexed item, sort rearranges marks ascending, with method comparison table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-02-list-methods.png?v=20260614)

### Quick Activity: Build and Update a Shopping List

Create an empty list, add four grocery items using **`append`**, remove the last item with **`pop`**, then print the list and its length.

```python
groceries = []
groceries.append("Rice")
groceries.append("Dal")
groceries.append("Milk")
groceries.append("Bread")
print("Before pop:", groceries)
groceries.pop()  # Remove last item — Bread
print("After pop:", groceries)
print("Items to buy:", len(groceries))
```

---

## Accessing List Elements — Indexing

- **Official Definition:** **Indexing** is accessing a single element in a sequence by its **position number**, starting at **0** for the first item. **Negative indexing** uses **-1** for the last item, **-2** for second-to-last, and so on.
- **In Simple Words:** Each item has a seat number — counting starts from **0**, or you count backwards from the end.
- **Real-Life Example:** **Cricket overs** — the first ball is ball 0 in Python's view; **-1** is always the last item.

For `fruits = ["apple", "banana", "mango", "grapes"]`:

| Index | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| Item | apple | banana | mango | grapes |
| Negative | -4 | -3 | -2 | -1 |

```python
fruits = ["apple", "banana", "mango", "grapes"]
print(fruits[0])  # Output: apple — first item
print(fruits[-1])  # Output: grapes — last item
print(fruits[-2])  # Output: mango — second from end

# Change a list item — lists are mutable
marks = [78, 85, 92, 64]
marks[2] = 95  # Change third mark (index 2) from 92 to 95
print(marks)  # Output: [78, 85, 95, 64]
```

**How the code works:**

- Valid indices for a list of length 4 are **0, 1, 2, 3**. The last index is always **`len(list) - 1`**, not `len(list)`.
- **`-1`** is very useful when you do not know the list length.
- **Common mistake:** Using `fruits[4]` for the last item — index 4 is **out of range** and causes an `IndexError`.

![List indexing diagram — positive indices 0 to 3 and negative indices -4 to -1 on fruits list, cricket overs analogy, mutable marks update, and IndexError warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-03-indexing.png?v=20260614)

---

## List Slicing — Getting a Portion of a List

- **Official Definition:** **Slicing** extracts a subsequence from a list using the syntax `list[start:stop:step]`, where `start` is inclusive and `stop` is exclusive.
- **In Simple Words:** Slicing is cutting a **slice** of the list — like taking two idlis from a plate of five.
- **Real-Life Example:** From a **playlist of 10 songs**, you play songs 3 to 5 only — that portion is a slice.

```python
temps = [32, 34, 31, 33, 35, 30, 29]  # Seven days of temperature
print(temps[2:5])  # Output: [31, 33, 35] — indices 2, 3, 4 (not 5)
print(temps[:3])  # Output: [32, 34, 31] — from start to index 3
print(temps[-2:])  # Output: [30, 29] — last two days
print(temps[::2])  # Output: [32, 31, 35, 29] — every second item
print(temps[::-1])  # Output: [29, 30, 35, 33, 31, 34, 32] — reversed
```

**How the code works:**

- **`[start:stop]`** includes index `start` but **stops before** index `stop`.
- **`[:stop]`** starts at 0; **`[start:]`** goes to the end; **`[::step]`** skips items; **`-1`** step reverses.
- The **original list is unchanged** — slicing creates a **new list**.
- **Common mistake:** Expecting `stop` to be inclusive — `[0:3]` gives **3 items** (indices 0, 1, 2), not index 3.

![List slicing diagram — temps[2:5] with exclusive stop, shorthand slices [:3] [-2:] [::2] [::-1], idli plate analogy, and new list created warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-04-list-slicing.png?v=20260614)

### Quick Activity: Slice a Week of Temperatures

Given a list of seven temperatures, print the first three days, the last two days, and the middle day using indexing and slicing.

```python
temps = [31, 33, 32, 35, 34, 30, 29]  # Mon to Sun
print("First three:", temps[:3])  # Output: [31, 33, 32]
print("Last two:", temps[-2:])  # Output: [30, 29]
print("Thursday:", temps[3])  # Output: 35
```

Indexing and slicing work the same way on **strings** — because strings are also ordered sequences.

---

## Strings — Indexing, Slicing, and Concatenation

- **Official Definition:** A **string** is an immutable sequence of Unicode characters in Python, written inside single `' '` or double `" "` quotes. **Concatenation** joins strings end-to-end using **`+`**; **`*`** repeats a string.
- **In Simple Words:** A string is any text stored as a chain of characters. You can glue pieces together with **`+`** or repeat with **`*`**.
- **Real-Life Example:** Your **name on an Aadhaar card** — each letter is one character. Adding **"Ji"** after a name is concatenation.

```python
name = "Priya"
city = 'Delhi'
message = "She said, 'Hello!'"
print(name[0])  # Output: P — first character
print(name[-1])  # Output: a — last character

word = "PYTHON"
print(word[1:4])  # Output: YTH — substring
print(word[::-1])  # Output: NOHTYP — reversed

# Concatenation and repetition
first_name = "Amit"
last_name = "Sharma"
full_name = first_name + " " + last_name
print(full_name)  # Output: Amit Sharma
line = "-" * 30
print(line)  # Output: ------------------------------
```

**How the code works:**

- Strings are **immutable** — you cannot change `name[0] = "p"` like you change a list item.
- A **`for` loop** over a string visits **each character** in order.
- **`+`** joins strings; both sides must be **strings** — `"Age: " + 25` causes `TypeError`; use **`str(25)`** or f-strings.
- **Common mistake:** Forgetting closing quotes — Python shows `SyntaxError: unterminated string`.

![Strings diagram — PYTHON character indexing and slicing, immutability garland analogy, concatenation Amit + Sharma, string repeat with asterisk, and Aadhaar name card example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-05-strings-concatenation.png?v=20260614)

---

## f-String Formatting — Clean and Readable Text Output

- **Official Definition:** An **f-string** (formatted string literal) is a string prefixed with **`f`** that embeds expressions inside **`{ }`** placeholders, evaluated at runtime.
- **In Simple Words:** Write your variables **inside** the sentence in curly braces — Python fills them in automatically.
- **Real-Life Example:** A **receipt template** — "You paid {amount} rupees for {item}" — fill in the blanks when printing.

```python
name = "Deepa"
marks = 87
message = f"{name} scored {marks} marks in Python."
print(message)  # Output: Deepa scored 87 marks in Python.

item = "Notebook"
quantity = 3
price = 45
total = quantity * price
bill = f"Item: {item} | Qty: {quantity} | Total: Rs.{total}"
print(bill)  # Output: Item: Notebook | Qty: 3 | Total: Rs.135

percentage = 87.4567
print(f"Score: {percentage:.2f}%")  # Output: Score: 87.46%
```

**How the code works:**

- The **`f`** before the opening quote enables f-string mode; **`{name}`** is replaced by its value.
- You can write **expressions** inside braces: `f"Total: {50 + 50}"` or `f"{quantity * price}"`.
- **`{percentage:.2f}`** formats a float to **two decimal places**.
- **Common mistake:** Forgetting the **`f`** prefix — without it, `{name}` prints literally as text.

![f-string formatting diagram — receipt template with curly brace placeholders, Deepa scored 87 example, bill with qty and total, :.2f decimal formatting, and missing f prefix mistake](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-06-fstrings.png?v=20260614)

### Quick Activity: Personalised Greeting with f-Strings

Store your name, city, and hobby in variables. Build one f-string sentence that includes all three, plus a calculation.

```python
name = "Sneha"
city = "Pune"
hobby = "painting"
years_left = 30 - 22
intro = f"Hi, I am {name} from {city}. I enjoy {hobby}. In {years_left} years I will turn 30."
print(intro)
```

---

## Built-in Functions — `len()`, `sorted()`, `min()`, `max()`, `sum()`

- **Official Definition:** A **built-in function** is a function provided by Python without importing any library — called by name with arguments in parentheses.
- **In Simple Words:** Built-in functions are **ready-made tools** — measure length, find smallest value, sort data, and more.
- **Real-Life Example:** A **weighing scale at a ration shop** — one tool that tells you the total weight without adding piece by piece.

Built-in functions complement **list methods**: methods like **`sort()`** change the list; functions like **`sorted()`** return a **new sorted list** and leave the original unchanged.

```python
fruits = ["apple", "banana", "mango"]
marks = [78, 92, 64, 85, 71]
word = "Python"

print(len(fruits))  # Output: 3
print(len(word))  # Output: 6
print(fruits[len(fruits) - 1])  # Output: mango — last item

sorted_marks = sorted(marks)  # New sorted list
print("Original:", marks)  # Output: [78, 92, 64, 85, 71] — unchanged
print("Sorted:", sorted_marks)  # Output: [64, 71, 78, 85, 92]

print(min(marks))  # Output: 64
print(max(marks))  # Output: 92
print(sum(marks))  # Output: 370

average = sum(marks) / len(marks)
print(f"Average: {average:.2f}")  # Output: Average: 74.00
```

**How the code works:**

- **`len(x)`** counts items — use **`len(fruits)`**, not `fruits.len()`.
- **`sorted(marks)`** returns a **new list**; **`marks.sort()`** changes **`marks`** in place and returns **`None`**.
- **`min()`** / **`max()`** need comparable items — mixing numbers and strings causes **`TypeError`**.
- **`sum()`** only works when **all items are numbers**.

| Function | Works On | Returns | Changes Original? |
|----------|----------|---------|-------------------|
| **`len(x)`** | List, string, etc. | Count of items | No |
| **`sorted(x)`** | List, string, etc. | New sorted list | No |
| **`min(x)`** | List of comparable items | Smallest item | No |
| **`max(x)`** | List of comparable items | Largest item | No |
| **`sum(x)`** | List of numbers | Total of all numbers | No |

![Built-in functions diagram — len counts items, sorted returns new copy, min and max find extremes, sum totals marks with average formula, ration shop scale analogy, and sorted vs sort comparison](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session04/session04-07-builtin-functions.png?v=20260614)

---

## Putting It Together — A Class Report Program

Real programs combine creation, access, methods, and built-in functions in one flow.

```python
students = ["Anita", "Rohit", "Priya"]
marks = [78, 92, 85]

students.append("Karan")
marks.append(64)

total = sum(marks)
count = len(marks)
average = total / count
top_score = max(marks)
top_index = marks.index(top_score)
top_student = students[top_index]

print("--- Class Report ---")
print(f"Students: {students}")
print(f"Marks: {marks}")
print(f"Average: {average:.2f}")
print(f"Highest: {top_score} by {top_student}")
print(f"Sorted marks: {sorted(marks)}")
```

**How the code works:**

- **`append`** keeps names and marks lists growing together — keep them in **sync** (same order).
- **`sum`**, **`len`**, **`max`**, **`sorted`** answer common questions without manual loops.
- **`marks.index(top_score)`** finds **where** the highest mark sits so you can get the matching name.

---

## Practice Programs — Beginner List and String Exercises

### Exercise 1: Analyse a Marks List

Given a list of five marks, compute total, average, highest, lowest, and a sorted copy — then print everything using f-strings.

```python
marks = [72, 88, 65, 91, 77]
print(f"Marks: {marks}")
print(f"Total: {sum(marks)}")
print(f"Average: {sum(marks) / len(marks):.2f}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")
print(f"Sorted: {sorted(marks)}")
```

### Exercise 2: String Indexing and Reversal

Take the string `"AGENTIC"`. Print the first character, last character, middle three characters, and the reversed string.

```python
word = "AGENTIC"
print("First:", word[0])  # Output: A
print("Last:", word[-1])  # Output: C
print("Middle:", word[2:5])  # Output: ENT
print("Reversed:", word[::-1])  # Output: CITNEGA
```

### Exercise 3: Build a Formatted Bill

Store item name, quantity, and price. Use an f-string to print a one-line bill with the calculated total.

```python
item = "Notebook"
quantity = 3
price = 45
print(f"Item: {item} | Qty: {quantity} | Price: Rs.{price} | Total: Rs.{quantity * price}")
```

---

## Debugging Lists and Strings

- **Print the list or string** after each change — especially after **`append`**, **`pop`**, or **`sort`**.
- **Check index bounds:** Valid indices run from **`0`** to **`len(list) - 1`**. Use **`-1`** for the last item.
- **Remember slice stop is exclusive:** `[0:3]` gives three items, not four.
- **Do not mix types carelessly:** Sorting or comparing lists with mixed types causes errors.
- **Trace with small examples:** Test on 3-item lists before large datasets.

```python
data = ["a", "b", "c"]
print("Length:", len(data))  # Output: 3
print("Valid indices: 0 to", len(data) - 1)  # Output: 0 to 2
print("Last item:", data[-1])  # Safe way to get last item
```

---

## Key Takeaways

- **Lists** store ordered, changeable collections — create with **`[]`**, grow with **`append`**, shrink with **`pop`**, and reorder with **`sort`**.
- **Indexing** (positive and negative) and **slicing** let you read or copy portions of lists and strings without rewriting data.
- **Strings** represent text; use **concatenation** for simple joins and **f-strings** for readable formatted output with variables and expressions.
- **Built-in functions** — **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, **`sum()`** — answer common data questions quickly without writing loops for every task.
- These skills connect directly to **functions, dictionaries, and data processing** — where lists and strings carry the information your programs analyse and act on.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **List `[]`** | Ordered, mutable collection of items |
| **String `' '` / `" "`** | Ordered, immutable sequence of characters (text) |
| **`append(x)`** | Adds item `x` to the end of a list |
| **`pop()`** | Removes and returns the last list item |
| **`pop(i)`** | Removes and returns the item at index `i` |
| **`sort()`** | Sorts the list in place (ascending by default) |
| **Positive index** | Position from start — first item is index `0` |
| **Negative index** | Position from end — last item is index `-1` |
| **Slicing `[start:stop:step]`** | Extracts a portion; `stop` is exclusive |
| **Concatenation `+`** | Joins strings end-to-end |
| **String repeat `*`** | Repeats a string a given number of times |
| **f-string `f"..."`** | Formatted string with `{variable}` placeholders |
| **`len(x)`** | Returns count of items in a list or characters in a string |
| **`sorted(x)`** | Returns a new sorted list; original unchanged |
| **`min(x)`** | Returns the smallest item in an iterable |
| **`max(x)`** | Returns the largest item in an iterable |
| **`sum(x)`** | Returns the total of numeric items in a list |
| **Mutable** | Can be changed after creation (lists are mutable) |
| **Immutable** | Cannot be changed in place (strings are immutable) |
| **IndexError** | Raised when an index is outside valid range |
| **Iterable** | A sequence Python can loop over or pass to built-in functions |
| **Method** | Function called on an object with dot notation — `list.append()` |
| **Built-in function** | Ready-made Python function — `len()`, `sum()`, etc. |
