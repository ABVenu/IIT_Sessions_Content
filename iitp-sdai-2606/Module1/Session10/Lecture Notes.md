# Hands-on Logic Building & DSA Problem Solving – II

## What You Will Learn in This Lesson

You have already set up **local development** on your laptop with **Python**, **VS Code**, and the **Terminal**. You also learned to plan problems using **input**, **output**, **conditions**, and **steps**, and solved beginner-level questions with **lists**, **strings**, and **dictionaries**.

In this lesson, you will move to **intermediate DSA problem solving**. You will learn to **analyse problem constraints**, write solutions using **nested logic** and **nested loops**, implement **Bubble Sort** and **Selection Sort** step by step, and use sorting to solve problems like **duplicate handling**, **second largest element**, and **ordered comparisons**.

By the end, you will be able to break a moderately complex problem into a clear algorithm, combine data structures with nested loops, and apply sorting as a practical tool inside real solutions.

---

## Why Intermediate Problems Need a Different Approach

- **Official Definition:** An **intermediate DSA problem** is a coding question that requires more than one simple loop or one direct condition to solve correctly.
- **In Simple Words:** The problem still uses lists, strings, or dictionaries — but you must compare values more carefully, handle repeats, or arrange data before answering.
- **Real-Life Example:** A scholarship committee receives 80 exam scores in random order. They need the **second highest** unique score, a check for **duplicate marks**, and a **sorted list** to pick the top ten — three tasks that cannot be solved with one careless pass.

Beginner problems often need only one loop. Intermediate problems commonly need:

- **Nested loops** — compare each value with others.
- **Extra conditions** — handle empty input, repeated maximum values, or ties.
- **Sorting** — arrange data first, then read the answer from the ordered list.

The good news is that you already know the building blocks. This lesson shows you how to **combine** them.

---

## Problem Analysis — Read the Rules Before You Code

- **Official Definition:** **Problem analysis** is the process of reading a question carefully, identifying its **constraints**, and converting the requirements into a step-by-step plan before writing code.
- **In Simple Words:** Problem analysis means understanding the rules of the game before you start playing.
- **Real-Life Example:** Before a cricket match, the umpire checks the pitch, team list, and overs limit. A programmer checks input size, allowed values, and expected output the same way.

### What Are Constraints?

- **Official Definition:** **Constraints** are the limits and conditions that define valid input and expected output for a problem.
- **In Simple Words:** Constraints tell you what kind of data you will receive and what special cases you must handle.
- **Real-Life Example:** A train ticket form says "Age must be between 5 and 100." That rule is a constraint — if you ignore it, your program may accept wrong data.

| Question to Ask | Why It Matters |
|---|---|
| How big can the input be? | Tells you whether a simple method is enough |
| Can values repeat? | Changes duplicate and ranking problems |
| Should output be sorted or just one answer? | Decides whether sorting is needed |
| Can the list or string be empty? | Prevents crashes and wrong assumptions |
| Are negative numbers possible? | Affects comparisons and sorting |

### From Problem Statement to Algorithm

- **Official Definition:** An **algorithm** is a fixed sequence of steps that solves a problem in a repeatable way.
- **In Simple Words:** An algorithm is a checked recipe — each step has a reason and a fixed order.
- **Real-Life Example:** Making chai: boil water → add tea leaves → add milk → strain → serve. Change the order and the result goes wrong.

**Problem analysis workflow:**

1. Read the problem twice in plain English.
2. Write down **input**, **output**, and **constraints**.
3. List special cases — empty list, one item, all same values.
4. Decide whether you need one loop, nested loops, or sorting.
5. Write numbered steps before opening your editor.
6. Test with small examples, then edge cases.

**Common mistake:** Starting to code immediately without listing constraints. Five extra minutes of planning often saves thirty minutes of debugging.

![Problem analysis before coding — read constraints, define input and output, write steps, then implement the algorithm on your local machine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-01-problem-analysis-constraints.png?v=20260704)

---

## Practice Activity: Analyse Before Coding

I will analyse this problem before writing any code.

**Problem statement:** Given a list of roll numbers, check whether any roll number appears more than once.

**My analysis:**

| Part | Answer |
|---|---|
| **Input** | `[101, 204, 101, 309, 204]` |
| **Output** | `True` (duplicate exists) or `False` |
| **Constraints** | List can be empty; values can repeat |
| **Special cases** | Empty list → no duplicate; one item → no duplicate |
| **Approach** | Compare each value with every other value using nested loops |

**My algorithm steps:**

1. If the list length is less than 2, return `False`.
2. Use an outer loop for the first roll number.
3. Use an inner loop for the remaining roll numbers.
4. If two different positions have the same value, return `True`.
5. If no match is found after all checks, return `False`.

This planning step makes the coding part straightforward.

---

## Nested Logic — When One Loop Is Not Enough

- **Official Definition:** **Nested logic** means placing one loop, condition, or block of code inside another loop or condition.
- **In Simple Words:** Nested logic is a task inside a task — the outer task repeats, and inside each repetition you do a smaller detailed check.
- **Real-Life Example:** An exam invigilator walks row by row (outer task). For each student, they compare roll numbers with nearby students (inner task). Both tasks work together.

### Nested Loops Pattern

- **Official Definition:** A **nested loop** is a loop placed inside another loop.
- **In Simple Words:** For each item in the outer loop, the inner loop does extra work.
- **Real-Life Example:** Checking every student against every other student in an attendance sheet.

```python
numbers = [4, 7, 4, 9]  # Sample list with a duplicate value
has_duplicate = False  # Flag to store whether duplicate is found

for i in range(len(numbers)):  # Outer loop picks first position
    for j in range(i + 1, len(numbers)):  # Inner loop picks later positions only
        if numbers[i] == numbers[j]:  # Compare values at two different indexes
            has_duplicate = True  # Mark duplicate as found

print("Duplicate found:", has_duplicate)  # Display final result
```

**How the code works:**

- The outer loop picks index `i`.
- The inner loop picks index `j` only after `i`, so the same pair is not checked twice.
- When two different positions hold the same value, the flag becomes `True`.
- This pattern is common for duplicate detection and pair comparison.

**Common doubt:** Why start the inner loop at `i + 1`? Because comparing `(2, 5)` and `(5, 2)` is the same pair — starting at `i + 1` avoids repeated work.

![Nested loops pair comparison — outer loop picks one index, inner loop compares with later indexes to detect duplicates and valid pairs without checking the same pair twice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-02-nested-loops-pair-comparison.png?v=20260704)

---

## Nested Logic with Lists

- **Official Definition:** A **list problem with nested logic** uses one or more inner loops or conditions to compare, count, or transform list items.
- **In Simple Words:** You scan the list more than once or compare items inside the list with each other.
- **Real-Life Example:** Finding whether two students in a class have the same phone number by comparing every pair in the contact list.

### Problem 1: Count Pairs with a Given Sum

**Problem statement:** Count how many pairs of numbers in a list add up to a target value.

**Logic plan:**

- Input: `[1, 2, 3, 4, 5]`, target = `6`
- Output: `2` (pairs are `(1, 5)` and `(2, 4)`)
- Approach: Nested loops to check every unique pair.

```python
numbers = [1, 2, 3, 4, 5]  # Input list
target = 6  # Required pair sum
pair_count = 0  # Counter for valid pairs

for i in range(len(numbers)):  # Outer loop picks first number
    for j in range(i + 1, len(numbers)):  # Inner loop picks second number after i
        if numbers[i] + numbers[j] == target:  # Check whether pair sum matches target
            pair_count = pair_count + 1  # Increase count for valid pair

print("Pair count:", pair_count)  # Display final answer
```

**How the code works:**

- Each pair is checked exactly once because `j` always starts after `i`.
- The `if` condition checks the sum rule.
- `pair_count` stores how many valid pairs were found.

### Problem 2: Find All Duplicate Values

**Problem statement:** Print all values that appear more than once in a list.

```python
marks = [78, 85, 78, 92, 85, 78]  # Input list with repeats
duplicates = []  # List to store duplicate values already recorded

for i in range(len(marks)):  # Outer loop picks first index
    for j in range(i + 1, len(marks)):  # Inner loop compares with later indexes
        if marks[i] == marks[j]:  # Check whether values match
            if marks[i] not in duplicates:  # Avoid adding same duplicate again
                duplicates.append(marks[i])  # Store duplicate value

print("Duplicates:", duplicates)  # Display all duplicate values
```

**How the code works:**

- Nested loops find matching values at different positions.
- `if marks[i] not in duplicates` prevents printing the same duplicate multiple times.
- This is a direct application of nested comparison logic.

---

## Nested Logic with Strings

- **Official Definition:** A **string problem with nested logic** compares characters or substrings using loops inside loops or conditions inside loops.
- **In Simple Words:** You check letters or parts of text against other letters or parts of text.
- **Real-Life Example:** Checking whether any two words in a sentence start with the same letter by comparing every word pair.

### Problem 1: Check Whether Any Two Characters Match at Different Positions

**Problem statement:** Return `True` if the same character appears at two different positions in a string.

```python
word = "programming"  # Input string
has_repeat = False  # Flag for repeated character at different positions

for i in range(len(word)):  # Outer loop picks first character index
    for j in range(i + 1, len(word)):  # Inner loop picks later character index
        if word[i] == word[j]:  # Compare characters at two positions
            has_repeat = True  # Mark repeat as found

print("Repeated character exists:", has_repeat)  # Display result
```

**How the code works:**

- Each character is compared with every character after it.
- If any match is found at different positions, the flag becomes `True`.
- This pattern is useful for duplicate character checks.

### Problem 2: Count Substrings with All Vowels

**Problem statement:** Count how many substrings of length 3 contain at least one vowel.

```python
text = "education"  # Input string
vowels = "aeiou"  # Allowed vowel characters
count = 0  # Counter for valid substrings

for i in range(len(text) - 2):  # Outer loop picks starting index of length-3 substring
    substring = text[i:i + 3]  # Extract 3-character substring
    has_vowel = False  # Flag for vowel inside current substring
    for character in substring:  # Inner loop scans characters in substring
        if character in vowels:  # Check whether character is a vowel
            has_vowel = True  # Mark vowel found
    if has_vowel:  # If substring contains at least one vowel
        count = count + 1  # Increase valid substring count

print("Substring count:", count)  # Display final answer
```

**How the code works:**

- The outer loop creates every substring of length 3.
- The inner loop checks characters inside that substring.
- Nested logic combines substring creation with character checking.

---

## Nested Logic with Dictionaries

- **Official Definition:** A **dictionary problem with nested logic** often combines dictionary lookups with loops over lists or strings.
- **In Simple Words:** You store counts or seen values in a dictionary while looping through data.
- **Real-Life Example:** A shopkeeper tracks how many times each product code appears in the day's bill using a notebook with product name and count columns.

### Problem 1: Find Keys with Value Greater Than a Limit

**Problem statement:** Given a dictionary of student names and marks, print names with marks above 80.

```python
student_marks = {  # Dictionary of names and marks
    "Amit": 78,
    "Riya": 92,
    "Arjun": 81,
    "Neha": 64
}

for name in student_marks:  # Outer loop visits each key
    if student_marks[name] > 80:  # Nested condition checks mark value
        print(name, "scored above 80")  # Print qualifying student name
```

**How the code works:**

- The loop visits each key in the dictionary.
- The nested `if` checks the value linked to that key.
- This is nested logic using a condition inside a loop.

### Problem 2: Build Frequency Map with Nested Checks

**Problem statement:** Count how many times each word appears in a list of words.

```python
words = ["apple", "banana", "apple", "mango", "banana", "apple"]  # Input word list
frequency = {}  # Empty dictionary for counts

for word in words:  # Outer loop visits each word
    if word in frequency:  # Nested condition checks whether word already exists
        frequency[word] = frequency[word] + 1  # Increase existing count
    else:
        frequency[word] = 1  # First occurrence gets count 1

for word in frequency:  # Second loop prints final dictionary contents
    print(word, ":", frequency[word])  # Display each word and its count
```

**How the code works:**

- The first loop builds the frequency dictionary.
- The nested `if` decides whether to update or create a count.
- The second loop displays the stored results.

---

## Bubble Sort — Step-by-Step Implementation

You have already learned the idea of **Bubble Sort** — comparing neighbours and swapping them until the list is in order. In this lesson, you will implement it carefully and **use it inside problem solving**.

- **Official Definition:** **Bubble Sort** is a sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
- **In Simple Words:** Larger values bubble toward one end, one pass at a time.
- **Real-Life Example:** Students in a height line swap places with neighbours until the tallest student reaches the last position.

### Bubble Sort Trace on Sample Data

Sort this list in ascending order:

`[91, 88, 91, 76, 95]`

| Pass | Main Action | List After Pass |
|---|---|---|
| Pass 1 | Compare neighbours and swap when left is bigger | `[88, 91, 76, 91, 95]` |
| Pass 2 | Largest values settle toward the right | `[88, 76, 91, 91, 95]` |
| Pass 3 | Continue bubbling | `[76, 88, 91, 91, 95]` |
| Pass 4 | Final adjustments | `[76, 88, 91, 91, 95]` |

After sorting, equal values like the two `91`s sit next to each other — very useful for duplicate detection.

### Bubble Sort Python Implementation

```python
def bubble_sort(numbers):  # Define function to sort a list
    n = len(numbers)  # Store number of items
    for pass_index in range(n - 1):  # Outer loop controls number of passes
        for i in range(n - 1 - pass_index):  # Inner loop compares neighbours in unsorted part
            if numbers[i] > numbers[i + 1]:  # Check if left value is bigger than right value
                temp = numbers[i]  # Store left value temporarily
                numbers[i] = numbers[i + 1]  # Move right value to left position
                numbers[i + 1] = temp  # Put stored value into right position
    return numbers  # Return sorted list

scores = [91, 88, 91, 76, 95]  # Sample unsorted marks list
sorted_scores = bubble_sort(scores)  # Call sorting function
print(sorted_scores)  # Display sorted result
```

**How the code works:**

- The outer loop runs one pass at a time.
- The inner loop compares neighbouring values.
- A swap happens only when the left value is bigger.
- After all passes, the list becomes sorted in ascending order.

**Common doubt:** Bubble Sort uses nested loops, which is why it naturally fits the nested logic theme of this lesson.

![Bubble Sort vs Selection Sort — Bubble Sort swaps neighbours until large values settle right; Selection Sort picks the smallest remaining value and places it on the left](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-03-bubble-vs-selection-sort.png?v=20260704)

---

## Selection Sort — Step-by-Step Implementation

- **Official Definition:** **Selection Sort** is a sorting algorithm that repeatedly selects the smallest element from the unsorted part and places it at the next correct position.
- **In Simple Words:** Find the smallest remaining value and put it in the next slot from the left.
- **Real-Life Example:** Arranging coins from smallest to largest by picking the next smallest coin each time.

### Selection Sort Trace on Sample Data

Sort this list in ascending order:

`[91, 88, 91, 76, 95]`

| Pass | Smallest Found | Action | List After Pass |
|---|---|---|---|
| Pass 1 | `76` at unsorted part | Swap with first position | `[76, 88, 91, 91, 95]` |
| Pass 2 | `88` | Already in place | `[76, 88, 91, 91, 95]` |
| Pass 3 | `91` | Already in place | `[76, 88, 91, 91, 95]` |
| Pass 4 | `91` | Already in place | `[76, 88, 91, 91, 95]` |

Selection Sort grows the sorted part from the left side.

### Selection Sort Python Implementation

```python
def selection_sort(numbers):  # Define function to sort a list
    n = len(numbers)  # Store number of items
    for current_index in range(n - 1):  # Outer loop picks position to fill
        min_index = current_index  # Assume current position has smallest value
        for i in range(current_index + 1, n):  # Inner loop searches unsorted part
            if numbers[i] < numbers[min_index]:  # Check if smaller value found
                min_index = i  # Update index of smallest value
        temp = numbers[current_index]  # Store current value before swap
        numbers[current_index] = numbers[min_index]  # Place smallest value at current position
        numbers[min_index] = temp  # Move old value to smallest value's old position
    return numbers  # Return sorted list

scores = [91, 88, 91, 76, 95]  # Sample unsorted marks list
sorted_scores = selection_sort(scores)  # Call sorting function
print(sorted_scores)  # Display sorted result
```

**How the code works:**

- The outer loop selects the next position to fill.
- The inner loop finds the smallest value in the unsorted part.
- One swap per pass places the correct value on the left.
- Both Bubble Sort and Selection Sort use nested loops — one for passes or positions, one for comparisons.

---

## Using Sorting to Handle Duplicates

- **Official Definition:** **Duplicate handling** means detecting, counting, or removing repeated values in a dataset.
- **In Simple Words:** Duplicate handling answers the question, "Have I seen this value before?"
- **Real-Life Example:** Checking whether the same roll number was entered twice in an exam registration form.

### Why Sorting Helps with Duplicates

After sorting, equal values appear **next to each other**. That makes duplicate detection easier — you only need to compare neighbours instead of every pair.

| Method | Idea | Best When |
|---|---|---|
| Nested loops | Compare every pair | Small lists, learning phase |
| Sort + neighbour scan | Compare adjacent values after sorting | You already need sorted output |
| Dictionary frequency | Count each value while looping once | You need counts, not just yes/no |

![Sorting as a problem-solving tool — after sorting, detect duplicates from neighbours, find second largest below the max, and read top scores in order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session10/session10-04-sorting-applications.png?v=20260704)

### Problem: Check Duplicates After Sorting

**Problem statement:** Return `True` if any value appears more than once in a list.

**Logic plan:**

1. Sort the list first.
2. Scan adjacent values.
3. If any neighbour pair matches, duplicate exists.

```python
def bubble_sort(numbers):  # Reuse bubble sort function
    n = len(numbers)  # Store list length
    for pass_index in range(n - 1):  # Outer loop for passes
        for i in range(n - 1 - pass_index):  # Inner loop for neighbour comparisons
            if numbers[i] > numbers[i + 1]:  # Swap if out of order
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap values
    return numbers  # Return sorted list

roll_numbers = [101, 204, 101, 309, 204]  # Input list with duplicates
sorted_rolls = bubble_sort(roll_numbers.copy())  # Sort a copy so original stays unchanged
has_duplicate = False  # Flag for duplicate detection

for index in range(len(sorted_rolls) - 1):  # Loop through adjacent pairs
    if sorted_rolls[index] == sorted_rolls[index + 1]:  # Compare neighbours
        has_duplicate = True  # Duplicate found

print("Duplicate exists:", has_duplicate)  # Display final answer
```

**How the code works:**

- Sorting brings equal values together.
- One single loop compares neighbours after sorting.
- This is often simpler than checking every pair in the original unsorted list.

**Common mistake:** Sorting the original list when you still need the unsorted order later. Use `.copy()` when required.

---

## Finding the Second Largest Element

- **Official Definition:** The **second largest element** is the highest value that is strictly smaller than the maximum, or the second position in a properly ordered unique ranking depending on problem rules.
- **In Simple Words:** Not the top score — the next score below the top.
- **Real-Life Example:** In a singing competition, the winner gets first place. The **runner-up** is the second highest performer.

### Why This Problem Is Tricky

- The maximum value may appear **more than once**.
- The list may have only **one unique value**.
- Sorting helps, but you must read the answer carefully after sorting.

| Input | Sorted List | Second Largest |
|---|---|---|
| `[10, 40, 20, 40]` | `[10, 20, 40, 40]` | `20` if duplicates of max are ignored |
| `[95, 95, 88, 76]` | `[76, 88, 95, 95]` | `88` |
| `[7]` | `[7]` | No second largest |

### Method 1: Using Sorting

```python
def selection_sort(numbers):  # Reuse selection sort function
    n = len(numbers)  # Store list length
    for current_index in range(n - 1):  # Outer loop for positions
        min_index = current_index  # Start with current index as minimum
        for i in range(current_index + 1, n):  # Inner loop finds smallest in unsorted part
            if numbers[i] < numbers[min_index]:  # Update minimum index if smaller value found
                min_index = i  # Store new minimum index
        numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]  # Swap values
    return numbers  # Return sorted list

marks = [95, 95, 88, 76, 90]  # Input marks list
sorted_marks = selection_sort(marks.copy())  # Sort a copy of the list
maximum_value = sorted_marks[-1]  # Last item is largest in ascending sort
second_largest = None  # Placeholder for answer

for value in reversed(sorted_marks):  # Scan from largest to smallest
    if value < maximum_value:  # First value strictly smaller than maximum
        second_largest = value  # Store second largest answer
        break  # Stop after finding answer

print("Second largest:", second_largest)  # Display final result
```

**How the code works:**

- Sorting arranges values from smallest to largest.
- `sorted_marks[-1]` gives the maximum.
- Scanning from the end finds the first value strictly smaller than the maximum.
- This handles repeated maximum values correctly.

### Method 2: Using Two Variables Without Full Sort

```python
marks = [95, 95, 88, 76, 90]  # Input marks list
largest = marks[0]  # Start largest with first value
second_largest = None  # No second largest yet

for value in marks:  # Loop through all marks
    if value > largest:  # If current value beats largest
        second_largest = largest  # Old largest becomes second largest
        largest = value  # Update largest
    elif value < largest and value != second_largest:  # Value is below largest but candidate for second
        if second_largest is None or value > second_largest:  # Update second largest if needed
            second_largest = value  # Store new second largest

print("Largest:", largest)  # Display largest value
print("Second largest:", second_largest)  # Display second largest value
```

**How the code works:**

- One loop tracks both largest and second largest.
- When a new largest appears, the old largest moves to second place.
- This avoids sorting but needs careful conditions.

**Common doubt:** Always check the problem rules. Some platforms want the second distinct value; others want the second position in sorted order.

---

## Ordered Comparisons with Sorting

- **Official Definition:** An **ordered comparison** checks values in sequence after arranging data in ascending or descending order.
- **In Simple Words:** Once data is sorted, comparing ranks, prices, or marks becomes much easier.
- **Real-Life Example:** After arranging products by price low to high, finding the cheapest three items means reading the first three entries.

### Problem 1: Print Top Three Scores

**Problem statement:** Given a list of marks, print the three highest scores in descending order.

**Logic plan:**

1. Sort marks in ascending order.
2. Read the last three values.
3. Print them from highest to lowest.

```python
def bubble_sort(numbers):  # Sorting helper function
    n = len(numbers)  # Store list length
    for pass_index in range(n - 1):  # Outer loop for passes
        for i in range(n - 1 - pass_index):  # Inner loop for neighbour checks
            if numbers[i] > numbers[i + 1]:  # Swap if needed
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap values
    return numbers  # Return sorted list

marks = [78, 92, 85, 92, 64, 88]  # Input marks
sorted_marks = bubble_sort(marks.copy())  # Sort a copy
top_three = sorted_marks[-3:]  # Take last three values
top_three.reverse()  # Reverse to show highest first

print("Top three scores:")  # Heading for output
for score in top_three:  # Loop through top three values
    print(score)  # Print each score
```

**How the code works:**

- Sorting places highest values at the end.
- Slicing `[-3:]` takes the last three items.
- Reversing prints them from highest to lowest.

### Problem 2: Check Whether a List Is Already Sorted

**Problem statement:** Return `True` if a list is already in ascending order.

```python
numbers = [10, 20, 30, 40]  # Input list
is_sorted = True  # Assume list is sorted until proven otherwise

for index in range(len(numbers) - 1):  # Loop through adjacent pairs
    if numbers[index] > numbers[index + 1]:  # Compare current value with next value
        is_sorted = False  # Order is broken

print("Already sorted:", is_sorted)  # Display result
```

**How the code works:**

- One loop compares neighbours.
- If any left value is bigger than the right neighbour, the list is not sorted.
- This problem connects directly to how Bubble Sort detects out-of-order pairs.

### Problem 3: Merge Two Sorted Lists Conceptually

**Problem statement:** Given two small sorted lists, combine them into one sorted list using comparisons.

```python
list_a = [1, 4, 7]  # First sorted list
list_b = [2, 3, 8]  # Second sorted list
merged = []  # Empty list for merged result
index_a = 0  # Pointer for list_a
index_b = 0  # Pointer for list_b

while index_a < len(list_a) and index_b < len(list_b):  # While both lists have items left
    if list_a[index_a] <= list_b[index_b]:  # Pick smaller front value from list_a
        merged.append(list_a[index_a])  # Add chosen value to merged list
        index_a = index_a + 1  # Move pointer in list_a
    else:
        merged.append(list_b[index_b])  # Pick smaller front value from list_b
        index_b = index_b + 1  # Move pointer in list_b

while index_a < len(list_a):  # Add remaining items from list_a if any
    merged.append(list_a[index_a])  # Append current item
    index_a = index_a + 1  # Move pointer forward

while index_b < len(list_b):  # Add remaining items from list_b if any
    merged.append(list_b[index_b])  # Append current item
    index_b = index_b + 1  # Move pointer forward

print("Merged sorted list:", merged)  # Display final merged list
```

**How the code works:**

- Two pointers compare the front values of both sorted lists.
- The smaller value is appended to `merged`.
- Remaining values from one list are added after the main loop.
- Ordered comparison thinking prepares you for harder merge problems later.

---

## Practice Activity: Scholarship Shortlist Problem

I will solve one complete intermediate problem using analysis, nested logic, and sorting.

**Problem statement:** A scholarship committee receives exam scores in random order. Find the second highest unique score. Also check whether any duplicate score exists.

**My analysis:**

| Part | Answer |
|---|---|
| **Input** | `[91, 88, 91, 76, 95, 88]` |
| **Output** | Second highest = `91`, duplicate = `True` |
| **Constraints** | Values can repeat; list may be small |
| **Steps** | Sort → scan for duplicate neighbours → find second distinct value from end |

```python
def selection_sort(numbers):  # Sorting helper function
    n = len(numbers)  # Store list length
    for current_index in range(n - 1):  # Outer loop for positions
        min_index = current_index  # Assume current index holds minimum
        for i in range(current_index + 1, n):  # Inner loop finds minimum in unsorted part
            if numbers[i] < numbers[min_index]:  # Update minimum index if needed
                min_index = i  # Store smaller index
        numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]  # Swap values
    return numbers  # Return sorted list

scores = [91, 88, 91, 76, 95, 88]  # Input scores
sorted_scores = selection_sort(scores.copy())  # Sort a copy of scores
has_duplicate = False  # Duplicate flag

for index in range(len(sorted_scores) - 1):  # Check adjacent pairs after sorting
    if sorted_scores[index] == sorted_scores[index + 1]:  # Compare neighbours
        has_duplicate = True  # Mark duplicate found

maximum_value = sorted_scores[-1]  # Get maximum from sorted list
second_highest = None  # Placeholder for second highest unique value

for value in reversed(sorted_scores):  # Scan from largest to smallest
    if value < maximum_value:  # First value strictly below maximum
        second_highest = value  # Store second highest
        break  # Stop scanning

print("Duplicate exists:", has_duplicate)  # Show duplicate result
print("Second highest unique score:", second_highest)  # Show second highest result
```

**How the code works:**

- Sorting groups equal scores together for easy duplicate detection.
- Scanning from the end finds the first value below the maximum.
- One problem combines constraint analysis, sorting, and ordered reading.

---

## Practice Activity: Run and Test on Local Machine

I will test my intermediate solution locally using the same workflow from the previous lesson.

1. Open my practice folder in VS Code.
2. Create `intermediate_practice.py`.
3. Paste one nested-loop solution and one sorting-based solution.
4. Save the file.
5. Open Terminal inside VS Code.
6. Run `python3 intermediate_practice.py`.
7. Test with normal input, empty list, and repeated maximum values.

```python
# Quick local test for duplicate detection using nested loops
numbers = []  # Empty list test case
has_duplicate = False  # Default answer

if len(numbers) >= 2:  # Only compare when at least two items exist
    for i in range(len(numbers)):  # Outer loop
        for j in range(i + 1, len(numbers)):  # Inner loop
            if numbers[i] == numbers[j]:  # Compare different positions
                has_duplicate = True  # Duplicate found

print("Empty list duplicate check:", has_duplicate)  # Should print False
```

**How the code works:**

- Local testing helps you catch edge cases early.
- Empty list handling prevents unnecessary nested loop work.
- Running with `python3` keeps your workflow consistent.

---

## Common Mistakes and Doubts

- **Skipping constraint analysis:** Always ask whether values can repeat or lists can be empty before coding.
- **Wrong nested loop range:** Starting inner loop at `i + 1` avoids checking the same pair twice.
- **Confusing second largest with second position:** If maximum repeats, second position in sorted list may still be the maximum.
- **Sorting the original list by mistake:** Use `.copy()` when you still need the unsorted data.
- **Forgetting edge cases:** Test empty list, one item, all same values, and repeated maximum.
- **Mixing up Bubble Sort and Selection Sort movement:** Bubble Sort pushes large values right; Selection Sort places small values left.

When stuck, rewrite the problem as a table of input, output, constraints, and steps — then decide whether nested loops or sorting is the cleaner tool.

---

## Key Takeaways

- **Problem analysis** turns a word problem into a safe step-by-step algorithm by listing constraints and special cases first.
- **Nested logic** and **nested loops** help you compare pairs, scan substrings, and build frequency maps for moderately complex tasks.
- **Bubble Sort** and **Selection Sort** both use nested loops and are useful not only as topics but as tools inside bigger solutions.
- **Sorting** makes duplicate detection, second largest finding, and ordered comparisons easier when arranged values reveal the answer quickly.
- Combining **lists**, **strings**, **dictionaries**, **loops**, **conditionals**, and **sorting** on your local machine builds the confidence needed for harder DSA patterns in upcoming topics.

In the next lesson, you will continue strengthening structured problem-solving and move toward new application areas where clean logic and data handling matter even more.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| Problem analysis | Study constraints before coding | Input size, repeats, empty cases |
| Constraints | Rules and limits of a problem | "Values may repeat" |
| Algorithm | Fixed step-by-step solution plan | Sort → scan → answer |
| Nested loop | Loop inside another loop | `for i` then `for j` |
| Nested logic | Condition or loop inside another structure | `if` inside `for` |
| Bubble Sort | Sort by swapping neighbours | Compare `numbers[i]` and `numbers[i + 1]` |
| Selection Sort | Sort by selecting smallest each pass | Track `min_index` |
| Duplicate handling | Detect repeated values | Compare pairs or neighbours |
| Second largest | Next value below maximum | Scan sorted list from end |
| Ordered comparison | Compare values after sorting | Top three from sorted end |
| `.copy()` | Create list copy before sorting | `marks.copy()` |
| `range(i + 1, n)` | Inner loop after outer index | Avoid duplicate pair checks |
| `reversed(list)` | Loop from end to start | Find second largest |
| `python3 file.py` | Run Python file locally | `python3 practice.py` |
