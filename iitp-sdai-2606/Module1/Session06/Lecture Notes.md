# Nested Logic, Loops & Intro to Complexity Analysis

## What You Will Learn in This Lesson

You have already learned **conditional statements** (`if`, `elif`, `else`), **loops** (`while` and `for`), **lists**, **strings**, and **dictionaries**. Your programs can make decisions, repeat actions, and store data in ordered lists or labelled key-value pairs.

In this lesson, you will combine decisions **inside** other decisions (**nested conditionals**) and loops **inside** other loops (**nested loops**). You will process **2D data**, generate **pairs and combinations**, and recognise simple **Big-O** patterns — **O(1)**, **O(n)**, and **O(n²)**.

By the end, you will handle multi-step decisions, print patterns and tables, scan grids of data, and explain why some code stays fast while similar-looking code slows down as data grows.

---

## Why Do Programs Need Nested Logic?

- **Official Definition:** **Nested logic** means placing one control structure (an `if` block or a `for` loop) **inside** another at a deeper indentation level.
- **In Simple Words:** First check one thing; **only if that passes**, check the next. Or repeat an action, and **inside each repetition**, repeat another action.
- **Real-Life Example:** At an airport, security checks your **boarding pass** first (outer). Only then they scan your **bag** (inner).

- A **movie ticket app** checks age, then seat availability, then payment — each step depends on the previous one.
- An **exam portal** loops through every student, and **for each student** loops through every subject mark.
- Nested work grows quickly when lists get large — which is why **efficiency** matters later in this lesson.

![Nested logic big picture — airport boarding pass then bag scan analogy, nested conditionals vs nested loops comparison, bank and exam portal layered rules, school assembly and 2D grid examples, and efficiency when data grows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-01-nested-logic-big-picture.png?v=20260620-ai)

---

## Nested Conditionals — Multi-Level Decision Logic

- **Official Definition:** A **nested conditional** is an `if`, `elif`, or `else` block written **inside** another conditional block.
- **In Simple Words:** Answer one question first; based on that answer, ask a **follow-up question** before deciding the final outcome.
- **Real-Life Example:** At a **bank loan counter** — first they check **income** (outer). Only if income is enough, they check **credit score** (inner).

### When to Use Nested vs Flat `elif`

| Situation | Better Approach | Why |
|-----------|-----------------|-----|
| One value, many ranges (marks → grade) | Flat **`elif` chain** | All checks at the same level |
| Step 1 must pass before Step 2 matters | **Nested `if`** | Inner check runs only when outer passes |
| Many independent conditions | **`and` / `or`** in one `if` | Keeps code readable |

- **Common mistake:** Nesting more than **3 levels** makes code hard to read — use **`and`**, **`or`**, or helper variables instead.
- **Reason to nest:** Different **error messages** at each level so the user knows exactly which step failed.

![Nested conditionals diagram — outer attendance gate then inner marks band, when to nest vs flat elif table, conditional inside loop O(n) pattern, and bank income-then-credit analogy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-02-nested-conditionals.png?v=20260620-ai)

### Example: Exam Eligibility with Attendance and Marks

A student is eligible for the final exam only if **attendance ≥ 75%**. If attendance passes, marks decide the category: **Distinction** (≥ 85), **Pass** (≥ 40), or **Fail** (< 40).

```python
# Get student data from input
attendance = float(input("Enter attendance percentage: "))  # e.g. 80.0
marks = float(input("Enter internal marks: "))  # e.g. 88.0

# Outer decision — attendance gate
if attendance >= 75:  # Must meet minimum attendance first
    if marks >= 85:  # Inner — highest grade band
        print("Eligible — Distinction")
    elif marks >= 40:  # Passing but not distinction
        print("Eligible — Pass")
    else:  # Attendance OK but marks too low
        print("Eligible to sit exam but currently Fail — improve marks")
else:  # Attendance too low — inner marks check never runs
    print("Not eligible — attendance below 75%")
```

**How the code works:**

- The **outer `if`** is the attendance gate — if it fails, the inner block is skipped entirely.
- The **inner `if` / `elif` / `else`** runs only when attendance passes; **`elif`** keeps mark categories mutually exclusive.
- **Common mistake:** Putting mark checks **outside** the attendance block would grade students who should be blocked.

### Example: Conditional Inside a Loop

```python
# Find all students who passed (marks >= 40)
students = ["Anita", "Rohit", "Priya", "Karan"]  # Names in order
marks = [78, 35, 92, 64]  # Matching marks by index

print("--- Pass List ---")
for i in range(len(students)):  # Loop through every index — O(n) pattern
    if marks[i] >= 40:  # Conditional inside the loop body
        print(students[i], ":", marks[i])  # Print only passing students
```

**How the code works:**

- The **loop visits every student**; the **`if` filters** who gets printed — one loop, one pass.

---

## Practice Activity — Multi-Step Ticket Pricing

A **theme park** charges adults (age ≥ 18) **Rs. 500** and children **Rs. 300**. On **weekends** add **Rs. 100** surcharge. **Members** get **10% discount** on the final price.

```python
# Theme park ticket calculator
age = int(input("Enter age: "))  # Visitor age
day = input("Enter day (e.g. Monday): ")  # Weekday name
member = input("Membership card? (yes/no): ").lower()  # Member status

if age >= 18:  # Adult ticket
    price = 500  # Base adult rate
else:  # Child ticket
    price = 300  # Base child rate

if day == "Saturday" or day == "Sunday":  # Weekend surcharge
    price = price + 100  # Add flat surcharge

if member == "yes":  # Membership discount on final price
    price = price - (price * 0.10)  # Subtract 10 percent

print("Final ticket price: Rs.", int(price))  # Show rounded rupee amount
```

**How the code works:**

- **Sequential conditionals** stack rules on a running `price` — clearer than deep nesting when each rule **adds independently**.
- Test with: adult + Saturday + member, child + Monday + no member, and age exactly 18.

---

## Nested Loops — Loops Inside Loops

- **Official Definition:** A **nested loop** is a loop whose body contains another loop. The **inner loop completes all iterations** for **each single iteration** of the outer loop.
- **In Simple Words:** For every round of the outer loop, run the entire inner loop from start to finish.
- **Real-Life Example:** A **school assembly** — for **each class** (outer), the teacher reads **every roll number** (inner).

- If outer runs **n** times and inner runs **m** times per outer round, total inner-body executions ≈ **n × m**.
- **Common mistake:** Reusing the same loop variable name for outer and inner — use **`i`** and **`j`**.

![Nested loops diagram — multiplication table 1 to 5 grid with n×m formula, star pattern rows, school assembly and pizza combo analogies, and common mistakes like swapped outer-inner order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-03-nested-loops.png?v=20260620-ai)

### Example: Multiplication Table (1 to 5)

```python
# Print multiplication table for numbers 1 through 5
print("--- Multiplication Table ---")
for i in range(1, 6):  # Outer loop — each number (row)
    for j in range(1, 6):  # Inner loop — multiply i by each j (column)
        product = i * j  # Calculate i × j
        print(f"{i} x {j} = {product}")  # Print one line of the table
    print("---")  # Separator after each row
```

**How the code works:**

- When **`i = 1`**, inner loop runs **`j = 1` through `5`** — five lines. Same for each **`i`** — total **5 × 5 = 25** lines.
- **Common mistake:** Swapping outer and inner changes **row vs column order**.

### Example: Star Pattern Triangle

```python
# Print a triangle — 1 star on row 1, 2 on row 2, etc.
rows = 5  # Number of rows
for i in range(1, rows + 1):  # Outer — each row
    for j in range(i):  # Inner — print i stars on row i
        print("*", end="")  # Same line, no newline
    print()  # New line after each row
```

- Inner loop count tied to outer variable **`i`** — row 1 prints 1 star, row 5 prints 5 stars.

---

## Processing 2D Data with Nested Loops

- **Official Definition:** **2D data** is data arranged in **rows and columns** — in Python, stored as a **list of lists**, where each inner list is one row.
- **In Simple Words:** A table with multiple rows; each row has multiple columns.
- **Real-Life Example:** A **cinema hall seating chart** — Row A: A1, A2, A3; Row B: B1, B2, B3.

```python
# Seating chart — each inner list is one row
hall = [
    ["A1", "A2", "A3"],  # Row 0
    ["B1", "B2", "B3"],  # Row 1
    ["C1", "C2", "C3"],  # Row 2
]

print("Front corner:", hall[0][0])  # Row 0, col 0 → A1
print("Back middle:", hall[2][1])  # Row 2, col 1 → C2

# Scan every seat with nested loops
for row in range(len(hall)):  # Outer — each row index
    for col in range(len(hall[row])):  # Inner — each column in that row
        print(f"Row {row}, Col {col} → {hall[row][col]}")
```

**How the code works:**

- **`hall[row][col]`** — first index is **row**, second is **column**. A **3×3** grid → inner body runs **9 times**.
- **Common mistake:** Index out of range — valid columns for 3 seats are **0, 1, 2** only.

### Example: Mark Sheet — Total and Average Per Student

```python
# Three students, three subjects — 2D marks grid
students = ["Anita", "Rohit", "Priya"]
marks_sheet = [
    [78, 85, 92],  # Anita
    [64, 71, 68],  # Rohit
    [88, 90, 95],  # Priya
]

print("--- Mark Sheet Report ---")
for i in range(len(students)):  # Outer — each student
    total = 0  # Reset per student — must be inside outer, outside inner
    for j in range(len(marks_sheet[i])):  # Inner — each subject mark
        total = total + marks_sheet[i][j]  # Accumulate marks
    average = total / len(marks_sheet[i])  # Average for this student
    print(f"{students[i]}: Total = {total}, Average = {average:.2f}")
```

**How the code works:**

- **`total = 0`** inside outer loop, outside inner loop — resets per student, accumulates per subject.
- **Common mistake:** Declaring `total = 0` before the outer loop — totals carry over between students.

![2D data grid diagram — cinema hall seat chart with row and column indices, hall[row][col] access, mark sheet total and average pattern, and cinema O/X seat scanner with counter outside loops](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-04-2d-data-grid.png?v=20260620-ai)

---

## Generating Pairs and Combinations

- **Official Definition:** Matching **every item from the outer loop** with **every item from the inner loop** lists all **combinations** from two sequences.
- **In Simple Words:** 3 flavours × 3 sizes → nested loops list every **flavour + size** option.
- **Real-Life Example:** A **pizza menu** — **crust type** (outer) × **topping** (inner) → every combo on the board.

### All Pairs from Two Lists

```python
# Match every city with every transport mode
cities = ["Delhi", "Mumbai"]
modes = ["Train", "Flight"]

print("--- Travel Options ---")
for city in cities:  # Outer — each city
    for mode in modes:  # Inner — each mode
        print(f"Go to {city} by {mode}")  # n × m combinations
```

**How the code works:**

- **2 × 2 = 4** lines — if cities have **n** items and modes have **m**, total = **n × m**.

### Unique Pairs from One List

List all unique teams of two from four friends — (Anita, Rohit) same as (Rohit, Anita), so print each pair once.

```python
friends = ["Anita", "Rohit", "Priya", "Karan"]

print("--- Unique Pairs ---")
for i in range(len(friends)):  # Outer — first person
    for j in range(i + 1, len(friends)):  # Inner — only later indices
        print(friends[i], "&", friends[j])  # No duplicates or self-pairs
```

**How the code works:**

- **`range(i + 1, len(friends))`** prevents double counting — **4 friends → 6 unique pairs**.

---

## Practice Activity — Seat Availability Scanner

Seats marked **`"O"`** are free; **`"X"`** are booked. Count available seats in this cinema grid.

```python
seats = [
    ["O", "X", "O", "O"],  # Row 1 — 3 available
    ["X", "X", "O", "O"],  # Row 2 — 2 available
    ["O", "O", "O", "X"],  # Row 3 — 3 available
]

available = 0  # Counter outside both loops
for row in range(len(seats)):
    for col in range(len(seats[row])):
        if seats[row][col] == "O":  # Nested loop + conditional inside
            available = available + 1

print("Available seats:", available)  # Output: 8
```

**How the code works:**

- Combines **nested loops** with a **conditional** — very common in real programs. Counter sits **outside both loops**.

---

## Why Does Efficiency Matter? — Complexity Basics

- **Official Definition:** **Computational efficiency** measures how the **steps** a program needs grow as **input size** grows.
- **In Simple Words:** Will your program stay fast with 10 items? What about 10 lakh items?
- **Real-Life Example:** Finding a contact among **5 names** takes seconds. Among **5 lakh names** without a smart method could take days.

You need **intuition**: some code does **fixed work**, some grows **with list size**, and some **explodes** when size doubles.

### Best Case, Average Case, and Worst Case

| Case | Meaning | Simple Analogy |
|------|---------|----------------|
| **Best case** | Fastest scenario for given input size | Keys on the **first cushion** you check |
| **Average case** | Typical scenario across many inputs | Keys found after checking **half** the sofa |
| **Worst case** | Slowest scenario — maximum work | Keys in the **last pocket** of the last bag |

- **Real-Life Example:** **IRCTC Tatkal** — best case: ticket in seconds; worst case: lakhs of users, long queue. Focus on **worst case** — UPI and exam portals must handle peak load. **Nested loops** multiply work as data grows.

---

## Big-O Notation — O(1), O(n), and O(n²)

- **Official Definition:** **Big-O notation** describes how an algorithm's step count **grows** relative to input size **`n`**, keeping the **dominant term** as **`n` becomes large**.
- **In Simple Words:** "If I double the data, does work stay the same, double, or multiply much more?"
- **Real-Life Example:** One parcel to one house = fixed work. Every house on a street = grows with length. Every house vs every other house = grows much faster.

| Big-O | Name | Growth | When You See It |
|-------|------|--------|-----------------|
| **O(1)** | Constant | Same regardless of n | Dictionary lookup, `list[0]` |
| **O(n)** | Linear | Grows with n | Single loop over a list |
| **O(n²)** | Quadratic | Grows like n × n | Nested loops over n items |

### How to Identify Big-O — Quick Checklist

1. **Zero loops** over growing data → likely **O(1)**.
2. **One loop** over size n → likely **O(n)**. An **`if` inside one loop** does not change this.
3. **Two nested loops** each up to n → likely **O(n²)**.
4. **Pick worst case** for classification — even if **`break`** exits early sometimes.

| Code Pattern | Big-O | n = 10 | n = 1000 |
|--------------|-------|--------|----------|
| `dict[key]` | O(1) | ~1 step | ~1 step |
| One `for` over list | O(n) | ~10 | ~1,000 |
| Two nested `for` over n | O(n²) | ~100 | ~1,000,000 |

![Big-O patterns diagram — O(1) O(n) O(n²) step growth bar chart at n=10 and n=1000, dict lookup and single loop vs nested loop examples, best average worst case panel, and loop-count identification checklist](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-05-big-o-patterns.png?v=20260620-ai)

### O(1) — Constant Time Example

```python
# Dictionary lookup and index access — fixed steps regardless of size
marks_by_roll = {"B-101": 78, "B-102": 92, "B-103": 64}  # Roll → mark
print("Mark:", marks_by_roll["B-102"])  # Direct key fetch — O(1) average

fruits = ["apple", "banana", "mango", "grape"]
print("First:", fruits[0])  # Jump to index 0 — always one step
```

**How the code works:**

- **`dict[key]`** and **`list[i]`** jump directly — work does not scale with collection size for access.

### O(n) — Linear Time Example

```python
# Find highest mark — one full pass through the list
marks = [72, 88, 65, 91, 77, 84]
highest = marks[0]  # Assume first is highest
for i in range(1, len(marks)):  # Visit each remaining mark once
    if marks[i] > highest:  # Found a bigger mark
        highest = marks[i]  # Update highest so far
print("Highest mark:", highest)  # O(n) — double data ≈ double work
```

**How the code works:**

- One **`for` loop** → **O(n)**. **`max(marks)`** does the same scan internally.

### O(n²) — Quadratic Time Example

```python
# Print every ordered pair from a list — nested loops
numbers = [10, 20, 30]  # n = 3
for i in range(len(numbers)):  # Outer — n times
    for j in range(len(numbers)):  # Inner — n times per outer step
        print(numbers[i], "with", numbers[j])  # n × n = 9 lines
```

**How the code works:**

- For **`n` items**, inner body runs **`n × n`** times. At **`n = 1000`**, about **10 lakh** iterations — fine for homework, risky at production scale.
- **Common mistake:** A third nested loop → **O(n³)** — avoid unless truly needed.

---

## Practice Activity — Label the Complexity

Read each snippet. Write **O(1)**, **O(n)**, or **O(n²)** on paper before checking the answer.

| Snippet | Code Idea | Answer |
|---------|-----------|--------|
| **A** | `print(menu["dosa"])` on a price dictionary | **O(1)** — single lookup |
| **B** | One `for` loop counting present days in a list | **O(n)** — one pass |
| **C** | Two nested `for` loops printing all name pairs | **O(n²)** — n × n work |

---

## Practice Programs

### Exercise 1: FizzBuzz with Nested Conditionals (1 to 20)

```python
for num in range(1, 21):  # O(n) — one loop
    if num % 3 == 0:  # Divisible by 3
        if num % 5 == 0:  # Also divisible by 5 — nested check
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:  # Divisible by 5 only
        print("Buzz")
    else:
        print(num)
```

### Exercise 2: Grand Total of a 2D Marks Grid

```python
grid = [[70, 80, 90], [85, 75, 95]]  # 2 students, 3 subjects
grand_total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        grand_total = grand_total + grid[row][col]
print("Grand total:", grand_total)  # Output: 495
```

### Exercise 3: Grades O(n) vs Pairwise Compare O(n²)

```python
students = ["Anita", "Rohit", "Priya"]
marks = [88, 72, 95]
n = len(students)

# Part 1 — O(n): grade each student
for i in range(n):
    if marks[i] >= 85:
        grade = "Distinction"
    elif marks[i] >= 40:
        grade = "Pass"
    else:
        grade = "Fail"
    print(f"{students[i]}: {marks[i]} → {grade}")

# Part 2 — O(n²): compare every unique pair
for i in range(n):
    for j in range(i + 1, n):
        if marks[i] > marks[j]:
            print(f"{students[i]} beats {students[j]}")
        elif marks[j] > marks[i]:
            print(f"{students[j]} beats {students[i]}")
        else:
            print(f"{students[i]} and {students[j]} tied")
```

**How the code works:**

- **Part 1** — one loop, **O(n)**. **Part 2** — nested loops, **O(n²)**. Big-O comes from **loop structure**, not from **`if`** inside loops.

---

## Debugging Nested Programs

- **Print loop variables** — `print(f"i={i}, j={j}")` on small inputs to trace execution order.
- **Test tiny grids first** — 2×2 before 10×10; index errors show up faster.
- **Reset counters in the right place** — per-row totals inside outer loop; grand totals outside both loops.
- **Check indentation** — one wrong space moves an inner `for` or `if` to the wrong block.
- **Estimate iterations** — outer 100 × inner 100 = **10,000** inner-body runs; slowness often means nested structure.

---

## Key Takeaways

- **Nested conditionals** model **multi-step decisions** — inner checks run only when outer checks pass; avoid excessive depth without `and`/`or`.
- **Nested loops** process **2D grids**, **patterns**, and **pairs** — total work is often **n × m**; place accumulators in the correct loop scope.
- **Best / average / worst case** intuition matters — design for **worst case** when data or traffic grows.
- **Big-O patterns**: **O(1)** fixed lookup, **O(n)** single pass, **O(n²)** nested loops — recognise these in code you write and read.
- These skills connect to **functions, algorithms, and backend systems** where loop structure affects whether apps stay responsive under load.

---

## Important Commands, Libraries, and Terminologies

| Term / Concept | What It Means |
|----------------|---------------|
| **Nested conditional** | An `if`/`elif`/`else` block inside another conditional block |
| **Nested loop** | A loop inside another loop's body |
| **2D data / list of lists** | Rows and columns — access with `grid[row][col]` |
| **Combination / pair generation** | All choices from nested iteration over two sequences |
| **Computational efficiency** | How program work grows as input size grows |
| **Best / average / worst case** | Minimum, typical, and maximum work for a given input size |
| **Big-O notation** | Growth rate of steps as `n` becomes large |
| **O(1) — constant time** | Work stays roughly the same as `n` grows |
| **O(n) — linear time** | Work grows in proportion to `n` — one pass |
| **O(n²) — quadratic time** | Work grows like `n × n` — nested double loop |
| **Input size `n`** | Number of items in the main list or dimension processed |
| **`range(len(list))`** | Index loop 0 to length−1 — common in 2D scanning |
| **`list[i][j]`** | Access row `i`, column `j` in a 2D list |
| **`end=""` in print** | Print without newline — useful for patterns |
| **Accumulator pattern** | Variable like `total` or `count` built up inside a loop |
| **Hashmap / dictionary lookup** | Key-based fetch — O(1) average intuition |
| **Quadratic growth** | Doubling `n` can quadruple work — hallmark of O(n²) |
