# Sorting Algorithms - Bubble Sort & Selection Sort

## What You Will Learn in This Lesson

You have already learned how to write reusable **functions** and divide a program into smaller logical parts. That idea is very useful now because sorting algorithms are easier to understand when each algorithm is written as a separate function.

In this lesson, you will learn two beginner-friendly sorting algorithms: **Bubble Sort** and **Selection Sort**. You will trace them manually, implement them in Python, and understand why both usually take **O(n^2)** time for a list of `n` items.

You may wonder why we study Bubble Sort and Selection Sort when Python already has fast built-in sorting. The main reason is to build **coding intuition** — once you understand how these simple algorithms work step by step, you can think more clearly about loops, comparisons, swaps, and how code behaves on real data.

By the end, you will be able to explain how both algorithms work, write their Python code, trace their steps on sample arrays, and compare their time and space complexity.

---

## What Is Sorting?

- **Official Definition:** **Sorting** is the process of arranging data in a specific order, usually ascending or descending.
- **In Simple Words:** Sorting means putting items in order, like smallest to biggest or A to Z.
- **Real-Life Example:** Arranging students in a line from shortest to tallest, or arranging exam marks from lowest to highest.

Sorting is useful because:

- Reports look cleaner and more readable.
- Rankings, leaderboards, and price filters depend on sorting.
- Many advanced algorithms expect sorted data as input.

**Important point:** Sorting works on a **list or collection** of items, not on a single value. If you have only one number like `4`, there is nothing to rearrange. You need multiple values — such as `[5, 1, 4, 2, 8]` — to perform sorting.

Sorting is not limited to numbers. The same comparison-and-swap logic also works on **strings** and other comparable data types.

Python and most programming languages provide built-in sorting that runs much faster (around **O(n log n)**). Bubble Sort and Selection Sort are taught first because they are easy to trace and help you understand how sorting logic is built from basic steps.

![Sorting in Python shown with exam marks, product prices, and student name cards moving from unsorted order to clean ascending order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-sorting-big-picture.png)

---

## What Is an Algorithm?

Before we write code, it helps to understand what an **algorithm** means in sorting.

- **Official Definition:** An **algorithm** is a clear series of steps used to solve a problem.
- **In Simple Words:** An algorithm is like a route map — step 1, step 2, step 3 — that takes you from the starting point to the goal.
- **Real-Life Example:** Going from home to office: go straight, take a right, then a left, then stop. That route is an algorithm for reaching the office.

For sorting, we first write the steps in plain language, then trace them on a sample list, and only then convert those steps into Python code.

---

## Important Terms Before Sorting

Before learning the algorithms, let us understand a few words that will appear again and again.

- **Official Definition:** An **array/list** is a collection of values stored in order.
- **In Simple Words:** A list is like a row of boxes, where each box has one value.
- **Real-Life Example:** `[50, 20, 80, 10]` can represent marks of four students.

- **Official Definition:** An **index** is the position number of an item in a list.
- **In Simple Words:** Index tells where an item is stored. Python starts counting from `0`.
- **Real-Life Example:** In `[50, 20, 80]`, index `0` has `50`, index `1` has `20`, and index `2` has `80`.

- **Official Definition:** A **swap** means exchanging the positions of two values.
- **In Simple Words:** Swap means two values change places.
- **Real-Life Example:** If two students are standing in the wrong order in a queue, they can exchange places.

Sorting algorithms mainly repeat two actions: **compare** values and **swap** values when required.

---

## Bubble Sort Intuition

- **Official Definition:** **Bubble Sort** is a sorting algorithm that repeatedly compares adjacent items and swaps them if they are in the wrong order.
- **In Simple Words:** Bubble Sort checks two neighbours at a time. The bigger value slowly moves to the right side, like a bubble rising to the top.
- **Real-Life Example:** Imagine students standing in a line by height. You compare two students standing next to each other and swap them if the taller one is before the shorter one.

Bubble Sort works in **passes**:

- In each pass, nearby values are compared.
- If the left value is bigger than the right value, they are swapped.
- After the first full pass, the largest value reaches the last position.
- After the next pass, the second-largest value reaches its correct position.

This is easy to understand, but not very fast for large lists.

![Bubble Sort intuition where neighbouring number cards are compared and larger values move step by step toward the right side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-bubble-sort-intuition.png)

---

## Bubble Sort Trace

Let us sort this list in ascending order — the same example used in the live session:

`[5, 1, 4, 2, 8]`

### Pass 1

| Comparison | Action | List After Action |
|---|---|---|
| Compare `5` and `1` | Swap | `[1, 5, 4, 2, 8]` |
| Compare `5` and `4` | Swap | `[1, 4, 5, 2, 8]` |
| Compare `5` and `2` | Swap | `[1, 4, 2, 5, 8]` |
| Compare `5` and `8` | No swap | `[1, 4, 2, 5, 8]` |

At the end of Pass 1, the largest value `8` has reached the last position.

### Pass 2

| Comparison | Action | List After Action |
|---|---|---|
| Compare `1` and `4` | No swap | `[1, 4, 2, 5, 8]` |
| Compare `4` and `2` | Swap | `[1, 2, 4, 5, 8]` |
| Compare `4` and `5` | No swap | `[1, 2, 4, 5, 8]` |

At the end of Pass 2, `5` is also in its correct position.

### Pass 3

| Comparison | Action | List After Action |
|---|---|---|
| Compare `2` and `4` | No swap | `[1, 2, 4, 5, 8]` |

Final sorted list: `[1, 2, 4, 5, 8]`.

The important pattern is simple: after each pass, one big value settles at the end.

---

## Bubble Sort Python Implementation

```python
def bubble_sort(numbers):  # Define a function that receives a list
    n = len(numbers)  # Store the number of items in the list
    for pass_index in range(n - 1):  # Run passes from first to second-last item
        for i in range(n - 1 - pass_index):  # Compare only the unsorted part of the list
            if numbers[i] > numbers[i + 1]:  # Check if neighbouring values are in wrong order
                temp = numbers[i]  # Store the left value safely before swapping
                numbers[i] = numbers[i + 1]  # Move the right value to the left position
                numbers[i + 1] = temp  # Put the stored left value into the right position
    return numbers  # Return the sorted list

marks = [5, 1, 4, 2, 8]  # Create a sample list of numbers
sorted_marks = bubble_sort(marks)  # Call the function and store the returned sorted list
print(sorted_marks)  # Display the sorted list
```

**How the code works:**

- `n = len(numbers)` counts how many values are present.
- The outer loop controls how many passes are needed.
- The inner loop compares neighbouring values like `numbers[i]` and `numbers[i + 1]`.
- If the left value is bigger, the code swaps both values using a temporary variable.
- `n - 1 - pass_index` avoids checking values that are already settled at the end.

**Common doubt:** Why do we need two loops? One loop is for passes, and the other loop is for comparisons inside each pass.

**Swap shortcut in Python:** You can also swap in one line: `numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]`. Both methods do the same job.

---

## Selection Sort Intuition

- **Official Definition:** **Selection Sort** is a sorting algorithm that repeatedly selects the smallest item from the unsorted part and places it at the beginning.
- **In Simple Words:** Selection Sort finds the smallest remaining value and puts it in the next correct position.
- **Real-Life Example:** Suppose you are playing cards and want to arrange them from smallest to largest. You scan all cards, pick the smallest one, and place it in the correct position. Then you repeat for the remaining cards.

Selection Sort works in **positions**:

- Start at the first position.
- Find the smallest value in the remaining list.
- Swap that smallest value into the current position.
- Move to the next position and repeat.

After every pass, the left side of the list becomes sorted.

**In-place sorting:** Selection Sort does not create a new list. It sorts inside the same list by swapping values. Think of it as sorting cards using only one hand — you can swap cards within that hand, but you cannot move cards to a second hand.

![Selection Sort intuition where the smallest value in the unsorted part is selected and placed into the next sorted position on the left](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-selection-sort-intuition.png)

---

## Selection Sort Trace

Let us sort the same list:

`[5, 1, 4, 2, 8]`

### Pass 1

- Current position is index `0`.
- Unsorted part is `[5, 1, 4, 2, 8]`.
- Smallest value is `1` at index `1`.
- Swap index `0` and index `1`.
- List becomes `[1, 5, 4, 2, 8]`.

### Pass 2

- Current position is index `1`.
- Unsorted part is `[5, 4, 2, 8]`.
- Smallest value is `2` at index `3`.
- Swap index `1` and index `3`.
- List becomes `[1, 2, 4, 5, 8]`.

### Pass 3

- Current position is index `2`.
- Unsorted part is `[4, 5, 8]`.
- Smallest value is `4`.
- It is already at the correct position.
- Final list remains `[1, 2, 4, 5, 8]`.

The important pattern is simple: after each pass, one small value settles at the beginning.

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
        numbers[current_index] = numbers[min_index]  # Put the smallest value in current position
        numbers[min_index] = temp  # Move the old current value to the smallest value's old position
    return numbers  # Return the sorted list

scores = [5, 1, 4, 2, 8]  # Create a sample list of scores
sorted_scores = selection_sort(scores)  # Call the function and store the sorted list
print(sorted_scores)  # Display the sorted list
```

**How the code works:**

- `current_index` marks the position we are trying to fill.
- `min_index` stores the index of the smallest value found so far.
- The inner loop searches the unsorted part for a smaller value.
- After the inner loop ends, the smallest value is swapped into the current position.
- The sorted area grows from the left side.

**Common doubt:** Why does Selection Sort swap only once per pass? Because it first finds the smallest value, then swaps it after the search is complete.

**Function reuse:** Once `selection_sort` is defined, you can call it on any list without rewriting the logic — for example, `selection_sort(array_2)` — which is one of the main benefits of writing sorting logic as a function.

---

## Bubble Sort vs Selection Sort

Both algorithms use nested loops, but their thinking is different.

| Point | Bubble Sort | Selection Sort |
|---|---|---|
| Main action | Compare neighbours | Find smallest remaining value |
| Direction of sorted part | Largest values settle on the right | Smallest values settle on the left |
| Swaps | Can swap many times in one pass | Usually swaps once per pass |
| Beginner intuition | Like pushing big values to the end | Like selecting the next smallest item |
| Time complexity | O(n^2) | O(n^2) |
| Extra space | O(1) | O(1) |

Bubble Sort is useful for understanding adjacent comparison. Selection Sort is useful for understanding how we repeatedly choose the best candidate for the next position.

**When both have O(n^2) time, which is better?** On **nearly sorted data**, Bubble Sort can finish early because it may stop swapping once values are already in order. Selection Sort still scans the full unsorted portion every pass to find the minimum. So Bubble Sort often performs better on nearly sorted lists.

Other sorting algorithms such as **Merge Sort** and **Heap Sort** exist for larger datasets and are much faster in practice, but Bubble Sort and Selection Sort are the best starting point for learning how sorting logic is built.

---

## Manual Tracing Method

- **Official Definition:** **Tracing** means manually following an algorithm step by step to see how values change.
- **In Simple Words:** Tracing is like dry running the code on paper before trusting the computer.
- **Real-Life Example:** Before submitting a maths answer, you may check every step again to confirm the final result.

When tracing sorting algorithms:

- Write the starting list clearly.
- Mark which part is sorted and which part is unsorted.
- Write every comparison that happens.
- Write every swap that happens.
- Write the list after each pass.

Tracing is also a useful **debugging skill**. When your sorting code gives unexpected output, tracing on paper helps you find where the logic went wrong.

### Activity: Trace Bubble Sort

Trace Bubble Sort on this list:

`[6, 2, 8, 4]`

Use this format:

| Pass | Comparisons Made | List After Pass |
|---|---|---|
| Pass 1 | Fill this yourself | Fill this yourself |
| Pass 2 | Fill this yourself | Fill this yourself |
| Pass 3 | Fill this yourself | Fill this yourself |

Expected final sorted list: `[2, 4, 6, 8]`.

### Activity: Trace Selection Sort

Trace Selection Sort on this list:

`[9, 1, 7, 3]`

Use this format:

| Pass | Smallest Value Found | List After Pass |
|---|---|---|
| Pass 1 | Fill this yourself | Fill this yourself |
| Pass 2 | Fill this yourself | Fill this yourself |
| Pass 3 | Fill this yourself | Fill this yourself |

Expected final sorted list: `[1, 3, 7, 9]`.

---

## Complexity Analysis of Bubble Sort and Selection Sort

- **Official Definition:** **Time complexity** describes how the running time of an algorithm grows when input size grows.
- **In Simple Words:** It tells us how much slower the algorithm becomes when the list becomes bigger.
- **Real-Life Example:** Checking one student's marks is quick. Comparing every student with many other students becomes slow when the class size grows.

Both Bubble Sort and Selection Sort use nested loops.

For a list of `n` items:

- The outer loop runs around `n` times.
- The inner loop also runs around `n` times.
- So the rough work becomes `n x n`.
- That is why both are called **O(n^2)** algorithms.

**Important caution:** Two nested loops do not always mean O(n^2) in every situation. You must check how many times each loop actually runs. Here, both loops run roughly `n` times, so O(n^2) is correct.

![Manual tracing connected to O(n squared) work, showing comparison checks growing with input size and O(1) extra space](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-complexity-tracing.png)

### Bubble Sort Optimization

You can improve Bubble Sort in two ways:

- Run the inner loop only on the **unsorted part** of the list (values already at the end are skipped).
- Stop early if a full pass completes with **no swaps** — this means the list is already sorted.

These optimizations do not change the worst-case O(n^2) time, but they help on nearly sorted data.

### Space Complexity

- **Official Definition:** **Space complexity** describes how much extra memory an algorithm needs as input size grows.
- **In Simple Words:** It tells us whether the algorithm needs extra big storage or works mostly inside the same list.
- **Real-Life Example:** Rearranging books on the same shelf needs little extra space; copying all books to a new shelf needs more space.

Bubble Sort and Selection Sort both use **O(1)** extra space because they sort inside the same list and only use a few variables like `temp`, `i`, or `min_index`.

---

## Common Mistakes and Doubts

- **Wrong loop range:** Going till `n` while checking `numbers[i + 1]` can cause an index error.
- **Confusing pass and comparison:** A pass contains many comparisons; they are not the same thing.
- **Thinking O(n^2) means exactly n^2 comparisons:** Big-O explains growth pattern, not exact step count.
- **Forgetting to trace:** Sorting code is much easier when you first trace small lists manually.

When in doubt, use a small list like `[4, 2, 1]` and write each pass on paper.

---

## Key Takeaways

- **Bubble Sort** compares neighbouring values and pushes larger values toward the end.
- **Selection Sort** repeatedly selects the smallest remaining value and places it at the next correct position.
- Both algorithms can be implemented using nested loops and simple swaps inside functions.
- Manual tracing helps you understand how the list changes after every pass and is a useful debugging skill.
- Both Bubble Sort and Selection Sort have **O(n^2)** worst-case time complexity and **O(1)** extra space complexity.
- On nearly sorted data, Bubble Sort can finish earlier than Selection Sort.

In the next lesson, you will continue building algorithmic thinking by comparing more problem-solving patterns and understanding when one approach is better than another.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| Algorithm | A series of steps to solve a problem | Compare neighbours, then swap |
| Sorting | Arranging data in order | `[3, 1, 2]` to `[1, 2, 3]` |
| Bubble Sort | Sorts by comparing adjacent values | Compare `numbers[i]` and `numbers[i + 1]` |
| Selection Sort | Sorts by selecting the smallest remaining value | Track `min_index` |
| Pass | One full round of algorithm work | One outer loop cycle |
| Comparison | Checking two values | `numbers[i] > numbers[i + 1]` |
| Swap | Exchanging two values | `a, b = b, a` |
| Trace | Manual dry run of steps | Write list after each pass |
| `range()` | Generates loop numbers | `range(n - 1)` |
| `len()` | Counts list items | `len(numbers)` |
| O(n^2) | Work grows roughly as n x n | Nested loops |
| O(1) space | Constant extra memory | Sorting inside same list |
