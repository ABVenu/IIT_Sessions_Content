# Objective Assignment: Hands-on Logic Building & DSA Problem Solving – II

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

Meera joins two batch WhatsApp groups. Group A roll numbers are `[101, 204, 305, 410]`. Group B roll numbers are `[204, 410, 512]`.

She wants the rolls that appear in **both** groups.

What should her program return?

A. `[204, 410]`  
B. `[101, 204, 305, 410, 512]`  
C. `[101, 305, 512]`  
D. `[512]`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because common elements are values present in both lists — only `204` and `410`.

B is incorrect because that merges both lists instead of finding intersection. C is incorrect because those rolls appear in only one group. D is incorrect because `512` is only in Group B.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

Arjun writes nested loops to check every unique pair of scores in a list. He starts the outer loop at index `i` and wants the inner loop to avoid comparing a score with itself and avoid checking the same pair twice.

Where should the inner loop start?

A. `range(i + 1, n)`  
B. `range(0, n)`  
C. `range(i, n)`  
D. `range(n, i, -1)`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because starting at `i + 1` compares each index only with later indexes, so pairs are unique and self-pairs are skipped.

B is incorrect because it rechecks earlier indexes and self-pairs. C is incorrect because `j = i` compares an item with itself. D is incorrect and does not match the standard unique-pair pattern.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

Priya needs the second largest value from `[12, 45, 30, 45, 18]`. She creates an ascending sorted list and reads one index.

Which index gives the second-last value in that sorted list?

A. `size - 2`  
B. `size - 1`  
C. `0`  
D. `size`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because after ascending sort, `size - 1` is the last (largest) and `size - 2` is the second-last value.

B is incorrect because that is the largest. C is incorrect because that is the smallest. D is incorrect because `size` is out of range for zero-based indexes.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

Kabir wants every dish-price pair whose product is even. He finds the first valid pair and immediately `return`s from the function.

What is the **main problem** with that approach for this requirement?

A. Early return stops after one pair and can miss other valid pairs  
B. Python cannot multiply two integers  
C. Nested loops are illegal in Python  
D. Even products never exist for positive numbers

**Correct Answer:** A

**Answer Explanation:**  
A is correct because “all even-product pairs” needs collecting matches and returning at the end; early return keeps only the first match.

B is incorrect because integer multiplication works in Python. C is incorrect because nested loops are valid. D is incorrect because even products are common (any even factor makes an even product).

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

Neha solves “find any two numbers that add to target `10`” with nested index loops on `[2, 4, 6, 8]`.

She uses early return when a valid pair is found.

Which statement is **most accurate**?

A. Early return is appropriate because the problem asks for one valid pair, not every pair  
B. She must never return early; she must always print every possible pair  
C. She should sort first; otherwise nested loops cannot check sums  
D. She must use a value-based `for x in nums` inner loop starting after `i`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because pair-with-sum often needs any one match, so early return is valid.

B is incorrect for a one-pair requirement. C is incorrect because nested loops can check sums without sorting. D is incorrect because value-based loops do not give a clean `i + 1` start the way index-based `range` does.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Rohan finds the second largest using `sorted(nums)` and then reads an index. A friend says this approach costs about the same as a single `O(n)` pass that tracks largest and second largest in one loop.

Which statement is **most accurate**?

A. `sorted()` is typically about **O(n log n)**, while a careful single pass can be **O(n)**  
B. `sorted()` is always **O(1)** because reading an index is instant  
C. Nested pair loops are always faster than `sorted()` for every list size  
D. `sorted()` has the same cost as printing one number

**Correct Answer:** A

**Answer Explanation:**  
A is correct because built-in sort is commonly O(n log n), while one linear scan is O(n).

B is incorrect — index read is O(1), but sorting itself is not. C is incorrect because nested pair checks are O(n²) and are not always faster. D is incorrect because sorting does real work proportional to n log n.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

Sana is planning a list problem before coding.

Which planning steps are **useful**?

A. Write down input, output, and special cases before opening the editor  
B. Decide whether she needs one matching pair or all matching pairs  
C. Skip planning and type nested loops immediately to save time  
D. Dry-run a small example on paper before coding  
E. Ask whether the list can be empty or too short

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A, B, D, and E match good problem analysis: clarify I/O, one-vs-all output rule, dry-run, and edge cases.

C is incorrect because skipping planning often causes wrong early-return vs collect-all choices and longer debugging.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

Vikram writes a function that can return pairs with **even** product or **odd** product based on a flag `is_even`.

Which statements are correct?

A. `product % 2 == 0` identifies an even product  
B. Collecting pairs in a list and returning after both loops is needed when all matches matter  
C. Setting `is_even=False` should keep only odd-product pairs  
D. Hard-coding only the even rule means he must copy-paste a second function for odd products  
E. Using `return` inside the inner loop as soon as one even pair is found still returns every odd pair later automatically

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A–D match the even/odd product design: modulus check, collect-all behaviour, flag switching, and avoiding duplicated nested-loop code via a parameter.

E is incorrect because an early `return` exits the function immediately and does not continue collecting later pairs.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

Ananya compares three approaches on a list of size `n`.

Which statements are correct?

A. Checking all unique pairs with nested `i` / `j` loops is roughly **O(n²)**  
B. `sorted(nums)` then reading `size - 2` is roughly **O(n log n)** overall  
C. A single loop that updates largest and second largest can be **O(n)**  
D. Nested unique-pair loops are **O(1)** because each pair is checked only once  
E. Starting the inner loop at `i + 1` avoids self-pairs and repeated pair orderings

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the complexity and indexing ideas from the lesson.

D is incorrect — “each pair once” still means about n²/2 checks, which is O(n²), not O(1).

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

Farhan debugs a pair-with-sum function on `nums = [1, 2, 3, 4, 5]` and `target = 7`.

Which observations are correct for an index-based nested solution with early return?

A. A valid pair such as `[2, 5]` or `[3, 4]` can be returned depending on loop order  
B. If no pair sums to the target, returning `[]` is a sensible empty result  
C. Using `for value in nums` for both loops makes it easy to start the inner loop at `i + 1`  
D. Comparing `nums[i] + nums[j]` only when `j > i` avoids using the same index twice  
E. Early return is wrong here because pair-with-sum must always return every valid pair

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D match the taught pair-with-sum behaviour: one valid pair is enough, empty result when none, and `j` after `i` prevents self-use.

C is incorrect because value-based loops do not naturally expose the outer index for `range(i + 1, n)`. E is incorrect for the common “find one pair” version that uses early return.
