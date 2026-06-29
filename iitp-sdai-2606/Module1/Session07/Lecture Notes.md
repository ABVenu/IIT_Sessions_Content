# Python Functions & Modular Programming

## What You Will Learn in This Lesson

You have already learned how Python programs use **conditions**, **loops**, **lists**, and **dictionaries** to solve problems step by step. You have also seen that when a program grows, the same logic often repeats many times.

In this lesson, you will learn how to write **functions** so that repeated logic is written once and reused many times. You will also learn how **parameters**, **arguments**, **return values**, **default values**, and **function calls** help divide a big program into smaller, clear, reusable parts.

By the end, you will be able to create your own functions, pass data into them, get results back, connect one function's output to another function's input, and organize Python programs in a modular way.

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
- The indented `print()` line belongs to the function.
- `greet_student()` calls the function and runs its body.
- **Common mistake:** Defining a function but forgetting to call it. There is no error, but there is also no output.

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
- **Common mistake:** Passing arguments in the wrong order — for example, putting marks where city should be — gives wrong output.

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

- **Common mistake:** Forgetting `return`. If a function calculates a value but does not return it, Python gives back `None` by default — and that value cannot be passed to another function.

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
- **Common mistake:** Putting a parameter with a default value before a parameter without one — Python will raise an error. Always write required parameters first, then default ones.

### Another Example: Train Fare with Default Rate

```python
def train_fare(distance, rate_per_km=2):  # distance is required, rate has a default
    return distance * rate_per_km  # Calculate and return fare

short_trip = train_fare(50)  # Uses default rate of 2 → fare is 100
long_trip = train_fare(300, 3)  # Uses custom rate of 3 → fare is 900

print("Short trip fare:", short_trip)  # Display fare with default rate
print("Long trip fare:", long_trip)  # Display fare with custom rate
```

**How the code works:**

- The same formula works for many situations just by changing the input or overriding the default.
- Default values make functions flexible without forcing the caller to pass every value every time.

---

## Local Variables Inside Functions

- **Official Definition:** A **local variable** is created inside a function and is available only inside that function.
- **In Simple Words:** A local variable belongs to one function only; other parts of the program cannot use it directly.
- **Real-Life Example:** A shopkeeper does a rough calculation on a small paper while preparing your bill; that paper is used only inside the billing process.

```python
def discounted_price(price):  # Define a function with price as input
    discount = price * 0.10  # Local variable for ten percent discount
    final_price = price - discount  # Local variable for final price
    return final_price  # Send the final price back

bill = discounted_price(1000)  # Store the returned discounted price
print("Final price:", bill)  # Display the final price
```

**How the code works:**

- `discount` and `final_price` exist only inside the function.
- Outside, we use the returned value stored in `bill`.
- **Common mistake:** Using `discount` outside the function causes an error because it is local.

---

## Connecting Functions — Output Becomes Input

- **Official Definition:** **Function composition** means using the output of one function as the input to another function.
- **In Simple Words:** One function finishes its work and passes the result to the next function — like passing a baton in a relay race.
- **Real-Life Example:** At a railway counter, one person checks seat availability, another calculates fare, and another prints the ticket. Each step depends on the previous one.

This is one of the most important ideas in modular programming: **the return value of Function A becomes the argument of Function B**.

![Return values and function chaining shown as a shopping bill pipeline where subtotal, delivery charge, coupon discount, and final bill pass outputs from one step to the next](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-return-function-chaining.png)

### Step-by-Step Chaining (Using Variables)

```python
def calculate_subtotal(price, quantity):  # Calculate item subtotal
    return price * quantity  # Multiply price by quantity and return it

def add_delivery(amount):  # Add a fixed delivery charge
    return amount + 40  # Return amount after delivery charge

def apply_coupon(amount):  # Apply a fixed coupon discount
    return amount - 50  # Return amount after coupon

item_total = calculate_subtotal(250, 3)  # Step 1: 250 × 3 = 750
with_delivery = add_delivery(item_total)  # Step 2: 750 + 40 = 790 (output of Step 1 is input here)
final_bill = apply_coupon(with_delivery)  # Step 3: 790 - 50 = 740 (output of Step 2 is input here)

print("Final bill:", final_bill)  # Display the final bill
```

**How the code works:**

- `calculate_subtotal(250, 3)` returns `750` → stored in `item_total`.
- `add_delivery(item_total)` receives `750` as its argument → returns `790`.
- `apply_coupon(with_delivery)` receives `790` as its argument → returns `740`.
- Each function has one clear job; the main program connects them in order.

### Nested Function Calls (One Inside Another)

You can also pass a function call directly as an argument to another function, without storing the middle result in a variable.

```python
def square(number):  # Calculate square of a number
    return number * number  # Multiply the number by itself

def double(number):  # Calculate double of a number
    return number * 2  # Multiply the number by two

result = double(square(5))  # square(5) returns 25, then double(25) returns 50
print("Result:", result)  # Display the final result
```

**How the code works:**

- Python runs the **innermost** call first: `square(5)` returns `25`.
- Then `double(25)` runs and returns `50`.
- The output of `square` becomes the input of `double` automatically.

### Real-World Example: GST Bill Pipeline

```python
def item_cost(price, qty):  # Calculate cost for one item
    return price * qty  # Return price multiplied by quantity

def add_gst(amount):  # Add 18% GST to an amount
    gst = amount * 0.18  # Calculate GST amount
    return amount + gst  # Return total including GST

def round_bill(amount):  # Round the bill to nearest rupee
    return round(amount)  # Return rounded amount

rice_bill = item_cost(60, 5)  # Step 1: rice cost = 300
with_gst = add_gst(rice_bill)  # Step 2: 300 + 54 GST = 354
final = round_bill(with_gst)  # Step 3: round 354.0 → 354

print("Rice bill with GST:", final)  # Display final rounded bill

# Same pipeline in one nested line:
nested_result = round_bill(add_gst(item_cost(60, 5)))  # All three steps in one expression
print("Nested result:", nested_result)  # Same answer: 354
```

**How the code works:**

- Step-by-step version stores each result in a variable — easier to read and debug.
- Nested version does the same work in one line — `item_cost` output feeds `add_gst`, whose output feeds `round_bill`.
- Both approaches produce the same result; choose based on readability.

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

The key idea is simple: **one function should do one clear job**.

![Modular programming shown as one large messy program being split into small reusable functions for total calculation, percentage calculation, result decision, and report printing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session07/session07-modular-programming.png)

### Example: Modular Student Result Program

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

- `calculate_total` returns `231` → passed as argument to `calculate_percentage`.
- `calculate_percentage` returns `77.0` → passed as argument to `decide_result`.
- `decide_result` returns `"Pass"`.
- Each function is small, named clearly, and easy to test on its own.

---

## Activity: Mobile Recharge Calculator

Build a recharge calculator by connecting three functions. The output of each function becomes the input of the next.

- `base_amount(plan_price, months)` — calculates total plan cost.
- `add_platform_fee(amount)` — adds a fixed fee of `10`.
- `apply_cashback(amount)` — subtracts cashback of `25`.

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

**How the code works:**

- Each function does one job and returns its result.
- The main code connects them step by step — output of one becomes input of the next.
- Try changing `299` to another plan price and `3` to another number of months; the same functions still work.

---

## Activity: Function Chaining with Default Values

Create a food order system where delivery fee uses a default rate, and each function's output feeds the next.

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

**How the code works:**

- `order_total` returns `600` → becomes input to `add_delivery`.
- `add_delivery` uses the default rate `30` because no custom rate was passed → returns `630`.
- `apply_discount` receives `630` → returns `567`.
- This activity combines **default values**, **return values**, and **function chaining** in one flow.

---

## Activity: Convert Repeated Code Into a Function

Repeated decision logic is a sign that a function is needed. Convert this pattern into a reusable function:

```python
def check_pass_fail(marks):  # Define a reusable result-checking function
    if marks >= 40:  # Check the passing condition
        return "Pass"  # Return Pass if marks are enough
    else:  # Handle marks below the passing score
        return "Fail"  # Return Fail if marks are low

print(check_pass_fail(85))  # Check result for one student
print(check_pass_fail(32))  # Check result for another student
```

**How the code works:**

- The decision logic is written once and reused for different marks.
- `return` sends the result back, so it can be stored or passed to another function later.
- This is the core mindset of functions: find repeated logic and give it a reusable name.

---

## Common Errors to Watch For

- **Forgetting parentheses:** `say_hello` only refers to the function; `say_hello()` actually calls it.
- **Indentation mistakes:** Indented lines belong to the function; non-indented lines run outside it.
- **Missing `return`:** A function without `return` gives back `None`, so the calculated value cannot be passed to another function.
- **Wrong argument order:** Arguments fill parameters by position, so the order must match.
- **Default before required:** A parameter with a default value must come after parameters without defaults.

Testing a function with normal, boundary, and unusual inputs builds confidence that it works correctly.

---

## Key Takeaways

- A **function** is a reusable block of code created with `def` and executed using a function call.
- **Parameters** receive input inside the function definition; **arguments** are the actual values passed during the call.
- **`return`** sends a result back so it can be stored, reused, or passed as input to another function.
- **Default parameter values** provide a backup when the caller does not pass that argument.
- **Function chaining** connects functions so one function's output becomes another function's input — step by step or nested.
- **Modular programming** divides a large program into small, clear functions, each with one responsibility.

In the next lesson, you will use these reusable blocks inside larger problem-solving patterns, making functions the base for cleaner, more professional Python programs.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| `def` | Keyword used to define a function | `def greet():` |
| Function call | Instruction to run a function | `greet()` |
| Parameter | Variable in the function definition | `def greet(name):` |
| Argument | Actual value passed during a call | `greet("Anita")` |
| `return` | Sends a result back from a function | `return total` |
| Local variable | Variable created inside a function | `discount = price * 0.10` |
| Default parameter | Backup value used if no argument is given | `rate_per_km=10` |
| Function composition | Output of one function used as input to another | `double(square(5))` |
| Nested function call | One function call placed inside another | `round_bill(add_gst(cost))` |
| Modular programming | Dividing code into small reusable functions | Separate total, percentage, result functions |
