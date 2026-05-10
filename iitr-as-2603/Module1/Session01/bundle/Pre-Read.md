# Define Variables

## What You'll Learn
In this lesson, you'll learn what variables are and how to create them in Python. Variables are the foundation of all programming!

## Why This Matters
Imagine you're building a calculator app. You need to remember:
- The first number the user enters
- The second number
- The operation they want to perform
- The result

Without variables, the computer has no way to remember these values. Variables are like labeled containers that store information your program needs.

---

## What is a Variable?

Think of a variable as a **labeled box** in the computer's memory. You give it a name (the label) and put data inside it (the contents).

```python
score = 100
```

This creates a box labeled `score` and puts the number `100` inside it.

### A Brief History: Why Variables Matter

In the early days of computing (1940s), programmers had to write numbers directly into machine code. If you wanted to change a value, you'd have to rewrite the entire program!

Variables revolutionized programming by introducing **symbolic names** for data. Now we can write `total = price * quantity` and the computer figures out the actual numbers. This was a game-changer - it made programs:
- **Reusable** - same code works with different data
- **Readable** - `age` is clearer than remembering "memory location 1047"
- **Flexible** - values can change while the program runs

### Another Way to Think About Variables

Consider a spreadsheet cell:
- Cell **A1** is like a variable name
- The **value in A1** is like the variable's value
- You can reference **A1** in formulas, and if A1 changes, all formulas update automatically

Variables work the same way in Python!

## Creating Variables in Python

Creating a variable in Python is simple - just use the equals sign `=`:

```python
age = 25
name = "Alice"
price = 19.99
is_active = True
```

**Important**: The `=` sign means "assign," not "equals" like in math!

### How to Read This Code

```python
age = 25
```

Read this as: **"age is assigned 25"** or **"assign 25 to age"**

Don't read it as "age equals 25" - that's mathematical equality, not assignment.

---

## Variables Can Change

Unlike in mathematics, variables in programming can be reassigned to different values:

```python
score = 100
print(score)  # Shows: 100

score = 150   # Change the value
print(score)  # Shows: 150
```

The variable `score` now contains `150` instead of `100`. The old value is gone.

---

## Real-World Example

```python
# Storing game information
player_name = "DragonMaster"
health = 100
level = 5

print(player_name)  # DragonMaster
print(health)       # 100
print(level)        # 5

# Player takes damage
health = 75
print(health)       # 75
```

---

## Try It Yourself (Before Class)

Run this code and see what happens:

```python
# Create variables
my_name = "YourNameHere"
my_age = 20
my_score = 95

# Print them
print(my_name)
print(my_age)
print(my_score)

# Change a variable
my_score = 100
print(my_score)  # What will this show?
```

**Expected Output:**
YourNameHere
20
95
100

---

## Key Takeaways

Before class, remember:
1. **Variables store data** - like labeled containers
2. **Use `=` to create variables** - `name = value`
3. **Variables can be reassigned** - they can change value
4. **The `=` means "assign"** - not mathematical equality

## Questions to Think About

Come to class ready to discuss:
- Why would we want to change a variable's value?
- What happens to the old value when we reassign a variable?
- Can you think of examples from apps you use that would need variables?

## What's Next?

In the live session, we'll:
- Practice creating many different variables
- Learn the rules for naming variables
- Understand how variables work in memory
- Build programs that use variables effectively

See you in class!


---

# Apply Variable Naming Conventions

## Why Naming Matters

Imagine reading a book where every character was named "Person1", "Person2", "Person3". Confusing, right?

Variable names are the same - they tell the story of your code. Good names make code **self-explanatory**. Bad names require constant mental translation and lead to bugs.

### The Cost of Bad Naming

Consider this real example:
```python
# Unclear
d = 86400
t = d * 7
```

vs.

```python
# Clear
seconds_per_day = 86400
seconds_per_week = seconds_per_day * 7
```

The second version needs no comments - the names explain everything. The first version forces you to guess what `d` and `t` mean.

**In professional development:**
- Poor naming wastes hours of debugging time
- Good naming prevents bugs before they happen
- Clear names reduce onboarding time for new team members

### Python's Philosophy: Community Standards

Python has an official style guide called **PEP 8**. It's not just suggestions - it's how the entire Python community writes code.

Following PEP 8 means:
- Your code looks professional
- Other Python developers can read it instantly
- You can read their code easily too
- Tools can automatically check your style

Think of it like **driving on the right side of the road** - it's a convention that makes everyone safer.

## Naming Rules (MUST Follow)

### Start with letter or underscore
✅ `age`, `_private`, `user1`
❌ `1age`, `@user`

### Only letters, numbers, underscores
✅ `student_name`, `score_2024`
❌ `student-name`, `score$`

### Case-sensitive
`age`, `Age`, `AGE` are THREE different variables

### No reserved keywords
❌ `for`, `if`, `while`, `class`

## Naming Conventions (Best Practice)

### Use snake_case
```python
student_name = "Alice"  # Good
studentName = "Alice"   # Works but not Pythonic
```

### Be descriptive
```python
student_count = 30    # Clear
sc = 30               # Unclear
```

### Booleans sound like questions
```python
is_active = True
has_permission = False
```

## Try Before Class
Which names are valid?
- `my_name` ✅
- `2nd_place` ❌ (starts with number)
- `first-name` ❌ (has hyphen)
- `_value` ✅


---

# Implement Integer Data Types

## What are Integers?

**Integers** are whole numbers - no decimal points!

Examples: `5`, `-3`, `0`, `1000`, `-999`

Not integers: `5.5`, `3.14`, `0.1` (these are floats)

### Why Do We Need Different Number Types?

You might wonder: "Why not just use one number type for everything?"

Think about real life:
- When counting apples, you say "5 apples", not "5.0 apples"
- When measuring height, you say "5.8 feet" (need decimals)

Computers work the same way! Different number types serve different purposes:
- **Integers**: Counting, indexing, discrete quantities
- **Floats**: Measurements, prices, scientific calculations

**Bonus**: Integer arithmetic is faster and more precise than float arithmetic. When you don't need decimals, integers are the better choice.

### Simple Analogy

Think of integers like **whole coins**:
- You can have 1 coin, 5 coins, 100 coins
- You can't have 2.7 coins (you can't split a coin)
- Even if you have zero coins, that's still a whole number: 0

Floats are like **liquid in a measuring cup** - you can have 2.5 cups, 3.14 cups, any amount!

## Creating Integer Variables

```python
age = 25
year = 2024
count = 0
temperature = -5
```

## Integer Operations

### Basic Arithmetic
```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
```

### Division: Two Types!

**Regular division** (`/`) - returns float:
```python
print(10 / 3)   # 3.3333...
print(10 / 2)   # 5.0 (still a float!)
```

**Integer division** (`//`) - returns integer:
```python
print(10 // 3)  # 3 (drops decimal)
print(10 // 2)  # 5 (integer)
```

### Modulo (Remainder)
```python
print(10 % 3)   # 1 (remainder of 10 ÷ 3)
print(10 % 2)   # 0 (10 is even, no remainder)
```

## When to Use Integers

✅ **Use integers for:**
- Counting things (10 students)
- Ages (25 years old)
- Years (2024)
- Quantities that don't need decimals

❌ **Don't use integers for:**
- Prices ($19.99)
- Measurements (5.5 feet)
- Percentages (87.5%)

## Try Before Class

```python
students = 30
teachers = 5

total_people = students + teachers
print(total_people)  # What will this print?

ratio = students // teachers
print(ratio)  # What about this?
```

## Key Points
- Integers = whole numbers
- Use `/` for decimal division, `//` for integer division
- Python integers have no size limit!
- Choose int when you don't need decimals


---

# Implement Float Data Types

## What are Floats?

**Floats** are numbers with decimal points.

Examples: `3.14`, `0.5`, `-2.75`, `100.0`

### Why Floats Matter

Imagine building a calculator that can only handle whole numbers. You couldn't:
- Calculate prices: $19.99
- Measure distances: 3.7 miles
- Find averages: 87.5%
- Do scientific work: π = 3.14159...

Floats give us the ability to work with **continuous quantities** - things that can be divided infinitely small, like length, weight, time, and money.

### Simple Analogy

**Integers** are like **stairs**: You're on step 1, step 2, step 3. No in-between.

**Floats** are like a **ramp**: You can be at position 1.5, 2.3, 2.75 - anywhere along the slope.

Both get you up a level, but floats give you more precise positions.

## Creating Floats
```python
price = 19.99
height = 5.8
temperature = 98.6
pi = 3.14159
```

Even `5.0` is a float (has decimal point)!

## Float Arithmetic
```python
a = 10.5
b = 2.5

print(a + b)  # 13.0
print(a - b)  # 8.0
print(a * b)  # 26.25
print(a / b)  # 4.2
```

## Precision Surprise
```python
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3!)
```

Why? Computers store decimals in binary - some can't be represented exactly.

**Think of it like measuring with a ruler**:
- You want to measure exactly 0.1 inches
- But your ruler only has marks at 0.09 and 0.11
- You have to pick the closest mark
- That tiny error adds up when you combine measurements

This is rare in practice, but important to know. For everyday calculations (prices, percentages), Python's floats work great!

## When to Use Floats
✅ Prices, measurements, percentages, scientific calculations
❌ Counting, ages, years (use int)

## Try It
```python
price = 19.99
quantity = 3
total = price * quantity
print(total)  # What will this be?
```


---

# Implement String Data Types

## What are Strings?

**Strings** are text data - any characters in quotes.

```python
name = "Alice"
message = 'Hello, World!'
email = "user@example.com"
```

Single `'` or double `"` quotes both work!

### Why Strings Are Different

You've learned numbers (int, float). Why do we need a separate type for text?

**Computers only understand numbers** (0s and 1s). When you write "Hello":
- The computer doesn't see letters
- It sees numbers: [72, 101, 108, 108, 111]
- Each letter has a number code
- Python handles this translation automatically!

This is why you can't do `"5" + 5` - one is the text character "5", the other is the number 5. They're stored completely differently.

### Simple Analogy

Think of a string like a **necklace**:
- Each character is a bead
- The beads are strung together in order
- "Hello" is 5 beads: H-e-l-l-o
- You can't have half a bead (can't split a character)
- The order matters: "Hello" ≠ "olleH"

### Why Order Matters

Unlike numbers (5 + 3 = 3 + 5), strings care about order:
- "cat" ≠ "act"
- "hello" ≠ "olleh"

This is because strings represent **language**, and language has grammar and meaning tied to order.

## String Operations

### Concatenation (Combining)
```python
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # "Hello World"
```

### Repetition
```python
laugh = "ha" * 3
print(laugh)  # "hahaha"
```

### Length
```python
name = "Alice"
print(len(name))  # 5
```

## Special Characters
```python
# Use opposite quotes inside
message = "He said, 'Hello!'"
message = 'She said, "Hi!"'

# Or escape quotes
message = "He said, \"Hello!\""
```

## When to Use Strings
✅ Names, messages, text, emails, URLs, addresses

## Try It
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)
```


---

# Implement Boolean Data Types

## What are Booleans?

**Booleans** have only TWO values: `True` or `False`

```python
is_student = True
has_graduated = False
is_raining = True
```

**Important**: Must be capitalized - `True` and `False` (not `true` or `false`)

### Why Booleans Exist

Programs constantly make decisions:
- Should I show this button?
- Is the user allowed to access this?
- Did the file save successfully?
- Has the timer run out?

All these are **yes/no questions**. Booleans are the data type designed specifically for this.

**Without booleans**, we'd have to use numbers:
```python
is_logged_in = 1  # 1 means yes, 0 means no? Confusing!
```

**With booleans**, the code is clear:
```python
is_logged_in = True  # Crystal clear!
```

### Simple Analogy

Booleans are like **checkbox questions** on a form:
- ☑ "Do you accept the terms?" → True (checked)
- ☐ "Subscribe to newsletter?" → False (unchecked)

Not like fill-in-the-blank questions where you can write anything - just check or don't check.

### The Power of Two

Having only two values might seem limiting, but it's incredibly powerful:
- Computers are built on billions of two-state switches
- Every decision tree breaks down into yes/no branches
- Simple + billions of operations = complex behavior

## When to Use Booleans
- Yes/No questions
- On/Off states  
- Enabled/Disabled
- Pass/Fail

## Boolean in Action
```python
is_logged_in = True

if is_logged_in:
    print("Welcome back!")  # This runs
```

## Naming Booleans
Make them sound like questions:
```python
is_active = True      # "Is it active?"
has_permission = False  # "Has permission?"
can_edit = True       # "Can edit?"
```


---

# Inspecting Data Types Using type()

## What is type()?

The `type()` function tells you **what kind of data** a variable contains.

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>
```

## Why Do We Need type()?

In Python, you don't have to declare types:
```python
x = 5  # Python automatically knows it's an int
```

But sometimes you need to **check** what type something is, especially when debugging:
```python
result = some_function()
print(type(result))  # "What did this function return?"
```

### Simple Analogy

Think of `type()` like asking **"What is this?"**

- You find a container in the fridge
- You ask: "Is this milk or juice?"
- `type()` tells you: "This is milk!"

Similarly, with variables:
- You have a variable `x`
- You ask: `type(x)`
- Python tells you: "This is an int!"

## Why Types Can Be Confusing

Consider this surprise:
```python
age = "25"  # Looks like a number, but it's a string!
print(type(age))  # <class 'str'>

result = age + 5  # ❌ Error! Can't add string and int
```

The `type()` function helps you spot these issues:
- `"25"` is text (string)
- `25` is a number (int)
- They look similar but behave differently!

## Python's Flexibility

Unlike some languages, Python lets variables **change types**:
```python
x = 5          # x is an int
print(type(x))  # <class 'int'>

x = "hello"     # Now x is a string!
print(type(x))  # <class 'str'>
```

This flexibility is powerful but can lead to bugs. The `type()` function helps you keep track.

## Try Before Class

```python
a = 10
b = 10.0
c = "10"

print(type(a))  # What will this show?
print(type(b))  # What about this?
print(type(c))  # And this?
```

**Hint**: They all look similar, but have different types!

## Key Points
- `type()` reveals what kind of data a variable holds
- Essential for debugging type errors
- Python variables can change types
- Use `type()` when unsure what you're working with


---

# Perform Arithmetic Operations

## Arithmetic Operators in Python

Python supports all standard math operations plus more!

### Why Programming Needs Arithmetic

Every program you've ever used does math behind the scenes:
- **Social media**: Counting likes, calculating timestamps, sorting posts
- **Games**: Health points, damage calculations, scoreboards
- **Shopping apps**: Prices, discounts, totals, tax
- **Music players**: Track duration, progress bar position
- **Maps**: Distance calculations, estimated arrival time

Without arithmetic operators, programs would be useless - they couldn't count, calculate, or keep score!

### Simple Analogy

Think of arithmetic operators as **buttons on a calculator**:
- **+** button for addition
- **−** button for subtraction
- **×** button for multiplication
- **÷** button for division

Python gives you these same "buttons" (operators) to perform calculations in code.

The difference? A calculator handles one operation at a time. Python can perform millions of calculations per second, automatically, following your instructions!

### Basic Operations

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division - always float)
```

### Special Operators

**Integer Division** (`//`):
```python
print(10 // 3)  # 3 (drops decimal)
```

**Modulo/Remainder** (`%`):
```python
print(10 % 3)   # 1 (remainder)
```

**Exponentiation** (`**`):
```python
print(2 ** 3)   # 8 (2³ = 2 × 2 × 2)
```

### Augmented Assignment

Shortcuts for updating variables:

```python
score = 100
score = score + 50  # Long way
score += 50         # Short way (same thing!)
```

All operators have shortcuts:
```python
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
```

## Try Before Class

```python
# Calculate area of rectangle
length = 10
width = 5
area = length * width
print(area)  # What will this be?

# Update score
score = 100
score += 50  # Add 50 points
score -= 25  # Lose 25 points
print(score)  # What's the final score?
```

## Key Points
- `/` always returns float, even for whole numbers
- `//` returns integer (floor division)
- `%` gives remainder (useful for even/odd checks)
- `**` is power/exponentiation
- Augmented assignment makes code cleaner


---

# Apply Operator Precedence

## Order of Operations (PEMDAS)

Just like in math, Python follows an order:

### Why This Matters

Without order rules, expressions would be ambiguous:
```python
result = 2 + 3 * 4
```

Should this be:
- `(2 + 3) * 4 = 20`? OR
- `2 + (3 * 4) = 14`?

**The answer**: Math rules say multiply first → `14`

### Simple Analogy

Think of operator precedence like a **cafeteria line**:
- VIP customers (parentheses) go first
- Regular customers follow in order (exponents, then ×/÷, then +/−)
- Everyone waits their turn!

Or like **assembly line priority**:
- Some tasks MUST happen before others
- Multiply before you add (just like you must bake before you frost a cake)

**P**arentheses
**E**xponents
**M**ultiplication/**D**ivision (left to right)
**A**ddition/**S**ubtraction (left to right)

```python
result = 2 + 3 * 4
print(result)  # 14, not 20!
# Because: 3 * 4 happens first (12), then + 2
```

## Use Parentheses

```python
result = (2 + 3) * 4
print(result)  # 20
# Parentheses force addition first
```

## Examples

```python
# Without parentheses
print(10 + 5 * 2)    # 20 (5*2=10, then +10)

# With parentheses  
print((10 + 5) * 2)  # 30 (10+5=15, then *2)
```

## Key Point
When in doubt, use parentheses!


---

# Use Comparison Operators

## What You'll Learn
In this lesson, you'll learn how to compare values in Python using comparison operators.

## What are Comparison Operators?
Comparison operators let you **compare two values** and get a True or False answer.

Think of it like asking questions:
- "Is 5 greater than 3?" → True
- "Is my age equal to 18?" → Could be True or False

### Why Programs Need to Compare

Every smart app you use makes comparisons constantly:
- **Netflix**: Is movie rating >= 4 stars? Show it in "Recommended"
- **Amazon**: Is price < $50? Show "Under $50" badge
- **Spotify**: Is play_count > 1000? Add to "Popular" playlist
- **Phone**: Is battery_level <= 20%? Show low battery warning

Without comparisons, apps couldn't filter, sort, or make decisions!

### Simple Analogy

Comparison operators are like **yes/no questions**:
- "Is the door locked?" → Yes/No (True/False)
- "Is the water hot?" → Yes/No (True/False)
- "Is today Monday?" → Yes/No (True/False)

Computers use these True/False answers to decide what to do next.

## The Six Comparison Operators

```python
# Equal to
5 == 5    # True
5 == 3    # False

# Not equal to
5 != 3    # True
5 != 5    # False

# Greater than
5 > 3     # True
3 > 5     # False

# Less than
3 < 5     # True
5 < 3     # False

# Greater than or equal to
5 >= 5    # True
5 >= 3    # True
3 >= 5    # False

# Less than or equal to
5 <= 5    # True
3 <= 5    # True
5 <= 3    # False
```

## Important Note
**Single `=` vs Double `==`**
- `=` assigns a value: `age = 18`
- `==` checks equality: `age == 18`

Don't confuse them!

## Real-World Example
```python
age = 17
can_vote = age >= 18
print(can_vote)  # False
```

## What's Next?
In the main lesson, you'll learn:
- How to use each comparison operator
- What True and False mean in Python
- Comparing different data types
- Practical applications


---

