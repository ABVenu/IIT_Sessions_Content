# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**Rahul** used an online compiler for quick Python practice during his first week. Now he wants to save many programs as separate files, organize them in folders, and run them from his laptop like developers do in companies.

What is the **best term** for this way of working?

A. Cloud-only compilation  
B. Local development  
C. Browser debugging only  
D. Database migration  

**Correct Answer:** B

**Answer Explanation:**  
**Local development** means writing, saving, and running code directly on your own computer using tools like Python, VS Code, and the Terminal.

**Why other options are wrong:**  
- A: Cloud-only compilation keeps work inside a browser tool, not on the laptop as files and folders.  
- C: Browser debugging alone does not describe saving and managing many programs locally.  
- D: Database migration is unrelated to setting up a coding workspace on a laptop.

---

## Q2 (MCQ, Easy)

**Anita** opens Terminal on her laptop and wants to confirm that **Python 3** is installed before her first local coding session.

Which command should she run?

A. `python --help`  
B. `python3 --version`  
C. `install python3`  
D. `code --version`  

**Correct Answer:** B

**Answer Explanation:**  
`python3 --version` checks which Python 3 version is available on the system. If installation is successful, it prints something like `Python 3.12.1`.

**Why other options are wrong:**  
- A: `python` alone may not always refer to Python 3 on every machine.  
- C: `install python3` is not the standard verification command after installation.  
- D: `code --version` checks VS Code, not Python.

---

## Q3 (MCQ, Easy)

**Vikram** creates a new program file in VS Code and saves it as `practice.txt` instead of `practice.py`.

Why is this a **mistake** for a Python program?

A. VS Code cannot open `.txt` files  
B. The `.py` extension tells the system the file contains Python code  
C. Terminal commands only work on Sundays  
D. Python files must always be named `hello.py`  

**Correct Answer:** B

**Answer Explanation:**  
A file ending with `.py` is recognized as a Python source file. Without the correct extension, your workflow and tooling may not treat the file as Python code.

**Why other options are wrong:**  
- A: VS Code can open `.txt` files, but that does not make them Python programs.  
- C: Terminal works any day; this is not a real technical rule.  
- D: Python files can have many valid names — only the `.py` extension matters.

---

## Q4 (MCQ, Easy)

**Meera** has already saved her file as `hello_local.py` inside a folder called `dsa_practice`. She opens Terminal inside VS Code and wants to run the program.

Which command should she use?

A. `run hello_local`  
B. `python3 hello_local.py`  
C. `print hello_local.py`  
D. `open hello_local.py`  

**Correct Answer:** B

**Answer Explanation:**  
`python3 hello_local.py` tells the Python 3 interpreter to execute the saved file. This is the standard way to run a local Python program from Terminal.

**Why other options are wrong:**  
- A: `run hello_local` is not a standard Python execution command.  
- C: `print` is a Python keyword used inside code, not a Terminal command to run a file.  
- D: `open` may launch a file with another app, but it does not execute Python code as a program.

---

## Q5 (MCQ, Moderate)

**Karan** is solving a beginner coding problem. Before writing code, he breaks the task into four planning parts on paper.

Which option correctly lists the **four parts of logic building** taught for beginner DSA problems?

A. Input, Output, Compiler, Debugger  
B. Input, Output, Conditions, Steps  
C. Loop, Function, Class, Module  
D. Print, Return, Import, Export  

**Correct Answer:** B

**Answer Explanation:**  
Logic building breaks a problem into **Input** (what data you receive), **Output** (what answer you must produce), **Conditions** (rules that decide the answer), and **Steps** (actions in order).

**Why other options are wrong:**  
- A: Compiler and Debugger are tools, not the four planning parts of a problem.  
- C: Loop, Function, Class, and Module are coding concepts, not the planning framework.  
- D: Print, Return, Import, and Export are not the four-part logic template.

---

## Q6 (MCQ, Moderate)

**Priya** is counting how many times each character appears in the string `"banana"` using a dictionary. She writes this line inside her loop:

```python
frequency[character] = frequency.get(character, 0) + 1
```

What does `frequency.get(character, 0)` do when `character` is **not yet** in the dictionary?

A. It crashes the program immediately  
B. It returns `0` as the default value  
C. It returns `1` automatically  
D. It deletes the dictionary  

**Correct Answer:** B

**Answer Explanation:**  
`.get(key, default)` safely looks up a key. If the key is missing, it returns the default value — here `0` — so you can add `1` and store the first occurrence cleanly.

**Why other options are wrong:**  
- A: `.get()` is designed to avoid crashes on missing keys.  
- C: The default is `0`, not `1`; you add `1` separately in the same line.  
- D: `.get()` reads from the dictionary; it does not delete it.

---

## Q7 (MSQ, Moderate)

**Arjun** installed VS Code and Python, but the **play button** to run his `.py` file is not visible.

Which actions can **correctly** help fix this issue?

A. Install and enable the Python extension published by Microsoft  
B. Open the project folder in VS Code instead of opening only a single loose file  
C. Save the file with a `.txt` extension to make Python detect it faster  
D. Restart VS Code after installing a new extension  

**Correct Answers:** A, B, D

**Answer Explanation:**  
The play button usually appears when the Python extension is active, the project folder is opened properly, and VS Code has been restarted after setup changes if needed.

**Why other options are wrong:**  
- C: Python files should use the `.py` extension, not `.txt`.

---

## Q8 (MSQ, Moderate)

**Sneha** is preparing a quick reference sheet about **DSA** and local coding tools.

Which statements are **correct**?

A. DSA stands for Data Structures and Algorithms  
B. A dictionary stores data as key-value pairs  
C. `mkdir folder_name` creates a new folder in Terminal  
D. A dry run means executing code only on a cloud server without reading the logic  

**Correct Answers:** A, B, C

**Answer Explanation:**  
DSA is Data Structures and Algorithms; dictionaries map keys to values; and `mkdir` creates folders in Terminal.

**Why other options are wrong:**  
- D: A **dry run** is a manual step-by-step trace of code logic on paper or in your head — not cloud-only execution.

---

## Q9 (MSQ, Hard)

**Ravi** builds a frequency dictionary for this list:

```python
nums = [1, 2, 3, 2, 4, 1]
```

He uses:

```python
counts[n] = counts.get(n, 0) + 1
```

Then he loops with `for key, value in counts.items():` to find duplicates.

Which statements are **correct**?

A. After building `counts`, the value for key `1` is `2`  
B. After building `counts`, the value for key `3` is `1`  
C. A number is a duplicate if its count is greater than `1`  
D. `.items()` gives only the keys and hides the count values  

**Correct Answers:** A, B, C

**Answer Explanation:**  
`1` appears twice and `3` appears once, so `counts[1] == 2` and `counts[3] == 1`. Duplicates are numbers with count greater than `1`. The `.items()` method returns both keys and values.

**Why other options are wrong:**  
- D: `.items()` returns key-value pairs, not keys alone.

---

## Q10 (MSQ, Hard)

**Neha** merges two sorted lists using the **two-pointer** approach:

```python
a = [1, 3, 5]
b = [2, 4, 6]
```

Which statements about this approach are **correct**?

A. Two pointers `i` and `j` usually start at index `0` in their respective lists  
B. At each step, compare `a[i]` and `b[j]` and append the smaller value to the merged list  
C. `sorted(a + b)` is the only correct way to merge two sorted lists  
D. After the main `while` loop, leftover elements from the longer list may still need to be added  

**Correct Answers:** A, B, D

**Answer Explanation:**  
The two-pointer method starts both indexes at `0`, compares current values, moves the pointer of the list from which the smaller value was taken, and may still need to append remaining elements after one list is exhausted.

**Why other options are wrong:**  
- C: `sorted(a + b)` can work as a shortcut, but it is not the only correct method — the two-pointer approach is the step-by-step merge technique taught for better control and efficiency understanding.
