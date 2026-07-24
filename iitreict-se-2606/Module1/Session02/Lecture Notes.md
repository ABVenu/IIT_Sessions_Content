# Operators & Conditional Statements

## What You Will Learn in This Lesson

In the previous lesson, you learned how to write Python programs in **OneCompiler** using **variables**, **data types**, **operators**, **expressions**, and basic **input/output**. Your programs could calculate marks, split bills, and show results — but they always followed the same straight path from top to bottom.

In this lesson, you will learn how to make your programs **think and choose**. You will use **conditional statements** (`if`, `elif`, `else`) to run different code depending on whether a condition is **True** or **False**. You will combine **comparison operators** and **boolean logic** (`and`, `or`, `not`) inside those conditions, practise **breaking word problems into testable steps**, and **trace execution paths** for sample inputs so you can debug confidently.

By the end, you will build single-branch and multi-branch programs that check exam results, apply discounts, validate user input, and handle multiple outcomes — the same decision-making pattern used in real apps and in the **agentic systems** you will design later in this course.

---

## Why Do Programs Need to Make Decisions?

- **Official Definition:** **Program flow control** is the ability of a program to change the order of execution based on conditions, rather than running every line in a fixed sequence.
- **In Simple Words:** Decision-making in code means the program picks what to do next — like choosing a different road at a fork.
- **Real-Life Example:** At a railway station, if your ticket is for Platform 3, you walk left; otherwise, you walk right. The platform number is the **condition**, and your direction is the **action**.

- **UPI apps** check your balance before allowing a payment — if balance is low, they show an error.
- **Exam result portals** display "Pass" or "Fail" based on marks.
- **ATMs** ask for your PIN — wrong PIN blocks withdrawal; correct PIN opens the menu.
- **AI agents** decide the next action based on rules — for example, if a request is incomplete, ask for more details; otherwise, continue the task.

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

```python
# Check scholarship eligibility: marks >= 80 AND attendance >= 75
marks = 88          # Marks out of 100
attendance = 82     # Attendance percentage
qualifies = (marks >= 80) and (attendance >= 75)  # Both conditions must be true
print(qualifies)  # Prints True because both conditions are met
```

**How the code works:**

- `and` requires **both** sides to be `True`.
- **Common mistake:** Using `=` instead of `==`. `marks = 80` assigns; `marks == 80` compares.

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

![if statement diagram — full voting eligibility code, syntax rules, True vs False paths, and step-by-step flow from input to output](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-03-if-statement-flow.png?v=20260614)

### `if` with User Input

```python
# Ask the user for their age and check voting eligibility (age 18+ in India)
age = int(input("Enter your age: "))  # Convert input text to a whole number
if age >= 18:  # Condition: is age 18 or above?
    print("You are eligible to vote.")  # Runs only when condition is True
```

**How the code works:**

- `int()` converts input text to a number before comparing.
- **Common mistake:** Forgetting `int()` — comparing `"20" >= 18` causes a `TypeError`.
- **Indentation** defines which lines belong to the `if` block. Wrong indentation causes an `IndentationError`.

### Quick Activity: Temperature Check

Write a program that asks for today's temperature in Celsius. If it is above 35, print a hot-weather warning.

```python
# Check if temperature is above 35 degrees Celsius
temperature = float(input("Enter temperature in Celsius: "))  # Allow decimal values
if temperature > 35:  # Condition: hotter than 35
    print("It is very hot today — stay hydrated!")  # Warning message
```

**How the code works:**

- `float()` handles decimal temperatures like 36.5.
- Run with 38 and 30 to see when the message appears vs when it does not.

An `if` handles "when true, do something." When the condition is false, `else` provides the alternative.

---

## The `else` Statement — What to Do When the Condition Is False

- **Official Definition:** An **`else` statement** runs when the `if` condition is `False`.
- **In Simple Words:** `else` means "otherwise, do this instead."
- **Real-Life Example:** "If the milk is boiled, turn off the gas; **else**, keep heating."

![if/else diagram — pass/fail decision tree with complete code for even/odd checker and modulus remainder explanation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-04-if-else-branches.png?v=20260614)

### Pass or Fail Program

```python
# Get marks and check pass or fail (passing marks = 40)
marks = int(input("Enter your marks out of 100: "))  # Convert input to integer
if marks >= 40:  # Marks 40 or above means pass
    print("Result: PASS")  # Student passed
else:  # Marks below 40
    print("Result: FAIL")  # Student failed
```

**How the code works:**

- Exactly **one** block runs — never both, never neither.
- `else` automatically covers everything the `if` did not catch.

### Even or Odd Number Checker

```python
# Check if a number is even using the modulus operator
number = int(input("Enter a whole number: "))  # Get number from user
if number % 2 == 0:  # Remainder 0 means even
    print(f"{number} is an even number.")  # Divisible by 2
else:  # Remainder is 1
    print(f"{number} is an odd number.")  # Not divisible by 2
```

**How the code works:**

- `number % 2` gives the remainder when divided by 2 — very useful for divisibility checks.

Many problems have **more than two** outcomes — like exam grades. That is what `elif` is for.

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

### Grade Calculator

```python
# Assign grade based on marks range
marks = int(input("Enter marks out of 100: "))  # Get marks as integer
if marks >= 90:  # 90 to 100
    print("Grade: A — Outstanding!")  # Top grade
elif marks >= 75:  # 75 to 89
    print("Grade: B — Very Good!")  # Second grade
elif marks >= 60:  # 60 to 74
    print("Grade: C — Good")  # Third grade
elif marks >= 40:  # 40 to 59
    print("Grade: D — Needs improvement")  # Pass grade
else:  # Below 40
    print("Grade: F — Failed")  # Fail grade
```

**How the code works:**

- If marks is 95, only "Grade: A" prints — remaining conditions are skipped.
- **Common mistake:** Putting `marks >= 40` before `marks >= 90` — almost everyone would get Grade D.

### Quick Activity: Electricity Bill Slab

An electricity board charges ₹5/unit for the first 100 units, ₹7/unit for 101–200, and ₹10/unit beyond 200. Write a program that asks for units consumed and prints the billing slab.

```python
# Determine billing slab based on units consumed
units = int(input("Enter total units consumed: "))  # Total electricity units
if units <= 100:  # First slab: up to 100 units
    print("Slab: First 100 units — rate ₹5 per unit")  # Lowest rate
elif units <= 200:  # Second slab: 101 to 200 units
    print("Slab: 101 to 200 units — rate ₹7 per unit")  # Middle rate
else:  # Above 200 units
    print("Slab: Above 200 units — rate ₹10 per unit")  # Highest rate
```

**How the code works:**

- `elif units <= 200` only runs when the first condition was `False`, so it means 101 to 200.
- Categorising input into ranges is one of the most common uses of `elif`.

### Train Ticket Category by Age

```python
# Determine train ticket type based on passenger age
age = int(input("Enter passenger age: "))  # Age in years
if age < 5:  # Children under 5
    print("Ticket: FREE (child under 5)")  # No ticket needed
elif age <= 12:  # Children aged 5 to 12
    print("Ticket: CHILD (half fare)")  # Discounted child ticket
elif age < 60:  # Adults aged 13 to 59
    print("Ticket: ADULT (full fare)")  # Standard fare
else:  # Senior citizens 60+
    print("Ticket: SENIOR CITIZEN (senior discount)")  # Senior discount
```

**How the code works:**

- Each `elif` handles one age range. Trace ages **4**, **12**, **30**, and **60** to confirm which branch runs.

---

## Combining Logical Operators Inside Conditions

Use `and`, `or`, and `not` directly inside `if` conditions when one check is not enough.

### Scholarship and Discount Examples

```python
# Example 1: and — both conditions must be True
marks = int(input("Enter marks: "))                # Get marks
attendance = int(input("Enter attendance %: "))    # Get attendance
if (marks >= 80) and (attendance >= 75):           # Both must pass
    print("You are eligible for the scholarship!") # Granted
else:  # Scholarship criteria not met
    print("Sorry, you do not meet the scholarship criteria.")  # Not eligible

# Example 2: or — at least one condition must be True
amount = float(input("Enter purchase amount in rupees: "))       # Bill amount
has_membership = input("Do you have a membership card? (yes/no): ")  # Membership
if (amount > 1000) or (has_membership == "yes"):  # Either condition gives discount
    discount = amount * 0.20           # 20% discount
    final_amount = amount - discount     # Price after discount
    print(f"Discount applied! You pay ₹{final_amount}")  # Discounted price
else:  # No discount applies
    print(f"No discount. You pay ₹{amount}")  # Full price
```

**How the code works:**

- `and` — both sides must be `True`. `or` — at least one side must be `True`.
- `not` flips `True` to `False` — useful when you want the opposite check.

![Logical operators in conditions — complete scholarship, discount, and login examples with full truth table and parentheses readability tip](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-06-logical-operators.png?v=20260614)

### Using `not` — Reversing a Condition

```python
# Allow login only when account is NOT locked
is_locked = False  # False means account is active
if not is_locked:  # not False becomes True — account is open
    print("Login successful! Welcome back.")  # User can log in
else:  # Account is locked
    print("Account is locked. Contact support.")  # Block access
```

**How the code works:**

- `not is_locked` is `True` when `is_locked` is `False`.
- Parentheses around comparisons in complex conditions make code easier to read.

---

## Nested Conditionals — Decisions Inside Decisions

- **Official Definition:** A **nested conditional** is an `if` block placed inside another `if` block.
- **In Simple Words:** Check a second condition only after the first one passes.
- **Real-Life Example:** "If you have a ticket, enter the stadium. If you also have a VIP pass, go to the premium stand."

### Login with Username and Password

```python
# Correct credentials (in real apps, stored securely in a database)
correct_username = "student01"  # Expected username
correct_password = "pass1234"   # Expected password

# Get login details and validate
username = input("Enter username: ")  # User types username
password = input("Enter password: ")  # User types password
if username == correct_username:    # Outer check: username
    if password == correct_password:  # Inner check: password
        print("Login successful! Welcome.")  # Both correct
    else:  # Password did not match
        print("Wrong password. Please try again.")  # Username OK, password wrong
else:  # Username did not match
    print("Username not found.")  # Username wrong
```

**How the code works:**

- The inner `if` only runs when the username is correct — different error messages for each failure.
- If nesting goes deeper than 2–3 levels, rewrite with `and`/`or` or `elif` for readability.

![Nested conditionals — full login validation flowchart with complete username/password code and separate error messages for each failure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-07-nested-conditionals.png?v=20260614)

---

## Common Mistakes with Conditionals

| Mistake | Wrong Code | Correct Code | Why It Fails |
|---------|-----------|--------------|--------------|
| Using `=` instead of `==` | `if marks = 50:` | `if marks == 50:` | `=` assigns; `==` compares |
| Forgetting the colon | `if marks >= 40` | `if marks >= 40:` | Python expects `:` |
| Wrong indentation | No indent after `if` | Indent with 4 spaces | Python cannot find the block |
| String vs number | `age == 18` when age is `"18"` | `int(age) == 18` | Different types |
| Wrong `elif` order | `>= 40` before `>= 90` | Put `>= 90` first | Higher threshold first |
| Empty `if` block | Nothing below `if` | Use `pass` or real code | Python disallows empty blocks |

![Common conditional mistakes — all six errors with wrong code, correct code, reason, and debugging tips for boundary values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-09-common-mistakes.png?v=20260614)

Use **`pass`** as a temporary placeholder inside an empty `if` block while you build structure — replace it with real code when ready.

---

## Logical Thinking — Breaking Word Problems Into Steps

- **Official Definition:** **Algorithmic thinking** is defining clear, ordered steps to solve a problem, where each step can be tested independently.
- **In Simple Words:** Read the word problem, list the rules in plain English, then write code.
- **Real-Life Example:** Making chai — boil water, add tea, add milk, add sugar. Order matters, just like in code.

### The STEP Method

1. **S — State** the word problem in plain English (one or two sentences).
2. **T — Identify inputs** the program needs from the user.
3. **E — List conditions and outcomes** for each case (what happens when True / False).
4. **P — Write Python code** following step 3 — then trace with sample inputs.

![STEP method — State, inputs, conditions/outcomes, and Python code with full cinema ticket example and complete working program](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session02/session02-08-step-method.png?v=20260614)

**Example:** Cinema charges ₹150 for adults, ₹80 for children (age 12 or below).

```python
# STEP: input = age; if age <= 12 → ₹80, else → ₹150
age = int(input("Enter your age: "))  # Input: age
if age <= 12:  # Child ticket
    print(f"Child ticket: ₹80")  # Price for age 12 and below
else:  # Adult ticket
    print(f"Adult ticket: ₹150")  # Price for age 13 and above
```

**How the code works:**

- Each condition from step E maps directly to an `if` or `else` block.
- Apply STEP before every conditional program — good logic beats memorising syntax.

### Quick Activity: Shop Discount

A shop gives 10% off when the bill is above ₹500. Write the STEP breakdown first, then code it.

```python
# Apply 10% discount if bill exceeds ₹500
bill = float(input("Enter bill amount in rupees: "))  # Total purchase amount
if bill > 500:  # Qualifies for discount
    discount = bill * 0.10  # 10% off
    final_bill = bill - discount  # Amount after discount
    print(f"Discount applied! You pay ₹{final_bill}")  # Discounted total
else:  # No discount
    print(f"No discount. You pay ₹{bill}")  # Full amount
```

**How the code works:**

- `bill` is available in both branches — do not use a variable created only inside the `if` block in the `else` block.

---

## Practice Programs — Beginner Conditional Exercises

Work through each program in OneCompiler. Type the code yourself, then **trace** with different inputs before you trust the output.

### Exercise 1: Simple ATM Withdrawal

```python
# Withdraw money with balance and input validation
balance = 5000  # Current balance in rupees
withdraw_amount = int(input("Enter amount to withdraw: "))  # Amount to withdraw
if withdraw_amount > balance:  # Not enough money
    print("Insufficient balance. Transaction failed.")  # Reject
elif withdraw_amount <= 0:  # Invalid amount
    print("Invalid amount. Please enter a positive number.")  # Reject
else:  # Valid withdrawal
    balance = balance - withdraw_amount  # Deduct amount
    print(f"Withdrawal successful! Remaining balance: ₹{balance}")  # Show new balance
```

**How the code works:**

- Check failure cases first (insufficient balance, invalid amount), then process valid withdrawals.
- Trace with **6000**, **0**, and **2000** — predict the branch before running.

### Exercise 2: Complete Student Result Program

```python
# Collect student data
student_name = input("Enter student name: ")               # Name
maths = int(input("Enter Maths marks: "))                  # Maths marks
science = int(input("Enter Science marks: "))              # Science marks
english = int(input("Enter English marks: "))              # English marks
attendance = int(input("Enter attendance percentage: "))  # Attendance %

# Calculate totals
total = maths + science + english  # Sum of all subjects
average = total / 3                # Average marks
passed_all = (maths >= 40) and (science >= 40) and (english >= 40)  # All subjects passed?

# Display summary
print("----- Result -----")  # Heading
print(f"Name: {student_name}")  # Name
print(f"Total: {total}")        # Total marks
print(f"Average: {average:.1f}")  # Average rounded to 1 decimal

# Overall result with nested division assignment
if passed_all and (attendance >= 75):  # Pass requires all subjects + 75% attendance
    print("Result: PASS")  # Student passed
    if average >= 75:  # First division
        print("Division: First")
    elif average >= 60:  # Second division
        print("Division: Second")
    else:  # Third division
        print("Division: Third")
else:  # Failed
    print("Result: FAIL")  # Did not meet requirements
    if not passed_all:
        print("Reason: Failed in one or more subjects.")  # Subject failure
    if attendance < 75:
        print("Reason: Attendance below 75%.")  # Attendance failure
```

**How the code works:**

- Combines `input()`, arithmetic, comparison, logical operators, `elif`, and nested `if`.
- The `else` block explains **why** the student failed.
- Trace with sample inputs: all pass + 80% attendance; one subject fail; attendance 70%.

---

## Tracing Execution Paths — Follow What Python Does

Before you write more code, learn to **trace** — walk through the program with a sample input and mark which branch runs. This habit catches most conditional bugs faster than guessing.

- **Official Definition:** **Tracing** means following the program line by line for a chosen input and recording which conditions become `True` or `False` and which block executes.
- **In Simple Words:** Pretend you are Python. Take one input value, check each condition in order, and note the path you take.
- **Real-Life Example:** Like following a metro map — for your destination, you mark which stations you pass and which lines you skip.

### Trace Table for a Grade Program

Use this table when you test `elif` chains. Fill one row per sample input.

| Sample marks | `>= 90`? | `>= 75`? | `>= 60`? | `>= 40`? | Branch that runs | Output |
|--------------|----------|----------|----------|----------|------------------|--------|
| 95 | True | — | — | — | First `if` | Grade A |
| 78 | False | True | — | — | First `elif` | Grade B |
| 55 | False | False | False | True | Third `elif` | Grade D |
| 30 | False | False | False | False | `else` | Grade F |

**Boundary values matter:** Always test the exact cut-off (for example **40** for pass/fail and **90** for Grade A). Off-by-one mistakes often hide at the boundary.

### Quick Activity: Trace Before You Run

For the cinema ticket program (`age <= 12` → ₹80, else → ₹150), mentally fill the path for ages **10**, **12**, and **13**. Then run the program in OneCompiler and confirm your predicted outputs match.

```python
# Trace this with ages 10, 12, and 13 before running
age = int(input("Enter your age: "))  # Sample inputs: 10, 12, 13
if age <= 12:  # True for 10 and 12; False for 13
    print("Child ticket: ₹80")  # Runs when age is 12 or below
else:  # Runs when age is 13 or above
    print("Adult ticket: ₹150")  # Adult fare
```

**How the code works:**

- Age **12** is the boundary — it must take the child path because of `<=`.
- If your prediction and the output disagree, check the operator (`<` vs `<=`) first.

---

## Debugging Conditional Programs

- **Print the condition:** Add `print(marks >= 40)` before the `if` to see `True` or `False`.
- **Check data types:** Use `print(type(variable))` — compare numbers with numbers, not strings.
- **Trace sample inputs:** Test boundary values like 39, 40, and 90 for pass/grade programs.
- **Read indentation:** Wrong block running usually means indentation is off.
- **Check `elif` order:** Same grade for everyone means conditions are in the wrong order.

```python
# Debug tip: print the condition result before the if block
marks = int(input("Enter marks: "))  # Get marks
print("Condition result:", marks >= 40)  # Remove this line after debugging
if marks >= 40:  # Check passing marks
    print("PASS")  # Passed
else:  # Marks below passing threshold
    print("FAIL")  # Failed
```

---

## Key Takeaways

- **Conditional statements** (`if`, `elif`, `else`) let your program choose different actions based on whether a condition is `True` or `False`.
- **Comparison operators** (`==`, `>`, `<`, etc.) and **logical operators** (`and`, `or`, `not`) build the conditions inside `if` statements.
- **Indentation** defines code blocks in Python — always indent `if`, `elif`, and `else` bodies with 4 spaces.
- The **STEP method** and **execution tracing** help you think clearly before and after typing — good logic beats memorising syntax.
- These decision-making skills prepare you for **loops** in upcoming lessons, and later for the rule-based choices inside **agentic systems**.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| `if` | Runs a block only when a condition is `True` |
| `elif` | Checks another condition when previous ones are `False` |
| `else` | Runs when all preceding conditions are `False` |
| `pass` | Placeholder for an empty block |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators — return `True` or `False` |
| `and`, `or`, `not` | Logical operators — combine or reverse conditions |
| **Boolean** | Data type: `True` or `False` |
| **Condition** | An expression that evaluates to `True` or `False` |
| **Conditional statement** | `if`/`elif`/`else` structure controlling program flow |
| **Indentation** | Leading spaces defining code blocks in Python |
| **Nested conditional** | An `if` inside another `if` block |
| **Algorithmic thinking** | Breaking a problem into clear, testable steps |
| **Execution tracing** | Following conditions True/False for a sample input to see which branch runs |
| `int()`, `float()` | Convert input to numbers for comparisons |
| `input()`, `print()` | Get user input and display output |
| `%` (modulus) | Remainder after division — useful for even/odd checks |
| **Colon (`:`)** | Required at the end of `if`, `elif`, and `else` lines |
