# Assignment 1: Objective Type Questions

---

**(MCQ)** What is the purpose of defining a function in Python?
A) To execute code immediately
B) To store data permanently
C) To group reusable logic under a name
D) To improve execution speed

**Correct answer:** C

**Explanation:**
A function allows you to encapsulate a block of logic, give it a meaningful name, and reuse it multiple times. Defining a function does not execute it; it only prepares the logic for reuse. This is essential for writing modular, maintainable programs.

---

**(MCQ)** What happens when a function is defined using `def` but never called?
A) The function runs once automatically
B) The function runs every time the file is executed
C) The function is stored but never executed
D) Python throws an error

**Correct answer:** C

**Explanation:**
Defining a function only tells Python *how* to execute the logic if it is called. If the function is never called, its body is never executed. This separation between definition and execution enables reuse.

---

**(MCQ)** In the following code, what is `name`?

```python
def greet(name):
    print(f"Hello, {name}")
```

A) Argument
B) Parameter
C) Return value
D) Function call

**Correct answer:** B

**Explanation:**
`name` appears in the function definition, so it is a **parameter**. Parameters act as placeholders that receive values (arguments) when the function is called.

---

**(MCQ)** In the function call `greet("Alice")`, what is `"Alice"`?
A) Parameter
B) Function body
C) Argument
D) Return value

**Correct answer:** C

**Explanation:**
Arguments are the actual values passed into a function when it is called. `"Alice"` is passed into the parameter `name`.

---

**(MCQ)** What is the key difference between `print()` and `return` inside a function?
A) `print()` stores values, `return` displays them
B) `print()` sends values back to the caller, `return` does not
C) `print()` outputs to the screen, `return` sends a value back to the caller
D) There is no difference

**Correct answer:** C

**Explanation:**
`print()` is used for displaying information to the user, while `return` passes data back to the part of the program that called the function. Returned values can be reused, stored, or passed to other functions, which is critical in pipelines.

---

**(MCQ)** What does the following function return?

```python
def add(a, b):
    print(a + b)
```

A) The sum of `a` and `b`
B) `None`
C) A tuple
D) An error

**Correct answer:** B

**Explanation:**
If a function does not explicitly use `return`, Python automatically returns `None`, even if the function prints something to the screen.

---

**(MCQ)** What happens when a `return` statement is executed inside a function?
A) The program stops completely
B) The loop inside the function restarts
C) The function exits immediately and sends a value back
D) The function continues executing remaining lines

**Correct answer:** C

**Explanation:**
When Python encounters `return`, it immediately exits the function and returns control (and optionally a value) to the caller. Any code after `return` inside the function is skipped.

---

**(MCQ)** What is returned by the following function call?

```python
def stats(values):
    return len(values), sum(values)

result = stats([1, 2, 3])
```

A) `6`
B) `3`
C) `(3, 6)`
D) `[3, 6]`

**Correct answer:** C

**Explanation:**
Returning multiple values in Python creates a tuple. Here, `len(values)` is `3` and `sum(values)` is `6`, so the function returns `(3, 6)`.
