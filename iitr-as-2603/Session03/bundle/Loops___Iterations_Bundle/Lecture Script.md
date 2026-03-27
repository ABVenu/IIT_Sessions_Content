### Write While Loops (25 minutes)


### CS Theory Bite

> **Origin**: While loops implement **iteration**, one of the two fundamental control structures (alongside selection) that make languages **Turing complete**. Alan Turing's machine (1936) was essentially an infinite while loop.
>
> **Analogy**: A `while` loop is like a **treadmill** — you keep running as long as the condition (your energy) holds True.
>
> **Why it matters**: While loops handle situations where you don't know how many iterations are needed — user input validation, searching, etc.


### Hook (3 minutes)

**Say**: "You're trying to guess a password. You keep trying WHILE you haven't guessed it. That's a while loop - repeating code until a condition becomes False!"

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1

print("Done!")
```

### While Loop Basics (8 minutes)

**Say**: "While loops repeat code AS LONG AS a condition is True."

**Structure**:
```python
while condition:
    # Code to repeat
    # Must update variables!
```

**Simple countdown**:
```python
count = 5

while count > 0:
    print(count)
    count -= 1  # MUST update or infinite loop!

print("Blastoff!")
```

**Key Points**:
- Condition checked BEFORE each iteration
- If condition starts False, code never runs
- MUST update variables or loop runs forever
- Use when you don't know how many times to loop

**Infinite loop danger**:
```python
# BAD - infinite loop!
x = 0
while x < 10:
    print(x)
    # Forgot to update x!
```

### Input Validation Pattern (6 minutes)

**Say**: "While loops are perfect for getting valid input from users!"

```python
age = int(input("Enter your age (0-120): "))

while age < 0 or age > 120:
    print("Invalid! Must be 0-120")
    age = int(input("Try again: "))

print(f"Valid age: {age}")
```

**Real-World**: Login system
```python
password = input("Enter password: ")

while len(password) < 8:
    print("Too short! Password must be 8+ characters")
    password = input("Try again: ")

print("Password accepted!")
```

### Advanced Examples (4 minutes)

**Say**: "Let's build a number guessing game!"

```python
secret = 42
guess = int(input("Guess my number (1-100): "))

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Correct! You win!")
```

### Common Patterns (3 minutes)

**Accumulator pattern**:
```python
total = 0
num = int(input("Enter number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))

print(f"Total: {total}")
```

**Counter pattern**:
```python
count = 0
num = 1

while num <= 100:
    count += 1
    num += 1

print(f"Counted to 100: {count} times")
```

### Practice (2 minutes)

New Year countdown:
```python
count = 10

while count > 0:
    print(count)
    count -= 1

print("Happy New Year!")
```


---

### Control Loops with Break (25 minutes)


### CS Theory Bite

> **Origin**: `break` implements **early termination** — exiting a loop before its natural end. This pattern uses **sentinel values** in algorithms — stop when you find what you're looking for.
>
> **Analogy**: `break` is like pulling the **emergency brake** — the loop stops immediately, no questions asked.
>
> **Why it matters**: Without `break`, you'd need complex boolean flags to exit loops — `break` keeps code clean.


### Hook (3 minutes)

**Say**: "You're searching for your keys. You check rooms one by one. BREAK means you found them - stop searching!"

```python
rooms = ["kitchen", "bedroom", "bathroom", "garage"]

for room in rooms:
    print(f"Checking {room}...")
    if room == "bathroom":
        print("Found keys!")
        break  # Stop searching!

print("Search complete!")
```

### Break Basics (6 minutes)

**Say**: "break exits a loop immediately, even if the condition is still True."

```python
count = 0

while count < 10:
    print(count)
    if count == 5:
        print("Breaking out!")
        break  # Exit loop NOW
    count += 1

print("After loop")  # This runs
```

**Key Points**:
- `break` exits the loop immediately
- Skips remaining code in loop
- Continues execution after the loop
- Works in both while and for loops

```python
while True:  # Infinite loop!
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted!")
        break  # Exit the infinite loop
    print("Wrong password")
```

### Break with While Loops (6 minutes)

**Say**: "Perfect for input validation with an escape!"

```python
while True:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age can't be negative!")
        continue  # Skip to next iteration

    if age > 120:
        print("Invalid age!")
        continue

    # Valid age!
    break

print(f"Age accepted: {age}")
```

**Real-World**: Search pattern
```python
numbers = [10, 25, 30, 15, 40]
target = 30
found = False

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not in list")
```

### Loop-Else Clause (6 minutes)

**Say**: "else after a loop runs ONLY if break was never called!"

```python
for item in sequence:
    if condition:
        break
else:
    # Runs if NO break occurred
    print("Loop completed normally")
```

**Example**: Finding a prime number
```python
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is prime!")
```

**Real-World**: Authentication
```python
users = ["alice", "bob", "charlie"]
username = input("Username: ")

for user in users:
    if user == username:
        print("User found!")
        break
else:
    print("User not found - creating new account")
```

### Nested Loops with Break (4 minutes)

**Say**: "break only exits the INNER loop, not the outer one!"

```python
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        print(f"  Inner loop: {j}")
        if j == 1:
            break  # Only breaks INNER loop
    print("Outer continues...")
```

### Practice (3 minutes)

Find first negative number:
```python
numbers = [5, 10, -3, 8, 12]

for num in numbers:
    if num < 0:
        print(f"First negative: {num}")
        break
else:
    print("No negative numbers found")
```


---

### Control Loops with Continue (25 minutes)


### CS Theory Bite

> **Origin**: `continue` implements the **filter pattern** — skip items that don't meet criteria and process only those that do. It's the loop equivalent of "next, please!"
>
> **Analogy**: `continue` is like a **bouncer checking IDs** — "You don't qualify? Skip. Next person." The line keeps moving.
>
> **Why it matters**: `continue` avoids deep nesting — instead of wrapping code in `if`, just skip the unwanted cases.


### Hook (3 minutes)

**Say**: "You're looking through a list of students. You want to print everyone EXCEPT those who are absent. That's continue - skip some, keep going!"

```python
# WITH continue - skip evens, keep going
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip evens
    print(num)  # Only odds print

print("Loop finished!")
# Output: 1 3 5 7 9
```

### Continue Basics (6 minutes)

**Say**: "continue skips the rest of the current iteration and jumps to the next one."

```python
while condition:
    # code
    if skip_condition:
        continue  # Jump to next iteration NOW
    # This code is skipped if continue executes
    # more code
```

**Key Points**:
- `continue` skips remaining code in current iteration
- Loop continues with next iteration
- Different from `break` which exits the loop entirely
- Works in both while and for loops

```python
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip when count is 3
    print(count)

# Output: 1 2 4 5 (3 is skipped!)
```

### Continue vs Break (6 minutes)

**Say**: "break EXITS the loop. continue SKIPS to next iteration."

```python
print("=== CONTINUE Demo ===")
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3, keep going
    print(i)
# Output: 1 2 4 5

print("\n=== BREAK Demo ===")
for i in range(1, 6):
    if i == 3:
        break  # Stop at 3
    print(i)
# Output: 1 2
```

**Real-World**: Processing data with errors
```python
scores = [85, 92, -1, 78, -1, 95]  # -1 means error

total = 0
count = 0

for score in scores:
    if score < 0:
        continue  # Skip error values
    total += score
    count += 1

average = total / count
print(f"Average: {average}")  # 87.5
```

### Common Patterns (4 minutes)

**Say**: "Use continue to filter out unwanted items!"

**Skip invalid data**:
```python
temperatures = [22.5, -999, 23.1, -999, 21.8, 24.2]
valid_temps = []

for temp in temperatures:
    if temp == -999:  # Error reading
        continue
    valid_temps.append(temp)

avg = sum(valid_temps) / len(valid_temps)
print(f"Average temp: {avg:.1f}°C")
```

**Process only certain items**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print only multiples of 3
for num in numbers:
    if num % 3 != 0:
        continue  # Skip non-multiples
    print(num)  # 3, 6, 9
```

### Input Validation with Continue (3 minutes)

```python
while True:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age can't be negative!")
        continue  # Ask again

    if age > 120:
        print("Invalid age!")
        continue  # Ask again

    # Valid age!
    break

print(f"Age accepted: {age}")
```

### Practice (3 minutes)

Print words longer than 3 characters:
```python
words = ["cat", "elephant", "dog", "giraffe", "ant", "bear"]

for word in words:
    if len(word) <= 3:
        continue  # Skip short words
    print(word)

# Output: elephant, giraffe, bear
```


---

### Write For Loops (20 minutes)


### CS Theory Bite

> **Origin**: For loops implement the **iterator pattern** (Gang of Four, 1994) — Python's `for` is actually a **for-each** loop, iterating over any iterable object, not just counting numbers.
>
> **Analogy**: A `for` loop is like a **conveyor belt** — items come one at a time, you process each, and it automatically stops at the end.
>
> **Why it matters**: For loops are the most common loop — 90% of iteration tasks are "do something for each item."


### Hook (2 minutes)

**Say**: "Want to print every student's name? You could copy-paste print() 30 times... or use a for loop and do it in 2 lines!"

```python
# Without for loop (while loop way)
fruits = ["apple", "banana", "orange"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# With for loop (clean!)
for fruit in fruits:
    print(fruit)
```

### For Loop Basics (6 minutes)

**Say**: "for loops automatically iterate through each item in a sequence."

```python
for item in sequence:
    # Do something with item
    # item is a variable holding current element
```

**Examples**:
```python
# List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# String (each character!)
for letter in "Python":
    print(letter)  # P y t h o n

# Tuple
coords = (10, 20, 30)
for coord in coords:
    print(coord)
```

**Key Points**:
- No manual indexing needed
- Works with lists, strings, tuples, sets, dictionaries
- Loop variable gets each item automatically
- Can't modify the original list during iteration

### Dictionary Iteration (5 minutes)

**Say**: "Dictionaries are different - you can iterate keys, values, or both!"

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Keys only (default)
for key in student:
    print(key)  # name, age, grade

# Values only
for value in student.values():
    print(value)  # Alice, 20, A

# Both keys and values
for key, value in student.items():
    print(f"{key}: {value}")
```

### Using Enumerate (4 minutes)

**Say**: "Need the index too? Use enumerate()!"

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Position {index}: {color}")

# Output:
# Position 0: red
# Position 1: green
# Position 2: blue
```

**Real-World**: Numbered list
```python
tasks = ["Buy milk", "Call mom", "Finish homework"]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
# Buy milk
# Call mom
# Finish homework
```

### Practice (3 minutes)

Sum all numbers in a list:
```python
numbers = [5, 10, 15, 20, 25]

total = 0
for num in numbers:
    total += num

print(f"Sum: {total}")  # 75
```


---

### Use Range() Function (15 minutes)


### CS Theory Bite

> **Origin**: `range()` uses **lazy evaluation** — it doesn't create a list in memory but generates numbers on demand. `range(1000000)` uses almost no memory!
>
> **Analogy**: `range()` is like a **number dispenser at a deli counter** — it gives you the next number when asked, not all numbers at once.
>
> **Why it matters**: `range()` is the bridge between counting loops (C-style) and Python's for-each — efficient numeric iteration.


### Hook (2 minutes)

**Say**: "Need to count 1 to 100? You could type [1, 2, 3, ... 100]. Or use range() and do it automatically!"

```python
# Manual way (tedious!)
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)

# Range way (automatic!)
for num in range(1, 11):
    print(num)
```

### Range Basics (5 minutes)

**Say**: "range() generates numbers on the fly. Three ways to use it!"

```python
# range(stop) - starts at 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - custom start
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step) - custom increment
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

**Key Points**:
- Stop value is NOT included
- Default start is 0
- Default step is 1
- Can count backwards with negative step

```python
# Counting backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### Common Patterns (4 minutes)

**Say**: "Here are the patterns you'll use most!"

```python
# Count exactly n times
for i in range(10):
    print("Hello!")  # Prints 10 times

# to n inclusive
n = 5
for i in range(1, n+1):
    print(i)  # 1, 2, 3, 4, 5

# Iterate through indices
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Odd numbers
for num in range(1, 21, 2):
    print(num)  # 1, 3, 5, ..., 19

# Even numbers
for num in range(0, 21, 2):
    print(num)  # 0, 2, 4, ..., 20
```

### Real-World Application (2 minutes)

**Multiplication table**:
```python
n = 7

print(f"Multiplication table for {n}:")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
```

### Practice (2 minutes)

Sum numbers 1 to 50:
```python
total = 0
for num in range(1, 51):
    total += num

print(f"Sum: {total}")  # 1275
```


---

### Control For Loops with Break and Continue (20 minutes)


### CS Theory Bite

> **Origin**: `break` and `continue` in for loops enable **early termination optimization** — stop searching once found. This turns O(n) worst-case into O(1) best-case.
>
> **Analogy**: Like **searching a phone book** — once you find the name (break), you stop flipping pages. Or skip entries that aren't relevant (continue).
>
> **Why it matters**: Efficient loops don't do unnecessary work — `break` and `continue` are optimization tools.


### Hook (3 minutes)

**Say**: "Imagine you're looking for your keys in a messy room. You check drawer after drawer. What happens when you find them? You BREAK - stop searching. What if a drawer is locked? You CONTINUE - skip it and check the next one!"

```python
drawers = ["socks", "locked", "books", "keys", "clothes"]

for drawer in drawers:
    if drawer == "locked":
        print(f"Skipping {drawer}")
        continue  # Skip this one
    if drawer == "keys":
        print("Found keys!")
        break  # Stop searching!
    print(f"Checking {drawer}...")

# Output:
# Checking socks...
# Skipping locked
# Checking books...
# Found keys!
```

### The Break Statement (5 minutes)

**Say**: "break exits the loop immediately."

```python
for item in collection:
    if condition:
        break  # Exit loop NOW
    # This code runs only if break doesn't execute
```

**Example - Find first even number**:
```python
numbers = [1, 3, 5, 8, 9, 11, 13]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even: {num}")
        break
    print(f"Checking {num}...")

# Output:
# Checking 1...
# Checking 3...
# Checking 5...
# Found first even: 8
```

### The Continue Statement (5 minutes)

**Say**: "continue skips the rest of this iteration and moves to the next."

```python
for item in collection:
    if condition:
        continue  # Skip rest, go to next
    # This code is skipped when continue executes
```

**Example - Print only positive numbers**:
```python
numbers = [5, -2, 10, -7, 3, 8]

for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)

# Output: 5 10 3 8
```

### Break vs Continue (3 minutes)

```python
# BREAK - Exits the entire loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2

# CONTINUE - Skips to next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4 (3 is skipped!)
```

### The For-Else Clause (4 minutes)

**Say**: "else after a loop runs ONLY if break was never called!"

```python
for item in collection:
    if condition:
        break
else:
    # Runs if NO break occurred
    print("Loop completed normally")
```

**Example - Search with feedback**:
```python
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not in list")

# Output: 4 not in list
```

**Real-World - Prime number check**:
```python
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is prime!")
```


---

### Write Nested Loops (20 minutes)


### CS Theory Bite

> **Origin**: Nested loops create **O(n²) complexity** — the foundation of algorithms like matrix operations, bubble sort, and grid traversals. Understanding nesting is key to **algorithmic thinking**.
>
> **Analogy**: Nested loops are like a **clock** — the minute hand (inner loop) completes a full cycle for every tick of the hour hand (outer loop).
>
> **Why it matters**: Matrix operations, pattern printing, and data cross-referencing all require nested iteration.


### Hook (3 minutes)

**Say**: "Imagine seating guests at a wedding with 5 tables, each with 6 chairs. How do you assign seat numbers? Table 1: seats 1-6. Table 2: seats 1-6. That's nested loops - a loop inside a loop!"

```python
for table in range(1, 6):      # 5 tables
    for seat in range(1, 7):    # 6 seats per table
        print(f"Table {table}, Seat {seat}")
```

### What are Nested Loops (4 minutes)

**Say**: "A nested loop is a loop inside another loop. The inner loop runs COMPLETELY for EACH iteration of the outer loop."

```python
for outer in range(3):      # Runs 3 times
    print(f"Outer: {outer}")
    for inner in range(2):  # Runs 2 times FOR EACH outer
        print(f"  Inner: {inner}")

# Output:
# Outer: 0
#   Inner: 0
#   Inner: 1
# Outer: 1
#   Inner: 0
#   Inner: 1
# Outer: 2
#   Inner: 0
#   Inner: 1
```

**Key Points**:
- Inner loop completes all iterations before outer moves forward
- Total iterations = outer × inner (3 × 2 = 6 in example above)
- Can have multiple levels (but keep it simple!)

### Simple Patterns (5 minutes)

**Rectangle pattern**:
```python
# rows, 6 columns
for row in range(4):
    for col in range(6):
        print('*', end=' ')
    print()  # New line after each row

# Output:
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
```

**Multiplication table**:
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()

# Output:
# ×1= 1  1×2= 2  1×3= 3  1×4= 4  1×5= 5
# ×1= 2  2×2= 4  2×3= 6  2×4= 8  2×5=10
# ...
```

### Working with 2D Lists (4 minutes)

**Say**: "Nested loops are perfect for 2D lists (lists of lists)!"

```python
# Create a 3x3 matrix of zeros
matrix = []

for row in range(3):
    current_row = []
    for col in range(3):
        current_row.append(0)
    matrix.append(current_row)

# Result: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**Iterate through 2D list**:
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for item in row:
        print(item, end=' ')
    print()

# Output:
# 2 3
# 5 6
# 8 9
```

### Advanced Patterns (2 minutes)

**Triangle pattern**:
```python
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Practice (2 minutes)

Print all pairs from two lists:
```python
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"{color}-{size}")

# Output:
# red-S
# red-M
# red-L
# blue-S
# blue-M
# blue-L
```


---

