# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**Anita** writes a greeting function for her college club website:

```python
def welcome():
    print("Welcome to the Coding Club")

welcome
```

She runs the program but sees **no message** on the screen.

What is the most likely reason?

A. Python does not allow functions without parameters  
B. She referred to the function name without calling it  
C. The function must be called before it is defined  
D. `print()` cannot be used inside a function  

**Correct Answer:** B

**Answer Explanation:**  
Writing `welcome` only creates a reference to the function object. To run the function body, Python needs a **function call** with parentheses: `welcome()`.

**Why other options are wrong:**  
- A: Functions without parameters are valid in Python.  
- C: The function is defined before the reference line; the issue is missing `()`.  
- D: `print()` works normally inside functions.

---

## Q2 (MCQ, Easy)

A **food delivery app** asks for a delivery address when you place an order. In function terms, `"Flat 302, Pune"` is the actual value sent during the call, while `address` in `def deliver(address):` is the placeholder that receives it.

Which pair correctly matches the terms?

A. `"Flat 302, Pune"` is the parameter; `address` is the argument  
B. `address` is the parameter; `"Flat 302, Pune"` is the argument  
C. Both are parameters  
D. Both are arguments  

**Correct Answer:** B

**Answer Explanation:**  
A **parameter** is written in the function definition (`address`). An **argument** is the actual value passed during the function call (`"Flat 302, Pune"`).

**Why other options are wrong:**  
- A: The terms are reversed.  
- C and D: One belongs to the definition and the other to the call; they are not the same role.

---

## Q3 (MCQ, Easy)

**Ravi** wants to create a reusable block of code named `calculate_bill` so the same logic is not copied again and again in his program.

Which keyword should he use to define this block?

A. `call`  
B. `func`  
C. `def`  
D. `return`  

**Correct Answer:** C

**Answer Explanation:**  
In Python, the **`def`** keyword is used to define a user-defined function.

**Why other options are wrong:**  
- A: `call` is not a Python keyword for defining functions.  
- B: `func` is not used to define functions in Python.  
- D: `return` sends a value back from a function, but it does not create the function itself.

---

## Q4 (MCQ, Easy)

A **billing helper** must calculate a total and also use that total later for tax calculation in the same program.

Which approach is better for storing and reusing the calculated value?

A. Use only `print()` inside the function  
B. Use `return` to send the value back to the caller  
C. Define the function after calling it  
D. Pass the function name without parentheses  

**Correct Answer:** B

**Answer Explanation:**  
`print()` only displays output on screen. **`return`** sends the result back so it can be stored in a variable or passed to another function.

**Why other options are wrong:**  
- A: A printed value is not directly reusable as data in later calculations.  
- C: A function must be defined before it is called.  
- D: A name without `()` does not execute the function.

---

## Q5 (MCQ, Moderate)

A **wallet app** uses this function:

```python
def add_money(amount, bonus=0):
    return amount + bonus

result = add_money(500)
```

What will `result` contain?

A. `0`  
B. `500`  
C. `None`  
D. Python will raise an error because `bonus` was not passed  

**Correct Answer:** B

**Answer Explanation:**  
`bonus=0` is a **default parameter**. When only `500` is passed, `amount` becomes `500` and `bonus` uses its default value `0`, so the returned value is `500 + 0 = 500`.

**Why other options are wrong:**  
- A: `0` would happen only if `amount` were `0`.  
- C: The function explicitly returns a number, not `None`.  
- D: Missing arguments are allowed when a default value exists.

---

## Q6 (MCQ, Moderate)

A **quiz app** uses this code:

```python
def add_numbers(a, b):
    return a + b

n = add_numbers(1, 2)
sum_of_natural = n * (n + 1) // 2
print("Sum of first", n, "natural numbers:", sum_of_natural)
```

What will be printed?

A. `Sum of first 1 natural numbers: 1`  
B. `Sum of first 2 natural numbers: 3`  
C. `Sum of first 3 natural numbers: 6`  
D. `Sum of first 3 natural numbers: 9`  

**Correct Answer:** C

**Answer Explanation:**  
`add_numbers(1, 2)` returns `3`, so `n = 3`. Then `sum_of_natural = 3 * (3 + 1) // 2 = 12 // 2 = 6`. The printed line is `Sum of first 3 natural numbers: 6`.

**Why other options are wrong:**  
- A and B: They use the wrong value of `n`.  
- D: `9` would come from a different formula or wrong `n`.

---

## Q7 (MSQ, Moderate)

A **parcel booking desk** uses positional arguments when staff enter package details in a fixed order.

```python
def book_parcel(weight_kg, destination):
    return weight_kg, destination

book_parcel(2, "Delhi")
```

Which statements are correct?

A. `weight_kg` and `destination` are parameters  
B. `2` and `"Delhi"` are arguments  
C. Arguments are matched to parameters by position  
D. `book_parcel("Delhi")` will work correctly for a 2 kg parcel  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Parameters appear in the function definition, arguments are the actual values passed during the call, and multiple arguments are matched **by position** — first to first, second to second.

**Why other options are wrong:**  
- D: The function needs two positional arguments. Passing only one causes a missing-argument error.

---

## Q8 (MSQ, Moderate)

A **student marks helper** compares two ways of sharing results:

```python
def show_total(a, b):
    print(a + b)

def get_total(a, b):
    return a + b
```

Which statements are correct?

A. `show_total(4, 5)` displays `9` on screen  
B. `x = get_total(4, 5)` stores `9` in `x`  
C. `y = show_total(4, 5)` stores `9` in `y`  
D. A returned value can be passed directly into another function call  

**Correct Answers:** A, B, D

**Answer Explanation:**  
`print()` displays output, while `return` gives a value back to the caller. Because `get_total` returns `9`, it can be stored or passed onward. `show_total` prints but does not return the sum.

**Why other options are wrong:**  
- C: `show_total` has no `return`, so `y` becomes `None`, not `9`.

---

## Q9 (MSQ, Hard)

A **startup team** refactors a long billing script into smaller reusable functions so each function has one clear job and repeated price logic is written only once.

Which statements about this modular approach are correct?

A. It follows the DRY principle by avoiding repeated code  
B. The output of one function can become the input of another function  
C. A function should ideally perform one clear task  
D. Modular programming means all logic must stay in one large block  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Modular programming splits work into smaller reusable functions. **DRY** means writing logic once and reusing it. Function chaining uses one function's return value as another function's argument. Good modular design gives each function one responsibility.

**Why other options are wrong:**  
- D: Modular programming is the opposite of keeping everything in one large block.

---

## Q10 (MSQ, Hard)

A **shop billing program** uses these functions:

```python
def multiply(a, b=2):
    return a * b

def add_tax(amount, rate=0.10):
    return amount + amount * rate

x = multiply(5)
y = multiply(3, 4)
bill = add_tax(add_tax(x))
```

Which statements are correct?

A. `x` is `10`  
B. `y` is `12`  
C. Calling `multiply()` with no arguments will raise an error  
D. `bill` is `11`  

**Correct Answers:** A, B, C

**Answer Explanation:**  
- `multiply(5)` uses default `b=2`, so `x = 10`.  
- `multiply(3, 4)` returns `12`, so `y = 12`.  
- `multiply()` fails because required parameter `a` is missing.  
- `add_tax(10)` returns `11`, then `add_tax(11)` returns `12.1`, so `bill` is `12.1`, not `11`.

**Why other options are wrong:**  
- D: `bill` is `12.1` after tax is applied twice with the default rate.

---
