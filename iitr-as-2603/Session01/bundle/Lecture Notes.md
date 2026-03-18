# Define Variables

## Introduction
Variables are the fundamental building blocks of programming. They allow programs to store, retrieve, and manipulate data. In this lesson, you'll learn how to create and use variables in Python.

---

<div align="center">

![Python Variables Memory Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.1.png)

*Variables are named references to objects — Python's type hierarchy shows all the types a variable can hold*

</div>

---

## What are Variables?

### Definition
A **variable** is a named location in computer memory that stores a value. Think of it as a labeled container where you can put data and retrieve it later.

### Why Variables Are Fundamental
Variables are one of the most revolutionary concepts in computing. Without them, we'd have to:
- Write every value directly in our code
- Rewrite programs whenever data changes
- Have no way to remember user inputs or calculations

Variables give programs **memory** and **flexibility** - they're the difference between a calculator that can only do 2+3, and one that can add any numbers you choose.

### Real-World Analogy
Imagine your locker at school:
- The **locker number** is like the variable name
- The **contents inside** are like the value
- You can **change what's inside** anytime

Or think of variables like **pronouns in language**:
- Instead of saying "John went to John's house because John forgot John's keys"
- We say "John went to **his** house because **he** forgot **his** keys"
- Variables let us say `total = price * quantity` instead of repeating actual numbers everywhere

### The Assignment Operator (=)

In Python, we create variables using the `=` operator:

```python
age = 25
```

**Important**: Read this as "age is assigned 25" or "25 is assigned to age"
- The `=` is **assignment**, not mathematical equality
- Variable name goes on the **left**
- Value goes on the **right**

---

## Creating Variables

### Basic Syntax

```python
variable_name = value
```

### Examples

```python
score = 100
name = "Alice"
price = 19.99
is_active = True
```

### What Happens in Memory

When you write `score = 100`:
1. Python allocates memory space
2. Stores the value `100` in that space
3. Creates a label `score` pointing to that memory location

Memory:  [100]

Label:   score

**Important Concept: Variables as References**

In Python, variables don't actually "contain" values - they **point to** (or reference) values in memory:

```python
x = 5
```

This creates the number `5` somewhere in memory, and makes `x` point to it. Think of it like:
- The value `5` is a house
- The variable `x` is the house's address
- You use the address to find the house

This is why we can have multiple variables pointing to the same value:
```python
a = 10
b = a  # b now points to the same value as a
```

**Python's Memory Management**

Unlike languages like C or C++, Python handles memory automatically:
- You don't need to declare variable types beforehand
- Python automatically allocates and frees memory
- This makes Python easier to learn, but understanding references helps avoid bugs

---

## Variable Reassignment

Variables can be changed - they're called "variables" because their values can **vary**!

### Example

```python
health = 100
print(health)  # Output: 100

health = 75    # Player took damage
print(health)  # Output: 75

health = 100   # Player healed
print(health)  # Output: 100
```

### What Happens to the Old Value?

When you reassign a variable, the old value is **discarded**:

```python
x = 5
x = 10  # The value 5 is gone, x now refers to 10
```

---

## Multiple Variables

You can create many variables in a program:

```python
# Game character
player_name = "DragonSlayer"
health = 100
mana = 50
level = 5
is_alive = True

print(player_name)  # DragonSlayer
print(health)       # 100
print(level)        # 5
```

### Multiple Assignment

Python allows creating multiple variables in one line:

```python
# Create three variables at once
x, y, z = 10, 20, 30

print(x)  # 10
print(y)  # 20
print(z)  # 30
```

### Same Value to Multiple Variables

```python
# All three variables get the same value
a = b = c = 0

print(a)  # 0
print(b)  # 0
print(c)  # 0
```

---

## Using Variables

Once created, you can use variables in your code:

### In Calculations

```python
price = 100
quantity = 3
total = price * quantity
print(total)  # 300
```

### In Strings (Preview)

```python
name = "Alice"
print("Hello, " + name)  # Hello, Alice
```

### Updating Variables Based on Current Value

```python
score = 100
score = score + 50  # Add 50 to current score
print(score)  # 150
```

**Shorthand** (you'll learn more later):
```python
score = 100
score += 50  # Same as: score = score + 50
print(score)  # 150
```

---

## Practical Examples

### Example 1: Simple Calculator

```python
num1 = 15
num2 = 7

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

print(sum_result)    # 22
print(difference)    # 8
print(product)       # 105
```

### Example 2: Shopping Cart

```python
item_price = 29.99
quantity = 2
tax_rate = 0.08

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal:", subtotal)  # 59.98
print("Tax:", tax)            # 4.7984
print("Total:", total)        # 64.7784
```

# Player completes level 1
player_score = player_score + 100
print("After level 1:", player_score)   # 100

# Player completes level 2
player_score = player_score + 150
print("After level 2:", player_score)   # 250

# Player loses points
player_score = player_score - 50
print("Final score:", player_score)     # 200

---

## Common Mistakes and How to Fix Them

### Mistake 1: Trying to Use Before Creating

```python
print(name)  # L NameError: name 'name' is not defined
```

**Fix**: Create the variable first
```python
name = "Alice"
print(name)  #  Alice
```

### Mistake 2: Confusing Assignment Direction

```python
25 = age  # L SyntaxError: cannot assign to literal
```

**Fix**: Variable name goes on the left
```python
age = 25  #  Correct
```

### Mistake 3: Using Quotes for Variable Names

```python
"score" = 100  # L SyntaxError
```

**Fix**: No quotes around variable names
```python
score = 100  #  Correct
```

---

## The print() Function

You've seen `print()` in examples. It displays values:

```python
age = 25
print(age)        # Shows: 25
print("Hello")    # Shows: Hello

# Multiple values
name = "Bob"
age = 30
print(name, age)  # Shows: Bob 30
```

---

## Key Takeaways

1. **Variables store data** - they're like labeled containers in memory
2. **Use `=` to assign values** - variable_name = value
3. **Variables can be reassigned** - their values can change
4. **Create before using** - must define a variable before referencing it
5. **`=` means assign, not equals** - don't confuse with mathematical equality

---

## Practice Exercise

Create a program that tracks a bank account:

```python
# Starting balance
account_balance = 1000
print("Starting balance:", account_balance)

# Deposit money
account_balance = account_balance + 500
print("After deposit:", account_balance)

# Withdraw money
account_balance = account_balance - 200
print("After withdrawal:", account_balance)

# Expected output:
# Starting balance: 1000
# After deposit: 1500
# After withdrawal: 1300
```

---



---

# Apply Variable Naming Conventions

## Introduction

Variable naming is more than just following syntax rules - it's about **communication**. Code is read far more often than it's written, and good naming makes your code self-documenting.

### Why Naming Conventions Exist

In the early days of programming, developers worked alone. But modern software is built by teams, often across countries and time zones. Without naming conventions:
- Reading someone else's code becomes a puzzle
- Different styles make codebases look inconsistent
- Onboarding new developers takes longer
- Bugs hide in unclear variable names

Think of naming conventions like **traffic rules** - they're not about restricting you, they're about making sure everyone can work together smoothly.

### PEP 8: Python's Style Guide

**PEP** stands for "Python Enhancement Proposal". PEP 8 is Python's official style guide, created in 2001.

It standardizes:
- How to name variables, functions, and classes
- How to format code (spacing, indentation)
- Best practices for writing readable Python

Following PEP 8 means your code looks "Pythonic" - like it belongs in the Python ecosystem.

**The Zen of Python** (type `import this` in Python) says:
> "Readability counts"
> "There should be one-- and preferably only one --obvious way to do it"

PEP 8 embodies these principles.

---

<div align="center">

![Python PEP 8 Naming Convention snake_case camelCase](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.2.png)

*PEP 8 naming conventions (snake_case for variables, UPPER_CASE for constants) keep Python code consistent and readable*

</div>

---

## Naming Rules (Must Follow)

### Start with letter or underscore
✅ `name`, `_value`
❌ `1name`, `@user`

### Only letters, numbers, underscores
✅ `student_name`, `score_2024`
❌ `student-name`, `total$`

### Case sensitive
`age` ≠ `Age` ≠ `AGE`

### No reserved keywords
❌ `for`, `if`, `while`, `class`

## Naming Conventions (Best Practice)

### snake_case: Python's Signature Style

Python uses **snake_case** (words separated by underscores) for variables and functions.

```python
student_name = "Alice"  # Pythonic ✅
studentName = "Alice"   # Not Pythonic (camelCase) ❌
StudentName = "Alice"   # Not Pythonic (PascalCase) ❌
```

**Why snake_case?**
- More readable than camelCase: `calculate_total_price` vs `calculateTotalPrice`
- Matches Python's standard library: `str.upper()`, `os.path`, `datetime.now()`
- Research shows snake_case is easier to read for most people

**Note**: Other languages use different conventions:
- JavaScript: `camelCase` (`studentName`)
- C#/Java: `PascalCase` for classes (`StudentName`)
- Python reserves `PascalCase` for class names only

### Be Descriptive: Names as Documentation

Your variable name should answer: "What does this store?"

```python
# Good - self-explanatory
student_count = 30
total_price = 199.99
is_logged_in = True

# Bad - requires comments or context
sc = 30       # What's sc? Student count? Score? Screen?
t = 199.99    # Total? Temperature? Time?
flag = True   # Flag for what?
```

**Exception**: Short names are fine for:
- Loop counters: `for i in range(10)`
- Mathematical formulas: `area = pi * r * r`
- Very local scope (< 5 lines)

### Constants in UPPER_CASE

Values that never change should use ALL_CAPS:

```python
MAX_SIZE = 100
PI = 3.14159
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30
```

This signals to other developers: "Don't modify this value"

**Real-world impact**: In a team project, if you see `MAX_CONNECTIONS = 100`, you know it's a configuration constant. If you see `max_connections = 100`, it might be a variable that changes.

## Key Takeaways
1. Follow rules to avoid errors
2. Use snake_case for variables
3. Be descriptive and clear
4. Avoid reserved keywords


---

# Implement Integer Data Types

## Introduction
Integers (int) are one of Python's fundamental data types. They represent whole numbers and are used for counting, indexing, and any quantity that doesn't require decimal precision.

---

<div align="center">

![Python Data Types Overview](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.3.jpg)

*Integers (int) are part of Python's numeric type hierarchy — whole numbers with unlimited precision*

</div>

---

## What are Integers?

### Definition
**Integer**: A whole number with no decimal point
- Can be positive: `5`, `100`, `2024`
- Can be negative: `-3`, `-50`, `-999`
- Can be zero: `0`

### Why Integers Are Fundamental

Integers are the mathematical foundation of computing. At the lowest level, computers understand only two states: on (1) and off (0). These binary digits combine to represent integers, which then represent everything else - text, images, videos, and more.

**Historical Note**: Early computers could only work with integers. Decimal numbers (floats) came later and required special hardware. Even today, integer operations are faster than float operations on most processors.

### Real-World Analogy

Think of integers like **counting blocks**:
- You can have 1 block, 2 blocks, 10 blocks
- You can't have 2.5 blocks - blocks are whole units
- Similarly, you can have 5 students, but not 5.3 students

Or think about **floors in a building**:
- Ground floor (0), 1st floor, 2nd floor...
- Basement levels: -1, -2, -3...
- No "floor 2.5"!

### Creating Integer Variables
```python
age = 25
year = 2024
score = 0
temperature = -10
```

### Checking Type
```python
count = 100
print(type(count))  # <class 'int'>
```

---

## Integer Arithmetic

### Addition and Subtraction
```python
a = 10
b = 3

sum_result = a + b
print(sum_result)  # 13

difference = a - b
print(difference)  # 7
```

### Multiplication
```python
price = 5
quantity = 10
total = price * quantity
print(total)  # 50
```

### Division: Two Types

**Regular Division** (`/`) - Always returns float:
```python
result = 10 / 3
print(result)        # 3.3333333...
print(type(result))  # <class 'float'>

result = 10 / 2
print(result)        # 5.0 (still a float!)
```

**Integer Division** (`//`) - Returns integer (floor division):
```python
result = 10 // 3
print(result)        # 3 (drops decimal part)
print(type(result))  # <class 'int'>

result = 10 // 2
print(result)        # 5 (integer)
```

### Modulo Operator (%)
Returns the remainder of division:
```python
print(10 % 3)  # 1 (10 ÷ 3 = 3 remainder 1)
print(15 % 4)  # 3 (15 ÷ 4 = 3 remainder 3)
print(10 % 2)  # 0 (10 ÷ 2 = 5 remainder 0)
```

**Use case - Check if number is even:**
```python
number = 10
if number % 2 == 0:
    print("Even")  # Prints this!
else:
    print("Odd")
```

### Exponentiation
```python
base = 2
exponent = 3
result = base ** exponent
print(result)  # 8 (2³ = 2 × 2 × 2)
```

---

## Integer Properties

### No Size Limit in Python 3

**This is special!** In most programming languages (C, C++, Java), integers have fixed sizes:
- C's `int`: typically -2,147,483,648 to 2,147,483,647 (32 bits)
- Exceed this range → overflow error or wraparound bugs

**Python's advantage**: Arbitrary precision integers
```python
# Python can handle huge numbers!
big_number = 123456789012345678901234567890
even_bigger = big_number ** 100  # Still works!
print(big_number)  # No overflow!
```

**How it works**: Python automatically allocates more memory as needed. The integer 5 takes less memory than 5000000000000, but both work seamlessly.

**Trade-off**: Slightly slower than fixed-size integers, but much safer and easier to use. Python prioritizes **correctness** over raw speed.

**Real-world impact**: No need to worry about integer overflow bugs that have caused:
- The Y2K problem (years stored as 2 digits)
- The 2038 problem (Unix timestamps overflow)
- Financial calculation errors in other languages

### Operations with Mixed Types
```python
int_num = 10
float_num = 3.5

result = int_num + float_num
print(result)        # 13.5
print(type(result))  # <class 'float'> - becomes float!
```

**Rule**: int + float = float

---

## Practical Examples

### Example 1: Calculate Average (Integer Division)
```python
total_score = 475
num_tests = 5

average = total_score // num_tests
print(average)  # 95
```

### Example 2: Split Bill
```python
total_bill = 100
num_people = 3

per_person = total_bill // num_people
print(per_person)  # 33

remainder = total_bill % num_people
print(remainder)  # 1 (someone pays extra dollar)
```

---

## Common Use Cases

| Use Case | Example |
|----------|---------|
| Counting | `student_count = 30` |
| Ages | `age = 25` |
| Years | `year = 2024` |
| Scores | `score = 95` |
| Quantities | `apples = 10` |
| IDs | `user_id = 12345` |

---

## Key Takeaways
1. Integers are whole numbers (no decimals)
2. Use `/` for float division, `//` for integer division
3. Use `%` to get remainder
4. Integer + float = float
5. Python integers have no size limit
6. Use integers when you don't need decimal precision


---

# Implement Float Data Types

## Introduction
Floats represent numbers with decimal points, providing precision for measurements, calculations, and scientific data.

---

<div align="center">

![Python Float Object Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.4.png)

*Floats represent decimal numbers using IEEE 754 standard — essential for scientific calculations and measurements*

</div>

---

## What are Floats?

### Definition
**Float**: Number with decimal point (floating-point number)

```python
price = 19.99
height = 5.8
percentage = 87.5
pi = 3.14159
```

### Why "Floating-Point"?

The name comes from how computers store these numbers. Unlike fixed-point notation, the decimal point can "float" to different positions:

- `1.23` (decimal point after first digit)
- `123.0` (decimal point after third digit)
- `0.0123` (decimal point before digits)

Computers use **scientific notation** internally:
- `1.23 × 10²` represents 123.0
- `1.23 × 10⁻²` represents 0.0123

This allows floats to represent both very large (3.4 × 10³⁸) and very small (1.0 × 10⁻³⁸) numbers in limited memory.

### Real-World Analogy

Think of floats like a **measuring tape**:
- You can measure 5 feet, 5.5 feet, 5.75 feet
- You can be precise, but not infinitely precise
- There's always a smallest unit you can measure

Integers are like **counting marbles**:
- You can only count whole marbles: 1, 2, 3...
- No "half a marble"

### Always Has Decimal Point
```python
x = 5.0   # Float (has decimal)
y = 5     # Integer (no decimal)

print(type(x))  # <class 'float'>
print(type(y))  # <class 'int'>
```

---

## Float Arithmetic

### Basic Operations
```python
a = 10.5
b = 2.5

print(a + b)  # 13.0
print(a - b)  # 8.0
print(a * b)  # 26.25
print(a / b)  # 4.2
```

### Division Always Returns Float
```python
result = 10 / 2
print(result)        # 5.0
print(type(result))  # <class 'float'>
```

---

## Precision Limitations

### The 0.1 + 0.2 Problem
```python
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3!)
```

**Why?** Computers store numbers in binary. Some decimals can't be represented exactly.

### Understanding the Problem

Think about representing 1/3 in decimal:
- 1/3 = 0.3333333... (infinite)
- We must round: 0.33 or 0.333 or 0.3333

The same happens in binary! In base-10, we can exactly represent 0.1, but in base-2 (binary):
- 0.1 (decimal) = 0.0001100110011001... (binary, repeating forever)

Computers have finite memory, so they must round. This tiny rounding error propagates through calculations.

**Historical Impact**: Float precision errors have caused:
- The Patriot missile failure (1991) - clock drift killed 28 people
- Ariane 5 rocket explosion (1996) - $370 million lost
- Vancouver Stock Exchange index error (1982) - accumulated rounding errors

For financial calculations, use Python's `decimal` module for exact decimal arithmetic.

### Practical Impact
```python
# Be careful with equality checks
if 0.1 + 0.2 == 0.3:
    print("Equal")
else:
    print("Not equal")  # This prints!
```

### Solution: Round for Display
```python
result = 0.1 + 0.2
print(round(result, 2))  # 0.3
```

---

## Mixed Type Arithmetic

### Int + Float = Float
```python
int_num = 10
float_num = 3.5

result = int_num + float_num
print(result)        # 13.5
print(type(result))  # <class 'float'>
```

---

## Common Use Cases
- Prices: `$19.99`
- Measurements: `5.8 feet`
- Percentages: `87.5%`
- Scientific: `3.14159`
- Temperatures: `98.6°F`

## Key Takeaways
1. Floats have decimal points
2. All division returns floats
3. Precision isn't perfect (binary representation)
4. Use for measurements, prices, percentages
5. Int + float = float


---

# Implement String Data Types

## Introduction
Strings represent text data in Python. They're one of the most commonly used data types.

---

<div align="center">

![Python String Character Indexing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.5.png)

*Strings are immutable sequences of characters — Python provides rich methods for slicing, searching, and transforming text*

</div>

---

## Understanding Strings

### Why "String"?

The term "string" comes from "string of characters" - imagine beads on a string, where each bead is a character. A string is a **sequence** of characters strung together:

"Hello" = ['H', 'e', 'l', 'l', 'o']

### From Numbers to Text

Remember: computers only understand numbers (binary). So how do they store text?

Each character is assigned a number:
- 'A' = 65
- 'B' = 66
- 'a' = 97
- '!' = 33

This mapping is called **character encoding**:
- **ASCII** (1960s): 128 characters - English letters, digits, symbols
- **Unicode** (1991): 1 million+ characters - emoji, Chinese, Arabic, math symbols 😊

Python 3 uses Unicode by default - that's why you can write: `message = "Hello 世界 🌍"`

### Strings Are Immutable

**Important concept**: Once created, strings cannot be changed. Every "modification" creates a **new** string:

```python
name = "Alice"
name = name.upper()  # Creates new string "ALICE"
# The original "Alice" is discarded
```

Think of strings like **printed words on paper** - you can't erase and change them, you must print a new paper.

**Why immutable?**
- **Safety**: No accidental changes
- **Efficiency**: Same string can be reused in memory
- **Hashable**: Can be used as dictionary keys (you'll learn later)

### Real-World Analogy

A string is like a **text message**:
- Made up of individual characters (letters, numbers, spaces, emojis)
- Has a specific order (sequence matters!)
- Once sent, you can't edit it - only send a new message

## Creating Strings

### Using Quotes
```python
# Single quotes
name = 'Alice'

# Double quotes
message = "Hello, World!"

# Both work the same!
```

### Quotes Inside Strings
```python
# Use opposite quote type
text1 = "He said, 'Hello!'"
text2 = 'She said, "Hi!"'

# Or escape with backslash
text3 = "He said, \"Hello!\""
```

### Multi-line Strings
```python
long_text = """This is a
multi-line string that
spans several lines."""
```

---

## String Operations

### Concatenation (+)
```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # "Hello World"
```

**Can't mix strings and numbers**:
```python
age = 25
# message = "Age: " + age  # ❌ Error!
message = "Age: " + str(age)  # ✅ Works!
```

### Repetition (*)
```python
laugh = "ha" * 3
print(laugh)  # "hahaha"

line = "=" * 20
print(line)  # "===================="
```

### Length
```python
name = "Alice"
length = len(name)
print(length)  # 5
```

---

## String Methods

### Upper and Lower Case
```python
name = "Alice"
print(name.upper())  # "ALICE"
print(name.lower())  # "alice"
```

### Strip Whitespace
```python
text = "  hello  "
print(text.strip())  # "hello"
```

### Replace
```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # "Hello Python"
```

### Check Contents
```python
email = "user@example.com"
print(email.startswith("user"))  # True
print(email.endswith(".com"))    # True
print("@" in email)              # True
```

---

## Practical Examples

### Example 1: Full Name
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)  # "Alice Johnson"
```

### Example 2: Email Creation
```python
username = "alice"
domain = "example.com"
email = username + "@" + domain
print(email)  # "alice@example.com"
```

---

## Key Takeaways
1. Strings are text in quotes
2. Use `+` to concatenate
3. Use `*` to repeat
4. Can't directly mix strings and numbers
5. Many useful string methods available
6. Use `len()` to get length


---

# Implement Boolean Data Types

## What are Booleans?

**Boolean**: Data type with two values - `True` or `False`

```python
is_active = True
is_logged_in = False
game_over = False
```

---

<div align="center">

![Python Boolean True False Values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.6.jpg)

*Booleans (True/False) are the foundation of logic — used in conditions, comparisons, and control flow*

</div>

---

### The Foundation of Computing

Booleans are named after **George Boole** (1815-1864), an English mathematician who invented Boolean algebra - the mathematics of True and False.

**Why this matters**: Boolean algebra is the **foundation of all digital computing**.

At the hardware level, computers are made of billions of **transistors** - tiny switches that are either:
- **ON** (electricity flowing) = True = 1
- **OFF** (no electricity) = False = 0

Everything your computer does - from displaying this text to running games - reduces to billions of True/False decisions happening billions of times per second.

**Historical Impact**: Without Boolean algebra:
- No computers, smartphones, or internet
- No digital logic gates (AND, OR, NOT)
- No programming languages

### Why Only Two Values?

Other data types have many values:
- Integers: ..., -2, -1, 0, 1, 2, ...
- Strings: infinite possibilities

Booleans have just **two** values because they represent **binary decisions**:
- Is the door open? Yes or No
- Is the user logged in? True or False
- Did the payment succeed? Success or Failure

This simplicity is powerful - it mirrors how we make decisions.

### Real-World Analogy

Think of booleans like **light switches**:
- A switch has two states: ON or OFF
- You can't have a switch "half on"
- Multiple switches control different lights (multiple boolean variables)

Or think of **yes/no questions**:
- "Are you a student?" → True or False
- "Is it raining?" → True or False
- "Have you eaten?" → True or False

## Creating Booleans
```python
# Direct assignment
is_student = True
has_permission = False

# From comparisons (preview of LO-13)
age = 20
is_adult = age >= 18  # True
```

## Boolean Usage

### In Conditions
```python
is_raining = True

if is_raining:
    print("Bring umbrella!")
```

### Storing State
```python
is_game_over = False

while not is_game_over:
    # Game logic
    pass
```

## Naming Convention
Boolean variables should sound like yes/no questions:
```python
is_active = True       # "Is it active?"
has_data = False       # "Has data?"
can_proceed = True     # "Can proceed?"
should_save = False    # "Should save?"
```

## Key Takeaways
1. Only two values: True/False
2. Must be capitalized
3. Used for yes/no logic
4. Name as questions
5. Essential for control flow


---

# Inspecting Data Types Using type()

## Introduction

Python is **dynamically typed** - you don't declare types explicitly. The `type()` function lets you inspect what type a variable currently holds, which is essential for understanding and debugging code.

---

<div align="center">

![Python type() Function Dynamic Typing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.7.jpg)

*type() reveals where a value sits in Python's type hierarchy — int, float, str, bool, list, dict, and more*

</div>

---

## Understanding type()

### Basic Usage

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>

is_active = True
print(type(is_active))  # <class 'bool'>
```

### What Does `<class 'int'>` Mean?

The output `<class 'int'>` tells us:
- This value belongs to the **class** (type) called `int`
- In Python, types are implemented as classes
- You'll learn more about classes later in OOP

For now, just recognize the type name: `int`, `str`, `float`, `bool`

---

## Why Type Inspection Matters

### Python's Dynamic Typing

Unlike languages like C or Java, Python doesn't require type declarations:

```python
# Python - types are inferred
x = 5        # Python knows it's an int
x = "hello"  # Now x is a string - type changed!

# Java - types must be declared
int x = 5;
x = "hello";  // ❌ Error! Can't assign string to int variable
```

**Advantage**: Faster to write, more flexible
**Challenge**: Sometimes you're not sure what type a variable is

The `type()` function solves this challenge.

### Real-World Analogy

Think of `type()` like a **label reader**:
- You find an unlabeled box in storage
- You use a label reader to scan it
- It tells you: "This is a box of tools" vs "This is a box of toys"

Similarly, `type()` tells you what kind of data a variable contains.

---

## Practical Examples

### Example 1: Debugging Type Errors

```python
age = "25"  # Accidentally a string!
bonus = age + 5  # ❌ TypeError

# Use type() to debug
print(type(age))    # <class 'str'> - Aha! Should be int
print(type(bonus))  # Won't run due to error

# Fix it
age = int(age)  # Convert to integer
print(type(age))  # <class 'int'> ✓
bonus = age + 5   # Now works!
```

### Example 2: Understanding Function Results

```python
result = 10 / 3
print(result)        # 3.3333...
print(type(result))  # <class 'float'> - division returns float

result = 10 // 3
print(result)        # 3
print(type(result))  # <class 'int'> - floor division returns int
```

# Must convert before arithmetic
age = int(user_input)
print(type(age))  # <class 'int'> - now it's a number

---

## Dynamic Typing: A Double-Edged Sword

### Flexibility

```python
x = 5          # x is an int
x = "hello"    # Now x is a string
x = [1, 2, 3]  # Now x is a list
# Python doesn't care - types can change
```

This flexibility is powerful but can lead to bugs:

```python
def calculate_total(price, quantity):
    return price * quantity

# Works as expected
total = calculate_total(10, 3)  # 30

# Unexpected behavior!
total = calculate_total(10, "3")  # "10101010101010" (repeats string 10 times!)
```

The `type()` function helps catch these issues.

---

## When to Use type()

| Scenario | Example |
|----------|---------|
| **Debugging errors** | Figure out why operations fail |
| **Learning code** | Understand what a function returns |
| **Validation** | Check if user input is the right type |
| **Testing** | Verify function output types |
| **Exploration** | Experiment with new Python features |

---

## Comparison with isinstance()

**Advanced note**: Python also has `isinstance()` for type checking:

```python
age = 25

# Using type()
print(type(age) == int)  # True

# Using isinstance() - preferred for checking
print(isinstance(age, int))  # True
```

`isinstance()` is generally better for type checking, but `type()` is great for inspection and learning.

---

## Key Takeaways

1. **type() reveals data types** - essential in dynamically typed Python
2. **Returns class object** - `<class 'int'>`, `<class 'str'>`, etc.
3. **Helps debug type errors** - find where types don't match expectations
4. **Types can change** - variables can be reassigned to different types
5. **Use for learning** - explore what functions return and how operations work

---

## Why Dynamic Typing Matters

**Python's philosophy**: "We're all consenting adults here"

Python trusts you to manage types correctly, rather than enforcing strict type declarations like C++ or Java. This makes Python:
- **Faster to write**: No boilerplate type declarations
- **More flexible**: Same function can work with multiple types
- **More forgiving**: Easier for beginners

But with great power comes great responsibility - use `type()` to verify your assumptions!


---

# Perform Arithmetic Operations

## Introduction
Python provides comprehensive arithmetic operators for all types of calculations, from basic math to complex scientific formulas.

---

<div align="center">

![Python Arithmetic Operations Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.11.png)

*Python's arithmetic operators (+, -, *, /, //, %, **) map directly to fundamental mathematical operations*

</div>

---

### Why Arithmetic Operators Are Fundamental

At its core, a computer is a **mathematical machine**. The word "computer" literally means "one who computes." Before electronic computers, "computers" were people who performed calculations!

**Historical perspective**:
- **1940s**: First electronic computers were built to calculate artillery tables and break codes
- **1950s**: FORTRAN (FORmula TRANslation) was created specifically for scientific calculations
- **Today**: Every app uses arithmetic - from social media (likes + 1) to games (damage calculations) to finance

Even tasks that don't seem mathematical involve arithmetic:
- **Text processing**: Character positions, string lengths
- **Graphics**: Pixel coordinates, color values
- **Networks**: Packet sizes, transfer speeds
- **Time**: Unix timestamps are numbers representing seconds since 1970

### Operators as Functions

In mathematics and computer science, operators are just **special syntax for functions**:

```python
# These are equivalent:
result = 5 + 3        # Operator syntax
result = add(5, 3)    # Function syntax (if 'add' existed)
```

**Why use operators instead of functions?**
- **Readability**: `a + b` is clearer than `add(a, b)`
- **Familiarity**: Matches mathematical notation
- **Conciseness**: Less typing, easier to scan

This is called **operator overloading** or **syntactic sugar** - making code sweeter (easier) to write and read.

### Real-World Analogy

Think of arithmetic operators like **tools in a toolbox**:
- **Addition (+)**: Like combining piles - put two piles together
- **Subtraction (-)**: Like removing items - take some away
- **Multiplication (*)**: Like repeated addition - "3 bags of 5 apples = 15 apples"
- **Division (/)**: Like splitting equally - "share 12 cookies among 4 people"
- **Modulo (%)**: Like the remainder when dividing - "13 cookies, 5 people, 3 left over"
- **Exponentiation (**)**: Like repeated multiplication - "2³ = 2×2×2"

Each tool has its specific purpose, and you choose the right one for the job.

---

## Basic Arithmetic Operators

### Addition (+)
```python
a = 10
b = 5
sum_result = a + b
print(sum_result)  # 15
```

**With different types**:
```python
int_num = 10
float_num = 3.5
result = int_num + float_num
print(result)  # 13.5 (becomes float)
```

### Subtraction (-)
```python
a = 10
b = 3
difference = a - b
print(difference)  # 7
```

**Can produce negatives**:
```python
result = 5 - 10
print(result)  # -5
```

### Multiplication (*)
```python
price = 19.99
quantity = 3
total = price * quantity
print(total)  # 59.97
```

**String repetition** (bonus):
```python
text = "Hello" * 3
print(text)  # "HelloHelloHello"
```

### Division (/)

**Always returns float**:
```python
result = 10 / 2
print(result)        # 5.0 (float, not 5)
print(type(result))  # <class 'float'>

result = 10 / 3
print(result)        # 3.3333333...
```

---

## Special Arithmetic Operators

### Why Python Has Two Division Operators

Most languages have just one division operator, but Python 3 has two: `/` and `//`. This was a deliberate design choice.

**The problem**: In Python 2 and many other languages, `/` behaved differently with ints vs floats:
```python
# Python 2 behavior (confusing!)
10 / 3    # → 3 (integer division)
10.0 / 3  # → 3.333... (float division)
```

This caused countless bugs when programmers forgot about integer division.

**Python 3's solution**: Make division behavior explicit:
- `/` **always** returns float (predictable)
- `//` **always** returns integer (when you need it)

This is Python's philosophy: "Explicit is better than implicit."

### Integer Division (//)

Returns integer, discarding remainder:
```python
result = 10 // 3
print(result)  # 3 (not 3.333...)

result = 15 // 4
print(result)  # 3

result = 20 // 5
print(result)  # 4
```

**With negatives**:
```python
result = -10 // 3
print(result)  # -4 (floors toward negative infinity)
```

### Modulo (%)

Returns remainder after division:
```python
print(10 % 3)   # 1 (10 = 3×3 + 1)
print(15 % 4)   # 3 (15 = 4×3 + 3)
print(20 % 5)   # 0 (20 = 5×4 + 0, no remainder)
```

**Practical use - Check even/odd**:
```python
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Get last digit**:
```python
number = 12345
last_digit = number % 10
print(last_digit)  # 5
```

### Exponentiation (**)

Raises number to a power:
```python
result = 2 ** 3
print(result)  # 8 (2³ = 2 × 2 × 2)

result = 5 ** 2
print(result)  # 25 (5²)

result = 10 ** 0
print(result)  # 1 (anything⁰ = 1)
```

**Square roots** (using fractional exponent):
```python
result = 16 ** 0.5
print(result)  # 4.0 (√16)
```

---

## Augmented Assignment Operators

Shortcuts for updating variables:

### Basic Augmented Operators

```python
x = 10

# Long way
x = x + 5
print(x)  # 15

# Short way (augmented assignment)
x += 5
print(x)  # 20
```

### All Augmented Operators

```python
score = 100

score += 50   # score = score + 50 → 150
score -= 25   # score = score - 25 → 125
score *= 2    # score = score * 2 → 250
score //= 10  # score = score // 10 → 25
score %= 7    # score = score % 7 → 4
score **= 2   # score = score ** 2 → 16
```

### When to Use Augmented Assignment

```python
# Updating game score
player_score = 0
player_score += 100  # Completed level
player_score += 50   # Bonus points
player_score -= 20   # Penalty

# Doubling a value
money = 100
money *= 2  # Now have 200

# Halving a value
portions = 8
portions //= 2  # Now have 4
```

---

## Practical Examples

### Example 1: Simple Calculator
```python
num1 = 15
num2 = 4

print(f"Sum: {num1 + num2}")           # 19
print(f"Difference: {num1 - num2}")    # 11
print(f"Product: {num1 * num2}")       # 60
print(f"Division: {num1 / num2}")      # 3.75
print(f"Integer Div: {num1 // num2}")  # 3
print(f"Remainder: {num1 % num2}")     # 3
print(f"Power: {num1 ** 2}")           # 225
```

### Example 2: Temperature Conversion
```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")  # 25°C = 77.0°F
```

---

## Operator Summary Table

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.666...` |
| `//` | Integer Division | `5 // 3` | `1` |
| `%` | Modulo | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

---

## Key Takeaways

1. **Seven arithmetic operators**: +, -, *, /, //, %, **
2. **Division** (`/`) always returns float
3. **Integer division** (`//`) returns integer, drops decimal
4. **Modulo** (`%`) returns remainder
5. **Exponentiation** (`**`) calculates powers
6. **Augmented assignment** (+=, -=, etc.) updates variables efficiently
7. **Mixed types** (int + float) return float
8. **Order matters** (we'll learn precedence in LO-12)

---

## Practice Exercises

Try these calculations:
```python
# Exercise 1: Calculate circle area
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"Area: {area}")

# Exercise 2: Convert hours to seconds
hours = 2
minutes = hours * 60
seconds = minutes * 60
print(f"{hours} hours = {seconds} seconds")

# Exercise 3: Check if number is even
number = 42
is_even = (number % 2 == 0)
print(f"{number} is even: {is_even}")
```


---

# Apply Operator Precedence

## Introduction

Operator precedence determines **which operations happen first** in complex expressions. Without these rules, `2 + 3 * 4` could mean either 20 or 14 - ambiguous and chaos!

---

---

<div align="center">

<div style="overflow: hidden; display: inline-block;">
  <img src="https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.12.jpg" 
       style="margin-right: -120px; display: block;" 
       alt="Python Operator Precedence Table">
</div>

*Python follows PEMDAS/BODMAS rules: Parentheses → Exponents → Multiplication/Division → Addition/Subtraction*

</div>

---

---

### Why Precedence Rules Exist

**The problem**: Expressions can be read multiple ways
- `2 + 3 * 4` could be `(2 + 3) * 4 = 20` or `2 + (3 * 4) = 14`

**The solution**: Universal rules everyone follows

**Historical note**: These rules come from mathematics, standardized over centuries. When programming languages were invented in the 1950s, they adopted mathematical conventions so formulas would work the same way in code as on paper.

### Real-World Analogy

Think of precedence like **grammar rules** in language:
- "I saw a man with a telescope" - Who has the telescope? Grammar rules help clarify.
- Similarly, operator precedence clarifies: "2 + 3 × 4" - Math rules say multiply first

Or think of it like **traffic rules**:
- At an intersection, who goes first? Traffic rules provide the answer (stop signs, right-of-way)
- In expressions, what happens first? Precedence rules provide the answer

### The Origin of PEMDAS

**PEMDAS** is a mnemonic (memory aid) taught in schools:
- **P**arentheses
- **E**xponents
- **M**ultiplication/**D**ivision
- **A**ddition/**S**ubtraction

This order reflects mathematical convention developed over 400+ years to avoid ambiguity.

## Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):

1. **Parentheses** `()`
2. **Exponentiation** `**`
3. **Multiplication, Division** `*`, `/`, `//`, `%` (left to right)
4. **Addition, Subtraction** `+`, `-` (left to right)

## Examples

```python
# Multiplication before addition
result = 2 + 3 * 4
# Evaluates as: 2 + (3 * 4) = 2 + 12 = 14

# Force different order with parentheses
result = (2 + 3) * 4
# Evaluates as: 5 * 4 = 20

# Complex expression
result = 10 + 5 * 2 - 3
# Step 1: 5 * 2 = 10
# Step 2: 10 + 10 = 20
# Step 3: 20 - 3 = 17

# With exponentiation
result = 2 + 3 ** 2 * 4
# Step 1: 3 ** 2 = 9
# Step 2: 9 * 4 = 36
# Step 3: 2 + 36 = 38
```

## Best Practice

**Use parentheses for clarity**, even when not required:

```python
# Harder to read
total = price * quantity + tax

# Clearer intent
total = (price * quantity) + tax
```

## Key Takeaways
1. Follow PEMDAS
2. Use parentheses to override
3. When unsure, add parentheses
4. Left-to-right for same precedence


---

# Use Comparison Operators

## Introduction

Comparison operators are the foundation of **decision-making** in programs. They allow code to ask questions and respond differently based on the answers.

---

<div align="center">

![Python Comparison Operators Table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.13.png)

*Comparison operators evaluate to True or False, enabling programs to branch into different execution paths*

</div>

---

### Why Comparison Operators Exist

Every useful program makes decisions:
- **ATM**: Is PIN correct? Is balance sufficient?
- **Game**: Is health > 0? Did score >= high score?
- **Login**: Does password match? Is account active?

Without comparisons, programs would just execute the same instructions every time - no intelligence, no adaptation.

### The Foundation of Logic

Comparison operators implement **Boolean logic**, invented by George Boole in the 1800s. This mathematical system deals with truth values (True/False) and forms the basis of:
- All computer logic gates
- Database queries (SQL WHERE clauses)
- Conditional statements in every programming language
- Search engine filters

### Real-World Analogy

Comparison operators are like **quality control inspectors**:
- Inspector checks: "Is this item > 5 inches?" → True or False
- Inspector checks: "Does weight == specification?" → True or False
- Based on answer, item passes or fails

Or think of them like **bouncers at a club**:
- "Is age >= 21?" → True: enter, False: denied
- "Is name on list?" → True: VIP entrance, False: regular line

## Comparison Operators

Comparison operators compare two values and return a **boolean** result: `True` or `False`.

### The Six Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

## Examples

### Equal To (`==`)

```python
age = 18
print(age == 18)  # True
print(age == 20)  # False

name = "Alice"
print(name == "Alice")  # True
print(name == "Bob")    # False
```

**Common Mistake**: Using `=` instead of `==`
```python
# Wrong - This assigns 18 to age
if age = 18:  # SyntaxError!

# Correct - This checks if age equals 18
if age == 18:  # Correct!
```

### Not Equal To (`!=`)

```python
status = "pending"
print(status != "completed")  # True
print(status != "pending")    # False
```

### Greater Than (`>`)

```python
score = 85
print(score > 75)   # True
print(score > 90)   # False
print(score > 85)   # False (not greater, equal!)
```

### Less Than (`<`)

```python
temperature = 25
print(temperature < 30)  # True
print(temperature < 20)  # False
print(temperature < 25)  # False (not less, equal!)
```

### Greater Than or Equal To (`>=`)

```python
age = 18
print(age >= 18)  # True (equal counts!)
print(age >= 16)  # True
print(age >= 21)  # False
```

### Less Than or Equal To (`<=`)

```python
attempts = 3
print(attempts <= 3)  # True (equal counts!)
print(attempts <= 5)  # True
print(attempts <= 2)  # False
```

## Comparing Different Data Types

### Numbers

```python
# Comparing integers and floats works
print(5 == 5.0)      # True
print(10 > 9.5)      # True
print(3.14 <= 3.14)  # True
```

### Strings

```python
# Strings are compared alphabetically
print("apple" < "banana")   # True
print("zebra" > "aardvark") # True
print("ABC" == "abc")       # False (case-sensitive!)
```

### Type Incompatibility

```python
# Can't meaningfully compare different types
print(5 == "5")      # False (different types!)
print(10 < "20")     # TypeError in Python 3
```

## Storing Comparison Results

```python
# Comparisons return boolean values
age = 20
is_adult = age >= 18
print(is_adult)        # True
print(type(is_adult))  # <class 'bool'>

# Can use in conditions
temperature = 35
is_hot = temperature > 30
print(f"Is it hot? {is_hot}")  # Is it hot? True
```

## Real-World Applications

### Age Verification

```python
age = int(input("Enter your age: "))
can_vote = age >= 18
can_drive = age >= 16

print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
```

### Grade Checker

```python
score = 85
is_passing = score >= 60
is_excellent = score >= 90

print(f"Passing: {is_passing}")    # True
print(f"Excellent: {is_excellent}")  # False
```

### Password Validation

```python
password = input("Enter password: ")
min_length = len(password) >= 8
print(f"Password long enough: {min_length}")
```

### Temperature Alert

```python
temperature = 38
is_fever = temperature >= 37.5
print(f"Has fever: {is_fever}")  # True
```

## Common Mistakes

### Using `=` Instead of `==`

```python
# Wrong
x = 5
if x = 5:  # SyntaxError
    print("Five")

# Correct
if x == 5:
    print("Five")
```

### Forgetting Type Matters

```python
user_input = input("Enter age: ")  # Returns string!
# user_input = "18" (string)

# Wrong comparison
if user_input >= 18:  # TypeError!

# Correct - convert first
age = int(user_input)
if age >= 18:
    print("Adult")
```

### Confusing `>` and `>=`

```python
score = 60
# Be clear about boundaries
print(score > 60)   # False
print(score >= 60)  # True
```

## Practice Exercise

Try to predict the output:

```python
a = 10
b = 20
c = 10

print(a == c)    # ?
print(a != b)    # ?
print(b > a)     # ?
print(a >= c)    # ?
print(b <= 15)   # ?
```

<details>
<summary>Answer</summary>

```python
print(a == c)    # True
print(a != b)    # True
print(b > a)     # True
print(a >= c)    # True
print(b <= 15)   # False
```
</details>

## Key Takeaways

1. **Six operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
2. **Return boolean**: All comparisons return `True` or `False`
3. **Type-aware**: Compare compatible types
4. **Not assignment**: `==` checks equality, `=` assigns
5. **Store results**: Can save comparison results in variables


---

