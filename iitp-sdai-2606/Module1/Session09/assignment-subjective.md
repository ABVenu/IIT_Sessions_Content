# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

**Priya** volunteers at her college **Coding Club Hackathon** help desk. After the morning round, she receives the team scores below and must prepare a quick report for the organizers.

```python
scores = [67, 89, 45, 89, 72, 45, 91]
```

She needs a small Python program that:

1. Finds the **highest score** in the list **without using** the built-in `max()` function.
2. Finds all **duplicate scores** — scores that appear **more than once** in the list.
3. Uses a **dictionary** with `.get()` to build the frequency map.
4. Uses `.items()` to check which scores have a count greater than `1`.
5. Stores duplicate scores in a list and prints the final report.

### Expected Output

Your program must print the output in **exactly** this format:

```text
Scores: [67, 89, 45, 89, 72, 45, 91]
Highest score: 91
Duplicate scores: [89, 45]
```

### Constraints

- Use `for` loops and `if` conditions only — no built-in `max()`, `sorted()`, or `Counter`.
- Build the frequency dictionary using `counts[score] = counts.get(score, 0) + 1`.
- Find duplicates using `for key, value in counts.items()`.
- Add duplicate scores to a result list using `append()`.
- Keep the entire solution in **one `.py` file**.
- Add at least **one comment** (`#`) explaining what your program does.

### Submission Instruction

1. Write your complete program in **VS Code** as a single `.py` file.
2. Save the file, open the integrated **Terminal**, and run it using `python3 your_file_name.py`.
3. Verify that your Terminal output matches the expected format exactly.
4. Copy your **complete code** and paste it in the **answer box** on the LMS.
5. Also paste the **Terminal output** below your code in the same answer box.

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Store the given score list in a variable.  
2. Assume the first score is the highest, then loop through all scores and update the highest when a bigger value is found.  
3. Build a frequency dictionary using `.get(score, 0) + 1` for each score.  
4. Loop through `counts.items()` and append any score whose count is greater than `1` to a duplicates list.  
5. Print the original list, highest score, and duplicate scores in the required format.

### Reference Solution — `hackathon_score_report.py`

```python
# Hackathon score report: highest score and duplicate score finder

scores = [67, 89, 45, 89, 72, 45, 91]
highest = scores[0]  # Start by assuming the first score is the highest

for score in scores:  # Check every score in the list
    if score > highest:  # If current score is bigger, update the highest
        highest = score

counts = {}  # Dictionary to store how many times each score appears
duplicates = []  # List to store scores that appear more than once

for score in scores:  # Build frequency map for each score
    counts[score] = counts.get(score, 0) + 1

for key, value in counts.items():  # Check each score and its count
    if value > 1:  # If count is greater than 1, it is a duplicate
        duplicates.append(key)

print("Scores:", scores)
print("Highest score:", highest)
print("Duplicate scores:", duplicates)
```

### Sample Verification

Starting list: `[67, 89, 45, 89, 72, 45, 91]`

- **Highest score:** `91` — found by comparing each value without using `max()`.  
- **Frequency map:** `{67: 1, 89: 2, 45: 2, 72: 1, 91: 1}`.  
- **Duplicates:** `89` and `45` both appear twice, so output is `[89, 45]`.  
- Final Terminal output matches the required three-line format.

### Alternative Approaches

- You may use `i = i + 1` style increments or `i += 1` — both are valid.  
- Duplicate order follows dictionary insertion order in Python 3.7+, which gives `[89, 45]` for this input.  
- You can add `print()` statements while developing to dry-run how `counts` grows after each loop step.
