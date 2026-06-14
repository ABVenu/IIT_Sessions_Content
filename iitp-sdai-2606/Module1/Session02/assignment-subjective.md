# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Ananya** manages billing at a **college cafeteria**. Regular customers often flash a **membership card**, and the counter gets busy during **peak hours** when bills are high. She wants a small Python program that automatically tells the cashier which **discount message** to apply — instead of mentally checking three different rules for every order.

### Problem Statement

Write a Python program that:

1. Asks for the **bill amount in rupees** (whole number) and stores it in a variable.
2. Asks **"Do you have a membership card? (yes/no): "** and stores the answer in a variable.
3. Stores whether the customer is a member in a **boolean variable** using a comparison, for example:
   ```python
   is_member = membership_answer == "yes"
   ```
4. Uses an **`if` / `elif` / `else`** chain to print **exactly one** of these messages based on the rules below:

   | Condition | Message to print |
   | --- | --- |
   | Bill is **₹1000 or more** **and** customer has membership | `Premium discount: 20% off` |
   | Bill is **₹1000 or more** (membership does not matter) | `Bulk discount: 10% off` |
   | Customer has membership (bill below ₹1000) | `Member discount: 5% off` |
   | None of the above | `No discount today` |

   **Important:** Check the **strictest / most specific rule first** (the row that needs both a high bill **and** membership), then fall through to the simpler rules — just like ordering grade bands from highest to lowest.

5. Uses `int()` when reading the bill amount so comparisons work on numbers, not strings.

### Sample Runs

**Sample Run 1**

Input:
```
Enter bill amount: 1200
Do you have a membership card? (yes/no): yes
```

Expected Output:
```
Premium discount: 20% off
```

**Sample Run 2**

Input:
```
Enter bill amount: 1200
Do you have a membership card? (yes/no): no
```

Expected Output:
```
Bulk discount: 10% off
```

**Sample Run 3**

Input:
```
Enter bill amount: 450
Do you have a membership card? (yes/no): yes
```

Expected Output:
```
Member discount: 5% off
```

**Sample Run 4**

Input:
```
Enter bill amount: 300
Do you have a membership card? (yes/no): no
```

Expected Output:
```
No discount today
```

### Constraints

- Use `input()` and `print()` for interaction and output.
- Use **`and`** in the condition that checks both bill amount and membership.
- Do **not** hard-code which message prints — let the `if` / `elif` / `else` chain decide from the user's inputs.
- Add at least **one comment** (`#`) explaining what the program does.
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

1. Read the bill amount with `int(input(...))` so numeric comparisons work.  
2. Read the membership answer as text and store a boolean with `is_member = membership_answer == "yes"`.  
3. Build an `if` / `elif` / `else` chain with the **combined rule first** (`bill >= 1000 and is_member`), then the high-bill-only rule, then membership-only, then the default.  
4. Print exactly one message — Python stops at the first matching branch.

### Reference Solution — `cafeteria_discount.py`

```python
# Cafeteria discount checker — applies one discount rule per bill

# Step 1: Read bill amount as integer
bill_amount = int(input("Enter bill amount: "))

# Step 2: Read membership answer and store boolean result
membership_answer = input("Do you have a membership card? (yes/no): ")
is_member = membership_answer == "yes"

# Step 3: Check rules from most specific to most general
if bill_amount >= 1000 and is_member:
    print("Premium discount: 20% off")
elif bill_amount >= 1000:
    print("Bulk discount: 10% off")
elif is_member:
    print("Member discount: 5% off")
else:
    print("No discount today")
```

### Sample Verification

| Bill | Membership | Branch matched | Output |
| --- | --- | --- | --- |
| 1200 | yes | First `if` (`>= 1000 and is_member`) | `Premium discount: 20% off` |
| 1200 | no | Second `elif` (`>= 1000`) | `Bulk discount: 10% off` |
| 450 | yes | Third `elif` (`is_member`) | `Member discount: 5% off` |
| 300 | no | `else` | `No discount today` |

### Alternative Approaches

- Compare membership directly: `membership_answer == "yes"` inside each condition instead of storing `is_member` — storing the boolean first matches the pattern of reusing comparison results and keeps conditions shorter.  
- Use `.lower()` on the membership answer if you want to accept `"Yes"` or `"YES"` — for this assignment, exact `"yes"` is enough.  
- You could add a short comment above each branch naming the rule it implements.
