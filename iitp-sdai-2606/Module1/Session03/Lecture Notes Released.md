# Loops & Iterations in Python

## What You Will Learn in This Lesson

You have already learned how to write Python programs using **variables**, **operators**, **input/output**, and **conditional statements** (`if`, `elif`, `else`). Your programs could make decisions — check marks, apply discounts, and validate input — but each instruction still ran only **once** from top to bottom.

In this lesson, you will learn how to **repeat actions automatically**. You will use **`while` loops** and **`for` loops** to run the same logic many times without copying code. You will also learn **`break`** and **`continue`** to control when a loop stops or skips a round.

By the end, you will be able to print number patterns, take repeated user input, calculate totals and averages, and break big problems into small testable steps — the same skills real apps use when they handle many users or transactions.

---

## Why Do Programs Need to Repeat Actions?

- **Official Definition:** A **loop** (or **iteration**) is a control structure that executes a block of code repeatedly until a condition is no longer met or every item in a sequence has been processed.
- **In Simple Words:** A loop tells Python, "Do this again and again" instead of writing the same line ten or hundred times.
- **Real-Life Example:** At a temple prasad counter, the volunteer gives one laddu to **each person** in the queue. The action repeats for every person — that is a loop in real life.

- Copy-pasting `print("Hello")` ten times works once, but printing it 100 times makes code hard to read and easy to break.
- **Exam result systems** loop through every student's marks to calculate pass or fail.
- **ATM machines** may ask for your PIN again and again until you enter the correct one.

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
- **Real-Life Example:** At an ATM, you enter your PIN until it is correct. You do not know how many tries you need — the loop keeps going **while** the PIN is wrong.

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

### Python Increment Syntax — Important Rule

- Python does **not** support `count++` or `count--` like C++ or Java.
- Always write **`count = count + 1`** to increase a counter, or use shorthand **`count += 1`**.
- To decrease a counter, use **`count -= 1`** (useful when counting down in a `while` loop).

### Infinite Loops — What Goes Wrong

An **infinite loop** happens when the `while` condition stays `True` forever — usually because you forgot to update the counter inside the loop.

```python
c = 1  # Counter starts at 1
while c <= 5:  # Condition is True at first
    print("Hello")  # Prints Hello again and again
    # Missing: c = c + 1  — c stays 1 forever!
```

**How the code works:**

- Because `c` never increases, `c <= 5` stays `True` and the loop never stops.
- **Always dry-run** your loop: trace the variable value round by round on paper before running large programs.

Now that you understand repeating **while a condition holds**, the next tool handles repeating **for each item** in a collection — that is the **`for` loop**.

---

## The `for` Loop — Repeat for Each Item in a Sequence

- **Official Definition:** A **`for` loop** iterates over each element in a **sequence** (such as a string, list, or range of numbers) and executes the loop body once per element.
- **In Simple Words:** `for` means "do this once for every item in the sequence."
- **Real-Life Example:** A teacher calls roll — "For each name on the list, mark present or absent." One instruction covers every student.

### Basic Syntax

```python
for item in sequence:  # item takes each value from sequence, one at a time
    # Indented code runs once per item
```

- `item` is a **loop variable** — you can choose any valid name (`i`, `student`, `num`).
- The **`in`** keyword means "take each value from this sequence, one at a time."
- Python automatically moves to the **next** item after each round — no manual counter needed when using `range()`.

### Example: Print Each Fruit in a List

```python
fruits = ["mango", "banana", "apple"]  # A list of three fruit names
for fruit in fruits:  # fruit takes each list item one by one
    print("Today's fruit:", fruit)  # Print a message for each fruit
```

**How the code works:**

- The loop body runs three times with `fruit` equal to `"mango"`, then `"banana"`, then `"apple"`.
- **Common mistake:** Expecting `print(fruit)` outside the loop to print all fruits — it only prints the **last** value.

### Example: Print "Hello" 10 Times Without Copy-Pasting

```python
for i in range(10):  # range(10) gives 0, 1, 2, ... 9 — ten rounds
    print("Hello")  # Runs inside the loop — prints Hello each round
print("Done")  # Runs once, outside the loop — after all 10 rounds finish
```

**How the code works:**

- `i` is the loop variable but we do not need its value here — we only need the loop to run 10 times.
- `print("Done")` is **outside** the loop, so it runs exactly once after the loop finishes.

To count numbers (1 to 10, even numbers, etc.), Python provides a helper called **`range()`**.

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

### Example: Print Even Numbers Till 20 (Two Ways)

**Way 1 — Use step size 2 in `range()`:**

```python
for num in range(0, 21, 2):  # 0, 2, 4, 6, ... 20
    print(num)  # Prints each even number
```

**Way 2 — Use modulo (`%`) with `if`:**

```python
for num in range(21):  # 0, 1, 2, ... 20
    if num % 2 == 0:  # num % 2 gives remainder — 0 means even
        print(num)  # Print only when the number is even
```

**How the code works:**

- **Way 1** skips odd numbers entirely by jumping in steps of 2.
- **Way 2** checks every number and prints only when `num % 2 == 0`. Both give the same even-number output.

---

## Choosing the Right Loop — `for` vs `while`

- **Official Definition:** **Loop selection** is the practice of picking the loop type whose condition model best matches the problem — counting over a sequence versus repeating until a state changes.
- **In Simple Words:** Ask yourself: "Do I know **how many times** or **what items**?" → use `for`. "Do I repeat **until something happens**?" → use `while`.
- **Real-Life Example:** Printing numbers 1 to 10 is a **`for`** job (you know the count). Waiting at an ATM until the correct PIN is entered is a **`while`** job (tries are unknown).

| Situation | Use | Reason |
|-----------|-----|--------|
| Print numbers 1 to 10 | `for` with `range()` | You know exactly how many rounds |
| Print "Hello" N times | `for` with `range(N)` | Fixed repetition count |
| ATM PIN until correct | `while` | Repeat until condition is met |
| Take input for N students | `for` or `while` | Both work — pick the cleaner approach |

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

- Both print 0, 1, 2, 3, 4. Prefer **`for`** when counting or iterating a sequence; prefer **`while`** when exit depends on **changing conditions** or repeated user input.
- Other languages have a **do-while** loop, but Python focuses on **`for`** and **`while`** — these two cover almost every repetition need.

Sometimes you need to **stop early** or **skip one round** — that is where **`break`** and **`continue`** help.

---

## The `break` Statement — Stop the Loop Early

- **Official Definition:** The **`break` statement** immediately terminates the innermost loop that contains it and transfers control to the first statement after that loop.
- **In Simple Words:** `break` means "stop the loop right now — we are done."
- **Real-Life Example:** You find your Aadhaar card in the second drawer — you **stop searching** the remaining drawers.

### Example: Stop a `while` Loop After One Round

```python
c = 1  # Start counter at 1
while c <= 5:  # Loop would normally run 5 times
    print(c)  # Print current count
    break  # Exit the loop immediately — only one round runs
print("Loop ended")  # This line runs after break
```

**How the code works:**

- Without `break`, the loop would print 1, 2, 3, 4, 5. With `break` after the first `print`, the loop stops after printing `1` once.
- **`break`** is useful when you find what you need early and do not want to keep looping.

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

### Example: Print 1 to 15, Skip 7 and 11

```python
num = 1  # Start from 1
while num <= 15:  # Loop while num is 15 or less
    if num == 7 or num == 11:  # Skip these two numbers
        num = num + 1  # Update counter BEFORE continue — avoid infinite loop
        continue  # Skip printing for 7 and 11
    print(num)  # Print all other numbers
    num = num + 1  # Move to next number
```

**How the code works:**

- When `num` is 7 or 11, `continue` skips the `print` line and moves to the next round.
- **Critical:** Always increment `num` before `continue` in a `while` loop, otherwise `num` stays stuck and the loop never ends.

---

## Automating Repetitive Tasks with Loops

- **Official Definition:** **Automation through iteration** means using loops to perform the same operation on many inputs or for many steps, reducing manual duplication and human error.
- **In Simple Words:** Write the logic once; let the loop apply it everywhere.
- **Real-Life Example:** A teacher collects marks from every student in class — one loop handles all students instead of writing separate code for each.

![Automation and accumulator pattern — shopping bill total code, four-step accumulator flow, counter pattern example, and average-outside-loop warning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session03/session03-06-automation-accumulator.png?v=20260614-ai)

### Example: Class Average from Repeated Input

**Problem:** Take names and English marks for 5 students, then print the class average.

```python
student_count = 5  # Number of students to process
total_students = student_count  # Keep a copy for division later
total_marks = 0  # Running sum — must start at 0

while student_count > 0:  # Loop while there are students left
    name = input("Enter student name: ")  # Get name each round
    marks = int(input("Enter marks in English: "))  # Get marks as integer
    total_marks = total_marks + marks  # Add to running total
    student_count = student_count - 1  # One fewer student left (same as student_count -= 1)

average = total_marks / total_students  # Divide ONCE, outside the loop
print("Class average:", average)  # Print final result
```

**How the code works:**

- **`total_marks`** is an **accumulator** — it builds a running sum inside the loop.
- **`total_students`** is saved before the loop because `student_count` becomes 0 by the end — dividing by 0 would cause an error.
- **`average`** is calculated **outside** the loop, after all marks are collected.
- **Common mistake:** Calculating `average` **inside** the loop — that recomputes average every round instead of once at the end.

---

## Iterative Thinking — Breaking Problems into Testable Parts

- **Official Definition:** **Iterative problem solving** is the approach of decomposing a problem into smaller steps, solving each step, and testing before combining them — often using loops to handle repeated sub-steps.
- **In Simple Words:** Do not solve the whole puzzle at once — solve one piece, check it, then move to the next.
- **Real-Life Example:** Preparing for board exams — you revise one chapter, test yourself with questions, then move to the next chapter instead of reading the entire book in one sitting.

### How to Approach a Loop Problem

| Step | What to Ask | Example (Class average) |
|------|-------------|-------------------------|
| **1 — Define the goal** | What should the program output? | Print average of five students' marks |
| **2 — Find the repetition** | What action repeats? | Take name and marks for each student |
| **3 — Pick the loop** | `for` or `while`? Over what? | `while student_count > 0:` |
| **4 — Build inside the loop** | What happens each round? | Input marks, add to `total_marks`, decrease counter |
| **5 — Finish outside the loop** | What runs once at the end? | `average = total_marks / total_students` |

After the loop, handle **one-time** steps (like dividing total by count) **outside** the loop.

### Worked Example: Same Problem with a `for` Loop

The class average problem can also be solved with a **`for` loop** — there is often more than one correct approach.

```python
student_count = int(input("Enter number of students: "))  # Dynamic student count
total_marks = 0  # Running sum starts at zero

for i in range(student_count):  # Loop exactly student_count times
    name = input("Enter student name: ")  # Get name each round
    marks = int(input("Enter marks in English: "))  # Get marks
    total_marks = total_marks + marks  # Accumulate total

average = total_marks / student_count  # Divide once, outside the loop
print("Class average:", average)  # Print final average
```

**How the code works:**

- **`for i in range(student_count)`** runs exactly the right number of times — no manual counter decrement needed.
- **`student_count`** stays unchanged, so you can safely divide by it at the end.
- **Test in parts:** First confirm `total_marks` is correct, then add the division step outside the loop.

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

### Exercise 2: Print 1 to 15, Skip 7 and 11

Use a `while` loop and `continue` to print all numbers from 1 to 15 except 7 and 11.

```python
num = 1  # Start from 1
while num <= 15:  # Loop until 15
    if num == 7 or num == 11:  # Numbers to skip
        num = num + 1  # Update before continue
        continue  # Skip printing
    print(num)  # Print all other numbers
    num = num + 1  # Move to next number
```

**How the code works:**

- **`continue`** skips the print for 7 and 11 but keeps the loop running for all other numbers.
- Updating `num` before `continue` prevents an infinite loop.

### Exercise 3: Even Numbers Till 20

Print all even numbers from 0 to 20 using a `for` loop with `range()` step size 2.

```python
for num in range(0, 21, 2):  # 0, 2, 4, ... 20
    print(num)  # Print each even number
```

**How the code works:**

- **`range(0, 21, 2)`** generates even numbers directly — no `if` check needed.

---

## Debugging Loop Programs

- **Dry-run on paper:** Trace the loop variable round by round before running — this is the fastest way to catch logic errors.
- **Print the loop variable:** Add `print(i)` inside the loop to see how values change each round.
- **Check off-by-one errors:** If you wanted 1 to 10 but got 1 to 9, your `range()` stop value is probably one too small.
- **Watch infinite loops:** If the program never stops, verify the variable in the `while` condition is **updated** inside the loop.
- **Trace with small data:** Test with 2 or 3 items first before large counts.
- **Place `break`/`continue` carefully:** In `while` loops, update counters **before** `continue` to avoid getting stuck.

---

## Key Takeaways

- **`while` loops** repeat code as long as a condition is `True` — ideal when you do not know how many tries you need (ATM PIN, repeated input).
- **`for` loops** visit each item in a sequence or each number from **`range()`** — ideal when you know how many times to count or iterate.
- **`break`** stops a loop early; **`continue`** skips one iteration and keeps going — use them to exit early or filter items without messy nested logic.
- **Iterative thinking** means breaking problems into small testable steps — build the loop first, verify the total or count, then add final calculations outside the loop.
- Python uses **`count = count + 1`** (not `count++`) and requires careful counter updates in **`while` loops** to avoid infinite loops.
- These skills prepare you for **lists, strings, and functions**, where loops become even more powerful for processing real data.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Does |
|----------------|--------------|
| **`while`** | Repeats a block while a condition is `True` |
| **`for`** | Repeats a block once for each item in a sequence |
| **`in`** | Used with `for` — "for each value in this sequence" |
| **`break`** | Exits the current loop immediately |
| **`continue`** | Skips the rest of the current iteration; loop continues |
| **`range(stop)`** | Generates numbers from 0 to stop − 1 |
| **`range(start, stop)`** | Generates numbers from start to stop − 1 |
| **`range(start, stop, step)`** | Generates numbers with a custom step (can count by 2, 3, etc.) |
| **Loop / Iteration** | Repeating a block of code multiple times |
| **Loop variable** | Variable that holds the current value in each round of a `for` loop |
| **Infinite loop** | A loop that never ends because its condition never becomes `False` |
| **Accumulator** | A variable (often starting at 0) that builds a total inside a loop |
| **Counter** | A variable that increases or decreases each iteration to track progress |
| **Dry run** | Tracing code step by step on paper to predict output before running |
| **Automation** | Using loops to apply the same logic to many inputs without duplicating code |
| **Iterative problem solving** | Breaking a problem into repeated, testable steps |
