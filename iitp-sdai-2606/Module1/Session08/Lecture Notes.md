# Sorting Algorithms - Bubble Sort & Selection Sort

## What You Will Learn in This Lesson

You have already learned how to write reusable **functions** and divide a program into smaller logical parts. That idea is very useful now because sorting algorithms are easier to understand when each algorithm is written as a separate function.

In this lesson, you will learn two beginner-friendly sorting algorithms: **Bubble Sort** and **Selection Sort**. You will trace them manually, implement them in Python, and understand why both usually take **O(n^2)** time for a list of `n` items.

By the end, you will be able to explain how both algorithms work, write their Python code, trace their steps on sample arrays, and compare their time and space complexity.

---

## What Is Sorting?

- **Official Definition:** **Sorting** is the process of arranging data in a specific order, usually ascending or descending.
- **In Simple Words:** Sorting means putting items in order, like smallest to biggest or A to Z.
- **Real-Life Example:** Arranging exam marks from lowest to highest, or arranging students' names alphabetically in an attendance sheet.

Sorting is useful because:

- Searching becomes easier after data is sorted.
- Reports look cleaner and more readable.
- Rankings, leaderboards, and price filters depend on sorting.
- Many advanced algorithms expect sorted data as input.

For example, an online shopping app can sort products by **price low to high**. A result portal can sort students by **marks high to low**. Sorting is a basic operation used in many real applications.

![Sorting in Python shown with exam marks, product prices, and student name cards moving from unsorted order to clean ascending order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-sorting-big-picture.png)

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

Let us sort this list in ascending order:

`[5, 3, 4, 1]`

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

marks = [5, 3, 4, 1]  # Create a sample list of numbers
sorted_marks = bubble_sort(marks)  # Call the function and store the returned sorted list
print(sorted_marks)  # Display the sorted list
```

**How the code works:**

- `n = len(numbers)` counts how many values are present.
- The outer loop controls how many passes are needed.
- The inner loop compares neighbouring values like `numbers[i]` and `numbers[i + 1]`.
- If the left value is bigger, the code swaps both values.
- `n - 1 - pass_index` avoids checking values that are already settled at the end.

**Common doubt:** Why do we need two loops? One loop is for passes, and the other loop is for comparisons inside each pass.

---

## Bubble Sort With Trace Printing

Sometimes, printing each pass helps you see what the algorithm is doing.

```python
def bubble_sort_trace(numbers):  # Define a function to sort and print each pass
    n = len(numbers)  # Store the length of the list
    for pass_index in range(n - 1):  # Run one pass at a time
        for i in range(n - 1 - pass_index):  # Compare neighbouring values in unsorted part
            if numbers[i] > numbers[i + 1]:  # Check if swap is needed
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap using Python shortcut
        print("After pass", pass_index + 1, ":", numbers)  # Show list after each pass
    return numbers  # Return the final sorted list

data = [7, 2, 5, 1]  # Create a sample list
bubble_sort_trace(data)  # Run the trace version of bubble sort
```

**How the code works:**

- The logic is the same as normal Bubble Sort.
- The `print()` line shows the list after each pass.
- Python allows a shortcut swap: `a, b = b, a`.
- Trace printing is useful for learning, but in real apps we usually avoid too many prints.

---

## Selection Sort Intuition

- **Official Definition:** **Selection Sort** is a sorting algorithm that repeatedly selects the smallest item from the unsorted part and places it at the beginning.
- **In Simple Words:** Selection Sort finds the smallest remaining value and puts it in the next correct position.
- **Real-Life Example:** Suppose you are arranging currency notes from smallest to largest. You pick the smallest note first, then the next smallest, then the next.

Selection Sort works in **positions**:

- Start at the first position.
- Find the smallest value in the remaining list.
- Swap that smallest value into the current position.
- Move to the next position and repeat.

After every pass, the left side of the list becomes sorted.

![Selection Sort intuition where the smallest value in the unsorted part is selected and placed into the next sorted position on the left](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-selection-sort-intuition.png)

---

## Selection Sort Trace

Let us sort the same list:

`[5, 3, 4, 1]`

### Pass 1

- Current position is index `0`.
- Unsorted part is `[5, 3, 4, 1]`.
- Smallest value is `1`.
- Swap `5` and `1`.
- List becomes `[1, 3, 4, 5]`.

### Pass 2

- Current position is index `1`.
- Unsorted part is `[3, 4, 5]`.
- Smallest value is `3`.
- It is already at the correct position.
- List remains `[1, 3, 4, 5]`.

### Pass 3

- Current position is index `2`.
- Unsorted part is `[4, 5]`.
- Smallest value is `4`.
- It is already at the correct position.
- Final list remains `[1, 3, 4, 5]`.

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

scores = [5, 3, 4, 1]  # Create a sample list of scores
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

![Manual tracing connected to O(n squared) work, showing comparison checks growing with input size and O(1) extra space](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session08/session08-complexity-tracing.png)

### Simple Growth Table

| Number of Items | Rough Comparisons |
|---|---|
| 5 | Around 25 |
| 10 | Around 100 |
| 100 | Around 10,000 |
| 1,000 | Around 1,000,000 |

This table is not about exact counting. It helps you feel the growth pattern: when input size increases, work grows much faster.

### Space Complexity

- **Official Definition:** **Space complexity** describes how much extra memory an algorithm needs as input size grows.
- **In Simple Words:** It tells us whether the algorithm needs extra big storage or works mostly inside the same list.
- **Real-Life Example:** Rearranging books on the same shelf needs little extra space; copying all books to a new shelf needs more space.

Bubble Sort and Selection Sort both use **O(1)** extra space because they sort inside the same list and only use a few variables like `temp`, `i`, or `min_index`.

---

## Activity: Compare Both Algorithms in Code

Use the same input list for both algorithms and compare the output.

```python
def bubble_sort(numbers):  # Define Bubble Sort function
    n = len(numbers)  # Store list length
    for pass_index in range(n - 1):  # Run passes
        for i in range(n - 1 - pass_index):  # Compare neighbours
            if numbers[i] > numbers[i + 1]:  # Check wrong order
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap neighbours
    return numbers  # Return sorted list

def selection_sort(numbers):  # Define Selection Sort function
    n = len(numbers)  # Store list length
    for current_index in range(n - 1):  # Choose each position
        min_index = current_index  # Assume current value is smallest
        for i in range(current_index + 1, n):  # Search rest of list
            if numbers[i] < numbers[min_index]:  # Check if smaller value exists
                min_index = i  # Store smaller value's index
        numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]  # Swap into position
    return numbers  # Return sorted list

data_for_bubble = [8, 3, 5, 2]  # Create data for Bubble Sort
data_for_selection = [8, 3, 5, 2]  # Create same data for Selection Sort

print("Bubble:", bubble_sort(data_for_bubble))  # Print Bubble Sort result
print("Selection:", selection_sort(data_for_selection))  # Print Selection Sort result
```

**How the code works:**

- Both functions receive the same values.
- Both return `[2, 3, 5, 8]`.
- Their outputs match, but their internal method is different.
- This activity builds the habit of comparing algorithms with the same input.

---

## Activity: Count Comparisons Manually

This activity helps you connect tracing with **O(n^2)** thinking. Use the list `[4, 1, 3, 2]` and count how many comparisons each algorithm makes.

### Bubble Sort Comparison Count

For basic Bubble Sort with `4` items:

- Pass 1 compares 3 pairs.
- Pass 2 compares 2 pairs.
- Pass 3 compares 1 pair.
- Total comparisons = `3 + 2 + 1 = 6`.

The list becomes sorted after these passes:

| Pass | List After Pass |
|---|---|
| Start | `[4, 1, 3, 2]` |
| Pass 1 | `[1, 3, 2, 4]` |
| Pass 2 | `[1, 2, 3, 4]` |
| Pass 3 | `[1, 2, 3, 4]` |

### Selection Sort Comparison Count

For Selection Sort with `4` items:

- Pass 1 checks 3 remaining values to find the smallest.
- Pass 2 checks 2 remaining values.
- Pass 3 checks 1 remaining value.
- Total comparisons = `3 + 2 + 1 = 6`.

The list becomes sorted like this:

| Pass | Smallest Selected | List After Pass |
|---|---|---|
| Start | Not selected yet | `[4, 1, 3, 2]` |
| Pass 1 | `1` | `[1, 4, 3, 2]` |
| Pass 2 | `2` | `[1, 2, 3, 4]` |
| Pass 3 | `3` | `[1, 2, 3, 4]` |

Both algorithms made the same number of comparisons here, but their movement style was different. Bubble Sort moved values by neighbouring swaps; Selection Sort directly selected the smallest remaining value.

---

## Common Mistakes and Doubts

- **Changing the original list:** These implementations sort the same list that is passed to the function. If you need the original list later, pass a copy using `numbers.copy()`.
- **Wrong loop range:** Going till `n` while checking `numbers[i + 1]` can cause an index error.
- **Confusing pass and comparison:** A pass contains many comparisons; they are not the same thing.
- **Thinking O(n^2) means exactly n^2 comparisons:** Big-O explains growth pattern, not exact step count.
- **Forgetting to trace:** Sorting code is much easier when you first trace small lists manually.

When in doubt, use a small list like `[4, 2, 1]` and write each pass on paper.

---

## Key Takeaways

- **Bubble Sort** compares neighbouring values and pushes larger values toward the end.
- **Selection Sort** repeatedly selects the smallest remaining value and places it at the next correct position.
- Both algorithms can be implemented using nested loops and simple swaps.
- Manual tracing helps you understand how the list changes after every pass.
- Both Bubble Sort and Selection Sort have **O(n^2)** time complexity and **O(1)** extra space complexity.

In the next lesson, you will continue building algorithmic thinking by comparing more problem-solving patterns and understanding when one approach is better than another.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
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
