# Assignment — Objective (Introduction to Programming, Python Basics & Development Environment Setup)

**Instructions:** Answer all questions. For multiple-select questions (MSQ), select **all** options that apply.

**Scope:** This quiz covers Session 1 fundamentals: **Python installation**; **VS Code and terminal setup**; **writing and executing Python scripts**; **variables**; **data types** (int, float, str, bool); **arithmetic operators** (`+`, `-`, `*`, `/`, `//`, `%`, `**`); and **comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`).

---

## Section A — Multiple Choice, Single Correct (MCQ)

### Q1 (Easy)

Ananya just installed Python on her laptop. She opens VS Code, creates a file called `hello.py`, types `print("Hello, World!")`, saves the file, and then runs it from the terminal by typing `python hello.py`. The message `Hello, World!` appears on the screen. What role did the **terminal** play in this workflow?

- A) It compiled the `.py` file into machine code before running it
- B) It acted as a text editor where she typed her Python code
- C) It executed a command that told the Python interpreter to run the script
- D) It automatically checked the code for errors before execution

**Answer Explanation (for Assess):**
**Correct answer: C.** The terminal is a command-line interface used to issue system commands. When Ananya typed `python hello.py`, she instructed the operating system to invoke the Python **interpreter** and pass the script to it. The interpreter then executed the code line by line.
**A** is wrong: Python is an interpreted language, not compiled. **B** is wrong: VS Code, not the terminal, is the text editor. **D** is wrong: the terminal does not automatically check Python syntax; that is the interpreter's job at runtime.

---

### Q2 (Easy)

A student writes the following line in Python:

```python
age = 20
```

What is the correct technical term for `age` in this statement?

- A) A keyword
- B) A variable
- C) A function
- D) A data type

**Answer Explanation (for Assess):**
**Correct answer: B.** `age` is a **variable** — a named storage location that holds a value. Here it stores the integer `20`.
**A** is wrong: keywords are reserved words like `if`, `for`, `while` that have special meaning in Python; user-defined names are not keywords. **C** is wrong: a function is a reusable block of code called with parentheses, e.g., `print()`. **D** is wrong: the data type of `age` is `int`, but `age` itself is not a data type — it is the variable name.

---

### Q3 (Easy)

Rahul runs the following code:

```python
x = 10
y = 3
print(x // y)
```

What is the output?

- A) 3.33
- B) 3
- C) 1
- D) 0

**Answer Explanation (for Assess):**
**Correct answer: B.** The `//` operator performs **floor division** — it divides and rounds the result down to the nearest whole number. `10 / 3 = 3.33...`, and floor division discards the decimal, giving `3`.
**A** is the result of regular division (`/`), not floor division. **C** would be the remainder (`%`), not the quotient. **D** is incorrect altogether.

---

### Q4 (Easy)

Which of the following is a valid Python variable name?

- A) `2score`
- B) `my-score`
- C) `my_score`
- D) `class`

**Answer Explanation (for Assess):**
**Correct answer: C.** `my_score` is valid — Python variable names can contain letters, digits, and underscores, but must **not** start with a digit or contain hyphens, and must not be reserved keywords.
**A** is wrong: variable names cannot start with a digit. **B** is wrong: hyphens (`-`) are not allowed; Python treats them as the subtraction operator. **D** is wrong: `class` is a reserved keyword in Python.

---

### Q5 (Easy)

What will the following code print?

```python
a = 7
b = 2
print(a % b)
```

- A) 3
- B) 3.5
- C) 1
- D) 0

**Answer Explanation (for Assess):**
**Correct answer: C.** The `%` operator returns the **remainder** after division. `7 ÷ 2 = 3` with a remainder of `1`, so `7 % 2 = 1`.
**A** is the quotient, not the remainder. **B** is the result of `7 / 2`. **D** would mean 7 is evenly divisible by 2, which it is not.

---

### Q6 (Easy)

A student writes:

```python
is_raining = True
temperature = 28.5
city = "Delhi"
visitors = 1200
```

Which variable holds a **float** value?

- A) `is_raining`
- B) `temperature`
- C) `city`
- D) `visitors`

**Answer Explanation (for Assess):**
**Correct answer: B.** `temperature = 28.5` stores a decimal number, which is a **float** in Python.
**A** holds a `bool` (`True`/`False`). **C** holds a `str` (a string enclosed in quotes). **D** holds an `int` (a whole number without a decimal point).

---

### Q7 (Moderate)

Priya writes the following code:

```python
x = 5
y = 2
result = x ** y
print(result)
```

What is the output and which operator is responsible?

- A) `10` — the multiplication operator
- B) `25` — the exponentiation operator
- C) `7` — the addition operator
- D) `2` — the floor division operator

**Answer Explanation (for Assess):**
**Correct answer: B.** The `**` operator is Python's **exponentiation** (power) operator. `5 ** 2` means 5 raised to the power of 2, which equals `25`.
**A** is wrong: multiplication would use `*` and give `10`. **C** is wrong: addition would give `7`. **D** is wrong: floor division would give `2`, but the operator used is `**`, not `//`.

---

### Q8 (Moderate)

What does the following comparison expression evaluate to?

```python
10 == "10"
```

- A) `True`, because both hold the value 10
- B) `False`, because Python compares both value and data type for `==`
- C) `True`, because Python automatically converts the string to an integer
- D) An error is raised because you cannot compare an `int` and a `str`

**Answer Explanation (for Assess):**
**Correct answer: B.** In Python, `==` checks both **value** and **type**. The integer `10` and the string `"10"` are different types, so the result is `False`. Python does **not** automatically convert types for `==`.
**A** is wrong: they look the same but are different types. **C** is wrong: Python does not implicitly cast types during comparison. **D** is wrong: Python does not raise an error here — it simply returns `False`.

---

### Q9 (Moderate)

A developer writes:

```python
marks = 85
passing_marks = 40
print(marks >= passing_marks)
```

What is the output?

- A) `85`
- B) `False`
- C) `True`
- D) `45`

**Answer Explanation (for Assess):**
**Correct answer: C.** The `>=` (greater than or equal to) operator compares `85` and `40`. Since `85` is greater than `40`, the expression evaluates to `True`.
**A** is wrong: comparison operators never return the numeric value itself; they return a boolean. **B** is wrong: `85 >= 40` is a true statement. **D** is wrong: subtraction was not performed here.

---

### Q10 (Moderate)

Vikram evaluates the expression:

```python
result = 2 + 3 * 4 - 1
print(result)
```

What is printed?

- A) `19`
- B) `13`
- C) `20`
- D) `11`

**Answer Explanation (for Assess):**
**Correct answer: B.** Python follows standard **operator precedence** (BODMAS/PEMDAS). Multiplication is evaluated before addition and subtraction: `3 * 4 = 12`, then `2 + 12 - 1 = 13`.
**A** would be the result if evaluated strictly left-to-right without precedence: `(2+3)*4-1 = 19`. **C** and **D** are incorrect arithmetic results.

---

## Section B — Multiple Select, Multiple Correct (MSQ)

*Select all correct options.*

### Q11 (Moderate — MSQ)

Which of the following are valid Python data types for the values shown?

- A) `x = 42` → `int`
- B) `x = 3.14` → `float`
- C) `x = "hello"` → `str`
- D) `x = True` → `str`
- E) `x = False` → `bool`

**Answer Explanation (for Assess):**
**Correct answers: A, B, C, E.**
`42` is an **int**; `3.14` is a **float**; `"hello"` is a **str**; `False` is a **bool**.
**D** is wrong: `True` is a **bool**, not a `str`. A string would require quotes, e.g., `"True"`.

---

### Q12 (Moderate — MSQ)

A student is exploring the difference between `/` and `//` in Python. Which statements are **correct**?

- A) `7 / 2` returns `3.5` — a float result
- B) `7 // 2` returns `3` — the quotient with the decimal discarded
- C) `7 / 2` returns `3` — Python automatically rounds down for `/`
- D) `7 // 2` returns `3.0` when at least one operand is a float, e.g., `7.0 // 2`
- E) Both `/` and `//` always return the same result

**Answer Explanation (for Assess):**
**Correct answers: A, B, D.**
`/` always returns a float in Python 3 (`3.5`). `//` performs floor division returning an `int` when both operands are integers (`3`), but returns a `float` if at least one operand is a float (`7.0 // 2 = 3.0`).
**C** is wrong: `/` does not round down; use `//` for that. **E** is wrong: they differ whenever division is not exact.

---

### Q13 (Moderate — MSQ)

Sunita is naming variables in her program. Which of the following names are **valid** Python variable names?

- A) `_score`
- B) `total_marks`
- C) `3rd_place`
- D) `class`
- E) `studentAge`

**Answer Explanation (for Assess):**
**Correct answers: A, B, E.**
`_score` (starts with underscore — allowed), `total_marks` (letters and underscores — allowed), and `studentAge` (camelCase — allowed) are all valid.
**C** is wrong: variable names cannot start with a digit. **D** is wrong: `class` is a Python reserved keyword and cannot be used as a variable name.

---

### Q14 (Hard — MSQ)

A teacher asks her class to predict the output of the following code:

```python
a = 10
b = 4
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a != b)
```

Which of the following output predictions are **correct**?

- A) `a / b` → `2.5`
- B) `a // b` → `2`
- C) `a % b` → `4`
- D) `a ** b` → `10000`
- E) `a != b` → `True`

**Answer Explanation (for Assess):**
**Correct answers: A, B, D, E.**
`10 / 4 = 2.5` (float division). `10 // 4 = 2` (floor division). `10 ** 4 = 10,000`. `10 != 4` is `True` because the values are not equal.
**C** is wrong: `10 % 4 = 2` (remainder of 10 ÷ 4), not `4`.

---

### Q15 (Hard — MSQ)

A developer reviews the following code and wants to know which statements about it are **true**:

```python
price = 199.99
quantity = 3
discount = 10
total = price * quantity
final_price = total - discount
print(final_price > 500)
print(final_price == 589.97)
```

- A) `price` is of type `float`
- B) `quantity` is of type `int`
- C) `total` evaluates to `599.97`
- D) `final_price > 500` prints `True`
- E) `final_price == 589.97` prints `False` due to floating-point precision issues in Python

**Answer Explanation (for Assess):**
**Correct answers: A, B, C, D.**
`price = 199.99` is a `float`; `quantity = 3` is an `int`. `199.99 * 3 = 599.97`, so `total = 599.97`. `final_price = 599.97 - 10 = 589.97`, and `589.97 > 500` is `True`.
**E** is wrong: in this particular case, Python's floating-point representation of `199.99 * 3 - 10` produces exactly `589.97`, so `final_price == 589.97` actually prints `True`, not `False`. While floating-point precision issues are a real concern in Python, they do not affect every calculation — this expression happens to be represented exactly.

---

*End of objective assignment.*
