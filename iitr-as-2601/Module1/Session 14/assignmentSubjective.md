

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

### **Question: AI Data Query and Ranking System**

**Task:**
Build a Python program using Pandas that simulates querying and analyzing an AI dataset.

Your program must:

1. Create or load a sample dataset containing at least:

   * Name
   * Score
   * Passed (Boolean)
   * Category (e.g., "A", "B")
2. Perform the following operations:

   * Select a single column and print it
   * Select multiple columns and store them in a new DataFrame
   * Use `iloc` to retrieve the first three rows
   * Use `loc` after setting a meaningful index
   * Filter rows where Score > 85
   * Filter rows where Score > 85 and Passed is True
   * Sort the filtered result in descending order of Score
3. Chain at least one filtering and sorting operation together.
4. Print labeled outputs for clarity.

**Requirements:**

* Use Boolean filtering correctly (`&`, `|`, `~`)
* Use parentheses for multiple conditions
* Demonstrate both `iloc` and `loc`
* Avoid modifying the original DataFrame unintentionally
* Write clean, readable code

**Sample Output (example):**

```id="queryexample"
High-performing students:
Name    Score
Alice   95
Bob     92
```
