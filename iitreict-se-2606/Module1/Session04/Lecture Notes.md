# Functions in Python

## What You Will Learn in This Lesson

You have already learned how to write Python programs using **variables**, **operators**, **conditional statements**, and **loops**. Your programs can make decisions with `if`/`elif`/`else` and repeat work with `for` and `while` — including `break` and `continue` when needed.

In this lesson, you will learn how to wrap repeated logic into **functions**. You will define functions with **`def`**, pass data using **parameters** and **arguments**, send results back with **`return`**, understand **local vs global scope**, and refactor repeated code into **reusable, readable** pieces.

By the end, you will build modular programs — small named blocks that work together — instead of one long script that is hard to read and hard to fix.

---

## Why Do Programs Need Functions?

- **Official Definition:** A **function** is a reusable block of code that performs a specific task when it is called.
- **In Simple Words:** A function is like a small machine. You give it some input, it does some work, and it can give you an output.
- **Real-Life Example:** A tea stall worker follows the same steps again and again: boil water, add tea, add milk, add sugar, serve. Instead of repeating these steps, we just say "make tea."

Functions are useful because:

- They reduce **repetition** in code.
- They make code easier to **read** and **test**.
- They make code easier to **update**, because a change is made in one place.
- They allow a big problem to be divided into smaller problems.

Without functions, a program becomes like a notebook where the same answer is copied again and again. If one step is wrong, you must fix it everywhere. With functions, you fix it once.

A simple way to picture a function is **input → process → output**, just like an ATM: you enter your PIN and amount (input), it checks your account (process), and it gives cash or a message (output).

![Python functions as a reusable machine where different inputs like numbers, names, and lists are processed into useful outputs such as greetings, bills, and results](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-functions-big-picture.png)

---

## Defining a Function Using `def`

- **Official Definition:** The **`def` keyword** is used in Python to define a function.
- **In Simple Words:** `def` tells Python, "I am creating a new function with this name."
- **Real-Life Example:** Writing a recipe name at the top of a notebook, like "Make Lemon Rice", and then writing the steps below it.

```python
def greet_student():  # Define a function named greet_student
    print("Hello, welcome to Python functions!")  # The work this function should do

greet_student()  # Call the function so the message is displayed
```

**How the code works:**

- `def greet_student():` creates the function.
- The indented `print()` line belongs to the function body.
- `greet_student()` **calls** the function and runs its body.
- **Common mistake:** Defining a function but forgetting to call it. There is no error, but there is also no output.

Every function needs a **clear purpose** in its name. Prefer `calculate_total` or `check_pass_fail` over vague names like `do_stuff` or `func1`.

---

## Function Calls

- **Official Definition:** A **function call** is the instruction that executes a function.
- **In Simple Words:** Calling a function means asking it to do its work now.
- **Real-Life Example:** A restaurant keeps a dosa recipe in the kitchen, but a dosa is made only when a customer places an order.

The definition is like saving the recipe; the call is like placing the order.

```python
def show_menu():  # Define a function to show menu items
    print("1. Idli")  # Display the first item
    print("2. Dosa")  # Display the second item
    print("3. Poha")  # Display the third item

show_menu()  # Run the function for the first time
show_menu()  # Run the same function again
```

**How the code works:**

- The function is written once but called two times.
- The same menu prints twice without copying the `print()` lines again.
- This shows the first big benefit of functions: **write once, reuse many times**.

### Quick Activity: Define and Call

Write a function named `say_welcome` that prints one welcome message. Call it three times and confirm the message appears three times.

```python
def say_welcome():  # Define a simple welcome function
    print("Welcome to the class!")  # Print one clear message

say_welcome()  # First call
say_welcome()  # Second call
say_welcome()  # Third call
```

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
def greet_by_name(name):  # name is a parameter that receives one value
    print("Hello", name)  # Use the received name inside the function

greet_by_name("Anita")  # "Anita" is an argument passed to the function
greet_by_name("Rahul")  # "Rahul" is another argument for the same function
```

**How the code works:**

- `name` behaves like a normal variable inside the function.
- When `"Anita"` is passed, `name` becomes `"Anita"`.
- The same function gives different output for different arguments.

### Multiple Parameters and Positional Arguments

When a function has more than one parameter, arguments are matched **by position** — first argument to first parameter, second to second, and so on.

```python
def show_student(name, city, marks):  # Three parameters in the definition
    print("Name:", name)  # Display the student's name
    print("City:", city)  # Display the student's city
    print("Marks:", marks)  # Display the student's marks

show_student("Priya", "Jaipur", 86)  # Three arguments in the same order
```

**How the code works:**

- `"Priya"` goes to `name`, `"Jaipur"` goes to `city`, and `86` goes to `marks`.
- **Common mistake:** Passing arguments in the wrong order — for example, putting marks where city should be — gives wrong output without an error message.

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

### `print()` vs `return`

| Feature | `print()` | `return` |
|---|---|---|
| Main purpose | Shows output on screen | Sends result back to code |
| Can reuse result later? | No, not directly | Yes |
| Used for | Displaying messages | Building logic and chaining functions |

- **Common mistake:** Forgetting `return`. If a function calculates a value but does not return it, Python gives back `None` by default — and that value cannot be passed usefully to another function.

### Quick Activity: Return a Result

Write a function `multiply(a, b)` that returns the product. Store the result in a variable and print it.

```python
def multiply(a, b):  # Define a function with two parameters
    return a * b  # Return the product to the caller

product = multiply(12, 5)  # Store returned value
print("Product:", product)  # Output: Product: 60
```

---

## Default Parameter Values

- **Official Definition:** A **default parameter value** is a value assigned to a parameter in the function definition, used when no argument is provided for that parameter during the call.
- **In Simple Words:** If the caller does not give a value, Python uses the backup value already written in the function.
- **Real-Life Example:** A food delivery app uses "standard delivery" by default unless you choose express delivery.

```python
def calculate_delivery_fee(distance, rate_per_km=10):  # rate_per_km has a default of 10
    fee = distance * rate_per_km  # Multiply distance by the rate
    return fee  # Return the calculated delivery fee

normal_fee = calculate_delivery_fee(5)  # Only distance given — default rate 10 is used
special_fee = calculate_delivery_fee(5, 15)  # Both distance and custom rate 15 are given

print("Normal fee:", normal_fee)  # Output: 50 (5 × 10)
print("Special fee:", special_fee)  # Output: 75 (5 × 15)
```

**How the code works:**

- `rate_per_km=10` is the default value written in the definition.
- First call passes only `distance`, so Python uses the default rate `10`.
- Second call passes both values, so the custom rate `15` is used instead.
- **Common mistake:** Putting a parameter with a default value before a parameter without one — Python will raise an error. Always write **required parameters first**, then default ones.

```python
def train_fare(distance, rate_per_km=2):  # distance is required, rate has a default
    return distance * rate_per_km  # Calculate and return fare

short_trip = train_fare(50)  # Uses default rate of 2 → fare is 100
long_trip = train_fare(300, 3)  # Uses custom rate of 3 → fare is 900

print("Short trip fare:", short_trip)  # Display fare with default rate
print("Long trip fare:", long_trip)  # Display fare with custom rate
```

---

## Local vs Global Scope

- **Official Definition:** **Scope** is the region of a program where a variable name is visible and usable. A **local variable** exists only inside a function. A **global variable** is defined outside functions and can be read from inside functions.
- **In Simple Words:** Local variables are private notes inside one room. Global variables are notices on the common notice board.
- **Real-Life Example:** A shopkeeper’s rough calculation on a small paper is local to billing. The shop’s GST rate written on the wall is global — every counter can read it.

```python
shop_name = "Masai Mart"  # Global variable — defined outside any function

def discounted_price(price):  # Define a function with price as input
    discount = price * 0.10  # Local variable for ten percent discount
    final_price = price - discount  # Local variable for final price
    print("Shop:", shop_name)  # Reading a global variable is allowed
    return final_price  # Send the final price back

bill = discounted_price(1000)  # Store the returned discounted price
print("Final price:", bill)  # Display the final price
# print(discount)  # This would cause NameError — discount is local
```

**How the code works:**

- `discount` and `final_price` exist only inside the function.
- Outside, we use the returned value stored in `bill`.
- `shop_name` can be **read** inside the function because it is global.
- **Common mistake:** Using a local name outside the function causes `NameError`.

### Why Avoid Changing Globals Inside Functions?

Changing a global from inside a function with `global` is possible, but it makes bugs hard to find — many places can silently change the same value. Prefer **passing inputs as parameters** and **returning results**.

```python
count = 0  # Global counter — avoid depending on this pattern in large programs

def add_one_local(n):  # Prefer this style — clear input and output
    return n + 1  # Return a new value instead of editing a global

count = add_one_local(count)  # Update by using the returned value
print("Count:", count)  # Output: Count: 1
```

**How the code works:**

- The function does not secretly edit `count` inside its body.
- The caller decides when to update `count` using the returned value.
- This style avoids common scope bugs and keeps each function easy to test.

| Kind | Where created | Who can use it | Typical use |
|------|---------------|----------------|-------------|
| **Local** | Inside a function | Only that function | Temporary calculations |
| **Global** | Outside functions | Readable from functions | Shared config (use carefully) |

---

## Connecting Functions — Output Becomes Input

- **Official Definition:** **Function composition** means using the output of one function as the input to another function.
- **In Simple Words:** One function finishes its work and passes the result to the next function — like passing a baton in a relay race.
- **Real-Life Example:** At a railway counter, one person checks seat availability, another calculates fare, and another prints the ticket. Each step depends on the previous one.

![Return values and function chaining shown as a shopping bill pipeline where subtotal, delivery charge, coupon discount, and final bill pass outputs from one step to the next](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-return-function-chaining.png)

```python
def calculate_subtotal(price, quantity):  # Calculate item subtotal
    return price * quantity  # Multiply price by quantity and return it

def add_delivery(amount):  # Add a fixed delivery charge
    return amount + 40  # Return amount after delivery charge

def apply_coupon(amount):  # Apply a fixed coupon discount
    return amount - 50  # Return amount after coupon

item_total = calculate_subtotal(250, 3)  # Step 1: 250 × 3 = 750
with_delivery = add_delivery(item_total)  # Step 2: 750 + 40 = 790
final_bill = apply_coupon(with_delivery)  # Step 3: 790 - 50 = 740

print("Final bill:", final_bill)  # Display the final bill
```

**How the code works:**

- Each function has one clear job; the main program connects them in order.
- You can also nest calls: `apply_coupon(add_delivery(calculate_subtotal(250, 3)))` — innermost runs first.

---

## Modular Programming — Reusable, Readable Code

- **Official Definition:** **Modular programming** is an approach where a program is divided into smaller, independent, reusable parts called functions or modules.
- **In Simple Words:** Instead of one big block of code, we split the program into small pieces, where each piece does one job.
- **Real-Life Example:** A college admission process has separate counters: document check, fee payment, ID card, and final confirmation.

The key idea is simple: **one function should do one clear job**.

![Modular programming shown as one large messy program being split into small reusable functions for total calculation, percentage calculation, result decision, and report printing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-modular-programming.png)

```python
def calculate_total(m1, m2, m3):  # Calculate total marks of three subjects
    return m1 + m2 + m3  # Add all marks and return the total

def calculate_percentage(total):  # Calculate percentage from total
    return total / 3  # Divide by number of subjects and return it

def decide_result(percentage):  # Decide pass or fail
    if percentage >= 40:  # Check if percentage is at least 40
        return "Pass"  # Return Pass for eligible percentage
    else:  # Handle percentage below 40
        return "Fail"  # Return Fail for low percentage

total = calculate_total(78, 84, 69)  # Calculate total marks
percentage = calculate_percentage(total)  # Output of calculate_total becomes input here
result = decide_result(percentage)  # Output of calculate_percentage becomes input here

print("Total:", total)  # Display total marks
print("Percentage:", percentage)  # Display percentage
print("Result:", result)  # Display final result
```

**How the code works:**

- `calculate_total` returns `231` → passed to `calculate_percentage`.
- `calculate_percentage` returns `77.0` → passed to `decide_result`.
- Each function is small, named clearly, and easy to test on its own.

### Refactoring Repeated Logic

Repeated `if` checks for many students are a signal to extract a function.

```python
def check_pass_fail(marks):  # Define a reusable result-checking function
    if marks >= 40:  # Check the passing condition
        return "Pass"  # Return Pass if marks are enough
    else:  # Handle marks below the passing score
        return "Fail"  # Return Fail if marks are low

print(check_pass_fail(85))  # Check result for one student
print(check_pass_fail(32))  # Check result for another student
```

Combine functions with **loops** from earlier learning when you need the same check for many values:

```python
marks_list = [85, 32, 67, 40]  # Several students' marks
for m in marks_list:  # Loop over each mark
    print(m, "→", check_pass_fail(m))  # Reuse the same function each time
```

Readable function habits to follow as you write more code:

- Choose **verb-based names** that state the job (`calculate_total`, not `ct`).
- Keep the body short — if it does two jobs, split into two functions.
- Prefer **return + store** over printing inside every helper, so results can be reused.

---

## Practice Activities

### Activity 1: Mobile Recharge Calculator

Build a recharge calculator by connecting three functions. The output of each function becomes the input of the next.

```python
def base_amount(plan_price, months):  # Calculate base recharge amount
    return plan_price * months  # Multiply plan price by months and return it

def add_platform_fee(amount):  # Add a fixed platform fee
    return amount + 10  # Return amount after platform fee

def apply_cashback(amount):  # Apply a fixed cashback
    return amount - 25  # Return final payable amount

base = base_amount(299, 3)  # Step 1: 299 × 3 = 897
with_fee = add_platform_fee(base)  # Step 2: 897 + 10 = 907
payable = apply_cashback(with_fee)  # Step 3: 907 - 25 = 882

print("Payable amount:", payable)  # Display final payable amount
```

### Activity 2: Function Chaining with Default Values

Create a food order flow where delivery fee uses a default rate.

```python
def order_total(item_price, quantity):  # Calculate order subtotal
    return item_price * quantity  # Return price × quantity

def add_delivery(amount, rate=30):  # Add delivery charge with default rate of 30
    return amount + rate  # Return amount plus delivery charge

def apply_discount(amount):  # Apply a 10% discount
    discount = amount * 0.10  # Calculate ten percent discount
    return amount - discount  # Return amount after discount

subtotal = order_total(150, 4)  # Step 1: 150 × 4 = 600
with_delivery = add_delivery(subtotal)  # Step 2: 600 + 30 (default) = 630
final = apply_discount(with_delivery)  # Step 3: 630 - 63 = 567

print("Final order amount:", final)  # Display the final amount
```

### Activity 3: Scope Check

Predict the output, then run the code. Confirm which names are local and which are global.

```python
tax_rate = 0.05  # Global configuration value

def add_tax(amount):  # amount is a parameter (local to this call)
    tax = amount * tax_rate  # tax is local; tax_rate is read from global
    return amount + tax  # Return amount including tax

print(add_tax(200))  # Output: 210.0
# print(tax)  # Would raise NameError — tax is local
```

---

## Common Errors to Watch For

- **Forgetting parentheses:** `say_hello` only refers to the function; `say_hello()` actually calls it.
- **Indentation mistakes:** Indented lines belong to the function; non-indented lines run outside it.
- **Missing `return`:** A function without `return` gives back `None`.
- **Wrong argument order:** Arguments fill parameters by position, so the order must match.
- **Default before required:** A parameter with a default value must come after parameters without defaults.
- **Scope bugs:** Do not use local variables outside the function; prefer parameters and return values over editing globals.

Testing a function with normal, boundary, and unusual inputs builds confidence that it works correctly.

---

## Key Takeaways

- A **function** is a reusable block of code created with `def` and executed using a function call.
- **Parameters** receive input in the definition; **arguments** are the actual values passed during the call. **Default values** act as backups when an argument is omitted.
- **`return`** sends a result back so it can be stored, reused, or passed as input to another function.
- **Local vs global scope** controls where a name is visible — keep most data local and pass values through parameters/returns to avoid silent bugs.
- **Modular programming** divides a large program into small, clear functions, each with one responsibility — then combine them with loops and conditions you already know.

These reusable blocks become the base for cleaner Python programs as you move into larger data structures and problem-solving patterns in upcoming lessons.

---

## Important Commands, Libraries, and Terminologies

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| `def` | Keyword used to define a function | `def greet():` |
| Function call | Instruction to run a function | `greet()` |
| Parameter | Variable in the function definition | `def greet(name):` |
| Argument | Actual value passed during a call | `greet("Anita")` |
| `return` | Sends a result back from a function | `return total` |
| Default parameter | Backup value used if no argument is given | `rate_per_km=10` |
| Local variable | Variable created inside a function | `discount = price * 0.10` |
| Global variable | Variable defined outside functions | `shop_name = "Masai Mart"` |
| Scope | Region where a name is visible | Local inside function; global outside |
| Function composition | Output of one function used as input to another | `double(square(5))` |
| Modular programming | Dividing code into small reusable functions | Separate total, percentage, result functions |
| `None` | Default return when `return` is missing | Forgotten `return` → `None` |
