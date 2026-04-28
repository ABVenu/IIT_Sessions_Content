# Advanced OOP in Python: Encapsulation, Custom Exceptions & Introduction to Version Control (Git)

## Context: What We Covered Before & What's Coming Today

In the previous session, we built deep knowledge of **Inheritance** — how one class can reuse code from another. We studied `super()`, types of inheritance, **Method Overriding**, **Method Resolution Order (MRO)**, **Method Overloading**, and an introduction to **Operator Overloading** using magic methods.

Today, we complete the final major pillars of **Object-Oriented Programming** and then transition to an entirely new topic:

- **Operator Overloading** (continued) — Class-based magic method example using `__add__`
- **Passing arguments to parent constructors via `super()`** — Practical class hierarchy example
- **Polymorphism** — Bringing together overloading, overriding, and duck typing under one concept
- **Encapsulation** — Hiding data, access specifiers (public, private, protected)
- **Getter and Setter** — The recommended way to access and modify private data
- **Custom Exception Handling** — Writing your own exception classes using inheritance
- **Version Control System (VCS)** — Why we need it, how it works
- **Introduction to Git** — The most widely used VCS, core terminology, and key commands

---

## Operator Overloading — Class-Based Example

In the last session, we learned that Python lets you redefine the behavior of standard operators for your own class objects. This is done by defining **magic methods** (also called **dunder methods**) inside your class.

**Quick Recap — how Python maps an operator to a magic method:**

When you write `ob1 + ob2`, Python internally executes:
```
ob1.__add__(ob2)
```
So `ob1` maps to `self`, and `ob2` is the second argument. You now have access to both objects inside the function.

![Operator overloading: objects use magic methods like `__add__` so `+` can mean custom behavior](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-01-operator-overloading.png)

**Example — defining a custom meaning for the `+` operator:**

```python
class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):          # 'self' is ob1, 'other' is ob2
        return self.a * other.a        # Custom behavior: multiply instead of add!

ob1 = A(1)    # ob1.a = 1
ob2 = A(2)    # ob2.a = 2
ob3 = A("hi") # ob3.a = "hi"
ob4 = A(3)    # ob4.a = 3

print(ob1 + ob2)   # Output: 2     → 1 * 2
print(ob3 + ob4)   # Output: hihihi → "hi" * 3 (string repeated 3 times)
```

**How the code works:**
- `ob1 + ob2` calls `ob1.__add__(ob2)`, which returns `1 * 2 = 2`.
- `ob3 + ob4` calls `ob3.__add__(ob4)`, which returns `"hi" * 3 = "hihihi"`.
- Multiplying a string by a number in Python **repeats** it that many times.
- This shows how the same operator (`+`) produces completely different results depending on the data type of the objects — this is **Operator Overloading** in action.

**Real-World Use Case:** If you have a `Complex` number class, you can define `__add__` to add the real parts and imaginary parts separately: `(real1 + real2)` and `(imaginary1 + imaginary2)`.

---

## Passing Arguments to a Parent Constructor Using `super()`

Let's revisit an important pattern: when the child class has **more attributes** than the parent class, and you need to properly initialize both.

![Calling the parent constructor with `super().__init__(...)` so shared fields are initialized before the child adds its own](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-02-super-constructor.png)

**Example — `EMP` (parent) and `Fun` (child) classes:**

```python
class EMP:
    def __init__(self, ID, name):
        self.a = ID      # Instance variable: employee ID
        self.b = name    # Instance variable: employee name

class Fun(EMP):
    def __init__(self, ID, name, email):
        super().__init__(ID, name)   # Pass ID and name to the parent constructor
        self.c = email               # Fun's own attribute: email

# Creating an object of Fun — needs 3 arguments
ob = Fun(101, "AP", "temp@mail.com")

# ob.a = 101, ob.b = "AP" (set by EMP's constructor via super())
# ob.c = "temp@mail.com" (set by Fun's own constructor)
```

**How the code works:**
- `Fun`'s constructor receives 3 arguments: `ID`, `name`, and `email`.
- `super().__init__(ID, name)` calls `EMP`'s constructor, which sets `self.a` and `self.b`.
- After `super()` returns, `Fun` then sets `self.c = email`.
- If you **skip the `super()` call**, the parent's attributes (`self.a` and `self.b`) are never initialized. Accessing `ob.a` would raise an `AttributeError`.

> **Key Rule:** Whenever you define a constructor in a child class and you inherit from a parent, **always call `super().__init__()`** to ensure the parent's attributes are properly initialized.

---

## Polymorphism

Now that we have studied inheritance, overloading, and overriding, it is time to see the bigger picture. All of these are actually examples of one central OOP concept: **Polymorphism**.

**Official Definition:** Polymorphism means *same interface, different behavior*. The word comes from Greek — "poly" (many) + "morphism" (forms). The same code can behave in different ways depending on context.

**In Simple Words:** Think of the `+` operator. When used with integers, it adds. When used with strings, it concatenates. When used with lists, it appends. The operator is the same — `+` — but its behavior is different based on the data type. That is polymorphism.

![Polymorphism: one interface (`perform_task`, `+`, etc.), different behavior by type; duck typing fits the same idea](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-03-polymorphism.png)

**What counts as "context"?**
- The **data type** of the object (e.g., `+` on `int` vs `str`)
- The **class** of the object (e.g., calling `perform_task()` on a `Pen` vs an `Eraser`)

**Three ways Python achieves Polymorphism:**

| Mechanism | What it means |
|---|---|
| **Method Overloading** | Same function name, different number/type of parameters (Python uses default args, `*args`, `**kwargs`) |
| **Operator Overloading** | Same operator, redefined behavior based on the object's class |
| **Method Overriding** | Child class redefines a method inherited from the parent |

**Duck Typing — Polymorphism without inheritance:**

```python
class Pen:
    def perform_task(self):
        print("Writing with pen")

class Eraser:
    def perform_task(self):
        print("Erasing with eraser")

# Same function call — different behavior based on the object type
def use_tool(tool):
    tool.perform_task()   # Doesn't care what type 'tool' is

use_tool(Pen())     # Output: Writing with pen
use_tool(Eraser())  # Output: Erasing with eraser
```

**Why this is polymorphism:** `perform_task()` is called the same way, but behaves differently depending on whether the object is a `Pen` or an `Eraser`. Python doesn't require them to inherit from a common base class — as long as both have the method, it works. This is **Duck Typing**.

> **Interview Tip:** When asked "What is polymorphism in Python?", say: *"Polymorphism means the same code behaves differently based on the context — the data type or class of the object. Python supports it through method overloading, operator overloading, and method overriding."*

---

## Encapsulation

The third major pillar of OOP is **Encapsulation**.

**Official Definition:** Encapsulation means bundling data (variables) and the methods that operate on that data together into a single unit (a class), and **restricting direct access** to some of the object's components.

**In Simple Words:** Think of a medicine capsule. You can see it from outside, but you can't directly touch what's inside. If you want to interact with it, you must do so through a specific pathway — swallowing it. In code, the data inside the class is the medicine; the methods (APIs) are the designated pathway.

![Encapsulation: data is bundled inside the class; access goes through controlled methods (like a capsule or vault)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-04-encapsulation.png)

**Why do we need Encapsulation?**

Consider your bank account. If someone could directly type:
```python
account.balance = 1000000
```
...and change your balance, that would be a serious security issue!

Your bank balance should only be modified through two controlled operations:
- **Withdraw** (deduct money)
- **Deposit** (add money)

Encapsulation enforces this. You hide the `balance` variable and only allow changes through specific methods.

**Object is itself a form of Encapsulation** — it bundles data and methods together. But now we go a step further: we control *who can access what*.

---

## Access Specifiers: Public, Private, and Protected

Access specifiers define **who can access** a variable or method.

| Specifier | Syntax | Who can access it? |
|---|---|---|
| **Public** | `self.name` (no underscore) | Anyone — inside the class, outside the class, via object |
| **Private** | `self.__name` (two underscores prefix) | Only inside the class. Cannot be accessed via an object from outside. |
| **Protected** | `self._name` (one underscore prefix) | Inside the class and inside subclasses (child classes) |

![Access specifiers in Python: public (open), private (`__`), protected (`_`) — who may read or change members](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-05-access-specifiers.png)

**Example — Bank Account with a private method:**

```python
class BankAccount:
    def __init__(self):
        self.balance = 1000        # Public variable — accessible from anywhere

    def __update_balance(self, amount):   # Private method — two underscores
        self.balance -= amount

    def withdraw(self, amount):    # Public method
        if self.balance > amount:
            self.__update_balance(amount)  # Calling private method INSIDE the class — OK
            self.show_balance()
        else:
            print("Invalid withdraw amount")

    def show_balance(self):
        print(f"Balance = {self.balance}")

account = BankAccount()
account.show_balance()    # Output: Balance = 1000
account.withdraw(500)     # Output: Balance = 500

# Trying to call the private method from OUTSIDE the class:
# account.__update_balance(500)  ← This will raise AttributeError!
```

**How the code works:**
- `self.balance` is **public** — accessible from anywhere.
- `self.__update_balance` is **private** — can only be called from inside `BankAccount`.
- `withdraw()` is **public** and internally calls `__update_balance()` — this is the only controlled way to change the balance.
- Attempting `account.__update_balance(500)` from outside raises: `AttributeError: 'BankAccount' object has no attribute '__update_balance'`

**Why this is safer:** Even if someone knows the method exists, they cannot call it from outside. The only way to modify balance is through `withdraw()`, which has its own validation logic. This is security through encapsulation.

> **Design Principle:** All data (instance variables) should ideally be **private**. You should provide controlled access through dedicated functions — getters and setters.

---

## Getter and Setter

Since data should be private, how do you read or update it from outside the class? The answer is **getter** and **setter** functions.

- **Getter** — a method that **returns** the value of a private variable
- **Setter** — a method that **sets** (updates) the value of a private variable, usually with validation

These are just normal functions — the names "getter" and "setter" are a **naming convention** to communicate their purpose clearly.

![Getters and setters: controlled read/write paths to private fields, often with validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-06-getter-setter.png)

**Example — Employee class with private salary:**

```python
class Employee:
    def __init__(self):
        self.__salary = 50000    # Private variable — two underscores

    def get_salary(self):        # GETTER — reads the private salary
        return self.__salary

    def set_salary(self, amount):  # SETTER — updates the private salary
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

emp = Employee()

print(emp.get_salary())    # Output: 50000  (using getter)
emp.set_salary(60000)      # Update salary using setter
print(emp.get_salary())    # Output: 60000

# Direct access will fail:
# print(emp.__salary)  ← AttributeError: 'Employee' object has no attribute '__salary'
```

**How the code works:**
- `self.__salary` is private — not accessible directly via `emp.__salary`.
- `get_salary()` is the only way to read the salary from outside.
- `set_salary()` validates the input (`amount > 0`) before updating — protecting against invalid data.
- This clean pattern prevents bugs and makes future debugging easier.

> **Note:** Python also provides `@property`, `@getter`, `@setter` decorators as a more elegant syntax for getters and setters. The example above shows the same goal achieved with plain methods — both approaches are valid.

---

## Custom Exception Handling

In a previous session, we learned the basics of exception handling — `try`, `except`, `finally`, and built-in exceptions like `ValueError`, `ZeroDivisionError`.

**The Problem with Built-In Exceptions:** Python provides a fixed set of exceptions. But in real projects, you'll encounter situations that Python has no pre-built exception for. For example:
- Age entered is below 18 → should raise an `InvalidAgeError`
- Bank balance goes below zero → should raise an `InsufficientFundsError`

These are **business logic errors** that you must define yourself.

**Why is this connected to Inheritance?**

Python's entire exception system is built on a class hierarchy. Every exception is a class that inherits (directly or indirectly) from the base `Exception` class. To create your own custom exception, you simply **inherit from `Exception`** (or one of its subclasses) and add your own logic.

This is why we studied inheritance first — now you can write your own exception classes.

![Custom exceptions inherit from `Exception`; your class adds messages and optional extra fields](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-07-custom-exceptions.png)

**Syntax for a Custom Exception:**

```python
class MyCustomError(Exception):       # Inherit from the built-in Exception class
    def __init__(self, message, code):
        super().__init__(message)      # Pass the message to the base Exception class
        self.code = code               # Store your own error code for bookkeeping
```

**How to raise it:**
```python
raise MyCustomError("Something went wrong", code=404)
```

---

**Full Example — `InvalidAgeError`:**

```python
# Step 1: Define the custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message, age):
        # Pass a descriptive message to the base Exception class
        super().__init__(f"{message}, but your age is {age}")

# Step 2: Define the function that may trigger the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 and above", age)
    else:
        print("Access granted")

# Step 3: Call the function inside a try-except block
try:
    age = int(input("Enter age: "))   # If non-integer entered → ValueError
    check_age(age)
except InvalidAgeError as e:
    print("Custom exception caught:", e)
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Execution completed")
```

**Sample Output (if age = 5):**
```
Enter age: 5
Custom exception caught: Age must be 18 and above, but your age is 5
Execution completed
```

**Sample Output (if age = "abc"):**
```
Enter age: abc
Invalid input. Please enter a number.
Execution completed
```

**How the code works:**
- `InvalidAgeError(Exception)` — our custom class inherits from Python's `Exception`.
- `super().__init__(...)` — passes the error message up to `Exception`, which stores it. This is the minimum requirement for a custom exception.
- `raise InvalidAgeError(...)` — triggers the exception when the condition is met (age < 18).
- `except InvalidAgeError as e` — catches specifically our custom exception. `e` contains the message we passed.
- `f"{message}, but your age is {age}"` — an **f-string** (formatted string). Anything inside `{}` is treated as a variable and replaced with its actual value.
- The `except ValueError` block handles the case where someone types text instead of a number.
- `finally` always runs — whether an exception occurred or not.

**Extending the check — what if age > 100 is also invalid?**

You can handle multiple conditions inside the same custom exception class:

```python
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 and above", age)
    elif age > 100:
        raise InvalidAgeError("Age must be 100 or below", age)
    else:
        print("Access granted")
```

No new class needed — just a different message passed to the same `InvalidAgeError`.

> **Design Tip:** Group related scenarios into a single custom exception class. But if two scenarios are conceptually very different (e.g., age validation vs. bank fraud detection), create separate classes for clarity and easier debugging.

---

## Version Control System (VCS)

We now shift to a completely new and critically important topic for software engineers: **Version Control**.

### The Problem It Solves

Imagine you've spent weeks building a working project. You then start adding a new feature. Midway through, you realize the whole project is broken. You want to go back to the last working version. What do you do?

**Naive solution:** Save a copy every time you reach a stable state.

But this creates problems:
1. **Disk space** — Multiple copies of large projects eat up storage quickly.
2. **No accountability** — You don't know who changed what and when.
3. **Collaboration nightmare** — If two people modify the same file at the same time, which version is correct?
4. **No history** — You can't easily trace when a bug was introduced.

**The Systematic Solution:** A **Version Control System (VCS)** — a dedicated tool that automatically tracks every change made to every file, stores the history, identifies who made each change, and lets you revert to any previous state at any time.

**Real-World Example:** Android releases a new stable version every two years (e.g., Android 14, 15, 16). But they simultaneously maintain and patch older supported versions. They can do this because all versions exist in their VCS as tagged snapshots — they don't need to keep separate manual copies.

![Version control: central shared repository and local copies; push sends commits up, pull brings updates down](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-08-vcs-architecture.png)

---

### Architecture of a VCS

```
User 1 (Local Repo)  ←──── pull ────┐
                     ─── push ────→  │
                                     Central Repository (Remote)
User 2 (Local Repo)  ←──── pull ────┘
                     ─── push ────→
```

**Key components:**

| Component | Description |
|---|---|
| **Central Repository** | The single source of truth. Hosted on a server. All users share this. |
| **Local Repository** | Your own copy of the codebase on your machine. You work here. |
| **Pull** | Download changes from the central repo to your local repo. |
| **Push** | Upload your committed changes from local repo to the central repo. |
| **Commit** | Saving a snapshot of your changes to your local repo with a message, author, and timestamp. |

**Workflow:**
1. You join a team. You **pull** the codebase from the central repo.
2. You modify files locally.
3. Once satisfied, you **commit** your changes (saving them in your local repo with metadata).
4. You **push** the commit to the central repo.
5. Your teammates **pull** and receive your changes.

---

### VCS Terminology

| Term | Meaning |
|---|---|
| **Trunk / Main / Master** | The primary line of development. This is the stable, production-ready codebase. |
| **Branch** | A separate line of development. You create a branch to work on a feature without touching the trunk. |
| **Merge** | Combining a branch back into the trunk after the feature is complete and verified. |
| **Tag** | A human-friendly name (nickname) given to a specific commit — e.g., `v1.0-stable`. Useful for marking release points. |

**Why create a Branch instead of working directly on trunk?**

If two teammates both modify the same file in the `main` branch and then push, their changes can **conflict**. A VCS will flag this as a **conflict** — it won't know which change to keep.

By working on separate branches:
- Your changes are isolated and don't affect anyone else.
- When your feature is ready and reviewed, you merge it back cleanly.
- The trunk remains stable at all times.

**Visual of branching and merging:**

![Git-style branch: work splits from main, then merges back after the feature is ready](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-09-git-branch-merge.png)

```
Trunk:    1 ──── 2 ──── 3 ──────────────── 6 (merged)
                  \                        /
Branch:            4 ──── 5 (your work) ──
```

---

## Introduction to Git

**Git** is the most widely used version control system in the industry today.

- **Type:** Distributed VCS — every user has a full copy of the repository, not just the current version.
- **Created by:** Linus Torvalds in 2005 — the same person who created the Linux operating system. He built Git to manage Linux kernel development.

**What Git provides:**
- Track every change made to every file
- Full history of **who** changed **what** and **when**
- Ability to **revert** to any previous state
- **Branching and merging** support
- **Collaboration** between multiple developers

---

### Core Git Commands — Overview

We'll do a hands-on demo in the next session. For now, understand **what each command does**:

#### `git init`
Converts a plain directory into a Git repository. Run this once when starting a new project from scratch.

```bash
git init
```

#### `git clone`
Copies an existing remote repository to your local machine. Use this when joining a project that already exists.

```bash
git clone <repository-url>
```

#### `git status`
Shows you what files have been modified, added, or deleted — and whether those changes have been staged for commit yet.

```bash
git status
```

Git divides files into two categories:
- **Tracked files** — Files already part of the repository. Git is aware of their history. When you modify them, `git status` shows them as "modified".
- **Untracked files** — Newly created files that Git doesn't know about yet. They only exist in your local system.

#### `git add`
Tells Git which files you want to include in your next commit. This is called **staging**.

```bash
git add filename.py         # Stage a specific file
git add .                   # Stage ALL modified files (use carefully)
```

> **Warning:** Using `git add .` stages everything — including test files or debugging code you may not want to push. It's safer to explicitly name files.

#### `git commit`
Saves a snapshot of all staged changes to your local repository. Includes a **message**, **author name**, and **timestamp** automatically.

```bash
git commit -m "Add login feature"
```

The `-m` flag is followed by your commit message. Always write a clear, descriptive message explaining *why* the change was made.

#### `git log`
Displays the full history of commits on the current branch.

```bash
git log
```

Each entry shows:
- A unique **commit ID** (hash)
- **Author** name and email
- **Date and time** of the commit
- The **commit message**

To see what files were changed in a specific commit, copy the commit ID and run:
```bash
git show <commit-id>
```
This shows the exact lines added (`+`) and removed (`-`) in that commit.

#### `git branch`
Lists all branches in your local repository. The currently active branch is marked with `*`.

```bash
git branch
```

#### `git push`
Uploads your committed changes from your local repository to the central (remote) repository.

```bash
git push
```

#### `git pull`
Downloads the latest changes from the central repository to your local repository. Run this at the start of every working day.

```bash
git pull
```

---

### The Complete Workflow in One Picture

![Git areas: working directory → staging (`git add`) → local history (`git commit`) → remote (`git push`); `git pull` updates local from remote](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/IITREICT-SE-2603/session11/iit-s11-10-git-workflow.png)

```
Your Files          Local Repo          Central Repo
(Working Dir)
   │
   │  git add
   ├──────────→  Staging Area
   │                  │
   │             git commit
   │                  ├──────────────→ Local History
   │                                       │
   │                                  git push
   │                                       ├──────────→ Remote Repo
   │                                                         │
   │◄─────────────────────────────────── git pull ──────────┘
```

---

## Key Takeaways

- **Operator Overloading** lets you redefine what standard operators (`+`, `-`, `*`) mean for your custom classes, using magic methods like `__add__`. The behavior changes based on the object type.
- **Polymorphism** is the unifying concept behind overloading, overriding, and duck typing — the same interface (function/operator name) behaves differently based on the context (data type or class).
- **Encapsulation** protects your data by hiding it inside a class and only exposing controlled access through methods. Use `__variable` (two underscores) for **private**, `_variable` (one underscore) for **protected**, and no underscore for **public**.
- **Getters and Setters** are the recommended pattern for reading and updating private variables. They add validation and prevent unauthorized or accidental changes to sensitive data.
- **Custom Exception Handling** leverages inheritance — you inherit from Python's built-in `Exception` class, pass your message via `super().__init__()`, and raise your custom exception with the `raise` keyword inside application logic.
- **Version Control Systems** solve the problem of tracking changes, enabling collaboration, reverting bad code, and maintaining multiple versions of a project. The core flow is: **pull → modify → add → commit → push**.
- **Git** is a distributed VCS where every developer has a full local copy of the repository. Key commands: `git init`, `git status`, `git add`, `git commit`, `git log`, `git branch`, `git push`, `git pull`.

---

## Important Commands, Libraries & Terminologies

| Term / Syntax | Meaning |
|---|---|
| `__add__(self, other)` | Magic method for `+` operator — triggered when `obj1 + obj2` is written |
| `super().__init__(args)` | Calls the parent class constructor and passes arguments to it |
| **Polymorphism** | Same interface, different behavior based on data type or object context |
| **Encapsulation** | Bundling data and methods together; restricting direct access to internal data |
| `self.__var` | Private variable — accessible only within the class |
| `self._var` | Protected variable — accessible within the class and subclasses |
| `self.var` | Public variable — accessible from anywhere |
| **Getter** | A method that returns the value of a private variable |
| **Setter** | A method that validates and sets the value of a private variable |
| `class MyError(Exception):` | Custom exception class inheriting from Python's built-in `Exception` |
| `raise MyError(message)` | Triggers (raises) a custom exception |
| `except MyError as e:` | Catches a specific custom exception; `e` holds the error message |
| `f"string {variable}"` | F-string (formatted string) — embeds variable values directly inside a string |
| **VCS** | Version Control System — tracks changes to files over time |
| **Repository (Repo)** | A directory managed by Git that stores all files and their change history |
| **Trunk / Main / Master** | The primary stable branch of a repository |
| **Branch** | An isolated line of development, created from trunk to work on a feature |
| **Merge** | Combining a feature branch back into the main/trunk branch |
| **Tag** | A named pointer to a specific commit — e.g., `v1.0` marks a release |
| `git init` | Initializes a new Git repository in the current directory |
| `git clone <url>` | Copies a remote repository to your local machine |
| `git status` | Shows modified, staged, and untracked files |
| `git add <file>` | Stages a file to be included in the next commit |
| `git commit -m "msg"` | Saves staged changes as a commit with a descriptive message |
| `git log` | Displays the full commit history of the current branch |
| `git show <id>` | Shows the exact changes made in a specific commit |
| `git branch` | Lists all branches; the active branch is marked with `*` |
| `git push` | Uploads local commits to the central (remote) repository |
| `git pull` | Downloads latest commits from the central repository to local |
| **Tracked file** | A file that Git already knows about and is monitoring for changes |
| **Untracked file** | A newly created file that Git is not yet aware of |
| **Commit ID (Hash)** | A unique identifier automatically generated by Git for each commit |
| **Conflict** | Occurs when two people modify the same lines of the same file simultaneously |
