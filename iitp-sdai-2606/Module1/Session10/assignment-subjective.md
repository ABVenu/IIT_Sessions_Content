# Subjective Assignment: Nested Loops and Second Largest

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

A campus fest team stores booth ratings in Python lists. They need two helpers:

1. Find **all** booth-id pairs whose **product is even**.  
2. Find the **second largest** rating after sorting.

Build both helpers in one file and print the required sample outputs.

## Task

Create a single Python file named `fest_list_practice.py`.

### Part A — Pair with even product

Write a function:

```python
def pair_with_even_product(nums):
    ...
```

**Rules:**

- Use nested loops with indexes.
- Inner loop must start at `i + 1`.
- Collect **all** pairs `[nums[i], nums[j]]` whose product is even.
- Do **not** return early on the first match.
- If no pair qualifies, return an empty list `[]`.

**Sample call:**

```python
print(pair_with_even_product([8, 3, 5]))
```

**Expected output:**

```text
[[8, 3], [8, 5]]
```

(Order of pairs should match nested-loop order: outer `i` ascending, inner `j` ascending.)

### Part B — Second largest using sorting

Write a function:

```python
def second_largest_using_sorting(nums):
    ...
```

**Rules:**

- Create an ascending sorted list with `sorted(nums)`.
- Return the value at index `size - 2`.
- You may assume the input has at least 2 elements for this task.

**Sample call:**

```python
print(second_largest_using_sorting([12, 45, 30, 18, 40]))
```

**Expected output:**

```text
40
```

### Part C — Local checks

At the bottom of the same file, also print:

```python
print(pair_with_even_product([1, 3, 5]))  # no even factor → empty list
print(second_largest_using_sorting([10, 20, 30, 40, 50, 15]))
```

**Expected output for these two prints:**

```text
[]
40
```

Add **one short comment** near the even-product function explaining why early `return` would be wrong for Part A.

---

## Submission Instructions

- Code all steps in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. For Part A, nest `i` and `j = i + 1 ...`, compute product, append when `product % 2 == 0`, return the list after both loops.  
2. For Part B, `sorted(nums)` then return `new_array[len(new_array) - 2]`.  
3. Run the sample prints to confirm `[[8, 3], [8, 5]]`, `40`, `[]`, and `40`.

### Complete Code

```python
def pair_with_even_product(nums):
    # Early return would miss later valid pairs; collect all matches instead.
    n = len(nums)
    pair_output = []

    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            if product % 2 == 0:
                pair_output.append([nums[i], nums[j]])

    return pair_output


def second_largest_using_sorting(nums):
    new_array = sorted(nums)
    size = len(new_array)
    return new_array[size - 2]


print(pair_with_even_product([8, 3, 5]))
print(second_largest_using_sorting([12, 45, 30, 18, 40]))
print(pair_with_even_product([1, 3, 5]))
print(second_largest_using_sorting([10, 20, 30, 40, 50, 15]))
```

### Alternative approaches

- Part A can later be extended with an `is_even` flag for odd products (optional; not required here).  
- Part B can also be solved with a single O(n) pass tracking largest and second largest; this task specifically asks for the `sorted()` + `size - 2` method.

### Notes for evaluation

- Accept solutions that match the expected printed values.  
- Do not require dictionary-based two-sum, Bubble Sort, or Selection Sort.  
- Small differences in spacing are fine; pair order should follow nested-loop order for `[8, 3, 5]`.
