# Operators & Conditional Statements

## What You Will Learn in This Lesson

You have already learned how to write Python programs using variables, arithmetic operators, comparison operators, logical operators, and basic **input/output**. Your programs could calculate marks, split bills, and show results — but they always followed the same straight path from top to bottom.

In this lesson, you will learn how to make your programs **think and choose**. You will use **conditional statements** (`if`, `elif`, `else`) to run different code depending on whether a condition is **True** or **False**. You will also practise **logical thinking** — breaking real problems into small, testable steps before writing code.

By the end, you will be able to write programs that check exam results, validate login details, compare numbers, and handle multiple possible outcomes — just like real apps do every day.

---

## Why Do Programs Need to Make Decisions?

- **Official Definition:** **Program flow control** is the ability of a program to change the order of execution based on conditions, rather than running every line in a fixed sequence.
- **In Simple Words:** Decision-making in code means the program picks what to do next — like choosing a different road at a fork.
- **Real-Life Example:** At a railway station, if your ticket is for Platform 3, you walk left; otherwise, you walk right. The platform number is the **condition**, and your direction is the **action**.

- **UPI apps** check your balance before allowing a payment — if balance is low, they show an error.
- **Exam result portals** display "Pass" or "Fail" based on marks.
- **ATMs** ask for your PIN — wrong PIN blocks withdrawal; correct PIN opens the menu.

Without conditionals, every program would be like a fixed recipe that never changes. Conditionals make programs **smart and responsive**.

![Program flow control diagram — railway platform fork shows True and False paths; real apps use the same decision logic for UPI balance, exam results, and ATM PIN validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-01-program-decision-flow.png?v=20260614)

---

## Quick Recap: Conditions and Boolean Values

A **condition** is any expression that Python evaluates as either **True** or **False**.

- **Official Definition:** A **boolean** is a data type that can hold only two values: `True` or `False`.
- **In Simple Words:** A boolean is a yes-or-no answer stored in code.
- **Real-Life Example:** When a shopkeeper asks "Do you have a membership card?" your answer is either yes or no.

### Comparison Operators — A Quick Reminder

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `50 == 50` | `True` |
| `!=` | Not equal to | `50 != 40` | `True` |
| `>` | Greater than | `85 > 40` | `True` |
| `<` | Less than | `30 < 40` | `True` |
| `>=` | Greater than or equal to | `40 >= 40` | `True` |
| `<=` | Less than or equal to | `35 <= 40` | `True` |

### Logical Operators — A Quick Reminder

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and False` | `False` |
| `or` | At least one must be True | `True or False` | `True` |
| `not` | Reverses True to False | `not True` | `False` |

![Boolean values and comparison operators — all six comparison operators with examples, logical and/or/not truth table, and the common = vs == mistake](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-02-boolean-conditions.png?v=20260614)

- **Common mistake:** Using `=` instead of `==`. `marks = 50` assigns a value; `marks == 50` compares values.
- The output of comparison and logical operators is always a **boolean** — `True` or `False`.

Now that you can build conditions, the next step is telling Python **what to do** when a condition is true — that is where `if` comes in.

---

## The `if` Statement — Running Code Only When a Condition Is True

- **Official Definition:** An **`if` statement** executes a block of code only when its condition evaluates to `True`.
- **In Simple Words:** `if` means "only do this when the check passes."
- **Real-Life Example:** "If it is raining, take an umbrella." The action happens only when the condition is true.

### Basic Syntax and Rules

```python
if condition:  # Condition followed by a colon
    # Indented code runs only when condition is True (usually 4 spaces)
```

- Start with `if`, then the **condition**, then a **colon `:`**.
- Indented lines belong to the `if` block. If the condition is `False`, Python **skips** that block.
- Lines **not indented** after the block always run.
- **Indentation** is mandatory — wrong indentation causes a `SyntaxError` or `IndentationError`.

![if statement diagram — full voting eligibility code, syntax rules, True vs False paths, and step-by-step flow from input to output](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-03-if-statement-flow.png?v=20260614)

### Real-World Style Example — Temperature and AC

```python
# If temperature is above 30, turn on the AC; otherwise turn it off
temperature = 30  # Current room temperature
if temperature > 30:  # Condition: hotter than 30
    print("Turn on the AC")  # Runs only when condition is True
else:  # Temperature is 30 or below
    print("Turn off the AC")  # Runs when condition is False
```

**How the code works:**

- The condition after `if` must evaluate to `True` or `False`.
- Only the matching indented block runs.

### `if` with User Input and Age Check

```python
# Check whether age is greater than 20
age = int(input("Enter your age: "))  # Convert input text to a whole number
if age > 20:  # Condition: is age above 20?
    print("You are above 20.")  # Runs only when condition is True
else:  # Age is 20 or below
    print("You are 20 or below.")  # Runs when condition is False
```

**How the code works:**

- `int()` converts input text to a number before comparing.
- **Common mistake:** Forgetting `int()` — comparing `"20" > 20` causes a `TypeError`.
- **Indentation** defines which lines belong to the `if` block.

An `if` handles "when true, do something." When the condition is false, `else` provides the alternative.

---

## The `else` Statement — What to Do When the Condition Is False

- **Official Definition:** An **`else` statement** runs when the `if` condition is `False`.
- **In Simple Words:** `else` means "otherwise, do this instead."
- **Real-Life Example:** "If the milk is boiled, turn off the gas; **else**, keep heating."

![if/else diagram — pass/fail decision tree with complete code for even/odd checker and modulus remainder explanation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-04-if-else-branches.png?v=20260614)

### Check Whether English Marks Cross the Passing Line

```python
# Passing marks in English is 50
marks_in_english = int(input("Enter marks in English: "))  # Convert input to integer
passing_marks = 50  # Minimum marks to pass
if marks_in_english > passing_marks:  # Marks above 50 means pass
    print("Student passed in English")  # Student passed
else:  # Marks 50 or below
    print("Student failed in English")  # Student failed
```

**How the code works:**

- Exactly **one** block runs — never both, never neither.
- `else` automatically covers everything the `if` did not catch.

Many problems have **more than two** outcomes — like borderline pass marks or grade bands. That is what `elif` is for.

---

## The `elif` Statement — Handling Multiple Conditions

- **Official Definition:** **`elif`** checks additional conditions when previous ones are `False`.
- **In Simple Words:** `elif` means "if the first check failed, try this next one."
- **Real-Life Example:** At a restaurant — thali, **elif** dosa, **else** default combo. Checked in order.

### Basic Syntax and Rules

```python
if condition_1:      # Checked first
    # Runs when condition_1 is True
elif condition_2:    # Checked only if condition_1 was False
    # Runs when condition_2 is True
else:                # Runs when all above are False
    # Default case
```

- Python checks **top to bottom** and stops at the **first** `True` condition.
- Only **one** block in the chain runs. Put the **strictest** condition first.

![if/elif/else chain — full grade A to F ladder with complete condition and outcome text, wrong-order warning, and billing slab use cases](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-05-elif-chain.png?v=20260614)

### English Marks — Pass, Borderline, or Fail

```python
# Three outcomes for English marks with passing marks = 50
marks_in_english = int(input("Enter marks in English: "))  # Get marks as integer
passing_marks = 50  # Minimum passing marks
if marks_in_english > passing_marks:  # Above 50
    print("Student passed in English with flying colours")  # Clear pass
elif marks_in_english == passing_marks:  # Exactly 50
    print("Student just passed in English")  # Borderline pass
else:  # Below 50
    print("Student failed in English")  # Fail
```

**How the code works:**

- If marks is 55, only the first `if` runs — remaining conditions are skipped.
- `elif` is used when conditions are **mutually exclusive** — only one outcome should print.
- **Common mistake:** Using only `if` for every check — multiple blocks might run when you want just one.

---

## Storing Comparison Results in a Variable

Instead of repeating the same comparison inside every `if`, you can store the boolean result first and reuse it.

```python
# Store the comparison result, then use it in if/else
marks_in_english = 55  # Student's English marks
passing_marks = 50  # Passing threshold
result_for_english = marks_in_english > passing_marks  # True or False stored in a variable
if result_for_english:  # Reuse the stored boolean
    print("Student passed in English")  # Passed
else:  # result_for_english is False
    print("Student failed in English")  # Failed
```

**How the code works:**

- `result_for_english` holds `True` when marks are above 50, otherwise `False`.
- Storing the result makes long programs easier to read and debug.
- You can `print(result_for_english)` to verify what Python evaluated before the `if` runs.

---

## Combining Logical Operators Inside Conditions

Use `and`, `or`, and `not` directly inside `if` conditions when one check is not enough.

```python
# and — both conditions must be True (mark range check)
marks_in_english = 55  # Student marks
if (marks_in_english > 50) and (marks_in_english < 60):  # Between 50 and 60
    print("Grade C")  # Marks fall in this band
```

**How the code works:**

- `and` requires **both** sides to be `True`.
- `or` requires **at least one** side to be `True`.
- `not` flips `True` to `False` and vice versa.
- Parentheses around comparisons in complex conditions make code easier to read.

![Logical operators in conditions — complete scholarship, discount, and login examples with full truth table and parentheses readability tip](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-06-logical-operators.png?v=20260614)

### Login Validation with `and` and `elif`

Use a flat `if` / `elif` chain with `and` — not nested `if` blocks inside each other.

```python
# Stored credentials (in real apps, these live in a secure database)
username = "Masai"  # Expected username
password = "Masai123"  # Expected password

# Get login details from the user
uname = input("Enter username: ")  # User types username
pwd = input("Enter password: ")  # User types password

if uname == username and pwd == password:  # Both match — login success
    print("Logged in successfully")  # Correct credentials
elif uname != username and pwd != password:  # Both are wrong
    print("Username and password both are incorrect")  # Both failed
elif uname != username:  # Only username is wrong
    print("Username is incorrect")  # Wrong username
elif pwd != password:  # Only password is wrong
    print("Password is not correct")  # Wrong password
```

**How the code works:**

- `and` checks that **both** username and password match before allowing login.
- Separate `elif` branches give **different error messages** for each failure case.
- Python checks conditions **top to bottom** and stops at the first match.

![Nested conditionals — full login validation flowchart with complete username/password code and separate error messages for each failure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-07-nested-conditionals.png?v=20260614)

---

## Variable Naming Conventions

When you create variables in Python, follow these simple rules:

- Use a **single word** or **words separated by underscores** — e.g. `marks_in_english`, not `MarksInEnglish`.
- Do **not** start a variable name with a **capital letter** or a **number**.
- Choose names that describe what the value stores — `passing_marks` is clearer than `pm`.

**Real-Life Example:** Labelling masala jars in the kitchen — "haldi", "jeera", "dhaniya" — each name tells you exactly what is inside.

---

## Common Mistakes with Conditionals

| Mistake | Wrong Code | Correct Code | Why It Fails |
|---------|-----------|--------------|--------------|
| Using `=` instead of `==` | `if marks = 50:` | `if marks == 50:` | `=` assigns; `==` compares |
| Forgetting the colon | `if marks >= 40` | `if marks >= 40:` | Python expects `:` after the condition |
| Wrong indentation | No indent after `if` | Indent with 4 spaces | Python cannot find the block |
| String vs number | `age == 18` when age is `"18"` | `int(age) == 18` | Different types cannot compare |
| Wrong `elif` order | `>= 40` before `>= 90` | Put `>= 90` first | Higher threshold must come first |
| Skipping `int()` on input | `num > 0` when num is `"5"` | `int(input(...))` | Input returns text, not a number |

![Common conditional mistakes — all six errors with wrong code, correct code, reason, and debugging tips for boundary values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-09-common-mistakes.png?v=20260614)

---

## Logical Thinking — Breaking Problems Into Steps

- **Official Definition:** **Algorithmic thinking** is defining clear, ordered steps to solve a problem, where each step can be tested independently.
- **In Simple Words:** Think of the exact steps first, then write code.
- **Real-Life Example:** Making chai — boil water, add tea, add milk, add sugar. Order matters, just like in code.

Before you type any conditional program, walk through these steps:

1. **Read the problem** in plain English — what should the program decide?
2. **List the inputs** you need from the user.
3. **Write each condition and its outcome** — one row per case.
4. **Translate each row** into an `if`, `elif`, or `else` block.

![STEP method — State, inputs, conditions/outcomes, and Python code with full cinema ticket example and complete working program](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-08-step-method.png?v=20260614)

**Example:** For the login problem, start by listing the rules — check username, then check password, then decide which message to print — before writing the `if` / `elif` chain.

---

## Practice Programs — Beginner Conditional Exercises

Work through each program in your online IDE. Type the code yourself and test with different inputs.

### Exercise 1: Positive or Negative Number

```python
# Check whether a number is positive or negative
num = int(input("Enter the number: "))  # Convert input to integer
if num >= 0:  # Zero and positive numbers
    print("Positive")  # Non-negative
else:  # Less than zero
    print("Negative")  # Negative number
```

**How the code works:**

- `int(input())` converts the user's text input to a whole number.
- `>= 0` treats zero as positive/non-negative, matching the solution discussed in class.

### Exercise 2: Largest of Two Numbers

```python
# Compare two numbers and print the larger one (or equal)
first_number = int(input("Enter the first number: "))  # First input
second_number = int(input("Enter the second number: "))  # Second input
if first_number > second_number:  # First is larger
    print("First is bigger")  # First wins
elif second_number > first_number:  # Second is larger
    print("Second is bigger")  # Second wins
else:  # Both are equal
    print("Both are equal")  # Tie
```

**How the code works:**

- Two separate inputs are compared with `>` and `elif`.
- The final `else` handles the case when both numbers are the same.

### Exercise 3: Login Credential System

```python
# Validate username and password against stored values
username = "Masai"  # Stored username
password = "Masai123"  # Stored password
uname = input("Enter username: ")  # User input for username
pwd = input("Enter password: ")  # User input for password
if uname == username and pwd == password:  # Both correct
    print("Logged in successfully")  # Login allowed
elif uname != username and pwd != password:  # Both wrong
    print("Username and password both are incorrect")  # Both failed
elif uname != username:  # Username wrong
    print("Username is incorrect")  # Wrong username only
elif pwd != password:  # Password wrong
    print("Password is not correct")  # Wrong password only
```

**How the code works:**

- `and` ensures both fields match before printing success.
- Each `elif` gives a **specific error message** so the user knows what went wrong.

### Exercise 4: Grade Calculator

```python
# Assign grade based on maths marks
math_marks = int(input("Enter the marks: "))  # Maths marks as integer
if math_marks > 90:  # Above 90
    print("Grade A")  # Top grade
elif math_marks >= 80:  # 80 to 90
    print("Grade B")  # Second grade
elif math_marks >= 70:  # 70 to 79
    print("Grade C")  # Third grade
else:  # Below 70
    print("Grade F")  # Fail grade
```

**How the code works:**

- Conditions are ordered from **highest threshold to lowest** — check `> 90` before `>= 80`.
- **Common mistake:** Putting `>= 70` before `> 90` — almost everyone would get Grade C.

---

## Key Takeaways

- **Conditional statements** (`if`, `elif`, `else`) let your program choose different actions based on whether a condition is `True` or `False`.
- **Comparison operators** (`==`, `>`, `<`, etc.) and **logical operators** (`and`, `or`, `not`) build the conditions inside `if` statements.
- **Indentation** and the **colon (`:`)** after every `if`, `elif`, and `else` line are mandatory Python syntax.
- You can **store boolean results** in variables like `result_for_english` and reuse them in later checks.
- **Think through the problem first**, then map each case to one branch — good logic beats memorising syntax.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| `if` | Runs a block only when a condition is `True` |
| `elif` | Checks another condition when previous ones are `False` |
| `else` | Runs when all preceding conditions are `False` |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators — return `True` or `False` |
| `and`, `or`, `not` | Logical operators — combine or reverse conditions |
| **Boolean** | Data type: `True` or `False` |
| **Condition** | An expression that evaluates to `True` or `False` |
| **Conditional statement** | `if`/`elif`/`else` structure controlling program flow |
| **Indentation** | Leading spaces defining code blocks in Python |
| **Colon (`:`)** | Required at the end of `if`, `elif`, and `else` lines |
| **Algorithmic thinking** | Breaking a problem into clear, testable steps |
| `int()` | Convert input text to a whole number for comparisons |
| `input()`, `print()` | Get user input and display output |
