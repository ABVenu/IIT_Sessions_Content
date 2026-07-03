# Python Functions & Modular Programming

## What You Will Learn in This Lesson

You have already learned how Python programs use **conditions**, **loops**, **lists**, and **dictionaries** to solve problems step by step. You have also seen that when a program grows, the same logic often repeats many times.

In this lesson, you will learn how to write **functions** so that repeated logic is written once and reused many times. You will also learn how **parameters**, **arguments**, **return values**, **default values**, and **function calls** help divide a big program into smaller, clear, reusable parts.

By the end, you will be able to create your own functions, pass data into them, get results back, connect one function's output to another function's input, and organize Python programs in a modular way.

---

## Why Do Programs Need Functions?

- **Official Definition:** A **function** is a reusable block of code that performs a specific task when it is called.
- **In Simple Words:** A function is like a small machine. You give it some input, it does some work, and it can give you an output.
- **Real-Life Example:** Every morning you make tea. You learned to boil water once, and now you repeat that step without reading the recipe again. Boiling water is a reusable step in your tea routine.

Functions are useful because:

- They reduce **repetition** in code.
- They make code easier to **read** and **test**.
- They make code easier to **update**, because a change is made in one place.
- They allow a big problem to be divided into smaller problems.

A key guideline in software development is **DRY — Don't Repeat Yourself**. Instead of copying the same lines again and again, you write the logic once inside a function and call it whenever needed.

Without functions, a program becomes like a notebook where the same answer is copied again and again. If one step is wrong, you must fix it everywhere. With functions, you fix it once.

A simple way to picture a function is **input → process → output**, just like an ATM: you enter your PIN and amount (input), it checks your account (process), and it gives cash or a message (output).

![Python functions as a reusable machine where different inputs like numbers, names, and lists are processed into useful outputs such as greetings, bills, and results](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-functions-big-picture.png)

---

## Defining a Function Using `def`

- **Official Definition:** The **`def` keyword** is used in Python to define a function.
- **In Simple Words:** `def` tells Python, "I am creating a new function with this name."
- **Real-Life Example:** Writing a recipe name at the top of a notebook, like "Make Lemon Rice", and then writing the steps below it.

```python
def greet_user():  # Define a function named greet_user
    print("Hello world from function")  # The work this function should do

greet_user()  # Call the function so the message is displayed
```

**How the code works:**

- `def greet_user():` creates the function.
- The indented `print()` line belongs to the function.
- `greet_user()` calls the function and runs its body.
- **Common mistake:** Defining a function but forgetting to call it. There is no error, but there is also no output.

### Predefined vs User-Defined Functions

`print()` is also a function in Python, but it is a **predefined** function — Python already knows about it. When you write `greet_user()`, you are calling a **user-defined** function that you created yourself. Python will raise an error if you call a function that has not been defined yet.

### Function Naming Guidelines

There are no strict naming rules, but good practice is to name a function after what it does:

- Adding two numbers → `add_numbers`
- Multiplying two numbers → `multiply`
- Sending an email → `send_email`

### Define Before You Call

In Python, a function must be **defined above** the line where you call it. If you call `greet_user()` on line 6, the `def greet_user():` block must appear before line 6.

Whatever you write inside a function is **scoped** to that function — it belongs to that function only.

---

## Function Calls

- **Official Definition:** A **function call** is the instruction that executes a function.
- **In Simple Words:** Calling a function means asking it to do its work now.
- **Real-Life Example:** A person is sitting in a room, but nothing happens until you call their name and ask them to help.

The definition is like saving the recipe; the call is like placing the order.

```python
def add_two_numbers():  # Define a function that takes two inputs from the user
    a = int(input("Enter A: "))  # Read the first number
    b = int(input("Enter B: "))  # Read the second number
    c = a + b  # Add both numbers
    print("Sum is", c)  # Display the result

add_two_numbers()  # Run the function for the first time
add_two_numbers()  # Run the same function again with new inputs
```

**How the code works:**

- The function is written once but called two times.
- Each call asks the user for two new numbers and prints the sum.
- This shows the first big benefit of functions: **write once, reuse many times**.

When Python runs your program, it reads the function definition first. When it reaches a function call, the **code pointer** jumps into the function, runs all its lines, and then returns to the next line after the call.

---

## Parameters and Arguments

- **Official Definition:** A **parameter** is a variable written in the function definition to receive input. An **argument** is the actual value passed during the function call.
- **In Simple Words:** A parameter is the empty box inside the function; an argument is the item you put into that box.
- **Real-Life Example:** In a food delivery app, "delivery address" is the parameter; "Flat 302, Pune" is the argument.

| Part | Where it appears | Example |
|---|---|---|
| **Parameter** | Inside the function definition | `def greet(name):` → `name` is a parameter |
| **Argument** | Inside the function call | `greet("Anita")` → `"Anita"` is an argument |

![Parameters as empty order slots, arguments as actual filled choices, and default values as backup options when no custom value is provided](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-parameters-arguments-default-values.png)

```python
def add_two_numbers(number1, number2):  # number1 and number2 are parameters
    total = number1 + number2  # Add the received values
    print("Sum is", total)  # Display the result

add_two_numbers(10, 20)  # 10 and 20 are arguments passed to the function
add_two_numbers(5, 7)  # Different arguments give a different result
```

**How the code works:**

- `number1` and `number2` behave like normal variables inside the function.
- When `10` and `20` are passed, those values are used for the addition.
- The same function gives different output for different arguments.

### Multiple Parameters and Positional Arguments

When a function has more than one parameter, arguments are matched **by position** — first argument to first parameter, second to second, and so on.

```python
def add_two_numbers(number1, number2):  # Two parameters in the definition
    result = number1 + number2  # Add both values
    print("Result:", result)  # Display the sum

add_two_numbers(10, 20)  # 10 goes to number1, 20 goes to number2
```

**How the code works:**

- If you pass only one argument when two are required, Python raises an error about a missing positional argument.
- **Common mistake:** Passing arguments in the wrong order gives wrong output.

---

## How Python Runs Your Code

- **Official Definition:** In every Python program, your top-level code runs inside an implicit **main** execution context.
- **In Simple Words:** Python always has a starting point. Your code runs line by line, and when you call a function, Python jumps into that function and comes back when it finishes.
- **Real-Life Example:** A manager (main program) assigns tasks to team members (functions). Each person completes their task and reports back before the manager continues.

```python
def greet_user():  # Define the greet function
    print("Hello from greet_user")  # Runs when greet_user is called

def add_two_numbers(a, b):  # Define a second function
    print("Sum is", a + b)  # Runs when add_two_numbers is called

print("Line 1 in main")  # Main code starts here
greet_user()  # Control jumps into greet_user, then returns here
add_two_numbers(3, 4)  # Control jumps into add_two_numbers, then returns here
print("Line 2 in main")  # Main code continues after both calls
```

**How the code works:**

- Python runs `print("Line 1 in main")` first.
- At `greet_user()`, execution moves into that function and returns when it finishes.
- At `add_two_numbers(3, 4)`, execution moves into that function and returns again.
- You can call one function from inside another function. This nesting can go to any level as long as each function is defined in the same file (or imported from another file).

---

## Returning Values Using `return`

- **Official Definition:** The **`return` statement** sends a value back from a function to the place where it was called.
- **In Simple Words:** `return` means "Here is the answer from this function."
- **Real-Life Example:** You give two numbers to a calculator; it does the work and gives the answer back to you.

`print()` only shows a value on screen. `return` gives a value back so it can be stored, reused, or passed to another function.

```python
def add_numbers(a, b):  # Define a function with two input numbers
    total = a + b  # Add both numbers and store the result
    return total  # Send the result back to the caller

answer = add_numbers(10, 20)  # Call the function and store the returned value
print("Total:", answer)  # Display the stored result
```

**How the code works:**

- `a` becomes `10` and `b` becomes `20`, so `total` becomes `30`.
- `return total` sends `30` back, which is stored in `answer`.
- If you write `sum = add_numbers(2, 4)` without `return`, `sum` would be `None`.

### `print()` vs `return`

| Feature | `print()` | `return` |
|---|---|---|
| Main purpose | Shows output on screen | Sends result back to code |
| Can reuse result later? | No, not directly | Yes |
| Used for | Displaying messages | Building logic and chaining functions |

- **Common mistake:** Forgetting `return`. If a function calculates a value but does not return it, Python gives back `None` by default — and that value cannot be passed to another function.

### Using a Returned Value for More Work

Once a function returns a value, you can use that value in further calculations:

```python
def add_numbers(a, b):  # Add two numbers and return the sum
    return a + b  # Send the sum back

n = add_numbers(1, 2)  # n becomes 3
sum_of_natural = n * (n + 1) // 2  # Use returned n in the formula n(n+1)/2
print("Sum of first", n, "natural numbers:", sum_of_natural)  # Output: 6
```

**How the code works:**

- `add_numbers(1, 2)` returns `3`, stored in `n`.
- The formula uses that returned value to compute the sum of the first `n` natural numbers.
- This is only possible because the function **returned** the value instead of only printing it.

---

## Default Parameter Values

- **Official Definition:** A **default parameter value** is a value assigned to a parameter in the function definition, used when no argument is provided for that parameter during the call.
- **In Simple Words:** If the caller does not give a value, Python uses the backup value already written in the function.
- **Real-Life Example:** A food delivery app uses "standard delivery" by default unless you choose express delivery.

```python
def add_two_numbers(a, b=0):  # b has a default value of 0
    total = a + b  # Add both numbers
    return total  # Return the sum

result1 = add_two_numbers(10)  # Only a is passed — b uses default 0 → result is 10
result2 = add_two_numbers(10, 10)  # Both values passed → result is 20

print("Result 1:", result1)  # Output: 10
print("Result 2:", result2)  # Output: 20
```

**How the code works:**

- `b=0` is the default value written in the definition.
- First call passes only `a`, so Python uses the default `b=0`.
- Second call passes both values, so the custom `b=10` is used.
- You can set default values for all parameters if needed.
- **Common mistake:** Putting a parameter with a default value before a parameter without one — Python will raise an error. Always write required parameters first, then default ones.

---

## Connecting Functions — Output Becomes Input

- **Official Definition:** **Function composition** means using the output of one function as the input to another function.
- **In Simple Words:** One function finishes its work and passes the result to the next function — like passing a baton in a relay race.
- **Real-Life Example:** At a restaurant counter, one person calculates item totals, another adds tax, and another gives the final bill. Each step depends on the previous one.

This is one of the most important ideas in modular programming: **the return value of Function A becomes the argument of Function B**.

![Return values and function chaining shown as a shopping bill pipeline where subtotal, delivery charge, coupon discount, and final bill pass outputs from one step to the next](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-return-function-chaining.png)

### Restaurant Billing Example

A restaurant has three items with fixed prices: Item 1 = ₹200, Item 2 = ₹300, Item 3 = ₹400. The program asks the user for quantities, calculates each item total, sums them, adds 10% tax, and prints the final amount.

**Step 1 — Without functions (all logic in one place):**

```python
item1_qty = int(input("Enter quantity of item 1: "))  # Read quantity for item 1
item2_qty = int(input("Enter quantity of item 2: "))  # Read quantity for item 2
item3_qty = int(input("Enter quantity of item 3: "))  # Read quantity for item 3

total_item1 = item1_qty * 200  # Item 1 costs 200 per unit
total_item2 = item2_qty * 300  # Item 2 costs 300 per unit
total_item3 = item3_qty * 400  # Item 3 costs 400 per unit

total_amount = total_item1 + total_item2 + total_item3  # Sum all item totals
tax = total_amount * 0.10  # Calculate 10% tax
final_amount = total_amount + tax  # Add tax to get final bill

print("Total amount to be collected:", final_amount)  # Display the final bill
```

**Step 2 — Refactored into reusable functions:**

```python
def total_for_item(item, quantity):  # Calculate total for one item based on its price
    if item == "item1":  # Check which item was ordered
        return quantity * 200  # Item 1 rate is 200
    elif item == "item2":  # Check for item 2
        return quantity * 300  # Item 2 rate is 300
    else:  # Handle item 3
        return quantity * 400  # Item 3 rate is 400

def calculate_total(t1, t2, t3):  # Add three item totals together
    return t1 + t2 + t3  # Return the combined total

def final_amount(total):  # Add 10% tax to the total
    return total + total * 0.10  # Return total plus 10% tax

item1_qty = int(input("Enter quantity of item 1: "))  # Read quantity for item 1
item2_qty = int(input("Enter quantity of item 2: "))  # Read quantity for item 2
item3_qty = int(input("Enter quantity of item 3: "))  # Read quantity for item 3

t1 = total_for_item("item1", item1_qty)  # Calculate total for item 1
t2 = total_for_item("item2", item2_qty)  # Calculate total for item 2
t3 = total_for_item("item3", item3_qty)  # Calculate total for item 3

total = calculate_total(t1, t2, t3)  # Output of total_for_item functions becomes input here
bill = final_amount(total)  # Output of calculate_total becomes input here

print("Total amount to be collected:", bill)  # Display the final bill
```

**How the code works:**

- `total_for_item` is reused three times with different items — no repeated price logic.
- `calculate_total(t1, t2, t3)` receives the three returned totals and returns their sum.
- `final_amount(total)` receives that sum and returns the amount with 10% tax added.
- Each function has one clear job; the main program connects them in order.

---

## Modular Programming

- **Official Definition:** **Modular programming** is an approach where a program is divided into smaller, independent, reusable parts called functions or modules.
- **In Simple Words:** Instead of one big block of code, we split the program into small pieces, where each piece does one job.
- **Real-Life Example:** A college admission process has separate counters: document check, fee payment, ID card, and final confirmation. Each counter has one responsibility.

Modular programming helps because:

- Each function is easier to understand and test.
- Bugs become easier to find.
- Reusable parts can be used again in future programs.
- The main program stays clean.

The key idea is simple: **one function should do one clear job**. The restaurant billing example above shows this — `total_for_item`, `calculate_total`, and `final_amount` each handle one step.

![Modular programming shown as one large messy program being split into small reusable functions for total calculation, percentage calculation, result decision, and report printing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-modular-programming.png)

---

## Common Errors to Watch For

- **Forgetting parentheses:** `greet_user` only refers to the function; `greet_user()` actually calls it.
- **Indentation mistakes:** Indented lines belong to the function; non-indented lines run outside it.
- **Calling before defining:** A function must be defined above the line where you call it.
- **Missing `return`:** A function without `return` gives back `None`, so the calculated value cannot be passed to another function.
- **Wrong argument order:** Arguments fill parameters by position, so the order must match.
- **Default before required:** A parameter with a default value must come after parameters without defaults.
- **Defining but never calling:** A defined function does nothing until you call it.

Testing a function with normal, boundary, and unusual inputs builds confidence that it works correctly.

---

## Key Takeaways

- A **function** is a reusable block of code created with `def` and executed using a function call.
- **Parameters** receive input inside the function definition; **arguments** are the actual values passed during the call.
- **`return`** sends a result back so it can be stored, reused, or passed as input to another function.
- **Default parameter values** provide a backup when the caller does not pass that argument.
- **Function chaining** connects functions so one function's output becomes another function's input.
- **Modular programming** and the **DRY principle** help you divide a large program into small, clear, reusable functions.

In the next lesson, you will use these reusable blocks inside larger problem-solving patterns, making functions the base for cleaner, more professional Python programs.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| `def` | Keyword used to define a function | `def greet_user():` |
| Function call | Instruction to run a function | `greet_user()` |
| Parameter | Variable in the function definition | `def greet(name):` |
| Argument | Actual value passed during a call | `greet("Anita")` |
| `return` | Sends a result back from a function | `return total` |
| Default parameter | Backup value used if no argument is given | `b=0` |
| DRY | Don't Repeat Yourself — avoid copying the same code | Write once in a function, call many times |
| Function composition | Output of one function used as input to another | `final_amount(calculate_total(t1, t2, t3))` |
| Modular programming | Dividing code into small reusable functions | Separate item total, sum, and tax functions |
| Predefined function | Function already built into Python | `print("Hello")` |
| User-defined function | Function you create with `def` | `def greet_user():` |
