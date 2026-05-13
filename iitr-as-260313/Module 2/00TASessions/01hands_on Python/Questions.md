
##### Subjective Question 1
#### A workshop team stores participant names in a list and attendance counts in a dictionary.

Write Python code that does all of the following:

- (a) defines a function named `attendance_report(names, attendance)`
- (b) iterates through the list of names
- (c) prints each name with its attendance count using an f-string
- (d) uses `attendance.get(name, 0)` so missing names do not cause an error
- (e) creates and returns a new list containing only the names whose attendance count is 3 or more
- (f) shows one sample function call with sample data



Write clean and readable code.

### **Submission Instructions**

1. Open **VS Code** any **Online Compiler** (make sure No AI Tool is used)
2. Run the code and verify its functionality
3. Once everything is working correctly, paste the final code in the answer box

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Define `attendance_report(names, attendance)` and loop through every name in the list.
2. For each name, read the count with `attendance.get(name, 0)` so missing keys do not raise an error.
3. Print each name and count with an f-string.
4. Append names with attendance of 3 or more to a new list and return that list.
5. Call the function once with sample data and print or use the returned list to show the result.

**Alternative approaches**

- Build the regular-attendee list with a list comprehension after the loop.
- Use `collections.Counter` on a separate frequency source if attendance were derived from raw logs instead of a pre-built dictionary.

**Reference solution (evaluators only — students may vary naming and print layout)**

```python
def attendance_report(names, attendance):
    regular_attendees = []
    for name in names:
        count = attendance.get(name, 0)
        print(f"{name}: {count}")
        if count >= 3:
            regular_attendees.append(name)
    return regular_attendees


names = ['Asha', 'Ravi', 'Meera']
attendance = {'Asha': 4, 'Ravi': 2, 'Kabir': 5}
regular = attendance_report(names, attendance)
print(regular)
```

**Sample output**

```text
Asha: 4
Ravi: 2
Meera: 0
['Asha']
```

---------------------------

##### Subjective Question 2

You are given a small list of student records. Each record contains the student's name, a list of scores, and whether the student is currently active.

## Dataset

```python
students = [
    {'name': 'asha', 'scores': [72, 85, 90], 'active': True},
    {'name': 'ravi', 'scores': [55, 60, 58], 'active': True},
    {'name': 'meera', 'scores': [88, 92, 95], 'active': False},
    {'name': 'kabir', 'scores': [63, 70, 75], 'active': True}
]
```

## Tasks

Write a Python program that does all of the following:

1. Define a function `calculate_average(scores)` that returns the average of a list of scores.
2. Define a function `get_status(average)` that returns:
   - `Strong` if the average is 80 or above
   - `Steady` if the average is 60 or above but below 80
   - `Needs Practice` if the average is below 60
3. Loop through the list and process only active students.
4. For each active student, print the student's name in title case, average score rounded to 2 decimals, and status.
5. Maintain a summary dictionary that counts how many active students fall under each status.
6. Print the final summary in a readable format.

## Expected Output

Your output should clearly show:

- each active student's name
- each active student's average score
- each active student's status
- final count of students in each status category

**Note:** Usage of IDEs or online IDEs such as Colab, Jupyter Notebook, VS Code, or similar tools is allowed. You may use them to verify your implementation. However, you must copy and paste the final code directly into the input box provided. Do not submit links to IDEs, notebooks, GitHub repositories, Google Drive files, or any external platform unless explicitly asked. Usage of AI tools will lead to disqualification.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Implement `calculate_average(scores)` as the sum of scores divided by the list length.
2. Implement `get_status(average)` with the three thresholds given in the question.
3. Loop through `students`, skip records where `active` is `False`, and compute average and status for each active student.
4. Print each active student's name in title case with the rounded average and status.
5. Update a summary dictionary keyed by status and print the final counts.

**Alternative approaches**

- Use `statistics.mean` for the average if learners are comfortable importing the standard library.
- Initialize the summary dictionary with zero counts for all three status labels before the loop so missing categories still print clearly.

**Reference solution (evaluators only — students may vary print formatting)**

```python
students = [
    {'name': 'asha', 'scores': [72, 85, 90], 'active': True},
    {'name': 'ravi', 'scores': [55, 60, 58], 'active': True},
    {'name': 'meera', 'scores': [88, 92, 95], 'active': False},
    {'name': 'kabir', 'scores': [63, 70, 75], 'active': True}
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_status(average):
    if average >= 80:
        return 'Strong'
    if average >= 60:
        return 'Steady'
    return 'Needs Practice'


summary = {'Strong': 0, 'Steady': 0, 'Needs Practice': 0}

for student in students:
    if not student['active']:
        continue
    average = calculate_average(student['scores'])
    status = get_status(average)
    print(student['name'].title(), round(average, 2), status)
    summary[status] += 1

print('Summary:', summary)
```

**Sample output**

```text
Asha 82.33 Strong
Ravi 57.67 Needs Practice
Kabir 69.33 Steady
Summary: {'Strong': 1, 'Steady': 1, 'Needs Practice': 1}
```

---------------------------

##### Subjective Question 3

A small library tracks how many times each book title has been borrowed.

## Dataset

```python
borrow_log = ['python basics', 'data structures', 'python basics', 'algorithms', 'data structures', 'python basics']
```

## Tasks

Write a Python program that does all of the following:

1. Start with an empty dictionary named `borrow_counts`.
2. Loop through `borrow_log` and update `borrow_counts` so each title maps to how many times it appears.
3. Define a function `most_borrowed(counts)` that returns the title with the highest count. If two titles tie, return either one.
4. Define a function `titles_above(counts, minimum)` that returns a list of titles borrowed at least `minimum` times.
5. Print the full dictionary, the most borrowed title, and the list returned by `titles_above(borrow_counts, 2)`.

Write clean and readable code.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Create `borrow_counts = {}` and loop through `borrow_log`.
2. Increment each title with `borrow_counts[title] = borrow_counts.get(title, 0) + 1`.
3. In `most_borrowed(counts)`, return the key with the highest value using `max(counts, key=counts.get)`.
4. In `titles_above(counts, minimum)`, collect titles whose counts meet the threshold.
5. Print the dictionary, the top title, and the filtered list for `minimum = 2`.

**Alternative approaches**

- Use `collections.Counter(borrow_log)` instead of manual counting.
- Sort titles by count before returning the top title if tie-breaking must be deterministic.

**Reference solution (evaluators only — students may vary print labels)**

```python
borrow_log = [
    'python basics',
    'data structures',
    'python basics',
    'algorithms',
    'data structures',
    'python basics'
]

borrow_counts = {}
for title in borrow_log:
    borrow_counts[title] = borrow_counts.get(title, 0) + 1


def most_borrowed(counts):
    return max(counts, key=counts.get)


def titles_above(counts, minimum):
    return [title for title, count in counts.items() if count >= minimum]


print(borrow_counts)
print(most_borrowed(borrow_counts))
print(titles_above(borrow_counts, 2))
```

**Sample output**

```text
{'python basics': 3, 'data structures': 2, 'algorithms': 1}
python basics
['python basics', 'data structures']
```

---------------------------

##### Subjective Question 4

You are given a seating grid for a classroom. Each inner list represents one row of seat labels.

## Dataset

```python
seating = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3', 'B4'],
    ['C1', 'C2']
]
```

## Tasks

Write a Python program that does all of the following:

1. Use nested loops to visit every seat in `seating`.
2. For each seat, print the seat label and its row number. Use 1-based row numbers in the output.
3. While looping, build a flat list named `all_seats` that contains every seat label in row order.
4. Define a function `count_by_row(grid)` that uses nested loops and returns a dictionary mapping each row number to the number of seats in that row.
5. Print `all_seats` and the dictionary returned by `count_by_row(seating)`.

Write clean and readable code.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Use nested loops with `enumerate(seating, start=1)` so row numbers are 1-based.
2. Print each seat label with its row number while appending labels to `all_seats`.
3. Implement `count_by_row(grid)` with nested loops that map each row number to `len(row)`.
4. Print `all_seats` and the dictionary returned by `count_by_row(seating)`.

**Alternative approaches**

- Flatten the grid with a list comprehension such as `[seat for row in seating for seat in row]`.
- Build the row-count dictionary with a dictionary comprehension over `enumerate(grid, start=1)`.

**Reference solution (evaluators only — students may vary print formatting)**

```python
seating = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3', 'B4'],
    ['C1', 'C2']
]

all_seats = []

for row_number, row in enumerate(seating, start=1):
    for seat in row:
        print(seat, row_number)
        all_seats.append(seat)


def count_by_row(grid):
    row_counts = {}
    for row_number, row in enumerate(grid, start=1):
        row_counts[row_number] = len(row)
    return row_counts


print(all_seats)
print(count_by_row(seating))
```

**Sample output**

```text
A1 1
A2 1
A3 1
B1 2
B2 2
B3 2
B4 2
C1 3
C2 3
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2']
{1: 3, 2: 4, 3: 2}
```

---------------------------

##### Subjective Question 5

A mentor wants to review weekly practice scores stored as a list of integers.

## Dataset

```python
scores = [42, 88, 55, 91, 67, 73, 49, 95, 60]
```

## Tasks

Write a Python program that does all of the following:

1. Define a function `filter_passing(values, passing_score)` that returns a new list containing only values greater than or equal to `passing_score`. Do not modify the original list.
2. Define a function `add_bonus(values, bonus)` that returns a new list with `bonus` added to every value.
3. Define a function `classify(values)` that returns a dictionary with keys `high`, `medium`, and `low`, where:
   - `high` counts values 80 or above
   - `medium` counts values from 60 up to but not including 80
   - `low` counts values below 60
4. Use `filter_passing(scores, 60)` and store the result in `qualified_scores`.
5. Pass `qualified_scores` into `add_bonus(..., 5)` and store the result in `adjusted_scores`.
6. Print `qualified_scores`, `adjusted_scores`, and `classify(scores)`.

Write clean and readable code.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Implement `filter_passing` and `add_bonus` so they return new lists without changing the input list.
2. Implement `classify` with separate counters for `high`, `medium`, and `low`.
3. Store `qualified_scores = filter_passing(scores, 60)`.
4. Pass that result into `add_bonus(..., 5)` and store `adjusted_scores`.
5. Print `qualified_scores`, `adjusted_scores`, and `classify(scores)`.

**Alternative approaches**

- Use `filter()` with a lambda for the passing filter, then convert the result to a list.
- Chain transformations in one expression only if the intermediate lists are still printed separately as required.

**Reference solution (evaluators only — students may vary helper style)**

```python
scores = [42, 88, 55, 91, 67, 73, 49, 95, 60]


def filter_passing(values, passing_score):
    return [value for value in values if value >= passing_score]


def add_bonus(values, bonus):
    return [value + bonus for value in values]


def classify(values):
    bands = {'high': 0, 'medium': 0, 'low': 0}
    for value in values:
        if value >= 80:
            bands['high'] += 1
        elif value >= 60:
            bands['medium'] += 1
        else:
            bands['low'] += 1
    return bands


qualified_scores = filter_passing(scores, 60)
adjusted_scores = add_bonus(qualified_scores, 5)

print(qualified_scores)
print(adjusted_scores)
print(classify(scores))
```

**Sample output**

```text
[88, 91, 67, 73, 95, 60]
[93, 96, 72, 78, 100, 65]
{'high': 3, 'medium': 3, 'low': 3}
```

---------------------------

##### Subjective Question 6

A billing helper should format an invoice line only after checking the amount.

## Tasks

Write a Python program that does all of the following:

1. Define a function `make_invoice_line(item_name, tax_rate)` that contains a nested function named `format_line(amount)`.
2. The nested function `format_line(amount)` should:
   - return `Invalid amount` if `amount` is less than or equal to 0
   - otherwise return a string in the form `Item: <item_name> | Amount: <amount> | Tax: <tax> | Total: <total>`, where `tax` and `total` are calculated using `tax_rate`
3. `make_invoice_line` should return the nested `format_line` function itself, not a formatted string.
4. Create one formatter by calling `make_invoice_line('Notebook', 0.18)`.
5. Use that returned function to print the result for amount `250`.
6. Use the same returned function to print the result for amount `-10`.

Write clean and readable code.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. Define `make_invoice_line(item_name, tax_rate)` with an inner function `format_line(amount)`.
2. Return `Invalid amount` when `amount <= 0`.
3. Otherwise compute `tax` and `total`, then return the formatted invoice string.
4. Return `format_line` from `make_invoice_line`, not the formatted string.
5. Create one formatter with `make_invoice_line('Notebook', 0.18)` and call it for `250` and `-10`.

**Alternative approaches**

- Use a closure that stores `item_name` and `tax_rate` in default arguments if learners want to avoid late-binding surprises in more advanced variants.
- Round `tax` and `total` before formatting if the teaching context prefers currency-style output.

**Reference solution (evaluators only — students may vary string layout)**

```python
def make_invoice_line(item_name, tax_rate):
    def format_line(amount):
        if amount <= 0:
            return 'Invalid amount'
        tax = amount * tax_rate
        total = amount + tax
        return f'Item: {item_name} | Amount: {amount} | Tax: {tax} | Total: {total}'

    return format_line


formatter = make_invoice_line('Notebook', 0.18)
print(formatter(250))
print(formatter(-10))
```

**Sample output**

```text
Item: Notebook | Amount: 250 | Tax: 45.0 | Total: 295.0
Invalid amount
```

---------------------------

##### Subjective Question 7

A text-processing pipeline should clean raw feedback and then summarize it.

## Dataset

```python
raw_feedback = '  Great   session!!!  Very helpful.  '
```

## Tasks

Write a Python program that does all of the following:

1. Define a function `clean_text(text)` that returns the text stripped of leading and trailing spaces and with all runs of whitespace replaced by a single space.
2. Define a function `word_stats(cleaned_text)` that returns a dictionary with:
   - `words`: the number of words in the cleaned text
   - `characters`: the number of characters in the cleaned text, excluding spaces
   - `longest_word`: the longest word in the cleaned text
3. Define a function `build_summary(stats)` that returns one readable sentence using the values from the dictionary returned by `word_stats`.
4. Link the functions in order: pass `raw_feedback` into `clean_text`, pass that result into `word_stats`, and pass that dictionary into `build_summary`.
5. Print the cleaned text, the stats dictionary, and the final summary sentence.

Write clean and readable code.

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. In `clean_text`, strip outer whitespace and collapse internal runs with `' '.join(text.strip().split())`.
2. In `word_stats`, split the cleaned text into words and build the required dictionary keys.
3. In `build_summary`, return one readable sentence that uses all three stats values.
4. Link the functions in order: `clean_text(raw_feedback)` → `word_stats(...)` → `build_summary(...)`.
5. Print the cleaned text, stats dictionary, and final summary sentence.

**Alternative approaches**

- Use `re.sub(r'\s+', ' ', text.strip())` in `clean_text` if learners prefer regular expressions.
- Compute `characters` with `sum(len(word) for word in words)` instead of removing spaces from the full string.

**Reference solution (evaluators only — students may vary summary wording)**

```python
raw_feedback = '  Great   session!!!  Very helpful.  '


def clean_text(text):
    return ' '.join(text.strip().split())


def word_stats(cleaned_text):
    words = cleaned_text.split()
    return {
        'words': len(words),
        'characters': len(cleaned_text.replace(' ', '')),
        'longest_word': max(words, key=len)
    }


def build_summary(stats):
    return (
        f"The feedback has {stats['words']} words, "
        f"{stats['characters']} characters without spaces, "
        f"and the longest word is '{stats['longest_word']}'."
    )


cleaned = clean_text(raw_feedback)
stats = word_stats(cleaned)
summary = build_summary(stats)

print(cleaned)
print(stats)
print(summary)
```

**Sample output**

```text
Great session!!! Very helpful.
{'words': 4, 'characters': 27, 'longest_word': 'session!!!'}
The feedback has 4 words, 27 characters without spaces, and the longest word is 'session!!!'.
```