# Subjective Assignment: Character Counter and Dictionary Report

## Practical Task (Medium)

A small text-analysis tool is needed for checking how many times each character appears in a word or short text. Build a Python program that uses a dictionary to count character frequency and then prints a useful report.

### Requirements

Write a Python program that:

1. Takes one string input from the user.
2. Creates an empty dictionary named `counts`.
3. Loops through every character in the input string.
4. Uses `get(character, 0)` to safely update the count of each character.
5. Prints the final dictionary of character counts.
6. Prints all unique characters using `keys()`.
7. Prints all count values using `values()`.
8. Prints each character and its count using `items()`.
9. Prints the number of unique characters using `len()`.
10. Prints the unique characters in sorted order using `sorted()`.
11. Prints the highest frequency using `max(counts.values())`.
12. Prints the lowest frequency using `min(counts.values())`.
13. Prints the total number of counted characters using `sum(counts.values())`.

### Input Format

One line containing a string.

### Example Input

```text
banana
```

### Expected Output

```text
Character counts: {'b': 1, 'a': 3, 'n': 2}
Unique characters: dict_keys(['b', 'a', 'n'])
Count values: dict_values([1, 3, 2])
Character report:
b appears 1 time(s)
a appears 3 time(s)
n appears 2 time(s)
Number of unique characters: 3
Sorted unique characters: ['a', 'b', 'n']
Highest frequency: 3
Lowest frequency: 1
Total characters counted: 6
```

### Constraints

- The input string will contain at least one character.
- Use only concepts covered here: dictionaries, key-value pairs, `get()`, `keys()`, `values()`, `items()`, `len()`, `sorted()`, `max()`, `min()`, and `sum()`.
- Do not use external libraries.
- Treat uppercase and lowercase as different characters. For example, `A` and `a` should be counted separately.
- Spaces may be counted as characters if they are present in the input.
- Write your complete program in [OneCompiler Python](https://onecompiler.com/python).

### Submission Instruction

1. Open [https://onecompiler.com/python](https://onecompiler.com/python) and create a new Python file.
2. Write your complete program in the editor, then click **Run** and verify the output.
3. Click the **Save** button at the top right.
4. Enter your **assignment name**, set visibility to **Public**, and save.
5. Click the **Share** button, copy the link, and submit that link in the answer box on the LMS.

![Step - 1](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/5b930478-03c2-4255-a724-d0990da5e4f4/C0AFXttOJJhW3o1S.png)

![Step-2](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/c817d308-66ca-4b5a-8579-db26951ad1a2/PGcKY2hqUQgysgPo.png)

---

## Answer Explanation

### Ideal Solution Walkthrough

The program should start by taking a string input. Then it should create an empty dictionary because the counts are not known before reading the string.

For every character, the program should use `counts.get(character, 0)` to get the old count. If the character is not present, the default count should be `0`; then the program should add `1` and store the updated value back in the dictionary.

After the dictionary is ready, the program should use dictionary methods and built-in functions to print the complete report.

### Complete Code

```python
# Take a string input from the user
text = input("Enter text: ")

# Create an empty dictionary to store character counts
counts = {}

# Loop through every character in the input text
for character in text:
    # Get the current count of the character, or 0 if it is not present
    old_count = counts.get(character, 0)

    # Increase the count by 1
    new_count = old_count + 1

    # Store the updated count in the dictionary
    counts[character] = new_count

# Print the complete dictionary of character counts
print("Character counts:", counts)

# Print all unique characters using keys()
print("Unique characters:", counts.keys())

# Print all count values using values()
print("Count values:", counts.values())

# Print every character and its count using items()
print("Character report:")
for character, count in counts.items():
    # Print one character-count pair
    print(f"{character} appears {count} time(s)")

# Print the number of unique characters using len()
print("Number of unique characters:", len(counts))

# Print unique characters in sorted order using sorted()
print("Sorted unique characters:", sorted(counts))

# Print the highest count using max() on values
print("Highest frequency:", max(counts.values()))

# Print the lowest count using min() on values
print("Lowest frequency:", min(counts.values()))

# Print the total number of counted characters using sum()
print("Total characters counted:", sum(counts.values()))
```

### Why This Code Works

- `counts = {}` creates an empty dictionary.
- Each character from the input becomes a dictionary key.
- The value against each key stores how many times that character has appeared.
- `get(character, 0)` avoids errors when a character appears for the first time.
- `keys()`, `values()`, and `items()` help inspect the dictionary in different ways.
- `len(counts)` counts unique characters.
- `sorted(counts)` sorts the keys.
- `max(counts.values())`, `min(counts.values())`, and `sum(counts.values())` analyse the numeric count values.

### Alternative Approach

The same counting logic can be written in a shorter form:

```python
# Take input from the user
text = input("Enter text: ")

# Create an empty dictionary
counts = {}

# Count every character using get() in one line
for character in text:
    # Safely increase the count for the current character
    counts[character] = counts.get(character, 0) + 1

# Print the final result
print(counts)
```

This shorter approach is also correct, but the full solution is better for this assignment because it prints the complete dictionary report.
