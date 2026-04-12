## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:
   - Create a **new folder** (name it as per your convenience, e.g., `python-loops-assignment`).

3. Write **separate Python files** for each question inside this folder.

4. For each program:
   - Run the code in the **terminal**
   - Verify the **output**

5. Once everything is ready:
   - Add the changes
   - Commit with a proper message
   - Push to GitHub

6. **Final submission:**
   - Submit the **GitHub folder link** (not the entire repo).

---

### 2.1 Number Printer

**Task:**
Write a Python program that prints all numbers from `0` to `N` (inclusive), where `N` is provided by the user.

**Constraints:**

* Use a `for` loop
* Use `range()`

**Sample Input:**
`4`
**Expected Output:**

```
0
1
2
3
4
```

---

### 2.2 Password Retry System

**Task:**
Create a program that repeatedly asks the user for a password until they enter `"admin123"`.

**Rules:**

* Use a `while` loop
* Print `"Access granted"` once the correct password is entered

**Sample Input:**

```
hello  
admin  
admin123
```

**Expected Output:**
`Access granted`


---

### 2.3 Score Evaluation Pipeline

**Task:**
You are given a list of student scores. Build a program that:

* Iterates through the list
* Prints `"Fail"` for scores below 50
* Prints `"Pass"` for scores 50 and above
* Skips further processing for failed scores using `continue`

**Sample Input:**

```python
scores = [72, 45, 89, 30, 60]
```

**Expected Output:**

```
Pass
Fail
Pass
Fail
Pass
```

**Requirements:**

* Use a `for` loop
* Use `continue`
* Correct indentation
