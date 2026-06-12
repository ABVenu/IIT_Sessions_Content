# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Riya** runs a **college fest food stall**. She sells **samosas** at **₹15 each** and **chai** at **₹10 per cup**. Customers often order both, and she wants a small Python program on her laptop to calculate each bill quickly instead of using a calculator every time.

### Problem Statement

Write a Python program that:

1. Asks the customer for their **name** (text input).
2. Asks how many **samosas** they bought (whole number).
3. Asks how many **chai cups** they bought (whole number).
4. Uses **variables** to store:
   - fixed prices: samosa = `15`, chai = `10`
   - the quantities entered by the customer
   - the **total bill** (samosas × price + chai × price)
5. Prints a clear bill summary on separate lines, for example:

```
Customer: Aarav
Samosas: 2 x 15 = 30
Chai: 3 x 10 = 30
Total Bill: 60
```

(Your program should work for **any** valid name and non-negative whole numbers the user types.)

### Sample Run

**Input (user types when prompted):**

```
Enter customer name: Aarav
How many samosas? 2
How many chai cups? 3
```

**Expected Output:**

```
Customer: Aarav
Samosas: 2 x 15 = 30
Chai: 3 x 10 = 30
Total Bill: 60
```

### Constraints

- Use `input()` and `print()` for user interaction and output.
- Convert samosa and chai counts to integers with `int()` before doing maths.
- Use **arithmetic operators** (`*`, `+`) for calculations — do not hard-code the final total.
- Add at least **one comment** (`#`) explaining what your program does.
- Write your complete program in [OneCompiler Python](https://onecompiler.com/python).

### Submission Instruction

1. Open [https://onecompiler.com/python](https://onecompiler.com/python) and create a new Python file.
2. Write your complete program in the editor, then click **Run** and verify the output.
3. Click the **Save** button at the top right.
4. Enter your **assignment name**, set visibility to **Public**, and save.
5. Click the **Share** button, copy the link, and submit that link in the answer box on the LMS.

![Step - 1](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/5b930478-03c2-4255-a724-d0990da5e4f4/C0AFXttOJJhW3o1S.png)

![Step-2](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/c817d308-66ca-4b5a-8579-db26951ad1a2/PGcKY2hqUQgysgPo.png)

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Prompt for the customer name with `input()` and store it in a variable.  
2. Prompt for samosa and chai counts; wrap each `input()` with `int()` so maths works on numbers, not strings.  
3. Store fixed prices in variables (`15` and `10`).  
4. Calculate line totals with `*` and grand total with `+`.  
5. Use multiple `print()` calls to show the bill in the required format.

### Reference Solution — `fest_stall_bill.py`

```python
# College fest stall bill calculator for samosas and chai

# Step 1: Get customer name
customer_name = input("Enter customer name: ")

# Step 2: Get quantities (convert to integers for maths)
samosas_count = int(input("How many samosas? "))
chai_count = int(input("How many chai cups? "))

# Step 3: Fixed prices
samosa_price = 15
chai_price = 10

# Step 4: Calculate line totals and grand total
samosas_total = samosas_count * samosa_price
chai_total = chai_count * chai_price
grand_total = samosas_total + chai_total

# Step 5: Print bill summary
print("Customer:", customer_name)
print("Samosas:", samosas_count, "x", samosa_price, "=", samosas_total)
print("Chai:", chai_count, "x", chai_price, "=", chai_total)
print("Total Bill:", grand_total)
```

### Sample Verification

For input `Aarav`, `2`, `3`:

- Samosas: `2 * 15 = 30`  
- Chai: `3 * 10 = 30`  
- Total: `30 + 30 = 60`

### Alternative Approaches

- Store `int(input(...))` directly in one line for each quantity (same logic, fewer variables).  
- Use an f-string for each line if you already know f-strings — comma-separated `print()` is enough for this assignment.  
- Add a short `#` comment above each major step for readability.
