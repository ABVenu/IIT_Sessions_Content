# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Arjun** manages a weekend **street food stall** near his college gate. Every evening he records how many plates of each dish he sold. Instead of adding numbers on paper, he wants a small Python program that stores each dish name and plate count in **lists**, then prints a quick **sales summary** — total plates sold, busiest and slowest day-by-dish counts, average plates per dish, and a sorted view of the counts.

### Problem Statement

Write a Python program that:

1. Asks **`Enter number of dishes sold today: `** and stores the value as an integer (use `int()`).
2. Creates two **empty lists**: **`dish_names`** and **`plate_counts`**.
3. Uses a **`for` loop** with **`range()`** to run exactly that many times — once per dish.
4. Inside each round of the loop:
   - Asks **`Enter dish name: `** and **`append`** the name to **`dish_names`**.
   - Asks **`Enter plates sold: `** and **`append`** the integer count to **`plate_counts`** (use `int()` on input).
5. **After** the loop ends (not inside it), calculates:
   - **`total_plates = sum(plate_counts)`**
   - **`highest = max(plate_counts)`**
   - **`lowest = min(plate_counts)`**
   - **`average = total_plates / len(plate_counts)`**
6. Creates a **copy** of the counts for sorting: **`sorted_counts = plate_counts[:]`**, then calls **`sorted_counts.sort()`** (ascending).
7. Prints the lines below in order. For the summary line, use **string concatenation** with **`+`** and **`str()`** — do not use f-strings.

```
Total plates sold: <total_plates>
Highest plates (one dish): <highest>
Lowest plates (one dish): <lowest>
Average plates per dish: <average>
Sorted plate counts: <sorted_counts>
Summary: <total_plates> plates recorded across <count> dishes.
```

Replace `<total_plates>`, `<highest>`, `<lowest>`, `<average>`, `<sorted_counts>`, and `<count>` with the computed values. The average may be a decimal — that is expected. The last line must be built with **`+`** and **`str()`** (e.g., `"Summary: " + str(total_plates) + " plates recorded across " + str(count) + " dishes."`).

### Sample Runs

**Sample Run 1**

Input:
```
Enter number of dishes sold today: 3
Enter dish name: Pani Puri
Enter plates sold: 45
Enter dish name: Vada Pav
Enter plates sold: 30
Enter dish name: Dosa
Enter plates sold: 52
```

Expected Output:
```
Total plates sold: 127
Highest plates (one dish): 52
Lowest plates (one dish): 30
Average plates per dish: 42.333333333333336
Sorted plate counts: [30, 45, 52]
Summary: 127 plates recorded across 3 dishes.
```

**Sample Run 2**

Input:
```
Enter number of dishes sold today: 2
Enter dish name: Idli
Enter plates sold: 20
Enter dish name: Samosa
Enter plates sold: 20
```

Expected Output:
```
Total plates sold: 40
Highest plates (one dish): 20
Lowest plates (one dish): 20
Average plates per dish: 20.0
Sorted plate counts: [20, 20]
Summary: 40 plates recorded across 2 dishes.
```

**Sample Run 3**

Input:
```
Enter number of dishes sold today: 4
Enter dish name: Biryani
Enter plates sold: 15
Enter dish name: Chaat
Enter plates sold: 38
Enter dish name: Kulcha
Enter plates sold: 22
Enter dish name: Lassi
Enter plates sold: 10
```

Expected Output:
```
Total plates sold: 85
Highest plates (one dish): 38
Lowest plates (one dish): 10
Average plates per dish: 21.25
Sorted plate counts: [10, 15, 22, 38]
Summary: 85 plates recorded across 4 dishes.
```

### Constraints

- Use **`append`** inside the loop to grow both lists — do not pre-fill dish data.
- Use **`sum()`**, **`len()`**, **`max()`**, and **`min()`** for the summary calculations.
- Sort **`sorted_counts`** with **`.sort()`** on the **slice copy** so **`plate_counts`** stays in entry order.
- Build the **`Summary:`** line only with **`+`** and **`str()`**.
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

1. Read **`dish_count`** with `int(input(...))` so the loop runs once per dish.  
2. Start with empty **`dish_names`** and **`plate_counts`** lists.  
3. Loop with **`for i in range(dish_count):`** — each round reads one dish name and plate count, then **`append`** both values.  
4. **After** the loop, use **`sum`**, **`max`**, **`min`**, and **`len`** for the numeric summary.  
5. Copy counts with **`plate_counts[:]`**, **`sort()`** the copy, and print all lines.  
6. Build the **`Summary:`** line with **`+`** and **`str()`** as required.

### Reference Solution — `stall_summary.py`

```python
# Street food stall — collect dish sales and print summary

# Step 1: Read how many dishes were sold
dish_count = int(input("Enter number of dishes sold today: "))

# Step 2: Empty lists for parallel data
dish_names = []
plate_counts = []

# Step 3: Collect one dish per loop round
for i in range(dish_count):
    name = input("Enter dish name: ")
    plates = int(input("Enter plates sold: "))
    dish_names.append(name)
    plate_counts.append(plates)

# Step 4: Summary calculations after all input
total_plates = sum(plate_counts)
highest = max(plate_counts)
lowest = min(plate_counts)
average = total_plates / len(plate_counts)

# Step 5: Sorted copy — original entry order preserved
sorted_counts = plate_counts[:]
sorted_counts.sort()

# Step 6: Print report
print("Total plates sold:", total_plates)
print("Highest plates (one dish):", highest)
print("Lowest plates (one dish):", lowest)
print("Average plates per dish:", average)
print("Sorted plate counts:", sorted_counts)
print("Summary: " + str(total_plates) + " plates recorded across " + str(dish_count) + " dishes.")
```

### Sample Verification

| Dishes | Plate counts | total | highest | lowest | average | sorted_counts |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 45, 30, 52 | 127 | 52 | 30 | 42.333… | [30, 45, 52] |
| 2 | 20, 20 | 40 | 20 | 20 | 20.0 | [20, 20] |
| 4 | 15, 38, 22, 10 | 85 | 38 | 10 | 21.25 | [10, 15, 22, 38] |

### Alternative Approaches

- Store **`count = len(plate_counts)`** in a variable for the summary line instead of reusing **`dish_count`** — both are equal if every round appends once.  
- Use **`sorted_counts = plate_counts.copy()`** instead of **`plate_counts[:]`** — same idea for a shallow copy.  
- **`plate_counts.sort()`** without a copy would reorder the original list; the assignment asks for a **sorted copy** while keeping entry order in **`plate_counts`**.
