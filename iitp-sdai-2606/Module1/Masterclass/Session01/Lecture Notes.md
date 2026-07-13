# Masterclass: Searching Algorithms – Binary Search

## What You Will Learn in This Lesson

In earlier lessons, you arranged lists using sorting algorithms such as **Bubble Sort** and **Selection Sort**. You also saw that once data is in order, finding a value becomes much easier than scanning randomly.

Today we move from **sorting** to **searching**. You will learn a fast method called **Binary Search** that works only on **sorted** data and often finishes in far fewer steps than checking every item one by one.

In this lesson, you will learn:

- Why **sorted data** is a must for binary search
- How binary search **halves** the search space each step
- How to write **iterative binary search** in Python
- Why time complexity is **O(log n)** and space complexity is **O(1)**
- How to **trace** every step on paper and solve simple search problems

By the end, you will be able to implement binary search, explain its speed in plain words, and apply it confidently on sorted lists.

---

## Why Searching Matters

Every day, software looks for something in a collection: a roll number in a result list, a product code in inventory, or a word in a dictionary.

- **Official Definition:** **Searching** is the process of finding whether a target value exists in a collection and, if it does, locating its position.
- **In Simple Words:** Searching means "Is this item present? If yes, where?"
- **Real-Life Example:** Finding your name in a sorted attendance sheet is searching. Finding a train number on the IRCTC list is also searching.

**Why we need smarter search:** If a list has one lakh students and you check each name from the start, it can take a long time. Binary search is designed for situations where the list is already sorted and you want fewer checks.

**Common doubt:** "If I can use a `for` loop, why learn binary search?"  
A loop that checks every item is fine for tiny lists. For large sorted lists, binary search can find the answer in roughly the number of times you can cut the list in half — often a handful of steps instead of thousands.

![Searching shown as finding a name on a sorted attendance sheet, opening a dictionary near the middle, and looking up a train ticket — ask if it exists and where](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session01/masterclass01-01-searching-matters.png?v=20260713)

---

## Linear Search: The Slow but Simple Baseline

Before binary search, meet the simplest approach so the improvement feels clear.

- **Official Definition:** **Linear Search** (also called sequential search) checks each element from start to end until the target is found or the list ends.
- **In Simple Words:** You look at the first box, then the second, then the third — one by one.
- **Real-Life Example:** Searching for your pen by opening every drawer from left to right without any order.

```python
# Full linear search example for comparison
def linear_search(numbers, target):  # Define a function that takes a list and the value to find
    for index in range(len(numbers)):  # Visit every index from 0 to last
        if numbers[index] == target:  # Check if the current value matches the target
            return index  # Return the position as soon as we find a match
    return -1  # If the loop finishes with no match, return -1 as "not found"


marks = [12, 45, 67, 89, 90]  # Sample list of marks (order does not matter for linear search)
print(linear_search(marks, 67))  # Expected output: 2 (because 67 is at index 2)
print(linear_search(marks, 50))  # Expected output: -1 (50 is not in the list)
```

**How the code works:**

- The function walks through every index using a `for` loop
- As soon as `numbers[index]` equals `target`, it returns that index
- If nothing matches, it returns `-1`
- In the worst case, it checks **all** `n` items → time complexity **O(n)**

**Activity — Count the checks:**  
Take the list `[10, 20, 30, 40, 50, 60, 70, 80]`. Mentally use linear search to find `80`. How many comparisons did you need? Write the number in your notebook. (Answer: **8** if you check from the left.)

Linear search is honest and simple. Binary search is smarter — but only when the list is sorted.

---

## Prerequisite: Sorted Data

Binary search is not magic. It has one hard rule: the collection must already be **sorted** (usually ascending, smallest to largest).

- **Official Definition:** A list is **sorted in ascending order** when each element is less than or equal to the next element.
- **In Simple Words:** Numbers go from small to big, like a staircase going up.
- **Real-Life Example:** Roll numbers `[1, 3, 5, 8, 12]` are sorted. Marks `[90, 40, 70]` are not sorted.

**Why sorting is required:** Binary search always looks at the **middle** value and decides whether the target lies on the **left half** or the **right half**. That decision is correct only if left values are smaller and right values are larger (for ascending order).

![Sorted ascending number cards ready for binary search contrasted with a messy unsorted row that is not safe to search this way](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session01/masterclass01-02-sorted-prerequisite.png?v=20260713)

**Common mistake:** Running binary search on an unsorted list. The code may return a wrong index or say "not found" even when the value exists.

**Quick check:**

| List | Sorted? | Safe for binary search? |
|---|---|---|
| `[2, 5, 9, 14, 21]` | Yes | Yes |
| `[21, 14, 9, 5, 2]` | Descending | Only if you reverse the comparison logic |
| `[9, 2, 14, 5]` | No | No — sort first |

**Activity — Spot the unsafe list:**  
Which of these is **not** ready for normal ascending binary search?  
A) `[1, 4, 7, 10]`  
B) `[3, 8, 2, 9]`  
C) `[11, 22, 33]`  
Write A, B, or C. (Answer: **B**)

Once the list is sorted, you are ready for the main idea: **divide and conquer by half**.

---

## How Binary Search Works

Imagine a thick dictionary. You do not start at page 1 for every word. You open near the middle, see whether your word comes earlier or later, and throw away half the book. That is binary search.

- **Official Definition:** **Binary Search** repeatedly compares the target with the middle element of the current search range and discards half of the remaining elements each time, until the target is found or the range becomes empty.
- **In Simple Words:** Check the middle. Keep only the useful half. Repeat.
- **Real-Life Example:** Guessing a number from 1 to 100. If someone says "higher" or "lower" after each guess, you cut the remaining range roughly in half each time.

![Binary search intuition: check the middle value, discard the useless half, then repeat until the target is found](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session01/masterclass01-03-binary-halving.png?v=20260713)

### The three pointers

Binary search usually tracks three positions:

| Name | Meaning | Simple picture |
|---|---|---|
| **`low`** | Left end of the current search range | Start of the remaining row |
| **`high`** | Right end of the current search range | End of the remaining row |
| **`mid`** | Middle index between `low` and `high` | The seat you check now |

### Step-by-step logic (ascending list)

1. Set `low = 0` and `high = last index`.
2. While `low <= high`:
   - Compute `mid = (low + high) // 2` (integer mid index).
   - If `arr[mid] == target`, return `mid` (found).
   - If `arr[mid] < target`, the target (if present) is on the **right** → set `low = mid + 1`.
   - If `arr[mid] > target`, the target (if present) is on the **left** → set `high = mid - 1`.
3. If the loop ends, return `-1` (not found).

**Logic to remember:** Every wrong middle answer throws away about half the remaining work. That is why binary search feels so fast on big sorted lists.

**Common doubt:** "What if there are two same values?"  
Classic binary search returns **one** valid index where the value matches. Finding the *first* or *last* occurrence needs a small variation you may learn in a future lesson. For this lesson, finding any matching index is enough.

**Activity — Number-guessing warm-up:**  
Think of a secret number from `1` to `50`. In your notebook, pretend a friend always answers "too low" or "too high." Write your guesses so each guess cuts the remaining range roughly in half. Count how many guesses you needed. Most careful strategies finish in about **6** guesses — that feeling is binary search.

---

## Trace: Finding a Value by Hand

Tracing means acting like the computer on paper. This builds confidence before coding.

**Example list (already sorted):**  
`arr = [3, 8, 15, 20, 27, 35, 42]`  
**Target:** `27`

![Binary search trace with low, mid, and high pointers on a sorted array, moving right when mid is too small until 27 is found](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session01/masterclass01-04-trace-pointers.png?v=20260713)

| Step | low | high | mid | arr[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 20 | 20 < 27 → go right → `low = 4` |
| 2 | 4 | 6 | 5 | 35 | 35 > 27 → go left → `high = 4` |
| 3 | 4 | 4 | 4 | 27 | Equal → **found at index 4** |

Only **3** comparisons. Linear search from the left would need **5** comparisons to reach `27`.

**Second trace — value missing:**  
Same list, target `16`.

| Step | low | high | mid | arr[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 20 | 20 > 16 → go left → `high = 2` |
| 2 | 0 | 2 | 1 | 8 | 8 < 16 → go right → `low = 2` |
| 3 | 2 | 2 | 2 | 15 | 15 < 16 → go right → `low = 3` |
| Stop | 3 | 2 | — | — | `low > high` → **not found (`-1`)** |

**Activity — Trace on your own:**  
List: `[5, 10, 15, 20, 25, 30, 35, 40]`  
Target: `10`  
Fill a small table with `low`, `high`, `mid`, `arr[mid]`, and decision until you find the index. (Expected final answer: index **1**)

Tracing teaches you that binary search is a calm loop of **compare → shrink → repeat**.

---

## Iterative Binary Search in Python

**Iterative** means we use a `while` loop instead of a function calling itself.

- **Official Definition:** An **iterative binary search** implements the binary search algorithm using a loop that updates `low` and `high` until the target is found or the range is empty.
- **In Simple Words:** Keep looping and adjusting the borders until you succeed or give up.
- **Real-Life Example:** Narrowing a train seat search on a printed chart by repeatedly folding the chart in half — no recursion, just repeated folding.

```python
# Iterative binary search on a sorted list (ascending order)
def binary_search(arr, target):  # Define a function that accepts a sorted list and the value to find
    low = 0  # Start searching from the first index
    high = len(arr) - 1  # Start searching up to the last index

    while low <= high:  # Continue while there is still a valid search range
        mid = (low + high) // 2  # Pick the middle index using integer division
        if arr[mid] == target:  # Check if the middle value is exactly the target
            return mid  # Return the found index immediately
        elif arr[mid] < target:  # If middle value is smaller, target must be on the right side
            low = mid + 1  # Move the left border just after mid
        else:  # Otherwise middle value is larger, so target must be on the left side
            high = mid - 1  # Move the right border just before mid

    return -1  # If the loop ends, the target is not present in the list


# Demo with a sorted list of product prices
prices = [99, 199, 299, 399, 499, 599, 699]  # Sorted ascending prices in rupees
print(binary_search(prices, 399))  # Expected output: 3
print(binary_search(prices, 450))  # Expected output: -1
print(binary_search(prices, 99))  # Expected output: 0
print(binary_search(prices, 699))  # Expected output: 6
```

**How the code works:**

- `low` and `high` mark the current window of indices still under consideration
- `mid` is always calculated with `//` so the index stays a whole number
- Equality means success; smaller middle means search right; larger middle means search left
- Returning `-1` is a common convention for "not found"
- The function never creates a new list — it only moves two integer borders

**Common mistakes to avoid:**

- Using `/` instead of `//` for `mid` (can create a float index and crash)
- Writing `while low < high` instead of `while low <= high` (may miss a single remaining element)
- Forgetting `mid + 1` / `mid - 1` and creating an infinite loop
- Passing an unsorted list and trusting the result

**Activity — Run and predict:**  
Before running, predict the outputs for:

```python
nums = [2, 4, 6, 8, 10]
print(binary_search(nums, 8))
print(binary_search(nums, 7))
```

Write your predictions, then run the function. (Expected: `3`, then `-1`)

---

## Time Complexity: Why O(log n)?

Complexity tells us how work grows when the input size grows. Binary search's speed story is the heart of this masterclass.

- **Official Definition:** **Time complexity** describes how the number of operations grows as the input size `n` grows, usually written with Big-O notation.
- **In Simple Words:** It answers, "If the list becomes much longer, how much slower does the algorithm get?"
- **Real-Life Example:** If doubling the crowd at a ticket window roughly doubles your wait, that feels like **O(n)**. If each question cuts the remaining queue in half, that feels closer to **O(log n)**.

### What is log n here?

In computer science, **log n** (for binary search) usually means: how many times can you divide `n` by 2 until you reach about 1?

| n (list size) | Rough max comparisons in binary search |
|---|---|
| 8 | about 3 |
| 16 | about 4 |
| 1,000 | about 10 |
| 1,000,000 | about 20 |

![Side-by-side comparison of slow linear search checking items one by one versus fast binary search that halves the range and finishes in few steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session01/masterclass01-05-complexity-logn.png?v=20260713)

Notice the pattern: even for one million items, binary search often needs only around **20** checks. Linear search might need up to **one million** checks in the worst case.

**Why O(log n) is correct:**

- Each successful "wrong mid" decision removes about half the remaining elements
- The remaining size follows roughly: `n → n/2 → n/4 → n/8 → ... → 1`
- The number of halvings is proportional to **log₂(n)**
- Therefore worst-case time complexity is **O(log n)**

**Best case:** Target is at the first mid → **O(1)**  
**Average / worst case for binary search:** **O(log n)**

**Activity — Feel the growth:**  
If a sorted list has `32` items, about how many binary search steps are needed in the worst case?  
Hint: `32 → 16 → 8 → 4 → 2 → 1`. Count the cuts. (Answer: about **5**)

Compared with Bubble Sort or Selection Sort at **O(n²)**, binary search is searching — not sorting — and it is dramatically faster once sorting is already done.

---

## Space Complexity: O(1)

Speed is not the only cost. Memory also matters.

- **Official Definition:** **Space complexity** measures the extra memory an algorithm needs relative to the input size.
- **In Simple Words:** Besides the original list, how many extra boxes does the method need?
- **Real-Life Example:** Searching a printed timetable with only your finger as a bookmark uses almost no extra paper. That is like **O(1)** extra space.

In iterative binary search we mainly store:

- `low`
- `high`
- `mid`

These are a few integers. Their count does **not** grow when the list grows from 100 items to 1,00,000 items.

**Result:** Extra space is **O(1)** (constant space).

**Why this matters:** On large datasets, an algorithm that needs a full extra copy of the list can waste memory. Iterative binary search keeps memory light because it only moves pointers.

**Common doubt:** "Does the list itself count as O(n) space?"  
Yes, the input list occupies memory, but when we say binary search uses **O(1)** space, we mean **extra** space beyond the given input.

---

## Binary Search vs Linear Search (Quick Compare)

| Point | Linear Search | Binary Search |
|---|---|---|
| Needs sorted data? | No | Yes |
| Typical time | O(n) | O(log n) |
| Extra space (iterative) | O(1) | O(1) |
| Easy to code? | Very easy | Slightly more careful with borders |
| Best when | List is small or unsorted | List is large and already sorted |

**Choosing wisely:** If you will search many times on the same data, sorting once and then using binary search can be a strong plan. If you search only once on a tiny unsorted list, linear search may be enough.

---

## Problem Solving with Binary Search

Algorithms become useful when you apply them to real questions. Below are beginner problems you can solve with the same iterative idea.

### Problem 1: Find a roll number

```python
# Problem: Check if a roll number exists in a sorted class list
def find_roll_number(roll_numbers, query):  # Function to search one roll number
    low = 0  # Left border starts at first index
    high = len(roll_numbers) - 1  # Right border starts at last index

    while low <= high:  # Keep searching while range is valid
        mid = (low + high) // 2  # Calculate middle index
        if roll_numbers[mid] == query:  # Found the exact roll number
            return True  # Return True for "present"
        elif roll_numbers[mid] < query:  # Mid value is smaller than query
            low = mid + 1  # Search the right half
        else:  # Mid value is larger than query
            high = mid - 1  # Search the left half

    return False  # Loop ended without a match


class_rolls = [101, 104, 109, 112, 118, 125]  # Sorted roll numbers
print(find_roll_number(class_rolls, 112))  # Expected: True
print(find_roll_number(class_rolls, 110))  # Expected: False
```

**How the code works:**

- Same binary search logic, but returns `True` / `False` instead of an index
- Useful when the caller only cares about presence, not position

### Problem 2: Find the index of a score

Here the list of scores is sorted and each score appears only once. Your job is to return the index of the target score, or `-1` if it is missing.

```python
# Problem: Return index of a target score in a sorted unique score list
def find_score_index(scores, target_score):  # Search for one score and return its index
    low = 0  # Initialise left border
    high = len(scores) - 1  # Initialise right border

    while low <= high:  # Continue until range collapses
        mid = (low + high) // 2  # Middle candidate index
        if scores[mid] == target_score:  # Exact match found
            return mid  # Return that index to the caller
        if scores[mid] < target_score:  # Target is larger than mid value
            low = mid + 1  # Discard left side including mid
        else:  # Target is smaller than mid value
            high = mid - 1  # Discard right side including mid

    return -1  # Target score is not in the list


scores = [35, 48, 56, 67, 72, 88, 95]  # Sorted unique scores
print(find_score_index(scores, 72))  # Expected: 4
print(find_score_index(scores, 50))  # Expected: -1
```

**How the code works:**

- Identical border movement as the core algorithm
- Returns the index so you can later print the student at that position

### Problem 3: Empty list and single-element edge cases

Good problem solvers always test edges.

```python
# Edge-case checks for iterative binary search
def binary_search(arr, target):  # Reuse the standard iterative binary search
    low = 0  # Left border
    high = len(arr) - 1  # Right border; becomes -1 if list is empty

    while low <= high:  # For empty list, 0 <= -1 is False, so loop never runs
        mid = (low + high) // 2  # Safe mid calculation for non-empty ranges
        if arr[mid] == target:  # Found target
            return mid  # Return index
        elif arr[mid] < target:  # Need right half
            low = mid + 1  # Move left border
        else:  # Need left half
            high = mid - 1  # Move right border

    return -1  # Not found (also covers empty list)


print(binary_search([], 5))  # Expected: -1 (empty list)
print(binary_search([7], 7))  # Expected: 0 (single matching element)
print(binary_search([7], 3))  # Expected: -1 (single non-matching element)
```

**How the code works:**

- Empty list: `high` starts as `-1`, so the `while` condition fails immediately
- One element: `low` and `high` both start at `0`, so exactly one mid is checked

**Activity — Solve this mini problem:**  
Sorted bus fares: `[15, 20, 25, 30, 40, 50]`  
Write (on paper) the `low` / `high` / `mid` values for searching fare `40`.  
Then confirm with the Python function. (Expected index: **4**)

---

## Full Practice: Build, Trace, and Analyse Together

Use this as a short end-to-end drill.

```python
# Complete practice script: iterative binary search + simple analysis helper
def binary_search_with_trace(arr, target):  # Binary search that also prints each step
    low = 0  # Start of current range
    high = len(arr) - 1  # End of current range
    steps = 0  # Counter for number of comparisons / loop rounds

    while low <= high:  # Keep going while range is valid
        steps = steps + 1  # Count this round
        mid = (low + high) // 2  # Compute middle index
        print("Step", steps, ": low =", low, ", high =", high, ", mid =", mid, ", value =", arr[mid])  # Show the current state
        if arr[mid] == target:  # Check for a hit
            print("Found at index", mid, "in", steps, "step(s)")  # Announce success
            return mid  # Return found index
        elif arr[mid] < target:  # Target is larger
            low = mid + 1  # Shrink from the left
        else:  # Target is smaller
            high = mid - 1  # Shrink from the right

    print("Not found after", steps, "step(s)")  # Announce failure with step count
    return -1  # Standard not-found result


data = [4, 9, 13, 18, 22, 27, 31, 36, 40]  # Sorted practice list
binary_search_with_trace(data, 27)  # Trace a successful search
binary_search_with_trace(data, 21)  # Trace an unsuccessful search
```

**How the code works:**

- Same binary search logic, plus `print` statements for learning
- `steps` helps you see why large `n` still needs only a few rounds
- Run both calls and notice how quickly the range collapses

**Activity — Notebook summary:**  
After running the script, write three lines in your notes:

1. One sentence defining binary search
2. The prerequisite it needs
3. Its time and space complexity

---

## Key Takeaways

- **Binary Search** finds a target in a **sorted** list by repeatedly checking the middle and discarding half the remaining range.
- The **iterative** Python version uses `low`, `high`, and `mid` inside a `while low <= high` loop and usually returns an index or `-1`.
- Worst-case time complexity is **O(log n)** because each step halves the search space; iterative extra space is **O(1)**.
- Always **trace** on paper for found and not-found cases, and test edge cases like empty lists and single-element lists.
- Once you are comfortable with this searching pattern, you can connect it to larger problem-solving habits: sort when needed, choose the right search strategy, and explain complexity clearly in interviews and projects.

---

## Important Commands, Libraries, Terminologies Used

| Term / Idea | Meaning (quick revision) |
|---|---|
| **Searching** | Finding whether a value exists and where it is |
| **Linear Search** | Check items one by one from start to end; O(n) time |
| **Binary Search** | Search by repeatedly checking mid and discarding half; needs sorted data |
| **Sorted data** | List arranged in ascending (or consistent) order |
| **Iterative** | Implemented with a loop (`while`), not recursion |
| **`low` / `high` / `mid`** | Left border, right border, and middle index of current range |
| **`//`** | Integer division in Python (needed for mid index) |
| **`-1` return** | Common signal for "not found" |
| **Time complexity O(log n)** | Work grows with how many times `n` can be halved |
| **Space complexity O(1)** | Extra memory stays constant for iterative binary search |
| **Trace** | Step-by-step dry run on paper before or while coding |
| **Edge case** | Special inputs such as empty list or one-element list |
