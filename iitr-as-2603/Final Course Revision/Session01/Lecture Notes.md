# Python Foundations and Version Control

This session covers the programming core that later topics sit on: how a Python program stores values, makes decisions, repeats work, organises data, and how Git keeps a recoverable history of that work. Short examples pin a definition. They are reminders of a rule.

## 1. What you are revising, and why it still matters

An agent, a database query, and a prompt template are all ordinary programs underneath. If a type is wrong, a loop never stops, or a secret is committed, the later system fails in a way that looks like an “AI problem” and is actually a Python or Git problem.

Keep three questions in mind while you revise:

1. What value does this expression produce, and what type is it?
2. What changes in memory, and what is only displayed?
3. What is saved in history, and what is still only on your machine?

## 2. Environment and how a program actually runs

Python is a language. A program is a text file the interpreter reads from top to bottom. The usual local stack is: Python installed on the machine, a terminal to type commands, and an editor such as VS Code to write and run files.

### 2.1 Install and PATH

The terminal finds Python by searching the system PATH, the list of folders it is allowed to look in. If Python is installed but `python3` is “not found”, the install often succeeded and the PATH entry did not. Installing on the local disk, rather than inside a synced folder such as OneDrive, avoids path and permission errors that appear only on some machines.

Check the interpreter you are actually using before you debug a library. Two Pythons on one laptop is a common reason a package is “installed” and still missing.

### 2.2 Scripts and notebooks

| Form | What it is | Practical point |
|---|---|---|
| `.py` file | A plain script | Runs top to bottom with `python3 filename.py` |
| `.ipynb` notebook | Cells you run one at a time | Needs a kernel, the interpreter attached to that notebook |

A notebook cell can succeed while a later cell still holds an old variable from a previous run. Restarting the kernel and running from the top is the reliable check. A script does not keep leftover state between runs.

### 2.3 Virtual environments

A virtual environment is a project-specific folder of packages. It keeps one project’s libraries from changing another project’s libraries. Create it, activate it, then install into it.

A package installed into the system Python is invisible inside an inactive environment, and the reverse is also true.

### 2.4 AI coding aids

Completion tools speed up typing and can suggest a fix. They do not replace reading the error. The habit that matters is: read the message, locate the line, state what you expected, then change one thing.

### 2.5 Secrets, in one paragraph

An API is a contract that lets one program ask another program for a result. An API key is a secret that proves the caller is allowed. Keys belong in a `.env` file that is listed in `.gitignore`, so Git never records them.

Hard-coding a key into a script puts the secret into history the moment you commit.

**Edge cases**

- `python` and `python3` can be different installations. Use the one your environment was created with.
- Auto-save in the editor does not run the file. Saving and executing are separate steps.
- An online compiler is a fallback when the local install is broken. It is a poor place for secrets or large files.

**Recall:** PATH, terminal, virtual environment, `.py` versus notebook, `.env`.

## 3. Variables, types, and names

A variable is a name bound to a value. `age = 26` stores the integer 26 under the name `age`. Assigning again, `age = 27`, rebinds the name.

Printing shows the current binding. The old value is gone unless some other name still refers to it.

Python is case-sensitive. `True` is a Boolean. `true` is an undefined name and raises an error.

`Score` and `score` are two different names.

### 3.1 The four basic types

| Type | Example | What it is for |
|---|---|---|
| `int` | `26` | Whole numbers |
| `float` | `3.14` | Numbers with a fractional part |
| `str` | `"hello"` | Text |
| `bool` | `True`, `False` | A yes-or-no result |

`type(x)` reports the type of the value currently bound to `x`. Built-in types are themselves classes. `type(10)` reports `int`.

### 3.2 Comments, expressions, and statements

A comment starts with `#` and is ignored by the interpreter. An expression produces a value (`2 + 3`). A statement does a job (`x = 5`, or a call to `print`).

Many lines are both: an assignment statement whose right-hand side is an expression.

### 3.3 Names that share one object

If `a = [1, 2]` and `b = a`, then `a` and `b` are two names for the same list. `a.append(3)` changes what `b` sees. This is the aliasing edge case.

Rebinding `a = [1, 2, 3]` creates a new list and leaves `b` pointing at the old one. Append mutates. Assignment rebinds.

**Edge cases**

- A name used before assignment raises `NameError`.
- Rebinding does not update other names that were pointing at the previous object.
- Floats are not exact decimal fractions. Equality checks on floats can fail around the fifteenth decimal place. Compare rounded values, or accept a small tolerance, when the values came from division.

**Recall:** rebinding, `type()`, case sensitivity, aliasing.

## 4. Operators

### 4.1 Arithmetic

| Operator | Meaning | Edge to remember |
|---|---|---|
| `+ - *` | Add, subtract, multiply | `+` on two strings joins them |
| `/` | True division | Always returns a float: `7 / 2` is `3.5` |
| `//` | Floor division | Drops the fractional part toward minus infinity |
| `%` | Remainder | Useful for “every nth” checks |
| `**` | Power | `2 ** 3` is `8` |

Precedence follows the usual order: brackets, then exponents, then multiplication and division, then addition and subtraction. When a line is hard to read, add parentheses. They document intent and remove doubt.

`+` joins two strings. `"age: " + 26` fails, because a string and a number are different types. Convert explicitly with `str(26)`.

The reverse conversion, `int("26")` or `float("3.5")`, fails with `ValueError` when the text is not a number (`int("26 years")`, `int("")`).

### 4.2 Comparison and assignment

Comparison operators are `==`, `!=`, `>`, `<`, `>=`, `<=`. Every comparison returns a Boolean.

`=` stores a value. `==` asks whether two values are equal. Writing `if x = 5` is a syntax error in Python, because assignment is not an expression you can drop into a condition the way some other languages allow.

Writing `if x == 5` is the test.

Compound assignment updates a name from its current value: `a += 10` means `a = a + 10`. The same pattern exists for `-=`, `*=`, and `/=`. The name must already exist.

`count += 1` on a name that was never set raises `NameError`.

### 4.3 Logical operators and short-circuit

`and` is true when both sides are true. `or` is true when at least one side is true. `not` flips the Boolean.

Precedence among them: brackets, then `not`, then `and`, then `or`. `True or False and False` is `True`, because `and` binds first.

Short-circuit evaluation skips work:

- `and` does not evaluate the right side when the left side is already false.
- `or` does not evaluate the right side when the left side is already true.

That is why `x != 0 and (10 / x) > 1` is safe when `x` is `0`: the division is never attempted. Swapping the sides removes the protection.

**Edge cases**

- `//` on negatives is a frequent surprise: `(-7) // 2` is `-4`, not `-3`, because floor division rounds toward negative infinity.
- Chaining comparisons such as `0 < x < 10` is allowed and means both tests must pass.
- `bool("False")` is `True`. Any non-empty string is true. Only the empty string is false among strings. `bool(0)` is `False`. `bool(0.0)` is `False`.

**Recall:** `/` versus `//`, `=` versus `==`, precedence, short-circuit.

## 5. Decisions, input, and output

### 5.1 if, elif, else

`if` runs its block only when the condition is true. `else` covers the remaining case. `elif` adds further conditions.

In one chain, exactly one branch runs: the first condition that is true. Later branches are skipped even if they would also have been true. Put the more specific test above the broader one.

Indentation defines the block. Four spaces is the convention. A missing indent, or a mix of tabs and spaces, is a syntax error, not a logic error.

Nested `if` statements are for layered checks, such as “logged in, and then an admin”.

### 5.2 input and print

`input()` always returns a string, even when the person types `42`. Convert with `int()` or `float()` before you do arithmetic. Converting an empty entry or a word raises `ValueError`.

A practical pattern is to validate inside a loop and ask again, which is covered with `while` below.

`print()` can take several arguments. `sep` is the text placed between them (default is a space). `end` is the text placed after them (default is a newline).

`end=""` keeps the next print on the same line, which is how nested loops draw a row of characters.

An f-string inserts values into text: `f"Hello {name}, {age} yrs"`. Format specs control appearance: `{pi:.2f}` shows two decimal places, `{num:,}` inserts thousands separators. The spec changes the displayed text.

It does not change the stored number.

**Edge cases**

- Two true `elif` conditions: only the first matching branch runs.
- `int(input())` crashes on blank input. Guard it, or catch the error, when the input comes from a person.
- An f-string with a missing name raises `NameError` at the moment the string is built, not later.

**Recall:** one branch per chain, indentation, `input()` is text, f-string format specs.

## 6. Loops

A loop repeats a block. Choose the kind from what you know before the loop starts.

| Loop | Driven by | Counter | Use when |
|---|---|---|---|
| `while` | A condition | You update it yourself | The number of repeats is unknown, such as “ask until the input is valid” |
| `for` | A sequence or `range` | Advances automatically | You are walking items, or you know the span |

### 6.1 while, and the infinite-loop edge

`while count < 5` keeps going for as long as the condition stays true. If the body never changes `count`, the condition never becomes false and the loop never ends. That is the classic failure.

Every `while` needs a change that moves the condition toward false: increment a counter, shorten a collection, or set a flag when the work is done.

A loop invariant is a fact that is true before the loop and still true after every iteration. “`count` is the number of greetings already printed” is an invariant for a counting loop. Invariants are how you argue that a loop is correct and that it will stop.

### 6.2 for and range

`for char in "Python"` visits each character. `for item in numbers` visits each element.

`range` produces a sequence of integers. The stop value is excluded.

- `range(5)` is `0, 1, 2, 3, 4`.
- `range(3, 10)` starts at 3 and stops before 10.
- `range(3, 10, 2)` is `3, 5, 7, 9`.
- `range(10, 3, -2)` walks downward. A positive step that never moves toward the stop produces an empty sequence, not an error. `range(10, 3)` is empty because the default step is `+1` and 10 is already past 3.

### 6.3 break, continue, and nesting

`break` leaves the nearest enclosing loop immediately. In a nested loop it leaves only the inner loop. The outer loop continues.

`continue` skips the rest of the current iteration and starts the next one. It does not leave the loop.

Total iterations of a simple nest are outer count times inner count, provided neither loop breaks early. The inner loop runs to completion for each outer step. Use the outer loop for rows and the inner loop for columns when you are walking a grid.

**Edge cases**

- `break` inside `if` still breaks the loop, not the `if`. `if` is not a loop.
- A `continue` placed before the counter update in a `while` can skip the update and spin forever.
- Off-by-one: `range(1, n)` visits `1` through `n - 1`. If the last value must be included, the stop is `n + 1`.

**Recall:** manual counter for `while`, stop is exclusive, `break` is innermost, empty `range` when the step points the wrong way.

## 7. Lists

A list is an ordered, mutable collection. It may hold mixed types and duplicates. Create one with `[]` or `list()`.

A list is the right everyday container for a sequence you will grow, reorder, or edit.

Indexing starts at `0`. Negative indexes count from the end: `-1` is the last item, `-2` the one before it. `items[len(items)]` is out of range.

`items[-1]` on an empty list is also out of range.

### 7.1 Slicing

`items[start:stop:step]` includes `start` and excludes `stop`. Omitting `start` means “from the beginning”. Omitting `stop` means “through the end”.

`items[::-1]` is a reversed copy, because the step is `-1`.

Slicing never raises an index error for a stop that runs past the end. It simply stops. Indexing a single missing position does raise `IndexError`.

That difference is easy to miss.

### 7.2 Walking a list

- `for item in items` gives each value.
- `for i in range(len(items))` gives each index, which you need when you must write back into the list.
- `enumerate(items)` gives index and value together.
- `zip(names, scores)` pairs two sequences element by element and stops at the shorter one. Extra items in the longer sequence are silently ignored.

### 7.3 Methods that change the list, and functions that do not

| Operation | Effect |
|---|---|
| `append(x)` | Adds one item at the end |
| `extend(other)` | Adds each item from another iterable |
| `insert(i, x)` | Inserts at an index and shifts the rest |
| `pop()` | Removes and returns the last item; `pop(i)` removes at an index |
| `remove(x)` | Removes the first matching value; errors if the value is absent |
| `sort()` | Sorts in place and returns `None` |
| `sorted(items)` | Returns a new sorted list and leaves the original |
| `reverse()` | Reverses in place |
| `count(x)`, `index(x)` | How many, and the first position |

`append([1, 2])` adds one element, and that element is a list. `extend([1, 2])` adds two numbers. Mixing them up is the usual “nested list appeared from nowhere” bug.

`list("ab")` produces `["a", "b"]`, because a string is iterable. `list(5)` fails, because an integer is not iterable.

**Edge cases**

- `items.sort()` used in a larger expression is a bug, because the method returns `None`. Assign from `sorted(items)` when you need the result.
- `remove` deletes by value, once. A second copy of the same value stays.
- Modifying a list while iterating over it skips or repeats elements. Iterate over a copy, or build a new list, when you are filtering.

**Recall:** zero-based and negative indexes, slice excludes stop, `append` versus `extend`, `sort` versus `sorted`.

## 8. Strings

A string is an immutable sequence of characters. You can index and slice it with the same rules as a list. You cannot assign to `text[0]`.

Any “change” builds a new string.

Quotes may be single, double, or triple. Triple quotes hold a multi-line string. `+` concatenates.

`*` repeats: `"ha" * 3` is `"hahaha"`. `len` counts characters, including spaces.

Useful methods: `lower`, `upper`, `title`, `capitalize`, `replace(old, new)`, `split`. `split()` with no argument breaks on whitespace and returns a list of words. `split(",")` breaks on commas.

Methods do not edit the original string. `name.upper()` returns a new string; `name` is unchanged unless you rebind it.

**Edge cases**

- `"Hello".lower() == "hello"` is the safe comparison when user text may vary in case. Category tags and dictionary keys have the same issue later: `"Returns"` and `"returns"` are different keys.
- `split(",")` on `"a, b"` leaves the space attached to `" b"`. Strip pieces when the separator sits next to spaces.
- Slicing still excludes the end: `"Python"[0:2]` is `"Py"`.

**Recall:** immutability, methods return new strings, case-sensitive matching.

## 9. Functions

A function is a named block you can call. `def` defines it.

The definition does not run the body. The call does.

```python
def area(width, height):  # define a function that expects two numbers
    return width * height  # send the product back to the caller

result = area(3, 4)  # call it and store 12
```

`return` sends a value back to the caller and ends the function immediately. Code after a `return` in the same block never runs. `print` only displays.

A function with no `return` returns `None`. Using that `None` in arithmetic fails later, often far from the function, which makes the bug look mysterious.

### 9.1 How arguments are passed

| Kind | Behaviour |
|---|---|
| Positional | Filled in order. Omitting a required one raises `TypeError` |
| Default | Used when the caller omits that argument |
| Keyword | Named at the call, so order can change: `area(height=4, width=3)` |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dictionary |

A parameter is the name in the definition. An argument is the value supplied at the call.

### 9.2 Scope

A name assigned inside a function is local. It disappears when the function returns. A name assigned outside is global.

A local name hides a global name spelled the same way; the function then sees the local one. Read globals freely. Assigning to a global name from inside a function needs an explicit `global` declaration, and even then it is usually clearer to return a value and assign it outside.

### 9.3 The mutable default argument

This is the sharpest function edge case:

```python
def add_item(item, bucket=[]):  # the default list is created once, at definition
    bucket.append(item)  # later calls that omit bucket share that same list
    return bucket  # the caller sees items from earlier calls too
```

The default list is created once, when the function is defined, and reused on every call that omits `bucket`. The second call still contains the first call’s item. The safe pattern is a default of `None`, then create a new list inside the function when the caller did not pass one.

Functions should do one clear job. A function that both computes and prints is harder to reuse, because the caller cannot capture the result.

**Edge cases**

- Extra positional arguments, or a missing required one, raise `TypeError` at the call.
- Returning several values actually returns one tuple. The caller can unpack it.
- A default argument is evaluated at definition time, not at call time. That is why the mutable default is shared.

**Recall:** `return` versus `print`, local shadows global, never use a list or dict as a default.

## 10. Dictionaries

A dictionary stores key-value pairs. Create one with `{}` or `dict()`. Keys are unique.

Assigning a key that already exists overwrites the value. There is no error and no second entry.

| Need | Form | If the key is missing |
|---|---|---|
| Read | `d[key]` | `KeyError` |
| Read safely | `d.get(key)` | Returns `None` |
| Read with a fallback | `d.get(key, default)` | Returns `default` |
| Existence | `key in d` | `False`. This checks keys, not values |
| Add or update | `d[key] = value` | Creates the key if needed |
| Remove and return the value | `d.pop(key)` | `KeyError` unless you pass a default |
| Remove the last inserted pair | `d.popitem()` | `KeyError` on an empty dict |
| Remove without a return | `del d[key]` | `KeyError` if absent |

Walk pairs with `for key, value in d.items()`. `keys()` and `values()` give the other views. Values are not required to be unique.

Nested dictionaries are ordinary values that happen to be dictionaries; reach an inner field with successive keys, and guard each level if any key might be absent.

**Edge cases**

- `in` on a dictionary tests keys. `20 in {"age": 20}` is `False`.
- Keys must be immutable. A string, number, or tuple of immutables can be a key. A list cannot.
- Two lookups of a missing key with `[]` crash the program. `.get` is the form to use when absence is a normal case, such as an optional field in a JSON object.

**Recall:** duplicate keys overwrite, `[]` versus `.get`, `in` checks keys, `pop` versus `del`.

## 11. Classes and objects

A class is a blueprint. An object is one instance built from that blueprint. The class name is conventionally PascalCase: `BankAccount`, `Computer`.

A method is a function defined inside the class. Its first parameter is `self`, the instance the method was called on. You do not pass `self` at the call site.

`account.deposit(50)` supplies the account as `self` automatically.

`__init__` is the constructor. It runs by itself when you write `account = BankAccount("Asha", 100)`. You never call `__init__` by name in ordinary code.

Its job is to set the starting attributes: `self.owner`, `self.balance`.

Each object has its own attribute values. Two accounts created from the same class do not share a balance. Changing one leaves the other alone.

That is the difference between instance attributes (set on `self`) and a value stored on the class itself, which would be shared. For this revision, store per-object data on `self` inside `__init__`.

A method can protect its own state. `withdraw` should refuse an amount larger than the balance, or a negative amount, and leave the object unchanged when the request is invalid. Returning a Boolean or raising an error are both acceptable signals.

Silent failure, where the method prints a message and the caller thinks the withdrawal happened, is the bug.

**Edge cases**

- Forgetting `self` in the definition makes the call fail with a missing-argument error, because Python still passes the instance.
- Using an attribute before `__init__` sets it raises `AttributeError`.
- `type(account)` reports the class. `isinstance` is the check you want when subclasses might appear later.

**Recall:** class versus object, `self`, `__init__` runs on creation, each instance has its own state.

## 12. Version control with Git and GitHub

Version control records how files changed, who changed them, when, and why. Without it, two people editing the same file overwrite each other, and there is no way back to last Tuesday’s working copy.

### 12.1 What kind of system Git is

| Style | Where the history lives | Weakness |
|---|---|---|
| Local only | One machine | A lost laptop loses the history |
| Centralized | One server | The server is a single point of failure |
| Distributed (Git) | A full copy on every machine, plus an optional remote | You must sync on purpose |

Git is the local tool. GitHub is a hosting service for Git repositories. The repository on your laptop and the repository on GitHub are separate copies until you push or pull.

### 12.2 The three areas

1. Working directory: the files you edit.
2. Staging area: the exact changes you have marked for the next snapshot.
3. Local repository: the commits, the permanent snapshots.

`git status` tells you which files are untracked, which are modified, and which are staged. `git diff` shows the unstaged edits. `git add file` stages.

`git add` of everything stages all current changes, including files you may not have meant to share. `git commit -m "message"` snapshots only what is staged. A beautiful commit message with nothing staged creates an empty situation you will notice on the next status: the edits are still uncommitted.

`git log` shows history. A useful message says why the change exists, not only which file moved.

### 12.3 Remotes, branches, and review

| Command | Job |
|---|---|
| `git clone url` | Copy a remote repository, history included, onto your machine |
| `git push` | Send your commits to the remote |
| `git pull` | Bring remote commits into your current branch |
| `git switch name` | Move onto another branch (`git checkout` is the older form) |
| `git branch -d name` | Delete a local branch that has been merged |

`main` (sometimes `master`) holds the stable line. A feature branch is an independent line for one piece of work. Remote-tracking names look like `origin/main`.

`origin` is the default nickname of the remote.

A pull request asks someone to review a branch before it is merged. Opening the request does not itself merge. Review can catch a secret, a broken path, or a change that fights someone else’s work.

The end-to-end habit is: create or clone, branch, edit, stage, commit, push, open a pull request, merge, delete the feature branch.

Access on a shared repository is layered: read, then write (push), then maintain, then admin. Private repositories are visible only to people who were granted access. Public repositories are visible to anyone.

### 12.4 Undoing, carefully

| Situation | Command | What you keep |
|---|---|---|
| Discard uncommitted edits in a file | `git restore file` | The last committed version of that file |
| Unstage, but keep the edits in the file | `git reset file` | Your working changes, no longer staged |
| Fix the message of the latest commit, before anyone else has it | `git commit --amend` | The same snapshot, with a new message |

Amending rewrites the latest commit. Do that before you push it. After it is shared, rewriting history forces everyone else to reconcile their copy.

A merge conflict happens when two branches edit the same lines. Git stops and marks the file. You choose the correct combined text, then stage and commit.

The conflict is resolved by a person, not by a second pull.

### 12.5 What must never be committed

`.env`, key files, and large generated folders belong in `.gitignore` before the first commit that would have included them. If a secret is committed and then deleted in a later commit, it is still in the history. Prevention is the practical rule: ignore the file first.

**Edge cases**

- `git commit` does not upload anything. Without `git push`, GitHub still has the old copy.
- `git pull` on a branch with uncommitted edits can refuse to proceed, or can create a merge you did not expect. Commit or stash first.
- `git add *` from the wrong folder can stage a virtual environment or a data dump. Read `git status` before every commit.
- Deleting a branch does not delete the commits if they were merged. Deleting an unmerged branch with force throws away that line of work.

**Recall:** working, staging, repository; commit is local; push publishes; a pull request is a review request; ignore secrets before they enter history.

## 13. How the pieces connect

A script reads input as text, converts types, branches with `if`, repeats with a loop, and stores structured records in a list of dictionaries. A function wraps one of those jobs and returns a value. A class wraps data and the methods that are allowed to change it.

Git records each of those files as a series of snapshots you can share and roll back.

When an exercise fails, classify it before you rewrite it:

| Symptom | Likely cause |
|---|---|
| `SyntaxError` | Indentation, a missing colon, or `=` inside a condition |
| `NameError` | Typo, or a name used before assignment |
| `TypeError` | String concatenated with a number, or a bad call signature |
| `ValueError` | `int()` on text that is not a whole number |
| `IndexError` | A list position that does not exist |
| `KeyError` | A dictionary key that does not exist |
| `AttributeError` | A method or attribute the object does not have |
| Tests pass locally and fail for someone else | A missing dependency, a path that only exists on your machine, or a secret that was never in the repo |

## 14. Worked micro-cases

These are the situations that look small and decide whether a program is correct. Talk through the result before you read the note under each one.

### Case A — the grading chain

A score of 95 is tested as `if score >= 90`, then `elif score >= 80`, then `elif score >= 70`. The first branch matches, so the later branches do not run. Reversing the tests, and checking `>= 70` first, would mark every passing score as the lowest grade, because 95 is also at least 70.

Order in an `elif` chain is part of the meaning.

### Case B — validation that must not crash

A prompt asks for an age. The person presses Enter. `int("")` raises `ValueError`, so a single conversion is not a complete input step.

The durable pattern is a `while` loop: read text, try the conversion, and `break` only when the conversion succeeds and the number is in a sensible range (an age of `-3` converts cleanly and is still wrong). `continue` sends control back to the prompt. The loop ends only on a value you are willing to keep.

### Case C — a search that should stop early

You walk a list of order ids looking for one match. After you find it, `break` avoids useless work. Without `break`, the loop is still correct if you only set a flag, but it always scans the rest of the list.

Inside a nested loop, that `break` does not abandon the outer scan. If the outer loop is “each customer” and the inner loop is “each order”, finding one order leaves the next customer still to be checked.

### Case D — two names, one list

`cart = ["pen"]` and `backup = cart` share one list. `cart.append("book")` changes `backup` as well. A real backup is a copy: `backup = cart.copy()` (or `cart[:]`).

Later, when an agent keeps a conversation history and also passes that history into a function, the same aliasing rule applies. If the function appends, the caller’s list changes too.

### Case E — a function that prints and returns nothing

```python
def total(prices):  # define a function that receives a list of prices
    print(sum(prices))  # display 30, and return nothing

bill = total([10, 20])  # bill becomes None, not 30
```

The screen shows `30`. `bill` is `None`. Any later line that adds tax to `bill` fails.

The fix is `return sum(prices)`, and let the caller decide whether to print. Display and result are different jobs.

### Case F — dictionary overwrite

Loading records in a loop with `catalog[item["sku"]] = item` keeps one record per SKU. A second row with the same SKU silently replaces the first. If duplicates should be an error, test `if sku in catalog` before assigning.

If duplicates should accumulate, the value should be a list of records, not a single record.

### Case G — a bank account that accepts a bad withdrawal

`withdraw` subtracts and then checks the balance. The account can go negative for a moment, and any other method that reads `self.balance` in between would see the illegal value. Check first, and change state only when the check passes.

The same “validate, then mutate” order shows up again when an agent is about to call a tool that writes data.

### Case H — the commit that did not contain the fix

You edit `app.py`, run it, and it works. `git commit -m "fix total"` was issued when `app.py` was still unstaged, or you committed a different file. `git status` after the commit still shows `app.py` as modified.

The working program and the committed program are different until you stage and commit again, and GitHub stays on the older commit until you push.

### Case I — the secret that status would have shown

A new `.env` appears as an untracked file. If `.gitignore` already lists `.env`, status hides it and `git add` of ordinary files will not pick it up. If the ignore rule is added after the file was committed, Git keeps tracking it.

Ignore rules do not rewrite history. They only change what future adds pick up.

## 15. Self-check

Answer without looking up, then check the section.

1. What does `7 / 2` return, and what does `7 // 2` return?
2. Why can `and` protect a later division from dividing by zero?
3. What does `range(5, 1)` produce, and why?
4. Which loop does `break` leave when the loops are nested?
5. What is the difference between `append` and `extend`?
6. Why does `items.sort()` assigned to a name give you `None`?
7. Why is a list a dangerous default argument?
8. What does `d.get("city")` return when `"city"` is absent, compared with `d["city"]`?
9. When does `__init__` run?
10. Which Git command publishes commits, and which command only snapshots them locally?
11. Why is deleting a secret in a new commit not the same as never having committed it?
12. What does a pull request do at the moment you open it?

If any answer is fuzzy, that section is the one to reread. The later revision sessions assume these rules are solid: JSON objects behave like dictionaries, tool arguments are function calls, and a shared repository is a Git history.

## Try this yourself

Copy this program into a file and run it. Before you run it, write down what you expect `bill` and `backup` to be.

```python
def total(prices):  # display a sum and return nothing
    print(sum(prices))  # the screen will show 30

cart = ["pen"]  # one list object
backup = cart  # a second name for that same list
cart.append("book")  # both names see the new item
bill = total([10, 20])  # bill is None
print(backup, bill)  # expect ['pen', 'book'] and None
```

**How the code works**

- `print` inside `total` does not create a value the caller can store.
- `backup = cart` does not copy the list. `append` changes the one list both names share.
- A real copy would be `cart.copy()` before the append.

## Key Takeaways

- A name points at a value. Assignment rebinds the name. Methods such as `append` can change the object other names still see.
- `return` gives a value back. `print` only displays. `input` always gives text.
- `while` needs a change that makes the condition false. `break` leaves only the nearest loop. A slice excludes the stop and does not raise for a stop past the end.
- Stage, then commit, then push. A pull request asks for review. Secrets belong in `.env` before the first commit that could have included them.
- The next notes use these rules when a JSON object behaves like a dictionary and a tool call behaves like a function.

## Important Commands, Libraries, Terminologies used

| Term | Meaning |
|---|---|
| `int`, `float`, `str`, `bool` | The four basic types |
| `=` / `==` | Store a value / ask whether two values are equal |
| `/` / `//` | True division / floor division |
| `and`, `or`, `not` | Logical tests, with short-circuit evaluation |
| `break` / `continue` | Leave the nearest loop / skip to the next iteration |
| `append` / `extend` | Add one item / add each item from another iterable |
| `sort()` / `sorted()` | Sort in place and return `None` / return a new list |
| `.get(key)` | Dictionary read that returns `None` when the key is missing |
| `self`, `__init__` | The instance itself / the constructor that runs on creation |
| Working tree, staging, commit | Edits, the next snapshot, the saved snapshot |
| `git push` / pull request | Publish commits / ask for review before a merge |
