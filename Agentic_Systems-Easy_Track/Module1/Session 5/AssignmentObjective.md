## Assignment 1: Objective Type Questions

Total: 15 Questions | Format: 7 MCQs + 8 MSQs/NATs

---

### 1.1 Easy

---

1. **(MCQ)**
   Which keyword is used in Python to execute a block of code only when a condition is true?
   A) for
   B) if
   C) while
   D) def

**Correct answer:** **B**

**Explanation:**
`if` checks a condition and executes the indented block only when the condition evaluates to `True`.

**Why others are incorrect:**

* `for` → used for loops
* `while` → loop based on condition repetition
* `def` → used to define functions

---

2. **(MCQ)**
   What is the data type of the result of the expression `5 > 3`?
   A) int
   B) str
   C) bool
   D) float

**Correct answer:** **C**

**Explanation:**
Comparison operators (`>`, `<`, `==`) always return a Boolean value (`True` or `False`).

---

3. **(MCQ)**
   Which of the following values evaluates to False?
   A) True
   B) 1
   C) 0
   D) "True"

**Correct answer:** **C**

**Explanation:**
In Python, `0` is considered falsy.

**Why others are incorrect:**

* `True` → truthy
* `1` → truthy
* `"True"` → non-empty string → truthy

---

4. **(MCQ)**
   Which operator checks for equality in Python?
   A) =
   B) !=
   C) ==
   D) <=

**Correct answer:** **C**

**Explanation:**
`==` compares two values for equality.
`=` is assignment, not comparison.

---

5. **(MCQ)**
   What does incorrect indentation in Python most commonly lead to?
   A) Logical warnings only
   B) Slower execution
   C) Syntax or runtime errors
   D) Automatic correction

**Correct answer:** **C**

**Explanation:**
Python uses indentation to define code blocks. Incorrect indentation often raises an `IndentationError` or changes program logic.

---

6. **(NAT)**
   What is the output of the following expression?

```
True and False
```

**Correct answer:** **False**

**Explanation:**
The `and` operator returns `True` only if **both** operands are `True`.

---

7. **(MSQ)**
   Which of the following are valid Boolean values in Python? *(Select all that apply)*
   A) True
   B) False
   C) "True"
   D) 1

**Correct answers:** **A, B**

**Explanation:**
Only `True` and `False` are Boolean literals in Python.

**Why others are incorrect:**

* `"True"` → string
* `1` → integer (truthy, but not Boolean)

---

## 1.2 Intermediate

---

8. **(MCQ)**
   What will be printed by the following code?

```python
x = 10

if x > 5:
    print("A")
else:
    print("B")
```

A) A
B) B
C) A B
D) Nothing

**Correct answer:** **A**

**Explanation:**
Since `x > 5` is `True`, the `if` block executes.

---

9. **(NAT)**
   Evaluate the expression:

```
not (5 > 3)
```

**Correct answer:** **False**

**Explanation:**
`5 > 3` is `True`; applying `not` reverses it to `False`.

---

10. **(MSQ)**
    Which statements about the `and` operator are true? *(Select all that apply)*
    A) It returns True only if both operands are True
    B) It returns True if at least one operand is True
    C) It is commonly used to enforce multiple conditions
    D) It can combine comparison expressions

**Correct answers:** **A, C, D**

**Explanation:**
`and` requires all conditions to be true and is commonly used to combine comparisons.

**Why B is incorrect:**
“At least one operand” describes the `or` operator.

---

11. **(NAT)**
    What is the output?

```python
x = 7

if x >= 5 and x <= 10:
    print("Inside")
else:
    print("Outside")
```

**Correct answer:** **Inside**

**Explanation:**
`x` satisfies both conditions, so the compound condition evaluates to `True`.

---

## 1.3 Hard

---

12. **(MSQ)**
    Which of the following conditions evaluate to True? *(Select all that apply)*
    A) True or False
    B) False and True
    C) not False
    D) not (True and True)

**Correct answers:** **A, C**

**Explanation:**

* `True or False` → True
* `not False` → True

**Why others are incorrect:**

* `False and True` → False
* `not (True and True)` → not True → False

---

13. **(NAT)**
    What will be printed?

```python
is_verified = True
is_blocked = False

if is_verified and not is_blocked:
    print("Allowed")
else:
    print("Denied")
```

**Correct answer:** **Allowed**

**Explanation:**
The user is verified and not blocked, so the condition passes.

---

14. **(MCQ)**
    Why does Python enforce indentation as part of its syntax?
    A) To reduce execution time
    B) To remove the need for comments
    C) To define program structure clearly
    D) To support object-oriented programming

**Correct answer:** **C**

**Explanation:**
Indentation replaces braces and clearly defines blocks, improving readability and reducing ambiguity.

---

15. **(NAT)**
    What error will this code raise?

```python
if True:
print("Hello")
```

**Correct answer:** **IndentationError**

**Explanation:**
The `print` statement is not indented under the `if` block, violating Python’s syntax rules.
