# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Meera** is a volunteer at her college **Sports Day leaderboard desk**. Each athlete is given a **rank score** (lower score means better rank). At the end of the morning heats, she receives the scores in random order and must publish the leaderboard in **ascending order** (best rank first).

She wants a small Python program with **two reusable sorting functions** so she can cross-check the result using both **Bubble Sort** and **Selection Sort**.

### Problem Statement

Write a Python program that:

1. Defines a function `bubble_sort(scores)` that:
   - receives a list of numbers
   - sorts the list in **ascending order** using the Bubble Sort logic (nested loops, adjacent comparisons, swaps)
   - returns the sorted list
2. Defines a function `selection_sort(scores)` that:
   - receives a list of numbers
   - sorts the list in **ascending order** using the Selection Sort logic (find minimum in unsorted part, swap into position)
   - returns the sorted list
3. Uses these three lists in your program:
   ```python
   original = [42, 15, 28, 9, 35]
   bubble_data = [42, 15, 28, 9, 35]
   selection_data = [42, 15, 28, 9, 35]
   ```
4. Calls `bubble_sort(bubble_data)` and `selection_sort(selection_data)` and stores the returned lists.
5. Prints the output in **exactly** this format:

```text
Original: [42, 15, 28, 9, 35]
Bubble Sort: [9, 15, 28, 35, 42]
Selection Sort: [9, 15, 28, 35, 42]
Both results match: Yes
```

### Expected Output

```text
Original: [42, 15, 28, 9, 35]
Bubble Sort: [9, 15, 28, 35, 42]
Selection Sort: [9, 15, 28, 35, 42]
Both results match: Yes
```

### Constraints

- Use `def`, nested loops, `len()`, `range()`, comparisons, and swaps as needed.
- Do **not** use Python's built-in `sorted()` or `list.sort()`.
- Keep both sorting functions in the **same file**.
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

1. Create `bubble_sort(scores)` with an outer loop for passes and an inner loop for adjacent comparisons.  
2. Swap neighbouring values when the left value is greater than the right value.  
3. Create `selection_sort(scores)` with an outer loop for each position and an inner loop to find the minimum index in the unsorted part.  
4. Swap the minimum value into the current position after the inner search completes.  
5. Use separate copies of the same starting list so each function sorts independently.  
6. Print the original list, both sorted results, and whether they match.

### Reference Solution — `sports_leaderboard_sort.py`

```python
# Sports Day leaderboard sorter using Bubble Sort and Selection Sort

def bubble_sort(scores):
    n = len(scores)
    for pass_index in range(n - 1):
        for i in range(n - 1 - pass_index):
            if scores[i] > scores[i + 1]:
                temp = scores[i]
                scores[i] = scores[i + 1]
                scores[i + 1] = temp
    return scores


def selection_sort(scores):
    n = len(scores)
    for current_index in range(n - 1):
        min_index = current_index
        for i in range(current_index + 1, n):
            if scores[i] < scores[min_index]:
                min_index = i
        temp = scores[current_index]
        scores[current_index] = scores[min_index]
        scores[min_index] = temp
    return scores


original = [42, 15, 28, 9, 35]
bubble_data = [42, 15, 28, 9, 35]
selection_data = [42, 15, 28, 9, 35]

bubble_result = bubble_sort(bubble_data)
selection_result = selection_sort(selection_data)

print("Original:", original)
print("Bubble Sort:", bubble_result)
print("Selection Sort:", selection_result)

if bubble_result == selection_result:
    print("Both results match: Yes")
else:
    print("Both results match: No")
```

### Sample Verification

Starting list: `[42, 15, 28, 9, 35]`

- **Bubble Sort** bubbles larger values rightward over multiple passes until the list becomes `[9, 15, 28, 35, 42]`.  
- **Selection Sort** repeatedly places the smallest remaining value on the left until the list becomes `[9, 15, 28, 35, 42]`.  
- Both methods produce the same final order, so the program prints `Both results match: Yes`.

### Alternative Approaches

- Use Python's one-line swap: `scores[i], scores[i + 1] = scores[i + 1], scores[i]` inside Bubble Sort.  
- Store `min_index` as `min_assume` or any clear variable name — the logic stays the same.  
- Print the match line with a boolean converted to text if you prefer: `print("Both results match:", "Yes" if bubble_result == selection_result else "No")`.
