# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

Priya uses **PhonePe** every day to pay her college canteen bill. The app shows her balance, sends payment confirmations, and blocks wrong PIN attempts.

What is the **best description** of what makes all of this work behind the screen?

A. The phone hardware stores money physically inside the SIM card  
B. Step-by-step instructions written in code tell the computer exactly what to do for each action  
C. The internet automatically guesses what Priya wants without any instructions  
D. UPI apps work only because users type faster on the keyboard

**Correct Answer:** B

**Answer Explanation:**  
Programming means giving the computer **clear, step-by-step instructions**. Apps like PhonePe are built from code that handles payments, messages, and checks — the computer does not guess.

**Why other options are wrong:**  
- A: Digital payments are software logic, not physical cash in a SIM.  
- C: Computers follow instructions; they do not guess intent on their own.  
- D: Typing speed has nothing to do with how an app is built.

---

## Q2 (MCQ, Easy)

Amit writes his first Python program in an **online compiler** on his friend's laptop because he has not installed Python yet.

What is the **main advantage** of using an online compiler for a beginner on day one?

A. It permanently replaces the need to learn Python syntax  
B. He can write and run Python code in the browser without installing Python on the machine  
C. It automatically writes all programs for him so he never has to type code  
D. It converts Python programs into WhatsApp messages

**Correct Answer:** B

**Answer Explanation:**  
An **online compiler** is a web tool with a code editor and Run button. Beginners can start coding immediately without local installation.

**Why other options are wrong:**  
- A: You still must learn syntax and logic.  
- C: Online compilers execute code you write; they do not auto-generate full programs.  
- D: That is not what an online compiler does.

---

## Q3 (MCQ, Easy)

In a Python program, Rahul adds this line above his code:

```python
# Show today's menu to the customer
```

What happens when Python runs this line?

A. Python prints "Show today's menu to the customer" on the screen  
B. Python stops the program with an error  
C. Python ignores this line because it is a comment  
D. Python stores the text in a variable called `menu`

**Correct Answer:** C

**Answer Explanation:**  
Lines starting with `#` are **comments** — notes for humans. Python skips them during execution.

**Why other options are wrong:**  
- A: Only `print()` displays text; comments do not.  
- B: Comments are valid Python; they do not cause errors.  
- D: Comments are not variable assignments.

---

## Q4 (MCQ, Easy)

Neha creates these variables in Python:

```python
age = 19
city = "Pune"
```

Which statement is **correct** about `age` and `city`?

A. `age` stores text and `city` stores a whole number  
B. `age` stores a whole number (int) and `city` stores text (str)  
C. Both variables must be declared with `int` and `str` keywords in Python  
D. Python cannot store numbers and text in variables at the same time in one program

**Correct Answer:** B

**Answer Explanation:**  
`19` is a whole number (**int**). `"Pune"` in quotes is text (**str**). Python uses **dynamic typing** — you assign values directly without declaring types upfront.

**Why other options are wrong:**  
- A: The types are reversed.  
- C: Python does not require `int age = 19` style declarations.  
- D: One program can hold many variables of different types.

---

## Q5 (MCQ, Moderate)

Karan checks whether a student's marks equal the full score:

```python
marks = 78
```

Which line **correctly checks** if `marks` is equal to `100` without changing the value stored in `marks`?

A. `marks = 100`  
B. `marks == 100`  
C. `100 = marks`  
D. `marks === 100`

**Correct Answer:** B

**Answer Explanation:**  
`==` is the **comparison** operator — it checks equality and returns `True` or `False`. `=` is **assignment** and would overwrite `marks`.

**Why other options are wrong:**  
- A: `=` assigns 100 to `marks`; it does not compare.  
- C: Invalid syntax — you cannot assign to a literal on the left.  
- D: Python uses `==`, not `===`.

---

## Q6 (MCQ, Moderate)

Sneha runs this program:

```python
quantity = input("How many notebooks did you buy? ")
total = quantity + 2
print(total)
```

She types `5` at the prompt. The program crashes with a **TypeError**.

What is the **most likely fix**?

A. Change `print` to `Print`  
B. Convert the input to an integer before adding: `total = int(quantity) + 2`  
C. Remove the quotes from the `input()` message  
D. Replace `+` with `==`

**Correct Answer:** B

**Answer Explanation:**  
`input()` always returns a **string**. `"5" + 2` is invalid in Python. Use `int(quantity)` before arithmetic.

**Why other options are wrong:**  
- A: `Print` would cause a `NameError`, not fix the type issue.  
- C: The prompt message must stay in quotes.  
- D: `==` compares values; it does not add them.

---

## Q7 (MSQ, Moderate)

A coaching centre stores student records in Python variables:

```python
roll_number = 1042
percentage = 88.5
name = "Anita"
is_scholarship = True
```

Which statements about these variables are **correct**?

A. `roll_number` holds an integer value  
B. `percentage` holds a float value because it has a decimal point  
C. `name` holds a string value  
D. `is_scholarship` can be stored as `true` (lowercase) in standard Python

**Correct Answers:** A, B, C

**Answer Explanation:**  
`1042` is **int**, `88.5` is **float**, `"Anita"` is **str**, and `True` is **bool** with a capital **T**.

**Why other options are wrong:**  
- D: Boolean literals in Python are `True` and `False` with capital first letters; lowercase `true` causes a `NameError`.

---

## Q8 (MSQ, Moderate)

Vikram splits a ₹1,500 dinner bill among 3 friends using Python variables:

```python
total_bill = 1500
friends = 3
share = total_bill / friends
```

Which statements about **arithmetic operators** in this snippet are **correct**?

A. `/` divides `total_bill` by `friends`  
B. `share` will be `500.0` (a float result in Python 3)  
C. `%` would give the remainder if used as `1500 % 3`  
D. `**` is required to divide two numbers in Python

**Correct Answers:** A, B, C

**Answer Explanation:**  
`/` performs division. `1500 / 3` is `500.0`. `%` returns remainder (`1500 % 3` is `0`). `**` is for exponentiation, not division.

**Why other options are wrong:**  
- D: Division uses `/`, not `**`.

---

## Q9 (MSQ, Hard)

A library membership rule says: a member gets a discount only if they are **18 or older** **and** have **paid the annual fee**.

```python
age = 20
fee_paid = True
```

Which expressions evaluate to **True** for this member?

A. `age >= 18 and fee_paid`  
B. `age < 18 or fee_paid`  
C. `not (age < 18)`  
D. `age == 20 and not fee_paid`

**Correct Answers:** A, B, C

**Answer Explanation:**  
- A: `20 >= 18` is `True` and `fee_paid` is `True` → `True and True` → **True**.  
- B: `age < 18` is `False`, but `fee_paid` is `True` → `False or True` → **True**.  
- C: `not (20 < 18)` → `not False` → **True**.  
- D: `not fee_paid` is `False`, so the `and` chain is **False**.

**Why other options are wrong:**  
- D: Fee was paid (`True`), so `not fee_paid` makes the whole expression false.

---

## Q10 (MSQ, Hard)

Meera debugs this program meant to print the sum of two numbers from the user:

```python
v1 = input("Enter first number: ")
v2 = input("Enter second number: ")
total = v1 + v2
print("Total is", total)
```

She enters `10` and `20`. The output is `Total is 1020` instead of `Total is 30`.

Which changes would **correctly fix** the program? (Select all that apply.)

A. `v1 = int(input("Enter first number: "))` and `v2 = int(input("Enter second number: "))`  
B. `total = int(v1) + int(v2)` after the two `input()` lines  
C. `total = v1 + v2` with no other changes — Python will auto-convert strings to integers  
D. Replace `print("Total is", total)` with `# Total is` so Python adds numbers silently

**Correct Answers:** A, B

**Answer Explanation:**  
`input()` returns strings, so `"10" + "20"` concatenates to `"1020"`. Converting with `int()` before addition fixes the maths. Both A (convert at input) and B (convert before adding) work.

**Why other options are wrong:**  
- C: Python does **not** auto-convert strings to integers for `+` between two strings.  
- D: Commenting out `print` hides output and does not fix the calculation.
