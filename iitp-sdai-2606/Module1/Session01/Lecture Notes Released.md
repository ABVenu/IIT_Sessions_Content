# Introduction to Programming & Python Basics

## What You Will Learn in This Lesson

This is your first step into the world of programming. You do not need any prior coding experience to follow along.

In this lesson, you will learn what programming really means, how to write and run your first **Python** program using a free **online compiler**, and how to store information using **variables** and **data types**. You will also learn how to do calculations with **operators**, and how to make your program talk to you using **input** and **output**.

By the end, you will be able to write small programs that ask a question, do a calculation, and show a result on the screen.

---

## What Is Programming?

- **Official Definition:** **Programming** is the process of writing step-by-step instructions that a computer can understand and execute to perform a task.
- **In Simple Words:** Programming is like giving very clear directions to a machine that never guesses — it only does exactly what you tell it.
- **Real-Life Example:** Think of programming like writing a recipe for a cook. If you write "add salt," the cook adds salt. If you forget to mention "turn on the gas," nothing gets cooked. Computers are the same — every step must be written clearly.

### Why Do We Need Programming?

- Almost everything digital around you runs on code — UPI payments, train ticket booking, WhatsApp, Netflix recommendations, and even the AI tools you will work with later in this course.
- Programming teaches you to **break big problems into small steps**, which is useful in life and in tech careers.

![Programming as a step-by-step recipe — every instruction must be clear; forget a step and the computer cannot finish the task; the same idea powers UPI, train booking, WhatsApp, and AI tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-01-programming-recipe-analogy.png)

### What Is Python?

- **Official Definition:** **Python** is a high-level, general-purpose programming language known for its simple, readable syntax.
- **In Simple Words:** Python is a language humans use to talk to computers — and it reads almost like plain English.
- **Real-Life Example:** If programming languages were languages you speak, Python is like Hindi or English — easy to start with and widely used everywhere.

- It is one of the most popular languages for **software development**, **data science**, and **AI**.
- You can start writing code in your browser on day one — no complicated installation needed.
- The syntax is beginner-friendly, so you can focus on **thinking logically** instead of fighting with complex rules like curly brackets and semicolons required in many other languages.

![Why Python for beginners — readable syntax like plain English, no install needed in the browser, and widely used in software development, data science, and AI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-02-python-beginner-language.png)

---

## Setting Up an Online Compiler

Before you can run Python code, you need a place to write it and execute it. For this course, we use a free **online compiler** — a website where you write code and see the output instantly, without installing anything on your laptop.

### What Is a Compiler?

- **Official Definition:** A **compiler** is a program that converts high-level code written by humans into low-level machine code (binary — 1s and 0s) that the computer's CPU can execute.
- **In Simple Words:** You write instructions in Python; the compiler translates them into a language the computer actually understands.
- **Real-Life Example:** Think of a compiler like a translator at a government office — you speak Hindi, the officer needs English, and the translator converts your words so the work gets done.

Without a compiler, your computer cannot run the Python code you write.

### What Is an Online Compiler?

- **Official Definition:** An **online compiler** is a web-based tool that lets you write, run, and test code directly in a browser.
- **In Simple Words:** It is like a digital notebook with a "Run" button — you type code, press Run, and the result appears on the screen.
- **Real-Life Example:** Just like you fill an online form without buying special software, an online compiler lets you write Python without installing it on your machine.

### Getting Started

In the live session, we used **[onlinecompiler.com/python](https://www.onlinecompiler.com/python)**. You can also search for "online Python compiler" in Google and pick a trusted option. **Programiz** is another good choice for your first week of practice.

Follow these steps on your laptop or desktop browser:

1. Open [onlinecompiler.com/python](https://www.onlinecompiler.com/python) (or your chosen online compiler) in Chrome or any modern browser.
2. You will see a **code editor** on one side — the main area where you type Python code.
3. Type your Python code in the editor.
4. Click **Run** to execute your code. The **output console** on the other side shows the result.
5. Over time, you may install Python on your laptop — but an online compiler is the best way to start on day one.

![OneCompiler workflow — open the online compiler, pick Python, type in the editor, click Run, and see output in the console; no installation needed on day one](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-03-onecompiler-workspace.png)

### Your First Python Program

Type the following in the online compiler and run it:

```python
# This is my very first Python program
# The print() function displays text on the screen
print("Hello, World!")  # This line prints a greeting message
```

**How the code works:**

- Lines starting with `#` are **comments** — notes for humans that Python ignores.
- `print()` is a built-in **function** that shows output on the screen. You will learn more about functions later; for now, think of `print()` as Python's way of talking back to you.
- The text in quotes is a **string** (text data).
- When you click Run, the compiler executes every line from top to bottom.

![Hello, World flow — type code, click Run, Python executes top to bottom; comments (#) are ignored, print() shows output; watch for case-sensitive print and straight quotes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-04-hello-world-flow.png)

### Comments in Python

Comments help you document your code so you (and others) can understand it later.

- **Single-line comment:** Start the line with `#`. Everything after `#` on that line is ignored by Python.
- **Multi-line comment:** Wrap the text in triple quotes (`"""` or `'''`). Python treats everything inside as a comment.

```python
# This is a single-line comment
age = 10  # You can also add a comment at the end of a line

"""
This is a multi-line comment.
You can write several lines here.
Python will ignore all of this.
"""
name = "Yash"
```

**How the code works:**

- Use `#` for short notes on one line.
- Use triple quotes when you need to explain a longer block of code without running it.

### Common Beginner Mistakes

- **Forgetting to click Run:** Typing code alone does nothing — you must press the Run button.
- **Spelling errors in `print`:** Python is case-sensitive — `Print` will cause an error.
- **Using smart quotes:** Copy-pasting from Word or WhatsApp may change `"` to curly quotes — use straight quotes from the keyboard.

### Quick Activity: Hello with Your Name

Write a program that prints your name and your city on two separate lines. Run it and confirm both lines appear in the output.

```python
# Print my name on the first line
print("Rahul Sharma")  # Replace with your actual name

# Print my city on the second line
print("Patna")  # Replace with your actual city
```

**How the code works:**

- Each `print()` call displays one line of output.
- Python runs both lines in order — first name, then city.

---

## Variables — Storing Information in Your Program

Once you can run code, the next step is to **store data**. A program that only prints fixed text cannot calculate your exam percentage or split a restaurant bill. For that, you need **variables**.

### What Is a Variable?

- **Official Definition:** A **variable** is a named reference that stores a value in a program's memory so it can be used later.
- **In Simple Words:** A variable is a labelled box where you keep a piece of information — like writing a name on a dabba and putting something inside it.
- **Real-Life Example:** At a kirana store, the shopkeeper writes "Rice — 2 kg" on a bag. The label is the variable name, and "2 kg" is the value.

![Variables as labelled boxes — name points to a value in memory; = assigns (not maths equality); values can change through reassignment like balance = balance - 120](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-05-variables-labeled-boxes.png)

### Creating a Variable in Python

Python uses **dynamic typing** — you do not need to declare the data type upfront. Python figures it out from the value you assign.

```python
# Create a variable called age and store the number 10 in it
age = 10  # The = sign assigns the value on the right to the name on the left

# Create a variable called name and store text in it
name = "Yash"  # Text values must be wrapped in quotes

# Display what is stored in the variables
print(age)   # This prints the number 10
print(name)  # This prints the text Yash
```

**How the code works:**

- `age = 10` creates a name `age` pointing to the value `10`.
- `name = "Yash"` stores text (a string) in the variable `name`.
- The `=` sign means **assignment**, not maths equality. Read it as "is assigned to."
- In other languages you might write `int age = 10` — in Python, just `age = 10` is enough.

### Changing a Variable (Reassignment)

```python
# Start with a wallet balance of 500 rupees
balance = 500  # Initial value stored in balance

# Spend 120 rupees on lunch
balance = balance - 120  # Subtract 120 from the current balance

# Print the remaining balance
print(balance)  # Output will show 380
```

**How the code works:**

- Variables are called "variable" because their value can **change**.
- `balance - 120` calculates the new amount, and `balance = ...` stores it back in the same variable.

### Quick Activity: Personal Info Card

Create variables for your name, age, and favourite subject. Print each one on a separate line using `print()`.

```python
# Store personal details in variables
my_name = "Amit"              # Your name as text
my_age = 19                   # Your age as a whole number
fav_subject = "Mathematics"   # Your favourite subject as text

# Display each variable
print(my_name)       # Shows your name
print(my_age)        # Shows your age
print(fav_subject)   # Shows your favourite subject
```

---

## Data Types — What Kind of Information Are You Storing?

Not all data is the same. Your age is a number, your name is text, and whether you passed an exam is true or false. Python needs to know **what type** of data you are storing.

### What Is a Data Type?

- **Official Definition:** A **data type** defines the kind of value a variable holds and what operations can be performed on it.
- **In Simple Words:** Data type is like labelling a dabba — "this one has numbers, that one has words."
- **Real-Life Example:** In a form, the "Age" field expects a number and the "Name" field expects text. Mixing them up causes errors — same in programming.

### Core Data Types You Will Use Today

| Data Type | What It Holds | Example |
|-----------|---------------|---------|
| **int** | Whole numbers (no decimals) | `25`, `0`, `-10` |
| **float** | Numbers with decimals | `3.14`, `98.2`, `-0.5` |
| **str** | Text (strings) | `"Hello"`, `'India'` |
| **bool** | True or False values | `True`, `False` |

![Core data types — int for whole numbers, float for decimals, str for text in quotes, bool for True/False; storing '85' as text breaks maths](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-06-data-types-overview.png)

### Examples

```python
# Integer, float, string, and boolean examples
age = 10                  # int — whole number
percentage = 98.2           # float — decimal number
name = "Yash"               # str — text in quotes
is_student_on_leave = True  # bool — True or False (capital T and F)

# Display each value
print(age)                  # Shows 10
print(percentage)           # Shows 98.2
print(name)                 # Shows Yash
print(is_student_on_leave)  # Shows True
```

**How the code works:**

- Python detects the type based on how you write the value — decimals make a `float`, quotes make a `str`.
- A common mistake is storing a number as text (`"85"` instead of `85`) — then maths will not work.
- Strings can use single quotes (`'India'`) or double quotes (`"Hello"`) — both work.

---

## Operators — Making Your Program Calculate and Compare

Variables store data. **Operators** let you do something useful with that data — add numbers, compare values, and combine conditions.

### What Is an Operator?

- **Official Definition:** An **operator** is a symbol that performs an operation on one or more values (operands) in an expression.
- **In Simple Words:** Operators are the maths symbols and logic symbols that make things happen — `+`, `-`, `>`, `and`, and so on.
- **Real-Life Example:** On a calculator, when you press `+`, the calculator knows you want to add. In Python, `+` does the same job.

---

## Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponent (power) | `2 ** 3` | `8` |

```python
# Store two numbers in variables
v1 = 10  # First number
v2 = 20  # Second number

# Perform different arithmetic operations
print(v1 + v2)   # Addition: 30
print(v1 - v2)   # Subtraction: -10
print(v1 * v2)   # Multiplication: 200
print(v1 / v2)   # Division: 0.5
print(v1 % 3)    # Modulus (remainder): 1
print(2 ** 3)    # Exponent (power): 8

# Real-life use: splitting a dinner bill
total_bill = 1500  # Total bill in rupees
num_friends = 3    # Number of people sharing
share = total_bill / num_friends  # Each person pays 500.0
print(share)
```

**How the code works:**

- Each `print()` line performs one operation and shows the result.
- `%` gives the remainder after division. `**` raises a number to a power.
- Storing values in variables (`total_bill`, `num_friends`) makes calculations readable.

![Arithmetic operators — + - * / for maths; % for remainder, ** for power; real-life example splitting a ₹1500 dinner bill among 3 friends](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-07-arithmetic-operators.png)

---

## Comparison Operators

Comparison operators check a condition and return `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<` | Less than | `10 < 3` | `False` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

```python
# Store exam marks
math_marks = 78     # Marks in Mathematics
passing_marks = 40  # Minimum marks needed to pass

# Compare the marks — result is always True or False
print(math_marks > passing_marks)   # True — 78 is greater than 40
print(math_marks == 100)            # False — 78 is not equal to 100
print(math_marks >= 75)             # True — 78 is greater than or equal to 75
```

**How the code works:**

- Comparison operators only **check** a condition — they do not change variables.
- **Common mistake:** Using `=` (assignment) instead of `==` (comparison). `=` stores a value; `==` checks if two values are equal.

---

## Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both conditions must be True | `True and False` | `False` |
| `or` | At least one condition must be True | `True or False` | `True` |
| `not` | Reverses the result | `not True` | `False` |

```python
# Check if a student meets two conditions
name = "Yash"   # Student name
age = 10        # Student age

# and — both conditions must be true
print(name == "Yash" and age == 10)  # True

# or — at least one condition must be true
print(name == "Rahul" or age == 10)  # True (age matches)

# not — reverses the result
print(not (age > 18))  # True (age is not greater than 18)
```

**How the code works:**

- `and` needs **both** sides to be `True`. `or` needs **at least one** side to be `True`.
- `not` flips `True` to `False` and vice versa.

![Comparison and logical operators — == > <= return True or False; and needs both sides True, or needs at least one, not reverses; watch = (assign) vs == (compare)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-08-comparison-logical-operators.png)

---

## The Assignment Operator

The assignment operator `=` stores a value into a variable.

```python
# Assign the value 10 to variable a
a = 10  # a now holds the value 10

# You can use the variable in calculations
b = a + 5  # b gets 15
print(b)   # Prints 15
```

**How the code works:**

- `a = 10` means "store 10 in the variable named a."
- You can use a variable on the right side of `=` to create a new value, as in `b = a + 5`.

---

## Expressions

An **expression** is a combination of values, variables, and operators that produces a result.

```python
# Store two values and add them
v1 = 10              # First value
v2 = 20              # Second value
v3 = v1 + v2         # Expression: adds v1 and v2
print(v3)            # Prints 30
```

**How the code works:**

- `v1 + v2` is an expression — Python calculates the result and stores it in `v3`.
- Clear variable names (`v1`, `v2`, `v3`) make expressions easy to read and debug.

### Quick Activity: Pocket Money Calculator

A student receives ₹2000 pocket money and spends ₹450 on books and ₹320 on food. Calculate and print how much money is left.

```python
# Starting pocket money and expenses
pocket_money = 2000  # Total money received
book_cost = 450      # Money spent on books
food_cost = 320      # Money spent on food

# Calculate and show remaining money
remaining = pocket_money - book_cost - food_cost  # Subtract both expenses
print(remaining)  # Prints 1230
```

---

## Input and Output — Talking to the User

So far, your programs used fixed values. Real programs need to **ask the user for information** and **show a result**. That is where `input()` and `print()` come in.

### What Is Input/Output?

- **Official Definition:** **Input** is data a program receives from an external source (like the user). **Output** is data the program displays or returns.
- **In Simple Words:** Input is when the program listens to you; output is when the program replies to you.
- **Real-Life Example:** At a railway counter, you tell the clerk your destination (input), and the clerk prints your ticket (output).

![Input and output flow — input() collects user text (always a string), convert with int() before maths, print() shows results; '22' + 5 errors but 22 + 5 works](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-09-input-output-flow.png)

---

## The `print()` Function — Showing Output

```python
# Print multiple items in one line
name = "Sneha"    # Store name in a variable
age = 21          # Store age in a variable
print("Name:", name, "Age:", age)  # Prints: Name: Sneha Age: 21
```

**How the code works:**

- `print()` can take multiple items separated by commas.
- Each `print()` call can show one or more values on the screen.

---

## The `input()` Function — Getting Input from the User

```python
# Ask the user to enter their name
name = input("Enter your name: ")  # Program waits for you to type and press Enter
print("Hello,", name)  # Uses whatever name the user typed

# input() always returns a string — convert before doing maths
v1 = int(input("Enter the value of V1: "))  # Converts user input to integer
v2 = int(input("Enter the value of V2: "))  # Converts user input to integer
total = v1 + v2                              # Add the two numbers
print("Total is", total)                     # Show the result
```

**How the code works:**

- `input()` shows a message and **waits** until the user presses Enter.
- Whatever the user types is stored as a **string** by default — use `int()` before doing maths with whole numbers.
- **Common mistake:** `"22" + 5` causes an error, but `22 + 5` works.
- If the user types something that is not a valid integer, Python will show an error.

---

## Putting It All Together — A Complete Interactive Program

This program asks the user for two numbers, adds them, and shows the total — the same pattern demonstrated in the live session.

```python
# Collect two numbers from the user
v1 = int(input("Enter the value of V1: "))  # First number from user
v2 = int(input("Enter the value of V2: "))  # Second number from user

# Calculate the total
total = v1 + v2  # Add both values

# Display the result
print("Total is", total)  # Output changes based on what the user types
```

**How the code works:**

- `int(input(...))` collects a number from the user and converts it from text to integer in one step.
- The output is different every time because it depends on user input.
- You can change `+` to `-`, `*`, or `/` to perform other operations.

### Quick Activity: Two-Number Calculator

Write a program that asks the user for two numbers, multiplies them, and prints the result. Use `int(input())` for both numbers.

---

## Debugging Tips

When your code shows an error, do not panic — every programmer faces this daily.

- **Read the error message** — the last line usually tells you what went wrong.
- **Check spelling, quotes, and data types** — remember that `input()` always gives you text until you convert it.
- **Test small pieces first** in the online compiler before combining into one big program.
- **Use `print()` to debug** — print variable values mid-program to see what Python is storing.

---

## Key Takeaways

- **Programming** means writing clear step-by-step instructions for a computer; **Python** is a beginner-friendly language widely used in software development and AI.
- An **online compiler** lets you write and run Python code in your browser — no installation needed on day one.
- A **compiler** converts your high-level Python code into binary so the computer can execute it.
- **Variables** store data, **data types** (int, float, str, bool) define what kind of data you are storing, and **operators** let you calculate, compare, and combine values.
- **`input()`** collects data from the user (always as text), and **`print()`** displays output — use `int()` to convert input before doing maths with whole numbers.
- **Comments** (`#` and triple quotes) help you document code without affecting execution.
- These building blocks prepare you for **conditional logic** (if/else decisions), which you will use to make programs that choose different paths based on conditions.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| `print()` | Displays output on the screen |
| `input()` | Takes text input from the user |
| `int()` | Converts a value to a whole number (integer) |
| **Variable** | A named container that stores a value |
| **int** | Data type for whole numbers (e.g., `42`) |
| **float** | Data type for decimal numbers (e.g., `3.14`) |
| **str** | Data type for text/strings (e.g., `"Hello"`) |
| **bool** | Data type for `True` or `False` |
| **Operator** | A symbol that performs an operation (`+`, `-`, `==`, `and`) |
| **Expression** | A combination of values and operators that produces a result |
| **Assignment (`=`)** | Stores a value into a variable |
| **Comparison (`==`, `>`, `<`)** | Checks a condition; returns `True` or `False` |
| **Arithmetic (`+`, `-`, `*`, `/`)** | Performs mathematical calculations |
| **Logical (`and`, `or`, `not`)** | Combines or reverses boolean conditions |
| **Compiler** | Converts high-level code to machine-readable binary |
| **Online compiler** | A web tool to write and run code in the browser |
| **Code editor** | The area where you type Python code |
| **Comment (`#`)** | A note for humans that Python ignores |
| **Function** | A reusable block of code — `print()` is a built-in function |
