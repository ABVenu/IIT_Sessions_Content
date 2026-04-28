# Objective Assignment — Advanced OOP in Python: Encapsulation, Custom Exceptions & Introduction to Git

---

## Question 1 — MCQ | Easy

Ravi is building a `Vector` class and wants the `+` operator to add the coordinates of two `Vector` objects together. Which magic method should he define inside the class to make `v1 + v2` work?

**A)** `__sum__(self, other)`
**B)** `__plus__(self, other)`
**C)** `__add__(self, other)`
**D)** `__combine__(self, other)`

**Correct Answer:** C

**Answer Explanation:**
- **C is correct.** Python maps the `+` operator to the `__add__` magic method. When you write `v1 + v2`, Python internally calls `v1.__add__(v2)`. Defining this method inside your class lets you control what `+` means for your objects.
- **A is incorrect.** `__sum__` is not a recognized magic method in Python; it does not map to any operator.
- **B is incorrect.** `__plus__` is not a valid dunder method in Python.
- **D is incorrect.** `__combine__` is not a standard magic method recognized by Python's operator system.

---

## Question 2 — MCQ | Easy

Ananya is writing an `Employee` class and wants to ensure that the `salary` attribute **cannot be accessed directly** from outside the class. Which of the following correctly declares `salary` as a **private** variable?

**A)** `self.salary = 50000`
**B)** `self._salary = 50000`
**C)** `self.__salary = 50000`
**D)** `self.#salary = 50000`

**Correct Answer:** C

**Answer Explanation:**
- **C is correct.** In Python, a variable prefixed with **two underscores** (`__`) is private. Python applies name mangling, renaming it internally to `_ClassName__salary`, making it inaccessible directly via `obj.__salary` from outside the class.
- **A is incorrect.** No underscores means the variable is **public** — accessible from anywhere.
- **B is incorrect.** A single underscore (`_`) is the convention for **protected** — accessible within the class and its subclasses. It is only a naming convention; Python does not enforce it.
- **D is incorrect.** `#` is not valid Python syntax for access control.

---

## Question 3 — MCQ | Easy

Rahul has an `Employee` class with a private `__salary` attribute. He wants to allow other parts of the program to safely **read** the salary without exposing the variable directly. What is the recommended approach?

**A)** Remove the double underscores to make `salary` a public variable
**B)** Define a getter method `get_salary()` that returns `self.__salary`
**C)** Use Python's built-in `read()` function on the attribute
**D)** Access it directly using `emp.__salary`

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** A **getter** method is a regular method defined inside the class whose sole purpose is to return the value of a private variable. It provides controlled, read-only access from outside the class.
- **A is incorrect.** Making the variable public defeats the entire purpose of encapsulation — it removes all access protection.
- **C is incorrect.** Python has no built-in `read()` function for object attributes.
- **D is incorrect.** Accessing `emp.__salary` from outside the class raises an `AttributeError` because Python's name mangling makes the attribute inaccessible by that name outside the class.

---

## Question 4 — MCQ | Easy

Sanya has modified some Python files in her local project and staged them using `git add`. She now wants to **save a snapshot** of those changes to her local repository with the message `"Fix login bug"`. Which command should she run?

**A)** `git push -m "Fix login bug"`
**B)** `git save "Fix login bug"`
**C)** `git commit -m "Fix login bug"`
**D)** `git add -m "Fix login bug"`

**Correct Answer:** C

**Answer Explanation:**
- **C is correct.** `git commit -m "message"` saves all staged changes as a permanent snapshot in the **local** repository. The `-m` flag is followed by the commit message.
- **A is incorrect.** `git push` sends commits to the **remote** repository — it does not accept `-m` and does not create a commit.
- **B is incorrect.** `git save` is not a valid Git command.
- **D is incorrect.** `git add` is used to **stage** files, not to create a commit. It does not accept a `-m` flag.

---

## Question 5 — MCQ | Moderate

Karan is studying the following code:

```python
class BankAccount:
    def __init__(self):
        self.balance = 5000

    def __deduct(self, amount):
        self.balance -= amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.__deduct(amount)
            print(f"Remaining balance: {self.balance}")
        else:
            print("Insufficient funds")

acc = BankAccount()
acc.__deduct(200)
```

What will happen when `acc.__deduct(200)` is called on the last line?

**A)** The balance will be reduced to `4800`
**B)** An `AttributeError` is raised because `__deduct` is private and cannot be called from outside the class
**C)** A `TypeError` is raised because `__deduct` requires two arguments but only one was provided
**D)** The code works fine because Python does not actually enforce private access restrictions

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** `__deduct` is a private method (double underscore prefix). Python applies **name mangling**, internally renaming it to `_BankAccount__deduct`. Calling `acc.__deduct(200)` from outside the class looks for a method named `__deduct` which doesn't exist under that name externally, raising `AttributeError: 'BankAccount' object has no attribute '__deduct'`.
- **A is incorrect.** The private method cannot be reached from outside — Python never executes the deduction logic.
- **C is incorrect.** While `self` counts as one argument, the issue here is access restriction, not argument count. The error is an `AttributeError`, not a `TypeError`.
- **D is incorrect.** Python **does** enforce private access through name mangling, which effectively blocks direct external access.

---

## Question 6 — MCQ | Moderate

Divya wants to create a custom exception `InsufficientFundsError` that stores a descriptive message and the current `balance`. Which of the following correctly defines this custom exception?

**A)**
```python
class InsufficientFundsError:
    def __init__(self, message, balance):
        self.message = message
        self.balance = balance
```

**B)**
```python
class InsufficientFundsError(Exception):
    def __init__(self, message, balance):
        super().__init__(message)
        self.balance = balance
```

**C)**
```python
class InsufficientFundsError(Exception):
    def __init__(self, message, balance):
        self.message = message
        self.balance = balance
```

**D)**
```python
class InsufficientFundsError(ValueError):
    pass
```

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** It inherits from `Exception` (making it a valid Python exception), calls `super().__init__(message)` to register the message with the base `Exception` class (so `str(e)` shows the message), and also stores `balance` as a custom instance variable.
- **A is incorrect.** It does not inherit from `Exception`, so it cannot be raised with `raise` or caught with a standard `except` block.
- **C is incorrect.** Although it inherits from `Exception`, it does **not** call `super().__init__(message)`. The message is stored on `self.message` but not passed to the base class, so `str(e)` will not display it correctly — this violates the expected exception behavior.
- **D is incorrect.** It inherits from `ValueError` with no custom attributes, which doesn't satisfy the requirement of storing a `balance` value.

---

## Question 7 — MSQ | Moderate

Priya is reviewing the concept of Polymorphism in Python. Which of the following statements are **correct**? *(Select all that apply.)*

**A)** Duck Typing requires both classes to inherit from a common base class for Polymorphism to work
**B)** Method Overriding is one form of Polymorphism — the child class redefines a method inherited from the parent
**C)** `5 + 3` evaluating to `8` while `"hello" + " world"` evaluating to `"hello world"` is an example of Operator Overloading, which is a form of Polymorphism
**D)** Polymorphism allows the same function or operator to behave differently depending on the type or class of the object

**Correct Answers:** B, C, D

**Answer Explanation:**
- **A is incorrect.** Duck Typing explicitly does **not** require a common base class. It only requires that the object has the needed method — if it "quacks like a duck", it is treated as a duck. `Pen` and `Eraser` can both have a `perform_task()` method without being related by inheritance.
- **B is correct.** When a child class redefines a parent's method, calling that method on a child object executes the child's version. The same method name produces different behavior depending on the class — this is Polymorphism.
- **C is correct.** The `+` operator behaves differently for `int` and `str`. Python internally calls `int.__add__()` for integers and `str.__add__()` for strings — the operator's behavior is overloaded based on data type. This is Operator Overloading, a key mechanism of Polymorphism.
- **D is correct.** This is the exact definition of Polymorphism: *same interface, different behavior based on context (type or class)*.

---

## Question 8 — MSQ | Moderate

Meena has just joined a software team and is learning about Version Control Systems. Which of the following statements about VCS concepts are **correct**? *(Select all that apply.)*

**A)** The **trunk/main/master** branch represents the primary, stable, production-ready codebase
**B)** A **branch** allows a developer to work on a new feature in isolation without affecting the main codebase
**C)** A **tag** is used to permanently delete a specific commit from the repository's history
**D)** **Merging** is the process of combining a feature branch back into the main branch once the feature is complete and verified

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct.** The trunk (also called `main` or `master`) is the primary line of development — the stable, production-ready version of the codebase that all developers share.
- **B is correct.** Branches create an isolated copy of the codebase where changes don't affect anyone else. Once the feature is ready and reviewed, it is merged back.
- **C is incorrect.** A **tag** is a human-friendly named pointer to a specific commit, used to mark release points (e.g., `v1.0-stable`). It does **not** delete anything. Tags are read-only labels, not destructive operations.
- **D is correct.** Merging takes the changes from a feature branch and integrates them into the main branch, combining both histories into one unified codebase.

---

## Question 9 — MSQ | Hard

Sameer runs the following code:

```python
class AgeError(Exception):
    def __init__(self, message, age):
        super().__init__(f"{message}: {age}")
        self.age = age

def verify_age(age):
    if age < 0:
        raise AgeError("Negative age not allowed", age)
    elif age > 120:
        raise AgeError("Age exceeds maximum limit", age)
    return "Valid age"

try:
    result = verify_age(-5)
    print(result)
except AgeError as e:
    print("Caught:", e)
    print("Age value:", e.age)
except ValueError:
    print("Not a number")
finally:
    print("Done")
```

Which of the following statements are **correct**? *(Select all that apply.)*

**A)** The output includes the line `Caught: Negative age not allowed: -5`
**B)** The `finally` block does not run because an exception was raised
**C)** `e.age` correctly holds the value `-5` because it was stored as an instance variable in `AgeError.__init__`
**D)** Both the `except AgeError` block and the `except ValueError` block execute when `verify_age(-5)` is called

**Correct Answers:** A, C

**Answer Explanation:**
- **A is correct.** `verify_age(-5)` raises `AgeError("Negative age not allowed", -5)`. The constructor calls `super().__init__("Negative age not allowed: -5")`, so `str(e)` is `"Negative age not allowed: -5"`. The `except AgeError` block prints `Caught: Negative age not allowed: -5`.
- **B is incorrect.** The `finally` block **always** runs — whether an exception was raised, caught, or not. It is designed to execute cleanup code unconditionally. The last line of output is `Done`.
- **C is correct.** Inside `AgeError.__init__`, `self.age = age` stores the raw integer value `-5` as an instance variable on the exception object. After `except AgeError as e`, `e.age` accesses this stored value directly.
- **D is incorrect.** Only the **first matching** `except` block runs. Since `AgeError` is raised and the first `except AgeError` clause matches, Python executes it and then skips all remaining `except` clauses. The `except ValueError` block is never reached.

---

## Question 10 — MSQ | Hard

Tanvir has been asked to contribute to a team project hosted on GitHub. His workflow is:
1. Copy the remote repository to his laptop
2. Create and modify Python files locally
3. Stage all his new files
4. Commit with the message `"Add initial files"`
5. Upload his commits to the remote repository

Which of the following statements about the Git commands involved are **correct**? *(Select all that apply.)*

**A)** `git clone <url>` copies the entire remote repository — including its full commit history — to his local machine
**B)** `git add .` stages all modified and newly created files in the current directory for the next commit
**C)** `git commit -m "Add initial files"` automatically pushes the committed changes to the remote repository
**D)** `git push` uploads the locally committed changes to the central (remote) repository

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct.** `git clone <url>` does not just download the current files — it downloads the **full repository**, including every commit, branch, and tag in the history. This is what makes Git a **distributed** VCS.
- **B is correct.** `git add .` stages all changes (modifications, new files, deletions) in the current working directory. It is the broadest staging command; use it carefully as it includes everything.
- **C is incorrect.** `git commit` only saves a snapshot to the **local** repository. It has no network communication whatsoever. A separate `git push` command is required to send the commit to the remote repository.
- **D is correct.** `git push` takes all commits that exist locally but not on the remote and uploads them. It is the final step in the standard `add → commit → push` workflow.
