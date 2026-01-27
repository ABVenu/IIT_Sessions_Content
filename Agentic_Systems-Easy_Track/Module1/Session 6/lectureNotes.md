# Python: Automation & Loops

## What You’ll Learn

In this lesson, you’ll learn how programs repeat work efficiently instead of doing the same task again and again by hand. You’ll understand how loops automate repetition, how Python iterates over collections of data, and how loop control statements guide execution. These ideas are essential for AI systems, where programs routinely process thousands—or millions—of items in a structured way.

![Loops](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/563e97d2-f26f-4711-aa07-21f9e6033b46/YJJHdO1djBjULrZy.png)

---

## 1. Why Automation and Loops Matter

Automation is the backbone of computing. Computers are not powerful because they can do complex things once; they are powerful because they can do simple things **reliably and repeatedly**.

In AI and data-driven systems, repetition is everywhere:
- Processing rows of data
- Training models over many iterations
- Evaluating predictions one by one
- Repeating steps until a condition is met

Loops are the mechanism that turns a single instruction into a scalable process. Without loops, AI systems would not be practical.

---

## 2. The `for` Loop: Repeating Work Over a Sequence

### What Is a `for` Loop?

A `for` loop allows you to execute a block of code **once for each item in a collection**. In Python, this is most commonly used to iterate over lists, strings, or ranges of numbers.

A basic `for` loop looks like this:

```python
for number in [1, 2, 3, 4]:
    print(number)
````

This reads as:

> For each number in the list, print it.

Python automatically:

* Takes one item at a time
* Assigns it to the loop variable
* Executes the indented block

---

### Iterating Over a Range of Numbers

Python provides the `range()` function to generate a sequence of numbers.

```python
for i in range(5):
    print(i)
```

This prints:

```
0
1
2
3
4
```

Important detail: `range(n)` starts at `0` and stops *before* `n`.

This pattern is extremely common in AI code, especially when running training steps or repeated evaluations.

---

## 3. Iterating Over Simple Lists

Lists are one of the most common data structures in Python. Loops allow you to process each element systematically.

```python
models = ["linear", "tree", "neural"]

for model in models:
    print(f"Training {model} model")
```

This approach is clearer and safer than indexing manually. Instead of worrying about positions, you work directly with the values.

In AI workflows, this pattern appears when:

* Looping over datasets
* Evaluating multiple experiments
* Applying the same transformation to many inputs

---

## 4. The `while` Loop: Repeating Until a Condition Changes

### What Is a `while` Loop?

A `while` loop repeats code **as long as a condition remains true**.

```python
count = 0

while count < 3:
    print("Processing batch")
    count += 1
```

This reads as:

> While the condition is true, keep looping.

Unlike `for` loops, which iterate over a fixed collection, `while` loops are used when:

* You don’t know in advance how many iterations are needed
* The stopping condition depends on runtime behavior

---

### Common Use Cases for `while` Loops

`while` loops are often used for:

* Waiting for a process to complete
* Retrying an operation
* Monitoring system state
* Interactive programs

Example:

```python
password = ""

while password != "admin123":
    password = input("Enter password: ")
```

This loop continues until the correct input is provided.

---

## 5. Loop Control: `break` and `continue`

### The `break` Statement

The `break` statement **immediately exits a loop**, even if the loop condition is still true.

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

This stops the loop as soon as `number` reaches 5.

In AI systems, `break` is often used to:

* Stop early when a condition is met
* Exit when an error is detected
* Terminate search or optimization processes

---

### The `continue` Statement

The `continue` statement skips the **rest of the current iteration** and moves to the next one.

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

This prints all numbers except 2.

`continue` is useful when:

* Some items should be ignored
* Certain conditions require skipping processing
* Filtering logic is needed inside loops

---

## 6. Indentation and Loop Structure

Just like conditionals, loops rely on indentation to define what belongs inside them.

```python
for i in range(3):
    print("Inside loop")
print("Outside loop")
```

Only the indented line repeats. Misplaced indentation is one of the most common beginner errors and can silently change program behavior.

Python’s design enforces clarity: **structure is visible at a glance**.

---

## 7. A Realistic Example: Automating a Task

```python
scores = [72, 45, 89, 60]

for score in scores:
    if score < 50:
        print("Fail")
        continue
    print("Pass")
```

This example combines:

* List iteration
* Conditionals
* Loop control
* Automation logic

Such patterns are foundational in AI pipelines, where each data point must be evaluated consistently.

---

## 8. Common Beginner Mistakes

* Forgetting to update the condition in a `while` loop (infinite loops)
* Confusing `break` and `continue`
* Overusing `while` when `for` is clearer
* Incorrect indentation

These mistakes are normal. Python’s error messages and careful reading usually reveal the issue.

---

## Key Takeaways

Loops allow programs to automate repetition. `for` loops iterate over known sequences, while `while` loops repeat until conditions change. Lists are commonly processed using loops, and `break` and `continue` provide fine-grained control over execution. Together, these tools enable scalable, efficient programs—the foundation of AI automation.

**Mental model:**
Loops repeat work.
`for` iterates over items.
`while` waits on conditions.
`break` stops.
`continue` skips.

---

## Additional Reading

* Python Loops (Official Tutorial):
  [https://docs.python.org/3/tutorial/controlflow.html#for-statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

* Iteration Patterns in Python:
  [https://developers.google.com/edu/python/loops](https://developers.google.com/edu/python/loops)

* Writing Clear Loops in Python:
  [https://realpython.com/python-for-loop/](https://realpython.com/python-for-loop/)
