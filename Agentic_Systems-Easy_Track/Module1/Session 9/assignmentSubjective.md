## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-files-assignment`).

3. Write **separate Python files** for each question inside this folder.

4. For each program:

   * Run the code in the **terminal**
   * Verify the **output**

5. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

6. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repo).

---

### **Question: File-Based Data Processing and Logging System**

**Task:**
Build a Python program that reads numeric data from a text file, processes it, and writes detailed logs of what happened during execution.

Your program must do the following:

1. Read a file named `numbers.txt`, where each line contains a single integer.
2. Convert each line into an integer and store all values in a list.
3. Compute:

   * Total number of values
   * Sum of values
   * Average value
4. Write the results to a file named `results.log` using **append mode**.
5. Log each major step, such as:

   * File opened
   * Data loaded
   * Computation completed
6. Use the `with` statement for **all file operations**.

**Requirements:**

* Do not hardcode numeric values
* Use clear variable names
* Separate data reading, computation, and logging logically
* Handle whitespace correctly using `strip()`

**Sample Log Output (example):**

```
File opened successfully
Read 5 numbers
Sum: 150
Average: 30.0
Processing completed
```
