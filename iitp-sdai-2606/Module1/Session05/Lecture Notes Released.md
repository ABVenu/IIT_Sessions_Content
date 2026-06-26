# DSA: Dictionaries & HashMaps - Built-in Functions

## What You Will Learn in This Lesson

You have already learned how to store many values using **lists** and how to work with **strings**. Lists and strings are accessed using positions like index `0`, `1`, `2`, and so on.

In this lesson, you will learn **dictionaries**, where data is stored using **key-value pairs**. You will also understand why dictionaries are called **hashmaps** in Python and why they are useful for fast lookups.

By the end, you will be able to:

- Create dictionaries using key-value pairs.
- Access, add, and update dictionary values.
- Use dictionary methods like **`get()`**, **`keys()`**, **`values()`**, and **`items()`**.
- Understand dictionary/hashmap intuition for fast lookup.
- Use built-in functions like **`len()`**, **`sorted()`**, **`max()`**, **`min()`**, and **`sum()`** with dictionary data.
- Build a small character-frequency counter using a dictionary.

---

## Why Programs Need Dictionaries

- **Official Definition:** A **dictionary** in Python is a data structure that stores data as **key-value pairs**.
- **In Simple Words:** A dictionary stores data with a label. You do not search using position; you search using a meaningful key.
- **Real-Life Example:** A phone book stores a person's name and phone number. You search by name and get the number directly.

If phone numbers were stored only in a list, you might need to check every contact one by one. With a dictionary, the name acts like a direct label for the number.

| Feature | List | Dictionary |
|---|---|---|
| Access by | Index, like `0`, `1`, `2` | Key, like `"name"` or `"Maa"` |
| Data style | Individual values | Key-value pairs |
| Best for | Ordered data | Labelled data |
| Example | Marks list | Contact book |

![Dictionaries big picture — phone contacts search by name, list vs dictionary comparison with indexed boxes vs labelled key-value pairs, e-commerce product ID to price, exam roll number to marks, and translation word mapping](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-01-dictionaries-big-picture.png?v=20260620)

---

## Creating and Defining Dictionaries

- **Official Definition:** A **key-value pair** stores one key and one value together, written as `key: value`.
- **In Simple Words:** The key is the label, and the value is the actual data stored under that label.
- **Real-Life Example:** In a student record, `"name"` can be the key and `"Yash"` can be the value.

A dictionary is written using curly braces **`{}`**.

```python
# Create a dictionary named student with three key-value pairs
student = {
    "name": "Yash",  # Store the student's name using the key "name"
    "age": 29,  # Store the student's age using the key "age"
    "marks": 91  # Store the student's marks using the key "marks"
}

# Print the complete dictionary
print(student)  # Output: {'name': 'Yash', 'age': 29, 'marks': 91}
```

**How the code works:**

- **`student`** is the dictionary variable.
- **`"name"`**, **`"age"`**, and **`"marks"`** are keys.
- **`"Yash"`**, **`29`**, and **`91`** are values.
- Each key-value pair is separated by a comma.

### Creating an Empty Dictionary and Adding Values Later

Sometimes you may not know the values in advance. In that case, you can create an empty dictionary and add values later.

```python
# Create an empty dictionary
student = {}

# Add the name key and its value
student["name"] = "Yash"

# Add the marks key and its value
student["marks"] = 82

# Add the age key and its value
student["age"] = 21

# Print the final dictionary
print(student)  # Output: {'name': 'Yash', 'marks': 82, 'age': 21}
```

**How the code works:**

- **`{}`** creates an empty dictionary.
- **`student["name"] = "Yash"`** adds a new key-value pair.
- The same pattern can be used when values come from user input.

### Creating a Dictionary Using `dict()`

Python also provides the **`dict()`** constructor to create dictionaries.

```python
# Create a dictionary using the dict() constructor
student = dict(name="Himanshu", age=22, marks=91)

# Print the dictionary
print(student)  # Output: {'name': 'Himanshu', 'age': 22, 'marks': 91}
```

**How the code works:**

- **`dict()`** is another way to create a dictionary.
- In this format, the keys are written without quotes.
- This is useful when keys are simple names like `name`, `age`, and `marks`.

### Important Rule: Keys Must Be Unique

Dictionary keys should be **unique**. If the same key is written again, Python keeps the latest value for that key.

```python
# Create a dictionary with the same key repeated
student = {
    "name": "Yash",  # First value for the key "name"
    "age": 29,  # Value for the key "age"
    "name": "Shubham"  # Latest value for the same key "name"
}

# Print the dictionary
print(student)  # Output: {'name': 'Shubham', 'age': 29}
```

**How the code works:**

- The key **`"name"`** appears twice.
- Python does not keep both names.
- The latest value **`"Shubham"`** overwrites the earlier value **`"Yash"`**.

---

## Accessing and Modifying Key-Value Pairs

- **Official Definition:** **Dictionary access** means getting a value using its key, written as `dictionary[key]`.
- **In Simple Words:** If you know the label, you can directly get the value stored under that label.
- **Real-Life Example:** If you know the contact name in your phone, you can directly open that contact number.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Access the value for the key "apple"
print(fruit_prices["apple"])  # Output: 40

# Update the value for the key "apple"
fruit_prices["apple"] = 45

# Add a new fruit and price
fruit_prices["orange"] = 30

# Print the updated dictionary
print(fruit_prices)  # Output: {'banana': 20, 'apple': 45, 'mango': 50, 'orange': 30}
```

**How the code works:**

- **`fruit_prices["apple"]`** accesses the value mapped to `"apple"`.
- **`fruit_prices["apple"] = 45`** updates the existing value.
- **`fruit_prices["orange"] = 30`** adds a new key-value pair.

If you use square bracket access for a key that does not exist, Python raises a **`KeyError`**. The safer method for uncertain keys is **`get()`**.

![Key-value access diagram — curly brace dictionary structure with name age city pairs, read update add delete operations, railway PNR key to seat value analogy, and contacts phone book example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-02-key-value-access.png?v=20260620)

---

## Dictionary Methods: `get()`, `keys()`, `values()`, and `items()`

- **Official Definition:** A **dictionary method** is a built-in function called on a dictionary using dot notation.
- **In Simple Words:** Methods are ready-made actions that dictionaries can perform.
- **Real-Life Example:** In a phone contact app, you can search one number, view all names, view all numbers, or view all name-number pairs.

### Using `get()` for Safe Lookup

The **`get()`** method is useful when a key may or may not exist.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Get the price of apple
print(fruit_prices.get("apple"))  # Output: 40

# Try to get the price of watermelon
print(fruit_prices.get("watermelon"))  # Output: None

# Try to get watermelon price with a default value
print(fruit_prices.get("watermelon", 0))  # Output: 0
```

**How the code works:**

- **`get("apple")`** returns `40` because `"apple"` exists.
- **`get("watermelon")`** returns `None` because `"watermelon"` does not exist.
- **`get("watermelon", 0)`** returns `0` because `0` is the default value.
- This avoids program crashes caused by missing keys.

### Using `keys()`

The **`keys()`** method returns all keys from a dictionary.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Print all keys
print(fruit_prices.keys())  # Output: dict_keys(['banana', 'apple', 'mango'])
```

**How the code works:**

- **`fruit_prices.keys()`** gives all dictionary keys.
- In this example, the keys are fruit names.

### Using `values()`

The **`values()`** method returns all values from a dictionary.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Print all values
print(fruit_prices.values())  # Output: dict_values([20, 40, 50])
```

**How the code works:**

- **`fruit_prices.values()`** gives all dictionary values.
- In this example, the values are prices.

### Using `items()`

The **`items()`** method returns key-value pairs together. It is commonly used with loops.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Loop through every key-value pair
for fruit, price in fruit_prices.items():
    # Print the fruit and its price
    print(f"{fruit} price is {price}")
```

**How the code works:**

- **`items()`** gives one key-value pair at a time.
- **`fruit`** receives the key.
- **`price`** receives the value.
- This is useful when you want to print or process every pair in a dictionary.

| Method | What It Returns | Use Case |
|---|---|---|
| **`get(key)`** | Value or `None` | Safe lookup |
| **`get(key, default)`** | Value or default | Safe lookup with fallback |
| **`keys()`** | All keys | View labels |
| **`values()`** | All values | View stored data |
| **`items()`** | Key-value pairs | Loop through dictionary |

![Dictionary methods diagram — get() safe lookup with default fallback, keys() values() items() panels, hotel reception desk analogy, and student marks method comparison table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-03-dictionary-methods.png?v=20260620)

---

## Mini Problem: Count Characters in a String

A common dictionary use case is **counting frequency**. Frequency means how many times something appears.

- **Official Definition:** A **frequency counter** stores each unique item as a key and its count as the value.
- **In Simple Words:** The dictionary remembers how many times each character has appeared.
- **Real-Life Example:** If students vote for fruits, you can count how many votes each fruit received.

For the string `"banana"`:

- `b` appears `1` time.
- `a` appears `3` times.
- `n` appears `2` times.

```python
# Store the input string
text = "banana"

# Create an empty dictionary to store character counts
counts = {}

# Go through each character in the string
for current_char in text:
    # Get the old count of the character, or use 0 if it is new
    current_value = counts.get(current_char, 0)

    # Increase the count by 1
    current_value += 1

    # Store the updated count back in the dictionary
    counts[current_char] = current_value

# Print the final character counts
print(counts)  # Output: {'b': 1, 'a': 3, 'n': 2}
```

**How the code works:**

- **`counts`** starts as an empty dictionary.
- The loop picks one character at a time from `"banana"`.
- **`counts.get(current_char, 0)`** checks whether the character already exists.
- If the character is new, the count starts from `0`.
- The count is increased by `1` and saved back into the dictionary.

This pattern is very useful in coding problems because dictionaries make repeated counting simple.

---

## HashMaps: Why Dictionaries Are Fast

- **Official Definition:** A **hashmap** is a data structure that stores key-value pairs using a **hash function** for fast lookup.
- **In Simple Words:** A hashmap is like an address system. Instead of searching everywhere, Python uses the key to reach the value quickly.
- **Real-Life Example:** If someone gives you the exact house address, you do not search every house in the city.

In Python, a **dictionary is a hashmap**. Different programming languages may use different names, but the idea is the same: store and retrieve data using key-value pairs.

Examples of names in different languages:

- Python: **dictionary**
- Java: **HashMap**
- JavaScript: **object**
- C++: **map**

### List Lookup vs Dictionary Lookup

If data is stored in a list, Python may need to check many values one by one. If data is stored in a dictionary, Python can use the key to reach the value quickly.

```python
# Create a dictionary of fruit prices
fruit_prices = {
    "banana": 20,  # Store banana price
    "apple": 40,  # Store apple price
    "mango": 50  # Store mango price
}

# Directly get the value using the key
print(fruit_prices["mango"])  # Output: 50
```

**How the code works:**

- Python uses the key **`"mango"`** to find the mapped value.
- You do not manually loop through all fruit names.
- This is why dictionaries are useful for fast lookups.

### Time Complexity Intuition

- A list search can take **O(n)** time because Python may check many values.
- A dictionary lookup is generally **O(1)** time because Python uses hashing to jump close to the value directly.
- **O(1)** means constant time: the lookup does not grow in the same way as checking every item one by one.

### Internal Hashing Intuition

Python internally creates a **hash value** from the key. That hash value helps Python decide where the value should be stored in memory.

Think of a car valet system:

- You give your car and receive a token/key.
- Later, you give the token back.
- The valet does not search every car randomly.
- The token helps the valet locate your car quickly.

Similarly, a dictionary key helps Python locate the value quickly.

---

## Hashable Keys: What Can Be Used as a Dictionary Key?

- **Official Definition:** A **hashable** value is a value that Python can convert into a stable hash.
- **In Simple Words:** A dictionary key should be something stable that Python can trust as a label.
- **Real-Life Example:** A roll number can be a stable key. A changing shopping list is not a stable key.

Valid key types commonly include:

- **String**, such as `"name"`
- **Integer**, such as `101`
- **Boolean**, such as `True`
- **Tuple**, when its values are also hashable

A **list** cannot be used as a dictionary key because lists can change.

```python
# Create a dictionary with valid key types
details = {
    "name": "Rahul",  # String key
    101: "Room A",  # Integer key
    True: "Active"  # Boolean key
}

# Access a value using an integer key
print(details[101])  # Output: Room A

# A list cannot be used as a key
# bad_dict = {[1, 2]: "value"}  # This would raise TypeError: unhashable type: 'list'
```

**How the code works:**

- **`"name"`**, **`101`**, and **`True`** are valid keys.
- A list like **`[1, 2]`** is not valid as a key.
- Values can still be lists; the restriction is mainly for keys.

![Hashmap fast lookup diagram — list scan vs dictionary direct key access, hash function jumping to mango price slot, bank locker analogy, and hashable vs unhashable key types table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-04-hashmap-fast-lookup.png?v=20260620)

---

## Built-in Functions for Dictionary Data

Python provides built-in functions that work well with dictionaries.

### `len()`

- **Official Definition:** **`len(dictionary)`** returns the number of key-value pairs in a dictionary.
- **In Simple Words:** It counts how many entries are present.
- **Real-Life Example:** Counting how many fruits are listed in a price chart.

```python
# Create a dictionary of prices
prices = {
    "apple": 30,  # Apple price
    "banana": 10,  # Banana price
    "mango": 20  # Mango price
}

# Count how many key-value pairs are present
print(len(prices))  # Output: 3
```

**How the code works:**

- The dictionary has three pairs.
- So **`len(prices)`** returns `3`.

### `sorted()`

- **Official Definition:** **`sorted()`** returns a new sorted list.
- **In Simple Words:** It arranges data in order without changing the original dictionary.
- **Real-Life Example:** Arranging fruit names alphabetically on a menu.

```python
# Create a dictionary of prices
prices = {
    "mango": 20,  # Mango price
    "apple": 30,  # Apple price
    "banana": 10  # Banana price
}

# Sort dictionary keys
print(sorted(prices))  # Output: ['apple', 'banana', 'mango']

# Sort dictionary values
print(sorted(prices.values()))  # Output: [10, 20, 30]
```

**How the code works:**

- **`sorted(prices)`** sorts the keys.
- **`sorted(prices.values())`** sorts the values.
- The original dictionary remains unchanged.

### `max()`, `min()`, and `sum()`

When dictionary values are numbers, you can use more built-in functions on **`values()`**.

```python
# Create a dictionary of prices
prices = {
    "mango": 20,  # Mango price
    "apple": 30,  # Apple price
    "banana": 10  # Banana price
}

# Find the maximum value
print(max(prices.values()))  # Output: 30

# Find the minimum value
print(min(prices.values()))  # Output: 10

# Find the total of all values
print(sum(prices.values()))  # Output: 60
```

**How the code works:**

- **`max(prices.values())`** finds the highest price.
- **`min(prices.values())`** finds the lowest price.
- **`sum(prices.values())`** adds all prices.

![len and sorted on dictionaries diagram showing key-value pair count, sorted keys, sorted values, and original dictionary unchanged note](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session05/session05-05-len-sorted-builtin.png?v=20260620)

---

## Practice Programs

### Practice 1: Create and Print a Student Dictionary

```python
# Create a dictionary for one student
student = {
    "name": "Amit",  # Store student name
    "age": 21,  # Store student age
    "marks": 88  # Store student marks
}

# Print the complete dictionary
print(student)  # Output: {'name': 'Amit', 'age': 21, 'marks': 88}
```

**How the code works:**

- The dictionary stores one student's details.
- Each detail has a key and a value.

### Practice 2: Safe Lookup with `get()`

```python
# Create a dictionary of scores
scores = {
    "Amit": 78,  # Amit's score
    "Sneha": 91,  # Sneha's score
    "Rahul": 85  # Rahul's score
}

# Get a score for a present key
print(scores.get("Sneha", "Not found"))  # Output: 91

# Get a score for an absent key
print(scores.get("Kiran", "Not found"))  # Output: Not found
```

**How the code works:**

- **`Sneha`** exists, so her score is returned.
- **`Kiran`** does not exist, so the default value is returned.

### Practice 3: Loop Through Key-Value Pairs

```python
# Create a menu dictionary
menu = {
    "Dosa": 60,  # Dosa price
    "Idli": 40,  # Idli price
    "Vada": 35  # Vada price
}

# Print each dish and price
for dish, price in menu.items():
    # Display one key-value pair
    print(f"{dish}: Rs.{price}")
```

**How the code works:**

- **`items()`** gives both the dish and price.
- The loop prints each pair one by one.

### Practice 4: Count Characters

```python
# Store a sample string
text = "banana"

# Create an empty dictionary for counts
counts = {}

# Loop through every character
for char in text:
    # Increase the count for the current character
    counts[char] = counts.get(char, 0) + 1

# Print the final result
print(counts)  # Output: {'b': 1, 'a': 3, 'n': 2}
```

**How the code works:**

- Each character becomes a dictionary key.
- The value stores how many times that character appears.
- **`get(char, 0)`** makes the counting logic safe and short.

---

## Common Debugging Tips

- Use **`get()`** when a key may not exist.
- Remember that duplicate keys are overwritten by the latest value.
- Check whether you used curly braces **`{}`** for dictionaries.
- Remember that dictionary keys must be hashable.
- Use **`sorted(dictionary)`** for sorted keys.
- Use **`sorted(dictionary.values())`** for sorted values.

---

## Key Takeaways

- **Dictionaries** store data as **key-value pairs**, which is useful for labelled information like contacts, prices, marks, and counts.
- You can create dictionaries using **curly braces**, an empty dictionary, or the **`dict()`** constructor.
- **`get()`**, **`keys()`**, **`values()`**, and **`items()`** are important dictionary methods for safe lookup and iteration.
- Python dictionaries work like **hashmaps**, which helps with fast key-based lookup.
- Built-in functions like **`len()`**, **`sorted()`**, **`max()`**, **`min()`**, and **`sum()`** help analyse dictionary data.

These dictionary skills will be useful whenever you need to store labelled data, count repeated values, or retrieve information quickly in upcoming programming tasks.

---

## Important Commands, Libraries, and Terminologies Used

| Term / Command | What It Does |
|---|---|
| **Dictionary** | Stores key-value pairs |
| **Key** | Label used to access a value |
| **Value** | Data stored against a key |
| **`{key: value}`** | Syntax for creating dictionary pairs |
| **`dict()`** | Constructor used to create a dictionary |
| **`dict[key]`** | Accesses or updates a value using a key |
| **`get(key)`** | Safely gets a value or returns `None` |
| **`get(key, default)`** | Safely gets a value or returns the default |
| **`keys()`** | Returns all keys |
| **`values()`** | Returns all values |
| **`items()`** | Returns key-value pairs |
| **Hashmap** | Data structure for fast key-based lookup |
| **Hash function** | Internal function that helps map a key to a storage location |
| **Hashable** | A value that can be used as a dictionary key |
| **`KeyError`** | Error when a missing key is accessed using square brackets |
| **`TypeError: unhashable type`** | Error when an invalid key type, like list, is used |
| **`len(dictionary)`** | Counts key-value pairs |
| **`sorted(dictionary)`** | Returns sorted dictionary keys |
| **`sorted(dictionary.values())`** | Returns sorted dictionary values |
| **`max(dictionary.values())`** | Finds the highest value |
| **`min(dictionary.values())`** | Finds the lowest value |
| **`sum(dictionary.values())`** | Adds all numeric values |
