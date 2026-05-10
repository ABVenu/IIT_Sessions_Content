### Define Variables (20 minutes)


### CS Theory Bite

> **Origin**: Variables trace back to **John von Neumann's stored-program architecture** (1945) — the idea that data and instructions live in the same memory, accessed by named addresses.
>
> **Analogy**: A variable is like a **labeled jar in a kitchen** — the label says what's inside, and you can swap the contents anytime without changing the label.
>
> **Why it matters**: Every program manipulates data through variables — they're the foundation of all computation.


### Hook (2 minutes)

**Say**: "Imagine playing a video game. The game needs to remember your score, your character's name, your health - all while you're playing. How does it do that? With variables! Today you'll learn how to make Python remember information."

```python
score = 0
score = score + 100
print(score)  # 100
```

### What are Variables (6 minutes)

**Say**: "A variable is like a labeled box. The label is the variable name, and you put data inside the box."

```python
# Create a variable
age = 25
print(age)  # 25

name = "Alice"
print(name)  # Alice

score = 100
print(score)  # 100
```

**Key Points**:
- Variable name on LEFT, value on RIGHT
- Use `=` to assign (not "equals" like math)
- Read as "age is assigned 25"

### Variable Reassignment (6 minutes)

**Say**: "Unlike math where x = 5 is permanent, in programming variables can change. They're called VARIables because they VARY!"

```python
health = 100
print(health)  # 100

health = 75   # Player took damage!
print(health)  # 75

health = 100  # Player healed!
print(health)  # 100
```

### Student Exercise (4 minutes)

**Say**: "Your turn! Create a variable called `money` with value 100. Then add 50 to it. Then subtract 30. Print it after each step."

```python
# Your code here
money = 100
print(money)

# Add 50

# Subtract 30
```

### Wrap-up (2 minutes)



---

### Apply Variable Naming Conventions (15 minutes)


### CS Theory Bite

> **Origin**: **PEP 8** was written by Guido van Rossum in 2001, codifying Python's philosophy: **"Readability counts"** (Zen of Python).
>
> **Analogy**: Naming conventions are like **road signs** — consistent formatting means everyone navigates the code without confusion.
>
> **Why it matters**: You read code 10x more than you write it — good names save hours of debugging.


### Hook (2 minutes)

**Say**: "You can name variables almost anything... but should you? Let's learn the rules and best practices!"

```python
x = 10      # Valid but unclear
age = 10    # Valid and clear!
```

### Naming Rules (5 minutes)

**Key Rules**:
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Cannot use Python keywords (if, for, while, etc.)
- Case-sensitive (Age ≠ age)

```python
# Valid
student_name = "Alice"
_private = 42
age2 = 25

# Invalid
2students = 10      # Error!
student-name = "Bob" # Error!
for = 5              # Error! (keyword)
```

### PEP 8 Conventions (6 minutes)

**Say**: "Python has style guidelines called PEP 8. Follow them to write professional code!"

**Best Practices**:
- Use `snake_case` for variables (all lowercase, underscores)
- Make names descriptive
- Avoid single letters except in loops

```python
# Good - follows PEP 8
student_name = "Alice"
total_score = 95
is_active = True

# Bad - works but not Pythonic
studentName = "Bob"   # camelCase (not Python style)
TotalScore = 85       # PascalCase (for classes)
x = True              # too vague
```

**Real-World**: Professional Python projects follow PEP 8. Learn it now!

### Practice (2 minutes)

Fix these names to follow PEP 8:
```python
StudentName = "Alice"  # Change to: student_name
totalPrice = 99.99     # Change to: total_price
2ndPlace = "Bob"       # Change to: second_place
```


---

### Implement Integer Data Types (16 minutes)


### CS Theory Bite

> **Origin**: Integers in computers use **binary representation**, dating back to **ENIAC** (1945). Python integers have **unlimited precision** — unlike C/Java's fixed 32/64-bit limits.
>
> **Analogy**: An integer is like a **counting abacus** — whole numbers only, no fractions, but Python's abacus has infinite beads.
>
> **Why it matters**: Integers are the most fundamental data type — counters, indices, IDs all use them.


### Hook (3 minutes)

**Say**: "What's 10 divided by 3? In math, it's 3.333... But what if you're splitting 10 cookies among 3 people? You can't split a cookie! That's where integer division comes in."

```python
cookies = 10
people = 3
each_gets = 10 // 3  # 3 cookies each
```

### What are Integers (5 minutes)

**Say**: "Integers are whole numbers - no decimals. They can be positive, negative, or zero."

```python
age = 25
year = 2024
count = 0
temperature = -5

print(type(age))  # <class 'int'>
```

**Key Points**:
- Integers have no decimal point
- Can be any size (Python handles big numbers!)
- Used for counting, indexing, IDs

### Integer Operations (5 minutes)

**Say**: "Python has two types of division - regular (/) gives decimals, floor (//) gives integers."

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (float!)
print(a // b)  # 3 (integer division)
print(a % b)   # 1 (remainder - modulo)
```

**Real-World**: Modulo (%) checks if number is even/odd!
```python
if num % 2 == 0:
    print("Even")
```

### Practice (3 minutes)

```python
candies = 25
friends = 4

each_gets = candies // friends  # 6
leftover = candies % friends    # 1

print(f"Each friend gets {each_gets} candies")
print(f"{leftover} candy left over")
```



---

### Implement Float Data Types (15 minutes)


### CS Theory Bite

> **Origin**: Floating-point numbers follow the **IEEE 754 standard** (1985), which standardized how computers represent decimals. The name "floating point" means the decimal point can "float" to different positions.
>
> **Analogy**: Floats are like **scientific notation** (6.02 × 10²³) — they trade perfect precision for enormous range.
>
> **Why it matters**: Understanding float imprecision (`0.1 + 0.2 != 0.3`) prevents subtle bugs in financial and scientific code.


### Hook (2 minutes)

**Say**: "Can you buy something for exactly $19.99? Not $19 or $20 - you need decimals! That's why we have floats."

```python
price = 19.99
tax = 1.60
total = 21.59  # All floats!
```

### What are Floats (5 minutes)

**Say**: "Floats are numbers with decimal points. Used for money, measurements, scientific calculations."

```python
price = 29.99
height = 5.8
pi = 3.14159

print(type(price))  # <class 'float'>
```

**Key Points**:
- Floats have decimal points
- Can be positive or negative
- Used when precision matters
- Division always returns float

```python
result = 10 / 2  # 5.0 (not 5)
print(type(result))  # <class 'float'>
```

### Float Precision (5 minutes)

**Say**: "Computers can't perfectly represent all decimals. This leads to small errors."

```python
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3!)
```

**Solution - Round when displaying**:
```python
result = 0.1 + 0.2
print(f"{result:.2f}")  # 0.30
```

**Real-World**: Always round currency to 2 decimals for display!

### Practice (3 minutes)

Calculate total with tax:
```python
price = 29.99
tax_rate = 0.08
tax = price * tax_rate
total = price + tax
print(f"Total: ${total:.2f}")  # Total: $32.39
```


---

### Implement String Data Types (21 minutes)


### CS Theory Bite

> **Origin**: Text encoding evolved from **ASCII** (1963, 128 characters) to **Unicode** (1991, 150K+ characters). Python 3 strings are Unicode by default — supporting every human language.
>
> **Analogy**: A string is like a **necklace of letter beads** — each character is one bead, and you can slice, count, or rearrange them.
>
> **Why it matters**: Strings are everywhere — user input, file content, API responses, database records all flow as text.


### Hook (3 minutes)

**Say**: "Every app you use has text - usernames, messages, posts. In Python, that's all strings!"

```python
username = "alice_2024"
message = "Hello World!"
email = "user@example.com"
```

### String Basics (6 minutes)

**Say**: "Strings are text in quotes. Use single or double quotes - both work the same!"

```python
name = "Alice"
city = 'New York'
message = "Hello World"

print(type(name))  # <class 'str'>
```

**Key Points**:
- Strings can use "" or ''
- Must match opening and closing quotes
- Use quotes inside strings: "She said 'Hi'"

**String Concatenation**:
```python
first = "John"
last = "Doe"
full_name = first + " " + last  # John Doe
```

### String Methods (6 minutes)

**Say**: "Strings have built-in methods to modify and check text. These are super useful for data cleaning!"

```python
name = "alice"
print(name.upper())      # ALICE
print(name.capitalize()) # Alice
print(name.title())      # Alice

text = "  hello  "
print(text.strip())      # hello (removes spaces)

email = "USER@EXAMPLE.COM"
print(email.lower())     # user@example.com
```

**Real-World**: Always lowercase emails before saving to database!

### Practice (6 minutes)

**Say**: "Let's build an email address from parts."

```python
first = "john"
last = "doe"
domain = "example.com"

# Solution
email = first + "." + last + "@" + domain
print(email)  # john.doe@example.com

# Better way with f-string
email = f"{first}.{last}@{domain}"
print(email)
```



---

### Implement Boolean Data Types (15 minutes)


### CS Theory Bite

> **Origin**: Named after mathematician **George Boole** (1854), who formalized logic into algebra. Every `if` statement, every `while` loop ultimately depends on Boolean values.
>
> **Analogy**: Booleans are like a **light switch** — only two states: ON (True) or OFF (False). No dimmer, no maybe.
>
> **Why it matters**: All program decisions reduce to True/False — booleans are the atoms of control flow.


### Hook (3 minutes)

**Say**: "Is the light on or off? Is the door open or closed? Life is full of yes/no questions - that's what booleans are for!"

```python
is_logged_in = True
has_permission = False
```

### Boolean Basics (6 minutes)

**Say**: "Booleans have only two values: True and False. Notice the capital letters - Python is picky!"

```python
is_raining = True
is_weekend = False

print(type(is_raining))  # <class 'bool'>
```

**Key Points**:
- Only two values: `True` and `False`
- Must be capitalized (true/false won't work!)
- Used for conditions and logic
- Result of comparisons are booleans

```python
age = 20
is_adult = age >= 18  # True (comparison result)
print(is_adult)  # True
```

**Real-World**: Every login system uses booleans - is user authenticated? Does user have admin rights?

### Boolean in Conditionals (4 minutes)

**Say**: "Booleans power if statements. They decide which code runs."

```python
is_member = True

if is_member:
    print("Welcome back!")
else:
    print("Please sign up")
```

### Practice (2 minutes)

Create booleans for real scenarios:
```python
is_sunny = True
has_homework = False
is_class_over = False

# Use in condition
if is_sunny:
    print("Let's go outside!")
```


---

### Inspect Data Types (10 minutes)


### CS Theory Bite

> **Origin**: Runtime type inspection powers **dynamic typing** — Python's design choice (vs static typing in C/Java). **Duck typing**: "If it walks like a duck and quacks like a duck, it's a duck."
>
> **Analogy**: `type()` is like an **ID scanner** — it tells you exactly what kind of data you're dealing with at any moment.
>
> **Why it matters**: Debugging type errors is the #1 beginner challenge — `type()` is your diagnostic tool.


### Hook (3 minutes)

**Say**: "Python needs to know what type of data it's working with. The `type()` function lets us inspect any variable's data type."

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

### Using type() Function (4 minutes)

**Say**: "Type() returns the class/type of any value. Super useful for debugging!"

```python
# Different types
x = 42              # int
y = 3.14            # float
z = "Hello"         # str
w = True            # bool

print(type(x))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(z))      # <class 'str'>
print(type(w))      # <class 'bool'>
```

**Key Use Cases**:
- Debugging unexpected behavior
- Validating user input types
- Understanding unfamiliar code
- Preventing type-related errors

**Real-World**: When building a calculator, use `type()` to ensure users enter numbers, not text!

### Practice (3 minutes)

Check types of different values:
```python
data = input("Enter something: ")
print(f"You entered: {data}")
print(f"Type: {type(data)}")  # Always 'str' from input!

# That's why we need conversion:
age = int(input("Age: "))
print(type(age))  # Now it's 'int'
```


---

### Perform Arithmetic Operations (21 minutes)


### CS Theory Bite

> **Origin**: Arithmetic operations are performed by the **ALU** (Arithmetic Logic Unit) inside your CPU — the same circuitry since the **Intel 4004** (1971). Python adds `//` (floor division) and `**` (power) beyond basic math.
>
> **Analogy**: Python operators are like a **calculator's buttons** — each symbol triggers a specific mathematical operation in the CPU.
>
> **Why it matters**: Arithmetic is the building block of algorithms — from simple totals to complex simulations.


### Hook (3 minutes)

**Say**: "Python is a powerful calculator! But it has special operators you might not know about. Let's explore them all!"

```python
print(10 + 3)   # Addition
print(10 // 3)  # Floor division (what's this?)
print(10 % 3)   # Modulo (huh?)
```

### Basic Operators (6 minutes)

**Say**: "These are the operators you know from math class."

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division - ALWAYS returns float!)
```

**Key Points**:
- Addition (+), subtraction (-), multiplication (*) work as expected
- Division (/) ALWAYS returns a float, even if dividing evenly
- Python handles very large numbers automatically

```python
print(10 / 2)  # 5.0 (not 5!)
print(type(10 / 2))  # <class 'float'>
```

### Special Operators (6 minutes)

**Say**: "Python has two special operators for division scenarios."

**Floor Division (//)**: Drops the decimal part
```python
print(10 // 3)  # 3 (not 3.333...)
print(7 // 2)   # 3 (not 3.5)
```

**Modulo (%)**: Returns the remainder
```python
print(10 % 3)   # 1 (10 ÷ 3 = 3 remainder 1)
print(7 % 2)    # 1 (odd number!)
print(8 % 2)    # 0 (even number!)
```

**Power (**)**: Exponentiation
```python
print(2 ** 3)   # 8 (2³)
print(5 ** 2)   # 25 (5²)
```

**Real-World**: Check if a number is even/odd using modulo!
```python
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Augmented Assignment (4 minutes)

**Say**: "Shortcuts for updating variables - you'll use these ALL the time!"

```python
score = 100
score += 50   # Same as: score = score + 50
print(score)  # 150

score -= 20   # Same as: score = score - 20
print(score)  # 130

score *= 2    # Same as: score = score * 2
print(score)  # 260
```

**All augmented operators**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### Practice (2 minutes)

Calculate total with tax:
```python
price = 19.99
quantity = 3
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Total: ${total:.2f}")
```


---

### Apply Operator Precedence (16 minutes)


### CS Theory Bite

> **Origin**: Operator precedence follows **mathematical convention** (PEMDAS/BODMAS) established centuries ago in algebra. Python's precedence table has 18 levels — but parentheses always win.
>
> **Analogy**: Precedence is like a **VIP list** — multiplication gets served before addition, but parentheses are the ultimate VIP pass.
>
> **Why it matters**: Misunderstood precedence causes silent bugs — `2 + 3 * 4` is 14, not 20.


### Hook (3 minutes)

**Say**: "What's 2 + 3 × 4? If you said 20, you forgot PEMDAS! Python follows the same math rules you learned in school."

```python
print(2 + 3 * 4)    # 14 (not 20!)
print((2 + 3) * 4)  # 20 (parentheses first!)
```

### PEMDAS in Python (6 minutes)

**Say**: "Python follows PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."

**Order of operations**:
1. **P**arentheses: `()`
2. **E**xponents: `**`
3. **M**ultiplication/Division: `*`, `/`, `//`, `%` (left to right)
4. **A**ddition/Subtraction: `+`, `-` (left to right)

```python
# Exponents first, then multiplication, then addition
print(2 + 3 * 4 ** 2)  # 2 + 3 * 16 = 2 + 48 = 50

# Multiplication before addition
print(10 + 5 * 2)      # 10 + 10 = 20

# Parentheses override everything
print((10 + 5) * 2)    # 15 * 2 = 30
```

**Key Point**: When operators have same precedence (like * and /), Python evaluates left to right.

```python
print(10 / 2 * 3)  # (10 / 2) * 3 = 5 * 3 = 15
print(10 * 2 / 3)  # (10 * 2) / 3 = 20 / 3 = 6.666...
```

**Real-World**: Complex formulas need careful ordering!
```python
# Area of a circle: πr²
radius = 5
area = 3.14 * radius ** 2  # Exponent first, then multiply
print(f"Area: {area}")
```

### Using Parentheses (4 minutes)

**Say**: "When in doubt, use parentheses! They make code clearer and prevent bugs."

```python
# Calculate average - needs parentheses!
a, b, c = 10, 20, 30
average = (a + b + c) / 3  # Correct: (60) / 3 = 20
# average = a + b + c / 3  # Wrong: 10 + 20 + 10 = 40
```

**Best Practice**: Use parentheses for clarity, even when not required
```python
# Both are correct, but second is clearer
total = price + price * tax_rate
total = price + (price * tax_rate)  # Better!
```

### Practice (3 minutes)

Predict the results:
```python
print(2 ** 3 + 4)       # 8 + 4 = 12
print(10 + 5 * 2)       # 10 + 10 = 20
print((10 + 5) * 2)     # 15 * 2 = 30
print(100 - 20 * 3)     # 100 - 60 = 40
print((100 - 20) * 3)   # 80 * 3 = 240
```


---

### Use Comparison Operators (20 minutes)


### CS Theory Bite

> **Origin**: Comparison operators implement **relational algebra** from predicate logic. Python uniquely allows **chaining**: `1 < x < 10` — most languages require `1 < x and x < 10`.
>
> **Analogy**: Comparisons are like a **judge's verdict** — they examine two values and declare True or False, nothing in between.
>
> **Why it matters**: Every `if` statement and `while` loop relies on comparisons to make decisions.


### Hook (2 minutes)

**Say**: "Raise your hand if you're 18 or older. How did your brain just make that decision? You compared your age to 18! That's exactly what comparison operators do in Python."

### Introduction to Comparison Operators (6 minutes)

**Say**: "Comparison operators let Python ask questions and get True/False answers."

```python
age = 20
print(age >= 18)  # True
```

**Key Points**:
- Result is always True or False (boolean)
- We're asking: "Is age greater than or equal to 18?"

### Common Operators in Detail (4 minutes)

**Say**: "Double equals checks if two values are the same. VERY different from single equals!"

```python
# Single = assigns
age = 18

# Double == compares
print(age == 18)  # True
print(age == 20)  # False
```

### Real-World Application (3 minutes)

**Say**: "Let's build a simple age checker!"

```python
age = int(input("Enter your age: "))

can_vote = age >= 18
can_drive = age >= 16
is_child = age < 13

print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is child: {is_child}")
```

### Common Mistakes (3 minutes)

**Say**: "Let me show you the #1 mistake beginners make."

```python
x = 5
if x = 5:  # SyntaxError!
    print("Five")
```

### Practice & Wrap-up (2 minutes)

```python
a = 10
b = 10
print(a == b)
print(a > b)
print(a >= b)
```



---

