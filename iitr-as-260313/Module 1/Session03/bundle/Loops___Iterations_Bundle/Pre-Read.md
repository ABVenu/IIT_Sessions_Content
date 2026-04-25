# Writing While Loops

## What You'll Learn
In this lesson, you'll learn how to use while loops to repeat code as long as a condition remains True. This is one of the most fundamental tools for making programs do repetitive tasks automatically.

## Why This Matters
Imagine you're building:
- A password checker that keeps asking until the user enters the correct password
- A game that runs until the player loses all lives
- A calculator app that keeps running until the user chooses "quit"
- A shopping cart that lets users add items until they're done

Without loops, you'd have to copy-paste the same code hundreds of times. Loops let you write the code once and run it as many times as needed!

---

## What is a While Loop?

A **while loop** repeats a block of code **as long as** a condition is True. Think of it like telling Python: "Keep doing this while this condition is true."

```python
while condition:
    # Code to repeat
```

The loop checks the condition **before** each repetition. If True, it runs the code. If False, it stops.

---

## Simple Example: Counting

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1

print("Done!")
```

**Output:**
1
2
3
4
5
Done!

**How it works:**
1. Start: `count` is 1
2. Check: Is `count <= 5`? Yes (1 <= 5) → Run code
3. Print 1, then `count` becomes 2
4. Check: Is `count <= 5`? Yes (2 <= 5) → Run code
5. Print 2, then `count` becomes 3
6. ... continues ...
7. Check: Is `count <= 5`? Yes (5 <= 5) → Run code
8. Print 5, then `count` becomes 6
9. Check: Is `count <= 5`? No (6 > 5) → Stop loop
10. Print "Done!"

---

## Real-World Example: Password Validation

```python
password = ""

while len(password) < 8:
    password = input("Enter password (min 8 characters): ")
    if len(password) < 8:
        print("Too short! Try again.")

print("Password accepted!")
```

**How this works:**
- Keeps asking for a password **while** it's too short
- Once user enters 8+ characters, condition becomes False and loop stops
- No matter how many times they enter a wrong password, the code is written once!

---

## The Critical Part: Updating the Condition

**WARNING:** The condition must eventually become False, or your loop will run forever!

### Infinite Loop (BAD)

```python
count = 1

while count <= 5:
    print(count)
    # Forgot to change count!
    # count will always be 1, so count <= 5 is always True
    # Loop never stops!
```

### Correct Loop (GOOD)

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1  # This makes condition eventually False!
```

**Key rule:** Your loop must change something that affects the condition, or it will run forever.

---

## Another Example: Game Menu

```python
choice = ""

while choice != "quit":
    print("\n--- Game Menu ---")
    print("1. Start Game")
    print("2. View Score")
    print("Type 'quit' to exit")

    choice = input("Your choice: ")

    if choice == "1":
        print("Starting game...")
    elif choice == "2":
        print("Your score: 100")
    elif choice == "quit":
        print("Thanks for playing!")
    else:
        print("Invalid choice")
```

**This keeps showing the menu until** the user types "quit".

---

## While Loops vs If Statements

### If Statement (Runs Once)

```python
score = 50

if score < 100:
    print("Keep playing")  # Prints once
```

### While Loop (Repeats)

```python
score = 50

while score < 100:
    print("Keep playing")  # Prints repeatedly
    score = score + 10     # Must update score!
```

**Key difference:**
- `if` checks once and moves on
- `while` checks repeatedly and keeps running

---

## Try It Yourself (Before Class)

Run this code and observe the output:

```python
number = 1

while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    number = number + 1

print("Finished checking numbers!")
```

**Expected output:** It will print whether each number from 1 to 10 is even or odd.

**Try modifying:**
1. Change `number <= 10` to `number <= 3` - what happens?
2. Change `number = number + 1` to `number = number + 2` - what happens?
3. Comment out the `number = number + 1` line - what happens? (Stop it with Ctrl+C!)

---

## Common While Loop Patterns

### Pattern 1: Counting

```python
count = 0
while count < 5:
    print("Hello")
    count += 1  # += is shorthand for count = count + 1
```

### Pattern 2: User Input Until Valid

```python
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))
```

### Pattern 3: Keep Running Until Command

```python
command = ""
while command != "stop":
    command = input("Enter command (type 'stop' to quit): ")
    print(f"You entered: {command}")
```

---

## Warning: Infinite Loops

If you accidentally create an infinite loop, your program will hang. Here's what to do:

**How to stop a stuck program:**
- Press `Ctrl + C` (or `Cmd + C` on Mac) in the terminal
- Or close the terminal window

**Common infinite loop mistake:**

```python
x = 5
while x > 0:
    print("Hello")
    # Forgot to change x!
```

This will print "Hello" forever because `x` is always 5, and 5 > 0 is always True.

---

## Key Takeaways

Before class, remember:
1. **While loops repeat** - as long as condition is True
2. **Condition checked first** - before each iteration
3. **Must update** - something in the loop must make condition False eventually
4. **Infinite loops are bad** - always make sure your condition can become False
5. **Great for user input** - when you don't know how many times to repeat

## Questions to Think About

Come to class ready to discuss:
- When would you use a while loop instead of just writing code multiple times?
- What happens if the condition is False from the start?
- How do you decide what condition to use for a while loop?

## What's Next?

In the live session, we'll:
- Write while loops for various scenarios
- Learn how to avoid infinite loops
- Use break and continue statements with while loops
- Build interactive programs with while loops
- Practice debugging loop problems

See you in class!


---

# Controlling While Loops Using Break Statement

## What You'll Learn
In this lesson, you'll learn how to use the `break` statement to exit a loop early, before the loop condition becomes False. This gives you more control over when your loops stop.

## What is Break?

`break` lets you **exit a loop immediately**, even if the loop condition is still True. It's like an emergency stop button!

### Simple Analogy

Think of break like **"found what I'm looking for, stop searching!"**:
- Looking through a playlist for a song. **Found it? BREAK - stop scrolling!**
- Testing passwords. **Correct one found? BREAK - stop trying!**
- Checking inventory items. **Found defect? BREAK - inspection failed!**

## Why This Matters
Sometimes you need to stop a loop immediately when something specific happens:
- A user types "quit" in a menu system
- You find what you're searching for in a list
- An error occurs and you need to stop processing
- A maximum number of attempts is reached

The `break` statement lets you exit the loop instantly, without waiting for the normal loop condition to become False.

---

## What is the Break Statement?

The **break statement** immediately exits the current loop, no matter what the loop condition says.

```python
while condition:
    # Some code
    if some_special_condition:
        break  # Exit loop right now!
    # More code
```

When Python hits `break`, it:
1. **Stops the loop immediately**
2. **Jumps to the first line after the loop**
3. **Doesn't check the loop condition again**

---

## Simple Example: Exit on Command

```python
while True:  # This would normally run forever!
    command = input("Enter command (or 'quit' to exit): ")

    if command == "quit":
        break  # Exit the loop

    print(f"You entered: {command}")

print("Program ended")
```

**Output example:**
Enter command (or 'quit' to exit): hello
You entered: hello
Enter command (or 'quit' to exit): test
You entered: test
Enter command (or 'quit' to exit): quit
Program ended

**Key point:** We used `while True` (infinite loop) but `break` stops it when needed.

---

## When to Use Break

### Use Case 1: Search and Stop

When you're looking for something and want to stop once you find it:

```python
numbers = [3, 7, 2, 9, 5, 11, 8]
target = 9
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at position {index}!")
        break  # No need to keep searching
    index += 1
```

### Use Case 2: Password Attempts

Limit the number of tries:

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == "secret123":
        print("Access granted!")
        break  # Correct password, exit loop

    attempts += 1
    remaining = max_attempts - attempts
    print(f"Wrong! {remaining} attempts remaining")

if password != "secret123":
    print("Account locked")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
total = 0

while True:
    number = input("Enter a number (or 'done' to finish): ")

    if number == "done":
        break

    total += int(number)
    print(f"Running total: {total}")

print(f"Final total: {total}")
```

**Try:**
1. Enter a few numbers, then type "done"
2. What happens if you type "done" immediately?

---

## Key Takeaways

Before class, remember:
1. **break exits immediately** - stops the loop right away
2. **No condition check** - doesn't wait for normal loop condition
3. **Great with while True** - creates controlled infinite loops
4. **Common use cases** - search-and-stop, user input validation, menu systems

## What's Next?

In the live session, we'll:
- Practice using break in various scenarios
- Understand when to use break vs. changing the loop condition
- Build programs with controlled loop exits

See you in class!


---

# Controlling While Loops Using Continue Statement

## What is Continue?

`continue` skips the **rest of the current loop iteration** and jumps to the next one. Unlike `break` (which exits the loop), continue just skips this round.

### Simple Analogy

Think of continue like **skipping a song**:
- Playing playlist → Don't like this song → Skip to next (continue) → Keep playing
- vs. Don't like playlist → Stop playback (break)

Or like **skipping questions on a test**:
- Question too hard? Skip it (continue), answer next question
- vs. Give up on test entirely (break)

## What You'll Learn
In this lesson, you'll learn how to use the `continue` statement to skip the rest of the current loop iteration and jump to the next one. This is useful when you want to skip certain cases but keep the loop running.

## Why This Matters
Sometimes you want to skip specific iterations without stopping the entire loop:
- Skipping invalid data while processing a list
- Filtering out unwanted items
- Ignoring certain conditions while continuing with others
- Processing only items that meet certain criteria

The `continue` statement gives you fine-grained control over individual loop iterations.

---

## What is the Continue Statement?

The **continue statement** skips the rest of the current iteration and immediately jumps to the next iteration of the loop.

```python
while condition:
    # Some code
    if skip_this_iteration:
        continue  # Skip rest of this iteration, go to next
    # This code is skipped when continue runs
```

**Key difference from break:**
- `break` → **Exit the entire loop**
- `continue` → **Skip to the next iteration**

---

## Simple Example: Skip Even Numbers

```python
number = 0

while number < 5:
    number += 1
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

**Output:**
1
3
5

**What happens:**
1. number = 1 → not even → print 1
2. number = 2 → even → `continue` skips print
3. number = 3 → not even → print 3
4. number = 4 → even → `continue` skips print
5. number = 5 → not even → print 5

---

## When to Use Continue

### Use Case 1: Filtering Input

Skip invalid entries:

```python
total = 0
count = 0

while count < 5:
    value = input("Enter a positive number: ")

    if int(value) <= 0:
        print("Invalid! Must be positive.")
        continue  # Skip to next iteration, don't count this

    total += int(value)
    count += 1  # Only increment for valid input

print(f"Average: {total / count}")
```

### Use Case 2: Processing Only Specific Items

```python
names = ["Alice", "Bob", "", "Charlie", "", "David"]
index = 0

while index < len(names):
    name = names[index]
    index += 1

    if name == "":
        continue  # Skip empty names

    print(f"Hello, {name}!")
```

**Output:**
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, David!

---

## Break vs Continue

### Break: Stop Everything

```python
for i in range(5):
    if i == 2:
        break  # Exit loop completely
    print(i)
# Output: 0, 1
```

### Continue: Skip One Iteration

```python
for i in range(5):
    if i == 2:
        continue  # Skip only i=2
    print(i)
# Output: 0, 1, 3, 4
```

---

## Real-World Example: Menu with Validation

```python
while True:
    print("\n1. Add item")
    print("2. View items")
    print("3. Quit")

    choice = input("Choose: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue  # Skip rest, show menu again

    if choice == "1":
        print("Adding item...")
    elif choice == "2":
        print("Viewing items...")
    elif choice == "3":
        print("Goodbye!")
        break
```

---

## Try It Yourself (Before Class)

Run this code:

```python
count = 0

while count < 10:
    count += 1

    if count % 3 == 0:
        continue

    print(count)
```

**Questions:**
1. What numbers get printed?
2. What numbers are skipped?
3. Try changing `count % 3 == 0` to `count == 5` - what happens?

---

## Key Takeaways

Before class, remember:
1. **continue skips to next iteration** - doesn't exit loop
2. **Rest of iteration is skipped** - code after continue doesn't run
3. **Loop keeps running** - unlike break which exits
4. **Great for filtering** - skip unwanted cases
5. **Loop condition still checked** - after each iteration

## What's Next?

In the live session, we'll:
- Practice using continue in various scenarios
- Learn when to use continue vs break
- Combine continue with break for complex logic
- Build programs with sophisticated loop control

See you in class!


---

# Writing For Loops to Iterate Over Sequences

## What is a For Loop?

For loops let you **process each item** in a collection automatically. Think: "For each item, do this..."

### Simple Analogy

Think of for loops like **going through a checklist**:
- "For each task on my to-do list, mark it complete"
- "For each friend, send birthday message"
- "For each photo, apply filter"

You work through the whole list, one item at a time!

## What You'll Learn
In this lesson, you'll learn how to use for loops to iterate over sequences like lists, strings, and other collections. For loops make it easy to process each item in a collection automatically.

## Why This Matters
For loops are one of the most commonly used features in Python:
- Process every student in a class list
- Check every character in a password
- Calculate the total of all prices in a shopping cart
- Display every item in a menu

For loops eliminate the need to manually access each element by index.

---

## What is a For Loop?

A **for loop** automatically iterates over each item in a sequence (list, string, range, etc.) and runs code for each item.

```python
for item in sequence:
    # Do something with item
```

**Key differences from while loops:**
- **While loop**: "Keep going while condition is True" (you control when it stops)
- **For loop**: "Go through each item in this sequence" (automatic iteration)

---

## Simple Examples

### Example 1: Iterate Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**
apple
banana
cherry

**What happens:**
1. Take first item ("apple") and run the code
2. Take second item ("banana") and run the code
3. Take third item ("cherry") and run the code
4. No more items → stop

### Example 2: Iterate Over a String

```python
word = "Python"

for letter in word:
    print(letter)
```

**Output:**
P
y
t
h
o
n

---

## For Loops vs While Loops

### Using While (More Code)

```python
fruits = ["apple", "banana", "cherry"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

### Using For (Cleaner)

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**For loops are better when:**
- You need to process every item in a sequence
- You don't need the index
- You want cleaner, more readable code

---

## Real-World Examples

### Example 1: Calculate Total Price

```python
prices = [19.99, 5.50, 12.00, 8.75]
total = 0

for price in prices:
    total += price

print(f"Total: ${total}")  # Total: $46.24
```

### Example 2: Count Vowels in a String

```python
text = "Hello World"
vowel_count = 0

for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")  # Vowels: 3
```

### Example 3: Print Numbered List

```python
students = ["Alice", "Bob", "Charlie"]

for student in students:
    print(f"Student: {student}")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
numbers = [10, 20, 30, 40, 50]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)
```

**Questions:**
1. What does this code do?
2. What will be in the `doubled` list?
3. Try changing `num * 2` to `num + 5` - what happens?

---

## Key Takeaways

Before class, remember:
1. **For loops iterate sequences** - automatically go through each item
2. **Cleaner than while** - for sequences you know the length of
3. **Works with many types** - lists, strings, ranges, tuples, etc.
4. **Loop variable** - gets each item automatically
5. **No index needed** - unless you specifically want it

## What's Next?

In the live session, we'll:
- Practice iterating over different data types
- Learn to use the range() function with for loops
- Understand when to use for vs while loops
- Combine for loops with break and continue

See you in class!


---

# Using Range() Function for Numeric Iteration

## What is range()?

Range is Python's **smart number generator**. Instead of creating all numbers at once, it generates them one-by-one as needed - like a vending machine dispensing one item at a time!

### Simple Analogy

Think of range like a **number counter at a deli**:
- Set it to count 1 to 100
- Numbers appear one at a time (not all at once!)
- Takes up almost no space (doesn't print 100 tickets upfront)
- You can start anywhere, stop anywhere, skip numbers

This makes counting billions of numbers possible without running out of memory!

## What You'll Learn
In this lesson, you'll learn how to use Python's `range()` function to generate sequences of numbers for use in for loops. This is essential for when you need to repeat code a specific number of times or iterate over numbers.

## Why This Matters
The `range()` function is one of the most commonly used tools in Python:
- Repeat an action N times ("do this 10 times")
- Count from 1 to 100
- Generate even/odd numbers
- Create countdowns
- Access list elements by index

---

## What is range()?

`range()` generates a sequence of numbers. It doesn't create a list in memory - it generates numbers on-demand, which is efficient.

### Three Ways to Use range()

**1. range(stop)** - Count from 0 to stop-1

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4 (stops before 5!)
```

**2. range(start, stop)** - Count from start to stop-1

```python
for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5 (stops before 6!)
```

**3. range(start, stop, step)** - Count with custom increment

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8 (every 2nd number)
```

---

## Important: range() Stops BEFORE the End

The stop value is **exclusive** (not included):

```python
range(5)      # 0, 1, 2, 3, 4 (NOT 5!)
range(1, 4)   # 1, 2, 3 (NOT 4!)
range(0, 10, 2) # 0, 2, 4, 6, 8 (NOT 10!)
```

**Why?** This makes it easier to work with list indices, which start at 0.

---

## Common Patterns

### Pattern 1: Repeat N Times

```python
# Print "Hello" 5 times
for i in range(5):
    print("Hello")
```

### Pattern 2: Count from 1 to N

```python
# Count 1 to 10
for i in range(1, 11):  # Note: 11, not 10!
    print(i)
```

### Pattern 3: Even Numbers

```python
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10
```

### Pattern 4: Countdown

```python
# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

---

## Real-World Examples

### Example 1: Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Example 2: Access List by Index

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Item {i}: {fruits[i]}")
# Output:
# Item 0: apple
# Item 1: banana
# Item 2: cherry
```

### Example 3: Sum of First N Numbers

```python
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} numbers: {total}")
# Sum of first 10 numbers: 55
```

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 6):
    print("*" * i)
```

**Questions:**
1. What pattern does this create?
2. Try changing `range(1, 6)` to `range(5, 0, -1)` - what happens?
3. Change `"*" * i` to `str(i) * i` - what do you get?

---

## Key Takeaways

Before class, remember:
1. **range(n)** - 0 to n-1
2. **range(start, stop)** - start to stop-1
3. **range(start, stop, step)** - custom increment
4. **Stop is exclusive** - never includes the stop value
5. **Efficient** - doesn't create a list in memory

## What's Next?

In the live session, we'll:
- Practice all three forms of range()
- Use range() to solve real problems
- Combine range() with lists and other data structures
- Learn advanced range() techniques

See you in class!


---

# Controlling For Loops with Break and Continue

## Why Control Flow in For Loops?

For loops normally process every single item in a sequence. But real-world programs need **intelligent iteration**:
- **Search**: Stop once you find what you're looking for (don't waste time!)
- **Filtering**: Skip invalid/unwanted items but keep processing others
- **Validation**: Exit immediately when you detect an error

Break and continue give you this power - making loops smart, not just repetitive!

### Simple Analogy

Think of break and continue like **instructions to a mail carrier**:
- **Break**: "Stop delivering mail on this street" (emergency, road closed)
- **Continue**: "Skip this house but keep delivering to others" (no mailbox, dog loose)

The mail carrier doesn't blindly follow the route - they adapt based on conditions!

## What You'll Learn
In this lesson, you'll learn how to use `break` and `continue` statements with for loops to control loop execution. These work the same way as with while loops but are commonly used with for loops in Python.

## Why This Matters
Just like with while loops, you often need to:
- Exit a loop early when you find what you're looking for
- Skip certain items in a sequence
- Handle special cases without breaking your loop logic

Break and continue give you fine control over for loop execution.

---

## Quick Recap

**break** → Exit the loop completely
**continue** → Skip to the next iteration

These work identically in both while and for loops!

---

## Using Break in For Loops

### Example 1: Search and Stop

```python
numbers = [3, 7, 12, 9, 15, 2]

for num in numbers:
    if num > 10:
        print(f"Found number greater than 10: {num}")
        break  # Stop searching
    print(f"Checking {num}...")

# Output:
# Checking 3...
# Checking 7...
# Found number greater than 10: 12
```

### Example 2: Early Exit on Invalid Data

```python
scores = [95, 87, 102, 76, 88]  # 102 is invalid!

for score in scores:
    if score > 100:
        print("Error: Invalid score!")
        break
    print(f"Valid score: {score}")
```

---

## Using Continue in For Loops

### Example 1: Skip Specific Items

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Output: 1, 3, 5, 7, 9 (only odd numbers)
```

### Example 2: Filter and Process

```python
words = ["hello", "", "world", "", "python"]

for word in words:
    if word == "":
        continue  # Skip empty strings
    print(f"Word: {word}")

# Output:
# Word: hello
# Word: world
# Word: python
```

---

## Combining Break and Continue

```python
numbers = [5, -2, 10, -7, 15, 20, -3]

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers

    if num > 15:
        print(f"Found large number: {num}")
        break  # Stop at first number > 15

    print(num)

# Output:
# 
# 
# 
# Found large number: 20
```

---

## Real-World Example: Validating Passwords

```python
passwords = ["abc", "secure123", "xyz", "password456"]

for password in passwords:
    if len(password) < 5:
        continue  # Skip short passwords

    if "456" in password:
        print(f"Warning: Weak password found - {password}")
        break

    print(f"Valid: {password}")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

**Questions:**
1. What numbers get printed?
2. Why is 5 skipped?
3. Why do numbers after 8 not print?

---

## Key Takeaways

Before class, remember:
1. **break in for loops** - exits the loop completely
2. **continue in for loops** - skips to next item in sequence
3. **Same as while loops** - behavior is identical
4. **Common patterns** - search-and-stop, filtering, validation
5. **Can combine** - use both in the same loop for complex logic

## What's Next?

In the live session, we'll:
- Practice break and continue with for loops
- Learn when to use each statement
- Build programs with sophisticated loop control
- Understand nested loops with break/continue

See you in class!


---

# Writing Nested Loops for Multi-Level Iteration

## What are Nested Loops?

Nested loops are **loops within loops** - allowing you to work with data that has multiple dimensions or levels. Think of them as tools for handling **grids**, **tables**, and **combinations**.

### Simple Analogy

Think of nested loops like **organizing a deck of cards**:
- **Outer loop**: Go through each suit (Hearts, Diamonds, Clubs, Spades)
- **Inner loop**: Go through each card in that suit (Ace, 2, 3... King)
- **Result**: For each suit, you process ALL 13 cards before moving to the next suit

Or like **filling ice cube trays**:
- **Outer loop**: Pick up each tray
- **Inner loop**: Fill each cube in that tray
- **Pattern**: Fill all cubes in tray 1, then move to tray 2

The inner loop **completely finishes** for each iteration of the outer loop!

## What You'll Learn
In this lesson, you'll learn how to write loops inside other loops (nested loops) to work with multi-dimensional data or create patterns. This is essential for working with grids, tables, and complex iterations.

## Why This Matters
Nested loops are used everywhere in programming:
- Creating multiplication tables
- Drawing patterns (stars, pyramids, grids)
- Processing 2D game boards (chess, tic-tac-toe)
- Working with rows and columns in spreadsheets
- Comparing every item with every other item

---

## What are Nested Loops?

A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

```python
for outer in outer_sequence:
    for inner in inner_sequence:
        # This runs for every combination of outer and inner
```

---

## Simple Example: Multiplication Table

```python
for i in range(1, 4):    # Outer loop: rows
    for j in range(1, 4):  # Inner loop: columns
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each row

# Output:
# x 1 = 1
# x 2 = 2
# x 3 = 3
#
# x 1 = 2
# x 2 = 4
# x 3 = 6
#
# x 1 = 3
# x 2 = 6
# x 3 = 9
```

**How it works:**
1. Outer loop: i = 1
   - Inner loop runs completely: j = 1, 2, 3
2. Outer loop: i = 2
   - Inner loop runs completely: j = 1, 2, 3
3. Outer loop: i = 3
   - Inner loop runs completely: j = 1, 2, 3

---

## Visual Example: Rectangle of Stars

```python
for row in range(3):     # 3 rows
    for col in range(5):   # 5 stars per row
        print("*", end="")
    print()  # New line after each row

# Output:
# *****
# *****
# *****
```

---

## Common Patterns

### Pattern 1: Right Triangle

```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

### Pattern 2: Number Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}{j}", end=" ")
    print()

# Output:
# 12 13
# 22 23
# 32 33
```

---

## Real-World Example: Comparing Items

```python
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]

for student in students:
    for subject in subjects:
        print(f"{student} takes {subject}")
    print()

# Output:
# Alice takes Math
# Alice takes Science
# Alice takes English
#
# Bob takes Math
# Bob takes Science
# Bob takes English
#
# Charlie takes Math
# Charlie takes Science
# Charlie takes English
```

---

## How Many Times Does Inner Loop Run?

```python
for i in range(3):        # Runs 3 times
    for j in range(4):      # Runs 4 times for EACH i
        print(f"({i}, {j})")

# Inner loop runs: 3 × 4 = 12 times total!
```

**Formula:** Total iterations = (outer iterations) × (inner iterations)

---

## Try It Yourself (Before Class)

Run this code:

```python
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

**Questions:**
1. What pattern does this create?
2. Why does the inner range use `i + 1`?
3. Try changing `print(j, end="")` to `print("*", end="")` - what happens?

---

## Key Takeaways

Before class, remember:
1. **Nested loops = loop inside loop** - inner runs completely for each outer iteration
2. **Common use** - grids, patterns, tables, combinations
3. **Total iterations** - multiply outer count by inner count
4. **Indentation matters** - shows which loop contains which code
5. **Can nest many levels** - but usually 2-3 is maximum for readability

## What's Next?

In the live session, we'll:
- Create various patterns with nested loops
- Work with 2D data structures
- Use break and continue in nested loops
- Understand performance implications
- Practice debugging nested loops

See you in class!


---

