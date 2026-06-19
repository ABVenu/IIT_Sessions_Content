# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A **school PE teacher** wants every student in a batch of 8 to hear the same warm-up instruction without typing `print("Stretch your arms")` eight separate times.

Which approach best uses a loop to repeat the message exactly 8 times?

A. Write eight separate `print("Stretch your arms")` lines  
B. Use a `for` loop with `range(8)` and put `print("Stretch your arms")` inside the loop body  
C. Use one `if` statement that prints the message when a variable equals 8  
D. Use `break` immediately after the first `print` so the message runs once

**Correct Answer:** B

**Answer Explanation:**  
A **`for` loop with `range(8)`** runs the indented body **8 times** — once per value in the range. That is the standard way to repeat an action a fixed number of times.

**Why other options are wrong:**  
- A: Copy-pasting eight lines works but is hard to maintain and is not using a loop.  
- C: A single `if` prints at most once; it does not repeat eight times.  
- D: `break` stops a loop early; it does not create repetition.

---

## Q2 (MCQ, Easy)

A **bank token display** needs to show token numbers starting from zero. A developer writes:

```python
for token in range(4):
    print(token)
```

Which numbers will be printed (each on its own line)?

A. `1`, `2`, `3`, `4`  
B. `0`, `1`, `2`, `3`  
C. `0`, `1`, `2`, `3`, `4`  
D. `1`, `2`, `3`

**Correct Answer:** B

**Answer Explanation:**  
**`range(4)`** generates integers from **0 up to 3** (it stops **before** 4). So the output is `0`, `1`, `2`, `3`.

**Why other options are wrong:**  
- A and D: `range(4)` does not start at 1.  
- C: The stop value 4 is **not included** in the sequence.

---

## Q3 (MCQ, Easy)

An **ATM simulation** uses this code, but the program never stops printing `1`:

```python
count = 1
while count <= 3:
    print(count)
```

What is the **most likely missing line** inside the loop body?

A. `break` before `print(count)`  
B. `count = count + 1` after `print(count)`  
C. Replace `while` with `for`  
D. Remove the colon after `count <= 3`

**Correct Answer:** B

**Answer Explanation:**  
Without updating `count`, it stays **1 forever**, so `count <= 3` remains **`True`** — an **infinite loop**. Adding **`count = count + 1`** lets the condition eventually become `False`.

**Why other options are wrong:**  
- A: `break` would exit after one print, not fix a stuck counter for a full 1–3 run.  
- C: A `for` loop could work, but the direct fix for this `while` bug is incrementing the counter.  
- D: Removing the colon causes a `SyntaxError`; it does not fix the logic.

---

## Q4 (MCQ, Easy)

A student migrating from C++ writes this inside a Python `while` loop:

```python
steps = steps + 1  # This line works
steps++             # This line causes an error
```

Which statement about Python counter updates is **correct**?

A. Python supports both `steps++` and `steps = steps + 1`  
B. Python only allows `steps++` inside `for` loops  
C. Python uses `steps = steps + 1` or `steps += 1`; it does not support `steps++`  
D. Python automatically increments every loop variable without any code

**Correct Answer:** C

**Answer Explanation:**  
Python has **no `++` or `--` operators**. You must write **`steps = steps + 1`** or the shorthand **`steps += 1`**.

**Why other options are wrong:**  
- A and B: `steps++` is invalid Python syntax everywhere.  
- D: `while` loops require **manual** counter updates; `for` with `range()` advances automatically but that is not the same as “every variable auto-increments.”

---

## Q5 (MCQ, Moderate)

A **fitness app** logs rep counts with this loop:

```python
for rep in range(1, 6):
    print(rep)
```

What is printed (each value on its own line)?

A. `1`, `2`, `3`, `4`, `5`, `6`  
B. `0`, `1`, `2`, `3`, `4`, `5`  
C. `1`, `2`, `3`, `4`, `5`  
D. `1`, `2`, `3`, `4`

**Correct Answer:** C

**Answer Explanation:**  
**`range(1, 6)`** starts at **1** and stops **before 6**, producing **1, 2, 3, 4, 5**.

**Why other options are wrong:**  
- A: 6 is excluded because `range` stops before the second argument.  
- B: The start value is 1, not 0.  
- D: 5 is included because the stop is 6, not 5.

---

## Q6 (MCQ, Moderate)

A **tiffin packing app** should print only **odd** ticket numbers from 1 to 10 and **skip** even numbers, but still finish checking all ten numbers.

Which keyword should sit inside the loop when an even number is detected?

A. `break` — stop the entire loop immediately  
B. `continue` — skip this round and move to the next number  
C. `else` — run when the loop condition fails  
D. `pass` — always required after every `if`

**Correct Answer:** B

**Answer Explanation:**  
**`continue`** skips the rest of the **current iteration** (e.g., skip `print`) and moves to the **next** value. The loop keeps running for remaining numbers.

**Why other options are wrong:**  
- A: `break` would stop after the first even number — you would not process all ten.  
- C: `else` on loops is a separate feature; it does not skip iterations.  
- D: `pass` is a no-op placeholder, not a skip mechanism.

---

## Q7 (MSQ, Moderate)

A **cricket scoring dashboard** uses different `range()` calls to list ball numbers.

Which statements about **`range()`** are **correct**?

A. `range(10)` produces 0, 1, 2, …, 9  
B. `range(1, 5)` includes the number 5 in its output  
C. `range(0, 10, 2)` produces 0, 2, 4, 6, 8  
D. `range(start, stop)` always stops **before** the `stop` value

**Correct Answers:** A, C, D

**Answer Explanation:**  
- A: One-argument `range(stop)` starts at 0 and ends at **stop − 1**.  
- C: Step 2 from 0 up to (but not including) 10 gives even numbers 0 through 8.  
- D: The upper bound is **exclusive** in two-argument form.  
- B is **false**: `range(1, 5)` gives **1, 2, 3, 4** — not 5.

**Why other options are wrong:**  
- B: Including 5 would require `range(1, 6)`.

---

## Q8 (MSQ, Moderate)

A **startup team** is choosing between `for` and `while` for two features: printing a fixed 10-row report, and retrying UPI payment until success.

Which statements about loop choice are **correct**?

A. Use `for` when you know how many times to repeat (e.g., 10 rows)  
B. Use `while` when repetition depends on a condition that may change (e.g., payment still failing)  
C. An ATM PIN retry until the correct PIN is entered fits a `while` loop naturally  
D. A `for` loop with `range()` requires you to manually write `i = i + 1` every round

**Correct Answers:** A, B, C

**Answer Explanation:**  
- A: Fixed counts map cleanly to **`for` + `range()`**.  
- B and C: **Repeat until condition changes** is the core `while` use case.  
- D is **false**: `for` over `range()` advances the loop variable automatically; manual increment is mainly a **`while`** concern.

**Why other options are wrong:**  
- D: Confuses `while` counter management with `for` over a sequence.

---

## Q9 (MSQ, Hard)

A developer wrote this **`while` loop** to print 1 through 5 but skip printing 3:

```python
num = 1
while num <= 5:
    if num == 3:
        continue
    print(num)
    num = num + 1
```

Which statements are **correct**?

A. When `num` is 3, `continue` runs before `num = num + 1`, so `num` stays 3 and the loop may never end  
B. `continue` skips the remaining lines in the current iteration, including `num = num + 1` when `num` is 3  
C. Updating `num` (e.g., `num = num + 1`) **before** the `if num == 3` check would prevent this infinite loop  
D. The program always prints `1`, `2`, `4`, `5` and terminates normally

**Correct Answers:** A, B, C

**Answer Explanation:**  
When **`num == 3`**, `continue` jumps to the next condition check **without** running `num = num + 1`, so **`num` remains 3** → infinite loop (A, B).  
Fix: increment **before** `continue`, or restructure so the counter always advances (C).  
D is **false** because the loop hangs at 3.

**Why other options are wrong:**  
- D: The program never reaches 4 and 5 because it never leaves 3.

---

## Q10 (MSQ, Hard)

A **class monitor** collects marks with this program:

```python
student_count = int(input("Enter number of students: "))
total_marks = 0

for i in range(student_count):
    marks = int(input("Enter marks: "))
    total_marks = total_marks + marks

average = total_marks / student_count
print("Class average:", average)
```

Which statements about this **accumulator pattern** are **correct**?

A. `total_marks` should be initialized to `0` before the loop starts  
B. `average` should be calculated **outside** the loop, after all marks are collected  
C. Moving `average = total_marks / student_count` **inside** the loop would still print only one final average with no side effects  
D. `student_count` is not modified inside the loop, so dividing by it at the end is safe

**Correct Answers:** A, B, D

**Answer Explanation:**  
- A: Accumulators start at **0** (or another neutral value) before adding in the loop.  
- B: The average needs the **final** total after all inputs — that happens **after** the loop.  
- D: `for i in range(student_count)` does not change `student_count` itself.  
- C is **false**: An average **inside** the loop recalculates and prints after **each** student, producing partial averages — not the same as one final result.

**Why other options are wrong:**  
- C: Inside the loop, output would change every iteration (e.g., after 1 student, after 2, …).
