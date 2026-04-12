## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-logic-assignment`).

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

### **Question: AI Dataset Inspection Pipeline**

**Task:**
Build a Python program using Pandas that simulates the first stage of an AI data workflow.

Your program must:

1. Create or load a CSV file (you may generate a small sample dataset).
2. Load the dataset using `pd.read_csv()`.
3. Display:

   * First 5 rows (`head()`)
   * Last 5 rows (`tail()`)
   * Structural information (`info()`)
   * Summary statistics (`describe()`)
4. Select a single column and store it in a variable.
5. Select multiple columns and store them in a new DataFrame.
6. Filter rows based on a numerical condition.
7. Print clear labels explaining each step.

**Requirements:**

* Use Pandas properly (no manual loops for filtering)
* Demonstrate column selection (single and multiple)
* Demonstrate row filtering
* Use meaningful column names (e.g., Age, Score, Label)
* Structure your script cleanly

**Sample Output (example):**

```
First 5 rows:
...

Dataset Info:
...

Filtered rows (Score > 80):
...
```
