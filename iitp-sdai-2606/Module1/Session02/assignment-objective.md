# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

An **AC remote app** checks the room temperature before switching the compressor on. The line `temperature == 30` is evaluated when the actual temperature stored in the variable is `30`.

What will Python evaluate this comparison as?

A. `True`  
B. `False`  
C. `30`  
D. A `TypeError` because numbers cannot be compared

**Correct Answer:** A

**Answer Explanation:**  
The `==` operator checks whether two values are **equal**. Since `30 == 30`, the expression evaluates to the boolean **`True`**.

**Why other options are wrong:**  
- B: The values match, so the result is not `False`.  
- C: Comparisons return booleans (`True`/`False`), not the number itself.  
- D: Comparing two integers with `==` is valid Python.

---

## Q2 (MCQ, Easy)

A **UPI payment app** runs this check before allowing a transfer:

```python
if account_balance > 500:
    print("Payment allowed")
```

The customer's balance is **₹200**, so the condition is `False`.

What happens to the indented `print("Payment allowed")` line?

A. Python runs it twice to double-check the balance  
B. Python skips that indented block and continues with code after the `if`  
C. Python stops the entire program with a `SyntaxError`  
D. Python automatically changes the balance to ₹600

**Correct Answer:** B

**Answer Explanation:**  
When an `if` condition is **`False`**, Python **does not execute** the indented block under it. Lines after the block still run normally.

**Why other options are wrong:**  
- A: Python never re-runs a block automatically.  
- C: A false condition is normal behaviour, not a syntax error.  
- D: Conditionals do not modify variable values on their own.

---

## Q3 (MCQ, Easy)

At a **railway station kiosk**, a program decides which platform message to show:

```python
if ticket_platform == 3:
    print("Walk left to Platform 3")
else:
    print("Walk right to other platforms")
```

The ticket is for **Platform 5**, so the `if` condition is `False`.

What is the role of the `else` block here?

A. It runs only when the `if` condition is `True`  
B. It runs when the `if` condition is `False`  
C. It checks a second condition before the `if` runs  
D. It runs at the same time as the `if` block

**Correct Answer:** B

**Answer Explanation:**  
`else` means **"otherwise."** It executes when the matching `if` condition evaluated to **`False`**.

**Why other options are wrong:**  
- A: That describes the `if` block, not `else`.  
- C: A second condition uses `elif`, not `else`.  
- D: Exactly **one** branch in an `if`/`else` pair runs — never both.

---

## Q4 (MCQ, Easy)

A student writes this line while building an **exam result checker**:

```python
if marks = 50:
    print("Exactly fifty")
```

What will happen when Python tries to run this program?

A. It compares `marks` with `50` and prints the message when they match  
B. It assigns `50` to `marks` and then prints the message every time  
C. It raises a `SyntaxError` because `=` cannot be used for comparison inside `if`  
D. It prints `Exactly fifty` only when `marks` is not equal to `50`

**Correct Answer:** C

**Answer Explanation:**  
Inside a condition you must use **`==`** to compare. **`=`** is for **assignment**, and Python does not allow a plain assignment expression as an `if` condition — this causes a **`SyntaxError`**.

**Why other options are wrong:**  
- A: `=` assigns; it does not compare.  
- B: Even assignment inside `if` is invalid syntax here.  
- D: The program fails before any message can print.

---

## Q5 (MCQ, Moderate)

A **school grade portal** uses this logic for maths marks:

```python
math_marks = 85
if math_marks > 90:
    print("Grade A")
elif math_marks >= 80:
    print("Grade B")
elif math_marks >= 70:
    print("Grade C")
else:
    print("Grade F")
```

What will the program print for `math_marks = 85`?

A. `Grade A`  
B. `Grade B`  
C. `Grade C`  
D. `Grade F`

**Correct Answer:** B

**Answer Explanation:**  
Python checks conditions **top to bottom** and stops at the first match.  
- `85 > 90` → `False`  
- `85 >= 80` → `True` → prints **`Grade B`**  
Remaining `elif`/`else` blocks are skipped.

**Why other options are wrong:**  
- A: 85 is not above 90.  
- C: The `>= 80` branch matches first, so `Grade C` never runs.  
- D: 85 is well above the fail threshold.

---

## Q6 (MCQ, Moderate)

An **ATM PIN checker** uses this code:

```python
age = input("Enter your age: ")
if age > 18:
    print("You can open a savings account")
```

The user types `20`, but the program crashes with a **`TypeError`**.

What is the **best fix**?

A. Remove the colon after `if age > 18`  
B. Change `>` to `==`  
C. Convert the input to an integer: `age = int(input("Enter your age: "))`  
D. Replace `print` with `Print`

**Correct Answer:** C

**Answer Explanation:**  
`input()` always returns a **string**. Comparing `"20" > 18` mixes text and number, causing a **`TypeError`**. Wrap the input with **`int()`** before comparing.

**Why other options are wrong:**  
- A: Removing the colon creates a different syntax error.  
- B: `==` checks equality; it does not fix the string-vs-int problem.  
- D: `Print` is undefined and would cause a `NameError`.

---

## Q7 (MSQ, Moderate)

A **scholarship desk** stores a student's marks in `score = 55` and checks eligibility bands.

Which of the following expressions evaluate to **`True`**?

A. `score > 50 and score < 60`  
B. `score == 55 or score == 100`  
C. `not (score > 60)`  
D. `score > 60 and score < 70`

**Correct Answers:** A, B, C

**Answer Explanation:**  
With `score = 55`:  
- A: `55 > 50` is `True` and `55 < 60` is `True` → **`True`**.  
- B: `55 == 55` is `True` → **`True or False`** → **`True`**.  
- C: `55 > 60` is `False`; `not False` → **`True`**.  
- D: `55 > 60` is `False`, so the whole `and` chain is **`False`**.

**Why other options are wrong:**  
- D: 55 is not greater than 60, so this band check fails.

---

## Q8 (MSQ, Moderate)

A team is reviewing how **`if` / `elif` / `else`** chains work in a **food-delivery discount engine**.

Which statements about these chains are **correct**?

A. Python evaluates conditions from top to bottom and stops at the first `True` match  
B. Exactly one block in a properly built `if` / `elif` / `else` chain runs per execution  
C. An `else` block is **mandatory** after every `if` statement  
D. An `elif` block is checked only when all previous conditions in the chain were `False`

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: Order matters — first matching branch wins.  
- B: Mutual exclusivity is the point of `elif` chains.  
- D: Each `elif` is a fallback after earlier failures.  
- C is incorrect: `else` is **optional**; an `if` alone is valid.

**Why other options are wrong:**  
- C: Many programs use only `if`, or `if`/`elif` without `else`.

---

## Q9 (MSQ, Hard)

A **learning portal** validates login with stored credentials:

```python
username = "Masai"
password = "Masai123"

uname = "masai"       # user typed lowercase
pwd = "Masai123"      # user typed correct password
```

The program uses this chain:

```python
if uname == username and pwd == password:
    print("Logged in successfully")
elif uname != username and pwd != password:
    print("Username and password both are incorrect")
elif uname != username:
    print("Username is incorrect")
elif pwd != password:
    print("Password is not correct")
```

Which statements are **correct** for this input?

A. `uname == username` evaluates to `False` because Python string comparison is case-sensitive  
B. `pwd == password` evaluates to `True`  
C. The first `if` block runs and prints `"Logged in successfully"`  
D. The program prints `"Username is incorrect"` because the username alone does not match

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: `"masai"` and `"Masai"` differ in case → **`False`**.  
- B: `"Masai123" == "Masai123"` → **`True`**.  
- First `if`: `False and True` → **`False`**.  
- Second `elif`: `True and False` → **`False`**.  
- Third `elif`: `uname != username` → **`True`** → prints **`Username is incorrect`**.

**Why other options are wrong:**  
- C: Username mismatch prevents successful login even though the password is correct.

---

## Q10 (MSQ, Hard)

A developer wrote this **grade calculator**, but the conditions are in the wrong order:

```python
math_marks = int(input("Enter the marks: "))
if math_marks >= 70:
    print("Grade C")
elif math_marks >= 80:
    print("Grade B")
elif math_marks > 90:
    print("Grade A")
else:
    print("Grade F")
```

Which statements are **true** about this code?

A. For `math_marks = 85`, the program prints `Grade C`  
B. For `math_marks = 95`, the program prints `Grade C`  
C. Putting `> 90` first, then `>= 80`, then `>= 70` would assign grades correctly  
D. Both `Grade B` and `Grade A` can print in a single run for the same input

**Correct Answers:** A, B, C

**Answer Explanation:**  
Because `>= 70` is checked first, any mark from 70 upward matches the first branch:  
- 85 → **`Grade C`** (A is true).  
- 95 → **`Grade C`** as well (B is true) — the higher bands are never reached.  
- C: Strictest/highest thresholds must come **first** in the chain.  
- D: Only **one** block runs per chain execution.

**Why other options are wrong:**  
- D: Python stops after the first matching branch; multiple grades cannot print.
