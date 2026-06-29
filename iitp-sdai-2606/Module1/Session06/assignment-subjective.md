# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Meera** manages weekend bookings for a **community cinema hall**. The hall seating chart is stored as a **2D list**, where:

- `"O"` means the seat is **open**
- `"X"` means the seat is **booked**

She wants a small Python program that scans the full hall grid and reports every open seat along with the total number of open seats.

### Problem Statement

Write a Python program that:

1. Uses this hardcoded seating chart:

```python
seats = [
    ["O", "X", "O", "O"],
    ["X", "X", "O", "O"],
    ["O", "O", "O", "X"],
]
```

2. Uses **nested loops** to scan every row and every column.
3. Uses a **conditional** to check whether a seat is open (`"O"`).
4. Prints each open seat on its own line in this format:

```text
Open seat at row 0, col 0
```

5. Keeps a **counter outside both loops** to count open seats.
6. Prints the final total in this format:

```text
Total open seats: 8
```

### Sample Output

```text
Open seat at row 0, col 0
Open seat at row 0, col 2
Open seat at row 0, col 3
Open seat at row 1, col 2
Open seat at row 1, col 3
Open seat at row 2, col 0
Open seat at row 2, col 1
Open seat at row 2, col 2
Total open seats: 8
```

### Constraints

- Use nested `for` loops with `range(len(...))` or direct row/column iteration.
- Do not use external libraries.
- Place the open-seat counter **outside both loops**.
- Reset logic is not needed because you are counting the full grid once.
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

1. Store the 2D seating chart in a variable named `seats`.  
2. Create `open_count = 0` before both loops so the counter is not reset incorrectly.  
3. Use an outer loop for rows and an inner loop for columns.  
4. Check whether `seats[row][col] == "O"`.  
5. If the seat is open, print its position and increase `open_count` by 1.  
6. After both loops finish, print the final total.

### Reference Solution — `cinema_open_seats.py`

```python
# Scan a cinema hall seating chart and count open seats

# Hardcoded 2D seating chart
seats = [
    ["O", "X", "O", "O"],
    ["X", "X", "O", "O"],
    ["O", "O", "O", "X"],
]

# Counter must stay outside both loops
open_count = 0

# Outer loop scans each row
for row in range(len(seats)):
    # Inner loop scans each column in the current row
    for col in range(len(seats[row])):
        # Check whether the current seat is open
        if seats[row][col] == "O":
            # Print the open seat position
            print(f"Open seat at row {row}, col {col}")

            # Increase the open-seat counter
            open_count = open_count + 1

# Print the final total after scanning the full grid
print("Total open seats:", open_count)
```

### Sample Verification

For the given grid:

- Row 0 has 3 open seats  
- Row 1 has 2 open seats  
- Row 2 has 3 open seats  

Total open seats = `3 + 2 + 3 = 8`

### Alternative Approaches

- Loop directly with `for row_index, row in enumerate(seats):` and `for col_index, seat in enumerate(row):` if you want index and value together.  
- Use `open_count += 1` instead of `open_count = open_count + 1` for a shorter update style.  
- Print using comma-separated `print()` instead of an f-string if you prefer the basics-only style.
