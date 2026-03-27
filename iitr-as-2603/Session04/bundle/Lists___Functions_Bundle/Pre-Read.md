## Creating and Initializing Lists in Python

## What Are Lists?

Lists are Python's **super-powered containers** for storing multiple items in order. Think of them as magical boxes that can hold anything and grow/shrink as needed!

### Simple Analogy

Think of lists like **a train**:
- **Multiple cars**: Each car (item) holds something different
- **Order matters**: Car #1, Car #2, Car #3... (positions/indices)
- **Add/remove cars**: Attach new cars, detach old ones (mutable!)
- **Mixed cargo**: One car has passengers, another has freight

Or like **a shopping list**:
- **Ordered items**: Milk, eggs, bread (sequential)
- **Easy to scan**: Check item by item
- **Update anytime**: Cross off bought items, add forgotten ones
- **One paper**, many items!

### Why Lists Changed Everything

Before lists/arrays, programmers needed separate variables for everything:
```python
# The nightmare scenario
score1 = 85
score2 = 92
score3 = 78
# ...imagine 1000 students! Impossible!
```

With lists - elegant and scalable:
```python
scores = [85, 92, 78, ...] # Can hold millions!
average = sum(scores) / len(scores)  # Easy!
```

### What You'll Learn

Lists are Python's most versatile data structure for storing ordered collections. You'll learn to create and initialize lists in various ways.

### Why It Matters

Lists are everywhere in programming:
- Shopping carts in e-commerce
- Student grades in education apps
- Todo items in task managers
- Data points in analytics
- User inputs in forms

Without lists, you'd need separate variables for each item - impossible at scale.

### Key Concepts

**List Basics:**
- Ordered collection of items
- Created with square brackets `[]`
- Items separated by commas
- Can hold any data type

**Simple Example:**
```python
# Create list
fruits = ['apple', 'banana', 'orange']

# Access items
print(fruits[0])  # apple
print(fruits[1])  # banana

# Get length
print(len(fruits))  # 3
```

### What to Expect

You'll learn:
1. Create empty lists
2. Initialize with values
3. Convert strings/ranges to lists
4. Build nested lists
5. Use special patterns (repetition, concatenation)

### Quick Examples

**Empty List:**
```python
cart = []
tasks = list()
```

**With Values:**
```python
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
mixed = ['text', 42, True, 3.14]
```

**From Range:**
```python
nums = list(range(10))  # [0, 1, 2, ..., 9]
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
```

**From String:**
```python
letters = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
words = "hello world".split()  # ['hello', 'world']
```

**Nested:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[0][1])  # 2
```

### Try to Predict

```python
# What will these create?
a = []
b = [1, 2, 3]
c = list(range(5))
d = list("hi")
e = "a,b,c".split(',')
```

Answers:
- a: `[]` (empty)
- b: `[1, 2, 3]`
- c: `[0, 1, 2, 3, 4]`
- d: `['h', 'i']`
- e: `['a', 'b', 'c']`

Lists are fundamental to Python - master creation first!


---

## Accessing List Elements Using Indexing

## What is Indexing?

Indexing is your **direct access pass** to any item in a list - like having a remote control to jump straight to any TV channel without scrolling through all of them!

### Simple Analogy

Think of indexing like **a parking garage**:
- **Spaces numbered**: 0, 1, 2, 3... (indices)
- **Find your car**: Go straight to space #42
- **No wandering**: Don't check spaces 0-41 first!
- **Instant access**: Same speed whether space #1 or #1000

Or like **chapters in a book**:
- **Want chapter 5?** Flip directly to it (use the index)
- **Don't read 1-4 first**: Skip straight there
- **Page numbers**: Like list indices

### Why Zero-Based?

Python starts counting at 0, not 1. **Why?**
- First item is **0 steps** from the start
- Think: "Distance from beginning" not "position number"
- Most programming languages do this (C, Java, JavaScript...)

```python
fruits = ['apple', 'banana', 'orange']
# 1         2
# apple is 0 steps from start!
```

### What You'll Learn

Indexing lets you access individual elements in a list by their position. Essential for working with list data.

### Why It Matters

Without indexing:
- Can't get specific elements
- Can't modify particular items
- Can't process data selectively

With indexing:
- Access any element instantly
- Modify specific positions
- Build complex algorithms

### Key Concepts

**Indexing Basics:**
- Use square brackets: `list[index]`
- Indices start at 0
- Access by position

**Example:**
```python
fruits = ['apple', 'banana', 'orange']

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange
```

### Positive vs Negative

**Positive (from start):**
```python
items = ['a', 'b', 'c', 'd']
items[0]   # 'a' (first)
items[3]   # 'd' (last)
```

**Negative (from end):**
```python
items[-1]  # 'd' (last)
items[-2]  # 'c' (second to last)
```

### Common Patterns

**First and Last:**
```python
data = [10, 20, 30, 40, 50]

first = data[0]      # 10
last = data[-1]      # 50
```

**Nested Lists:**
```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])  # 2
```

**Finding:**
```python
names = ['Alice', 'Bob', 'Charlie']

# Check if exists
if 'Bob' in names:
    idx = names.index('Bob')
    print(f"Found at {idx}")  # 1
```

### Try to Predict

```python
lst = ['x', 'y', 'z']

a = lst[0]    # ?
b = lst[-1]   # ?
c = lst[1]    # ?
d = lst[-2]   # ?
```

Answers:
- a: 'x'
- b: 'z'
- c: 'y'
- d: 'y'

Indexing is the foundation - master it first!


---

## Extracting List Portions Using Slicing

## What is Slicing?

Slicing is Python's **superpower notation** for grabbing chunks of lists - like using a pizza cutter to get exactly the slices you want!

### Simple Analogy

Think of slicing like **a bakery display case**:
- **Muffins in a row**: Your list [muffin1, muffin2, muffin3...]
- **Customer says**: "I'll take muffins 2 through 5"
- **Baker grabs them**: Picks that range, puts in a box
- **Original stays**: Display case still full!

Or like **DVR recording**:
- **Full show**: 60 minutes (your list)
- **You want**: Minutes 10-20 (a slice)
- **Extract**: Save just that segment
- **Simple command**: show[10:20]

### The Magic Syntax

```python
list[start:stop:step]
```

- **start**: "Begin here" (included)
- **stop**: "Stop here" (NOT included - important!)
- **step**: "Take every Nth item"

**Why stop is exclusive?** Makes ranges work perfectly with loops! `range(5)` gives 0-4, `list[:5]` gives first 5 items. Beautiful!

### What You'll Learn

Slicing lets you extract portions of a list using a concise syntax. Essential for data manipulation and analysis.

### Why It Matters

Without slicing:
- Must loop to extract portions
- Code becomes verbose
- Harder to read and maintain

With slicing:
- One-line extraction
- Clean, readable code
- Built-in list operations

### The Slice Syntax

**Basic Format:**
```python
list[start:stop:step]
```

- `start`: Where to begin (inclusive)
- `stop`: Where to end (exclusive)
- `step`: Interval between elements

**Example:**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements 2 through 6
portion = numbers[2:7]
print(portion)  # [2, 3, 4, 5, 6]

# Notice: stop at 7 means up to (not including) 7
```

### Common Patterns

**First/Last n Elements:**
```python
data = [10, 20, 30, 40, 50, 60]

# First 3
first = data[:3]     # [10, 20, 30]

# Last 2
last = data[-2:]     # [50, 60]
```

**Copy a List:**
```python
original = [1, 2, 3, 4, 5]
copy = original[:]

# Modify copy without affecting original
copy.append(6)
```

**Reverse a List:**
```python
nums = [1, 2, 3, 4, 5]
reversed = nums[::-1]  # [5, 4, 3, 2, 1]
```

**Skip Elements:**
```python
items = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Every 2nd element
evens = items[::2]   # [0, 2, 4, 6, 8]

# Every 3rd
every_third = items[::3]  # [0, 3, 6]
```

### Key Rules

1. **Stop is Exclusive:**
```python
lst = [1, 2, 3, 4, 5]
lst[1:3]  # [2, 3] - stops before index 3
```

2. **Omit Start or Stop:**
```python
lst[:3]   # From beginning to index 3
lst[3:]   # From index 3 to end
lst[:]    # Entire list (creates copy)
```

3. **Negative Indices:**
```python
lst[-3:]  # Last 3 elements
lst[:-2]  # All except last 2
```

### Try to Predict

```python
data = [10, 20, 30, 40, 50, 60, 70, 80]

a = data[2:5]    # ?
b = data[:4]     # ?
c = data[5:]     # ?
d = data[-2:]    # ?
e = data[::2]    # ?
f = data[::-1]   # ?
```

Answers:
- a: `[30, 40, 50]`
- b: `[10, 20, 30, 40]`
- c: `[60, 70, 80]`
- d: `[70, 80]`
- e: `[10, 30, 50, 70]`
- f: `[80, 70, 60, 50, 40, 30, 20, 10]`

Slicing is powerful - master it for cleaner code!


---

## Iterating Through Lists Using Loops

## What is Iteration?

Iteration is **automatically going through every item** in your list - like a machine that processes each piece on an assembly line!

### Simple Analogy

Think of iteration like **handing out flyers**:
- **Stack of flyers**: Your list
- **You**: The loop
- **Action**: Give one flyer to each person
- **Automatic**: Move to next person, repeat until done

Or like **feeding animals at a zoo**:
- **List of enclosures**: Your list
- **Zookeeper**: The loop
- **Each cage**: Gets fed (processed)
- **Systematic**: Don't skip any, don't feed twice

### Why Iteration is Magic

**Without iteration** - nightmare:
```python
print(list[0])
print(list[1])
print(list[2])
# ...what if there are 1000 items?!
```

**With iteration** - elegant:
```python
for item in list:
    print(item)
# Works for any size list!
```

**Scales infinitely** - same code handles 10 items or 10 million!

### What You'll Learn

Iteration means processing each element in a list one by one. Essential for working with list data.

### Why It Matters

Without iteration:
- Can't process multiple elements
- Can't apply logic to each item
- Limited to manual access

With iteration:
- Process all elements automatically
- Apply transformations
- Calculate aggregates

### Basic For Loop

**Most Common Pattern:**
```python
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)
# apple
# banana
# orange
```

**With Conditions:**
```python
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

### Getting Index with enumerate()

Sometimes you need both the position and the value:

```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# apple
# banana
# orange

# Start counting from 1
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
# apple
# banana
# orange
```

### Parallel Lists with zip()

Process multiple related lists together:

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
```

### Common Patterns

**Calculate Sum:**
```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(total)  # 150
```

**Build New List:**
```python
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]
```

**Count Matches:**
```python
grades = [85, 92, 78, 90, 88]
passing = 0

for grade in grades:
    if grade >= 80:
        passing += 1

print(f"Passing: {passing}")  # 4
```

### Important: Don't Modify While Iterating

```python
# WRONG - unpredictable behavior
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # BAD!

# RIGHT - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

### Try to Predict

```python
scores = [70, 85, 90, 75]
total = 0

for score in scores:
    total += score

average = total / len(scores)

# What is total?
# What is average?
```

Answers:
- total: `320`
- average: `80.0`

Iteration unlocks the power of lists!


---

## Using List Comprehensions

## What Are List Comprehensions?

List comprehensions are Python's **one-liner magic** for creating lists - like using a formula instead of manual calculation!

### Simple Analogy

Think of list comprehensions like **a factory machine**:
- **Traditional loop**: Manually take each raw material, process it, put in output box (slow!)
- **Comprehension**: Feed raw materials into machine, get processed items out (fast!)
- **Same result**: Processed items, but comprehension is elegant and quick

Or like **Excel formulas**:
- **Manual**: Type value in each cell one by one (tedious!)
- **Formula**: Write once, applies to all cells (=A1*2, drag down)
- **Comprehension**: Same idea for Python lists!

### Why Comprehensions Rock

**Readability**: Clear intent - "create list of squares"
**Speed**: 2-3x faster than loops (optimized internally)
**Pythonic**: Professional Python code uses them everywhere

**Before comprehensions existed** (Python 1.x), programmers had to write verbose loops. **After** (Python 2.0+), one clean line does it all!

### What You'll Learn

List comprehensions are a concise way to create lists in Python - transforming loops into single, elegant lines.

### Why It Matters

Without comprehensions:
```python
squares = []
for x in range(5):
    squares.append(x ** 2)
# lines, verbose
```

With comprehensions:
```python
squares = [x ** 2 for x in range(5)]
# line, clear intent
```

### Basic Syntax

**Pattern:**
```python
[expression for item in iterable]
```

**Examples:**
```python
# Numbers 0-4
nums = [x for x in range(5)]
# [0, 1, 2, 3, 4]

# Squares
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Uppercase strings
words = ['hello', 'world']
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']
```

### Adding Filters

Add `if` at the end to filter:

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Only long words
words = ['a', 'bat', 'elephant']
long = [w for w in words if len(w) > 3]
# ['elephant']
```

### if-else for Transformation

Use conditional expression to transform all elements:

```python
# Categorize as even/odd
types = ['even' if x % 2 == 0 else 'odd' for x in range(4)]
# ['even', 'odd', 'even', 'odd']

# Replace negatives with zero
nums = [5, -2, 8, -1]
positive = [x if x > 0 else 0 for x in nums]
# [5, 0, 8, 0]
```

### Key Differences

**Filter (omits items):**
```python
[x for x in list if condition]
# Some items removed
```

**Transform (keeps all):**
```python
[x if cond else y for x in list]
# All items kept, some changed
```

### Common Use Cases

**Extract data:**
```python
users = [{'name': 'Alice'}, {'name': 'Bob'}]
names = [u['name'] for u in users]
# ['Alice', 'Bob']
```

**Process strings:**
```python
data = "10,20,30"
numbers = [int(x) for x in data.split(',')]
# [10, 20, 30]
```

**Calculate:**
```python
prices = [10, 20, 30]
with_tax = [p * 1.08 for p in prices]
# [10.8, 21.6, 32.4]
```

### Benefits

1. **Concise** - One line vs multiple
2. **Faster** - Optimized internally
3. **Readable** - Clear intent
4. **Pythonic** - Preferred style

### Try to Predict

```python
result = [x * 3 for x in range(4) if x % 2 != 0]
```

What is `result`?

Answer: `[3, 9]`
- range(4) gives [0, 1, 2, 3]
- Filter odd: [1, 3]
- Multiply by 3: [3, 9]

List comprehensions = concise + powerful!


---

# Define Functions

## What are Functions?

Functions are **reusable blocks of code** that perform a specific task. They're like creating your own custom commands!

### Simple Analogy

Think of functions like **remote control buttons**:
- **Power button**: One press does a complex series of actions (turn on screen, load settings, connect to input, etc.)
- **You**: Just press button (call function)
- **Inside**: Complex code runs automatically
- **Result**: You work at a higher level - thinking in terms of actions, not implementation

Or like **a vending machine**:
- **Button**: You press "A3"
- **Hidden process**: Machine finds item, charges card, dispenses snack
- **You see**: Simple interface, complex internals

Functions let you create **custom actions** for your program!

### Why Functions Matter

Before functions, programmers copied the same code everywhere:
```python
# Without functions - repetitive nightmare!
print("-" * 40)
print("Welcome!")
print("-" * 40)

# ...100 lines later...
print("-" * 40)  # Same code again!
print("Welcome!")
print("-" * 40)
```

With functions - write once, use anywhere:
```python
def show_welcome():
    print("-" * 40)
    print("Welcome!")
    print("-" * 40)

show_welcome()  # Use anywhere, anytime!
```

## What are Functions?

Functions are reusable blocks of code that perform a specific task.

```python
def greet():
    print("Hello!")

greet()  # Calls the function
# Output: Hello!
```

## Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break code into logical pieces
3. **Maintainability**: Easier to update and debug

## Basic Syntax

```python
def function_name():
    # Code here
    pass
```

## Example

```python
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()
say_hello()
say_hello()

# Output: Hello, World! (3 times)
```


---

# Using Function Parameters to Accept Inputs

## Why Parameters?

Imagine having a different calculator for every pair of numbers you want to add - one for "5+3", another for "10+20", etc. Ridiculous, right? **Parameters** solve this - one function, infinite uses!

### Simple Analogy

Think of parameters like **placeholders in a Mad Libs game**:
- **Template**: "Hello, [NAME]! You are [AGE] years old."
- **Parameters**: NAME and AGE are slots you fill in
- **Infinite variations**: Change the values, get different results
- **Same structure**, different data each time

Or like **a blender**:
- **Machine**: The function (same every time)
- **Ingredients**: Parameters (different each time)
- **Banana smoothie**: blend(banana, milk, ice)
- **Berry smoothie**: blend(berries, yogurt, ice)
- **One blender**, many recipes!

## What You'll Learn
In this lesson, you'll learn how to define functions that accept parameters (inputs), making your functions flexible and reusable for different data.

## Why This Matters
Functions without parameters can only do one specific thing. Parameters make functions powerful:
- A calculator function that works with any two numbers
- A greeting function that works with any name
- A discount function that works with any price
- A validation function that checks any password

Parameters turn functions from single-use tools into versatile, reusable building blocks.

---

## What are Function Parameters?

**Parameters** are variables listed in the function definition that accept values when the function is called.

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is an argument
greet("Bob")    # "Bob" is an argument
```

**Key terms:**
- **Parameter**: Variable in function definition (`name`)
- **Argument**: Actual value passed when calling (`"Alice"`, `"Bob"`)

---

## Simple Example

```python
def add(a, b):  # a and b are parameters
    sum_result = a + b
    print(f"{a} + {b} = {sum_result}")

add(5, 3)   # 5 + 3 = 8
add(10, 20) # 10 + 20 = 30
add(7, 2)   # 7 + 2 = 9
```

**One function, many uses!** The same function works with different numbers.

---

## Multiple Parameters

You can have as many parameters as you need:

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")
```

**Order matters!** Arguments must match parameter order.

---

## Real-World Examples

### Example 1: Calculate Area

```python
def rectangle_area(length, width):
    area = length * width
    print(f"Area: {area} square units")

rectangle_area(5, 3)   # Area: 15 square units
rectangle_area(10, 8)  # Area: 80 square units
```

### Example 2: Check Password Strength

```python
def check_password(password, min_length):
    if len(password) >= min_length:
        print("Password is strong enough")
    else:
        print(f"Password too short. Need {min_length} characters")

check_password("abc", 8)        # Too short
check_password("secure123", 8)  # Strong enough
```

---

## Parameters Make Functions Flexible

### Without Parameters (Limited)

```python
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Only works for Alice!
```

### With Parameters (Flexible)

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
greet("Charlie") # Hello, Charlie!
```

---

## Try It Yourself (Before Class)

Write and run this function:

```python
def multiply(x, y):
    result = x * y
    print(f"{x} × {y} = {result}")

multiply(4, 5)
multiply(10, 3)
multiply(7, 7)
```

**Questions:**
1. What does each call print?
2. Try adding a third parameter `z` - what changes?
3. What happens if you call `multiply(5)` (only one argument)?

---

## Key Takeaways

Before class, remember:
1. **Parameters = inputs** - make functions flexible
2. **Defined in ()** - after function name
3. **Order matters** - arguments match parameter positions
4. **Multiple parameters** - separate with commas
5. **Reusability** - one function, many uses

## What's Next?

In the live session, we'll:
- Write functions with various parameter counts
- Learn about return values (sending data back)
- Explore default parameters
- Understand parameter vs argument terminology

See you in class!


---

# Returning Values from Functions Using Return

## Why Return?

Functions without return are like **ovens that cook but never open** - food cooks inside, but you can't get it out to eat! Return lets functions **give back** their results.

### Simple Analogy

Think of return like **an ATM dispensing cash**:
- **Input**: You insert card, enter PIN, request $100
- **Processing**: ATM validates, checks balance, prepares money
- **Return**: Money comes out of slot (this is the return!)
- **You use it**: Take money, buy things elsewhere

Or like **a microwave**:
- **Input**: Put food in, set timer
- **Processing**: Heats food inside
- **Return**: Beep! Food is ready (you take it out)
- **vs. No return**: Food cooks but stays locked inside forever!

### Return vs Print: The Big Confusion

**Beginners' biggest mistake**: Thinking `print()` and `return` are the same.
- **print()**: Shows something to YOU (the human)
- **return**: Gives something to THE CODE (for further use)

```python
def bad_calculator(a, b):
    print(a + b)  # Shows answer, but code can't use it!

# This doesn't work!
total = bad_calculator(5, 3) + 10  # Error! Can't add None + 10
```

Return makes functions **useful**, not just pretty displays!

## What You'll Learn
In this lesson, you'll learn how to use the `return` statement to send values back from functions, allowing you to use function results in other parts of your code.

## Why This Matters
So far, functions just print output. But what if you want to:
- Use a function's result in a calculation
- Store a function's result in a variable
- Pass a function's result to another function
- Make decisions based on a function's result

The `return` statement lets functions send data back to the caller, making them infinitely more useful.

---

## What is Return?

The `return` statement sends a value back from a function to wherever it was called.

```python
def add(a, b):
    return a + b  # Send the sum back

result = add(5, 3)  # result gets 8
print(result)       # 8
```

**Key difference:**
- `print()` → Shows output on screen
- `return` → Sends value back to use in code

---

## Return vs Print

### With Print (Limited)

```python
def add(a, b):
    print(a + b)  # Just displays

add(5, 3)  # Shows: 8
x = add(5, 3)  # x gets None (not the sum!)
print(x)  # None
```

### With Return (Flexible)

```python
def add(a, b):
    return a + b  # Send value back

result = add(5, 3)  # result gets 8
x = add(10, 20)     # x gets 30
total = add(result, x)  # Can use in more calculations!
print(total)  # 38
```

---

## Simple Examples

### Example 1: Calculate and Return

```python
def square(n):
    return n * n

x = square(5)  # x = 25
y = square(10) # y = 100
z = x + y      # z = 125
print(z)       # 125
```

### Example 2: Return in Conditions

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if is_even(4):
    print("4 is even")  # This prints!

if is_even(7):
    print("7 is even")  # This doesn't run
```

---

## Return Stops Function Execution

Once `return` runs, the function exits immediately:

```python
def check_age(age):
    if age < 18:
        return "Too young"  # Exit here if True
    return "Old enough"     # Only runs if age >= 18

print(check_age(15))  # "Too young"
print(check_age(25))  # "Old enough"
```

---

## Real-World Examples

### Example 1: Calculate Discount

```python
def apply_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price

shirt_price = apply_discount(50, 20)   # $40
shoe_price = apply_discount(100, 15)   # $85
total = shirt_price + shoe_price       # $125
print(f"Total: ${total}")
```

### Example 2: Validate Password

```python
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

password = input("Enter password: ")
if is_strong_password(password):
    print("Password accepted!")
else:
    print("Password too weak!")
```

---

## Returning Multiple Values

Python can return multiple values using tuples:

```python
def get_user_info():
    name = "Alice"
    age = 25
    city = "NYC"
    return name, age, city  # Returns tuple

name, age, city = get_user_info()
print(f"{name}, {age}, {city}")  # Alice, 25, NYC
```

---

## Try It Yourself (Before Class)

Run this code:

```python
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a, p = calculate_rectangle(5, 3)
print(f"Area: {a}, Perimeter: {p}")
```

**Questions:**
1. What values do `a` and `p` get?
2. Try returning just `area` without `perimeter` - what changes?
3. What happens if you don't return anything?

---

## Key Takeaways

Before class, remember:
1. **return sends values back** - for use in other code
2. **return exits function** - code after return doesn't run
3. **return vs print** - return for data, print for display
4. **Can return anything** - numbers, strings, booleans, tuples
5. **No return = None** - functions return None by default

## What's Next?

In the live session, we'll:
- Practice writing functions with return values
- Use returned values in complex calculations
- Understand when to return vs print
- Learn about returning multiple values
- Handle functions that return None

See you in class!


---

# Applying Default Parameters in Function Definitions

## Why Default Parameters?

Functions with lots of required parameters are annoying to use. Default parameters make functions **easy to use** for common cases while staying **powerful** for complex cases!

### Simple Analogy

Think of default parameters like **ordering coffee**:
- **Required**: "I want a coffee" (must specify)
- **Defaults**: Medium size, regular milk, normal temperature (most people want this)
- **Override when needed**: "Make it large, almond milk, extra hot" (customize!)
- **Result**: Quick ordering for most, detailed control when needed

Or like **phone settings**:
- **Auto-brightness**: ON by default (works for 90% of users)
- **Override**: Turn off and set manually if you want
- **Smart design**: Common case is easy, customization available

Default parameters = **convenience with flexibility**!

## What You'll Learn
In this lesson, you'll learn how to provide default values for function parameters, making some arguments optional when calling the function.

## Why This Matters
Default parameters make functions more flexible:
- Users can provide custom values OR use sensible defaults
- Reduces the number of required arguments
- Makes functions easier to use
- Common in professional Python code

Example: `print()` has default parameter `end="\n"` (newline). You can override it: `print("Hi", end="")`

---

## What are Default Parameters?

**Default parameters** have predefined values. If the caller doesn't provide a value, the default is used.

```python
def greet(name, greeting="Hello"):  # greeting has default
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice! (uses default)
greet("Bob", "Hi")          # Hi, Bob! (overrides default)
greet("Charlie", "Hey")     # Hey, Charlie!
```

---

## Syntax

```python
def function_name(required_param, optional_param=default_value):
    # code
```

**Rules:**
1. Default parameters come AFTER required parameters
2. Can have multiple default parameters
3. Caller can override any default

---

## Simple Examples

### Example 1: Power Function

```python
def power(base, exponent=2):  # exponent defaults to 2 (square)
    return base ** exponent

print(power(5))      # 25 (5²)
print(power(5, 3))   # 125 (5³)
print(power(2, 4))   # 16 (2⁴)
```

### Example 2: Greeting with Time

```python
def greet(name, time_of_day="day"):
    if time_of_day == "morning":
        print(f"Good morning, {name}!")
    elif time_of_day == "evening":
        print(f"Good evening, {name}!")
    else:
        print(f"Good day, {name}!")

greet("Alice")                # Good day, Alice!
greet("Bob", "morning")       # Good morning, Bob!
greet("Charlie", "evening")   # Good evening, Charlie!
```

---

## Real-World Examples

### Example 1: Calculate Discount

```python
def apply_discount(price, discount=10):  # 10% default
    final_price = price * (1 - discount/100)
    return final_price

print(apply_discount(100))      # 90 (10% off)
print(apply_discount(100, 20))  # 80 (20% off)
print(apply_discount(50, 5))    # 47.5 (5% off)
```

### Example 2: Print Message with Separator

```python
def print_message(message, sep="-", length=20):
    print(sep * length)
    print(message)
    print(sep * length)

print_message("Hello")           # Uses defaults
print_message("Python", "*")     # Custom separator
print_message("Code", "=", 30)   # Custom both
```

---

## Order Matters!

**Correct:** Required parameters first, then defaults

```python
def greet(name, greeting="Hello"):  # ✓ Correct
    print(f"{greeting}, {name}")
```

**Incorrect:** Defaults before required

```python
def greet(greeting="Hello", name):  # ✗ SyntaxError!
    print(f"{greeting}, {name}")
```

---

## Multiple Defaults

```python
def create_profile(name, age=18, city="Unknown", country="USA"):
    print(f"{name}, {age}, {city}, {country}")

create_profile("Alice")                    # Alice, 18, Unknown, USA
create_profile("Bob", 25)                  # Bob, 25, Unknown, USA
create_profile("Charlie", 30, "NYC")       # Charlie, 30, NYC, USA
create_profile("David", 22, "LA", "USA")   # David, 22, LA, USA
```

---

## Try It Yourself (Before Class)

```python
def repeat_text(text, times=3, separator=" "):
    return (text + separator) * times

print(repeat_text("Hi"))
print(repeat_text("Hello", 5))
print(repeat_text("Python", 2, "-"))
```

**Questions:**
1. What does each call output?
2. Can you call it with just one argument?
3. What happens if you provide all three arguments?

---

## Key Takeaways

Before class, remember:
1. **Default parameters** - have predefined values
2. **Optional arguments** - caller can skip or override
3. **Order matters** - required first, defaults after
4. **Multiple defaults** - can have many
5. **Common pattern** - makes functions flexible

## What's Next?

In the live session, we'll:
- Write functions with multiple default parameters
- Learn about keyword arguments
- Understand when to use defaults
- Combine defaults with return values

See you in class!


---

