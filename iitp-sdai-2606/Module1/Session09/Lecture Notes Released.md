# Hands-on Logic Building, Development Setup & DSA Problem Solving – I

## What You Will Learn in This Lesson

You have already learned how to use **lists**, **strings**, **dictionaries**, **loops**, **conditionals**, and **functions** to solve problems step by step. You have also seen how sorting algorithms like **Bubble Sort** and **Selection Sort** work by comparing and rearranging values inside a list.

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
- You can build confidence before solving problems on coding practice platforms.

An **IDE-based setup** (editor + Python + Terminal together) is better for long-term learning. Online compilers are fine for quick tests, but for the next several months of practice, working locally is the preferred approach.

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

On **macOS**, you can also install Python using **Homebrew** (`brew install python`) if you prefer command-line installation.

**Helpful tip:** If you are unsure about the exact steps for your laptop, search for installation steps for your operating system. The steps differ slightly for Windows, Mac, and Linux, but the goal is always the same — get Python 3 installed and verify it works.

### One Command for Software Development: Use `python3`

In professional software development, teams use **`python3`** as the standard command to run Python 3 programs.

- **`python3`** clearly means Python 3 — the version used in companies, cloud servers, and modern projects.
- **`python`** alone can mean different things on different laptops, so developers avoid mixing both commands.

**Use `python3` everywhere in this course** — in Terminal, VS Code, practice files, and local testing. Do not switch between `python` and `python3`. Pick one habit and stay consistent.

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
6. **Enable** the extension after installation — installing alone is not enough; the extension must be active.
7. Optionally install the **Python Extension Pack** for beginners — it bundles useful tools in one step.

### Create Your First Python File in VS Code

1. Create a practice folder on your laptop (for example, `python_practice`).
2. Click **File → Open Folder** and choose that folder. Always open the **folder**, not just a single file.
3. Click **New File** and save it as `hello_local.py`.
4. Type your Python code inside the editor.
5. Save the file using **Ctrl + S** (Windows/Linux) or **Cmd + S** (macOS).

```python
# My first locally saved Python program
message = "Hello from my laptop"  # Store a text message in a variable
print(message)  # Display the message on the screen
```

**How the code works:**

- The file name ends with `.py`, which tells the system this is a Python program.
- VS Code highlights keywords like `print` in color, which makes reading easier.
- Saving the file stores your work permanently on your laptop.

### Run Code Using the Play Button

After the Python extension is installed and enabled:

1. Open your project **folder** in VS Code.
2. Select the correct **Python interpreter** if VS Code asks you to choose one.
3. Look for the **play button** (▶) at the top-right of the editor.
4. Click it to run the file and see output in the integrated Terminal below.

**If the play button does not appear:**

- Confirm the Python extension is **installed and enabled**.
- Make sure you opened a **folder**, not just a loose file.
- Restart VS Code after installing a new extension.
- Select the Python interpreter from the command palette.

**Common mistake:** Saving a file without the `.py` extension. Always use names like `practice.py`, not `practice.txt`.

---

## Understanding the Terminal

- **Official Definition:** A **Terminal** (also called **Command Line** or **Shell**) is a text-based interface where you type commands to control your computer.
- **In Simple Words:** The Terminal is a place where you type instructions instead of clicking buttons.
- **Real-Life Example:** Using the Terminal is like telling a shopkeeper exactly what you want by speaking clearly, instead of pointing at many shelves.

Developers use the Terminal to:

- Check whether Python is installed.
- Create folders and move between them.
- Run Python files directly.
- Open the Python interactive shell for quick experiments.

### Useful Terminal Commands

| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print current folder path | Shows where you are |
| `ls` | List files in current folder | macOS/Linux |
| `dir` | List files in current folder | Windows |
| `mkdir folder_name` | Create a new folder | `mkdir python_practice` |
| `cd folder_name` | Change directory | `cd python_practice` |
| `cd ..` | Go one folder back | Move to parent folder |
| `python3 file.py` | Run a Python file | `python3 hello_local.py` |
| `python3` | Open Python interactive shell | Type commands line by line |

### Python Interactive Shell

If you type `python3` in the Terminal without a file name, Python opens an **interactive shell** (also called REPL).

- You can type Python commands one line at a time and see instant results.
- This is useful for quick checks, like testing `print("hello")` or a small calculation.
- Type `exit()` or press **Ctrl + D** (macOS/Linux) to leave the shell.

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
3. Create a file named `hello_local.py`.
4. Write complete Python code and save it.
5. Run the file using the **play button** in VS Code, **or** open the integrated Terminal and type `python3 hello_local.py`.
6. Read the output shown in the Terminal.

```python
# My first program running fully on local machine
print("Hello, Python project setup is completed.")  # Simple message to confirm setup works
```

**How the code works:**

- `print()` displays text in the Terminal.
- Running this file locally confirms that Python, VS Code, and Terminal are all connected correctly.
- If you see the message on screen, your local setup is working.

**Common mistakes:**

- Running the command from the wrong folder — use `cd` to enter the folder where the file is saved.
- Forgetting to save the file before running it — unsaved changes will not appear in output.
- Spelling the file name incorrectly in the Terminal — file names are case-sensitive on macOS/Linux.

---

## What Is DSA?

Before solving problems, let us clarify one term you will hear often in coding practice.

- **Official Definition:** **DSA** stands for **Data Structures and Algorithms** — the study of how data is stored and how step-by-step procedures solve problems efficiently.
- **In Simple Words:** DSA means choosing the right container for your data (list, string, dictionary) and writing the right steps (loops, conditions) to get the answer.
- **Real-Life Example:** Sorting exam marks is an algorithm. Storing marks in a list or a dictionary is a data structure choice.

In this lesson, you already know the building blocks:

| Data Structure | What It Stores | Simple Use |
|---|---|---|
| **List** | Multiple values in order | `[9, 2, 10, 1, 7]` |
| **String** | Text characters | `"banana"` |
| **Dictionary** | Key-value pairs | `{"a": 3, "b": 1}` |

You will combine these with **loops** and **conditionals** to solve beginner problems.

---

## Logic Building — How to Think Before Coding

- **Official Definition:** **Logic building** is the process of converting a problem statement into clear inputs, outputs, conditions, and step-by-step instructions before writing code.
- **In Simple Words:** Logic building means planning the solution on paper first, then coding.
- **Real-Life Example:** Before cooking biryani, you check ingredients, decide serving size, and follow steps in order. Coding works the same way.

Every beginner DSA problem can be broken into four parts:

| Part | Question to Ask | Example |
|---|---|---|
| **Input** | What data am I receiving? | A list of numbers |
| **Output** | What answer must I return or print? | Largest number |
| **Conditions** | What rules decide the answer? | If a number is bigger, update the largest |
| **Steps** | What actions happen in order? | Loop, compare, update, print |

### Sample Logic Template

For the problem "Find the largest number in a list without using `max()`":

- **Input:** `[9, 2, 10, 1, 7, 20, 19, 99]`
- **Output:** `99`
- **Conditions:** If current number is greater than the largest so far, update the largest.
- **Steps:**
  1. Assume the first value is the largest.
  2. Visit every remaining value using a loop.
  3. If a value is bigger, update the largest.
  4. Print the final largest value.

In class, you were given time to **think first, then code**. This habit builds confidence and reduces mistakes.

![Logic building framework — break every problem into Input, Output, Conditions, and Steps before writing code, like following a recipe before cooking](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-03-logic-building-framework.png?v=20260704)

---

## Beginner DSA Problem Solving

- **Official Definition:** A **beginner DSA problem** is a coding question solved using basic data structures, loops, and conditionals without advanced algorithms.
- **In Simple Words:** You receive some data, follow clear steps, and produce an answer.
- **Real-Life Example:** Finding the highest score in a class test sheet, or counting how many times each letter appears in a name.

In this lesson, we solved four problems that combine **lists**, **strings**, and **dictionaries**.

![Beginner DSA with lists, strings, and dictionaries — use loops and conditionals to solve maximum, vowel count, frequency, and Two Sum style problems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session09/session09-04-dsa-structures-problems.png?v=20260704)

### Problem 1: Find the Largest Number in a List (Without `max()`)

**Problem statement:** Given a list of numbers, find and print the largest number. Do not use the built-in `max()` function.

**Logic plan:**

- Input: `[9, 2, 10, 1, 7, 20, 19, 99]`
- Output: `99`
- Steps: Start with first value as largest, compare with others, update when needed.

```python
numbers = [9, 2, 10, 1, 7, 20, 19, 99]  # Input list of numbers
largest = numbers[0]  # Assume first number is the largest for now

for num in numbers:  # Visit each number one by one
    if num > largest:  # If current number is bigger than our guess
        largest = num  # Update largest because our assumption was wrong

print("Maximum value is:", largest)  # Display the final answer
```

**How the code works:**

- `largest = numbers[0]` sets a starting guess.
- The loop checks every value in the list.
- The `if` block updates the answer only when a bigger value appears.
- After the loop ends, `largest` holds the correct result.

---

### Problem 2: Count Character Frequency in a String

**Problem statement:** Given a string, count how many times each character appears.

**Example:**

- Input: `"banana"`
- Output: `{'b': 1, 'a': 3, 'n': 2}`

**Logic plan:**

- Input: a string like `"banana"`
- Output: a dictionary with each character as key and its count as value
- Data structure choice: **dictionary** — because you need to map each character to its count
- Steps: Loop over each character, update its count in the dictionary

```python
text = "banana"  # Input string
frequency = {}  # Empty dictionary to store character counts

for character in text:  # Visit each character one by one
    frequency[character] = frequency.get(character, 0) + 1  # Get current count (0 if new) and add 1

print(frequency)  # Display {'b': 1, 'a': 3, 'n': 2}
```

**How the code works:**

- `frequency.get(character, 0)` checks if the character already exists in the dictionary.
- If the character is new, it returns `0` as the default value.
- Adding `1` increases the count for that character.
- This is cleaner than writing a long `if-else` block for every update.

**Common doubt:** A string is the **input**, but a dictionary is the best **tool** to build the frequency map output.

---

### Problem 3: Find Duplicate Elements in a List

**Problem statement:** Given a list, print all numbers that appear more than once.

**Example:**

- Input: `[1, 2, 3, 2, 4, 1]`
- Output: `[1, 2]`

**Logic plan:**

- Build a frequency dictionary (same pattern as Problem 2).
- Loop through the dictionary using `.items()`.
- If count is greater than 1, the number is a duplicate — add it to the output list.

```python
nums = [1, 2, 3, 2, 4, 1]  # Input list
counts = {}  # Dictionary to count how many times each number appears
output = []  # List to store duplicate numbers

for n in nums:  # Visit each number in the list
    counts[n] = counts.get(n, 0) + 1  # Build frequency map using same logic as character count

for key, value in counts.items():  # Loop through dictionary key-value pairs
    if value > 1:  # If a number appears more than once, it is duplicated
        output.append(key)  # Add duplicated number to output list

print(output)  # Display [1, 2]
```

**How the code works:**

- First loop builds `counts` — for example `{1: 2, 2: 2, 3: 1, 4: 1}`.
- `counts.items()` gives both the number (`key`) and how many times it appeared (`value`).
- `output.append(key)` adds duplicated numbers to a result list.
- This problem reuses the frequency-counting pattern from Problem 2.

---

### Problem 4: Merge Two Sorted Lists

**Problem statement:** Given two sorted lists, merge them into one sorted list.

**Example:**

- Input: `a = [1, 3, 5]` and `b = [2, 4, 6]`
- Output: `[1, 2, 3, 4, 5, 6]`

**Logic plan:**

- Use two pointers — one for each list.
- Compare the current values at both pointers.
- Pick the smaller value, add it to the result, and move that pointer forward.
- Repeat until one list is fully processed.

**Shortcut vs proper approach:**

- `sorted(a + b)` works but is slower for large lists.
- The **two-pointer** approach compares values step by step and is more efficient.

```python
a = [1, 3, 5]  # First sorted list
b = [2, 4, 6]  # Second sorted list
merged = []  # Result list to build
i = 0  # Pointer for list a
j = 0  # Pointer for list b

while i < len(a) and j < len(b):  # While both lists still have elements
    if a[i] < b[j]:  # Pick the smaller value from a
        merged.append(a[i])  # Add it to merged list
        i = i + 1  # Move pointer i forward
    else:  # b[j] is smaller or equal
        merged.append(b[j])  # Add it to merged list
        j = j + 1  # Move pointer j forward

print(merged)  # Display [1, 2, 3, 4, 5, 6]
```

**How the code works:**

- `i` and `j` track the current position in each list.
- The `while` loop runs only while **both** lists still have elements to compare.
- Each iteration adds the smaller value to `merged` and moves one pointer forward.

**Practice challenge:** What happens when one list is longer than the other? After the `while` loop ends, leftover elements from the longer list still need to be added. Try debugging this edge case on your own — it is a great logic-building exercise.

---

## Dry Run — Trace Your Code Step by Step

- **Official Definition:** A **dry run** is the manual step-by-step execution of code using sample input, without relying only on the computer output.
- **In Simple Words:** Dry run means walking through your code line by line in your head or on paper.
- **Real-Life Example:** Before submitting an exam answer sheet, you re-read each step to check for mistakes. A dry run does the same for code.

How to dry run effectively:

1. Write down the input values.
2. Track how each variable changes after every line.
3. For dictionary problems, draw the dictionary state after each loop step.
4. If tracing in your head is hard, add a `print()` statement after important lines and run the code.

This technique was used heavily in class — especially for the character frequency problem where the dictionary grows step by step (`{'b': 1}` → `{'b': 1, 'a': 1}` → `{'b': 1, 'a': 2, 'n': 1}` and so on).

---

## Common Mistakes and Doubts

- **Wrong folder in Terminal:** If the file is not found, use `pwd` or `cd` to confirm you are inside the correct folder.
- **Not saving before running:** Always save the file first; otherwise old code may run.
- **Skipping logic planning:** Jumping directly to code often creates confusion and wrong outputs.
- **Opening a file instead of a folder in VS Code:** The play button may not appear if you open only a single file — open the project folder instead.
- **Extension installed but not enabled:** After installing the Python extension, make sure it is enabled and restart VS Code if needed.
- **Forgetting leftover elements in merge:** The two-pointer merge must handle remaining items after one list is exhausted.
- **Mixing `print` and `return`:** In practice problems, know whether the platform expects printed output or a returned value.

When stuck, rewrite the problem in plain English, then convert each sentence into one line of code.

---

## Key Takeaways

- **Local development** with Python, VS Code, and Terminal helps you work like a real developer and manage many practice files easily.
- **Use `python3` consistently** in Terminal and VS Code — this is the standard command for Python 3 in software development.
- **Logic building** means breaking every problem into input, output, conditions, and steps before writing code.
- **Lists**, **strings**, and **dictionaries** are the main tools for the beginner DSA problems in this lesson.
- **Loops and conditionals** let you scan data, count items, compare values, and build answers step by step.
- **Dry runs** and **print debugging** help you understand what your code is doing at each step.

In the next lesson, you will continue strengthening problem-solving skills with more DSA patterns and slightly harder challenges.

---

## Important Commands, Libraries, Terminologies Used

| Term / Syntax | Meaning | Simple Example |
|---|---|---|
| Local development | Running code on your own machine | Save and run `practice.py` |
| VS Code | Code editor for writing programs | Create and edit `.py` files |
| Terminal | Text interface to run commands | `python3 hello.py` |
| `python3 --version` | Check Python 3 installation | Shows installed version |
| `mkdir` | Create a new folder | `mkdir python_practice` |
| `cd` | Change folder in Terminal | `cd python_practice` |
| `.py` file | Python source code file | `hello_local.py` |
| DSA | Data Structures and Algorithms | List + loop to find maximum |
| Input | Data given to a program | `[9, 2, 10, 1, 7]` |
| Output | Answer produced by a program | `99` |
| Logic building | Planning before coding | Input, output, conditions, steps |
| Dry run | Manual step-by-step code trace | Track dictionary after each loop |
| `for` loop | Repeat action for each item | `for x in numbers` |
| `if` condition | Run code only when rule is true | `if x > largest` |
| `append()` | Add item to end of list | `output.append(key)` |
| `.get(key, default)` | Safe dictionary lookup with fallback | `counts.get(n, 0)` |
| `.items()` | Loop through dictionary key-value pairs | `for key, value in counts.items()` |
| Dictionary | Key-value storage | `{"a": 3, "b": 1}` |
| Two-pointer technique | Two indexes moving through data | Merge two sorted lists |
| Frequency count | Track how many times value appears | Character count in `"banana"` |
