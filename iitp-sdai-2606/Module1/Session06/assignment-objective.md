# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A **metro station** checks passengers in two steps: first whether they have a valid ticket, and only then whether they are carrying an oversized bag.

Which term best describes putting one `if` block inside another `if` block?

A. Nested loop  
B. Nested conditional  
C. Dictionary lookup  
D. Constant time access  

**Correct Answer:** B

**Answer Explanation:**  
When one conditional block is written inside another, it is called a **nested conditional**. The inner check runs only after the outer check passes.

**Why other options are wrong:**  
- A: A nested loop involves loops inside loops, not `if` blocks.  
- C: Dictionary lookup is about fetching a value using a key.  
- D: Constant time access is a Big-O idea, not a control-structure pattern.

---

## Q2 (MCQ, Easy)

In a **school assembly**, the principal calls each class one by one. For every class, the teacher reads every roll number in that class.

What does a **nested loop** mean?

A. One loop is written inside another loop  
B. One `if` is written inside another `if`  
C. A loop can run only once in a program  
D. A loop must always use `while`  

**Correct Answer:** A

**Answer Explanation:**  
A **nested loop** means a loop is placed inside another loop. For each iteration of the outer loop, the inner loop usually runs completely.

**Why other options are wrong:**  
- B: That describes nested conditionals, not nested loops.  
- C: Loops are meant to repeat work; they are not limited to one run.  
- D: Nested loops can use `for`, `while`, or a mix of both.

---

## Q3 (MCQ, Easy)

A **cinema hall** stores seat data in a 2D list:

```python
hall = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"],
]
```

What will `hall[2][1]` print?

A. `A2`  
B. `B2`  
C. `C2`  
D. `C3`  

**Correct Answer:** C

**Answer Explanation:**  
In a 2D list, the first index is the **row** and the second index is the **column**. `hall[2][1]` means row 2, column 1, which is `"C2"`.

**Why other options are wrong:**  
- A: That is row 0, column 1.  
- B: That is row 1, column 1.  
- D: That is row 2, column 2.

---

## Q4 (MCQ, Easy)

A **food delivery app** stores dish prices in a dictionary:

```python
menu = {"dosa": 60, "idli": 40, "vada": 30}
```

Which operation is the best example of **O(1)** time?

A. `menu["dosa"]`  
B. Loop through every item in `menu`  
C. Two nested loops over all menu items  
D. Add every price in `menu` using one loop  

**Correct Answer:** A

**Answer Explanation:**  
Direct dictionary lookup using a key is treated as **constant time** on average because the program jumps directly to the required value.

**Why other options are wrong:**  
- B and D: One full loop over growing data is **O(n)**.  
- C: Two nested loops over the same growing data are **O(n²)**.

---

## Q5 (MCQ, Moderate)

A **coding club** prints all coordinate pairs using:

```python
for i in range(4):
    for j in range(5):
        print(i, j)
```

Approximately how many lines will be printed?

A. 9  
B. 20  
C. 4  
D. 5  

**Correct Answer:** B

**Answer Explanation:**  
The outer loop runs 4 times and the inner loop runs 5 times for each outer value. Total prints are `4 × 5 = 20`.

**Why other options are wrong:**  
- A: `9` would come from `3 × 3`, not `4 × 5`.  
- C and D: These count only one loop, not both nested loops together.

---

## Q6 (MCQ, Moderate)

While searching for a contact name in a long phone list, the name is found at the **very last position**.

Which case does this represent?

A. Best case  
B. Average case  
C. Worst case  
D. Constant case  

**Correct Answer:** C

**Answer Explanation:**  
When the target is at the end, the program does the **maximum work** needed for that search. This is the **worst case**.

**Why other options are wrong:**  
- A: Best case is when the answer is found immediately.  
- B: Average case is a typical middle situation, not the slowest one.  
- D: Constant case is not a standard best/average/worst-case label here.

---

## Q7 (MSQ, Moderate)

A **bank ATM** program checks card validity first, and only then checks whether the balance is enough for withdrawal.

Which statements about **nested conditionals** are correct?

A. The inner condition runs only when the outer condition passes  
B. An `elif` block can appear inside an outer `if` block  
C. Python decides block structure using indentation  
D. Nested conditionals mean the inner check must run even when the outer check fails  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Nested conditionals depend on the outer check passing first. Python uses indentation to show which code belongs inside which block, and `elif` can be used inside a nested structure when needed.

**Why other options are wrong:**  
- D: If the outer condition fails, the inner block is skipped.

---

## Q8 (MSQ, Moderate)

A **billing app** analyses different code patterns to understand performance.

Which patterns are **O(n)** in the usual sense?

A. One `for` loop adding every value in a list  
B. `numbers[0]` on a list  
C. One `for` loop with an `if` check inside it  
D. Two nested `for` loops over the same list  

**Correct Answers:** A, C

**Answer Explanation:**  
A single loop over `n` items is **O(n)**. An `if` inside that loop does not change the overall loop count, so it remains **O(n)**.

**Why other options are wrong:**  
- B: Direct index access is **O(1)**.  
- D: Two nested loops over the same growing input are **O(n²)**.

---

## Q9 (MSQ, Hard)

A **startup team** compares three programs that process customer data.

Which statements about **Big-O** are correct?

A. Two nested loops over the same input size `n` are usually **O(n²)**  
B. Three nested loops over the same input size `n` are usually **O(n³)**  
C. An `if` statement inside one loop automatically makes the code **O(n²)**  
D. In complexity analysis, worst case is often the most important case to consider  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Two fully nested loops over `n` give `n × n` work, and three give `n × n × n`. Worst case shows the maximum work a program may need. A single `if` inside one loop does not by itself create quadratic growth.

**Why other options are wrong:**  
- C: The number of loops matters more than the presence of an `if` inside one loop.

---

## Q10 (MSQ, Hard)

A **clothing store app** generates shirt-and-pant combinations:

```python
shirts = ["white", "black"]
pants = ["black", "khaki", "gray"]

for shirt in shirts:
    for pant in pants:
        if shirt == "black" and pant == "black":
            continue
        print(shirt, pant)
```

Which statements are correct?

A. The inner loop runs completely for every shirt  
B. `continue` skips only the current unwanted combination  
C. `break` would stop only the inner loop where it is written  
D. This pattern always has **O(1)** time complexity  

**Correct Answers:** A, B, C

**Answer Explanation:**  
For each shirt, the program checks every pant. `continue` skips one pair and moves to the next pant. `break` exits the loop in which it appears, which here would be the inner loop.

**Why other options are wrong:**  
- D: The work grows with the number of shirts and pants, so it is not constant time.
