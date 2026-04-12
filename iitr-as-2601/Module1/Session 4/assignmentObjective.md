# Assignment: Python Fundamentals for AI

1. **(MCQ)**
   What is the output of the following code?

```python
x = 5
print(type(x))
```

A) `<class 'float'>`
B) `<class 'str'>`
C) `<class 'int'>`
D) `<class 'bool'>`

✅ **Correct answer:** C
**Explanation:** `5` is a whole number, so Python treats it as an integer (`int`).

---

2. **(MCQ)**
   Which of the following is a valid Python variable name?
   A) `2value`
   B) `value_2`
   C) `value-2`
   D) `value 2`

✅ **Correct answer:** B
**Explanation:** Variable names can include letters, numbers, and underscores, but cannot start with a number or contain spaces or hyphens.

---

3. **(MCQ)**
   What does the `input()` function always return?
   A) Integer
   B) Float
   C) Boolean
   D) String

✅ **Correct answer:** D
**Explanation:** `input()` always returns user input as a string, even if the user types a number.

---

4. **(MCQ)**
   Which operator is used for exponentiation in Python?
   A) `^`
   B) `**`
   C) `exp()`
   D) `pow`

✅ **Correct answer:** B
**Explanation:** `**` is the exponentiation operator (e.g., `2 ** 3 = 8`).

---

5. **(MCQ)**
   Which data type is used to represent `True` or `False`?
   A) `int`
   B) `str`
   C) `bool`
   D) `float`

✅ **Correct answer:** C
**Explanation:** Boolean values (`True`, `False`) are of type `bool`.

---

6. **(NAT)**
   What is the output?

```python
print(10 // 3)
```

✅ **Correct answer:** `3`
**Explanation:** `//` performs floor division, returning the integer part of the division.

---

7. **(MSQ)**
   Which of the following are valid string definitions in Python? *(Select all)*
   A) `"AI"`
   B) `'AI'`
   C) `AI`
   D) `"A" + "I"`

✅ **Correct answers:** A, B, D
**Explanation:** Strings must be inside quotes. `"A" + "I"` is valid string concatenation. `AI` without quotes is treated as a variable name.

---

### 1.2 Intermediate (4 Questions — Application & Logic)

8. **(MCQ)**
   What will be the output?

```python
x = "10"
y = 5
print(x + str(y))
```

A) 15
B) `"105"`
C) Error
D) `"15"`

✅ **Correct answer:** B
**Explanation:** Both values are strings, so Python concatenates them instead of adding numerically.

---

9. **(NAT)**
   What is the value of `result`?

```python
result = (2 + 3) * 4 ** 2
```

✅ **Correct answer:** `80`
**Explanation:** `(2 + 3) = 5`, `4 ** 2 = 16`, and `5 * 16 = 80`.

---

10. **(MSQ)**
    Which statements about Python variables are true? *(Select all)*
    A) Variables store values directly
    B) Variables are references to objects
    C) Variable types are fixed at declaration
    D) A variable can point to different types over time

✅ **Correct answers:** B, D
**Explanation:** Python variables reference objects, and the same variable can point to different data types over time.

---

11. **(NAT)**
    What is printed?

```python
accuracy = 0.873
print(f"Accuracy is {accuracy}")
```

✅ **Correct answer:** `Accuracy is 0.873`
**Explanation:** f-strings insert variable values directly into the string.

---

### 1.3 Hard (4 Questions — Edge Cases & Deeper Understanding)

12. **(MSQ)**
    Which of the following will raise a `TypeError`? *(Select all)*
    A) `"5" + 5`
    B) `int("5") + 5`
    C) `"AI" * 3`
    D) `"AI" - "A"`

✅ **Correct answers:** A, D
**Explanation:** Python does not allow adding or subtracting incompatible types like strings and integers, or subtracting strings.

---

13. **(NAT)**
    What is the output?

```python
x = True
print(x + 1)
```

✅ **Correct answer:** `2`
**Explanation:** In Python, `True` behaves like `1` in arithmetic operations.

---

14. **(MCQ)**
    Why is Python often called a “glue language” in AI?
    A) It replaces low-level languages
    B) It connects data, models, and systems
    C) It is the fastest language
    D) It enforces strict typing

✅ **Correct answer:** B
**Explanation:** Python integrates different tools, libraries, and systems used across the AI pipeline.

---

15. **(NAT)**
    What is the type of the following expression?

```python
type(input("Enter value: "))
```

✅ **Correct answer:** `<class 'str'>`
**Explanation:** `input()` always returns a string, regardless of what the user enters.
