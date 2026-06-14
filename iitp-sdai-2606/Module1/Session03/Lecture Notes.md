# Loops & Iterations in Python

## What You Will Learn in This Lesson

You have already learned how to write Python programs using **variables**, **operators**, **input/output**, and **conditional statements** (`if`, `elif`, `else`). Your programs could make decisions — check marks, apply discounts, and validate input — but each instruction still ran only **once** from top to bottom.

In this lesson, you will learn how to **repeat actions automatically**. You will use **`while` loops** and **`for` loops** to run the same logic many times without copying code. You will also learn **`break`** and **`continue`** to control when a loop stops or skips a round.

By the end, you will be able to print tables, validate input until it is correct, process lists of marks or prices, and break big problems into small testable steps — the same skills real apps use when they handle hundreds of users or transactions.

---

## Why Do Programs Need to Repeat Actions?

- **Official Definition:** A **loop** (or **iteration**) is a control structure that executes a block of code repeatedly until a condition is no longer met or every item in a sequence has been processed.
- **In Simple Words:** A loop tells Python, "Do this again and again" instead of writing the same line ten or hundred times.
- **Real-Life Example:** At a temple prasad counter, the volunteer gives one laddu to **each person** in the queue. The action repeats for every person — that is a loop in real life.

- **UPI apps** may retry a failed payment check several times before showing an error.
- **Train ticket apps** loop through every seat to show which ones are available.
- **Exam result systems** loop through every student's marks to calculate pass or fail.

Without loops, you would copy-paste the same code for every student, every item, or every retry. Loops make programs **scalable and clean**.

![Loops big picture — temple prasad queue analogy, while vs for comparison, break and continue summary, and real app examples like UPI retries and exam result systems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-01-loops-big-picture.png?v=20260614-ai)

---

## Understanding Loops — The Big Picture

| Loop Type | Best When | Simple Idea |
|-----------|-----------|-------------|
| **`while` loop** | You repeat **until a condition changes** | "Keep doing this **while** something is true." |
| **`for` loop** | You repeat **for each item** in a known list or count | "Do this **for every** student / number / letter." |

- **`break`** — stop the loop **immediately** (like finding your keys and stopping the search).
- **`continue`** — skip **this round only** and move to the next (like skipping one bad apple but still packing the rest).

Conditionals decide **what** to do; loops decide **how many times** to do it. Together, they let you build programs that think **and** repeat.

---

## The `while` Loop — Repeat While a Condition Is True

- **Official Definition:** A **`while` loop** repeatedly executes a block of code as long as its condition evaluates to `True`. The condition is checked **before** each repetition.
- **In Simple Words:** `while` means "keep going until the check fails."
- **Real-Life Example:** "While the traffic light is red, wait." You keep waiting until the light turns green — the condition changes.

### Basic Syntax and Rules

```python
while condition:  # Condition checked before each round — must end with a colon
    # Indented code runs again and again while condition is True
    # Something inside must eventually make condition False
```

- Start with `while`, then the **condition**, then a **colon `:`**.
- Indented lines are the **loop body** — they repeat while the condition is `True`.
- **Critical rule:** Something inside the loop must **change** so the condition can eventually become `False`. Otherwise you get an **infinite loop** — the program runs forever because the condition never becomes `False`.

![while loop diagram — counter 1 to 5 code, password validation use case, syntax rules, infinite loop warning, and step-by-step condition check flow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-02-while-loop.png?v=20260614-ai)

### Example: Count from 1 to 5

```python
count = 1  # Start the counter at 1
while count <= 5:  # Condition: keep going while count is 5 or less
    print(count)  # Print the current number
    count = count + 1  # Increase count by 1 so the loop can eventually stop
```

**How the code works:**

- Each round prints `count`, then adds 1. When `count` becomes 6, condition `6 <= 5` is `False` and the loop stops.
- **Common mistake:** Forgetting `count = count + 1` — the loop prints `1` forever.

### Example: Password Validation (Repeat Until Input Is Valid)

```python
password = ""  # Start with an empty password so the loop runs at least once
while len(password) < 8:  # Condition: password must be at least 8 characters long
    password = input("Enter password (minimum 8 characters): ")  # Ask user again
print("Password accepted!")  # This line runs only after the loop ends
```

**How the code works:**

- `len(password)` returns the number of characters in the text.
- The loop keeps asking until the user types 8 or more characters — ideal when you do not know how many tries are needed.

### Quick Activity: Savings Goal Tracker

A student saves ₹500 every month. Write a program that starts with ₹0 and adds ₹500 each round until the total reaches at least ₹5000, printing the balance after each month.

```python
balance = 0  # Starting savings in rupees
monthly_saving = 500  # Amount saved each month
while balance < 5000:  # Keep saving while total is below the goal
    balance = balance + monthly_saving  # Add this month's saving
    print("Current balance: ₹", balance)  # Show progress after each month
print("Goal reached! Final balance: ₹", balance)  # Message after loop ends
```

**How the code works:**

- Each round adds ₹500 and prints the new balance. After 10 rounds, `balance` is 5000 → condition `5000 < 5000` is `False` → loop stops.

Now that you understand repeating **while a condition holds**, the next tool handles repeating **for each item** in a collection — that is the **`for` loop**.

---

## The `for` Loop — Repeat for Each Item in a Sequence

- **Official Definition:** A **`for` loop** iterates over each element in a **sequence** (such as a string, list, or range of numbers) and executes the loop body once per element.
- **In Simple Words:** `for` means "do this once for every item in the list."
- **Real-Life Example:** A teacher calls roll — "For each name on the list, mark present or absent." One instruction covers every student.

### Basic Syntax

```python
for item in sequence:  # item takes each value from sequence, one at a time
    # Indented code runs once per item
```

- `item` is a variable name — you can choose any valid name (`student`, `mark`, `fruit`).
- Python automatically moves to the **next** item after each round — no manual counter needed for simple cases.

### Example: Print Each Fruit in a List

```python
fruits = ["mango", "banana", "apple"]  # A list of three fruit names
for fruit in fruits:  # fruit takes each list item one by one
    print("Today's fruit:", fruit)  # Print a message for each fruit
```

**How the code works:**

- The loop body runs three times with `fruit` equal to `"mango"`, then `"banana"`, then `"apple"`.
- **Common mistake:** Expecting `print(fruit)` outside the loop to print all fruits — it only prints the **last** value.

### Quick Activity: Class Attendance Counter

Given a list of attendance statuses, count how many students are present.

```python
attendance = ["present", "absent", "present", "present", "absent"]  # Five students
present_count = 0  # Counter starts at zero
for status in attendance:  # Check each student's status
    if status == "present":  # Condition from your previous learning
        present_count = present_count + 1  # Increase count when present
print("Total present:", present_count)  # Print final count after loop ends
```

**How the code works:**

- Combines a **`for` loop** with an **`if` statement** — a pattern you will use often. Output: `Total present: 3`.

To count numbers (1 to 10, table rows, etc.), Python provides a helper called **`range()`**.

---

## The `range()` Function — Counting Made Easy

- **Official Definition:** The **`range()`** function generates a sequence of integers, commonly used with `for` loops to repeat a block a specific number of times.
- **In Simple Words:** `range()` gives you numbers one by one — like a token counter at a bank that calls 1, 2, 3… without writing each number yourself.
- **Real-Life Example:** A cricket over has 6 balls — `range(1, 7)` gives you ball numbers 1 through 6.

### Three Forms of `range()`

| Form | Meaning | Example Output |
|------|---------|----------------|
| `range(stop)` | From 0 up to **stop − 1** | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, stop)` | From **start** up to **stop − 1** | `range(2, 7)` → 2, 3, 4, 5, 6 |
| `range(start, stop, step)` | From **start** to **stop − 1**, jumping by **step** | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

- **`range()` stops before the second number** — `range(5)` does **not** include 5.
- **Common mistake:** Writing `range(1, 5)` when you want 1 to 5 inclusive — you need `range(1, 6)`.

![for loop and range diagram — fruit list iteration, three range() forms with examples, multiplication table code, and common off-by-one mistakes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-03-for-loop-range.png?v=20260614-ai)

### Example: Print Numbers 1 to 5

```python
for num in range(1, 6):  # Generates 1, 2, 3, 4, 5 (stops before 6)
    print(num)  # Prints each number on its own line
```

**How the code works:**

- `range(1, 6)` produces 1 through 5. `num` automatically gets the next number each round — no manual counter needed.

### Quick Activity: Multiplication Table for 7

Print the table of 7 from `7 × 1` to `7 × 10`.

```python
number = 7  # The number whose table we want
for i in range(1, 11):  # Multipliers 1 through 10
    result = number * i  # Multiply 7 by the current multiplier
    print(number, "x", i, "=", result)  # Print one line of the table
```

**How the code works:**

- One small loop replaces ten separate `print` statements. Change `number = 7` to print any other table.

---

## Choosing the Right Loop — `for` vs `while`

- **Official Definition:** **Loop selection** is the practice of picking the loop type whose condition model best matches the problem — counting over a sequence versus repeating until a state changes.
- **In Simple Words:** Ask yourself: "Do I know **how many times** or **what items**?" → use `for`. "Do I repeat **until something happens**?" → use `while`.
- **Real-Life Example:** Printing a fixed menu of 5 thali items is a **`for`** job. Waiting until the cooker whistle blows is a **`while`** job.

| Situation | Use | Reason |
|-----------|-----|--------|
| Print table of 10 rows | `for` with `range()` | You know exactly how many rounds |
| Process every mark in a list | `for` over the list | You have a collection to visit |
| Ask password until 8+ characters | `while` | Repeat until condition is met |
| Menu until user types "quit" | `while True` + `break` | Exit only on a special command |

![for vs while decision guide — situation table with recommended loop type, side-by-side count 0 to 4 code, and thali menu vs cooker whistle analogy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-04-for-vs-while.png?v=20260614-ai)

```python
# Using for — cleaner when you know the count
for i in range(5):  # range(5) gives 0, 1, 2, 3, 4
    print(i)  # Print each number

# Using while — you manage the counter yourself
count = 0  # Start counter at 0
while count < 5:  # Condition: less than 5
    print(count)  # Print current count
    count = count + 1  # Move to next number
```

**How the code works:**

- Both print 0, 1, 2, 3, 4. Prefer **`for`** when counting or iterating a sequence; prefer **`while`** when exit depends on **changing conditions** or user input.

Sometimes you need to **stop early** or **skip one round** — that is where **`break`** and **`continue`** help.

---

## The `break` Statement — Stop the Loop Early

- **Official Definition:** The **`break` statement** immediately terminates the innermost loop that contains it and transfers control to the first statement after that loop.
- **In Simple Words:** `break` means "stop the loop right now — we are done."
- **Real-Life Example:** You find your Aadhaar card in the second drawer — you **stop searching** the remaining drawers.

### Example: Menu Until User Quits

```python
while True:  # Loop runs forever until break stops it
    command = input("Type a command (type quit to exit): ")  # Read user input
    if command == "quit":  # Check if user wants to stop
        break  # Exit the loop immediately
    print("Running command:", command)  # Runs only if user did not type quit
print("Goodbye!")  # Runs after break — outside the loop
```

**How the code works:**

- `while True` creates a loop that would run forever without `break`. When the user types `"quit"`, `break` jumps out.
- **Pattern:** `while True` + `break` is common for menus and games.

### Example: Find a Number in a List (Stop When Found)

```python
numbers = [3, 7, 12, 9, 5]  # List of numbers to search
target = 12  # Number we are looking for
for num in numbers:  # Check each number one by one
    if num == target:  # Found a match
        print("Found", target)  # Report success
        break  # Stop searching — no need to check remaining items
```

**How the code works:**

- Without `break`, the loop would check every number even after finding 12. **`break` saves time** when you only need the first match.

---

## The `continue` Statement — Skip One Round and Keep Going

- **Official Definition:** The **`continue` statement** skips the remaining statements in the current loop iteration and proceeds to the next iteration of the loop.
- **In Simple Words:** `continue` means "skip this round, but keep the loop running."
- **Real-Life Example:** While packing tiffin boxes, you skip one spoiled roti but continue packing the rest — you do not stop the whole kitchen.

| Statement | Effect | Analogy |
|-----------|--------|---------|
| **`break`** | Exits the **entire** loop | Stop the search completely |
| **`continue`** | Skips **this iteration only** | Skip one bad item, keep going |

![break and continue diagram — effect comparison table, while True menu with break, odd numbers with continue, search early exit, and infinite loop caution](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-05-break-continue.png?v=20260614-ai)

### Example: Print Only Odd Numbers from 1 to 10

```python
for num in range(1, 11):  # Numbers 1 through 10
    if num % 2 == 0:  # If number is even (remainder 0 when divided by 2)
        continue  # Skip even numbers — go to next num
    print(num)  # Runs only for odd numbers: 1, 3, 5, 7, 9
```

**How the code works:**

- `%` gives the remainder — `num % 2 == 0` means even. `continue` skips the `print` for even numbers but keeps checking the rest.
- **In `while` loops:** Put counter updates **before** `continue`, or you may accidentally create an infinite loop.

### Example: Grade Every Student in a List

```python
marks_list = [92, 35, 78, 44, 88]  # Marks for five students
for marks in marks_list:  # Check each student's marks
    if marks >= 40:  # Passing condition
        print(marks, "→ PASS")  # Student passed
    else:  # Marks below 40
        print(marks, "→ FAIL")  # Student failed
```

**How the code works:**

- The **loop** handles repetition; the **conditional** handles the pass/fail decision. One loop replaces five separate `if` blocks.

---

## Automating Repetitive Tasks with Loops

- **Official Definition:** **Automation through iteration** means using loops to perform the same operation on many inputs or for many steps, reducing manual duplication and human error.
- **In Simple Words:** Write the logic once; let the loop apply it everywhere.
- **Real-Life Example:** A photocopy machine repeats the same print action for 50 pages — you do not draw each page by hand.

![Automation and accumulator pattern — shopping bill total code, four-step accumulator flow, counter pattern example, and average-outside-loop warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-06-automation-accumulator.png?v=20260614-ai)

### Example: Calculate Total Bill for a Shopping List

```python
prices = [120, 85, 250, 40, 199]  # Price of each item in rupees
total_bill = 0  # Bill starts at zero
for price in prices:  # Loop through each item price
    total_bill = total_bill + price  # Add current price to running total
print("Total bill: ₹", total_bill)  # Print final amount after all items
```

**How the code works:**

- Works for 5 items or 500 items — same loop structure. **Pattern name:** **accumulator** — start with 0, add each value in the loop.

---

## Iterative Thinking — Breaking Problems into Testable Parts

- **Official Definition:** **Iterative problem solving** is the approach of decomposing a problem into smaller steps, solving each step, and testing before combining them — often using loops to handle repeated sub-steps.
- **In Simple Words:** Do not solve the whole puzzle at once — solve one piece, check it, then move to the next.
- **Real-Life Example:** Preparing for board exams — you revise one chapter, test yourself with questions, then move to the next chapter instead of reading the entire book in one sitting.

### The LOOP Method for Problem Solving

| Step | Meaning | Example (Find average of marks) |
|------|---------|----------------------------------|
| **L — List the goal** | What should the program output? | Print average of five marks |
| **O — Observe the repetition** | What repeats? | Add each mark to a total |
| **O — Outline the loop** | `for` or `while`? Over what? | `for mark in marks_list:` |
| **P — Process inside the loop** | What happens each round? | `total = total + mark` |

After the loop, handle **one-time** steps (like dividing total by count) **outside** the loop.

![LOOP method for problem solving — List goal, Observe repetition, Outline loop, Process inside loop with average marks calculator code example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-07-loop-method.png?v=20260614-ai)

### Worked Example: Average Marks Calculator

**Problem:** Given marks `[80, 65, 90, 72, 88]`, find and print the average.

```python
marks = [80, 65, 90, 72, 88]  # Five test scores
total = 0  # Running sum
for mark in marks:  # Add each mark
    total = total + mark  # Accumulate total
count = len(marks)  # Number of students — len() returns list length
average = total / count  # Divide total by count — outside the loop
print("Average marks:", average)  # Prints 79.0
```

**How the code works:**

- **Test in parts:** First confirm `total` is 395, then add the division step outside the loop.
- **`len(marks)`** counts how many items are in the list. **Common mistake:** Calculating `average` **inside** the loop — that recomputes average every round instead of once at the end.

---

## Practice Exercises

Work through these on your own online compiler. Test with different inputs to build confidence.

### Exercise 1: Sum of First N Natural Numbers

Ask the user for `n`, then use a loop to find 1 + 2 + 3 + … + n.

```python
n = int(input("Enter a positive number: "))  # Get upper limit from user
total = 0  # Running sum starts at zero
for num in range(1, n + 1):  # Loop from 1 to n inclusive
    total = total + num  # Add current number to total
print("Sum from 1 to", n, "is:", total)  # Print final result
```

**How the code works:**

- **`total`** accumulates the sum inside the loop using the **accumulator** pattern.

### Exercise 2: Valid PIN Entry (While Loop)

Keep asking for a 4-digit PIN until the user enters exactly `"1234"`. Print "Access granted" when correct.

```python
pin = ""  # Start with empty PIN so loop runs at least once
while pin != "1234":  # Repeat until correct PIN is entered
    pin = input("Enter 4-digit PIN: ")  # Read user input as text
print("Access granted")  # Runs only after correct PIN
```

**How the code works:**

- Compare PIN as **text** (`"1234"`) — no `int()` needed because leading zeros would break numeric comparison.

### Exercise 3: First Failing Mark (Use `break`)

Given marks `[78, 82, 35, 90, 88]`, print "Fail found" and stop when you hit the first mark below 40.

```python
marks = [78, 82, 35, 90, 88]  # Student marks list
for mark in marks:  # Check marks in order
    if mark < 40:  # First failing mark
        print("Fail found:", mark)  # Report the failing mark
        break  # Stop checking remaining marks
```

**How the code works:**

- The loop stops at the **first** fail because **`break`** exits immediately — marks after 35 are never checked.

---

## Debugging Loop Programs

- **Print the loop variable:** Add `print(i)` inside the loop to see how values change each round.
- **Check off-by-one errors:** If you wanted 1 to 10 but got 1 to 9, your `range()` stop value is probably one too small.
- **Watch infinite loops:** If the program never stops, verify the variable in the `while` condition is **updated** inside the loop.
- **Trace with small data:** Test with 2 or 3 items first before large lists.
- **Place `break`/`continue` carefully:** They affect only the loop they sit inside.

---

## Key Takeaways

- **`while` loops** repeat code as long as a condition is `True` — ideal when you do not know how many tries you need (validation, guessing games, menus).
- **`for` loops** visit each item in a sequence or each number from **`range()`** — ideal when you know what to iterate over or how many times to count.
- **`break`** stops a loop early; **`continue`** skips one iteration and keeps going — use them to search faster or filter items without messy nested logic.
- **Iterative thinking** means breaking problems into small testable steps — build the loop first, verify the total or count, then add final calculations outside the loop.
- These skills prepare you for **lists, strings, and functions**, where loops become even more powerful for processing real data.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **`while`** | Repeats a block while a condition is `True` |
| **`for`** | Repeats a block once for each item in a sequence |
| **`break`** | Exits the current loop immediately |
| **`continue`** | Skips the rest of the current iteration; loop continues |
| **`range(stop)`** | Generates numbers from 0 to stop − 1 |
| **`range(start, stop)`** | Generates numbers from start to stop − 1 |
| **`range(start, stop, step)`** | Generates numbers with a custom step (can count down) |
| **`len()`** | Returns the number of items in a sequence |
| **Loop / Iteration** | Repeating a block of code multiple times |
| **Infinite loop** | A loop that never ends because its condition never becomes `False` |
| **Accumulator** | A variable (often starting at 0) that builds a total inside a loop |
| **Counter** | A variable that increases each iteration to track count |
| **`while True`** | A loop that runs until `break` stops it — common for menus |
| **Automation** | Using loops to apply the same logic to many inputs without duplicating code |
| **Iterative problem solving** | Breaking a problem into repeated, testable steps |
