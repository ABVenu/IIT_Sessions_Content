# Subjective Assignment — Advanced OOP in Python: Inheritance, Overriding & Overloading

---

## Question 1 — Practical Coding Task | Medium

### The E-Commerce Product Catalog

You are building a backend module for a small e-commerce platform. The platform sells two types of products: **physical products** (like books, gadgets) and **digital products** (like e-books, software licenses). Both share common attributes, but they behave differently in certain ways — for example, a physical product has a shipping weight, while a digital product has a file size and is delivered instantly.

**Your task:** Design a class hierarchy in Python that models this system using the OOP concepts covered in this session.

---

### Requirements

**1. Base Class: `Product`**
- Constructor accepts: `name` (str), `price` (float), `category` (str)
- Method `get_info()` — prints the product's name, price, and category in a readable format
- Method `apply_discount(percent)` — reduces the price by the given percentage and prints the new price

**2. Child Class: `PhysicalProduct` (inherits from `Product`)**
- Constructor additionally accepts: `weight_kg` (float)
- Use `super().__init__()` to initialize the base class attributes
- Override `get_info()` to also display the shipping weight
- Add method `shipping_cost()` — returns `weight_kg * 50` (₹50 per kg)

**3. Child Class: `DigitalProduct` (inherits from `Product`)**
- Constructor additionally accepts: `file_size_mb` (float)
- Use `super().__init__()` to initialize the base class attributes
- Override `get_info()` to also display the file size and print `"Delivery: Instant Download"`
- Add method `shipping_cost()` — always returns `0` (digital products have no shipping cost)

**4. Function: `checkout(product)`**
- Accepts any product object (physical or digital) — use Duck Typing
- Calls `product.get_info()` and then prints the shipping cost using `product.shipping_cost()`

**5. Demo**
- Create one `PhysicalProduct` object and one `DigitalProduct` object
- Call `apply_discount(10)` on the physical product (10% off)
- Pass both objects through `checkout()`

---

### Expected Output (approximate format)

```
--- Product Info ---
Name: Python Programming Book
Price: ₹450.0
Category: Books
Shipping Weight: 0.8 kg
New price after 10% discount: ₹405.0
--- Checkout ---
Name: Python Programming Book
Price: ₹405.0
Category: Books
Shipping Weight: 0.8 kg
Shipping Cost: ₹40.0

--- Product Info ---
Name: Data Science Masterclass
Price: ₹999.0
Category: Online Course
File Size: 1200 MB
Delivery: Instant Download
--- Checkout ---
Name: Data Science Masterclass
Price: ₹999.0
Category: Online Course
File Size: 1200 MB
Delivery: Instant Download
Shipping Cost: ₹0
```

---

### Submission

- Code and Run using VS Code or any online compiler 
- Once Everything is ready - paste the code in the code editor/answer box

---

## Answer Explanation

### Ideal Solution

```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")

    def apply_discount(self, percent):
        self.price = self.price - (self.price * percent / 100)
        print(f"New price after {percent}% discount: ₹{self.price}")


class PhysicalProduct(Product):
    def __init__(self, name, price, category, weight_kg):
        super().__init__(name, price, category)
        self.weight_kg = weight_kg

    def get_info(self):
        super().get_info()
        print(f"Shipping Weight: {self.weight_kg} kg")

    def shipping_cost(self):
        return self.weight_kg * 50


class DigitalProduct(Product):
    def __init__(self, name, price, category, file_size_mb):
        super().__init__(name, price, category)
        self.file_size_mb = file_size_mb

    def get_info(self):
        super().get_info()
        print(f"File Size: {self.file_size_mb} MB")
        print("Delivery: Instant Download")

    def shipping_cost(self):
        return 0


def checkout(product):
    product.get_info()
    print(f"Shipping Cost: ₹{product.shipping_cost()}")


# Demo
book = PhysicalProduct("Python Programming Book", 450.0, "Books", 0.8)
course = DigitalProduct("Data Science Masterclass", 999.0, "Online Course", 1200)

print("--- Product Info ---")
book.get_info()
book.apply_discount(10)

print("\n--- Checkout ---")
checkout(book)

print("\n--- Product Info ---")
course.get_info()

print("\n--- Checkout ---")
checkout(course)
```

### Walkthrough

**Inheritance & `super()`:**
Both `PhysicalProduct` and `DigitalProduct` inherit from `Product`. Their constructors call `super().__init__(name, price, category)` to let the base class handle the common attributes. This avoids duplicating `self.name = name`, `self.price = price`, and `self.category = category` in every child class.

**Method Overriding:**
Both child classes override `get_info()`. Instead of completely replacing the parent's logic, they call `super().get_info()` first to print the common fields, then add their own class-specific output (`weight_kg` for physical, `file_size_mb` + delivery note for digital). This is the recommended pattern — extend the parent's behavior rather than rewrite it.

**Duck Typing in `checkout()`:**
The `checkout()` function does not check whether `product` is a `PhysicalProduct` or `DigitalProduct`. It simply calls `.get_info()` and `.shipping_cost()` on whatever is passed. Because both classes implement these methods, the function works polymorphically — this is Duck Typing in action.

**Alternative Approaches:**
- You could compute the discount inside `apply_discount` using `round()` for cleaner float display: `self.price = round(self.price * (1 - percent/100), 2)`.
- You could make `shipping_cost()` an abstract method in `Product` using the `abc` module (`from abc import ABC, abstractmethod`) to enforce that every subclass must implement it — a more robust design for larger systems.
- For the digital product, `shipping_cost()` returning `0` (int) instead of `0.0` (float) is acceptable; Python handles both fine in this context.
