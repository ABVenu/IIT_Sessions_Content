# Masterclass: Sorting Algorithms – Insertion Sort

## What You Will Learn in This Lesson

You have already learnt **Binary Search**, **Bubble Sort**, and **Selection Sort**. You know two ways to arrange a list, and you know how to search quickly once a list is in order.

Now let us learn another important sort: **Insertion Sort**. It builds a **sorted portion** on the left of the list and grows that portion by one element at a time, just as you insert a playing card into the correct place in your hand.

In this lesson, you will learn:

- How a **sorted subarray** grows from the left, one index at a time
- How **array traversal** visits each new element that still needs a home
- How **element shifting** opens a gap so the current value can sit correctly
- How to **implement** Insertion Sort with loops, comparisons, and shifts
- How to **trace** each iteration and name the current element and its final index
- How to apply Insertion Sort to simple **sorting** and **ordered-list** problems
- The **merits** and **demerits** of Insertion Sort, where it is used, and the **names** of other important sorts

By the end, you will be able to explain Insertion Sort in plain words, dry-run it on paper, and write a complete Python version.

---

## Why Learn Another Sorting Method?

**Bubble Sort** and **Selection Sort** already put a list in order. **Binary Search** then reads that order quickly. Insertion Sort is still worth learning because it uses a different idea: keep a neat left side and **insert** each new value into its correct place.

- **Official Definition:** **Sorting** means rearranging the elements of a collection so they follow a chosen order, usually **ascending** (small to large) or **descending** (large to small).
- **In Simple Words:** Sorting is lining things up so the next item is never "out of turn."
- **Real-Life Example:** Arranging cricket scores from lowest to highest, or arranging train departure times from morning to night, is sorting.

**Why Insertion Sort feels natural:** It matches something you already do with cards, photos, and books on a shelf. It is also a calm way to *create* the sorted data that fast search needs.

**Common doubt:** "I already know I can call a built-in sort. Why write this by hand?"  
Built-in sort is fine in daily coding. Learning Insertion Sort trains your eyes to see **comparisons**, **movement of elements**, and **growing sorted regions** — skills you need for interviews, tracing bugs, and later algorithms.

---

## The Card-Hand Picture

Think of five playing cards dealt face up on a table: `7, 2, 9, 4, 5`. You pick them up one by one and keep the cards **already in your hand** in sorted order.

- The first card, `7`, is already "sorted" because a single card cannot be out of order.
- The second card, `2`, is compared with `7` and slipped to the left.
- Each new card is **inserted** into the correct place among the cards you already hold.

That habit is Insertion Sort. The hand is the **sorted subarray**. The table is the **unsorted** remaining part.

![Playing cards in a hand stay sorted while a new card is slipped into the correct gap, and waiting cards remain on the table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session02/masterclass02-01-card-hand.png?v=20260823)

**Activity — Sort five numbers like cards:**  
Write these marks on paper: `45, 12, 78, 23, 56`. Cover all except the first number. Uncover one number at a time and rewrite the left group so it stays sorted. Your final left group should be `12, 23, 45, 56, 78`.

Once you can do this with cards, the same idea maps cleanly onto a Python list and its **indices**.

---

## Sorted Subarrays: The Growing Left Side

Insertion Sort never sorts the whole list in one jump. It keeps a promise: after some work, the **left part** is sorted, and the **right part** is still waiting.

- **Official Definition:** A **sorted subarray** is a continuous slice of a list whose elements are already in the required order. In Insertion Sort, that slice is usually `arr[0]` to `arr[i - 1]`.
- **In Simple Words:** The left side is a neat queue. The right side is still a messy queue.
- **Real-Life Example:** In a temple queue, the people who have already taken tokens and stood in token order are the sorted part. New arrivals are still outside.

**The starting promise:** At the beginning, only index `0` is the sorted subarray. One element is always sorted by itself. That is why the algorithm starts considering elements from index `1`.

Watch the boundary move on this list: `[29, 10, 14, 37, 13]`

| After this work | Sorted subarray (left) | Unsorted part (right) |
|---|---|---|
| Start | `[29]` | `[10, 14, 37, 13]` |
| Insert `10` | `[10, 29]` | `[14, 37, 13]` |
| Insert `14` | `[10, 14, 29]` | `[37, 13]` |
| Insert `37` | `[10, 14, 29, 37]` | `[13]` |
| Insert `13` | `[10, 13, 14, 29, 37]` | *(empty)* |

![A growing sorted subarray on the left stays neat while the unsorted part on the right waits, with a clear boundary between them](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session02/masterclass02-02-sorted-subarray.png?v=20260823)

**Logic to remember:** The length of the sorted subarray grows by **exactly one** after each outer-loop round. When the unsorted part becomes empty, the whole list is sorted.

**Common mistake:** Thinking the right side is also being rearranged in the same round. In one round, Insertion Sort only finds a home for **one** new element. Other right-side values stay where they are.

**Activity — Name the boundary:**  
For `[8, 3, 6, 1]`, after two outer-loop steps (`i = 1` and `i = 2`), what is the sorted left part? Write it. (Answer: `[3, 6, 8]`)

The next skill is walking through the list so each new element gets its turn. That walk is **array traversal**.

---

## Array Traversal: Giving Every New Element a Turn

To grow the sorted left side, the program must visit each remaining index from left to right.

- **Official Definition:** **Array traversal** means visiting the elements of an array (or Python list) in a planned order, usually from a start index to an end index.
- **In Simple Words:** Traversal is walking down a row of lockers and opening them one by one.
- **Real-Life Example:** A teacher calling roll numbers from `2` onwards, because student `1` is already marked present, is a traversal that skips the first seat on purpose.

In Insertion Sort the **outer loop** traverses the unsorted part:

- Start at index `i = 1` (the first element that might be out of place)
- End at the last index `n - 1`
- Each value of `i` is the **current element** that must be inserted into the sorted subarray on its left

The **inner loop** then traverses **backwards** from `i - 1` towards `0`, because the correct seat for the current element may be somewhere on the left.

**Why two directions?**  
Forward traversal picks the next new card. Backward traversal looks through the cards already in hand to find the gap.

**Common doubt:** "Can I start the outer loop at `0`?"  
You can write `for i in range(n)`, but then the first round does nothing useful. Starting at `1` is cleaner and matches the idea that `arr[0]` is already a sorted subarray.

```python
# Show which index Insertion Sort would pick as the current element
marks = [45, 12, 78, 23, 56]  # Unsorted sample list of marks
n = len(marks)  # Store how many items are in the list

for i in range(1, n):  # Traverse from the second item to the last item
    current = marks[i]  # The element that must be inserted into the left side
    print("Outer step i =", i, "current element =", current, "left side =", marks[:i])  # Show the growing boundary
```

**How the code works:**

- `range(1, n)` visits `1, 2, 3, 4` for a list of length `5`
- `marks[:i]` is the current sorted-or-being-built left slice
- This script only **prints** the traversal; it does not sort yet

**Activity — Count the outer steps:**  
A list has `6` elements. How many times does the outer loop run if it starts at index `1`? Write the number. (Answer: **5**)

Traversal tells you *which* element is current. The next idea explains *how* that element moves into place: **shifting**, not random swapping.

---

## Element Shifting: Opening a Seat on the Left

Many beginners think sorting always means **swap two values**. Insertion Sort is different. It often **shifts** larger left-side elements one step to the right to create an empty seat, then drops the current value into that seat.

- **Official Definition:** **Element shifting** copies a value from index `j` to index `j + 1`, so a gap opens at a lower index. The original current value is stored separately (often called `key`) so it is not lost.
- **In Simple Words:** People in a cinema row slide one seat right to make space for a friend who arrived late.
- **Real-Life Example:** On a bookshelf, you push books to the right to insert a new book by author name. You do not swap the new book with a random book in the middle.

**Why we save the current value first:**  
If you start overwriting `arr[j + 1] = arr[j]` without saving `arr[i]`, the current element is destroyed. That saved copy is the **`key`**.

**Why shift instead of swap here:**  
A swap exchanges two positions. During insertion you may need to move **several** larger values right, one after another. Shifting does that in a straight line and then performs **one** final write of `key`.

![Cinema row sliding right to open a seat for a late friend holding 25 — shifting, not swapping two seats](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session02/masterclass02-03-element-shifting.png?v=20260823)

Look at inserting `13` into `[10, 14, 29, 37, 13]`.

| Action | List after the action | Notes |
|---|---|---|
| Save `key = 13` | `[10, 14, 29, 37, 13]` | `13` is safe in `key` |
| `37 > 13`, shift right | `[10, 14, 29, 37, 37]` | Gap is forming on the left of `37` |
| `29 > 13`, shift right | `[10, 14, 29, 29, 37]` | Gap moves left |
| `14 > 13`, shift right | `[10, 14, 14, 29, 37]` | Gap moves left again |
| `10 < 13`, stop | `[10, 14, 14, 29, 37]` | Correct seat is index `1` |
| Place `key` | `[10, 13, 14, 29, 37]` | Insertion complete |

**Logic:** Shift while the left neighbour is **strictly greater** than `key`. Using `>` (not `>=`) keeps equal values in their original relative order. That property is called **stability**.

**Common mistakes:**

- Forgetting to store `key` before shifting
- Shifting left instead of right
- Stopping the inner loop too early, so `key` sits in the wrong gap
- Using a swap-only habit and losing the "make a seat" picture

**Activity — Cinema row, then decide shift or swap:**  
Four seats on paper: `20, 40, 60, 25`. Treat `25` as the late friend, slide each larger number one seat right, then seat `25` and write every row. (Expected final: `20, 25, 40, 60`.)  
Would swapping only `60` and `25` finish the job? Write yes or no. (Answer: **No** — a single swap gives `20, 40, 25, 60`, which is still unsorted.)

You now have the three building blocks: a **sorted subarray**, a **traversal** that picks the next element, and **shifting** that opens its seat. Next, put them together as the full algorithm.

---

## How Insertion Sort Works

- **Official Definition:** **Insertion Sort** builds a sorted prefix of the list. For each index `i` from `1` to `n - 1`, it takes `arr[i]` as the current key and inserts that key into the correct position inside `arr[0 ... i]`.
- **In Simple Words:** Take the next item. Slide bigger left-side items right. Drop the item into the hole.
- **Real-Life Example:** A shopkeeper receiving new price tags inserts each tag into an already ordered price file, instead of throwing all tags on the floor and re-sorting from scratch.

### Steps (ascending order)

1. Treat `arr[0]` as the first sorted subarray.
2. Set `i = 1`. The current element is `key = arr[i]`.
3. Set `j = i - 1`. Walk left while `j >= 0` and `arr[j] > key`.
4. Each time the while condition is true, shift: `arr[j + 1] = arr[j]`, then `j = j - 1`.
5. Place the key: `arr[j + 1] = key`.
6. Increase `i` by `1` and repeat until `i` reaches the last index.

**Need for the `j >= 0` check:** If `key` is smaller than every left-side value, `j` becomes `-1`. The correct seat is then index `0`. In Python, `arr[-1]` is not an error — it secretly means the **last** item. The `j >= 0` check runs first, so the comparison never uses that last item by mistake.

**Common doubt:** "What if the current element is already larger than the last sorted value?"  
The inner loop never runs. `key` is written back to the same index. That is the **best case** for that round — almost no work.

---

## Trace: Find the Current Element and Its Correct Position

Tracing means you act like the computer. For every outer step, write the **current element (`key`)**, the **shifts**, and the **final index** where `key` lands.

**Example list:** `arr = [29, 10, 14, 37, 13]`

### Outer step `i = 1` — current element `10`

| Check | `j` | `arr[j]` compared with `10` | Action |
|---|---|---|---|
| 1 | 0 | `29 > 10` | Shift `29` to index `1` |
| Stop | `-1` | no more left items | Place `10` at index `0` |

List becomes `[10, 29, 14, 37, 13]`. Correct position of `10` is **index 0**.

### Outer step `i = 2` — current element `14`

| Check | `j` | `arr[j]` compared with `14` | Action |
|---|---|---|---|
| 1 | 1 | `29 > 14` | Shift `29` to index `2` |
| 2 | 0 | `10 < 14` | Stop walking left |
| Place | — | — | Place `14` at index `1` |

List becomes `[10, 14, 29, 37, 13]`. Correct position of `14` is **index 1**.

### Outer step `i = 3` — current element `37`

| Check | `j` | `arr[j]` compared with `37` | Action |
|---|---|---|---|
| 1 | 2 | `29 < 37` | No shift |
| Place | — | — | `37` stays at index `3` |

List stays `[10, 14, 29, 37, 13]`. Correct position of `37` is **index 3** (already home).

### Outer step `i = 4` — current element `13`

| Check | `j` | `arr[j]` compared with `13` | Action |
|---|---|---|---|
| 1 | 3 | `37 > 13` | Shift `37` right |
| 2 | 2 | `29 > 13` | Shift `29` right |
| 3 | 1 | `14 > 13` | Shift `14` right |
| 4 | 0 | `10 < 13` | Stop |
| Place | — | — | Place `13` at index `1` |

List becomes `[10, 13, 14, 29, 37]`. Correct position of `13` is **index 1**.

![Trace of inserting 13: current element highlighted, larger values shift right, then 13 lands at index 1](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session02/masterclass02-04-trace-insert.png?v=20260823)

Only **four** outer steps were needed for five elements. That matches `n - 1`.

**Activity — Trace on your own:**  
List: `[5, 2, 4, 6]`  
For `i = 1` and `i = 2` only, write `key`, each shift, and the index where `key` is placed.  
(Expected after `i = 1`: `[2, 5, 4, 6]`. Expected after `i = 2`: `[2, 4, 5, 6]`.)

Paper traces make the Python code feel obvious, because the code is only those table rows turned into a `for` and a `while`.

---

## Implement Insertion Sort in Python

**Iterative Insertion Sort** uses an outer `for` loop for traversal and an inner `while` loop for comparisons and shifting.

```python
# Full Insertion Sort for a list of numbers in ascending order
def insertion_sort(arr):  # Define a function that sorts the given list in place
    n = len(arr)  # Count how many elements must be processed
    for i in range(1, n):  # Traverse from the second element to the last element
        key = arr[i]  # Save the current element so shifting cannot overwrite it
        j = i - 1  # Start comparing from the neighbour immediately on the left
        while j >= 0 and arr[j] > key:  # Walk left while left values are larger than key
            arr[j + 1] = arr[j]  # Shift the larger element one seat to the right
            j = j - 1  # Move one index further left to continue the search for a seat
        arr[j + 1] = key  # Drop the saved current element into the opened seat
    return arr  # Return the same list, now sorted, so the caller can print it


scores = [29, 10, 14, 37, 13]  # Unsorted sample scores
print(insertion_sort(scores))  # Expected output: [10, 13, 14, 29, 37]
print(insertion_sort([7]))  # Expected output: [7] (already a sorted subarray of length 1)
print(insertion_sort([]))  # Expected output: [] (empty list needs no work)
```

**How the code works:**

- The outer loop picks each **current element** exactly once
- `key` protects that element while the left side slides right
- The inner `while` both **compares** and **shifts**
- `arr[j + 1] = key` writes the current element into its **correct position**
- The function changes the original list (**in-place**) and also returns it for easy printing

**Common mistakes to avoid:**

- Writing `arr[j] >= key` if you want a **stable** sort for equal values
- Using `j > 0` instead of `j >= 0`, which refuses to insert at index `0`
- Forgetting `j = j - 1`, which can create an infinite loop
- Creating a new list every shift when a simple in-place shift is enough

**Activity — Predict, then run:**  
Before running, write the output of:

```python
print(insertion_sort([4, 3, 2, 1]))
print(insertion_sort([1, 2, 3, 4]))
```

(Expected: `[1, 2, 3, 4]` both times. The second call does almost no shifting.)

---

## Best Case, Worst Case, and Extra Memory

Complexity answers a practical question: if the list becomes much longer, how much slower does Insertion Sort become?

- **Official Definition:** **Time complexity** describes how the number of comparisons and shifts grows as the list size `n` grows. **Space complexity** describes extra memory beyond the input list.
- **In Simple Words:** Time is "how much walking and sliding." Space is "how many extra boxes."
- **Real-Life Example:** If exam papers are almost in roll-number order, inserting a few misplaced papers is quick. If they are in reverse order, every paper must slide past many others.

| Situation | What happens | Time | Extra space |
|---|---|---|---|
| Already sorted | Inner loop almost never shifts | **O(n)** best case | **O(1)** |
| Reverse sorted | Almost every left item shifts | **O(n²)** worst case | **O(1)** |
| Random order | Mix of short and long inner loops | **O(n²)** average | **O(1)** |

**Why extra space is O(1):** You store a few integers (`i`, `j`, `key`, `n`). You do not copy the whole list.

**When Insertion Sort is a wise choice:** The list is **small**, or the list is **almost sorted**. In those cases the inner loop stays short, and the algorithm feels efficient and easy to understand.

**When another method may be better:** For huge, fully shuffled data, faster advanced sorts exist. You may meet those in a future lesson. For this lesson, Insertion Sort is the right tool to master.

**Activity — Feel the best case:**  
List: `[1, 2, 4, 3, 5]`. How many shifts are needed to place `3`? Walk **left** from `4` in your notebook. (Answer: **1** shift — only `4` moves right.)

Those time and space facts are the reason Insertion Sort has a clear list of strengths and limits. Let us name them plainly.

---

## Merits and Demerits of Insertion Sort

Every algorithm has a personality. Insertion Sort is calm and careful, not a sprint champion for huge messy lists.

- **Official Definition:** **Merits** are the strengths that make an algorithm a good choice in some situations. **Demerits** are the limits that make it a poor choice in others.
- **In Simple Words:** Merits are "why we like it." Demerits are "when we should pick something else."
- **Real-Life Example:** A bicycle is wonderful for a short lane. It is a weak choice for a 400 km highway trip. Insertion Sort is like that bicycle.

**Merits**

- **Simple to write and trace** — one `for` loop, one `while` loop, and a `key`
- **In-place** — extra memory stays **O(1)**
- **Stable** — equal values keep their original relative order
- **Adaptive** — almost-sorted lists finish in about **O(n)** time
- **Online-friendly** — you can insert one new item into an already ordered list without restarting from scratch
- **Strong on small lists** — few elements mean few shifts, so it feels fast enough

**Demerits**

- **Slow on large shuffled data** — average and worst-case time is **O(n²)**
- **Many shifts** — moving values one seat at a time can become tiring work
- **Not the main engine for huge datasets** — real products usually pick a faster sort when `n` is very large
- **Array shifting costs grow quickly** — the bigger the left side, the farther a small `key` may have to travel

**How to choose:** Use Insertion Sort when the list is **small** or **almost sorted**, or when new items keep arriving one by one. For a huge random list, remember the names of the faster sorts listed later in this lesson.

---

## Practical Applications

Insertion Sort is not only a classroom story. Software uses the same "insert into a neat left side" habit in small, everyday jobs.

![Insertion Sort helping in a live leaderboard, a shop price file, a short marks list, and an almost-sorted attendance sheet](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/masterclass/session02/masterclass02-05-where-it-is-used.png?v=20260823)

- **Official Definition:** A **practical application** is a real task where the algorithm's idea is used, not only practised on paper.
- **In Simple Words:** These are places where "slide and insert" actually helps people and programs.
- **Real-Life Example:** A cricket app inserting one new score into a short leaderboard is Insertion Sort thinking.

**Where you will see this idea**

- **Small lists** — five to twenty items, such as a short marks list or a tiny menu of prices
- **Nearly sorted data** — an attendance sheet that is almost in order, with only one or two names out of place
- **Live ordered lists** — a new UPI amount, token number, or leaderboard score arriving while the rest is already sorted
- **Online insertion** — keep accepting new values and placing each one without re-sorting the whole collection from zero
- **Inside bigger library sorts** — many built-in sorts switch to Insertion Sort for very small runs, because it is simple and cheap there

**Activity — Spot the good fit:**  
Which job is a better match for Insertion Sort?  
A) Sorting one crore random product IDs  
B) Inserting one new fare into a list of six already-sorted bus fares  
Write A or B. (Answer: **B**)

---

## Other Important Sorts in Software Engineering

Insertion Sort is one member of a larger family. In software engineering you will also hear these names. You already know **Bubble Sort** and **Selection Sort**. Learn the rest as names for now.

- **Merge Sort**
- **Quick Sort**
- **Heap Sort**
- **Shell Sort**
- **Counting Sort**
- **Radix Sort**
- **Bucket Sort**
- **Timsort**

You do not need their full logic in this lesson. Remember the names, and remember that **Insertion Sort** is the one you can now implement, trace, and justify.

---

## Problem Solving with Insertion Sort

Algorithms become useful when you apply the same insertion idea to real questions.

### Problem 1: Sort exam marks in ascending order

```python
# Problem: Arrange student marks from lowest to highest
def sort_marks(marks):  # Function that sorts a marks list using Insertion Sort
    n = len(marks)  # Number of mark entries
    for i in range(1, n):  # Visit each mark after the first
        key = marks[i]  # Current mark that must be inserted
        j = i - 1  # Index of the last value in the current sorted subarray
        while j >= 0 and marks[j] > key:  # Shift every larger mark one step right
            marks[j + 1] = marks[j]  # Copy the larger mark to the right seat
            j = j - 1  # Continue walking left
        marks[j + 1] = key  # Place the current mark in its correct seat
    return marks  # Return the sorted marks


print(sort_marks([45, 12, 78, 23, 56]))  # Expected: [12, 23, 45, 56, 78]
print(sort_marks([88, 88, 70]))  # Expected: [70, 88, 88]
```

**How the code works:**

- Same Insertion Sort core, named for a marks context
- Equal marks (`88` and `88`) stay in their original relative order because the inner condition uses `>`

### Problem 2: Insert one new value into an already ordered list

Sometimes the list is already sorted and only **one** new item arrives — a new UPI amount, a new token number, or a new score on a leaderboard.

```python
# Problem: Insert one value into a list that is already sorted
def insert_into_sorted(ordered, new_value):  # Add new_value into the correct place
    result = ordered[:]  # Copy the original ordered list so the input is not changed
    result.append(new_value)  # Temporarily park the new value at the right end
    key = result[-1]  # The newly added value is the current element
    j = len(result) - 2  # Start from the last already-sorted index
    while j >= 0 and result[j] > key:  # Shift larger values right
        result[j + 1] = result[j]  # Open a seat by moving one element right
        j = j - 1  # Keep walking left
    result[j + 1] = key  # Drop the new value into the correct seat
    return result  # Return the longer ordered list


prices = [99, 199, 299, 499]  # Already sorted prices in rupees
print(insert_into_sorted(prices, 249))  # Expected: [99, 199, 249, 299, 499]
print(insert_into_sorted(prices, 50))  # Expected: [50, 99, 199, 299, 499]
print(insert_into_sorted(prices, 600))  # Expected: [99, 199, 299, 499, 600]
```

**How the code works:**

- This is **one outer step** of Insertion Sort
- `append` makes the new value the current element at the end
- Shifting then finds its correct position inside the old sorted subarray

### Problem 3: Empty list, one element, and already-sorted edges

Good problem solvers always test edges.

```python
# Edge-case checks for Insertion Sort
def insertion_sort(arr):  # Standard in-place Insertion Sort
    n = len(arr)  # Length may be 0 or 1
    for i in range(1, n):  # For empty or one-element lists, this loop never runs
        key = arr[i]  # Current element
        j = i - 1  # Left neighbour index
        while j >= 0 and arr[j] > key:  # Shift larger left values
            arr[j + 1] = arr[j]  # Right-shift
            j = j - 1  # Move left
        arr[j + 1] = key  # Insert key
    return arr  # Sorted list (or the same tiny list)


print(insertion_sort([]))  # Expected: []
print(insertion_sort([42]))  # Expected: [42]
print(insertion_sort([3, 3, 3]))  # Expected: [3, 3, 3]
print(insertion_sort([10, 20, 30]))  # Expected: [10, 20, 30] (already sorted)
```

**How the code works:**

- `range(1, 0)` and `range(1, 1)` produce no values, so empty and single-item lists are safe
- An already-sorted list still traverses `n - 1` outer steps, but the inner loop stays quiet

**Activity — Solve this mini problem:**  
Ordered tokens: `[11, 18, 25, 40]`. A new token `20` arrives. On paper, write each shift, then the final list. Confirm with `insert_into_sorted`. (Expected: `[11, 18, 20, 25, 40]`)

---

## Full Practice: Traverse, Shift, and Trace Together

Use this script as an end-to-end drill. It prints the **current element**, the **sorted subarray before insertion**, and the list after each outer step.

```python
# Complete practice script: Insertion Sort with a learning trace
def insertion_sort_with_trace(arr):  # Sort the list and print each outer step
    n = len(arr)  # Number of elements
    print("Start:", arr)  # Show the original unsorted list
    for i in range(1, n):  # Traverse each new current element
        key = arr[i]  # Save the current element
        print("Current element:", key, "at index", i, "| sorted left:", arr[:i])  # Name key and left subarray
        j = i - 1  # Begin walking left
        while j >= 0 and arr[j] > key:  # Compare and shift
            arr[j + 1] = arr[j]  # Move a larger element right
            j = j - 1  # Continue left
        arr[j + 1] = key  # Place key in its correct position
        print("After inserting", key, "at index", j + 1, "->", arr)  # Show the new list and landing index
    print("Final sorted list:", arr)  # Confirm the unsorted part is now empty
    return arr  # Return the sorted list


data = [29, 10, 14, 37, 13]  # Practice list used in the paper trace
insertion_sort_with_trace(data)  # Run the traced sort and match it with your notebook
```

**How the code works:**

- Same Insertion Sort logic, plus `print` statements for learning
- Each printed "Current element" line is exactly what you named on paper
- The landing `index` in the print is `j + 1` after the inner loop ends

**Activity — Notebook summary:**  
After running the script, write three lines in your notes:

1. One sentence defining Insertion Sort
2. What a **sorted subarray** is in this algorithm
3. The difference between a **shift** and a **swap**

---

## Key Takeaways

- **Insertion Sort** grows a **sorted subarray** on the left by inserting one **current element** at a time.
- **Array traversal** and **element shifting** work together: the outer loop picks `key`, the inner loop walks left, larger values slide right, and `key` lands at index `j + 1`.
- Merits include being **simple**, **stable**, **in-place**, and fast on **small** or **almost-sorted** data; demerits are **O(n²)** time and many shifts on large shuffled lists.
- It is useful for short lists, live leaderboards, and one-by-one inserts. Other important names in software engineering are **Merge Sort**, **Quick Sort**, **Heap Sort**, **Shell Sort**, **Counting Sort**, **Radix Sort**, **Bucket Sort**, and **Timsort**.
- Once you can trace and implement this sort, you can compare it with other methods and choose the right tool for the size and shape of the data.

---

## Important Commands, Libraries, Terminologies Used

| Term / Idea | Meaning (quick revision) |
|---|---|
| **Sorting** | Rearranging items into ascending or descending order |
| **Insertion Sort** | Insert each next element into the already sorted left portion |
| **Sorted subarray** | Left slice `arr[0 ... i-1]` that stays in order after each outer step |
| **Current element / `key`** | The value at index `i` being inserted; saved so shifts cannot overwrite it |
| **Array traversal** | Visiting indices in a planned order (outer loop forward, inner loop backward) |
| **Element shifting** | Copy `arr[j]` to `arr[j + 1]` to open a seat for `key` |
| **Comparison** | Check `arr[j] > key` to decide whether to shift |
| **Correct position** | The index `j + 1` where `key` is written after the inner loop |
| **In-place** | Sorts by changing the original list; no full extra copy |
| **Stable sort** | Equal values keep their original relative order (`>` not `>=`) |
| **Time O(n)** | Best case when the list is already (or almost) sorted |
| **Time O(n²)** | Worst and average cases when many shifts are needed |
| **Space O(1)** | Extra memory stays constant (`i`, `j`, `key`) |
| **Trace** | Paper dry-run of each `i`, `key`, shift, and landing index |
| **`range(1, n)`** | Outer-loop traversal that skips the first already-sorted index |
| **Merit** | A strength of the algorithm, such as stability or O(n) on nearly sorted data |
| **Demerit** | A limit of the algorithm, such as O(n²) on large shuffled lists |
| **Online insertion** | Placing each new value as it arrives, without a full re-sort |
| **Merge / Quick / Heap / Timsort** | Other important sorts you will hear in software engineering |
