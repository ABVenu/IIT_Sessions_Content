**Q1: What does the 'and' operator do?**
A. Returns True if one condition is True
B. Returns True if both are True
C. Returns False always
D. Skips conditions

**Answer:** B

---

**Q2: What does the 'or' operator return?**
A. True if both are True
B. True if at least one is True
C. False always
D. Only numbers

**Answer:** B

---

**Q3: Which statement starts a condition block?**
A. for
B. while
C. if
D. print

**Answer:** C

---

**Q4: What is a nested conditional statement?**
A. Loop inside loop
B. if inside another if
C. Function inside loop
D. Print inside input

**Answer:** B

---

**Q5: When does the 'else' block execute?**
A. When if is True
B. When all conditions are False
C. Always runs
D. Only with loops

**Answer:** B

---

**Q6: What will this output?
if True:
 if False: print("A")
 else: print("B")**
A. A
B. B
C. Both
D. Error

**Answer:** B

---

**Q7: Which keyword is used for checking multiple conditions?**
A. else
B. elif
C. def
D. break

**Answer:** B

---

**Q8: What will this print?
if False: print("X")
elif True: print("Y")
else: print("Z")**
A. X
B. Y
C. Z
D. Nothing

**Answer:** B

---

### **Subjective Question**

Follow the instructions below and complete all tasks:

1. Create a folder named **Agentic Systems Design** on your computer
2. Inside it, create a subfolder **Module 1**
3. Inside that, create another folder **Session 2**
4. Open this folder in VS Code
5. Create a Python file named **conditions.py**
6. Write code to solve all the questions given below
7. Run the code using the terminal (`python3 conditions.py`) and verify the output
8. Once everything works correctly, copy and paste your complete code into the answer box

---

### **Tasks**

Write Python code for the following:

- Take a number as input from the user and check whether it is positive, negative, or zero using **if / elif / else**.
- Take a number and check whether it is even or odd.
- Write a program to check if a person is eligible to vote (age ≥ 18).
- Write a program using **nested if** to check:
  - If a number is greater than 10
  - If yes, check whether it is even or odd

- Take two boolean inputs and print the result using **logical operators (and, or)**.
- Write a program to take marks as input and print grade:
  - ≥ 90 → A
  - ≥ 75 → B
  - ≥ 50 → C
  - Otherwise → Fail

---

### Solution

```
# 1. Check positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check even or odd
num2 = int(input("Enter another number: "))
if num2 % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4. Nested if condition
num3 = int(input("Enter a number: "))
if num3 > 10:
    if num3 % 2 == 0:
        print("Greater than 10 and Even")
    else:
        print("Greater than 10 and Odd")
else:
    print("Number is not greater than 10")


# 5. Logical operators
a = input("Enter True/False: ") == "True"
b = input("Enter True/False: ") == "True"

print("AND result:", a and b)
print("OR result:", a or b)


# 6. Grade calculation
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```
