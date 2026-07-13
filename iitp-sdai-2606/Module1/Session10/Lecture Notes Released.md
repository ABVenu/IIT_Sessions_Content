# Hands-on Logic Building & DSA Problem Solving – II

## What You Will Learn in This Lesson

You have already set up **local development** on your laptop with **Python**, **VS Code**, and the **Terminal**. You also learned to plan problems using **input**, **output**, **conditions**, and **steps**, and solved beginner-level questions with **lists**, **strings**, and **dictionaries**.

In this lesson, you will move to **intermediate DSA problem solving** with **lists** and **nested loops**. You will **analyse problems**, convert ideas into algorithms, and solve moderately complex tasks such as **common elements**, **pair with a given sum**, **pair with even (or odd) product**, and **second largest using sorting**. You will also compare **time complexity** ideas like **O(n)**, **O(n²)**, and **O(n log n)**.

By the end, you will be able to break a moderately complex list problem into a clear plan, use index-based nested loops correctly, and apply Python’s built-in `sorted()` when sorting helps you read the answer.

---

## Why Intermediate Problems Need a Different Approach

- **Official Definition:** An **intermediate DSA problem** is a coding question that requires more than one simple loop or one direct condition to solve correctly.
- **In Simple Words:** The problem still uses lists — but you must compare values carefully, often with a loop inside another loop.
- **Real-Life Example:** A scholarship committee receives exam scores in random order. Finding the **second highest** score needs more care than finding the first number in a list.

Beginner problems often need only one loop. Intermediate problems commonly need:

- **Nested loops** — compare each value with others.
- **Extra conditions** — decide when to stop early or collect every match.
- **Sorting** — arrange data first, then read the answer from the ordered list.

The good news is that you already know the building blocks. This lesson shows you how to **combine** them.

---

## Problem Analysis — Plan Before You Code

- **Official Definition:** **Problem analysis** is the process of reading a question carefully and converting the requirements into a step-by-step plan before writing code.
- **In Simple Words:** Understand the rules of the game before you start playing.
- **Real-Life Example:** Before a cricket match, the umpire checks the pitch and overs limit. A programmer checks input, output, and special cases the same way.

| Question to Ask | Why It Matters |
|---|---|
| What is the input and output? | Keeps your function focused |
| Can values repeat? | Changes how you read “second largest” |
| Do I need one pair or all pairs? | Decides early `return` vs collecting results |
| Can the list be empty or too short? | Prevents crashes and wrong assumptions |

**Problem analysis workflow:**

1. Read the problem twice in plain English.
2. Write down **input**, **output**, and special cases.
3. Decide whether you need one loop, nested loops, or sorting.
4. Write numbered steps before opening your editor.
5. Dry-run with a small example, then code.

**Common mistake:** Starting to code immediately without listing the output rules. Five extra minutes of planning often saves thirty minutes of debugging.

![Problem analysis before coding — read constraints, define input and output, write steps, then implement the algorithm on your local machine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-01-problem-analysis-constraints.png?v=20260704)

---

## Nested Loops — When One Loop Is Not Enough

- **Official Definition:** A **nested loop** is a loop placed inside another loop.
- **In Simple Words:** For each item in the outer loop, the inner loop does extra work.
- **Real-Life Example:** An exam invigilator walks row by row (outer task). For each student, they compare roll numbers with nearby students (inner task).

### Index-Based vs Value-Based Iteration

In Python you can loop over **values** directly:

```python
numbers = [4, 7, 4, 9]  # Sample list

for value in numbers:  # Value-based loop — easy for single-pass work
    print(value)  # Prints each number
```

For **pair problems**, you usually need **indexes** with `range` and `len`, so the inner loop can start at `i + 1`:

```python
numbers = [4, 7, 4, 9]  # Sample list
n = len(numbers)  # Store length once

for i in range(n):  # Outer index
    for j in range(i + 1, n):  # Inner index starts after i
        print(numbers[i], numbers[j])  # Print each unique pair of values
```

**How the code works:**

- Value-based loops are clean when you only need each item once.
- Index-based loops are required when the inner loop must start **after** the outer index.
- Starting at `i + 1` avoids comparing the same pair twice and avoids comparing an item with itself.

![Nested loops pair comparison — outer loop picks one index, inner loop compares with later indexes to detect duplicates and valid pairs without checking the same pair twice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-02-nested-loops-pair-comparison.png?v=20260704)

---

## Problem 1: Find Common Elements in Two Lists

- **Official Definition:** **Common elements** are values that appear in both lists.
- **In Simple Words:** Find numbers that belong to list A **and** list B.
- **Real-Life Example:** Two class sections publish roll numbers. Common rolls are students registered in both lists.

**Problem statement:** Given two lists, return the values that appear in both.

**Example:**

- List A: `[1, 2, 3, 4]`
- List B: `[3, 4, 6]`
- Common elements: `[3, 4]`

**Logic plan:**

1. Loop through every value in the first list.
2. For each value, scan the second list.
3. If the value appears in the second list and is not already collected, store it.

```python
def find_common_elements(first, second):  # Define function for two lists
    common = []  # Store shared values

    for value in first:  # Outer loop visits each value in first list
        for other in second:  # Inner loop scans second list
            if value == other:  # Value exists in both lists
                if value not in common:  # Avoid adding the same common value twice
                    common.append(value)  # Save the common value

    return common  # Return all shared values


print(find_common_elements([1, 2, 3, 4], [3, 4, 6]))  # Expected: [3, 4]
```

**How the code works:**

- Nested loops compare every value from the first list with values from the second list.
- The `if value not in common` check keeps the result list clean.
- This pattern is nested logic on **lists** — the main data structure focus of this lesson.

---

## Problem 2: Pair with a Given Sum

- **Official Definition:** A **pair-with-sum** problem asks whether two different positions in a list add up to a target value.
- **In Simple Words:** Find two numbers that make a required total.
- **Real-Life Example:** Two friends want a restaurant bill of exactly 700 rupees. You check which two dish prices add to 700.

**Problem statement:** Given a list and a target sum, return one pair of indexes (or values) whose sum equals the target. If no pair exists, return an empty result.

**Example:**

- Numbers: `[1, 2, 3, 4, 5]`, target = `7`
- One valid pair: `(2, 5)` or `(3, 4)` depending on your walk order

**Logic plan:**

1. Use nested loops with `j` starting at `i + 1`.
2. Check whether `nums[i] + nums[j]` equals the target.
3. On the first match, return that pair immediately.
4. If no match is found, return an empty result.

```python
def pair_with_sum(nums, target):  # Find one pair that adds to target
    n = len(nums)  # Store list length

    for i in range(n):  # Outer index
        for j in range(i + 1, n):  # Inner index after i
            if nums[i] + nums[j] == target:  # Check sum rule
                return [nums[i], nums[j]]  # Early return on first valid pair

    return []  # No pair found


print(pair_with_sum([1, 2, 3, 4, 5], 7))  # One valid pair such as [2, 5] or [3, 4]
print(pair_with_sum([1, 2, 3], 100))  # Expected: []
```

**How the code works:**

- Nested index loops check unique pairs only.
- **Early return** stops as soon as one valid pair is found — useful when the problem asks for any one pair.
- Time complexity of this nested approach is **O(n²)** because each pair may be checked in the worst case.

**Look-ahead (optional practice):** The same problem can often be solved in **O(n)** using a **dictionary** of seen values. That approach was left as post-class practice and is not required for this lesson’s core lab.

---

## Problem 3: Pair with Even Product (and Odd Product)

- **Official Definition:** A **pair-with-product** problem finds pairs whose **product** satisfies a rule, such as even or odd.
- **In Simple Words:** Multiply two numbers and check whether the answer is even or odd.
- **Real-Life Example:** In a puzzle game, only pairs whose product is even unlock the next level.

**Problem statement:** Given a list, return **all** pairs whose product is even.

**Example:**

- Numbers: `[8, 3, 5]`
- Even-product pairs: `(8, 3)` and `(8, 5)` — because `8 * 3 = 24` and `8 * 5 = 40`

**Important rule difference from pair-with-sum:**

- Pair-with-sum often returns **one** pair → early `return` is fine.
- Pair-with-even-product needs **all** matching pairs → collect in a list and return at the end.

```python
def pair_with_even_product(nums):  # Collect all pairs with even product
    n = len(nums)  # Store length
    pair_output = []  # Result list

    for i in range(n):  # Outer index
        for j in range(i + 1, n):  # Inner index after i
            product = nums[i] * nums[j]  # Multiply the pair
            if product % 2 == 0:  # Even product check
                pair_output.append([nums[i], nums[j]])  # Save this pair

    return pair_output  # Return after checking all pairs


print(pair_with_even_product([8, 3, 5]))  # Expected: [[8, 3], [8, 5]]
```

**How the code works:**

- Nested loops build every unique pair.
- `product % 2 == 0` checks evenness.
- Returning early would miss later valid pairs — so collect first, return last.

### Make the Rule Flexible with a Flag

Instead of hard-coding “always even,” pass an argument that chooses even or odd:

```python
def pair_with_product_rule(nums, is_even=True):  # Flag chooses even or odd rule
    n = len(nums)  # Store length
    pair_output = []  # Result list

    for i in range(n):  # Outer index
        for j in range(i + 1, n):  # Inner index after i
            product = nums[i] * nums[j]  # Multiply the pair
            product_is_even = (product % 2 == 0)  # True when product is even

            if is_even and product_is_even:  # User asked for even products
                pair_output.append([nums[i], nums[j]])  # Save even pair
            if (not is_even) and (not product_is_even):  # User asked for odd products
                pair_output.append([nums[i], nums[j]])  # Save odd pair

    return pair_output  # Return collected pairs


print(pair_with_product_rule([8, 3, 5], is_even=True))  # Even products
print(pair_with_product_rule([8, 3, 5], is_even=False))  # Odd products
```

**How the code works:**

- `is_even=True` keeps the original even-product behaviour.
- `is_even=False` switches the filter to odd products.
- One function covers both rules without copying the nested-loop structure twice.

---

## Finding the Second Largest Element Using Sorting

- **Official Definition:** The **second largest element** is the second-highest value when the list is arranged in order — often read as the second-last item after ascending sort.
- **In Simple Words:** After sorting small to large, look at the value just before the largest.
- **Real-Life Example:** In a singing competition, first place is the top score. The runner-up is the next score in the ranking.

### Method Used in This Lesson: `sorted()` Then Index `size - 2`

```python
def second_largest_using_sorting(nums):  # Find second largest via built-in sort
    new_array = sorted(nums)  # Ascending sorted copy
    size = len(new_array)  # Length of sorted list
    return new_array[size - 2]  # Second-last index is second largest for distinct-style ranking


print(second_largest_using_sorting([10, 40, 20, 30, 50, 15]))  # Sorted ends with ..., 40, 50 → 40
```

**How the code works:**

- `sorted(nums)` creates an ascending list.
- Index `size - 1` is the largest value.
- Index `size - 2` is the second-last value — treated here as the second largest.

**Edge-case thinking:** If all values are the same, there is no meaningful second largest. Always check the problem rules before returning `size - 2` blindly.

### Time Complexity Note

| Approach | Rough cost | Why |
|---|---|---|
| Nested loops comparing many pairs | **O(n²)** | Two nested `for` loops over the list |
| One pass tracking largest / second largest | **O(n)** | Single loop |
| `sorted()` then read an index | **O(n log n)** | Built-in sort (often merge/quick sort internally) + O(1) index read |

Sorting is convenient and clear. A single-pass method can be faster for very large lists, but `sorted()` is a practical tool when you want an ordered view of the data.

---

## Practice Activity: Analyse, Then Code One Nested Problem

Analyse this pair problem before writing code.

**Problem statement:** Given `[2, 4, 6, 8]` and target `10`, return one pair that adds to `10`.

**Sample analysis:**

| Part | Answer |
|---|---|
| **Input** | List of numbers + target sum |
| **Output** | One valid pair, or empty if none |
| **Special cases** | Empty list; no pair exists |
| **Approach** | Index-based nested loops with early return |

**Algorithm steps:**

1. Store `n = len(nums)`.
2. Outer loop `i` from `0` to `n - 1`.
3. Inner loop `j` from `i + 1` to `n - 1`.
4. If sum equals target, return that pair immediately.
5. After all loops, return `[]`.

Then implement the function and run it locally with `python3`.

---

## Practice Activity: Run and Test on Local Machine

1. Open your practice folder in VS Code.
2. Create `intermediate_practice.py`.
3. Paste one nested-loop solution (common elements, pair sum, or even product) and the second-largest sorting solution.
4. Save the file.
5. Open Terminal inside VS Code.
6. Run `python3 intermediate_practice.py`.
7. Test with a normal list, a list with no matching pair, and a short list for second largest.

```python
# Quick local check for pair with sum
print(pair_with_sum([1, 2, 3, 4, 5], 7))  # Should print one valid pair
print(pair_with_sum([1, 2, 3], 100))  # Should print []
```

**How the code works:**

- Local testing helps you catch empty-result cases early.
- Running with `python3` keeps your workflow consistent with the previous lesson.

---

## Common Mistakes and Doubts

- **Skipping the plan:** Always write input, output, and whether you need one match or all matches.
- **Wrong nested loop range:** Start the inner loop at `i + 1` to avoid repeated pairs and self-pairs.
- **Early return too soon:** Use early return for “find one pair”; collect all pairs when the problem asks for every match.
- **Value loop when you need indexes:** Prefer `range` / `len` when the inner loop depends on `i + 1`.
- **Second largest edge cases:** If all numbers are equal, `size - 2` may not mean a true second distinct maximum — read the problem rules.
- **Forgetting sort cost:** `sorted()` is usually **O(n log n)**, not free.

When stuck, rewrite the problem as a table of input, output, and steps — then decide whether nested loops or sorting is the cleaner tool.

---

## Key Takeaways

- **Problem analysis** turns a word problem into safe steps before you open the editor.
- **Nested loops with indexes** solve list problems like common elements, pair with sum, and pair with product.
- **Early return vs collect-all** depends on whether the problem wants one answer or every valid pair.
- **`sorted()` + index `size - 2`** is a practical way to read the second largest value; its cost is about **O(n log n)**.
- Nested solutions are often **O(n²)**; knowing that helps you compare approaches in upcoming practice.

In the next lesson, you will continue strengthening structured problem-solving and move toward new application areas where clean logic and data handling matter even more.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| Problem analysis | Study input/output before coding | Write steps first |
| Nested loop | Loop inside another loop | `for i` then `for j` |
| Index-based loop | Loop with `range` and positions | `for i in range(n)` |
| Value-based loop | Loop over items directly | `for value in nums` |
| `range(i + 1, n)` | Inner loop after outer index | Unique pairs only |
| Early return | Stop after first valid answer | Pair with sum |
| Collect all pairs | Append matches, return at end | Even-product pairs |
| `product % 2 == 0` | Even product check | Pair filter |
| `is_even` flag | Switch even/odd product rule | Function argument |
| `sorted(nums)` | Built-in ascending sort | Second largest helper |
| `size - 2` | Second-last index after sort | Second largest value |
| O(n²) | Nested loop cost | Pair checks |
| O(n log n) | Typical built-in sort cost | `sorted()` |
| `python3 file.py` | Run Python file locally | `python3 practice.py` |
