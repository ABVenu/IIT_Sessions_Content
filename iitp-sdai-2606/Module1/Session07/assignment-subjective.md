# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Neha** manages a **campus stationery counter** that sells three fixed-price items:

- Notebook — ₹50 each  
- Pen — ₹20 each  
- Folder — ₹80 each  

Instead of calculating every bill manually, she wants a small Python program built from **reusable functions** so each step has one clear job and the final bill is produced by chaining function outputs.

### Problem Statement

Write a Python program that:

1. Defines a function `total_for_item(item, quantity)` that returns the line total for one item:
   - `"notebook"` → `quantity * 50`
   - `"pen"` → `quantity * 20`
   - `"folder"` → `quantity * 80`
2. Defines a function `calculate_subtotal(n1, n2, n3)` that returns the sum of three item totals.
3. Defines a function `apply_discount(subtotal, rate=0.05)` that:
   - returns `subtotal` unchanged when `subtotal < 500`
   - otherwise returns `subtotal - subtotal * rate`
4. Defines a function `final_bill(amount)` that adds **10% tax** to `amount` and returns the final payable amount.
5. Reads three integer quantities from the user in this order:
   - notebooks
   - pens
   - folders
6. Uses function chaining so that:
   - the three `total_for_item(...)` results become arguments to `calculate_subtotal(...)`
   - the subtotal becomes input to `apply_discount(...)`
   - the discounted amount becomes input to `final_bill(...)`
7. Prints only the final line in this exact format:

```text
Final amount to be collected: <value>
```

### Sample Input

```text
5
2
3
```

### Sample Output

```text
Final amount to be collected: 553.85
```

### How the Sample Output Is Calculated

- Notebook total: `5 × 50 = 250`  
- Pen total: `2 × 20 = 40`  
- Folder total: `3 × 80 = 240`  
- Subtotal: `250 + 40 + 240 = 530`  
- Discount at 5% because subtotal ≥ 500: `530 - 26.5 = 503.5`  
- Tax at 10%: `503.5 + 50.35 = 553.85`

### Second Sample Input

```text
2
1
1
```

### Second Sample Output

```text
Final amount to be collected: 220.0
```

### How the Second Sample Output Is Calculated

- Notebook total: `100`  
- Pen total: `20`  
- Folder total: `80`  
- Subtotal: `200`  
- No discount because subtotal `< 500`  
- Tax at 10%: `200 + 20 = 220.0`

### Constraints

- Use `def`, parameters, arguments, `return`, and at least one default parameter value.
- Do not put all billing logic in one long block; each function must do one clear job.
- Do not use external libraries.
- Assume all quantities are whole numbers `≥ 0`.
- Write your complete program in a single `.py` file.

### Submission Instruction

- Code all the points mentioned above in a single `.py` file in VS Code.
- Run the code and verify it with both sample inputs.
- Then submit the code in the code editor/answer box in the LMS.

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Create `total_for_item(item, quantity)` to handle one item's price logic using `if` / `elif` / `else`.  
2. Create `calculate_subtotal(n1, n2, n3)` to add the three returned totals.  
3. Create `apply_discount(subtotal, rate=0.05)` with a default discount rate and a conditional check for `subtotal >= 500`.  
4. Create `final_bill(amount)` to add 10% tax and return the payable amount.  
5. Read notebook, pen, and folder quantities from the user.  
6. Chain the functions in order and print the final bill.

### Reference Solution — `stationery_bill.py`

```python
def total_for_item(item, quantity):
    if item == "notebook":
        return quantity * 50
    elif item == "pen":
        return quantity * 20
    else:
        return quantity * 80


def calculate_subtotal(n1, n2, n3):
    return n1 + n2 + n3


def apply_discount(subtotal, rate=0.05):
    if subtotal < 500:
        return subtotal
    return subtotal - subtotal * rate


def final_bill(amount):
    return amount + amount * 0.10


notebook_qty = int(input("Enter quantity of notebooks: "))
pen_qty = int(input("Enter quantity of pens: "))
folder_qty = int(input("Enter quantity of folders: "))

n1 = total_for_item("notebook", notebook_qty)
n2 = total_for_item("pen", pen_qty)
n3 = total_for_item("folder", folder_qty)

subtotal = calculate_subtotal(n1, n2, n3)
discounted = apply_discount(subtotal)
bill = final_bill(discounted)

print("Final amount to be collected:", bill)
```

### Sample Verification

**Input:** `5`, `2`, `3`

- `n1 = 250`, `n2 = 40`, `n3 = 240`
- `subtotal = 530`
- `discounted = 530 - 26.5 = 503.5`
- `bill = 503.5 + 50.35 = 553.85`

**Input:** `2`, `1`, `1`

- `n1 = 100`, `n2 = 20`, `n3 = 80`
- `subtotal = 200`
- `discounted = 200`
- `bill = 220.0`

### Alternative Approaches

- Chain directly in one line:  
  `bill = final_bill(apply_discount(calculate_subtotal(n1, n2, n3)))`  
  after computing `n1`, `n2`, and `n3`.
- Store item prices in a dictionary and look up rates inside `total_for_item`, if you want easier future updates.
- Round the final amount with `round(bill, 2)` if you want exactly two decimal places in display.
