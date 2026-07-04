# Hands-on Logic Building, Development Setup & DSA Problem Solving – I

## What You Will Learn in This Lesson

You have already learned how to use **lists**, **strings**, **dictionaries**, **loops**, **conditionals**, and **functions** to solve problems step by step. You have also seen how sorting algorithms work by comparing and rearranging values inside a list.

In this lesson, you will move from browser-based coding to **local development** on your own laptop. You will set up **Python**, **VS Code**, and the **Terminal**, then write and run programs locally. After that, you will practice **logic building** — breaking a problem into inputs, outputs, conditions, and steps — and solve beginner **DSA** problems using lists, strings, and dictionaries.

By the end, you will be able to set up a working Python environment, run `.py` files from your machine, and solve basic coding problems using the core data structures you already know.

---

## Why Move from Online Compiler to Local Setup?

- **Official Definition:** **Local development** means writing, saving, and running code directly on your own computer instead of only inside a browser tool.
- **In Simple Words:** Local setup means your laptop becomes your coding workspace — like having your own study table instead of using a shared cyber cafe computer every time.
- **Real-Life Example:** Online compilers are useful for quick practice, but real projects, internships, and job interviews expect you to work with files, folders, and a code editor on your machine.

Local setup helps because:

- You can save many programs as separate files and organize them in folders.
- You can use a professional editor like **VS Code** with helpful features such as syntax highlighting and error hints.
- You can run programs from the **Terminal**, which is how developers work in companies.
- You can build confidence before solving problems on platforms like **LeetCode** and **HackerRank**.

![Local development big picture — move from browser online compiler to your laptop with Python 3, VS Code, and Terminal using python3 to run saved files](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-01-local-dev-big-picture.png?v=20260704)

---

## Installing Python on Your Laptop

- **Official Definition:** **Python** is the programming language interpreter that reads your `.py` files and executes the instructions inside them.
- **In Simple Words:** Python is the engine that runs your code. Without installing it, your laptop cannot understand Python files.
- **Real-Life Example:** Installing Python is like installing a music player app — once it is there, you can play any song file saved on your device.

### Steps to Install Python

1. Open the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest stable version for your operating system — **Windows**, **macOS**, or **Linux**.
3. Run the installer.
4. On **Windows**, tick the option **"Add Python to PATH"** before clicking Install. This step is very important.
5. Finish installation and restart your Terminal or VS Code if they were already open.

### One Command for Software Development: Use `python3`

In professional software development, teams use **`python3`** as the standard command to run Python 3 programs.

- **`python3`** clearly means Python 3 — the version used in companies, cloud servers, and modern projects.
- **`python`** alone can mean different things on different laptops, so developers avoid mixing both commands.

**Use `python3` everywhere in this course** — in Terminal, VS Code, practice files, and LeetCode local testing. Do not switch between `python` and `python3`. Pick one habit and stay consistent.

### Check Whether Python Is Installed

Open **Terminal** (macOS/Linux) or **Command Prompt / PowerShell** (Windows) and run:

```bash
python3 --version  # Shows installed Python 3 version
```

**How the code works:**

- `python3 --version` asks the system which Python 3 version is available.
- If you see something like `Python 3.12.1`, installation is successful.
- If you see an error like `command not found`, Python is not added to PATH yet — reinstall and tick **"Add Python to PATH"** on Windows.

**Common doubt:** If `python3` does not work after installation, close and reopen Terminal or VS Code once. Your system needs a fresh session to read the updated PATH.

---

## Setting Up VS Code

- **Official Definition:** **Visual Studio Code (VS Code)** is a free code editor used to write, edit, and manage source code files.
- **In Simple Words:** VS Code is your digital notebook for coding — clean, fast, and designed for programmers.
- **Real-Life Example:** If Python is the engine, VS Code is the steering wheel and dashboard that helps you drive comfortably.

### Steps to Install and Open VS Code

1. Download VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Install it like any normal desktop application.
3. Open VS Code after installation.
4. Click the **Extensions** icon on the left sidebar.
5. Search for **Python** and install the extension published by **Microsoft**.
6. Optionally install **Pylance** for better code suggestions.

### Create Your First Python File in VS Code

1. Click **File → Open Folder** and choose a folder such as `python_practice`.
2. Click **New File** and save it as `hello_local.py`.
3. Type your Python code inside the editor.
4. Save the file using **Ctrl + S** (Windows/Linux) or **Cmd + S** (macOS).

```python
# My first locally saved Python program
message = "Hello from my laptop"  # Store a text message in a variable
print(message)  # Display the message on the screen
```

**How the code works:**

- The file name ends with `.py`, which tells the system this is a Python program.
- VS Code highlights keywords like `print` in color, which makes reading easier.
- Saving the file stores your work permanently on your laptop.

**Common mistake:** Saving a file without the `.py` extension. Always use names like `practice.py`, not `practice.txt`.

---

## Understanding the Terminal

- **Official Definition:** A **Terminal** (also called **Command Line** or **Shell**) is a text-based interface where you type commands to control your computer.
- **In Simple Words:** The Terminal is a place where you type instructions instead of clicking buttons.
- **Real-Life Example:** Using the Terminal is like telling a shopkeeper exactly what you want by speaking clearly, instead of pointing at many shelves.

Developers use the Terminal to:

- Check whether Python is installed.
- Move between folders.
- Run Python files directly.
- Install libraries later in the course.

### Useful Terminal Commands

| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print current folder path | Shows where you are |
| `ls` | List files in current folder | macOS/Linux |
| `dir` | List files in current folder | Windows |
| `cd folder_name` | Change directory | `cd python_practice` |
| `cd ..` | Go one folder back | Move to parent folder |
| `python3 file.py` | Run a Python file | `python3 hello_local.py` |

### Open Terminal Inside VS Code

1. Open your project folder in VS Code.
2. Click **Terminal → New Terminal** from the top menu.
3. A Terminal panel opens at the bottom of VS Code.
4. Type commands there without leaving the editor.

This is the most comfortable workflow for beginners because you can write code above and run commands below in the same window.

![VS Code integrated workflow — write and save a Python file in the editor, then run python3 in the integrated Terminal to see output below](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-02-vscode-terminal-workflow.png?v=20260704)

---

## Write, Save, and Run Python Programs Locally

- **Official Definition:** **Program execution** is the process of giving a saved source file to the Python interpreter so it can run line by line.
- **In Simple Words:** Running a program means telling Python, "Please read this file and do what it says."
- **Real-Life Example:** Saving a `.py` file is like writing an exam answer sheet. Running it is like submitting that sheet to the examiner for checking.

### Full Workflow

1. Create a folder for practice, such as `dsa_practice`.
2. Open that folder in VS Code.
3. Create a file named `sum_numbers.py`.
4. Write complete Python code and save it.
5. Open the integrated Terminal.
6. Run the file using `python3 sum_numbers.py`.
7. Read the output shown in the Terminal.

```python
# Program to add two numbers entered by the user
first_number = int(input("Enter first number: "))  # Read first number as integer
second_number = int(input("Enter second number: "))  # Read second number as integer
total = first_number + second_number  # Add both numbers
print("Sum is:", total)  # Show the final result
```

**How the code works:**

- `input()` reads text typed by the user.
- `int()` converts that text into a whole number.
- The `+` operator adds both numbers.
- `print()` displays the answer in the Terminal.

**Common mistakes:**

- Running the command from the wrong folder — use `cd` to enter the folder where the file is saved.
- Forgetting to save the file before running it — unsaved changes will not appear in output.
- Spelling the file name incorrectly in the Terminal — file names are case-sensitive on macOS/Linux.

---

## Logic Building — How to Think Before Coding

- **Official Definition:** **Logic building** is the process of converting a problem statement into clear inputs, outputs, conditions, and step-by-step instructions before writing code.
- **In Simple Words:** Logic building means planning the solution on paper first, then coding.
- **Real-Life Example:** Before cooking biryani, you check ingredients, decide serving size, and follow steps in order. Coding works the same way.

Every beginner DSA problem can be broken into four parts:

| Part | Question to Ask | Example |
|---|---|---|
| **Input** | What data am I receiving? | A list of marks |
| **Output** | What answer must I return or print? | Highest mark |
| **Conditions** | What special cases exist? | Empty list, negative values |
| **Steps** | What actions happen in order? | Loop, compare, update answer |

### Sample Logic Template

For the problem "Find the largest number in a list":

- **Input:** `[45, 12, 78, 9]`
- **Output:** `78`
- **Conditions:** If the list has only one item, that item is the answer.
- **Steps:**
  1. Assume the first value is the largest.
  2. Visit every remaining value using a loop.
  3. If a value is bigger, update the largest.
  4. Print the final largest value.

This template works for most beginner problems in this lesson.

![Logic building framework — break every problem into Input, Output, Conditions, and Steps before writing code, like following a recipe before cooking](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-03-logic-building-framework.png?v=20260704)

---

## Beginner DSA Problem Solving with Lists

- **Official Definition:** A **list problem** is a coding question where the main data is stored in a Python list and solved using loops and conditionals.
- **In Simple Words:** You receive a row of values and must calculate something from them.
- **Real-Life Example:** Finding the highest score in a class test sheet written as a list of marks.

![Beginner DSA with lists, strings, and dictionaries — use loops and conditionals to solve maximum, vowel count, frequency, and Two Sum style problems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-04-dsa-structures-problems.png?v=20260704)

### Problem 1: Find the Maximum Value in a List

**Problem statement:** Given a list of numbers, find and print the largest number.

**Logic plan:**

- Input: `[10, 45, 2, 89, 33]`
- Output: `89`
- Steps: Start with first value as max, compare with others, update when needed.

```python
numbers = [10, 45, 2, 89, 33]  # Input list of numbers
maximum_value = numbers[0]  # Assume first number is the largest for now

for value in numbers:  # Visit each number one by one
    if value > maximum_value:  # Check whether current value is bigger
        maximum_value = value  # Update the largest value found so far

print("Maximum value is:", maximum_value)  # Display the final answer
```

**How the code works:**

- `maximum_value = numbers[0]` sets a starting guess.
- The loop checks every value in the list.
- The `if` block updates the answer only when a bigger value appears.
- After the loop ends, `maximum_value` holds the correct result.

### Problem 2: Count How Many Numbers Are Even

**Problem statement:** Count how many numbers in a list are divisible by 2.

```python
numbers = [4, 7, 10, 13, 20, 25]  # Input list
even_count = 0  # Start counter at zero

for value in numbers:  # Check each number
    if value % 2 == 0:  # If remainder on division by 2 is zero, number is even
        even_count = even_count + 1  # Increase the counter

print("Even count is:", even_count)  # Show final count
```

**How the code works:**

- `%` gives the remainder after division.
- `value % 2 == 0` means the number is even.
- `even_count` increases only when the condition is true.

### Problem 3: Create a New List of Squares

**Problem statement:** For each number in a list, store its square in a new list.

```python
numbers = [1, 2, 3, 4, 5]  # Input list
squares = []  # Empty list to store results

for value in numbers:  # Visit each number
    square_value = value * value  # Multiply number by itself
    squares.append(square_value)  # Add result to the new list

print("Squares:", squares)  # Display the final list
```

**How the code works:**

- `squares = []` creates an empty output list.
- `append()` adds each computed square at the end.
- The original list stays unchanged while a new list is built.

---

## Beginner DSA Problem Solving with Strings

- **Official Definition:** A **string problem** is a coding question where the main data is text and is solved using indexing, loops, and conditionals.
- **In Simple Words:** You receive a word or sentence and must check, count, or transform characters.
- **Real-Life Example:** Checking whether a PAN card name matches the spelling on an Aadhaar card.

### Problem 1: Count Vowels in a String

**Problem statement:** Count how many vowels (`a, e, i, o, u`) appear in a given word.

```python
word = "education"  # Input string
vowels = "aeiou"  # Allowed vowel characters
count = 0  # Start vowel counter at zero

for character in word:  # Visit each character one by one
    if character in vowels:  # Check whether character is a vowel
        count = count + 1  # Increase count when vowel is found

print("Vowel count is:", count)  # Display the final answer
```

**How the code works:**

- `for character in word` loops through each letter.
- `character in vowels` checks membership in the vowel set.
- The counter increases only for vowel letters.

### Problem 2: Check Whether a String Is a Palindrome

**Problem statement:** Return whether a string reads the same forward and backward.

```python
text = "madam"  # Input string
reversed_text = ""  # Empty string to build reverse version

for index in range(len(text) - 1, -1, -1):  # Loop from last index to first index
    reversed_text = reversed_text + text[index]  # Add character to reverse string

if text == reversed_text:  # Compare original and reversed strings
    print("Palindrome")  # Same forward and backward
else:
    print("Not a palindrome")  # Different forward and backward
```

**How the code works:**

- `range(len(text) - 1, -1, -1)` moves backward through indexes.
- `reversed_text` stores the reversed form.
- Final `if` compares both strings.

**Common doubt:** You can also solve this using two pointers or slicing, but the loop method is easier to trace as a beginner.

### Problem 3: Count Words in a Sentence

**Problem statement:** Count how many words are present in a sentence separated by spaces.

```python
sentence = "Python is easy to learn"  # Input sentence
words = sentence.split(" ")  # Split sentence into a list of words
word_count = len(words)  # Count items in the list

print("Word count is:", word_count)  # Display the answer
```

**How the code works:**

- `split(" ")` breaks the sentence at each space.
- `len(words)` counts how many word pieces were created.

---

## Beginner DSA Problem Solving with Dictionaries

- **Official Definition:** A **dictionary problem** is a coding question where data is stored as key-value pairs and solved using lookups, counting, or updates.
- **In Simple Words:** You use labels to store and find information quickly.
- **Real-Life Example:** A cricket scoreboard where player name is the key and runs scored is the value.

### Problem 1: Count Frequency of Characters

**Problem statement:** Count how many times each character appears in a string.

```python
text = "banana"  # Input string
frequency = {}  # Empty dictionary to store counts

for character in text:  # Visit each character
    if character in frequency:  # If character already exists in dictionary
        frequency[character] = frequency[character] + 1  # Increase its count
    else:
        frequency[character] = 1  # First time seen, set count to 1

print(frequency)  # Display character frequencies
```

**How the code works:**

- The dictionary stores each character as a key.
- The value stores how many times that character appeared.
- The `if` checks whether the key already exists before updating.

### Problem 2: Find the Most Frequent Mark

**Problem statement:** Given student marks in a list, find the mark that appears most often.

```python
marks = [78, 85, 78, 92, 85, 78]  # Input list of marks
frequency = {}  # Dictionary to count each mark

for mark in marks:  # Visit each mark
    if mark in frequency:  # If mark already counted before
        frequency[mark] = frequency[mark] + 1  # Increase count
    else:
        frequency[mark] = 1  # First occurrence

most_frequent_mark = marks[0]  # Start with any mark as current best answer
highest_count = 0  # Track highest frequency seen so far

for mark in frequency:  # Loop through dictionary keys
    if frequency[mark] > highest_count:  # Compare current count with best count
        highest_count = frequency[mark]  # Update best count
        most_frequent_mark = mark  # Update best mark

print("Most frequent mark is:", most_frequent_mark)  # Display final answer
```

**How the code works:**

- First loop builds the frequency dictionary.
- Second loop scans the dictionary to find the key with the highest count.
- This pattern appears often in counting problems.

### Problem 3: Check Two Sum Using a Dictionary

**Problem statement:** Check whether any two numbers in a list add up to a target value.

```python
numbers = [2, 7, 11, 15]  # Input list
target = 9  # Required sum
seen = {}  # Dictionary to store numbers already visited

found = False  # Flag to track whether answer exists

for index in range(len(numbers)):  # Loop using index
    current_value = numbers[index]  # Current number
    required = target - current_value  # Number needed to reach target

    if required in seen:  # If required number was seen before
        found = True  # Pair exists
        print("Pair found:", required, current_value)  # Show the pair
        break  # Stop because answer is found
    else:
        seen[current_value] = index  # Store current number for future lookup

if found == False:  # If loop ended without finding a pair
    print("No pair found")  # Inform that no valid pair exists
```

**How the code works:**

- For each number, the code calculates what partner number is needed.
- The dictionary stores numbers already seen.
- If the needed partner was seen earlier, a valid pair exists.

This is a classic beginner pattern that also appears on coding platforms.

---

## Practice Activity: Break the Problem Before Coding

I will solve one fresh problem using the logic-building method before writing code.

**Problem statement:** Given a list of names, print how many names start with the letter `A`.

**My logic plan:**

- Input: `["Amit", "Riya", "Arjun", "Neha", "Anita"]`
- Output: `3`
- Conditions: Ignore uppercase/lowercase differences if needed.
- Steps:
  1. Start a counter at `0`.
  2. Loop through each name.
  3. If the first character is `A`, increase the counter.
  4. Print the counter.

```python
names = ["Amit", "Riya", "Arjun", "Neha", "Anita"]  # Input list of names
count = 0  # Counter for names starting with A

for name in names:  # Visit each name
    if name[0] == "A":  # Check first character
        count = count + 1  # Increase count when condition matches

print("Names starting with A:", count)  # Display final answer
```

**How the code works:**

- `name[0]` reads the first character of each string.
- The counter increases only when the first letter is exactly `A`.
- This activity shows why planning first makes coding faster and cleaner.

---

## Practice Activity: Run One Program Fully on Local Machine

I will follow the complete local workflow once from start to finish.

1. Create a folder named `session09_practice`.
2. Open it in VS Code.
3. Create `even_numbers.py`.
4. Write a program that prints all even numbers from 1 to 20.
5. Save the file.
6. Open Terminal inside VS Code.
7. Run `python3 even_numbers.py`.
8. Confirm the output appears in the Terminal.

```python
# Print even numbers from 1 to 20
for number in range(1, 21):  # Loop from 1 to 20 inclusive
    if number % 2 == 0:  # Check whether number is even
        print(number)  # Print only even numbers
```

**How the code works:**

- `range(1, 21)` generates numbers from 1 to 20.
- `% 2 == 0` selects even numbers only.
- Running this file locally confirms that Python, VS Code, and Terminal are working correctly.

---

## Common Mistakes and Doubts

- **Wrong folder in Terminal:** If the file is not found, use `pwd` or `cd` to confirm you are inside the correct folder.
- **Not saving before running:** Always save the file first; otherwise old code may run.
- **Skipping logic planning:** Jumping directly to code often creates confusion and wrong outputs.
- **Off-by-one errors in loops:** Check whether your loop should include the last index or stop one step earlier.
- **Forgetting empty input cases:** Ask what should happen if a list or string is empty.
- **Mixing `print` and `return`:** In practice problems, know whether the platform expects printed output or a returned value.

When stuck, rewrite the problem in plain English, then convert each sentence into one line of code.

---

## Key Takeaways

- **Local development** with Python, VS Code, and Terminal helps you work like a real developer and manage many practice files easily.
- **Use `python3` consistently** in Terminal and VS Code — this is the standard command for Python 3 in software development.
- **Logic building** means breaking every problem into input, output, conditions, and steps before writing code.
- **Lists**, **strings**, and **dictionaries** are the main tools for beginner DSA problems in this lesson.
- **Loops and conditionals** let you scan data, count items, compare values, and build answers step by step.
- Solving small problems locally builds the confidence needed for coding practice platforms and more advanced algorithm topics later.

In the next lesson, you will continue strengthening problem-solving skills with more DSA patterns and slightly harder challenges.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| Local development | Running code on your own machine | Save and run `practice.py` |
| VS Code | Code editor for writing programs | Create and edit `.py` files |
| Terminal | Text interface to run commands | `python3 hello.py` |
| `python3 --version` | Check Python 3 installation | Shows installed version |
| `cd` | Change folder in Terminal | `cd python_practice` |
| `.py` file | Python source code file | `sum_numbers.py` |
| Input | Data given to a program | `[10, 20, 30]` |
| Output | Answer produced by a program | `30` |
| Logic building | Planning before coding | Input, output, steps |
| `for` loop | Repeat action for each item | `for x in numbers` |
| `if` condition | Run code only when rule is true | `if x > max_value` |
| `append()` | Add item to end of list | `squares.append(4)` |
| `split()` | Break string into parts | `"a b".split(" ")` |
| Dictionary | Key-value storage | `{"a": 2, "b": 1}` |
| Frequency count | Track how many times value appears | Character count in word |
| Two Sum pattern | Find pair with target sum using lookup | Use dictionary `seen` |

---

## Typical LeetCode Questions — Solve Yourself

The problems below are **typical beginner LeetCode-style questions** that match what you practiced in this lesson. They use **lists**, **strings**, **dictionaries**, **loops**, and **conditionals** only.

**Important:** Try to **solve these yourself** on [LeetCode](https://leetcode.com/) or on your local machine before looking at hints or solutions. Write the logic plan first, then code, then test with your own examples.

### List-Based Questions

| # | Problem Name | LeetCode ID | Why Practice This |
|---|---|---|---|
| 1 | Two Sum | 1 | Dictionary lookup with target difference |
| 2 | Contains Duplicate | 217 | Check repeated values in a list |
| 3 | Best Time to Buy and Sell Stock | 121 | Track minimum and maximum profit |
| 4 | Maximum Subarray | 53 | Update best sum while looping |
| 5 | Move Zeroes | 283 | Rearrange list using loops |
| 6 | Running Sum of 1d Array | 1480 | Build a new list from previous values |
| 7 | Find Pivot Index | 724 | Prefix sum style thinking |
| 8 | Squares of a Sorted Array | 977 | Transform list values in order |

### String-Based Questions

| # | Problem Name | LeetCode ID | Why Practice This |
|---|---|---|---|
| 1 | Valid Anagram | 242 | Compare character frequency |
| 2 | Valid Palindrome | 125 | Two-pointer / character checking |
| 3 | Reverse String | 344 | Swap or rebuild characters |
| 4 | First Unique Character in a String | 387 | Frequency count in string |
| 5 | Length of Last Word | 58 | Traverse string from end |
| 6 | Implement strStr() | 28 | Substring search with loops |
| 7 | Reverse Vowels of a String | 345 | Selective character swapping |
| 8 | Excel Sheet Column Number | 168 | Character-to-number mapping |

### Dictionary / Hash Map-Based Questions

| # | Problem Name | LeetCode ID | Why Practice This |
|---|---|---|---|
| 1 | Ransom Note | 383 | Character availability count |
| 2 | Valid Anagram | 242 | Hash map frequency pattern |
| 3 | Two Sum | 1 | Store seen values for fast lookup |
| 4 | Majority Element | 169 | Count occurrences and compare |
| 5 | First Unique Character in a String | 387 | Track first index using map |
| 6 | Intersection of Two Arrays II | 350 | Count common elements |
| 7 | Find Words That Can Be Formed by Characters | 1160 | Frequency comparison |
| 8 | Sort Array by Increasing Frequency | 1636 | Count first, then sort by count |

### Mixed Beginner Questions (Lists + Strings + Conditions)

| # | Problem Name | LeetCode ID | Why Practice This |
|---|---|---|---|
| 1 | Fizz Buzz | 412 | Conditions with loops |
| 2 | Number of Steps to Reduce a Number to Zero | 1342 | While loop logic |
| 3 | Remove Element | 27 | List filtering with condition |
| 4 | Merge Sorted Array | 88 | Two-list comparison |
| 5 | Longest Common Prefix | 14 | String comparison across list |
| 6 | Plus One | 66 | Carry handling in digits |
| 7 | Single Number | 136 | Unique value detection |
| 8 | Missing Number | 268 | Expected vs actual sum |

### How to Practice These Effectively

1. Read the problem twice and write the **input**, **output**, and **steps** before coding.
2. Solve it first in VS Code with your own test cases.
3. Submit on LeetCode only after your local tests pass.
4. If stuck for more than 20 minutes, review the topic pattern — counting, two pointers, prefix sum, or dictionary lookup — then try again without opening the full solution.
5. Maintain a notebook of solved problems with your logic plan and final code.

**Solve yourself. Do not copy answers.** The goal is to build thinking speed, not to increase solved-count numbers alone.
