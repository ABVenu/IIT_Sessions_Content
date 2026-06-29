# Nested Logic, Loops & Intro to Complexity Analysis

## What You Will Learn

You already know basic **conditionals**, **loops**, **lists**, and **dictionaries**. In this lesson, you will combine those ideas to write programs that make multi-step decisions and repeat work inside repeated work.

By the end, you should be able to:

- Write **nested conditional logic** for step-by-step decisions.
- Use **nested loops** for combinations and 2D data.
- Understand **best case**, **average case**, and **worst case** in simple words.
- Identify simple **Big-O** patterns: **O(1)**, **O(n)**, and **O(n²)**.

![Nested logic big picture — airport boarding pass then bag scan analogy, nested conditionals vs nested loops comparison, bank and exam portal layered rules, school assembly and 2D grid examples, and efficiency when data grows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-01-nested-logic-big-picture.png?v=20260620-ai)

---

## Quick Recap: Dictionaries

- **Official Definition:** A **dictionary** stores data in **key-value pairs**.
- **In Simple Words:** A key is like a label, and the value is the actual data stored against that label.
- **Real-Life Example:** In a phone contact list, a person's name can act like a key and the phone number is the value.

Important points:

- A dictionary is also commonly understood as a **hashmap**.
- You can create a dictionary, add values, update values, and loop through key-value pairs.
- The `.items()` method is useful when you want both the key and the value during iteration.

```python
# Create a dictionary with student names as keys and marks as values
marks = {"Anita": 85, "Rohit": 72, "Priya": 91}

# Loop through both key and value using items()
for name, score in marks.items():
    # Print each student's name and score
    print(name, "scored", score)
```

**How the code works:**

- `marks` stores names mapped to marks.
- `.items()` gives one key-value pair at a time.
- `name` receives the key and `score` receives the value.

This recap connects directly to today's topic because loops and conditions are often used while working with dictionaries, lists, and nested data.

---

## Nested Conditionals

- **Official Definition:** A **nested conditional** is an `if`, `elif`, or `else` block written inside another conditional block.
- **In Simple Words:** First check one condition. Only if that condition passes, check the next condition.
- **Real-Life Example:** At a concert gate, first the staff checks whether you have a ticket. Only after that, they check whether it is a VIP ticket or a normal ticket.

### Why Nesting Is Useful

- Some checks only make sense after another check has passed.
- For example, checking whether a ticket is VIP makes sense only when the person already has a ticket.
- The inner condition runs only when the outer condition is true.

![Nested conditionals diagram — outer attendance gate then inner marks band, when to nest vs flat elif table, conditional inside loop O(n) pattern, and bank income-then-credit analogy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-02-nested-conditionals.png?v=20260620-ai)

### Example: Concert Entry Check

```python
# Store whether the customer has a ticket
has_ticket = True

# Store the type of ticket
ticket_type = "VIP"

# First check whether the customer has any ticket
if has_ticket:
    # This inner check runs only when has_ticket is True
    if ticket_type == "VIP":
        # Print this when the ticket is VIP
        print("Access granted through VIP entrance")
    else:
        # Print this when the ticket is present but not VIP
        print("Access granted through normal entrance")
else:
    # Print this when the customer has no ticket
    print("No ticket, entry not allowed")
```

**How the code works:**

- The outer `if has_ticket` checks the main requirement first.
- The inner `if ticket_type == "VIP"` runs only after the ticket check passes.
- If `has_ticket` is `False`, Python directly runs the outer `else`.

### Indentation Matters

- In Python, indentation decides which code is inside which block.
- The inner `if` must be indented inside the outer `if`.
- If indentation is wrong, the program logic may change or Python may show an error.

---

## Keeping Conditions Readable

Nested conditions are useful, but too much nesting can make code hard to read. If two or more conditions must all be true together, using `and` can sometimes make the code simpler.

### Example: ATM Withdrawal Check

```python
# Store whether the ATM card is valid
card_is_valid = True

# Store the account balance
balance = 5000

# Store the requested withdrawal amount
withdraw_amount = 1500

# Check all required conditions together
if card_is_valid and withdraw_amount > 0 and balance >= withdraw_amount:
    # Allow withdrawal only when all conditions are true
    print("Withdrawal allowed")
else:
    # Show failure when any one required condition fails
    print("Withdrawal not allowed")
```

**How the code works:**

- `card_is_valid` checks whether the card can be used.
- `withdraw_amount > 0` checks that the user entered a valid positive amount.
- `balance >= withdraw_amount` checks that enough money is available.
- `and` means all three conditions must be true.

Use nesting when the second question depends on the first answer. Use `and` when several checks are part of the same rule and the code remains easy to read.

---

## Nested Loops

- **Official Definition:** A **nested loop** is a loop written inside another loop.
- **In Simple Words:** For every one round of the outer loop, the inner loop runs completely.
- **Real-Life Example:** For every class in a school, the teacher reads every roll number in that class.

Important idea:

- If the outer loop runs `n` times and the inner loop runs `m` times, total work is about `n × m`.
- The inner loop starts again for every new value of the outer loop.
- Use different variable names like `i` and `j` to avoid confusion.

![Nested loops diagram — multiplication table 1 to 5 grid with n×m formula, star pattern rows, school assembly and pizza combo analogies, and common mistakes like swapped outer-inner order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-03-nested-loops.png?v=20260620-ai)

### Example: Basic Nested Loop Trace

```python
# Outer loop runs for values 0, 1, and 2
for i in range(3):
    # Inner loop runs for values 0, 1, 2, and 3
    for j in range(4):
        # Print the current outer and inner loop values
        print(i, j)
```

**How the code works:**

- When `i = 0`, the inner loop prints `j = 0, 1, 2, 3`.
- Then `i = 1`, and the inner loop again prints `j = 0, 1, 2, 3`.
- Then `i = 2`, and the inner loop again runs fully.
- Total prints are `3 × 4 = 12`.

---

## Generating Combinations with Nested Loops

- **Official Definition:** A **combination pattern** uses nested loops to match every item from one list with every item from another list.
- **In Simple Words:** Pick one shirt, try it with every pant, then pick the next shirt and again try every pant.
- **Real-Life Example:** A clothing app can show every shirt-pant combination from available choices.

### Example: Shirt and Pant Combinations

```python
# Store available shirts
shirts = ["white", "black"]

# Store available pants
pants = ["black", "khaki", "gray"]

# Loop through every shirt
for shirt in shirts:
    # For each shirt, loop through every pant
    for pant in pants:
        # Print the current combination
        print(shirt, "shirt with", pant, "pant")
```

**How the code works:**

- First, `shirt` becomes `"white"`.
- The inner loop pairs `"white"` with all pants.
- Then `shirt` becomes `"black"`.
- The inner loop again pairs `"black"` with all pants.
- Total combinations are `2 × 3 = 6`.

### Using `continue` in a Nested Loop

Sometimes you may want to skip one unwanted combination but continue checking the remaining combinations.

```python
# Store available shirts
shirts = ["white", "black"]

# Store available pants
pants = ["black", "khaki", "gray"]

# Loop through every shirt
for shirt in shirts:
    # Loop through every pant for the current shirt
    for pant in pants:
        # Skip the all-black combination
        if shirt == "black" and pant == "black":
            # Continue means skip the current iteration
            continue

        # Print only allowed combinations
        print(shirt, "shirt with", pant, "pant")
```

**How the code works:**

- When both shirt and pant are black, `continue` skips the print.
- Other combinations still get printed.
- This is useful when one pair is invalid but the full loop should not stop.

### Using `break` in a Nested Loop

`break` stops the current loop immediately. In a nested loop, it stops the loop where it is written.

```python
# Store available shirts
shirts = ["white", "black"]

# Store available pants
pants = ["black", "khaki", "gray"]

# Loop through every shirt
for shirt in shirts:
    # Loop through every pant for the current shirt
    for pant in pants:
        # Stop checking more pants once khaki is found
        if pant == "khaki":
            # Break exits the inner loop
            break

        # Print combinations before khaki is reached
        print(shirt, "shirt with", pant, "pant")
```

**How the code works:**

- The inner loop stops when `pant == "khaki"`.
- The outer loop can still move to the next shirt.
- `break` is stronger than `continue` because it exits the loop instead of only skipping one iteration.

---

## 2D Lists and Matrices

- **Official Definition:** A **2D list** is a list that contains other lists inside it.
- **In Simple Words:** It is like a table with rows and columns.
- **Real-Life Example:** A classroom marksheet can have students as rows and subject marks as columns.

![2D data grid diagram — cinema hall seat chart with row and column indices, hall[row][col] access, mark sheet total and average pattern, and cinema O/X seat scanner with counter outside loops](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-04-2d-data-grid.png?v=20260620-ai)

### Example: Defining and Reading a 2D List

```python
# Create a 2D list with three rows
numbers = [
    # First row of numbers
    [1, 2, 3, 4, 5],
    # Second row of numbers
    [11, 22, 33, 44, 55],
    # Third row of numbers
    [100, 200, 300, 400, 500],
]

# Print the full 2D list
print(numbers)

# Print the first item from the first row
print(numbers[0][0])
```

**How the code works:**

- `numbers[0]` gives the first row.
- `numbers[0][0]` gives the first element of the first row.
- The first index is the row, and the second index is the column.

### Iterating Over a 2D List

```python
# Create a 2D list with rows and columns
numbers = [
    # First row
    [1, 2, 3],
    # Second row
    [10, 20, 30],
    # Third row
    [100, 200, 300],
]

# Loop through every row
for row in numbers:
    # Loop through every value inside the current row
    for value in row:
        # Print each value one by one
        print(value)
```

**How the code works:**

- The outer loop picks one inner list at a time.
- The inner loop reads every value from that selected row.
- This is a common pattern for processing matrix-like data.

### Using `enumerate()` with 2D Lists

`enumerate()` is useful when you want both the index and the value.

```python
# Create a simple 2D list
matrix = [
    # Row 0
    [1, 2, 3],
    # Row 1
    [4, 5, 6],
]

# Get row index and row data together
for row_index, row in enumerate(matrix):
    # Get column index and value together
    for col_index, value in enumerate(row):
        # Print position and value
        print(row_index, col_index, value)
```

**How the code works:**

- `enumerate(matrix)` gives row index and row data.
- `enumerate(row)` gives column index and cell value.
- This makes 2D list traversal easier to read.

---

## Nested `while` Loops and Mixed Nesting

Nesting is not limited to only `for` loops. You can nest:

- a `for` loop inside another `for` loop,
- a `while` loop inside another `while` loop,
- a `for` loop inside a `while` loop,
- a `while` loop inside a `for` loop.

### Example: Nested `while` Loop

```python
# Start the outer counter
i = 0

# Run the outer loop while i is less than 3
while i < 3:
    # Start the inner counter for each i
    j = 0

    # Run the inner loop while j is less than 2
    while j < 2:
        # Print current values of i and j
        print(i, j)

        # Increase the inner counter
        j = j + 1

    # Increase the outer counter
    i = i + 1
```

**How the code works:**

- For every value of `i`, `j` starts again from `0`.
- The inner loop finishes before the outer loop moves ahead.
- This is the same nesting idea, only using `while`.

---

## Why Efficiency Matters

- **Official Definition:** **Complexity analysis** studies how the number of steps in a program grows when input size grows.
- **In Simple Words:** It helps us understand whether code will stay fast when data becomes large.
- **Real-Life Example:** Finding a phone number in a telephone book can be slow if you check every page one by one, but faster if you use the sorted order or index.

Two programs can give the same final answer but take very different time. That is why efficiency matters.

### Telephone Book Example

- **Approach 1:** Check every page and every name until the name is found.
- **Approach 2:** Use the sorted nature of the book, jump near the required alphabet, and reduce the search area.
- Both approaches may find the same phone number, but the second approach needs fewer checks.

This idea prepares us for Big-O notation.

---

## Best Case, Average Case, and Worst Case

- **Official Definition:** These are ways to describe how an algorithm behaves under different input situations.
- **In Simple Words:** Sometimes the answer is found quickly, sometimes after some work, and sometimes after maximum work.
- **Real-Life Example:** Searching for a name in a list is easiest if the name is first and slowest if the name is last.

| Case | Meaning | Simple Example |
|---|---|---|
| **Best case** | The luckiest input; minimum work | Target is the first item |
| **Average case** | A normal or middle situation | Target is somewhere around the middle |
| **Worst case** | The most work needed | Target is at the end or not found |

### Example: Searching in a List

```python
# Store numbers in a list
numbers = [10, 20, 30, 40, 50]

# Store the target value
target = 40

# Loop through every number
for number in numbers:
    # Check whether current number is the target
    if number == target:
        # Print when target is found
        print("Found target")

        # Stop searching after target is found
        break
```

**How the code works:**

- If `target` is `10`, the search stops quickly. This is the best case.
- If `target` is near the middle, it is an average kind of case.
- If `target` is `50` or missing, the loop does the most work. This is the worst case.

In complexity analysis, we usually focus on the **worst case** because it tells us the maximum work our program may need.

---

## Big-O Notation

- **Official Definition:** **Big-O notation** describes how the work done by code grows as input size `n` grows.
- **In Simple Words:** It answers this question: if data becomes bigger, how much extra work will my code do?
- **Real-Life Example:** Reading one fixed page is constant work, reading every page grows with the book, and comparing every page with every other page grows much faster.

![Big-O patterns diagram — O(1) O(n) O(n²) step growth bar chart at n=10 and n=1000, dict lookup and single loop vs nested loop examples, best average worst case panel, and loop-count identification checklist](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session06/session06-05-big-o-patterns.png?v=20260620-ai)

| Big-O | Name | Simple Pattern |
|---|---|---|
| **O(1)** | Constant time | Direct access, no growing loop |
| **O(n)** | Linear time | One loop over `n` items |
| **O(n²)** | Quadratic time | Two nested loops over `n` items |

---

## O(1): Constant Time

**O(1)** means the work stays almost the same even if the input size grows.

### Example: Direct Index Access

```python
# Store values in a list
numbers = [10, 20, 30, 40, 50]

# Directly access the first value
first_number = numbers[0]

# Print the accessed value
print(first_number)
```

**How the code works:**

- `numbers[0]` directly accesses one position.
- Even if the list has 200 items or 20 lakh items, this line still reads one selected position.
- This is why direct index access is treated as **constant time**.

Dictionary lookup is also commonly understood as **O(1) average time** because Python can fetch a value directly using its key.

---

## O(n): Linear Time

**O(n)** means work grows in proportion to input size. If there are more items, the loop does more work.

### Example: Sum All Numbers

```python
# Define a function to sum all numbers
def sum_numbers(numbers):
    # Start total from zero
    total = 0

    # Loop through every number in the list
    for number in numbers:
        # Add the current number to total
        total = total + number

    # Print the final total
    print(total)

# Call the function with a sample list
sum_numbers([10, 20, 30, 40])
```

**How the code works:**

- The loop reads every item in the list.
- If the list has 1,000 items, the loop runs about 1,000 times.
- If the list has 20 lakh items, the loop runs about 20 lakh times.
- This is called **linear time**, written as **O(n)**.

---

## O(n²): Quadratic Time

**O(n²)** usually appears when there are two nested loops and both depend on the input size.

### Example: Multiply Every Number with Every Number

```python
# Define a function for nested multiplication
def nested_multiply(numbers):
    # Loop through every number as the first value
    for i in numbers:
        # Loop through every number as the second value
        for j in numbers:
            # Print the multiplication of both values
            print(i * j)

# Call the function with a small list
nested_multiply([2, 4, 6])
```

**How the code works:**

- The outer loop runs `n` times.
- For every outer loop value, the inner loop also runs `n` times.
- Total work becomes `n × n`, which is **O(n²)**.
- For 3 numbers, it prints 9 results.

### O(n³) as an Extra Pattern

If three nested loops all depend on the input size, the work can become **O(n³)**.

```python
# Store numbers in a list
numbers = [1, 2, 3]

# First loop depends on n
for i in numbers:
    # Second loop also depends on n
    for j in numbers:
        # Third loop also depends on n
        for k in numbers:
            # Print one triple combination
            print(i, j, k)
```

**How the code works:**

- First loop: `n` times.
- Second loop: `n` times for each first-loop value.
- Third loop: `n` times for each second-loop value.
- Total work becomes `n × n × n`.

### Fixed Inner Loop Nuance

Not every nested loop automatically changes the final Big-O by the same amount. If an inner loop always runs a fixed number of times, it acts like constant work.

```python
# Store a growing list
numbers = [10, 20, 30, 40]

# Store a fixed list with only two values
fixed_values = [1, 2]

# Loop through all numbers
for number in numbers:
    # Loop through only two fixed values
    for value in fixed_values:
        # Print the pair
        print(number, value)
```

**How the code works:**

- The outer loop grows with `n`.
- The inner loop always runs only 2 times.
- So the growth is still mainly based on `n`, not `n²`.

---

## How to Identify Simple Big-O Patterns

Use this quick checklist:

- No loop over growing data and direct access only: usually **O(1)**.
- One loop over all items: usually **O(n)**.
- Two nested loops over the same growing input: usually **O(n²)**.
- Three nested loops over the same growing input: usually **O(n³)**.
- An `if` inside a loop does not automatically change Big-O; the loop count matters more.
- A `break` can stop early in some cases, but worst-case analysis still checks the maximum possible work.

---

## Practice Activity: Label the Complexity

Read each idea and identify the Big-O.

| Code Idea | Big-O | Reason |
|---|---|---|
| Access `numbers[0]` | **O(1)** | Direct access to one position |
| Sum every value in a list | **O(n)** | One loop over all values |
| Print every number with every number | **O(n²)** | Two nested loops over the list |
| Print every shirt with every pant | **O(n × m)** | One loop depends on shirts, one on pants |

---

## Debugging Nested Programs

- Print loop variables like `i` and `j` to see the order clearly.
- Test with small inputs first, such as 2 shirts and 3 pants.
- Check indentation carefully because Python uses indentation to decide block structure.
- Keep counters in the correct place: outside both loops for a grand total, inside the outer loop for row-wise totals.
- Estimate iterations before running large nested loops.

---

## Key Takeaways

- **Nested conditionals** help when one decision depends on another decision.
- **Nested loops** help process combinations, 2D lists, and repeated repeated work.
- The inner loop completes fully for every outer loop iteration.
- **Best, average, and worst case** describe how code behaves in different input situations.
- **Big-O** helps you quickly recognise whether code is constant, linear, quadratic, or worse as data grows.

These ideas prepare you to reason about algorithms more confidently. As programs become larger, choosing the right loop and condition structure becomes important for writing readable and efficient code.

---

## Important Commands, Libraries, and Terminologies Used

| Term / Concept | Meaning |
|---|---|
| `if` | Runs a block only when a condition is true |
| `elif` | Checks another condition after a previous `if` fails |
| `else` | Runs when previous conditions fail |
| Nested conditional | A conditional block inside another conditional block |
| Nested loop | A loop inside another loop |
| Outer loop | The loop that contains another loop |
| Inner loop | The loop written inside another loop |
| `for` loop | Repeats work over a sequence |
| `while` loop | Repeats work while a condition remains true |
| `range()` | Generates a sequence of numbers for looping |
| `continue` | Skips the current loop iteration |
| `break` | Stops the current loop |
| 2D list | A list of lists, like rows and columns |
| Matrix | A table-like arrangement of values |
| `enumerate()` | Gives index and value together while looping |
| `.items()` | Gives key-value pairs from a dictionary |
| Big-O notation | A way to describe how code grows with input size |
| O(1) | Constant time |
| O(n) | Linear time |
| O(n²) | Quadratic time |
| O(n³) | Cubic time |
| Best case | Minimum work for a lucky input |
| Average case | Typical or middle-level work |
| Worst case | Maximum work the code may need |
