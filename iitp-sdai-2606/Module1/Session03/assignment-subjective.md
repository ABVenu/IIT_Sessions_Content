# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Neha** is the class monitor for Section B. After the weekly English test, she must share a quick summary with her teacher: **total marks**, **class average**, and **how many students passed** (marks **40 or above**). Entering marks one by one is fine — she wants a small Python program that does the counting automatically instead of using a calculator.

### Problem Statement

Write a Python program that:

1. Asks the user: **`Enter number of students: `** and stores the value as an integer in a variable (use `int()`).
2. Initializes **`total_marks = 0`** and **`pass_count = 0`** before the loop.
3. Uses a **`for` loop** with **`range()`** to run exactly that many times — once per student.
4. Inside each round of the loop:
   - Asks **`Enter marks: `** and stores the marks as an integer (use `int()`).
   - Adds the marks to **`total_marks`** (accumulator pattern).
   - If the marks are **40 or more**, increases **`pass_count`** by 1.
5. **After** the loop ends (not inside it), calculates:
   - **`average = total_marks / student_count`**
6. Prints exactly these three lines (labels and spacing as shown):

```
Total marks: <total_marks>
Class average: <average>
Students passed: <pass_count>
```

Replace `<total_marks>`, `<average>`, and `<pass_count>` with the computed values. The average may be a decimal (e.g., `72.5`) — that is expected.

### Sample Runs

**Sample Run 1**

Input:
```
Enter number of students: 3
Enter marks: 80
Enter marks: 65
Enter marks: 90
```

Expected Output:
```
Total marks: 235
Class average: 78.33333333333333
Students passed: 3
```

**Sample Run 2**

Input:
```
Enter number of students: 4
Enter marks: 55
Enter marks: 35
Enter marks: 40
Enter marks: 22
```

Expected Output:
```
Total marks: 152
Class average: 38.0
Students passed: 2
```

**Sample Run 3**

Input:
```
Enter number of students: 2
Enter marks: 40
Enter marks: 39
```

Expected Output:
```
Total marks: 79
Class average: 39.5
Students passed: 1
```

### Constraints

- Use a **`for` loop** with **`range()`** — do not use a `while` loop for this task.
- Use **`total_marks`** and **`pass_count`** as accumulators initialized **before** the loop.
- Calculate **`average` only once**, **outside** the loop.
- Use an **`if` statement** inside the loop to check `marks >= 40` for the pass count.
- Add at least **one comment** (`#`) explaining what the program does.
- Write your complete program in [OneCompiler Python](https://onecompiler.com/python).

### Submission Instruction

1. Open [https://onecompiler.com/python](https://onecompiler.com/python) and create a new Python file.
2. Write your complete program in the editor, then click **Run** and verify the output against the sample runs above.
3. Click the **Save** button at the top right.
4. Enter your **assignment name**, set visibility to **Public**, and save.
5. Click the **Share** button, copy the link, and submit that link in the answer box on the LMS.

![Step - 1](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/5b930478-03c2-4255-a724-d0990da5e4f4/C0AFXttOJJhW3o1S.png)

![Step-2](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/c817d308-66ca-4b5a-8579-db26951ad1a2/PGcKY2hqUQgysgPo.png)

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Read **`student_count`** with `int(input(...))` so the loop runs the correct number of times.  
2. Set **`total_marks = 0`** and **`pass_count = 0`** before the loop — both are accumulators.  
3. Loop with **`for i in range(student_count):`** — each round reads one student's marks.  
4. Inside the loop: add marks to **`total_marks`**; if **`marks >= 40`**, add 1 to **`pass_count`**.  
5. **After** the loop, compute **`average = total_marks / student_count`** and print all three summary lines.

### Reference Solution — `class_summary.py`

```python
# Class monitor summary — total marks, average, and pass count

# Step 1: Read how many students to process
student_count = int(input("Enter number of students: "))

# Step 2: Initialize accumulators before the loop
total_marks = 0
pass_count = 0

# Step 3: Collect marks once per student
for i in range(student_count):
    marks = int(input("Enter marks: "))
    total_marks = total_marks + marks  # Add to running total
    if marks >= 40:  # Pass threshold
        pass_count = pass_count + 1  # Count passes

# Step 4: Calculate average once, outside the loop
average = total_marks / student_count

# Step 5: Print summary
print("Total marks:", total_marks)
print("Class average:", average)
print("Students passed:", pass_count)
```

### Sample Verification

| Students | Marks entered | total_marks | average | pass_count |
| --- | --- | --- | --- | --- |
| 3 | 80, 65, 90 | 235 | 78.333… | 3 |
| 4 | 55, 35, 40, 22 | 152 | 38.0 | 2 |
| 2 | 40, 39 | 79 | 39.5 | 1 |

### Alternative Approaches

- Use **`pass_count += 1`** and **`total_marks += marks`** shorthand instead of long-form addition — same logic.  
- A **`while` loop** with a decreasing counter could also work, but this assignment requires a **`for` loop** with **`range()`**.  
- You could use **`for i in range(1, student_count + 1)`** if you prefer 1-based counting — `range(student_count)` is sufficient because only the number of iterations matters, not the value of `i`.
