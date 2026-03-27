## Creating and Initializing Lists in Python

### Hook (2 minutes)

**Scenario:**
You're building a shopping app and need to store a user's cart items. Or tracking daily temperatures for a week. Managing student grades for a class. Collecting user responses in a survey.

All these scenarios require storing multiple related values. You could create separate variables:

```python
temp_monday = 72
temp_tuesday = 75
temp_wednesday = 68
temp_thursday = 71
temp_friday = 73
temp_saturday = 76
temp_sunday = 74
```

But this is tedious, error-prone, and doesn't scale. What if you need to track 365 days?

**Enter lists** - Python's most versatile data structure for storing ordered collections of items.

**What You'll Learn:**
1. Create empty lists and lists with initial values
2. Understand list syntax and structure
3. Create lists with different data types
4. Use list() constructor
5. Create lists from strings and ranges
6. Build nested lists for multi-dimensional data

---

### CS Theory Bite

> **Origin**: Lists implement **dynamic arrays** — automatically resizing arrays invented for **FORTRAN** (1957). Python lists use **over-allocation** (extra space) to make `append()` amortized O(1).
>
> **Analogy**: A list is like a **numbered shelf** — items sit in order, you can add/remove from any position, and the shelf grows as needed.
>
> **Why it matters**: Lists are Python's most versatile data structure — used in 90% of programs.



### Section 1: Creating Empty Lists (3 minutes)

**Method 1: Square Brackets**

```python
# Empty list using []
shopping_cart = []
print(shopping_cart)  # []
print(type(shopping_cart))  # <class 'list'>
```

**Method 2: list() Constructor**

```python
# Empty list using list()
tasks = list()
print(tasks)  # []
print(type(tasks))  # <class 'list'>
```

**When to Use Each:**
- `[]` - Most common, concise, preferred
- `list()` - Useful for converting other types to lists

**Checking if Empty:**

```python
cart = []

if cart:
    print("Cart has items")
else:
    print("Cart is empty")
# Output: Cart is empty

# Or explicitly check length
if len(cart) == 0:
    print("No items")
# Output: No items
```

---

### Section 2: Creating Lists with Initial Values (4 minutes)

**List Literals:**

```python
# List of integers
scores = [85, 92, 78, 95, 88]
print(scores)  # [85, 92, 78, 95, 88]

# List of strings
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# List of floats
prices = [19.99, 29.99, 9.99, 49.99]
print(prices)  # [19.99, 29.99, 9.99, 49.99]

# List of booleans
flags = [True, False, True, True]
print(flags)  # [True, False, True, True]
```

**Mixed Data Types:**

```python
# Lists can contain different types
student = ['Alice', 21, 3.8, True]
print(student)
# ['Alice', 21, 3.8, True]
# Name, age, GPA, is_enrolled
```

**Single Element Lists:**

```python
# Single element (note the comma is optional but clear)
single = [42]
print(single)  # [42]
print(len(single))  # 1
```

**Lists with Duplicates:**

```python
# Duplicates are allowed
numbers = [1, 2, 2, 3, 3, 3, 4]
print(numbers)  # [1, 2, 2, 3, 3, 3, 4]
print(len(numbers))  # 7
```

---

### Section 3: Creating Lists from Other Sequences (3 minutes)

**From Strings:**

```python
# Convert string to list of characters
word = "Python"
letters = list(word)
print(letters)
# ['P', 'y', 't', 'h', 'o', 'n']

# Split string into list of words
sentence = "Hello world from Python"
words = sentence.split()
print(words)
# ['Hello', 'world', 'from', 'Python']

# Split with custom delimiter
csv_data = "apple,banana,orange"
fruits = csv_data.split(',')
print(fruits)
# ['apple', 'banana', 'orange']
```

**From Range:**

```python
# Create list from range
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# Range with start and stop
evens = list(range(2, 11, 2))
print(evens)  # [2, 4, 6, 8, 10]

# Countdown
countdown = list(range(10, 0, -1))
print(countdown)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**From Tuples:**

```python
# Convert tuple to list
coordinates = (10, 20, 30)
coord_list = list(coordinates)
print(coord_list)  # [10, 20, 30]
```

---

### Section 4: Nested Lists (3 minutes)

**2D Lists (Lists of Lists):**

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access rows
print(matrix[0])  # [1, 2, 3]
print(matrix[1])  # [4, 5, 6]

# Access elements
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8
```

**Practical Example - Student Grades:**

```python
# Each inner list: [name, math, science, english]
students = [
    ['Alice', 85, 90, 88],
    ['Bob', 78, 82, 86],
    ['Charlie', 92, 89, 94]
]

# Access student data
print(students[0])  # ['Alice', 85, 90, 88]
print(students[0][0])  # 'Alice'
print(students[0][1])  # 85 (math score)

# Calculate average for first student
math, sci, eng = students[0][1], students[0][2], students[0][3]
average = (math + sci + eng) / 3
print(f"Alice's average: {average}")  # 87.67
```

**Jagged Lists (Uneven Nested Lists):**

```python
# Not all sublists need same length
shopping_lists = [
    ['milk', 'eggs', 'bread'],
    ['apples', 'bananas'],
    ['chicken', 'rice', 'beans', 'cheese']
]

for i, items in enumerate(shopping_lists):
    print(f"List {i+1} has {len(items)} items: {items}")
# List 1 has 3 items: ['milk', 'eggs', 'bread']
# List 2 has 2 items: ['apples', 'bananas']
# List 3 has 4 items: ['chicken', 'rice', 'beans', 'cheese']
```

---

### Section 5: Special List Creation Patterns (2 minutes)

**Repeated Elements:**

```python
# Create list with repeated values
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

# Repeated strings
dashes = ['-'] * 10
print(dashes)
# ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

# Repeated lists (be careful!)
matrix = [[0] * 3] * 3  # DON'T DO THIS!
print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Problem: All rows reference same list
matrix[0][0] = 1
print(matrix)
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  # All rows changed!

# Correct way (covered in comprehensions later)
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]  # Only first row changed
```

**Concatenation:**

```python
# Combine lists with +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Multiple lists
odds = [1, 3, 5]
evens = [2, 4, 6]
tens = [10, 20, 30]
all_numbers = odds + evens + tens
print(all_numbers)
# [1, 3, 5, 2, 4, 6, 10, 20, 30]
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Temperature Tracking**

```python
# Week of temperatures
temperatures = [72, 75, 68, 71, 73, 76, 74]

print(f"Temperatures for the week: {temperatures}")
print(f"Number of days: {len(temperatures)}")

# Find average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.1f}°F")
# Average temperature: 72.7°F
```

**Application 2: Shopping Cart**

```python
# Items with prices
cart = [
    ['Laptop', 999.99],
    ['Mouse', 29.99],
    ['Keyboard', 79.99],
    ['Monitor', 299.99]
]

print("Shopping Cart:")
total = 0
for item in cart:
    name, price = item[0], item[1]
    print(f"  {name}: ${price}")
    total += price

print(f"\nTotal: ${total}")
# Total: $1409.96
```

**Application 3: Survey Responses**

```python
# Collect responses
responses = []

# Simulate adding responses
responses = [5, 4, 5, 3, 4, 5, 4, 5, 3, 5]

print(f"Total responses: {len(responses)}")

# Count 5-star ratings
five_stars = responses.count(5)
print(f"5-star ratings: {five_stars}")

# Calculate satisfaction rate
satisfaction_rate = (five_stars / len(responses)) * 100
print(f"Satisfaction rate: {satisfaction_rate}%")
# Satisfaction rate: 50.0%
```

**Application 4: Course Schedule**

```python
# Days and times for classes
schedule = [
    ['Monday', '9:00 AM', 'Math'],
    ['Monday', '11:00 AM', 'English'],
    ['Tuesday', '10:00 AM', 'Science'],
    ['Wednesday', '9:00 AM', 'Math'],
    ['Thursday', '2:00 PM', 'History'],
    ['Friday', '10:00 AM', 'Science']
]

print("Weekly Schedule:")
for class_info in schedule:
    day, time, subject = class_info
    print(f"{day} at {time}: {subject}")
```

---

### Summary (1 minute)

**Key Concepts Covered:**

1. **Creating Empty Lists:**
   - `[]` - preferred
   - `list()` - constructor

2. **Lists with Values:**
   - `[1, 2, 3]` - direct initialization
   - Can hold any type
   - Duplicates allowed
   - Order matters

3. **From Other Types:**
   - `list(string)` - characters
   - `string.split()` - words
   - `list(range(n))` - numbers
   - `list(tuple)` - from tuple

4. **Nested Lists:**
   - Lists within lists
   - Access with multiple indices
   - 2D matrices, tables

5. **Special Patterns:**
   - `[0] * 5` - repeated elements
   - `list1 + list2` - concatenation

**Quick Reference:**

```python
# Empty
empty = []
empty = list()

# With values
numbers = [1, 2, 3, 4, 5]
mixed = ['text', 42, True, 3.14]

# From range
nums = list(range(1, 11))  # 1-10

# From string
chars = list("hello")
words = "a b c".split()

# Nested
matrix = [[1, 2], [3, 4]]

# Repeated
zeros = [0] * 10

# Combined
result = [1, 2] + [3, 4]
```

**Remember:**
- Lists are mutable (can be changed)
- Lists are ordered (maintain sequence)
- Lists allow duplicates
- Lists can contain any type
- Use `len()` for size
- Use `[]` for creation (most common)

**Next Steps:**
- Learn list indexing (accessing elements)
- Master list slicing (extracting portions)
- Explore list methods (append, insert, remove)
- Practice with real data

Lists are the foundation of Python data structures - master them!


---

## Accessing List Elements Using Indexing

### Hook (2 minutes)

**Scenario:**
You have a list of 100 student names. You need to:
- Get the first student's name for an award
- Check the last student on the list
- Find the 50th student
- Access the 3rd student from the end

Without indexing, you'd have no way to access specific elements in your list!

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# How do I get 'Charlie'?
# How do I get the last name?
# How do I get from the end?
```

**Indexing** is your tool to access individual elements by their position.

**What You'll Learn:**
1. Access elements using positive indices
2. Use negative indices to count from the end
3. Handle index errors gracefully
4. Access elements in nested lists
5. Check element existence
6. Find element positions

---

### CS Theory Bite

> **Origin**: **Zero-based indexing** comes from **C** (1972) — the index represents memory offset from the start. Negative indexing (`-1` for last) is Python's elegant addition.
>
> **Analogy**: Indexing is like **apartment numbers** — each element has a unique address. Negative indices count from the back entrance.
>
> **Why it matters**: O(1) random access by index is what makes lists powerful — instant access to any element.



### Section 1: Positive Indexing (4 minutes)

**Basic Indexing (Zero-Based):**

```python
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

# Index:    0        1         2        3       4
# Access first element
first = fruits[0]
print(first)  # apple

# Access second element
second = fruits[1]
print(second)  # banana

# Access third element
third = fruits[2]
print(third)  # orange

# Access last element (must know length)
last = fruits[4]
print(last)  # mango
```

**Key Points:**
- Indices start at 0, not 1
- First element: index 0
- Last element: index (length - 1)
- `fruits[0]` means "get item at position 0"

**Using with len():**

```python
fruits = ['apple', 'banana', 'orange']

# Get last element using length
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(f"Last fruit: {last_fruit}")  # orange

# Length is 3, so indices are 0, 1, 2
print(f"Length: {len(fruits)}")  # 3
print(f"Valid indices: 0 to {len(fruits)-1}")  # 0 to 2
```

**Visual Example:**

List: ['A', 'B', 'C', 'D', 'E']
Index:  0    1    2    3    4

fruits[0] → 'A'
fruits[2] → 'C'
fruits[4] → 'E'

---

### Section 2: Negative Indexing (3 minutes)

**Counting from the End:**

```python
numbers = [10, 20, 30, 40, 50]

# Negative indices count from the end
# Index:   -5  -4  -3  -2  -1
# Value:   10  20  30  40  50

# Last element
last = numbers[-1]
print(last)  # 50

# Second to last
second_last = numbers[-2]
print(second_last)  # 40

# Third from end
third_last = numbers[-3]
print(third_last)  # 30

# First element (from the end)
first = numbers[-5]
print(first)  # 10
```

**Why Use Negative Indexing:**

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without negative indexing (need to know length)
last = data[len(data) - 1]  # Verbose

# With negative indexing (clean and simple)
last = data[-1]  # Clean!

# Get last 3 elements
last_three = [data[-3], data[-2], data[-1]]
print(last_three)  # [8, 9, 10]
```

**Relationship Between Positive and Negative:**

```python
items = ['a', 'b', 'c', 'd', 'e']

# These are equivalent:
print(items[0])   # 'a'
print(items[-5])  # 'a'

print(items[4])   # 'e'
print(items[-1])  # 'e'

# Formula: negative_index = positive_index - len(list)
# items[2] = items[2 - 5] = items[-3]
```

---

### Section 3: Index Errors and Validation (3 minutes)

**IndexError - Out of Bounds:**

```python
colors = ['red', 'green', 'blue']

# Valid indices: 0, 1, 2 (or -3, -2, -1)

# This works
print(colors[0])  # red
print(colors[2])  # blue

# This fails - index too high
try:
    print(colors[3])
except IndexError as e:
    print(f"Error: {e}")
# Error: list index out of range

# This fails - index too low
try:
    print(colors[-4])
except IndexError as e:
    print(f"Error: {e}")
# Error: list index out of range
```

**Safe Access with Validation:**

```python
def safe_get(lst, index):
    """Safely get element with bounds checking"""
    if -len(lst) <= index < len(lst):
        return lst[index]
    else:
        return None  # Or raise custom error

scores = [85, 90, 78, 92]

print(safe_get(scores, 0))   # 85
print(safe_get(scores, 10))  # None (safe)
print(safe_get(scores, -1))  # 92
print(safe_get(scores, -10)) # None (safe)
```

**Using try-except:**

```python
def get_element(lst, index, default=None):
    """Get element or return default if out of bounds"""
    try:
        return lst[index]
    except IndexError:
        return default

numbers = [1, 2, 3]

print(get_element(numbers, 0))      # 1
print(get_element(numbers, 10))     # None
print(get_element(numbers, 10, -1)) # -1 (custom default)
```

---

### Section 4: Accessing Nested Lists (3 minutes)

**2D List Indexing:**

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access rows (first index)
row0 = matrix[0]  # [1, 2, 3]
row1 = matrix[1]  # [4, 5, 6]
row2 = matrix[2]  # [7, 8, 9]

# Access specific elements (row, column)
element = matrix[0][0]  # 1 (row 0, col 0)
element = matrix[0][2]  # 3 (row 0, col 2)
element = matrix[1][1]  # 5 (row 1, col 1)
element = matrix[2][2]  # 9 (row 2, col 2)

# Using negative indices
last_row = matrix[-1]      # [7, 8, 9]
last_element = matrix[-1][-1]  # 9
```

**Practical Example - Student Data:**

```python
students = [
    ['Alice', 85, 90, 88],   # [name, math, science, english]
    ['Bob', 78, 82, 86],
    ['Charlie', 92, 89, 94]
]

# Access Alice's data
alice = students[0]
print(f"Student: {alice}")
# ['Alice', 85, 90, 88]

# Access Alice's name
name = students[0][0]
print(f"Name: {name}")  # Alice

# Access Alice's math grade
math_grade = students[0][1]
print(f"Math grade: {math_grade}")  # 85

# Access Charlie's English grade
english_grade = students[2][3]
print(f"Charlie's English: {english_grade}")  # 94

# Last student's first subject
last_student_first_subject = students[-1][1]
print(last_student_first_subject)  # 92
```

---

### Section 5: Finding Elements (2 minutes)

**Check if Element Exists:**

```python
fruits = ['apple', 'banana', 'orange']

# Using 'in' operator
if 'banana' in fruits:
    print("Banana is in the list")
# Banana is in the list

if 'grape' in fruits:
    print("Grape is in the list")
else:
    print("Grape not found")
# Grape not found
```

**Find Index of Element:**

```python
numbers = [10, 20, 30, 40, 50]

# Find index of value
index = numbers.index(30)
print(f"30 is at index {index}")  # 30 is at index 2

# Access using found index
value = numbers[index]
print(f"Value at index {index}: {value}")  # 30

# Error if not found
try:
    index = numbers.index(100)
except ValueError as e:
    print(f"Error: {e}")
# Error: 100 is not in list
```

**Safe Find:**

```python
def find_index(lst, value):
    """Find index or return -1 if not found"""
    try:
        return lst.index(value)
    except ValueError:
        return -1

colors = ['red', 'green', 'blue']

print(find_index(colors, 'green'))  # 1
print(find_index(colors, 'yellow')) # -1
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Grade Lookup System**

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana']
grades = [85, 92, 78, 88]

# Look up specific student grade
student_index = 2
student_name = students[student_index]
student_grade = grades[student_index]

print(f"{student_name}'s grade: {student_grade}")
# Charlie's grade: 78

# Find student by name
name_to_find = 'Diana'
if name_to_find in students:
    index = students.index(name_to_find)
    grade = grades[index]
    print(f"{name_to_find}'s grade: {grade}")
# Diana's grade: 88
```

**Application 2: Shopping Cart**

```python
cart_items = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
cart_prices = [999.99, 29.99, 79.99, 299.99]

# Display cart with numbers
for i in range(len(cart_items)):
    item = cart_items[i]
    price = cart_prices[i]
    print(f"{i+1}. {item}: ${price}")

# Laptop: $999.99
# Mouse: $29.99
# Keyboard: $79.99
# Monitor: $299.99

# Remove item by position (user sees 1-based, code uses 0-based)
remove_position = 2  # User input
remove_index = remove_position - 1  # Convert to 0-based

removed_item = cart_items[remove_index]
print(f"Removing: {removed_item}")
# Removing: Mouse
```

**Application 3: First and Last Analysis**

```python
temperatures = [72, 75, 68, 71, 73, 76, 74]

# First and last day
first_day = temperatures[0]
last_day = temperatures[-1]

print(f"First day: {first_day}°F")
print(f"Last day: {last_day}°F")

# Temperature change
change = last_day - first_day
print(f"Change: {change:+d}°F")  # +2°F

# Highest and lowest
highest = max(temperatures)
lowest = min(temperatures)

highest_index = temperatures.index(highest)
lowest_index = temperatures.index(lowest)

print(f"Highest: {highest}°F on day {highest_index + 1}")
print(f"Lowest: {lowest}°F on day {lowest_index + 1}")
```

---

### Summary (1 minute)

**Key Concepts Covered:**

1. **Positive Indexing:**
   - Starts at 0
   - `list[0]` - first element
   - `list[len(list)-1]` - last element

2. **Negative Indexing:**
   - Counts from end
   - `list[-1]` - last element
   - `list[-2]` - second to last

3. **Index Validation:**
   - Check bounds before access
   - Use try-except for safety
   - Valid range: `-len(list)` to `len(list)-1`

4. **Nested Lists:**
   - `list[row][col]` - 2D access
   - Multiple levels possible

5. **Finding Elements:**
   - `value in list` - check existence
   - `list.index(value)` - find position

**Quick Reference:**

```python
items = ['a', 'b', 'c', 'd', 'e']

# Positive indices
items[0]   # 'a' (first)
items[2]   # 'c' (third)
items[4]   # 'e' (last)

# Negative indices
items[-1]  # 'e' (last)
items[-2]  # 'd' (second to last)

# Nested
matrix = [[1,2], [3,4]]
matrix[0][1]  # 2

# Find
'b' in items  # True
items.index('c')  # 2
```

**Remember:**
- Indices start at 0
- Use negative for end access
- Always validate bounds
- `index()` raises error if not found
- Nested lists use multiple `[]`

Indexing is fundamental to working with lists - practice accessing elements!


---

## Extracting List Portions Using Slicing


---

### CS Theory Bite

> **Origin**: Slicing syntax `[start:stop:step]` was inspired by **MATLAB** and **Fortran 90** array sections. Python creates a **new list** (copy), not a view.
>
> **Analogy**: Slicing is like **cutting a deck of cards** — pick any contiguous section, or take every Nth card with step.
>
> **Why it matters**: Slicing extracts subsequences in one expression — replacing verbose loop-based copying.



### Hook (2 minutes)

"Imagine you're working with a dataset containing sales data for the entire year - 365 days worth of numbers. Your manager asks you to analyze just the data for Q1, or maybe just the weekends, or perhaps every other day. Would you manually copy each individual value? Of course not! That's where slicing becomes your superpower.

Slicing is like having a smart knife that can cut exactly the portion you need from a list. Whether you want the first 10 items, the last 5, every third element, or even the entire list in reverse - slicing handles it all with a single, elegant syntax.

Today, we'll master list slicing - one of Python's most powerful and frequently used features. By the end, you'll be extracting, copying, and manipulating list portions with just a few keystrokes."

---

### Section 1: Slice Syntax Basics (3 minutes)

The slice syntax uses square brackets with colons to specify the portion you want:

```python
# Syntax: list[start:stop:step]
# start: index where slice begins (inclusive)
# stop: index where slice ends (exclusive)
# step: interval between elements (optional, default 1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
first_five = numbers[0:5]
print(first_five)  # [0, 1, 2, 3, 4]

# From index 3 to 7
middle = numbers[3:7]
print(middle)  # [3, 4, 5, 6]

# Notice: stop index is NOT included
# numbers[3:7] gets indices 3, 4, 5, 6 (not 7)
```

**Key Points:**
- Start is inclusive, stop is exclusive
- `[start:stop]` gets elements from start up to (but not including) stop
- Original list remains unchanged - slicing creates a new list

**Why Exclusive Stop?**
```python
# Exclusive stop makes splitting easier
data = [1, 2, 3, 4, 5, 6, 7, 8]

first_half = data[0:4]   # [1, 2, 3, 4]
second_half = data[4:8]  # [5, 6, 7, 8]

# No overlap, no gaps - perfect split
```

---

### Section 2: Omitting Start and Stop (3 minutes)

You can omit start or stop to slice from the beginning or to the end:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Omit start - begins from index 0
first_five = numbers[:5]
print(first_five)  # [0, 1, 2, 3, 4]

# Omit stop - goes to the end
from_five = numbers[5:]
print(from_five)  # [5, 6, 7, 8, 9]

# Omit both - copies entire list
copy = numbers[:]
print(copy)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Verify it's a copy
copy[0] = 999
print(numbers[0])  # Still 0 - original unchanged
```

**Common Patterns:**

```python
fruits = ['apple', 'banana', 'orange', 'mango', 'grape']

# First 3 items
print(fruits[:3])  # ['apple', 'banana', 'orange']

# Last 2 items
print(fruits[-2:])  # ['mango', 'grape']

# Everything except first
print(fruits[1:])  # ['banana', 'orange', 'mango', 'grape']

# Everything except last
print(fruits[:-1])  # ['apple', 'banana', 'orange', 'mango']
```

**Creating Shallow Copies:**
```python
# [:] is the standard way to copy a list
original = [1, 2, 3, 4, 5]
copy = original[:]

# Modify copy
copy.append(6)

print(original)  # [1, 2, 3, 4, 5] - unchanged
print(copy)      # [1, 2, 3, 4, 5, 6]
```

---

### Section 3: Using Negative Indices in Slices (3 minutes)

Negative indices count from the end, making it easy to work with list tails:

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 1   2   3   4   5   6   7   8   9
#      -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Last 3 elements
last_three = data[-3:]
print(last_three)  # [80, 90, 100]

# All except last 2
except_last_two = data[:-2]
print(except_last_two)  # [10, 20, 30, 40, 50, 60, 70, 80]

# From -7 to -3 (exclusive)
middle_portion = data[-7:-3]
print(middle_portion)  # [40, 50, 60, 70]

# Mix positive and negative
mixed = data[2:-2]
print(mixed)  # [30, 40, 50, 60, 70, 80]
```

**Practical Examples:**

```python
log_entries = ['entry1', 'entry2', 'entry3', 'entry4', 'entry5',
               'entry6', 'entry7', 'entry8', 'entry9', 'entry10']

# Get last 5 log entries
recent = log_entries[-5:]
print(recent)  # ['entry6', 'entry7', 'entry8', 'entry9', 'entry10']

# Remove first and last (trim)
trimmed = log_entries[1:-1]
print(trimmed)  # ['entry2', 'entry3', ..., 'entry9']

# Get everything except last 3
main_portion = log_entries[:-3]
print(main_portion)  # ['entry1', 'entry2', ..., 'entry7']
```

---

### Section 4: The Step Parameter (4 minutes)

The step parameter lets you skip elements at regular intervals:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every second element
evens = numbers[0:10:2]
print(evens)  # [0, 2, 4, 6, 8]

# Every second element starting from index 1
odds = numbers[1:10:2]
print(odds)  # [1, 3, 5, 7, 9]

# Every third element
every_third = numbers[::3]
print(every_third)  # [0, 3, 6, 9]

# From index 2, every 2nd element
from_two = numbers[2::2]
print(from_two)  # [2, 4, 6, 8]
```

**Step with Range:**

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Index 1 to 8, step 2
result = data[1:8:2]
print(result)  # [20, 40, 60, 80]

# First 6 elements, every 2nd
first_six_alternate = data[:6:2]
print(first_six_alternate)  # [10, 30, 50]
```

**Negative Step - Reversing:**

```python
numbers = [1, 2, 3, 4, 5]

# Reverse the entire list
reversed_list = numbers[::-1]
print(reversed_list)  # [5, 4, 3, 2, 1]

# Last 3 in reverse
last_three_rev = numbers[-3:][::-1]
# Or directly: numbers[:-4:-1]
print(last_three_rev)  # [5, 4, 3]

# Every second element in reverse
every_second_rev = numbers[::-2]
print(every_second_rev)  # [5, 3, 1]
```

**Practical Applications:**

```python
# Palindrome check
word = list("racecar")
is_palindrome = word == word[::-1]
print(is_palindrome)  # True

# Process every nth item
transactions = list(range(1, 101))  # 1 to 100

# Process every 10th transaction for audit
audit_sample = transactions[::10]
print(audit_sample)  # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

# Get alternating values
readings = [100, 98, 102, 99, 101, 97, 103, 98]
odd_position_readings = readings[::2]
even_position_readings = readings[1::2]
print(odd_position_readings)   # [100, 102, 101, 103]
print(even_position_readings)  # [98, 99, 97, 98]
```

---

### Section 5: Slice Assignment (3 minutes)

Slices can be used on the left side of assignment to modify list portions:

```python
# Replace a slice
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers[2:5] = [30, 40, 50]
print(numbers)  # [1, 2, 30, 40, 50, 6, 7, 8]

# Replace with different length
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30, 40, 50]
print(numbers)  # [1, 20, 30, 40, 50, 4, 5]

# Delete elements using slice assignment
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[2:5] = []
print(numbers)  # [1, 2, 6, 7]

# Insert elements
numbers = [1, 2, 5, 6]
numbers[2:2] = [3, 4]  # Insert at index 2
print(numbers)  # [1, 2, 3, 4, 5, 6]
```

**Replacing with Step:**

```python
# Replace every second element
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] = [10, 20, 30, 40, 50]
print(numbers)  # [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]

# Must match number of elements when using step
# numbers[::2] = [1, 2]  # Error: attempting to replace 5 items with 2
```

**Practical Uses:**

```python
# Replace middle section
grades = [65, 70, 45, 50, 55, 85, 90]
# Teacher adjusts middle grades after curve
grades[2:5] = [60, 65, 70]
print(grades)  # [65, 70, 60, 65, 70, 85, 90]

# Clear portion of list
tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
tasks[1:4] = []  # Remove tasks 2-4
print(tasks)  # ['task1', 'task5']

# Insert multiple items at once
menu = ['Appetizer', 'Main Course', 'Dessert']
menu[2:2] = ['Salad', 'Soup']  # Insert before dessert
print(menu)  # ['Appetizer', 'Main Course', 'Salad', 'Soup', 'Dessert']
```

---

### Section 6: Common Slicing Patterns (2 minutes)

**Split List:**
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mid = len(data) // 2
first_half = data[:mid]
second_half = data[mid:]

print(first_half)   # [1, 2, 3, 4, 5]
print(second_half)  # [6, 7, 8, 9, 10]
```

**Remove Duplicates at Boundaries:**
```python
# Remove first and last
items = ['start', 'a', 'b', 'c', 'end']
core = items[1:-1]
print(core)  # ['a', 'b', 'c']
```

**Chunk Processing:**
```python
data = list(range(20))

# Process in chunks of 5
chunk_size = 5
for i in range(0, len(data), chunk_size):
    chunk = data[i:i+chunk_size]
    print(f"Chunk: {chunk}")
# Chunk: [0, 1, 2, 3, 4]
# Chunk: [5, 6, 7, 8, 9]
# Chunk: [10, 11, 12, 13, 14]
# Chunk: [15, 16, 17, 18, 19]
```

**Sliding Window:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
window_size = 3

for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i+window_size]
    print(f"Window at {i}: {window}")
# Window at 0: [1, 2, 3]
# Window at 1: [2, 3, 4]
# Window at 2: [3, 4, 5]
# ...
```

**Interleave Lists:**
```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

combined = [None] * (len(list1) + len(list2))
combined[::2] = list1
combined[1::2] = list2

print(combined)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### Section 7: Performance and Best Practices (1 minute)

**Memory Efficiency:**
```python
# Slicing creates a new list (shallow copy)
large_list = list(range(1000000))

# This creates a copy
portion = large_list[:1000]  # New list with 1000 elements

# For read-only access on large lists, consider itertools.islice
from itertools import islice

# No copy created - returns iterator
portion_iter = islice(large_list, 1000)
```

**Best Practices:**

1. **Use slicing for copying:**
```python
copy = original[:]  # Clear intent
```

2. **Prefer slicing over loops for extraction:**
```python
# Good
first_ten = data[:10]

# Less efficient
first_ten = []
for i in range(10):
    first_ten.append(data[i])
```

3. **Be cautious with negative step:**
```python
# Clear for reversal
reversed_list = items[::-1]

# Confusing
weird = items[10:2:-2]  # Hard to understand
```

---

### Summary (1 minute)

Today we mastered list slicing - Python's powerful syntax for extracting list portions:

**Key Concepts:**
- **Basic syntax:** `list[start:stop:step]`
- **Start is inclusive, stop is exclusive**
- **Omit start/stop:** `[:5]`, `[5:]`, `[:]`
- **Negative indices:** Count from end (`[-3:]`, `[:-2]`)
- **Step parameter:** Skip elements (`[::2]`), reverse (`[::-1]`)
- **Slice assignment:** Modify portions (`list[2:5] = [...]`)

**Common Patterns:**
- First n: `list[:n]`
- Last n: `list[-n:]`
- Copy: `list[:]`
- Reverse: `list[::-1]`
- Skip: `list[::step]`

**Remember:**
- Slicing always creates a new list
- Original list unchanged unless using slice assignment
- Use slicing for clean, readable code
- Perfect for splitting, sampling, and reversing

Slicing is fundamental to Python - master it, and you'll write more elegant, efficient code. Practice these patterns until they become second nature!


---

## Iterating Through Lists Using Loops


---

### CS Theory Bite

> **Origin**: List iteration uses Python's **iterator protocol** (`__iter__` + `__next__`). For loops call `iter()` on the list, then `next()` until `StopIteration` — the same protocol for ALL iterables.
>
> **Analogy**: Iterating a list is like **reading a book** — start at page 1, process each page, stop at the end. The bookmark (`iterator`) tracks your position.
>
> **Why it matters**: Iteration is the most common list operation — mastering it unlocks data processing.



### Hook (2 minutes)

"You have a list of 100 student names and need to print each one with a greeting. Or maybe you have a list of prices and need to calculate which ones are above $50. Or perhaps you need to process temperature readings from the last 30 days. What do all these tasks have in common? Iteration - the ability to process each element in a list.

Iteration is how you bring lists to life. A list sitting there is just data. But when you loop through it, applying logic to each element, you turn static data into dynamic processing. You can filter, transform, analyze, or take action on every item.

Today, we'll master list iteration in Python. You'll learn multiple ways to loop through lists - from basic for loops to advanced techniques with enumerate() and zip(). By the end, you'll be processing lists efficiently and elegantly, whether you're handling 10 items or 10,000."

---

### Section 1: Basic For Loop Iteration (3 minutes)

**Iterating Directly Over Elements:**

```python
# Simple iteration
fruits = ['apple', 'banana', 'orange', 'mango']

for fruit in fruits:
    print(fruit)
# apple
# banana
# orange
# mango

# Processing each element
prices = [10.99, 25.50, 5.75, 100.00]

for price in prices:
    print(f"${price:.2f}")
# $10.99
# $25.50
# $5.75
# $100.00

# Conditional processing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
# is even
# is even
# is even
# is even
# is even
```

**Accumulating Results:**

```python
# Sum all elements
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(total)  # 150

# Build new list
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]

# Count matching elements
grades = [85, 92, 78, 90, 88, 76, 95, 82]
passing = 0

for grade in grades:
    if grade >= 80:
        passing += 1

print(f"Passing students: {passing}")  # 6
```

**Finding Elements:**

```python
# Find first match
numbers = [12, 45, 23, 78, 34, 89, 56]
target = 78
found = False

for num in numbers:
    if num == target:
        found = True
        break

print(f"Found: {found}")  # True

# Find maximum
numbers = [12, 45, 23, 78, 34, 89, 56]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")  # 89
```

---

### Section 2: Using enumerate() (3 minutes)

**Getting Index and Value:**

```python
# Basic enumerate
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# apple
# banana
# orange

# Start counting from 1
fruits = ['apple', 'banana', 'orange']

for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruit}")
# apple
# banana
# orange
```

**Practical Applications:**

```python
# Modify specific indices
grades = [78, 85, 92, 88, 76]

for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = 80  # Curve to minimum 80
        print(f"Curved grade at position {i}: {grade} → {grades[i]}")

print(grades)  # [80, 85, 92, 88, 80]

# Find positions of matching elements
items = ['apple', 'banana', 'apple', 'orange', 'apple']
apple_positions = []

for index, item in enumerate(items):
    if item == 'apple':
        apple_positions.append(index)

print(apple_positions)  # [0, 2, 4]

# Create index-value mapping
words = ['hello', 'world', 'python']
word_map = {}

for i, word in enumerate(words):
    word_map[i] = word

print(word_map)  # {0: 'hello', 1: 'world', 2: 'python'}
```

**Parallel Processing:**

```python
# Process with both index and value
students = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78, 88]

for i, student in enumerate(students):
    print(f"{i+1}. {student}: {scores[i]}")
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: 88
```

---

### Section 3: While Loop Iteration (2 minutes)

**Index-Based Iteration:**

```python
# Basic while loop
fruits = ['apple', 'banana', 'orange', 'mango']
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
# apple
# banana
# orange
# mango

# Skip elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 2  # Skip every other element
# 
# 
# 
# 
```

**Conditional Termination:**

```python
# Stop when condition met
numbers = [10, 20, 30, 40, 50, 60, 70]
i = 0

while i < len(numbers) and numbers[i] < 50:
    print(numbers[i])
    i += 1
# 
# 
# 
# 

# Search with early exit
items = ['apple', 'banana', 'orange', 'mango']
target = 'orange'
i = 0

while i < len(items):
    if items[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
# Found orange at index 2
```

---

### Section 4: Iterating with zip() (3 minutes)

**Parallel Iteration:**

```python
# Combine two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# Three or more lists
first_names = ['Alice', 'Bob', 'Charlie']
last_names = ['Smith', 'Jones', 'Brown']
ages = [25, 30, 22]

for first, last, age in zip(first_names, last_names, ages):
    print(f"{first} {last}, age {age}")
# Alice Smith, age 25
# Bob Jones, age 30
# Charlie Brown, age 22
```

**Creating Pairs and Dictionaries:**

```python
# Create dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']

person = {}
for key, value in zip(keys, values):
    person[key] = value

print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Or use dict() constructor
person = dict(zip(keys, values))

# Create list of tuples
products = ['laptop', 'mouse', 'keyboard']
prices = [999, 29, 79]

cart = list(zip(products, prices))
print(cart)  # [('laptop', 999), ('mouse', 29), ('keyboard', 79)]
```

**Handling Different Lengths:**

```python
# zip stops at shortest list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana is skipped

# Use itertools.zip_longest for longest
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78]

for name, score in zip_longest(names, scores, fillvalue=0):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: 0
```

---

### Section 5: Modifying Lists While Iterating (3 minutes)

**Safe Modification Patterns:**

```python
# WRONG - Don't modify while iterating
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # BAD - can skip elements
# Result may be unpredictable

# RIGHT - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Create copy with [:]
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # [1, 3, 5]

# RIGHT - Use list comprehension instead
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

**Modifying Elements (Safe):**

```python
# Modify elements by index - SAFE
prices = [10.00, 20.00, 30.00, 40.00]

for i in range(len(prices)):
    prices[i] = prices[i] * 1.1  # 10% increase

print(prices)  # [11.0, 22.0, 33.0, 44.0]

# Using enumerate - SAFE
grades = [75, 82, 68, 91, 79]

for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = 80  # Curve to minimum

print(grades)  # [80, 82, 80, 91, 80]
```

**Building New Lists:**

```python
# Filter and transform - create new list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

for num in numbers:
    if num % 2 == 0:
        even_squares.append(num ** 2)

print(even_squares)  # [4, 16, 36, 64, 100]

# Or use list comprehension
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
```

---

### Section 6: Nested Lists and 2D Iteration (2 minutes)

**Iterating Through 2D Lists:**

```python
# Matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate rows
for row in matrix:
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Iterate all elements
for row in matrix:
    for element in matrix:
        print(element, end=' ')
    print()  # New line after each row
# 2 3
# 5 6
# 8 9

# With indices
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")
# matrix[0][0] = 1
# matrix[0][1] = 2
# ...
```

**Practical 2D Examples:**

```python
# Student grades by subject
grades = [
    [85, 90, 78],  # Alice
    [92, 88, 95],  # Bob
    [78, 82, 80]   # Charlie
]

students = ['Alice', 'Bob', 'Charlie']

# Calculate averages
for i, student_grades in enumerate(grades):
    avg = sum(student_grades) / len(student_grades)
    print(f"{students[i]}: {avg:.1f}")
# Alice: 84.3
# Bob: 91.7
# Charlie: 80.0
```

---

### Section 7: Loop Control (1 minute)

**break and continue:**

```python
# break - exit loop early
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num > 5:
        break
    print(num)
# 2 3 4 5

# continue - skip to next iteration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# 3 5 7 9

# else clause - executes if loop completes normally
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num > 10:
        print("Found large number")
        break
else:
    print("No large numbers found")
# No large numbers found
```

---

### Summary (1 minute)

Today we mastered list iteration in Python:

**Basic Iteration:**
- `for item in list:` - Direct iteration over elements
- `for i in range(len(list)):` - Index-based iteration
- `while i < len(list):` - While loop with index

**Advanced Techniques:**
- `enumerate(list)` - Get index and value together
- `enumerate(list, start=1)` - Custom starting index
- `zip(list1, list2)` - Iterate multiple lists in parallel

**Safe Modification:**
- Iterate over copy: `for item in list[:]:`
- Use indices: `for i in range(len(list)):`
- Build new list instead of modifying

**Control Flow:**
- `break` - Exit loop early
- `continue` - Skip to next iteration
- `for...else` - Execute if loop completes

**Remember:**
- Don't modify list while iterating directly over it
- Use enumerate() when you need indices
- Use zip() for parallel lists
- List comprehensions often cleaner than loops

Iteration is fundamental to working with lists. Master these patterns and you'll process data efficiently!


---

## Using List Comprehensions


---

### CS Theory Bite

> **Origin**: List comprehensions came from **Haskell** (1990) and **mathematical set notation**: `{x² | x ∈ ℕ, x < 10}` → `[x**2 for x in range(10)]`. Added in **Python 2.0** (PEP 202, 2000).
>
> **Analogy**: A comprehension is like an **assembly line blueprint** — describe the transformation once, and it produces the entire output automatically.
>
> **Why it matters**: Comprehensions are faster than loops (C-level optimization) and more readable for simple transformations.



### Hook (2 minutes)

"You need to create a list of squares from 1 to 100. With a traditional loop, you'd write 4 lines of code - initialize empty list, loop through range, calculate square, append to list. But what if I told you Python has a way to do this in just one elegant line?

List comprehensions are Python's superpower for creating lists. They're faster, more readable, and more Pythonic than traditional loops. Think of them as a recipe: 'Give me this expression, for each item, from this source, where this condition is true.' One line, crystal clear intent.

Master list comprehensions and you'll write code that's not just shorter, but actually easier to understand. Whether you're filtering data, transforming values, or building complex structures, comprehensions make your code shine. Today, we'll go from basics to advanced techniques that will transform how you work with lists."

---

### Section 1: Basic List Comprehension Syntax (3 minutes)

**From Loop to Comprehension:**

```python
# Traditional loop approach
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension - one line!
squares = [num ** 2 for num in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**Syntax Breakdown:**

```python
# Pattern: [expression for item in iterable]
#           ^^^^^^^^^^     ^^^^    ^^^^^^^^
#           what to       loop    where from
#           create        variable

# Simple examples
numbers = [x for x in range(5)]
print(numbers)  # [0, 1, 2, 3, 4]

doubles = [x * 2 for x in range(5)]
print(doubles)  # [0, 2, 4, 6, 8]

strings = [str(x) for x in range(5)]
print(strings)  # ['0', '1', '2', '3', '4']
```

**Working with Existing Lists:**

```python
# Transform each element
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Calculate from elements
prices = [10.99, 25.50, 5.75, 100.00]
with_tax = [price * 1.08 for price in prices]
print(with_tax)  # [11.8692, 27.54, 6.21, 108.0]

# String operations
names = ['alice', 'bob', 'charlie']
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

**Mathematical Operations:**

```python
# Squares
squares = [n ** 2 for n in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Cubes
cubes = [n ** 3 for n in range(1, 6)]
print(cubes)  # [1, 8, 27, 64, 125]

# Formula application
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

### Section 2: Comprehensions with Conditionals (3 minutes)

**Filtering with if:**

```python
# Pattern: [expression for item in iterable if condition]

# Get only even numbers
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Get only odd numbers
odds = [n for n in numbers if n % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

# Filter by value threshold
scores = [45, 78, 92, 67, 85, 54, 90]
passing = [score for score in scores if score >= 70]
print(passing)  # [78, 92, 85, 90]
```

**String Filtering:**

```python
# Filter by length
words = ['a', 'bat', 'cat', 'elephant', 'dog']
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['elephant']

# Filter by starting letter
fruits = ['apple', 'banana', 'apricot', 'orange', 'avocado']
a_fruits = [fruit for fruit in fruits if fruit.startswith('a')]
print(a_fruits)  # ['apple', 'apricot', 'avocado']

# Filter by content
emails = ['user@gmail.com', 'test@yahoo.com', 'admin@gmail.com']
gmail = [email for email in emails if 'gmail' in email]
print(gmail)  # ['user@gmail.com', 'admin@gmail.com']
```

**Transform AND Filter:**

```python
# Square only even numbers
numbers = range(1, 11)
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Uppercase only long words
words = ['hi', 'hello', 'hey', 'goodbye']
long_upper = [word.upper() for word in words if len(word) > 3]
print(long_upper)  # ['HELLO', 'GOODBYE']

# Price with discount for expensive items
prices = [15, 50, 120, 30, 200]
discounted = [price * 0.9 for price in prices if price > 100]
print(discounted)  # [108.0, 180.0]
```

---

### Section 3: if-else in Comprehensions (3 minutes)

**Conditional Expression (Ternary):**

```python
# Pattern: [true_expr if condition else false_expr for item in iterable]

# Categorize as even/odd
numbers = range(1, 6)
types = ['even' if n % 2 == 0 else 'odd' for n in numbers]
print(types)  # ['odd', 'even', 'odd', 'even', 'odd']

# Replace negatives with zero
values = [5, -2, 8, -7, 3]
positive_only = [x if x > 0 else 0 for x in values]
print(positive_only)  # [5, 0, 8, 0, 3]

# Cap values at maximum
scores = [85, 105, 92, 110, 78]
capped = [score if score <= 100 else 100 for score in scores]
print(capped)  # [85, 100, 92, 100, 78]
```

**Pass/Fail Grading:**

```python
grades = [85, 72, 90, 65, 78, 95]
results = ['Pass' if grade >= 70 else 'Fail' for grade in grades]
print(results)  # ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']

# With letter grades
letter_grades = [
    'A' if score >= 90 else 
    'B' if score >= 80 else 
    'C' if score >= 70 else 
    'D' if score >= 60 else 'F'
    for score in grades
]
print(letter_grades)  # ['B', 'C', 'A', 'D', 'C', 'A']
```

**Data Cleaning:**

```python
# Replace None with default
data = [10, None, 30, None, 50]
cleaned = [x if x is not None else 0 for x in data]
print(cleaned)  # [10, 0, 30, 0, 50]

# Sanitize strings
inputs = ['hello', '', 'world', '  ', 'python']
valid = [s if s.strip() else 'N/A' for s in inputs]
print(valid)  # ['hello', 'N/A', 'world', 'N/A', 'python']
```

---

### Section 4: Nested Comprehensions (3 minutes)

**2D Lists (Matrices):**

```python
# Create 3x3 matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]

# Identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identity)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

# Multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# ...
```

**Flattening Lists:**

```python
# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten to 1D
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With filtering
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(even_flat)  # [2, 4, 6, 8]
```

**Cartesian Product:**

```python
# All combinations
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = [(color, size) for color in colors for size in sizes]
print(products)
# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Coordinate grid
coords = [(x, y) for x in range(3) for y in range(3)]
print(coords)
# [(0, 0), (0, 1), (0, 2),
#  (1, 0), (1, 1), (1, 2),
#  (2, 0), (2, 1), (2, 2)]
```

---

### Section 5: Working with Multiple Lists (2 minutes)

**Using zip() in Comprehensions:**

```python
# Combine two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Create tuples
pairs = [(name, score) for name, score in zip(names, scores)]
print(pairs)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Calculate from multiple sources
prices = [100, 200, 300]
quantities = [2, 1, 3]
totals = [p * q for p, q in zip(prices, quantities)]
print(totals)  # [200, 200, 900]

# String formatting
students = ['Alice', 'Bob']
grades = [92, 85]
reports = [f"{name}: {grade}" for name, grade in zip(students, grades)]
print(reports)  # ['Alice: 92', 'Bob: 85']
```

**enumerate() in Comprehensions:**

```python
# Add index to values
fruits = ['apple', 'banana', 'orange']
indexed = [(i, fruit) for i, fruit in enumerate(fruits)]
print(indexed)  # [(0, 'apple'), (1, 'banana'), (2, 'orange')]

# Numbered list
numbered = [f"{i+1}. {fruit}" for i, fruit in enumerate(fruits)]
print(numbered)  # ['1. apple', '2. banana', '3. orange']
```

---

### Section 6: Practical Applications (3 minutes)

**Data Transformation:**

```python
# Parse CSV-like data
data = "10,20,30,40,50"
numbers = [int(x) for x in data.split(',')]
print(numbers)  # [10, 20, 30, 40, 50]

# Extract from dictionaries
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]
names = [user['name'] for user in users]
print(names)  # ['Alice', 'Bob', 'Charlie']

adults = [user for user in users if user['age'] >= 25]
print(adults)  # [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
```

**Text Processing:**

```python
# Extract words
sentence = "The quick brown fox jumps"
words = [word for word in sentence.split()]
print(words)  # ['The', 'quick', 'brown', 'fox', 'jumps']

# Filter and clean
text = "Hello123 World456 Python789"
letters_only = [''.join(c for c in word if c.isalpha()) for word in text.split()]
print(letters_only)  # ['Hello', 'World', 'Python']

# First letters
words = ['apple', 'banana', 'cherry']
initials = [word[0].upper() for word in words]
print(initials)  # ['A', 'B', 'C']
```

**Mathematical Sequences:**

```python
# Fibonacci-like with comprehension + recursion
fibs = [0, 1]
fibs.extend([fibs[i-1] + fibs[i-2] for i in range(2, 10)])
print(fibs)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Prime numbers (simple check)
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = [n for n in range(2, 50) if is_prime(n)]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### Section 7: Performance and Best Practices (1 minute)

**When to Use Comprehensions:**

```python
# GOOD - Simple transformation
squares = [x ** 2 for x in range(10)]

# GOOD - Simple filtering
evens = [x for x in range(10) if x % 2 == 0]

# AVOID - Too complex, use regular loop
# BAD - Hard to read
result = [
    x * y + z if x > y else y * z + x 
    for x in range(10) 
    for y in range(10) 
    for z in range(10)
    if x + y + z > 15
]

# BETTER - Use regular loop for complex logic
result = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            if x + y + z > 15:
                if x > y:
                    result.append(x * y + z)
                else:
                    result.append(y * z + x)
```

**Performance Tips:**

```python
# Comprehensions are faster than loops
import time

# Traditional loop
start = time.time()
squares = []
for i in range(1000000):
    squares.append(i ** 2)
loop_time = time.time() - start

# Comprehension
start = time.time()
squares = [i ** 2 for i in range(1000000)]
comp_time = time.time() - start

print(f"Loop: {loop_time:.4f}s")
print(f"Comprehension: {comp_time:.4f}s")
# Comprehension is typically 20-30% faster
```

---

### Summary (1 minute)

List comprehensions are a powerful Python feature for creating lists:

**Basic Syntax:**
- `[expression for item in iterable]`
- `[expr for item in iterable if condition]`
- `[expr if cond else other for item in iterable]`

**Key Benefits:**
- More concise than loops
- Faster performance
- More readable (when simple)
- Pythonic style

**Common Patterns:**
- Transform: `[x * 2 for x in numbers]`
- Filter: `[x for x in numbers if x > 0]`
- Both: `[x * 2 for x in numbers if x > 0]`
- Nested: `[x for row in matrix for x in row]`

**Best Practices:**
- Use for simple to moderate transformations
- Keep them readable (< 2 lines)
- Use regular loops for complex logic
- Combine with zip(), enumerate(), range()

**Remember:**
- Comprehensions create new lists
- Original data unchanged
- Can nest but keep it simple
- Performance boost over loops

Master comprehensions and your Python code becomes elegant and efficient!


---

### Defining Reusable Functions in Python


### CS Theory Bite

> **Origin**: Functions (called **subroutines** in the 1950s) were formalized to enable **code reuse**. The **DRY principle** (Don't Repeat Yourself) — Andy Hunt & Dave Thomas, 1999 — is built on functions.
>
> **Analogy**: A function is like a **recipe** — define it once, cook it anytime you want. Change the recipe, and every dish improves.
>
> **Why it matters**: Functions are the primary unit of code organization — every large program is built from small functions.


### Hook (3 minutes)

"Imagine you're making breakfast. Every morning, you follow the same routine to make coffee - you don't relearn the steps each time. Functions in Python work the same way: define once, use many times!"

Think about your calculator's 'add' button - programmers wrote ONE function and reused it thousands of times!

### Section 1: What is a Function? (4 minutes)

A function is a named block of reusable code that performs a specific task.

**Without functions - repetitive code:**
```python
# Print header - First time
print("=" * 40)
print("   Welcome to My Program")
print("=" * 40)

# Later, print header again (copy-paste!)
print("=" * 40)
print("   Welcome to My Program")
print("=" * 40)
```

This is repetitive! If we change the header, we update it everywhere. Functions solve this.

### Section 2: Function Syntax (5 minutes)

```python
def function_name():
    # Function body (indented)
    # Code to execute
    pass
```

**Components:**
- `def` - keyword to start function definition
- `function_name` - descriptive name (PEP 8 conventions)
- `()` - parentheses (for parameters later)
- `:` - colon to start the block
- Indented code - function body

**Example:**
```python
def greet():
    print("Hello, World!")
    print("Welcome to Python!")
```

Note: Defining doesn't run it! We must CALL it.

### Section 3: Calling Functions (4 minutes)

```python
# STEP 1: Define
def greet():
    print("Hello, World!")
    print("Welcome to Python!")

# STEP 2: Call
greet()  # Output: Hello, World!
         #         Welcome to Python!

# Call multiple times
greet()
greet()  # Each call executes the entire function!
```

**Practical example:**
```python
def print_header():
    print("=" * 40)
    print("   Welcome to My Program")
    print("=" * 40)

print_header()  # Use anywhere
print("Loading...")
print_header()  # Use again
```

### Section 4: Functions Can Contain Any Code (4 minutes)

**Conditionals:**
```python
def check_age():
    age = 20
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

check_age()
```

**Loops:**
```python
def print_countdown():
    for i in range(5, 0, -1):
        print(i)
    print("Blast off!")

print_countdown()
```

**Multiple operations:**
```python
def daily_report():
    print("Generating report...")
    total = 100 + 200 + 300
    print(f"Total: {total}")
```

### Section 5: Why Use Functions? (3 minutes)

**Benefits:**
1. Reusability - Write once, use many times
2. Organization - Break large programs into manageable pieces
3. Maintainability - Update code in one place
4. Readability - Descriptive names make code self-documenting

**Example:**
```python
def show_menu():
    print("=" * 30)
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

show_menu()  # On startup
# ... code ...
show_menu()  # After game over
# To change menu, update function once!
```

### Section 6: Common Mistakes (3 minutes)

**Mistake 1: Forgetting to call**
```python
def greet():
    print("Hello!")
# Nothing happens - not called!
```

**Mistake 2: Indentation errors**
```python
def greet():
print("Hello!")  # IndentationError!
```

**Mistake 3: Calling before defining**
```python
greet()  # NameError!

def greet():
    print("Hello!")
```

### Section 7: Practice (2 minutes)

Write a function `print_stars` that prints 5 stars:
```python
def print_stars():
    print("*" * 5)

print_stars()  # *****
```

### Wrap-Up (2 minutes)

**Key points:**
- Functions are reusable blocks of code
- Define with `def` keyword
- Call using function name with parentheses
- Make code organized and maintainable

**Template:**
```python
def function_name():
    # Your code here
    pass

function_name()  # Call it
```


---

### Using Function Parameters to Accept Inputs


### CS Theory Bite

> **Origin**: Parameters implement **parameterized abstraction** — functions that adapt to different inputs. Python uses **pass-by-object-reference** (neither pure pass-by-value nor pass-by-reference).
>
> **Analogy**: Parameters are like **power outlets** — the function is an appliance, and parameters are the sockets where you plug in different data.
>
> **Why it matters**: Parameters make functions flexible — one function, many uses with different inputs.


### Hook (3 minutes)

"Yesterday we learned functions, but they always did the SAME thing. Imagine if your calculator's 'add' button could only add 2+3 every time - not very useful!"

Today: Make functions flexible by passing data to them!

Think of a vending machine - ONE machine accepts INPUT (your selection) and gives different OUTPUT. Functions work the same way!

### Section 1: The Problem Without Parameters (4 minutes)

**Inflexible function:**
```python
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Hello, Alice!
greet_alice()  # Hello, Alice! (same every time)
```

To greet different people, we'd need many functions - impractical! **Solution: Parameters!**

### Section 2: What Are Parameters? (5 minutes)

A parameter is a variable in the function definition that acts as a placeholder for data.

**Syntax:**
```python
def function_name(parameter):
    # Use parameter here
    print(parameter)
```

**Example:**
```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
greet("Charlie")  # Hello, Charlie!
```

**Key points:**
- Parameter is a variable name
- Gets its value when function is called
- Can be used anywhere in function body

### Section 3: Parameters vs Arguments (3 minutes)

```python
def greet(name):  # 'name' is a PARAMETER
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an ARGUMENT
```

**Remember:**
- Parameter = placeholder in definition
- Argument = actual value when calling

**Example:**
```python
def square(number):  # parameter
    print(number ** 2)

square(5)   # 5 is argument -> 25
square(10)  # 10 is argument -> 100
```

### Section 4: Multiple Parameters (5 minutes)

**Syntax:**
```python
def function_name(param1, param2, param3):
    pass
```

**Examples:**
```python
def greet_full(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full("Alice", "Smith")  # Hello, Alice Smith!

def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)   # 5 + 3 = 8
```

**Order matters!**
```python
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old")

introduce("Alice", 25)  # Correct
introduce(25, "Alice")  # Wrong! "My name is 25..."
```

### Section 5: Different Data Types (4 minutes)

**Strings:**
```python
def shout(message):
    print(message.upper() + "!")

shout("hello")  # HELLO!
```

**Numbers:**
```python
def print_times(text, count):
    for i in range(count):
        print(text)

print_times("Python", 3)
```

**Mixed types:**
```python
def make_sentence(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

make_sentence("Alice", 25, "New York")
```

### Section 6: Common Mistakes (3 minutes)

**Wrong number of arguments:**
```python
def add(a, b):
    print(a + b)

add(5)        # Error: missing argument
add(5, 3, 2)  # Error: too many arguments
add(5, 3)     # Correct
```

**Wrong order:**
```python
def subtract(a, b):
    print(a - b)

subtract(10, 3)  # 7
subtract(3, 10)  # -7 (different!)
```

### Section 7: Real-World Application (3 minutes)

**Validation:**
```python
def validate_username(username):
    if len(username) < 3:
        print("Username too short!")
    elif len(username) > 20:
        print("Username too long!")
    else:
        print("Username valid!")

validate_username("ab")        # Too short!
validate_username("alice123")  # Valid!
```

### Section 8: Practice (2 minutes)

Write `calculate_bmi` that takes weight and height:
```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

calculate_bmi(70, 1.75)  # BMI: 22.86
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. Parameters = placeholders in definition
2. Arguments = actual values when calling
3. Multiple parameters = separate with commas
4. Order matters
5. Any data type can be a parameter

**Template:**
```python
def function_name(param1, param2):
    # Use parameters
    pass

function_name(value1, value2)
```


---

### Returning Values from Functions Using Return


### CS Theory Bite

> **Origin**: Return values connect to **functional programming** (lambda calculus, 1930s) — functions as mathematical mappings: input → output. **Pure functions** (same input → same output) are the gold standard.
>
> **Analogy**: `return` is like a **vending machine** — you insert input (money + selection), and the machine gives back a specific output (snack).
>
> **Why it matters**: Functions without return values are limited to side effects — return values enable composition and data flow.


### Hook (3 minutes)

"Our functions print results, but imagine if your calculator showed the answer but didn't let you USE it in another calculation. Frustrating, right?"

Today: Learn how to make functions send data BACK using return statements!

Think of a vending machine - it doesn't just SHOW you the snack, it GIVES it to you. The `return` statement works the same way!

### Section 1: The Problem - Functions That Only Print (4 minutes)

**Current limitation:**
```python
def add(a, b):
    result = a + b
    print(result)  # Just prints

add(5, 3)  # Prints: 8

# But we can't use the result!
total = add(5, 3)  # Prints: 8
print(total)       # Prints: None
```

**What we need:**
```python
def add(a, b):
    return a + b  # Give back the result

total = add(5, 3)   # total = 8
print(total)        # Prints: 8
doubled = total * 2 # We can use it!
```

### Section 2: What is Return? (5 minutes)

The `return` statement sends a value back to the caller and immediately exits the function.

**Syntax:**
```python
def function_name():
    return value  # Send value back
```

**Example:**
```python
def get_greeting():
    return "Hello, World!"

message = get_greeting()
print(message)  # Hello, World!
```

**Key points:**
- `return` gives a value back
- Function stops when it hits `return`
- Store returned value in a variable
- Use returned value in expressions

### Section 3: Return vs Print (4 minutes)

**Print version:**
```python
def add_print(a, b):
    print(a + b)  # Shows on screen

x = add_print(3, 4)  # Prints: 7
print(x)             # Prints: None
```

**Return version:**
```python
def add_return(a, b):
    return a + b  # Gives value back

x = add_return(3, 4)  # x = 7
print(x)              # Prints: 7
```

**Key difference:**
- `print()` displays to screen (for humans)
- `return` gives data back (for programs)

### Section 4: Using Returned Values (5 minutes)

**In calculations:**
```python
def square(n):
    return n * n

result = square(5)                # 25
total = square(3) + square(4)     # 9 + 16 = 25
```

**In conditionals:**
```python
def is_adult(age):
    return age >= 18

if is_adult(20):
    print("Can vote!")
```

### Section 5: Returning Different Data Types (4 minutes)

**Strings, numbers, booleans:**
```python
def make_greeting(name):
    return f"Hello, {name}!"

def is_even(num):
    return num % 2 == 0
```

**Multiple values:**
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9])
```

### Section 6: Return Stops Execution (3 minutes)

```python
def check_number(num):
    if num > 10:
        return "Too big!"
    if num < 0:
        return "Negative!"
    return "Perfect!"

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

### Section 7: Common Mistakes (3 minutes)

```python
# Forgetting to return
def add(a, b):
    result = a + b  # Forgot return!

# Not capturing
square(5)  # Value lost!
result = square(5)  # Correct

# Code after return
def greet():
    return "Hello"
    print("World")  # Never executes!
```

### Section 8: Real-World Application (3 minutes)

```python
def is_valid_password(password):
    if len(password) < 8:
        return False
    return True

def calculate_total(price, quantity, tax_rate):
    return price * quantity * (1 + tax_rate)

order_total = calculate_total(10.99, 3, 0.08)
```

### Section 9: Practice (2 minutes)

Write `calculate_discount` that returns final price:
```python
def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

final = calculate_discount(100, 20)
print(f"Final: ${final}")  # $80.00
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. `return` sends value back to caller
2. Return stops execution immediately
3. Returned values can be stored and used
4. Print shows output; return gives usable data
5. No return means function returns `None`

**Template:**
```python
def function_name(params):
    result = some_value
    return result

value = function_name(args)
```


---

### Applying Default Parameters in Function Definitions


### CS Theory Bite

> **Origin**: Default parameters are Python's alternative to **function overloading** (C++/Java). They enable **progressive disclosure** — simple calls for common cases, detailed calls for edge cases.
>
> **Analogy**: Default parameters are like **restaurant menu defaults** — "How do you want your steak?" "Medium" is the default, but you can specify rare or well-done.
>
> **Why it matters**: Defaults simplify function calls — users only specify what differs from the common case.


### Hook (3 minutes)

"Ever use a copy machine? The settings are pre-configured: single-sided, one copy, black and white. But you CAN change them! This is how default parameters work - sensible defaults with customization when needed."

Think about ordering coffee - default is medium with no sugar, but you can say "large with 2 sugars" to override!

### Section 1: The Problem - Too Many Required Arguments (4 minutes)

**Inflexible:**
```python
def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice", "Hello", "!")
greet("Bob", "Hello", "!")    # Repeating "Hello" and "!"
greet("Charlie", "Hello", "!")
```

**Solution - default parameters:**
```python
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")              # Hello, Alice!
greet("Bob")                # Hello, Bob!
greet("Charlie", "Hi")      # Hi, Charlie!
greet("David", "Hey", "?")  # Hey, David?
```

### Section 2: What Are Default Parameters? (5 minutes)

A default parameter has a pre-assigned value in the function definition. If no argument is provided, the default is used.

**Syntax:**
```python
def function_name(param1, param2=default_value):
    pass
```

**Example:**
```python
def power(base, exponent=2):  # exponent defaults to 2
    return base ** exponent

print(power(5))      # 5^2 = 25
print(power(5, 3))   # 5^3 = 125
print(power(2, 4))   # 2^4 = 16
```

**Key points:**
- Default parameters make arguments optional
- If not provided, default value is used
- Can override by passing a value
- Defaults must come after regular parameters

### Section 3: Syntax Rules (4 minutes)

**Rule 1: Defaults after required parameters**
```python
# WRONG
def greet(greeting="Hello", name):  # SyntaxError!
    pass

# CORRECT
def greet(name, greeting="Hello"):
    pass
```

**Rule 2: Multiple defaults**
```python
def make_coffee(size="medium", sugar=0, milk=False):
    print(f"{size} coffee, {sugar} sugar, milk: {milk}")

make_coffee()               # All defaults
make_coffee("large")        # Override size
make_coffee("small", 2)     # Override size and sugar
```

**Rule 3: Mixing required and default**
```python
def order_pizza(size, topping="cheese", extra=False):
    print(f"{size} pizza with {topping}")

order_pizza("large")              # Must provide size
order_pizza("medium", "pepperoni")
```

### Section 4: Using Default Parameters (5 minutes)

**Configuration:**
```python
def connect_to_server(host, port=8080, timeout=30):
    print(f"Connecting to {host}:{port}, timeout: {timeout}s")

connect_to_server("localhost")
connect_to_server("example.com", 443)
```

**Formatting:**
```python
def format_price(amount, currency="USD", decimals=2):
    return f"{currency} {amount:.{decimals}f}"

print(format_price(19.99))        # USD 19.99
print(format_price(19.99, "EUR")) # EUR 19.99
```

### Section 5: Keyword Arguments with Defaults (4 minutes)

```python
def create_user(username, role="user", active=True, notifications=True):
    print(f"User: {username}, Role: {role}")
    print(f"Active: {active}, Notifications: {notifications}")

create_user("alice", notifications=False)  # Skip some defaults
create_user("bob", active=False)
```

### Section 6: Common Use Cases (3 minutes)

```python
def print_header(text, width=50, char="="):
    print(char * width)
    print(text.center(width))
    print(char * width)

print_header("Welcome")        # Defaults
print_header("Hello", 30, "*") # Custom

def calculate_shipping(weight, distance, express=False):
    cost = weight * 0.5 + distance * 0.1
    return cost * 2 if express else cost
```

### Section 7: Common Mistakes (3 minutes)

**Mistake 1: Mutable defaults**
```python
# DANGEROUS
def add_item(item, items=[]):  # BAD!
    items.append(item)
    return items

# CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**Mistake 2: Wrong order**
```python
# WRONG
def greet(greeting="Hello", name):  # SyntaxError!
    pass

# CORRECT
def greet(name, greeting="Hello"):
    pass
```

### Section 8: Practice (2 minutes)

Write `send_email` with recipient (required), subject (default "No Subject"), urgent (default False):
```python
def send_email(recipient, subject="No Subject", urgent=False):
    priority = "HIGH" if urgent else "NORMAL"
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")

send_email("alice@example.com")
send_email("bob@example.com", "Meeting", True)
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. Default parameters provide fallback values
2. Make arguments optional and functions flexible
3. Required parameters before defaults
4. Override by position or keyword
5. Avoid mutable defaults (use None)

**Template:**
```python
def function_name(required, optional=default):
    pass

function_name(value1)         # Uses default
function_name(value1, value2) # Overrides
```

Congratulations! You now know Python function fundamentals!


---

