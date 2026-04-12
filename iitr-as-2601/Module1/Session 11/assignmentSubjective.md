## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-data-assignment`).

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

### **Question: NumPy-Based Dataset Preparation Pipeline**

**Task:**
Build a Python program using NumPy that simulates a realistic AI-style data preparation pipeline.

Your program must:

1. Set a random seed for reproducibility.
2. Generate a **2D NumPy array** representing a dataset with:

   * Rows as samples
   * Columns as features
3. Compute the **mean and standard deviation per feature** using axis-aware operations.
4. Normalize the dataset using broadcasting:

   ```
   normalized = (data - mean) / std
   ```
5. Slice the normalized array to:

   * Extract the first 80% of samples as a training set
   * Extract the remaining samples as a test set
6. Modify a sliced value intentionally and **observe its effect** on the original array (to demonstrate view behavior).
7. Print:

   * Original data shape
   * Mean and standard deviation shapes
   * Training and test set shapes
   * A brief message explaining what changed due to slicing

**Requirements:**

* Use NumPy vectorized operations only (no Python loops for math)
* Use `.shape`, slicing, broadcasting, and random generation
* Use clear variable names and clean structure
* Demonstrate understanding of views vs copies

**Sample Output (example):**

```
Original data shape: (100, 3)
Mean shape: (3,)
Training data shape: (80, 3)
Test data shape: (20, 3)
Note: Modifying the slice affected the original array
```