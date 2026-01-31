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

### **Question: User Data Processing System**

**Task:**
Build a modular Python program that manages and analyzes user data using **multiple data collections**.

Your program must do the following:

1. Store multiple users in a **list**, where each user is represented as a **dictionary** containing:

   * `"name"` (string)
   * `"scores"` (list of integers)
   * `"roles"` (set of strings)

2. Write a function that:

   * Accepts the list of users
   * Iterates through each user
   * Calculates the **average score** for each user
   * Returns the average

3. Write another function that:

   * Accepts a user’s roles (set)
   * Returns `True` if the user has `"admin"` access, otherwise `False`

4. In a `main()` function:

   * Print each user’s name
   * Print their average score
   * Print whether they have admin access

**Requirements:**

* Use lists, dictionaries, sets, and tuples where appropriate
* Do not hardcode values inside functions
* Use iteration and membership checks
* Use clear variable names and clean structure
* Call `main()` to run the program

**Sample Output (example):**

```
Name: Alice
Average Score: 82.5
Admin Access: True
```
