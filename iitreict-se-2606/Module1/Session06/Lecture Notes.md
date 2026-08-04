# Sorting Algorithms – Bubble Sort & Selection Sort

## What You Will Learn in This Lesson

You have already learned Python's core **data structures** — **lists**, **strings**, **tuples**, **dictionaries**, and **sets**. You used **indexing**, **slicing**, **key–value** operations, and built-ins like **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, and **`sum()`** to work with in-memory data.

In this lesson, you will learn how sorting actually works under the hood using two beginner-friendly algorithms: **Bubble Sort** and **Selection Sort**. You will:

- Trace each algorithm **manually** on small arrays
- Implement both algorithms in **Python** (run them in **OneCompiler** or your usual editor)
- Analyse why both usually take **O(n²)** time
- Compare your custom sorts with Python's built-in **`sorted()`** and **`list.sort()`**

By the end, you will explain both algorithms, write their code, and know when a built-in sort is enough versus when learning the algorithm matters.

---

## What Is Sorting?

- **Official Definition:** **Sorting** is the process of arranging data in a specific order, usually ascending or descending.
- **In Simple Words:** Sorting means putting items in order — smallest to biggest, or A to Z.
- **Real-Life Example:** Arranging exam marks from lowest to highest, or arranging names alphabetically on an attendance sheet.

Sorting is useful because:

- Searching becomes easier after data is sorted.
- Reports and leaderboards look cleaner.
- Price filters and rankings depend on sorting.
- Many advanced algorithms expect sorted data as input.

An online shopping app can sort products by **price low to high**. A result portal can sort students by **marks high to low**. Sorting is a basic operation used in many real applications.

![Sorting in Python shown with exam marks, product prices, and student name cards moving from unsorted order to clean ascending order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-sorting-big-picture.png)

---

## Important Terms Before Sorting

- **Official Definition:** An **array/list** is a collection of values stored in order.
- **In Simple Words:** A list is like a row of boxes, where each box has one value.
- **Real-Life Example:** `[50, 20, 80, 10]` can represent marks of four students.

- **Official Definition:** An **index** is the position number of an item in a list. Python starts at `0`.
- **In Simple Words:** Index tells where an item sits.
- **Real-Life Example:** In `[50, 20, 80]`, index `0` has `50`, index `1` has `20`, and index `2` has `80`.

- **Official Definition:** A **swap** means exchanging the positions of two values.
- **In Simple Words:** Two values change places.
- **Real-Life Example:** If two students stand in the wrong order in a queue, they exchange places.

Sorting algorithms mainly repeat two actions: **compare** values and **swap** values when required.

---

## Bubble Sort Intuition

- **Official Definition:** **Bubble Sort** repeatedly compares adjacent items and swaps them if they are in the wrong order.
- **In Simple Words:** It checks two neighbours at a time. The bigger value slowly moves to the right — like a bubble rising to the top.
- **Real-Life Example:** Students standing by height — compare neighbours and swap if the taller one stands before the shorter one.

Bubble Sort works in **passes**:

- In each pass, nearby values are compared.
- If the left value is bigger than the right value, they are swapped.
- After the first full pass, the largest value reaches the last position.
- After the next pass, the second-largest value reaches its correct position.

This is easy to understand, but not very fast for large lists.

![Bubble Sort intuition where neighbouring number cards are compared and larger values move step by step toward the right side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-bubble-sort-intuition.png)

---

## Bubble Sort Trace

Let us sort this list in ascending order: `[5, 3, 4, 1]`

### Pass 1

| Comparison | Action | List After Action |
|---|---|---|
| Compare `5` and `3` | Swap | `[3, 5, 4, 1]` |
| Compare `5` and `4` | Swap | `[3, 4, 5, 1]` |
| Compare `5` and `1` | Swap | `[3, 4, 1, 5]` |

At the end of Pass 1, the largest value `5` has reached the last position.

### Pass 2

| Comparison | Action | List After Action |
|---|---|---|
| Compare `3` and `4` | No swap | `[3, 4, 1, 5]` |
| Compare `4` and `1` | Swap | `[3, 1, 4, 5]` |

At the end of Pass 2, `4` is also in its correct position.

### Pass 3

| Comparison | Action | List After Action |
|---|---|---|
| Compare `3` and `1` | Swap | `[1, 3, 4, 5]` |

Final sorted list: `[1, 3, 4, 5]`.

The important pattern: after each pass, one big value settles at the end.

---

## Bubble Sort Python Implementation

Open **OneCompiler** (Python) or your editor and run the code below.

```python
def bubble_sort(numbers):  # Define a function that receives a list
    n = len(numbers)  # Store the number of items in the list
    for pass_index in range(n - 1):  # Run passes from first to second-last item
        for i in range(n - 1 - pass_index):  # Compare only the unsorted part
            if numbers[i] > numbers[i + 1]:  # Check if neighbours are in wrong order
                temp = numbers[i]  # Store the left value before swapping
                numbers[i] = numbers[i + 1]  # Move the right value to the left
                numbers[i + 1] = temp  # Put the stored left value on the right
    return numbers  # Return the sorted list

marks = [5, 3, 4, 1]  # Create a sample list of numbers
sorted_marks = bubble_sort(marks)  # Call the function and store the result
print(sorted_marks)  # Display the sorted list — Output: [1, 3, 4, 5]
```

**How the code works:**

- `n = len(numbers)` counts how many values are present.
- The outer loop controls how many passes are needed.
- The inner loop compares neighbours like `numbers[i]` and `numbers[i + 1]`.
- If the left value is bigger, the code swaps both values.
- `n - 1 - pass_index` avoids checking values already settled at the end.

**Common doubt:** Why two loops? One loop is for passes; the other is for comparisons inside each pass.

---

## Bubble Sort With Trace Printing

Printing each pass helps you see what the algorithm is doing.

```python
def bubble_sort_trace(numbers):  # Define a function to sort and print each pass
    n = len(numbers)  # Store the length of the list
    for pass_index in range(n - 1):  # Run one pass at a time
        for i in range(n - 1 - pass_index):  # Compare neighbouring values
            if numbers[i] > numbers[i + 1]:  # Check if swap is needed
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Python swap shortcut
        print("After pass", pass_index + 1, ":", numbers)  # Show list after each pass
    return numbers  # Return the final sorted list

data = [7, 2, 5, 1]  # Create a sample list
bubble_sort_trace(data)  # Run the trace version of bubble sort
```

**How the code works:**

- The logic is the same as normal Bubble Sort.
- The `print()` line shows the list after each pass.
- Python allows a shortcut swap: `a, b = b, a`.
- Trace printing is useful for learning; real apps usually avoid too many prints.

---

## Selection Sort Intuition

- **Official Definition:** **Selection Sort** repeatedly selects the smallest item from the unsorted part and places it at the beginning.
- **In Simple Words:** Find the smallest remaining value and put it in the next correct position.
- **Real-Life Example:** Arranging currency notes from smallest to largest — pick the smallest note first, then the next smallest, and so on.

Selection Sort works in **positions**:

- Start at the first position.
- Find the smallest value in the remaining list.
- Swap that smallest value into the current position.
- Move to the next position and repeat.

After every pass, the left side of the list becomes sorted.

![Selection Sort intuition where the smallest value in the unsorted part is selected and placed into the next sorted position on the left](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-selection-sort-intuition.png)

---

## Selection Sort Trace

Let us sort the same list: `[5, 3, 4, 1]`

### Pass 1

- Current position is index `0`.
- Unsorted part is `[5, 3, 4, 1]`.
- Smallest value is `1` → swap `5` and `1`.
- List becomes `[1, 3, 4, 5]`.

### Pass 2

- Current position is index `1`.
- Unsorted part is `[3, 4, 5]`.
- Smallest value is `3` — already correct.
- List remains `[1, 3, 4, 5]`.

### Pass 3

- Current position is index `2`.
- Unsorted part is `[4, 5]`.
- Smallest value is `4` — already correct.
- Final list remains `[1, 3, 4, 5]`.

The important pattern: after each pass, one small value settles at the beginning.

---

## Selection Sort Python Implementation

```python
def selection_sort(numbers):  # Define a function that receives a list
    n = len(numbers)  # Store the number of items in the list
    for current_index in range(n - 1):  # Move through each position except the last
        min_index = current_index  # Assume current position has the smallest value
        for i in range(current_index + 1, n):  # Search the remaining unsorted part
            if numbers[i] < numbers[min_index]:  # Check if a smaller value is found
                min_index = i  # Update the index of the smallest value
        temp = numbers[current_index]  # Store the current value before swapping
        numbers[current_index] = numbers[min_index]  # Put the smallest value in place
        numbers[min_index] = temp  # Move the old current value to the old min position
    return numbers  # Return the sorted list

scores = [5, 3, 4, 1]  # Create a sample list of scores
sorted_scores = selection_sort(scores)  # Call the function and store the sorted list
print(sorted_scores)  # Display the sorted list — Output: [1, 3, 4, 5]
```

**How the code works:**

- `current_index` marks the position we are trying to fill.
- `min_index` stores the index of the smallest value found so far.
- The inner loop searches the unsorted part for a smaller value.
- After the inner loop ends, the smallest value is swapped into the current position.
- The sorted area grows from the left side.

**Common doubt:** Why does Selection Sort swap only once per pass? It first finds the smallest value, then swaps once after the search is complete.

---

## Bubble Sort vs Selection Sort

Both algorithms use nested loops, but their thinking is different.

| Point | Bubble Sort | Selection Sort |
|---|---|---|
| Main action | Compare neighbours | Find smallest remaining value |
| Direction of sorted part | Largest values settle on the right | Smallest values settle on the left |
| Swaps | Can swap many times in one pass | Usually swaps once per pass |
| Beginner intuition | Push big values to the end | Select the next smallest item |
| Time complexity | O(n²) | O(n²) |
| Extra space | O(1) | O(1) |

![Bubble Sort vs Selection Sort — Bubble Sort swaps neighbours until large values settle right; Selection Sort picks the smallest remaining value and places it on the left](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-03-bubble-vs-selection-sort.png?v=20260704)

Bubble Sort teaches adjacent comparison. Selection Sort teaches repeatedly choosing the best candidate for the next position.

---

## Manual Tracing Method

- **Official Definition:** **Tracing** means manually following an algorithm step by step to see how values change.
- **In Simple Words:** Tracing is like dry-running the code on paper before trusting the computer.
- **Real-Life Example:** Before submitting a maths answer, you check every step again.

When tracing sorting algorithms:

- Write the starting list clearly.
- Mark which part is sorted and which part is unsorted.
- Write every comparison and every swap.
- Write the list after each pass.

### Activity: Trace Bubble Sort

Trace Bubble Sort on `[6, 2, 8, 4]`. Use this format:

| Pass | Comparisons Made | List After Pass |
|---|---|---|
| Pass 1 | Fill this yourself | Fill this yourself |
| Pass 2 | Fill this yourself | Fill this yourself |
| Pass 3 | Fill this yourself | Fill this yourself |

Expected final sorted list: `[2, 4, 6, 8]`.

### Activity: Trace Selection Sort

Trace Selection Sort on `[9, 1, 7, 3]`. Use this format:

| Pass | Smallest Value Found | List After Pass |
|---|---|---|
| Pass 1 | Fill this yourself | Fill this yourself |
| Pass 2 | Fill this yourself | Fill this yourself |
| Pass 3 | Fill this yourself | Fill this yourself |

Expected final sorted list: `[1, 3, 7, 9]`.

---

## Complexity Analysis — Why O(n²)?

- **Official Definition:** **Time complexity** describes how running time grows when input size grows.
- **In Simple Words:** It tells how much slower the algorithm becomes when the list gets bigger.
- **Real-Life Example:** Checking one student's marks is quick. Comparing every student with many others becomes slow when the class grows.

Both Bubble Sort and Selection Sort use nested loops. For a list of `n` items:

- The outer loop runs around `n` times.
- The inner loop also runs around `n` times.
- Rough work becomes `n × n` — that is why both are called **O(n²)** algorithms.

![Manual tracing connected to O(n squared) work, showing comparison checks growing with input size and O(1) extra space](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-complexity-tracing.png)

| Number of Items | Rough Comparisons |
|---|---|
| 5 | Around 25 |
| 10 | Around 100 |
| 100 | Around 10,000 |
| 1,000 | Around 1,000,000 |

This table is not exact counting — it helps you feel the growth pattern.

### Space Complexity

- **Official Definition:** **Space complexity** describes how much extra memory an algorithm needs as input size grows.
- **In Simple Words:** Does it need a big extra shelf, or can it rearrange books on the same shelf?
- **Real-Life Example:** Rearranging books on the same shelf needs little extra space; copying all books to a new shelf needs more.

Both algorithms use **O(1)** extra space — they sort inside the same list and only use a few variables like `temp`, `i`, or `min_index`.

---

## Activity: Count Comparisons Manually

Use the list `[4, 1, 3, 2]` and count comparisons for each algorithm.

### Bubble Sort Comparison Count

For basic Bubble Sort with `4` items: Pass 1 → 3 pairs, Pass 2 → 2 pairs, Pass 3 → 1 pair. Total = `3 + 2 + 1 = 6`.

| Pass | List After Pass |
|---|---|
| Start | `[4, 1, 3, 2]` |
| Pass 1 | `[1, 3, 2, 4]` |
| Pass 2 | `[1, 2, 3, 4]` |
| Pass 3 | `[1, 2, 3, 4]` |

### Selection Sort Comparison Count

For Selection Sort with `4` items: also `3 + 2 + 1 = 6` comparisons.

| Pass | Smallest Selected | List After Pass |
|---|---|---|
| Start | — | `[4, 1, 3, 2]` |
| Pass 1 | `1` | `[1, 4, 3, 2]` |
| Pass 2 | `2` | `[1, 2, 3, 4]` |
| Pass 3 | `3` | `[1, 2, 3, 4]` |

Same comparison count here, different movement style: neighbours vs selecting the minimum.

---

## Comparing Custom Sorts with `sorted()` and `list.sort()`

You already used **`sorted()`** on collections. Now connect that to what you just built.

- **Official Definition:** **`sorted(iterable)`** returns a **new sorted list** and leaves the original unchanged. **`list.sort()`** sorts the list **in place** and returns **`None`**.
- **In Simple Words:** `sorted()` gives you a fresh arranged copy. `list.sort()` rearranges the same list.
- **Real-Life Example:** `sorted()` is like photocopying your notebook pages in order and keeping the messy original. `list.sort()` is like rearranging the original pages themselves.

```python
def bubble_sort(numbers):  # Custom Bubble Sort — sorts in place
    n = len(numbers)  # Count items
    for pass_index in range(n - 1):  # Outer passes
        for i in range(n - 1 - pass_index):  # Neighbour comparisons
            if numbers[i] > numbers[i + 1]:  # Wrong order?
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap
    return numbers  # Return same list, now sorted

marks = [8, 3, 5, 2]  # Original sample data
print("sorted():", sorted(marks))  # New list — Output: [2, 3, 5, 8]
print("Original after sorted():", marks)  # Still [8, 3, 5, 2]

copy_for_bubble = marks.copy()  # Keep original safe
print("bubble_sort():", bubble_sort(copy_for_bubble))  # Output: [2, 3, 5, 8]

marks_for_sort = [8, 3, 5, 2]  # Fresh list for list.sort()
result = marks_for_sort.sort()  # Sorts in place
print("list.sort() return:", result)  # Output: None
print("List after list.sort():", marks_for_sort)  # Output: [2, 3, 5, 8]
```

**How the code works:**

- **`sorted(marks)`** and **`bubble_sort(copy)`** both produce `[2, 3, 5, 8]`, but built-in sorting is much faster for large data.
- **`list.sort()`** returns **`None`** — always print the list after calling it, not the return value.
- Custom Bubble/Selection Sort teach **how** sorting works; for real projects, prefer **`sorted()`** or **`list.sort()`**.

| Tool | Changes Original? | Returns | Best Use |
|------|-------------------|---------|----------|
| **`sorted(x)`** | No | New sorted list | Keep original + get ordered copy |
| **`list.sort()`** | Yes | `None` | Sort this list and keep it |
| **Bubble / Selection** | Yes (typical) | Sorted list | Learning algorithms and tracing |

### Quick Activity: Same Input, Three Ways

In OneCompiler, run Bubble Sort, Selection Sort, and `sorted()` on `[8, 3, 5, 2]` and confirm all three agree on `[2, 3, 5, 8]`.

```python
def bubble_sort(numbers):  # Custom Bubble Sort for the activity
    n = len(numbers)  # Count items
    for pass_index in range(n - 1):  # Outer passes
        for i in range(n - 1 - pass_index):  # Neighbour comparisons
            if numbers[i] > numbers[i + 1]:  # Wrong order?
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap
    return numbers  # Return sorted list

def selection_sort(numbers):  # Custom Selection Sort
    n = len(numbers)  # Count items
    for current_index in range(n - 1):  # Fill each position
        min_index = current_index  # Assume current is smallest
        for i in range(current_index + 1, n):  # Search remaining
            if numbers[i] < numbers[min_index]:  # Found smaller?
                min_index = i  # Remember its index
        numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]  # One swap
    return numbers  # Return sorted list

data = [8, 3, 5, 2]  # Shared sample
print("Bubble:", bubble_sort(data.copy()))  # Custom algorithm
print("Selection:", selection_sort(data.copy()))  # Custom algorithm
print("Built-in:", sorted(data))  # Python built-in
print("Original still:", data)  # Output: [8, 3, 5, 2] — copy protected it
```

**How the code works:**

- **`data.copy()`** keeps the original list safe while custom sorts rearrange their own copies.
- All three approaches should print the same ordered values.
- Prefer built-ins for real tasks; prefer custom sorts when the goal is understanding steps.

---

## Common Mistakes and Doubts

- **Changing the original list:** These implementations sort the list passed in. If you need the original later, pass **`numbers.copy()`**.
- **Wrong loop range:** Going till `n` while checking `numbers[i + 1]` can cause an **`IndexError`**.
- **Confusing pass and comparison:** A pass contains many comparisons — they are not the same thing.
- **Thinking O(n²) means exactly n² comparisons:** Big-O explains growth pattern, not exact step count.
- **Printing `list.sort()` return value:** It is always **`None`** — print the list itself.
- **Mixing Bubble and Selection movement:** Bubble pushes large values **right**; Selection places small values **left**.
- **Forgetting to trace:** Sorting code is much easier when you first trace small lists on paper.

When in doubt, use a small list like `[4, 2, 1]` and write each pass on paper in OneCompiler with print-after-pass versions.

### Quick Check on Paper

For `[3, 1, 2]`, write the list after Pass 1 of Bubble Sort and after Pass 1 of Selection Sort. Confirm Bubble ends Pass 1 with `3` at the end, and Selection ends Pass 1 with `1` at the start.

---

## Key Takeaways

- **Bubble Sort** compares neighbouring values and pushes larger values toward the end.
- **Selection Sort** repeatedly selects the smallest remaining value and places it at the next correct position.
- Manual **tracing** and comparison counting connect clearly to **O(n²)** time and **O(1)** extra space.
- Python's **`sorted()`** and **`list.sort()`** give the same ordered result much more efficiently — use them in practice; use custom sorts to understand the idea.
- These skills prepare you for harder problem-solving where nested loops, ordered data, and algorithm choice matter together.

---

## Important Commands, Libraries, and Terminologies

| Term / Syntax | Meaning |
|---|---|
| **Sorting** | Arranging data in a chosen order |
| **Bubble Sort** | Sort by comparing and swapping adjacent values |
| **Selection Sort** | Sort by selecting the smallest remaining value each pass |
| **Pass** | One full outer-loop round of algorithm work |
| **Comparison / Swap** | Checking two values / exchanging two values |
| **Trace** | Manual dry run of steps on paper or with prints |
| **`range()` / `len()`** | Loop bounds / count of list items |
| **O(n²)** | Work grows roughly like n × n (nested loops) |
| **O(1) space** | Constant extra memory — sort inside the same list |
| **`sorted(x)`** | Returns a new sorted list; original unchanged |
| **`list.sort()`** | Sorts list in place; returns `None` |
| **`list.copy()`** | Shallow copy so the original stays safe |
| **OneCompiler** | Online Python environment to run and test sorting code |
