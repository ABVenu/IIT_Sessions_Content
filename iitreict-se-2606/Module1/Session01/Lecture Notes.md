# Introduction to Programming & Python Basics

## What You Will Learn in This Lesson

This is your first step into the world of programming. You do not need any prior coding experience to follow along.

In this lesson, you will learn what a **program** is, how **Python** code is written and executed, and how to use **OneCompiler** — a free online compiler at [onecompiler.com](https://onecompiler.com/) — without installing anything on your laptop. You will store information using **variables** and **data types**, calculate and compare values with **operators** and **expressions**, and build simple interactive programs with **input()** and **print()**.

By the end, you will be able to write small programs that ask a question, do a calculation, and show a result on the screen.

---

## What Is Programming?

- **Official Definition:** **Programming** is the process of writing step-by-step instructions that a computer can understand and execute to perform a task.
- **In Simple Words:** Programming is like giving very clear directions to a machine that never guesses — it only does exactly what you tell it.
- **Real-Life Example:** Think of programming like writing a recipe for a cook. If you write "add salt," the cook adds salt. If you forget to mention "turn on the gas," nothing gets cooked. Computers are the same — every step must be written clearly.

### What Is a Program?

- **Official Definition:** A **program** is a complete set of instructions written in a programming language that the computer can run from start to finish.
- **In Simple Words:** A program is the finished recipe file — not just one step, but the full list of steps saved together so the computer can follow them in order.
- **Real-Life Example:** A UPI payment app is a large program. Your first Hello World file is also a program — smaller, but the same idea: write instructions, then run them.

### How Python Code Is Written and Executed

- You **write** Python code as plain text — usually one instruction per line — in a code editor (here, inside OneCompiler).
- When you click **Run**, Python reads your file **from top to bottom**, executes each line, and shows results (or errors) in the output area.
- If a line has a mistake (wrong spelling, missing quotes, wrong data type), Python stops and shows an **error message** — that is normal while learning.

### Why Do We Need Programming?

- Almost everything digital around you runs on code — UPI payments, train ticket booking, WhatsApp, and the **AI and agentic systems** you will build and design later in this course.
- Programming teaches you to **break big problems into small steps**, which is useful in life and in tech careers.

![Programming as a step-by-step recipe — every instruction must be clear; forget a step and the computer cannot finish the task; the same idea powers UPI, train booking, WhatsApp, and AI tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-01-programming-recipe-analogy.png)

### What Is Python?

- **Official Definition:** **Python** is a high-level, general-purpose programming language known for its simple, readable syntax.
- **In Simple Words:** Python is a language humans use to talk to computers — and it reads almost like plain English.
- **Real-Life Example:** If programming languages were languages you speak, Python is like Hindi or English — easy to start with and widely used everywhere.

- It is one of the most popular languages for **software**, **data**, **AI**, and **agentic systems**.
- You can start writing code in your browser on day one — no complicated installation needed.
- The syntax is beginner-friendly, so you can focus on **thinking logically** instead of fighting with complex rules.

![Why Python for beginners — readable syntax like plain English, no install needed in the browser, and widely used in software, data, AI, and agentic systems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-02-python-beginner-language.png)

---

## Setting Up OneCompiler

Before you can run Python code, you need a place to write it and execute it. For this course, we use **OneCompiler** — a free **online compiler** at [https://onecompiler.com/](https://onecompiler.com/) where you write code and see the output instantly, without installing anything on your laptop.

### What Is an Online Compiler?

- **Official Definition:** An **online compiler** is a web-based tool that lets you write, run, and test code directly in a browser.
- **In Simple Words:** It is like a digital notebook with a "Run" button — you type code, press Run, and the result appears on the screen.
- **Real-Life Example:** Just like you fill an online form without buying special software, an online compiler lets you write Python without installing it on your machine.

### What Is OneCompiler?

- **Official Definition:** **OneCompiler** is a free online compiler that lets you write, run, save, and share code in 100+ programming languages — including Python — directly in your browser.
- **In Simple Words:** OneCompiler is your coding workspace on the internet — open the website, pick Python, write code, and run it.
- **Real-Life Example:** Think of OneCompiler like a shared online document for code — you can write your program, save it, and send the link to your instructor or a friend.

### Why OneCompiler Is Best to Start With

- It is the **best way to start for beginners** — no complicated installation, no confusing setup on day one.
- It works on any laptop or phone with an internet connection.
- You can **save all your code and work** in one place and come back to it anytime.
- You can **share a link** to your saved program with your instructor or classmates for review or help.

### How to Get Started on OneCompiler

Follow these steps on your laptop or desktop browser:

1. Open [https://onecompiler.com/](https://onecompiler.com/) in Chrome or any modern browser.
2. Click **Python** from the language list.
3. **Sign up or sign in** to save your work and share links — recommended from day one.
4. Type your Python code in the **code editor** — the main writing area on the screen.
5. Click **Run** to execute your code. The **output** appears below or beside the editor.
6. Use **Save** to store your program and **Share** to copy a link for others.

![OneCompiler workflow — open onecompiler.com, pick Python, type in the editor, click Run, and see output below; sign in to save work and share links with your instructor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-03-onecompiler-workspace.png)

### Your First Python Program

Type the following in OneCompiler and run it:

```python
# This is my very first Python program
# The print() function displays text on the screen
print("Hello, World!")  # This line prints a greeting message
```

**How the code works:**

- Lines starting with `#` are **comments** — notes for humans that Python ignores.
- `print()` shows output on the screen. The text in quotes is a **string** (text data).
- When you click Run, OneCompiler executes every line from top to bottom.

![Hello, World flow — type code, click Run, Python executes top to bottom; comments (#) are ignored, print() shows output; watch for case-sensitive print and straight quotes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-04-hello-world-flow.png)

### Common Beginner Mistakes on OneCompiler

- **Forgetting to click Run:** Typing code alone does nothing — you must press the Run button.
- **Not saving your work:** Use Save so you do not lose your progress.
- **Spelling errors in `print`:** Python is case-sensitive — `Print` will cause an error.
- **Using smart quotes:** Copy-pasting from Word or WhatsApp may change `"` to curly quotes — use straight quotes from the keyboard.

### Quick Activity: Hello with Your Name

In OneCompiler, write a program that prints your name and your city on two separate lines. Run it and confirm both lines appear in the output.

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

```python
# Create a variable called age and store the number 22 in it
age = 22  # The = sign assigns the value on the right to the name on the left

# Create a variable called name and store text in it
name = "Priya"  # Text values must be wrapped in quotes

# Display what is stored in the variables
print(age)   # This prints the number 22
print(name)  # This prints the text Priya
```

**How the code works:**

- `age = 22` creates a name `age` pointing to the value `22`.
- `name = "Priya"` stores text (a string) in the variable `name`.
- The `=` sign means **assignment**, not maths equality. Read it as "is assigned to."

### Variable Naming Rules

- Names can contain letters, numbers, and underscores — but **cannot start with a number** (`score1` ✓, `1score` ✗).
- Names are **case-sensitive** — `Age` and `age` are different variables.
- Use **descriptive names** — `student_marks` is better than `x` when you are learning.
- Avoid Python **reserved words** like `print`, `if`, `else` as variable names.

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

**How the code works:**

- Three variables store three different pieces of information — text and a number.
- Each `print()` shows one value. Replace the sample data with your own details and run again.

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
| **float** | Numbers with decimals | `3.14`, `99.5`, `-0.5` |
| **str** | Text (strings) | `"Hello"`, `'India'` |
| **bool** | True or False values | `True`, `False` |

![Core data types — int for whole numbers, float for decimals, str for text in quotes, bool for True/False; use type() to debug; storing '85' as text breaks maths](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-06-data-types-overview.png)

### Examples and Checking Types

```python
# Integer, float, string, and boolean examples
students = 40          # int — whole number
temperature = 36.6     # float — decimal number
city = "Bengaluru"     # str — text in quotes
is_passed = True       # bool — True or False (capital T and F)

# Use type() to check what kind of data each variable holds
print(type(students))     # Shows <class 'int'>
print(type(temperature))  # Shows <class 'float'>
print(type(city))         # Shows <class 'str'>
print(type(is_passed))    # Shows <class 'bool'>
```

**How the code works:**

- Python detects the type based on how you write the value — decimals make a `float`, quotes make a `str`.
- `type()` tells you the data type — useful when debugging. A common mistake is storing a number as text (`"85"` instead of `85`) — then maths will not work.

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
| `//` | Floor division (whole number division) | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponent (power) | `2 ** 3` | `8` |

```python
# Store two numbers in variables
a = 20  # First number
b = 6   # Second number

# Perform different arithmetic operations
print(a + b)   # Addition: 26
print(a - b)   # Subtraction: 14
print(a * b)   # Multiplication: 120
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus (remainder): 2
print(a ** 2)  # Exponent: 400

# Real-life use: splitting a dinner bill
total_bill = 1500  # Total bill in rupees
num_friends = 3    # Number of people sharing
share = total_bill / num_friends  # Each person pays 500.0
print(share)
```

**How the code works:**

- Each `print()` line performs one operation and shows the result.
- `/` always gives a float in Python 3. `//` drops the decimal; `%` gives the remainder.
- Storing values in variables (`total_bill`, `num_friends`) makes calculations readable.

![Arithmetic operators — + - * / for maths; // for whole-number division, % for remainder, ** for power; real-life example splitting a ₹1500 dinner bill among 3 friends](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-07-arithmetic-operators.png)

---

## Comparison Operators

Comparison operators check a condition and return `True` or `False`. You will use these heavily when you learn **if/else** statements.

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
- **Common mistake:** Using `=` (assignment) instead of `==` (comparison).

---

## Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both conditions must be True | `True and False` | `False` |
| `or` | At least one condition must be True | `True or False` | `True` |
| `not` | Reverses the result | `not True` | `False` |

```python
# Check if a student can get a scholarship
marks = 85              # Student's marks
attendance = 90         # Attendance percentage
eligible = (marks >= 80) and (attendance >= 75)  # Both must be true
print(eligible)  # True

# Check if a number is outside the range 1 to 100
number = 150  # A number greater than 100
out_of_range = (number < 1) or (number > 100)  # True if either condition is true
print(out_of_range)  # True
```

**How the code works:**

- `and` needs **both** sides to be `True`. `or` needs **at least one** side to be `True`.
- Parentheses `()` group conditions clearly — a good habit from the start.

![Comparison and logical operators — == > <= return True or False; and needs both sides True, or needs at least one, not reverses; watch = (assign) vs == (compare); += -= shortcuts update variables](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-08-comparison-logical-operators.png)

---

## Assignment Operators

Assignment operators update a variable's value in a shortcut way.

| Operator | Meaning | Example | Same As |
|----------|---------|---------|---------|
| `=` | Assign value | `x = 5` | `x = 5` |
| `+=` | Add and assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |

```python
# Start with a score of 0
score = 0  # Initial score before any points are added
score += 10  # Same as score = score + 10; score is now 10
score += 5   # score is now 15
score -= 3   # score is now 12
print(score)  # Prints 12
```

**How the code works:**

- `+=` adds to the current value and stores the result back. `-=` subtracts similarly.
- These shortcuts are common in games, counters, and loops.

---

## Expressions and Order of Operations

An **expression** is a combination of values, variables, and operators that produces a result.

```python
# Calculate total price with 18% GST
price = 1000       # Base price of an item
gst_rate = 0.18    # 18% GST as a decimal
total = price + (price * gst_rate)  # Parentheses control calculation order
print(total)  # Prints 1180.0
```

**How the code works:**

- Python follows maths rules: **parentheses first**, then `**`, then `* / // %`, then `+ -`.
- Clear variable names (`price`, `gst_rate`, `total`) make expressions easy to read and debug.

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

**How the code works:**

- Store the starting amount and each expense in clear variable names.
- Subtract both expenses from pocket money to get what remains, then print the result.

---

## Input and Output — Talking to the User

So far, your programs used fixed values. Real programs need to **ask the user for information** and **show a result**. That is where `input()` and `print()` come in.

### What Is Input/Output?

- **Official Definition:** **Input** is data a program receives from an external source (like the user). **Output** is data the program displays or returns.
- **In Simple Words:** Input is when the program listens to you; output is when the program replies to you.
- **Real-Life Example:** At a railway counter, you tell the clerk your destination (input), and the clerk prints your ticket (output).

![Input and output flow — input() collects user text (always a string), convert with int() or float() before maths, print() and f-strings show results; '22' + 5 errors but 22 + 5 works](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session01/session01-09-input-output-flow.png)

---

## The `print()` Function — Showing Output

```python
# Print multiple items in one line
name = "Sneha"    # Store name in a variable
age = 21          # Store age in a variable
print("Name:", name, "Age:", age)  # Prints: Name: Sneha Age: 21

# Print with f-strings — embed variables inside text
marks = 92  # Store marks for use inside the f-string
print(f"Sneha scored {marks} marks out of 100")
```

**How the code works:**

- `print()` can take multiple items separated by commas.
- An **f-string** starts with `f"` and puts variables inside `{}` curly braces.

---

## The `input()` Function — Getting Input from the User

```python
# Ask the user to enter their name
name = input("Enter your name: ")  # Program waits for you to type and press Enter
print("Hello,", name)  # Uses whatever name the user typed

# input() always returns a string — convert before doing maths
age_text = input("Enter your age: ")  # User types 22, but Python stores "22" as text
age_number = int(age_text)  # Converts "22" to the number 22
print(type(age_number))     # Shows <class 'int'>
```

**How the code works:**

- `input()` shows a message and **waits** until the user presses Enter.
- Whatever the user types is stored as a **string** — use `int()` or `float()` before maths.
- **Common mistake:** `"22" + 5` causes an error, but `22 + 5` works.

---

## Putting It All Together — A Complete Interactive Program

This program asks for marks, calculates the percentage, and shows the result.

```python
# Collect inputs from the user
subject = input("Enter subject name: ")  # Store subject name as text
marks_obtained = int(input("Enter marks obtained: "))  # Convert to integer
total_marks = int(input("Enter total marks: "))        # Convert to integer

# Calculate percentage
percentage = (marks_obtained / total_marks) * 100  # Formula: (obtained/total) * 100

# Display the result
print(f"In {subject}, you scored {marks_obtained} out of {total_marks}.")  # Show marks summary
print(f"Your percentage is {percentage}%")  # Show calculated percentage
```

**How the code works:**

- `int()` is used directly inside `input()` — a shorter way to convert numbers.
- The percentage formula divides obtained by total, then multiplies by 100.
- f-strings format the final output neatly for the user.

### Quick Activity: Simple EMI Calculator

Write a program that asks for the total price of a mobile phone and the number of months for EMI. Use `float()` for price and `int()` for months. Divide price by months and print the monthly EMI.

```python
# Ask for the phone price and convert the text to a decimal number
phone_price = float(input("Enter mobile phone price: "))  # Example: 30000.0

# Ask for EMI months and convert the text to a whole number
months = int(input("Enter number of EMI months: "))  # Example: 12

# Calculate monthly EMI by dividing price by months
monthly_emi = phone_price / months  # Each month share of the total price

# Show the monthly EMI clearly to the user
print(f"Your monthly EMI is Rs. {monthly_emi}")  # Displays the calculated EMI
```

**How the code works:**

- `float()` is used for price because money can have decimals (like `29999.50`).
- `int()` is used for months because the count of months is a whole number.
- Dividing price by months gives one month's EMI; the f-string prints it neatly.

---
## Practice Program: Mini Student Report Card

Combine everything you learned into one program.

```python
# Collect student information from the user
student_name = input("Enter student name: ")         # Get student name
maths_marks = int(input("Enter Maths marks: "))      # Get Maths marks
science_marks = int(input("Enter Science marks: "))  # Get Science marks
english_marks = int(input("Enter English marks: "))   # Get English marks

# Calculate total and average
total_marks = maths_marks + science_marks + english_marks  # Add all three subjects
average = total_marks / 3                                   # Divide by 3 for average

# Display the report card
print("----- Report Card -----")              # Print a heading line
print(f"Name: {student_name}")                # Show student name
print(f"Maths: {maths_marks}")                # Show Maths marks
print(f"Science: {science_marks}")            # Show Science marks
print(f"English: {english_marks}")            # Show English marks
print(f"Total: {total_marks}")                # Show total of all subjects
print(f"Average: {average}")                  # Show average marks
```

**How the code works:**

- The program uses `input()` to collect data and `int()` to convert marks to numbers.
- Arithmetic operators calculate total and average. Multiple `print()` calls format a clean report card.

---

## Debugging Tips

When your code shows an error, do not panic — every programmer faces this daily.

- **Read the error message** — the last line usually tells you what went wrong.
- **Check spelling, quotes, and data types** — use `type()` if maths fails unexpectedly.
- **Test small pieces first** on OneCompiler before combining into one big program.
- **Use `print()` to debug** — print variable values mid-program to see what Python is storing.

---

## Key Takeaways

- A **program** is a full set of instructions; **programming** means writing those steps clearly for a computer, and **Python** is a beginner-friendly language used widely in software, AI, and agentic systems.
- **OneCompiler** ([onecompiler.com](https://onecompiler.com/)) lets you write and run Python code in your browser — type code, click Run to execute top to bottom, save your work, and share links when needed.
- **Variables** store data, **data types** (int, float, str, bool) define what kind of data you are storing, and **operators** and **expressions** let you calculate, compare, and combine values.
- **`input()`** collects data from the user (always as text), and **`print()`** displays output — use `int()` or `float()` to convert input before doing maths.
- These building blocks prepare you for **conditional logic** (if/else decisions) in upcoming sessions, where programs will choose different paths based on conditions.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **Program** | A complete set of instructions the computer can run from start to finish |
| `print()` | Displays output on the screen |
| `input()` | Takes text input from the user |
| `type()` | Shows the data type of a value |
| `int()` | Converts a value to a whole number (integer) |
| `float()` | Converts a value to a decimal number |
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
| **f-string** | A formatted string like `f"Hello {name}"` to embed variables in text |
| **OneCompiler** | Free online compiler at [onecompiler.com](https://onecompiler.com/) to write, run, save, and share Python code |
| **Code editor** | The area in OneCompiler where you type Python code |
| **Comment (`#`)** | A note for humans that Python ignores |
