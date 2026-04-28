# Subjective Assignment — Advanced OOP in Python: Encapsulation, Custom Exceptions & Introduction to Git

---

## Question 1 — Practical Coding Task | Medium

### The Library Book Loan System

You are building the backend for a digital library. The library manages books, each with a limited number of physical copies. When a member tries to borrow a book, the system must check if copies are available. When they try to return one, the system must ensure they aren't returning more copies than were ever loaned out. Any violation should raise a **custom exception** — not a generic Python error.

**Your task:** Implement this system in Python using Encapsulation, Getters & Setters, and Custom Exception Handling.

---

### Requirements

**1. Custom Exception: `BookNotAvailableError`**
- Inherits from `Exception`
- Constructor accepts: `message` (str) and `title` (str — the book's title)
- Must call `super().__init__()` with the message
- Must also store `title` as an instance variable

**2. Custom Exception: `InvalidReturnError`**
- Inherits from `Exception`
- Constructor accepts: `message` (str) and `title` (str)
- Same structure as above

**3. Class: `Book`**
- All three core attributes must be **private**:
  - `__title` (str)
  - `__total_copies` (int)
  - `__available_copies` (int) — starts equal to `__total_copies`
- **Getter methods:**
  - `get_title()` — returns `__title`
  - `get_available_copies()` — returns `__available_copies`
  - `get_total_copies()` — returns `__total_copies`
- **Setter method:**
  - `set_total_copies(n)` — updates `__total_copies` only if `n > 0`, otherwise prints `"Invalid: copies must be greater than 0"`
- **Method `borrow()`:**
  - If `__available_copies > 0`: decrement it by 1 and print a confirmation message
  - Otherwise: raise `BookNotAvailableError` with an appropriate message and the book's title
- **Method `return_book()`:**
  - If `__available_copies < __total_copies`: increment `__available_copies` by 1 and print a confirmation message
  - Otherwise: raise `InvalidReturnError` (all copies are already in — nothing was borrowed)

**4. Demo**
- Create a `Book` object: title `"Clean Code"`, `2` total copies
- Successfully borrow it twice (both should succeed)
- Attempt to borrow a third time — handle the `BookNotAvailableError` and print the error and the book title from the exception
- Return one copy successfully
- Attempt to return when all copies are already back — handle the `InvalidReturnError`

---

### Expected Output (approximate format)

```
Borrowed: Clean Code. Copies left: 1
Borrowed: Clean Code. Copies left: 0
Error: No copies available for "Clean Code"
Book title from exception: Clean Code
Returned: Clean Code. Copies left: 1
Error: All copies of "Clean Code" are already returned
```

---

### Submission

- Code and run using VS Code or any online compiler
- Once everything is working, paste your code in the code editor / answer box

---

## Answer Explanation

### Ideal Solution

```python
# --- Custom Exceptions ---

class BookNotAvailableError(Exception):
    def __init__(self, message, title):
        super().__init__(message)
        self.title = title


class InvalidReturnError(Exception):
    def __init__(self, message, title):
        super().__init__(message)
        self.title = title


# --- Book Class ---

class Book:
    def __init__(self, title, total_copies):
        self.__title = title
        self.__total_copies = total_copies
        self.__available_copies = total_copies   # All copies start as available

    # Getters
    def get_title(self):
        return self.__title

    def get_available_copies(self):
        return self.__available_copies

    def get_total_copies(self):
        return self.__total_copies

    # Setter with validation
    def set_total_copies(self, n):
        if n > 0:
            self.__total_copies = n
        else:
            print("Invalid: copies must be greater than 0")

    def borrow(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"Borrowed: {self.__title}. Copies left: {self.__available_copies}")
        else:
            raise BookNotAvailableError(
                f'No copies available for "{self.__title}"',
                self.__title
            )

    def return_book(self):
        if self.__available_copies < self.__total_copies:
            self.__available_copies += 1
            print(f"Returned: {self.__title}. Copies left: {self.__available_copies}")
        else:
            raise InvalidReturnError(
                f'All copies of "{self.__title}" are already returned',
                self.__title
            )


# --- Demo ---

book = Book("Clean Code", 2)

# Two successful borrows
book.borrow()
book.borrow()

# Third borrow — triggers BookNotAvailableError
try:
    book.borrow()
except BookNotAvailableError as e:
    print(f"Error: {e}")
    print(f"Book title from exception: {e.title}")

# Successful return
book.return_book()

# Over-return — triggers InvalidReturnError
book.return_book()   # This brings copies back to 2 (all returned)
try:
    book.return_book()
except InvalidReturnError as e:
    print(f"Error: {e}")
```

---

### Walkthrough

**Encapsulation:**
All three attributes (`__title`, `__total_copies`, `__available_copies`) are declared with double underscores, making them private. No code outside the class can read or change them directly — all access goes through the provided getter and setter methods. This mirrors real-world systems where critical data (like inventory counts) must be protected from accidental modification.

**Getter and Setter:**
The `get_*` methods provide read-only external access to private data. The `set_total_copies()` setter adds a validation gate (`n > 0`) before allowing any update — this is the key advantage of setters over direct attribute access. A direct assignment like `book.__total_copies = -5` could corrupt the system; the setter prevents it.

**Custom Exception Handling:**
Both `BookNotAvailableError` and `InvalidReturnError` inherit from `Exception`. Each calls `super().__init__(message)` to register the human-readable message with the base class (so `str(e)` works correctly), while also storing the `title` as an instance variable on the exception object. This allows the `except` block to extract structured information (`e.title`) beyond just the text message — a key advantage of custom exceptions over generic ones.

**Alternative Approaches:**
- You could add a `borrowed_count` attribute instead of tracking available copies — `borrowed_count` increments on borrow and decrements on return, and the borrow guard becomes `if self.__borrowed_count < self.__total_copies`.
- For a more Pythonic approach, Python's `@property` decorator can turn `get_title()` into a property so callers write `book.title` instead of `book.get_title()` — both are valid design choices.
- The `borrow()` and `return_book()` methods could be extended to accept a `member_name` parameter to track **who** borrowed which book, making the system ready for multi-user scenarios.
