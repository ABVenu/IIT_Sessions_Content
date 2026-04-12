## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:
   - Create a **new folder** (name it as per your convenience, e.g., `python-logic-assignment`).

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
### 1. Pass or Fail Checker

**Task:**
Write a Python program that asks the user for a numeric score and prints `"Pass"` if the score is **50 or above**, otherwise prints `"Fail"`.

**Constraints:**

* Use an `if-else` statement
* Score is an integer

**Sample Input:**
`45`
**Expected Output:**
`Fail`


---

### 2. Access Control System

**Task:**
Ask the user for:

1. Their age
2. Whether they have an ID card (`True` or `False`)

Print `"Entry allowed"` only if the user is **18 or older AND has an ID**.

**Sample Input:**

```
Age: 20  
Has ID: True
```

**Expected Output:**
`Entry allowed`

**Stretch:** Handle incorrect Boolean input gracefully.


---

### 2.3 Secure Transaction Validator

**Task:**
Create a mini-program that simulates a bank withdrawal.

Ask for:

* Account balance (integer)
* Withdrawal amount (integer)
* Verification status (`True` / `False`)

Rules:

* Withdrawal succeeds only if the user is verified **and** withdrawal amount is less than or equal to balance
* Otherwise, print `"Transaction denied"`

**Sample Input:**

```
Balance: 5000  
Withdrawal: 3000  
Verified: True
```

**Expected Output:**
`Withdrawal successful`

**Requirements:**

* Use compound Boolean expressions
* Correct indentation
* Clear variable naming
