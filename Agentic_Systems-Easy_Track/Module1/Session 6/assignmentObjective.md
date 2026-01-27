## Assignment 1: Objective Type Questions

### 1.1 Easy

---

1. **(MCQ)**
   What does the following code print?

```python
for i in range(3):
    print(i)
```

A) 1 2 3
B) 0 1 2
C) 0 1 2 3
D) Error

**Correct answer:** **B**

**Explanation:**
`range(3)` generates `0, 1, 2`. Each value is printed on a new line.

**Why others are incorrect:**

* A) starts from 1 → incorrect
* C) `3` is excluded in `range(3)`
* D) code is syntactically correct

---

2. **(MCQ)**
   Which function is commonly used to generate a sequence of numbers in a `for` loop?
   A) `list()`
   B) `seq()`
   C) `range()`
   D) `count()`

**Correct answer:** **C**

**Explanation:**
`range()` is designed specifically to generate sequences of numbers efficiently.

---

3. **(MCQ)**
   Which loop is best suited when the number of iterations is known in advance?
   A) `while`
   B) `if`
   C) `for`
   D) infinite loop

**Correct answer:** **C**

**Explanation:**
`for` loops are ideal when iteration count or iterable size is known.

---

4. **(MCQ)**
   What is the primary purpose of a `while` loop?
   A) Iterate over a list
   B) Repeat code while a condition remains true
   C) Replace `for` loops
   D) Stop program execution

**Correct answer:** **B**

**Explanation:**
A `while` loop keeps executing as long as its condition is `True`.

---

5. **(MCQ)**
   Which keyword immediately exits a loop?
   A) `stop`
   B) `exit`
   C) `break`
   D) `pass`

**Correct answer:** **C**

**Explanation:**
`break` terminates the loop instantly and transfers control outside it.

**Why others are incorrect:**

* `stop`, `exit` → not loop-control keywords
* `pass` → does nothing, loop continues

---

6. **(NAT)**
   How many times will `"Hello"` be printed?

```python
for i in range(2):
    print("Hello")
```

**Correct answer:** **2**

**Explanation:**
`range(2)` runs twice (`0` and `1`).

---

7. **(MSQ)**
   Which of the following are valid uses of a `for` loop in Python? *(Select all that apply)*
   A) Iterating over a list
   B) Iterating over a string
   C) Iterating over a range of numbers
   D) Iterating over a boolean

**Correct answers:** **A, B, C**

**Explanation:**
Lists, strings, and ranges are iterable.

**Why D is incorrect:**
A Boolean is not iterable.

---

### 1.2 Intermediate

---

8. **(NAT)**
   What is the output?

```python
for i in range(1, 5, 2):
    print(i)
```

**Correct answer:**

```
1
3
```

**Explanation:**
Starts at `1`, increments by `2`, stops before `5`.

---

9. **(MCQ)**
   What happens when the `continue` statement is executed inside a loop?
   A) The loop stops permanently
   B) The program crashes
   C) The current iteration ends and the next one begins
   D) The loop restarts from the beginning

**Correct answer:** **C**

**Explanation:**
`continue` skips the remaining code in the current iteration and moves to the next one.

---

10. **(MSQ)**
    Which statements about `while` loops are true? *(Select all that apply)*
    A) They may run infinitely if the condition never becomes false
    B) They are best used when the number of iterations is fixed
    C) They depend on a condition
    D) They require manual updates to the loop variable

**Correct answers:** **A, C, D**

**Explanation:**
`while` loops are condition-based and require explicit updates to avoid infinite loops.

**Why B is incorrect:**
Fixed iteration counts favor `for` loops.

---

11. **(NAT)**
    What is printed?

```python
x = 0
while x < 3:
    print(x)
    x += 1
```

**Correct answer:**

```
0
1
2
```

**Explanation:**
The loop runs while `x` is less than `3`, incrementing each time.

---

### 1.3 Hard

---

12. **(MSQ)**
    Which of the following will result in an infinite loop? *(Select all that apply)*

A)

```python
x = 0
while x < 5:
    print(x)
```

B)

```python
x = 0
while x < 5:
    x += 1
```

C)

```python
while True:
    break
```

D)

```python
while True:
    print("Run")
```

**Correct answers:** **A, D**

**Explanation:**

* A → `x` never changes
* D → condition always `True` with no exit

**Why others are incorrect:**

* B updates `x` correctly
* C breaks immediately

---

13. **(NAT)**
    What is the output?

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**Correct answer:**

```
0
1
2
```

**Explanation:**
The loop stops when `i` becomes `3`.

---

14. **(MCQ)**
    Why is indentation especially important in loops?
    A) It improves performance
    B) It defines which statements repeat
    C) It reduces memory usage
    D) It prevents runtime errors

**Correct answer:** **B**

**Explanation:**
Indentation tells Python exactly which lines belong inside the loop.

---

15. **(NAT)**
    How many times does `"Pass"` print?

```python
scores = [60, 40, 80]

for score in scores:
    if score < 50:
        continue
    print("Pass")
```

**Correct answer:** **2**

**Explanation:**

* `60` → Pass
* `40` → skipped
* `80` → Pass
