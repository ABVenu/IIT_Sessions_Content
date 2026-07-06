# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**Rahul** helps his college library team arrange returned books on a shelf by **call number** from smallest to largest before the next shift.

What is the **best description** of what he is doing?

A. Encrypting book titles so only librarians can read them  
B. Arranging data in a specific order, usually ascending or descending  
C. Deleting duplicate books from the database  
D. Converting every book title into a single integer  

**Correct Answer:** B

**Answer Explanation:**  
**Sorting** means arranging items in a chosen order — such as ascending call numbers or descending popularity scores.

**Why other options are wrong:**  
- A: Sorting is about order, not encryption.  
- C: Removing duplicates is a different operation.  
- D: Sorting rearranges existing values; it does not force every title to become one integer.

---

## Q2 (MCQ, Easy)

During **sports day**, volunteers line up students by height using a method where each volunteer compares **two neighbours** and swaps them if the taller student is standing on the left.

Which sorting algorithm matches this idea most closely?

A. Selection Sort  
B. Bubble Sort  
C. Printing the list without changing the order of values  
D. Using Python's built-in `sorted()` function  

**Correct Answer:** B

**Answer Explanation:**  
**Bubble Sort** repeatedly compares **adjacent** values and swaps them when they are out of order, pushing larger values toward the end over multiple passes.

**Why other options are wrong:**  
- A: Selection Sort finds the smallest remaining value and places it at the next position — it does not focus on neighbour swaps.  
- C: Printing displays values but does not rearrange them into sorted order.  
- D: The scenario describes the step-by-step logic of Bubble Sort, not calling a built-in sorting function.

---

## Q3 (MCQ, Easy)

A coding club stores member roll numbers in this list:

```python
rolls = [1042, 1015, 1088]
```

What is the **index** of the value `1015`?

A. `0`  
B. `1`  
C. `2`  
D. `1015`  

**Correct Answer:** B

**Answer Explanation:**  
Python list indices start at `0`. In `[1042, 1015, 1088]`, index `0` is `1042`, index `1` is `1015`, and index `2` is `1088`.

**Why other options are wrong:**  
- A: Index `0` holds `1042`, not `1015`.  
- C: Index `2` holds `1088`.  
- D: `1015` is the value itself, not its index position.

---

## Q4 (MCQ, Easy)

**Anita** writes this line in her notebook:

```python
single_score = 87
```

She asks: "Can I sort this one score into ascending order?"

What is the **correct answer**?

A. Yes, Bubble Sort works on a single number  
B. Yes, but only Selection Sort works on a single number  
C. No, sorting needs multiple items in a list or collection  
D. No, because Python cannot store numbers in variables  

**Correct Answer:** C

**Answer Explanation:**  
Sorting rearranges **multiple** values relative to one another. A single value like `87` has nothing to compare or reorder.

**Why other options are wrong:**  
- A and B: Neither algorithm applies meaningfully to one isolated value.  
- D: Python can store numbers in variables; the issue is that one value cannot be sorted.

---

## Q5 (MCQ, Moderate)

**Karan** runs **Bubble Sort** in ascending order on this list:

```python
scores = [5, 1, 4, 2, 8]
```

After **Pass 1** is complete, what will the list look like?

A. `[1, 2, 4, 5, 8]`  
B. `[1, 4, 2, 5, 8]`  
C. `[5, 1, 4, 2, 8]`  
D. `[1, 5, 4, 2, 8]`  

**Correct Answer:** B

**Answer Explanation:**  
In Pass 1, adjacent comparisons bubble the largest value `8` to the last position:

- `5` and `1` → swap → `[1, 5, 4, 2, 8]`  
- `5` and `4` → swap → `[1, 4, 5, 2, 8]`  
- `5` and `2` → swap → `[1, 4, 2, 5, 8]`  
- `5` and `8` → no swap → `[1, 4, 2, 5, 8]`

**Why other options are wrong:**  
- A: The list is fully sorted only after all passes, not after Pass 1.  
- C: This is the starting list before any swaps.  
- D: This is the list after only the first comparison, not after the full pass.

---

## Q6 (MCQ, Moderate)

**Priya** is arranging playing cards from smallest to largest. On each round, she scans the remaining unsorted cards, finds the **smallest** card, and places it in the next correct position on the left.

Which algorithm follows this idea?

A. Bubble Sort  
B. Selection Sort  
C. Sorting a single integer  
D. Printing the list without changing it  

**Correct Answer:** B

**Answer Explanation:**  
**Selection Sort** repeatedly selects the smallest value from the unsorted portion and swaps it into the current position on the left.

**Why other options are wrong:**  
- A: Bubble Sort focuses on adjacent comparisons and bubbling larger values to the right.  
- C: A single integer cannot be sorted.  
- D: Printing does not rearrange values.

---

## Q7 (MSQ, Moderate)

A hackathon leaderboard tool uses **Bubble Sort** to arrange scores in ascending order.

Which statements about Bubble Sort are **correct**?

A. It compares adjacent elements in each pass  
B. After one complete pass, the largest value moves toward the end  
C. Its typical worst-case time complexity is O(n^2)  
D. It always finishes in exactly one pass for every input list  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Bubble Sort compares neighbours, bubbles the largest value rightward each pass, and uses nested loops that lead to **O(n^2)** worst-case time.

**Why other options are wrong:**  
- D: Most lists need multiple passes — one pass is not enough in general.

---

## Q8 (MSQ, Moderate)

**Vikram** analyses why both **Bubble Sort** and **Selection Sort** are called **O(n^2)** algorithms for a list of size `n`.

Which statements are **correct**?

A. The outer loop runs roughly `n` times  
B. The inner loop also runs roughly `n` times in the worst case  
C. Two nested loops always guarantee O(n^2) in every Python program  
D. The total work grows roughly like `n × n` in the worst case  

**Correct Answers:** A, B, D

**Answer Explanation:**  
For both elementary sorting algorithms, each loop runs about `n` times, so worst-case work scales as **n × n**, giving **O(n^2)**.

**Why other options are wrong:**  
- C: Nested loops alone do not automatically mean O(n^2) — you must check how many times each loop actually runs.

---

## Q9 (MSQ, Hard)

**Meera** compares **Bubble Sort** and **Selection Sort** while preparing a report for her programming lab.

Which statements are **correct**?

A. Both algorithms can sort inside the same list using O(1) extra space  
B. Both have worst-case time complexity O(n^2)  
C. Selection Sort usually performs more swaps inside a single pass than Bubble Sort  
D. On nearly sorted data, Bubble Sort may finish earlier than Selection Sort  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Both sort in place with constant extra variables (**O(1)** space) and **O(n^2)** worst-case time. Bubble Sort can stop early when few swaps are needed on nearly sorted data; Selection Sort still scans for the minimum each pass.

**Why other options are wrong:**  
- C: Bubble Sort can swap many times in one pass; Selection Sort usually swaps once per pass after finding the minimum.

---

## Q10 (MSQ, Hard)

**Arjun** reviews this **Selection Sort** function:

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```

Which statements about this code are **correct**?

A. `min_index = i` starts by assuming the current position holds the smallest value so far  
B. `range(i + 1, n)` searches only the unsorted part of the list  
C. After each outer-loop iteration, the sorted region on the left grows by one position  
D. This function has O(n) time complexity because Python has only two loops  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Selection Sort assumes the current index is the minimum, scans the rest of the list, updates `min_index`, swaps once, and grows the sorted left side each pass.

**Why other options are wrong:**  
- D: Two nested loops that each run about `n` times give **O(n^2)** time, not O(n).
