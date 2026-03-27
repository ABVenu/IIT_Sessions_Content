# Writing While Loops for Repeated Execution

Test your understanding of while loops and their application in Python.

---

## What is the output of this code?
```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

A) 1 2 3
B) 1 2 3 4
C) 0 1 2 3
D) Infinite loop

<details><summary>Answer</summary>
**A) 1 2 3**

**Explanation:** Starts at 1, loops while count <= 3, increments each time. Prints 1, 2, 3. When count becomes 4, condition (4 <= 3) is False, loop stops.
</details>

---

## What are the THREE essential parts of a while loop?

A) Start, Middle, End
B) Initialization, Condition, Update
C) Begin, Loop, Finish
D) Input, Process, Output

<details><summary>Answer</summary>
**B) Initialization, Condition, Update**

**Explanation:**
- **Initialization**: Set variables before loop
- **Condition**: Test that determines if loop continues
- **Update**: Modify variables to eventually make condition False
Missing any part can cause errors or infinite loops.
</details>

---

## What causes an infinite loop?

A) Loop condition that's always True
B) Forgetting to update loop variables
C) Condition that never becomes False
D) All of the above

<details><summary>Answer</summary>
**D) All of the above**

**Explanation:** An infinite loop occurs when the condition never becomes False. This happens when:
- Condition is literally `while True:` without break
- Loop variables aren't updated (`count += 1` missing)
- Logic error prevents condition from becoming False
</details>

---

## What is the output?
```python
x = 5
while x > 0:
    print(x)
    x -= 2
```

A) 5 4 3 2 1
B) 5 3 1
C) 5 3 1 -1
D) Infinite loop

<details><summary>Answer</summary>
**B) 5 3 1**

**Explanation:** Starts at 5, decrements by 2 each time:
- x=5: 5 > 0? YES → Print 5, x=3
- x=3: 3 > 0? YES → Print 3, x=1
- x=1: 1 > 0? YES → Print 1, x=-1
- x=-1: -1 > 0? NO → Stop
</details>

---

## What is a sentinel value?

A) A guard that protects code
B) A special value that signals loop termination
C) A counter variable
D) An error message

<details><summary>Answer</summary>
**B) A special value that signals loop termination**

**Explanation:** A sentinel value is a specific value that tells the loop to stop. Example: entering "quit" to exit a menu, or 0 to stop summing numbers. It acts as a signal that input is complete.
</details>

---

## When should you use a while loop instead of a for loop?

A) Always use while, never for
B) When you know exact number of iterations
C) When you don't know how many iterations in advance
D) Only for infinite loops

<details><summary>Answer</summary>
**C) When you don't know how many iterations in advance**

**Explanation:** Use while when iterations depend on a condition (e.g., "until user enters correct password"). Use for when you know the count (e.g., "exactly 10 times").
</details>

---

## What is the output?
```python
total = 0
num = 1

while num <= 4:
    total += num
    num += 1

print(total)
```

A) 4
B) 10
C) 14
D) 15

<details><summary>Answer</summary>
**B) 10**

**Explanation:** Sum of 1+2+3+4 = 10
- num=1: total=0+1=1, num=2
- num=2: total=1+2=3, num=3
- num=3: total=3+3=6, num=4
- num=4: total=6+4=10, num=5
- num=5: 5 <= 4? NO → Exit, print 10
</details>

---

## What is an accumulator in a loop?

A) A variable that accumulates speed
B) A variable that builds up a result over iterations
C) A type of loop
D) An error counter

<details><summary>Answer</summary>
**B) A variable that builds up a result over iterations**

**Explanation:** An accumulator collects results as the loop runs. Examples:
- `total += number` (sum accumulator)
- `count += 1` (counter)
- `product *= num` (multiplication accumulator)
Initialized before loop, updated inside loop.
</details>

---

## What happens if the while condition is False from the start?

A) Error occurs
B) Loop runs once anyway
C) Loop body never executes
D) Program crashes

<details><summary>Answer</summary>
**C) Loop body never executes**

**Explanation:** Python checks the condition BEFORE entering the loop. If False initially, the body is skipped entirely (zero iterations). This is normal behavior, not an error.
</details>

---

## What is the output?
```python
i = 0
while i < 3:
    print(i * 2)
    i += 1
```

A) 0 1 2
B) 0 2 4
C) 2 4 6
D) 0 2 4 6

<details><summary>Answer</summary>
**B) 0 2 4**

**Explanation:** Loop runs 3 times (i=0, 1, 2), printing i*2:
- i=0: Print 0*2=0, i=1
- i=1: Print 1*2=2, i=2
- i=2: Print 2*2=4, i=3
- i=3: 3 < 3? NO → Stop
</details>

---

## What is a "priming read"?

A) Reading input to prime a pump
B) First input read before entering the loop
C) Reading input twice
D) Fastest way to read input

<details><summary>Answer</summary>
**B) First input read before entering the loop**

**Explanation:** Priming read gets initial value to test in loop condition. Pattern:
```python
value = input()  # Priming read
while value != "quit":
    # Process value
    value = input()  # Read next
```
Ensures first value is available for condition check.
</details>

---

## What is the output?
```python
n = 10
count = 0

while n > 1:
    n //= 2
    count += 1

print(count)
```

A) 3
B) 4
C) 5
D) 10

<details><summary>Answer</summary>
**A) 3**

**Explanation:** Counts how many times you can divide by 2:
- n=10: 10//2=5, count=1
- n=5: 5//2=2, count=2
- n=2: 2//2=1, count=3
- n=1: 1 > 1? NO → Stop, print 3
</details>

---

## Which code pattern validates user input?

A) `while input_valid: get_input()`
B) `while input_invalid: get_input()`
C) `for i in range(10): get_input()`
D) `if input_invalid: get_input()`

<details><summary>Answer</summary>
**B) `while input_invalid: get_input()`**

**Explanation:** Validation pattern loops WHILE input is invalid:
```python
age = int(input())
while age < 0 or age > 120:  # While invalid
    age = int(input("Try again: "))
```
Forces user to provide valid input before continuing.
</details>

---

## What is the difference between `count += 1` and `count = count + 1`?

A) They're completely different
B) They're equivalent (same result)
C) First is faster
D) Second is more accurate

<details><summary>Answer</summary>
**B) They're equivalent (same result)**

**Explanation:** `count += 1` is shorthand for `count = count + 1`. Both increment count by 1. The `+=` operator is more concise and commonly used. Other compound operators: `-=`, `*=`, `//=`, etc.
</details>

---

## What is the output?
```python
password = "secret"
attempts = 0

while password != "python" and attempts < 2:
    password = "python"
    attempts += 1

print(attempts)
```

A) 0
B) 1
C) 2
D) Infinite loop

<details><summary>Answer</summary>
**B) 1**

**Explanation:**
- Initial: password="secret", attempts=0
- Check: "secret" != "python" AND 0 < 2? YES → Enter loop
- Set password="python", attempts=1
- Check: "python" != "python" AND 1 < 2? NO (first condition False)
- Exit loop, print 1
</details>

---




---

# Controlling While Loops Using Break Statement

Test your understanding of the break statement and its use in controlling loop flow.

---

## What does the break statement do?

A) Pauses the loop temporarily
B) Exits the loop immediately
C) Skips to the next iteration
D) Restarts the loop from the beginning

<details><summary>Answer</summary>
**B) Exits the loop immediately**

**Explanation:** The break statement terminates the loop right away, regardless of the loop condition. Execution continues after the loop.
</details>

---

## What is the output?
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

A) 0 1 2
B) 0 1 2 3
C) 0 1 2 3 4
D) 3 4

<details><summary>Answer</summary>
**A) 0 1 2**

**Explanation:** Loop prints 0, 1, 2. When i=3, the break statement executes, exiting the loop before printing 3.
</details>

---

## Can you use break in a for loop?

A) No, only in while loops
B) Yes, in both while and for loops
C) Yes, but only in Python 3
D) No, break is not a Python keyword

<details><summary>Answer</summary>
**B) Yes, in both while and for loops**

**Explanation:** The break statement works in ANY type of loop - while, for, or nested combinations of both.
</details>

---

## What happens with nested loops and break?

A) Break exits all nested loops
B) Break only exits the innermost loop
C) Break causes an error in nested loops
D) Break exits the outermost loop only

<details><summary>Answer</summary>
**B) Break only exits the innermost loop**

**Explanation:** Break exits the closest enclosing loop. To exit outer loops, you need a flag variable and check it in the outer loop.
</details>

---

## What is the output?
```python
count = 0
while True:
    count += 1
    if count == 3:
        break
    print(count)
```

A) 1 2
B) 1 2 3
C) Infinite loop
D) 0 1 2

<details><summary>Answer</summary>
**A) 1 2**

**Explanation:** Prints 1, then 2. When count=3, breaks before printing. `while True` creates infinite loop, but break provides exit.
</details>

---

## When does the else clause of a loop execute?

A) Always after the loop
B) Only if break was used
C) Only if loop completed without break
D) Never

<details><summary>Answer</summary>
**C) Only if loop completed without break**

**Explanation:** Loop-else runs if the loop finishes normally (condition becomes False). If break executes, else is skipped.
</details>

---

## What is the output?
```python
for num in [1, 3, 5, 6, 7]:
    if num % 2 == 0:
        print("Found even")
        break
else:
    print("No even numbers")
```

A) Found even
B) No even numbers
C) Found even<br>No even numbers
D) Error

<details><summary>Answer</summary>
**A) Found even**

**Explanation:** Found 6 (even), printed "Found even", broke. Since break executed, else clause is skipped.
</details>

---

## Is `while True:` with break a common pattern?

A) No, it's bad practice
B) Yes, common for menus and input
C) It causes infinite loops always
D) Only used for debugging

<details><summary>Answer</summary>
**B) Yes, common for menus and input**

**Explanation:** `while True:` with break is a standard pattern for menu systems, continuous input, and event loops. It's clean and readable when used properly.
</details>

---

## What is the output?
```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n > 3:
        break
    print(n * 2)
```

A) 2 4 6
B) 2 4 6 8
C) 2 4 6 8 10
D) 8 10

<details><summary>Answer</summary>
**A) 2 4 6**

**Explanation:** Prints doubled values: 2, 4, 6 (for n=1, 2, 3). When n=4, condition n > 3 is True, so break executes.
</details>

---

## How do you break from BOTH loops in nested loops?

A) Use break twice
B) Use flag variable
C) Break automatically exits all loops
D) It's not possible

<details><summary>Answer</summary>
**B) Use flag variable**

**Explanation:** Set a flag in inner loop when breaking, then check flag in outer loop to break that too. Pattern:
```python
found = False
for i in ...:
    for j in ...:
        if condition:
            found = True
            break
    if found:
        break
```
</details>

---

## What is the output?
```python
i = 0
while i < 5:
    i += 1
    if i == 2:
        break
print(i)
```

A) 1
B) 2
C) 5
D) 0

<details><summary>Answer</summary>
**B) 2**

**Explanation:** i increments to 1, then to 2. When i==2, break exits loop. Final value of i is 2.
</details>

---

## Can a loop have multiple break statements?

A) No, only one break per loop
B) Yes, any number of breaks
C) Only two breaks maximum
D) Breaks must be in else clause

<details><summary>Answer</summary>
**B) Yes, any number of breaks**

**Explanation:** You can have as many break statements as needed. First one that executes will exit the loop.
</details>

---

## What is the output?
```python
for i in range(10):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print(i)
```

A) 1 3 5
B) 1 3 5 7
C) 0 2 4 6 8
D) 7 9

<details><summary>Answer</summary>
**A) 1 3 5**

**Explanation:** Skips evens (continue). Prints odds: 1, 3, 5. When i=7 (odd and > 5), break executes. (Note: This question uses continue from next lesson but tests break understanding)
</details>

---

## Where does execution continue after break?

A) At the beginning of the loop
B) At the line after the loop
C) Program terminates
D) At the nearest else clause

<details><summary>Answer</summary>
**B) At the line after the loop**

**Explanation:** Break exits the loop and execution continues with the first statement after the loop body.
</details>

---

## What is the output?
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"{i},{j}")
```

A) 0,0 1,0 2,0
B) 0,0 0,1 1,0 1,1 2,0 2,1
C) 0,0
D) All combinations from 0,0 to 2,2

<details><summary>Answer</summary>
**A) 0,0 1,0 2,0**

**Explanation:** For each i (0, 1, 2), inner loop prints once (j=0), then breaks at j=1. Outer loop continues normally.
</details>

---




---

# Controlling While Loops Using Continue Statement

Test your understanding of the continue statement and how it differs from break.

---

## What does the continue statement do?

A) Exits the loop immediately
B) Skips the rest of the current iteration and goes to the next
C) Pauses the loop temporarily
D) Restarts the loop from the beginning

<details><summary>Answer</summary>
**B) Skips the rest of the current iteration and goes to the next**

**Explanation:** Continue jumps to the next iteration, skipping any code below it in the current iteration. The loop continues running.
</details>

---

## What is the output?
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

A) 1 2 4 5
B) 1 2 3 4 5
C) 1 2
D) 3 4 5

<details><summary>Answer</summary>
**A) 1 2 4 5**

**Explanation:** Loop iterates 1-5. When i=3, continue skips the print statement. Prints 1, 2, (skip 3), 4, 5.
</details>

---

## What is the difference between break and continue?

A) They do the same thing
B) Break exits the loop, continue skips to next iteration
C) Continue exits the loop, break skips to next iteration
D) Break is for while loops, continue is for for loops

<details><summary>Answer</summary>
**B) Break exits the loop, continue skips to next iteration**

**Explanation:**
- **break**: Terminates loop completely
- **continue**: Skips rest of current iteration, continues with next one
They work in both while and for loops.
</details>

---

## What is the output?
```python
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    print(count)
```

A) 1 3 4 5
B) 1 2 3 4 5
C) 2 3 4 5
D) 1 3 4 5 6

<details><summary>Answer</summary>
**A) 1 3 4 5**

**Explanation:** Increments first (important!), then checks condition. When count=2, continue skips print. Prints 1, (skip 2), 3, 4, 5.
</details>

---

## What happens if you forget to increment before continue in a while loop?

A) Syntax error
B) Infinite loop
C) Loop runs once
D) Nothing, it's fine

<details><summary>Answer</summary>
**B) Infinite loop**

**Explanation:** If increment is after continue, it never executes when continue happens. Counter never changes, condition stays True forever = infinite loop!

**Wrong:**
```python
while count < 5:
    if count == 3:
        continue  # Infinite loop here!
    count += 1
```

**Right:**
```python
while count < 5:
    count += 1  # Increment first!
    if count == 3:
        continue
```
</details>

---

## How many times does the print execute?
```python
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        continue
    print(num)
```

A) 2 times
B) 3 times
C) 4 times
D) 5 times

<details><summary>Answer</summary>
**B) 3 times**

**Explanation:** Skips even numbers (2, 4) with continue. Prints odd numbers: 1, 3, 5 = 3 times.
</details>

---

## Can you use continue in a for loop?

A) No, only in while loops
B) Yes, in both while and for loops
C) Yes, but only in Python 3
D) No, continue is not valid in Python

<details><summary>Answer</summary>
**B) Yes, in both while and for loops**

**Explanation:** Continue works identically in BOTH while and for loops. It skips to the next iteration in either type.
</details>

---

## What is the output?
```python
numbers = [5, -2, 8, -1, 3]
total = 0

for num in numbers:
    if num < 0:
        continue
    total += num

print(total)
```

A) 13
B) 16
C) 18
D) 11

<details><summary>Answer</summary>
**B) 16**

**Explanation:** Skip negative numbers (-2, -1). Sum positives: 5 + 8 + 3 = 16. Continue prevents negatives from being added.
</details>

---

## What happens with nested loops and continue?

A) Continue affects all nested loops
B) Continue only affects the innermost loop
C) Continue causes an error in nested loops
D) Continue affects the outermost loop only

<details><summary>Answer</summary>
**B) Continue only affects the innermost loop**

**Explanation:** Just like break, continue only affects the closest enclosing loop. To skip iteration in outer loop, you need logic there too.
</details>

---

## What is the output?
```python
for i in range(5):
    if i == 0:
        continue
    if i == 3:
        break
    print(i)
```

A) 1 2
B) 1 2 3
C) 0 1 2
D) 1 2 4

<details><summary>Answer</summary>
**A) 1 2**

**Explanation:**
- i=0: continue (skip print)
- i=1: print 1
- i=2: print 2
- i=3: break (exit loop)
Never reaches i=4. Output: 1, 2.
</details>

---

## Which pattern is cleaner for filtering?
```python
# Option A
for item in items:
    if valid(item):
        process(item)

# Option B
for item in items:
    if not valid(item):
        continue
    process(item)
```

A) Option A is always better
B) Option B is cleaner for complex processing
C) They're identical
D) Option A is faster

<details><summary>Answer</summary>
**B) Option B is cleaner for complex processing**

**Explanation:** When process(item) is many lines, Option B (early continue) avoids deep nesting. Check invalid case first, skip it, then all processing code stays at top level.
</details>

---

## What is the output?
```python
word = "hello"
for char in word:
    if char in "aeiou":
        continue
    print(char, end="")
```

A) hello
B) eo
C) hll
D) aeiou

<details><summary>Answer</summary>
**C) hll**

**Explanation:** Skips vowels (e, o) with continue. Prints consonants only: h, l, l.
</details>

---

## Can a loop have multiple continue statements?

A) No, only one continue per loop
B) Yes, any number of continues
C) Only two continues maximum
D) Continues must be in else clause

<details><summary>Answer</summary>
**B) Yes, any number of continues**

**Explanation:** Multiple continues work like multiple filters. Each one skips different unwanted cases. First one reached executes.

```python
for num in numbers:
    if num == 0:
        continue  # Skip zeros
    if num < 0:
        continue  # Skip negatives
    # Process positive non-zero
```
</details>

---

## What's the purpose of continue in data processing?

A) Speed up loops
B) Filter out invalid/unwanted data
C) Stop processing when done
D) Count iterations

<details><summary>Answer</summary>
**B) Filter out invalid/unwanted data**

**Explanation:** Continue is perfect for data cleaning - skip error values, outliers, empty entries, etc. Process only valid data without stopping the loop.
</details>

---

## What is the output?
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"{i},{j}", end=" ")
    print()
```

A) 0,0 0,2 1,0 1,2 2,0 2,2
B) 0,0 1,0 2,0
C) All combinations from 0,0 to 2,2
D) 0,1 1,1 2,1

<details><summary>Answer</summary>
**A) 0,0 0,2 1,0 1,2 2,0 2,2**

**Explanation:** For each i (0, 1, 2), inner loop prints j=0 and j=2, skips j=1. Continue only affects inner loop, outer continues normally.

Output (with newlines from print()):
0,0 0,2
1,0 1,2
2,0 2,2
</details>

---




---

# Writing For Loops to Iterate Over Sequences

Test your understanding of for loops and iteration in Python.

---

## What is the output?
```python
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)
```

A) apple banana
B) apple<br>banana
C) ["apple", "banana"]
D) 0 1

<details><summary>Answer</summary>
**B) apple<br>banana**

**Explanation:** For loop iterates through list, printing each fruit on a new line. Output is:
apple
banana
</details>

---

## What does the loop variable represent?

```python
for item in my_list:
    print(item)
```

A) The index of the current element
B) The actual value of the current element
C) The entire list
D) The number of items

<details><summary>Answer</summary>
**B) The actual value of the current element**

**Explanation:** In a for loop, the loop variable (`item`) holds the actual value from the sequence, not the index. Each iteration assigns the next value to `item`.
</details>

---

## What is the output?
```python
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)
```

A) 15
B) 5
C) 12345
D) [1, 2, 3, 4, 5]

<details><summary>Answer</summary>
**A) 15**

**Explanation:** Accumulator pattern. Starts at 0, adds each number: 0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15.
</details>

---

## Can you iterate through a string with a for loop?

A) No, only lists
B) Yes, strings are sequences
C) Only if you convert to list first
D) No, strings are not iterable

<details><summary>Answer</summary>
**B) Yes, strings are sequences**

**Explanation:** Strings are iterable sequences. For loop iterates one character at a time:
```python
for char in "hi":
    print(char)
# Prints: h, then i
```
</details>

---

## What is the output?
```python
word = "cat"
for letter in word:
    print(letter, end=" ")
```

A) cat
B) c a t
C) c a t (with newlines)
D) Error

<details><summary>Answer</summary>
**B) c a t**

**Explanation:** Loop iterates each character. `end=" "` prints space instead of newline. Output: `c a t `
</details>

---

## What does enumerate() do?

A) Counts the items
B) Provides both index and value
C) Sorts the list
D) Only works with numbers

<details><summary>Answer</summary>
**B) Provides both index and value**

**Explanation:** `enumerate()` returns pairs of (index, value):
```python
for i, item in enumerate(["a", "b"]):
    print(i, item)
# Output: 0 a, then 1 b
```
</details>

---

## What is the output?
```python
for i, color in enumerate(["red", "blue"]):
    print(f"{i}: {color}")
```

A) 0: red<br>1: blue
B) 1: red<br>2: blue
C) red blue
D) Error

<details><summary>Answer</summary>
**A) 0: red<br>1: blue**

**Explanation:** enumerate() starts at index 0 by default. First pair is (0, "red"), second is (1, "blue").
</details>

---

## What does zip() do?

A) Compresses files
B) Combines multiple sequences
C) Sorts lists
D) Filters items

<details><summary>Answer</summary>
**B) Combines multiple sequences**

**Explanation:** `zip()` pairs elements from multiple sequences:
```python
for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)
# Output: 1 x, then 2 y
```
</details>

---

## What is the output?
```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

A) Alice: 25<br>Bob: 30
B) Alice Bob 25 30
C) Error
D) [Alice, 25] [Bob, 30]

<details><summary>Answer</summary>
**A) Alice: 25<br>Bob: 30**

**Explanation:** zip() creates pairs: ("Alice", 25) and ("Bob", 30). Loop unpacks and prints each pair.
</details>

---

## How do you iterate over dictionary key-value pairs?

A) `for item in dict:`
B) `for key, value in dict.items():`
C) `for i in range(len(dict)):`
D) `for dict[key]:`

<details><summary>Answer</summary>
**B) `for key, value in dict.items():`**

**Explanation:** `.items()` returns key-value pairs:
```python
for k, v in {"a": 1, "b": 2}.items():
    print(k, v)
# Prints: a 1, then b 2
```
</details>

---

## What is the output?
```python
student = {"name": "Alice", "age": 20}

for key in student:
    print(key)
```

A) name age
B) Alice 20
C) name: Alice<br>age: 20
D) Error

<details><summary>Answer</summary>
**A) name age**

**Explanation:** Iterating dictionary directly gives keys only (same as `.keys()`). Each key printed on new line.
</details>

---

## What happens with nested for loops?

```python
for i in [1, 2]:
    for j in [3, 4]:
        print(i, j)
```

A) Prints 4 combinations
B) Prints 2 combinations
C) Error
D) Prints only outer loop

<details><summary>Answer</summary>
**A) Prints 4 combinations**

**Explanation:** Outer loop runs twice, inner loop runs twice per outer iteration: (1,3), (1,4), (2,3), (2,4) = 4 total.
</details>

---

## When should you use a for loop instead of while?

A) Always use for
B) When iterating known sequences
C) When you need infinite loops
D) Only for numbers

<details><summary>Answer</summary>
**B) When iterating known sequences**

**Explanation:** For loops are ideal for sequences (lists, strings, ranges). While loops better for unknown iterations or conditions.
</details>

---

## What is the output?
```python
numbers = [1, 2, 3]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)
```

A) [2, 4, 6]
B) [1, 2, 3]
C) 2 4 6
D) 6

<details><summary>Answer</summary>
**A) [2, 4, 6]**

**Explanation:** Loop transforms each number (multiply by 2) and appends to new list. Result: [2, 4, 6].
</details>

---

## Do break and continue work in for loops?

A) No, only in while loops
B) Yes, same as while loops
C) Only break works
D) Only continue works

<details><summary>Answer</summary>
**B) Yes, same as while loops**

**Explanation:** Both `break` (exit loop) and `continue` (skip to next iteration) work identically in for and while loops.
</details>

---




---

# Using Range() Function for Numeric Iteration

Test your understanding of the range() function in Python.

---

## What is the output?
```python
for i in range(5):
    print(i, end=" ")
```

A) 1 2 3 4 5
B) 0 1 2 3 4
C) 0 1 2 3 4 5
D) 1 2 3 4

<details><summary>Answer</summary>
**B) 0 1 2 3 4**

**Explanation:** `range(5)` with a single argument starts at 0 (default), stops before 5, and steps by 1 (default). It generates 5 numbers: 0, 1, 2, 3, 4. The stop value (5) is **exclusive** and not included.
</details>

---

## How do you generate numbers from 1 to 10 (inclusive)?

A) `range(10)`
B) `range(1, 10)`
C) `range(1, 11)`
D) `range(0, 10)`

<details><summary>Answer</summary>
**C) `range(1, 11)`**

**Explanation:** The stop value in range() is **exclusive** (never included). To get 1 through 10, you need to start at 1 and stop before 11. Think of it as: start at 1, while i < 11. This is the most common mistake with range()!
</details>

---

## What is the output?
```python
for i in range(2, 10, 2):
    print(i, end=" ")
```

A) 2 4 6 8 10
B) 2 4 6 8
C) 0 2 4 6 8
D) 2 3 4 5 6 7 8 9

<details><summary>Answer</summary>
**B) 2 4 6 8**

**Explanation:** `range(2, 10, 2)` means start at 2, stop before 10, step by 2. This generates: 2, 4, 6, 8. The value 10 is not included because the stop is exclusive. The step of 2 creates even numbers.
</details>

---

## What does the third argument in range() control?

A) The starting value
B) The stopping value
C) The step/increment value
D) The number of iterations

<details><summary>Answer</summary>
**C) The step/increment value**

**Explanation:** In `range(start, stop, step)`, the third argument controls how much to increment (or decrement) each iteration. Default step is 1. Step of 2 counts by twos, step of -1 counts backwards.
</details>

---

## What is the output?
```python
for i in range(10, 0, -1):
    print(i, end=" ")
```

A) 10 9 8 7 6 5 4 3 2 1
B) 10 9 8 7 6 5 4 3 2 1 0
C) 0 1 2 3 4 5 6 7 8 9 10
D) Error - range can't count backwards

<details><summary>Answer</summary>
**A) 10 9 8 7 6 5 4 3 2 1**

**Explanation:** Negative step (-1) makes range count backwards. Start at 10, stop before 0 (exclusive), decrement by 1. This gives 10, 9, 8, ..., 1. Zero is not included because stop is exclusive.
</details>

---

## What happens with `range(10, 1)`?

A) Generates 10, 9, 8, ..., 2
B) Generates 1, 2, 3, ..., 10
C) Generates an empty sequence (nothing)
D) Causes an error

<details><summary>Answer</summary>
**C) Generates an empty sequence (nothing)**

**Explanation:** When start (10) is greater than stop (1) with a positive step (default 1), range is empty. You can't count UP from 10 to 1. To count backwards, you MUST use negative step: `range(10, 1, -1)`.
</details>

---

## What is the default start value if not specified?

A) 1
B) 0
C) None
D) 10

<details><summary>Answer</summary>
**B) 0**

**Explanation:** `range(5)` is equivalent to `range(0, 5)`. The default start is 0, which aligns with Python's zero-based indexing. This is why `range(5)` gives 0, 1, 2, 3, 4 (five numbers starting from 0).
</details>

---

## What is the default step value if not specified?

A) 0
B) 1
C) 2
D) -1

<details><summary>Answer</summary>
**B) 1**

**Explanation:** If the step isn't specified, it defaults to 1. `range(1, 10)` is equivalent to `range(1, 10, 1)`, which counts 1, 2, 3, 4, 5, 6, 7, 8, 9.
</details>

---

## How many numbers does `range(10)` generate?

A) 9
B) 10
C) 11
D) 0

<details><summary>Answer</summary>
**B) 10**

**Explanation:** `range(10)` generates exactly 10 numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. The single-argument form `range(n)` generates n numbers starting from 0. This is useful when you need exactly n iterations.
</details>

---

## What is the output?
```python
for i in range(1, 10, 3):
    print(i, end=" ")
```

A) 1 2 3 4 5 6 7 8 9
B) 1 4 7
C) 1 4 7 10
D) 3 6 9

<details><summary>Answer</summary>
**B) 1 4 7**

**Explanation:** Start at 1, stop before 10, step by 3. Sequence: 1, 1+3=4, 4+3=7, 7+3=10 (but 10 is excluded). Result: 1, 4, 7. The step controls the increment between values.
</details>

---

## Can range() accept float (decimal) arguments?

A) Yes, any number type works
B) No, only integers are allowed
C) Yes, but it rounds them
D) Only the step can be a float

<details><summary>Answer</summary>
**B) No, only integers are allowed**

**Explanation:** range() only accepts integer arguments. `range(1.5, 5.5)` causes a TypeError. If you need float ranges, you'd need to use numpy.arange() or create your own solution with a while loop.
</details>

---

## What is the difference between range() and a list?

A) No difference, they're the same
B) range() is memory-efficient and generates on demand
C) Lists are faster
D) range() stores all values in memory

<details><summary>Answer</summary>
**B) range() is memory-efficient and generates on demand**

**Explanation:** range() is a "lazy" sequence - it generates values one at a time as needed, not all at once. `range(1000000)` uses tiny memory. `list(range(1000000))` creates a huge list in memory. This makes range very efficient for large sequences.
</details>

---

## What is the output?
```python
print(list(range(3, 8)))
```

A) [3, 4, 5, 6, 7]
B) [3, 4, 5, 6, 7, 8]
C) [4, 5, 6, 7]
D) [3, 8]

<details><summary>Answer</summary>
**A) [3, 4, 5, 6, 7]**

**Explanation:** `range(3, 8)` starts at 3 and stops before 8 (exclusive). Converting to a list with `list()` shows all generated values: [3, 4, 5, 6, 7]. The stop value (8) is never included.
</details>

---

## Which generates odd numbers from 1 to 9?

A) `range(1, 9, 2)`
B) `range(1, 10, 2)`
C) `range(0, 9, 2)`
D) `range(2, 10, 2)`

<details><summary>Answer</summary>
**B) `range(1, 10, 2)`**

**Explanation:** Start at 1 (first odd), stop before 10, step by 2. Generates: 1, 3, 5, 7, 9. Option A would give 1, 3, 5, 7 (missing 9 because 9 < 10 but 9 is not < 9). The step of 2 from an odd start gives odd numbers.
</details>

---

## What is the output?
```python
for i in range(5, 5):
    print(i)
print("Done")
```

A) 5
   Done
B) Error
C) Done
D) Nothing

<details><summary>Answer</summary>
**C) Done**

**Explanation:** `range(5, 5)` has start equal to stop, creating an empty range. The loop body never executes (zero iterations). The program continues and prints "Done". This is valid - range can be empty without causing an error.
</details>

---



## Common Mistakes to Avoid

1. **Forgetting exclusive stop**: `range(10)` goes 0-9, not 0-10
2. **Wrong direction**: `range(10, 1)` is empty, need `range(10, 1, -1)`
3. **Off-by-one errors**: For 1-10, use `range(1, 11)` not `range(1, 10)`
4. **Float arguments**: range doesn't accept decimals
5. **Inclusive thinking**: Stop is always exclusive
6. **Missing negative step**: Can't count down without it
7. **Step of 0**: Causes error (infinite loop)

## Quick Reference

```python
# Basic patterns
range(5)           # 0, 1, 2, 3, 4 (5 numbers)
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8 (evens)
range(1, 10, 2)    # 1, 3, 5, 7, 9 (odds)

# Backwards
range(10, 0, -1)   # 10, 9, 8, ..., 1
range(5, -1, -1)   # 5, 4, 3, 2, 1, 0

# Useful formulas
range(n)           # n iterations (0 to n-1)
range(1, n+1)      # 1 to n inclusive
range(len(list))   # All valid indices of list
range(a, b+1)      # a to b inclusive
```


---

# Controlling For Loops with Break and Continue

## 

What will be the output of this code?

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

A) 0 1 2 3
B) 0 1 2
C) 0 1 2 3 4
D) 1 2 3

**Answer: B) 0 1 2**

**Explanation:** The loop prints values 0, 1, and 2. When i becomes 3, the if condition is True and break executes, immediately exiting the loop. The number 3 is never printed because break occurs before the print statement for that iteration.

---

## 

What does the continue statement do in a for loop?

A) Stops the entire program
B) Exits the loop completely
C) Skips the rest of the current iteration and moves to the next one
D) Restarts the loop from the beginning

**Answer: C) Skips the rest of the current iteration and moves to the next one**

**Explanation:** The continue statement causes the loop to skip all remaining code in the current iteration and immediately proceed to the next iteration. It does NOT exit the loop entirely (that's what break does).

---

## 

What will this code print?

```python
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num, end=' ')
```

A) 1 2 3 4 5
B) 2 4
C) 1 3 5
D) 1 2 3 4

**Answer: C) 1 3 5**

**Explanation:** The loop iterates from 1 to 5. When num is even (2 or 4), continue skips the print statement. Only odd numbers (1, 3, 5) are printed.

---

## 

What is the output of this code?

```python
for i in range(3):
    if i == 5:
        break
    print(i)
```

A) 0 1 2
B) Nothing
C) 0 1 2 3 4
D) Error

**Answer: A) 0 1 2**

**Explanation:** The range(3) produces values 0, 1, 2. The condition `i == 5` is never True since i never reaches 5. Therefore, break never executes and all three values are printed normally.

---

## 

When does the else clause of a for loop execute?

A) Always after the loop
B) Only if the loop encounters a break statement
C) Only if the loop completes without encountering a break
D) Never

**Answer: C) Only if the loop completes without encountering a break**

**Explanation:** The for-else clause is a special Python feature where the else block executes only when the loop completes its normal iteration without encountering a break statement. If break executes, the else block is skipped.

---

## 

What will be the output?

```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i, end=' ')
```

A) 0 1 3
B) 0 1 2 3
C) 0 1 3 4
D) 0 1 2 3 4

**Answer: A) 0 1 3**

**Explanation:**
- i=0: No conditions met, print 0
- i=1: No conditions met, print 1
- i=2: First if is True, continue skips print
- i=3: No conditions met, print 3
- i=4: Second if is True, break exits loop
Result: 0 1 3

---

## 

Which statement is TRUE about break in nested loops?

A) Break exits all nested loops
B) Break exits only the innermost loop containing it
C) Break exits the outermost loop
D) Break is not allowed in nested loops

**Answer: B) Break exits only the innermost loop containing it**

**Explanation:** In nested loops, a break statement only exits the loop it's directly inside of (the innermost one). To break out of outer loops, you need additional logic like flag variables or function returns.

---

## 

What will this code output?

```python
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 5:
        print("Found")
        break
else:
    print("Not found")
```

A) Found
B) Not found
C) Nothing
D) Error

**Answer: B) Not found**

**Explanation:** The number 5 is not in the list, so the break never executes. The loop completes normally, and therefore the else clause executes, printing "Not found". This is a common pattern for search operations with for-else.

---

## 

What is the main difference between break and continue?

A) There is no difference
B) break exits the loop, continue skips to the next iteration
C) break skips to the next iteration, continue exits the loop
D) break can only be used in while loops

**Answer: B) break exits the loop, continue skips to the next iteration**

**Explanation:** break completely terminates the loop and continues execution after the loop. continue skips the remaining code in the current iteration but continues with the next iteration of the loop.

---

## 

What will be printed?

```python
for i in range(1, 4):
    for j in range(1, 3):
        if j == 2:
            break
        print(f"{i},{j}", end=' ')
```

A) 1,1 2,1 3,1
B) 1,1 1,2 2,1 2,2 3,1 3,2
C) 1,1 2,1
D) 1,1

**Answer: A) 1,1 2,1 3,1**

**Explanation:** The outer loop runs for i=1,2,3. The inner loop starts with j=1 (print i,j), then j=2 triggers break, exiting the inner loop. This pattern repeats for each i value. Result: 1,1  2,1  3,1

---

## 

How many times will "Hello" be printed?

```python
for i in range(10):
    if i % 3 == 0:
        continue
    if i > 5:
        break
    print("Hello")
```

A) 3 times
B) 4 times
C) 5 times
D) 6 times

**Answer: A) 3 times**

**Explanation:**
- i=0: divisible by 3, continue (skip)
- i=1: print "Hello"
- i=2: print "Hello"
- i=3: divisible by 3, continue (skip)
- i=4: print "Hello"
- i=5: print "Hello" (5 is NOT > 5)
- i=6: 6 > 5, break
Total printed: 1, 2, 4, 5 = 4 times

Wait, let me recount:
- i=0: 0 % 3 == 0, continue
- i=1: 1 % 3 != 0, 1 > 5? No, print "Hello"
- i=2: 2 % 3 != 0, 2 > 5? No, print "Hello"
- i=3: 3 % 3 == 0, continue
- i=4: 4 % 3 != 0, 4 > 5? No, print "Hello"
- i=5: 5 % 3 != 0, 5 > 5? No, print "Hello"
- i=6: 6 % 3 == 0, continue
- i=7: 7 % 3 != 0, 7 > 5? Yes, break

Wait, that's still 4 times (1, 2, 4, 5).

Let me recalculate:
- i=0: 0 % 3 == 0 → continue
- i=1: 1 % 3 = 1 (not 0) → 1 > 5? No → print
- i=2: 2 % 3 = 2 (not 0) → 2 > 5? No → print
- i=3: 3 % 3 == 0 → continue
- i=4: 4 % 3 = 1 (not 0) → 4 > 5? No → print
- i=5: 5 % 3 = 2 (not 0) → 5 > 5? No → print
- i=6: 6 % 3 == 0 → continue
- i=7: 7 % 3 = 1 (not 0) → 7 > 5? Yes → break

So it prints at i = 1, 2, 4, 5 = 4 times

Actually, I need to change the answer. Let me update it.

Actually, the order matters! Let me trace again carefully:
```python
for i in range(10):  # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    if i % 3 == 0:   # Check if divisible by 3
        continue
    if i > 5:        # Check if greater than 5
        break
    print("Hello")
```

- i=0: 0%3==0 True → continue (skip rest)
- i=1: 1%3==0 False → 1>5 False → print "Hello"
- i=2: 2%3==0 False → 2>5 False → print "Hello"
- i=3: 3%3==0 True → continue (skip rest)
- i=4: 4%3==0 False → 4>5 False → print "Hello"
- i=5: 5%3==0 False → 5>5 False → print "Hello"
- i=6: 6%3==0 True → continue (skip rest)
- i=7: 7%3==0 False → 7>5 True → break

Printed at: i=1, 2, 4, 5 = 4 times

So the answer should be B) 4 times. Let me fix this.

**Answer: B) 4 times**

**Explanation:**
- i=0: 0 % 3 == 0, continue (skip)
- i=1: Not divisible by 3, 1 ≤ 5, print "Hello"
- i=2: Not divisible by 3, 2 ≤ 5, print "Hello"
- i=3: 3 % 3 == 0, continue (skip)
- i=4: Not divisible by 3, 4 ≤ 5, print "Hello"
- i=5: Not divisible by 3, 5 ≤ 5, print "Hello"
- i=6: 6 % 3 == 0, continue (skip)
- i=7: Not divisible by 3, but 7 > 5, break
Total: 4 times (at i=1, 2, 4, 5)

---

## 

What makes for-else useful?

A) It always executes after a for loop
B) It provides a clean way to handle "not found" scenarios in searches
C) It executes only when break is encountered
D) It makes loops run faster

**Answer: B) It provides a clean way to handle "not found" scenarios in searches**

**Explanation:** The for-else clause is particularly useful for search operations. If the item is found, you break (and else doesn't execute). If the loop completes without finding the item, the else clause can handle that "not found" case cleanly without needing extra flag variables.

---

## 

Can you use both break and continue in the same loop?

A) No, Python will raise an error
B) Yes, but only in while loops
C) Yes, they can be used together in the same loop
D) No, you must choose one or the other

**Answer: C) Yes, they can be used together in the same loop**

**Explanation:** You can use both break and continue in the same loop. They serve different purposes: continue skips to the next iteration, while break exits the loop. However, only one of them will execute in any given iteration. Order matters when checking conditions.

---

## 

What will this code output?

```python
text = "Python"
for char in text:
    if char == 'o':
        break
    if char in 'aeiou':
        continue
    print(char, end='')
```

A) Pythn
B) Pyth
C) Pyt
D) Python

**Answer: B) Pyth**

**Explanation:**
- 'P': Not a vowel, print 'P'
- 'y': Not a vowel, print 'y'
- 't': Not a vowel, print 't'
- 'h': Not a vowel, print 'h'
- 'o': Equals 'o', break (exit loop)
- 'n': Never reached
Result: "Pyth"

---

## 

Which scenario is break MOST useful for?

A) Processing all items in a list
B) Filtering out unwanted values
C) Stopping when a target is found or condition is met
D) Counting items in a collection

**Answer: C) Stopping when a target is found or condition is met**

**Explanation:** Break is most useful for early exit scenarios, such as:
- Searching for an item and stopping when found
- Stopping when a threshold is reached
- Exiting when an error condition occurs
- Stopping when a goal is achieved

For filtering, continue is more appropriate. For processing all items, no control flow modification is needed.

---

## Summary

### Key Concepts Tested:

1. **Break Statement**: Exits loop immediately when executed
2. **Continue Statement**: Skips remaining code in current iteration, moves to next
3. **For-Else Clause**: Executes only if loop completes without break
4. **Nested Loops**: Break/continue only affect innermost loop
5. **Combined Usage**: Both can be used in same loop with different conditions
6. **Use Cases**:
   - Break: Search, early exit, threshold detection
   - Continue: Filtering, skipping invalid data
   - For-else: Search completion detection

### Common Patterns:

```python
# Search pattern with break
for item in items:
    if item == target:
        print("Found!")
        break

# Filter pattern with continue
for num in numbers:
    if num < 0:
        continue
    process(num)

# For-else pattern
for item in items:
    if item == target:
        break
else:
    print("Not found")

# Combined usage
for num in range(100):
    if num % 5 == 0:
        continue  # Skip multiples of 5
    if num > 50:
        break  # Stop after 50
    print(num)
```

### Best Practices:

1. **Use break** when you need to stop processing early
2. **Use continue** when you need to skip certain items
3. **Use for-else** instead of flag variables when possible
4. **Order matters** when combining break and continue
5. **Comment your intent** to make code clear
6. **Consider readability** - sometimes restructuring is better than complex break/continue logic


---

# Writing Nested Loops for Multi-Level Iteration

## 

What will be the output of this code?

```python
for i in range(3):
    for j in range(2):
        print('*', end=' ')
    print()
```

A) 6 stars in one line
B) 3 rows with 2 stars each
C) 2 rows with 3 stars each
D) Error

**Answer: B) 3 rows with 2 stars each**

**Explanation:** The outer loop runs 3 times (for rows), and the inner loop runs 2 times (for columns). After each inner loop completes, `print()` creates a new line. This produces 3 rows, each containing 2 stars.

---

## 

How many total iterations occur in this nested loop?

```python
for i in range(4):
    for j in range(3):
        print(i, j)
```

A) 4
B) 7
C) 12
D) 16

**Answer: C) 12**

**Explanation:** Total iterations = outer iterations × inner iterations = 4 × 3 = 12. The inner loop runs completely for each iteration of the outer loop.

---

## 

What pattern will this code create?

```python
for i in range(1, 5):
    for j in range(i):
        print('*', end=' ')
    print()
```

A) Rectangle
B) Right triangle
C) Inverted triangle
D) Diamond

**Answer: B) Right triangle**

**Explanation:** Row 1 prints 1 star (range(1)), Row 2 prints 2 stars (range(2)), Row 3 prints 3 stars (range(3)), Row 4 prints 4 stars (range(4)). This creates a right-angled triangle pattern.

---

## 

What does this code print?

```python
for i in range(2):
    for j in range(2):
        print(i + j, end=' ')
    print()
```

A) 0 1 1 2
B) 0 1<br>1 2
C) 0 2<br>1 3
D) 0 0<br>1 1

**Answer: B) 0 1<br>1 2**

**Explanation:**
- i=0, j=0: print 0
- i=0, j=1: print 1, then newline
- i=1, j=0: print 1
- i=1, j=1: print 2, then newline
Output: First row "0 1", second row "1 2"

---

## 

Which loop controls the number of rows in a nested loop pattern?

A) The innermost loop
B) The outer loop
C) Both loops equally
D) Neither loop

**Answer: B) The outer loop**

**Explanation:** In nested loops for printing patterns, the outer loop typically controls how many rows are printed, while the inner loop controls what gets printed in each row.

---

## 

What will this create?

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

A) All stars
B) All dots
C) Diagonal line of stars
D) Checkerboard pattern

**Answer: C) Diagonal line of stars**

**Explanation:** The condition `i == j` is true only on the diagonal: (0,0), (1,1), (2,2). These positions get '*', all others get '.', creating a diagonal pattern.

---

## 

What is the time complexity of a simple nested loop with both loops running n times?

A) O(n)
B) O(n²)
C) O(2n)
D) O(n log n)

**Answer: B) O(n²)**

**Explanation:** When you have two nested loops both running n times, the total number of iterations is n × n = n². This is quadratic time complexity, written as O(n²).

---

## 

How do you create an inverted triangle (5 rows, decreasing stars)?

A) `for i in range(5, 0, -1): for j in range(i): print('*')`
B) `for i in range(5): for j in range(5-i): print('*')`
C) Both A and B
D) Neither A nor B

**Answer: C) Both A and B**

**Explanation:** Both approaches work:
- A: i goes 5,4,3,2,1, j range uses i directly
- B: i goes 0,1,2,3,4, j range is 5-i which gives 5,4,3,2,1
Both produce the same inverted triangle pattern.

---

## 

What is the purpose of `print()` after the inner loop in pattern printing?

A) Print the pattern
B) End the program
C) Move to the next line/row
D) Clear the screen

**Answer: C) Move to the next line/row**

**Explanation:** The `print()` statement with no arguments outputs a newline character, moving the cursor to the next line. This separates rows in the pattern.

---

## 

How do you access an element in a 2D list at row 2, column 3?

A) `matrix[2][3]`
B) `matrix[3][2]`
C) `matrix(2, 3)`
D) `matrix[2, 3]`

**Answer: A) `matrix[2][3]`**

**Explanation:** Use two sets of square brackets: first for row index, second for column index. `matrix[2][3]` accesses row 2 (third row), column 3 (fourth column) since indexing starts at 0.

---

## 

What creates a checkerboard pattern?

A) `if i == j:`
B) `if (i + j) % 2 == 0:`
C) `if i != j:`
D) `if i < j:`

**Answer: B) `if (i + j) % 2 == 0:`**

**Explanation:** When the sum of indices is even, print one character; when odd, print another. This creates the alternating pattern of a checkerboard.

---

## 

How many nested loops are needed to generate all 3-digit combinations (000-999)?

A) 1
B) 2
C) 3
D) 4

**Answer: C) 3**

**Explanation:** One loop for each digit position: hundreds, tens, and ones. Three nested loops allow iteration through all combinations of three digits.

---

## 

What's the correct way to break out of both nested loops?

A) Use double break
B) Use a flag variable
C) Use return (in a function)
D) Both B and C

**Answer: D) Both B and C**

**Explanation:** Break only exits the innermost loop. To exit both:
- Set a flag in inner loop, check flag after inner loop to break outer
- Or use return if code is in a function, which exits the entire function

---

## 

What does this nested loop create?

```python
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(0)
    matrix.append(row)
```

A) A 1D list of zeros
B) A 3x3 matrix of zeros
C) An empty list
D) Error

**Answer: B) A 3x3 matrix of zeros**

**Explanation:** The outer loop creates 3 rows. For each row, the inner loop appends 3 zeros. The result is a 2D list (matrix) with 3 rows and 3 columns, all filled with zeros.

---

## 

Which is TRUE about nested loops?

A) Inner loop runs once per outer loop iteration
B) Outer loop runs once per inner loop iteration
C) Both loops run simultaneously
D) Only one loop runs at a time

**Answer: A) Inner loop runs once per outer loop iteration**

**Explanation:** For each single iteration of the outer loop, the entire inner loop runs from start to finish. If outer loop has 3 iterations and inner has 4, the inner loop runs completely 3 times (total 12 iterations).

---

## Summary

### Key Concepts Tested:

1. **Basic Structure**: Outer loop for rows, inner for columns
2. **Total Iterations**: Multiply loop counts (m × n)
3. **Patterns**: Triangle, rectangle, diagonal, checkerboard
4. **Indexing**: matrix[row][col] syntax
5. **Control Flow**: Breaking from nested loops
6. **Time Complexity**: O(n²) for double nested
7. **Newline Handling**: `print()` after inner loop
8. **Conditional Patterns**: Using i and j relationships
9. **2D Data Structures**: Creating matrices with nested loops
10. **Multiple Levels**: Triple nesting for 3D iterations

### Common Patterns to Remember:

```python
# Rectangle: m rows, n columns
for i in range(m):
    for j in range(n):
        print('*', end=' ')
    print()

# Right Triangle: increasing
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# Inverted Triangle: decreasing
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

# Diagonal pattern
for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

# Checkerboard pattern
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

### Best Practices:

1. **Start Small**: Test with 3×3 before scaling
2. **Visualize**: Draw the pattern before coding
3. **Name Variables**: Use `row, col` for clarity
4. **Don't Forget Newlines**: Add `print()` after inner loop
5. **Watch Indices**: Ensure correct [row][col] order
6. **Consider Performance**: Nested loops multiply complexity
7. **Test Edge Cases**: Empty lists, single elements
8. **Use Functions**: Extract complex logic from loops


---

