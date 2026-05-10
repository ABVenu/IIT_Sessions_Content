# Install Pandas and Create Series

## 1. Why Pandas?
We use Pandas because **Lists are too simple** and **Excel is too manual**. 
In the real world, data isn't just a list of numbers; it has *context*. A list `[100, 200]` is meaningless. A Series `{'Revenue': 100, 'Cost': 200}` tells a story. Pandas gives us the **speed** of low-level arrays (NumPy) with the **usability** of high-level spreadsheets.

## 2. Analogy: The Locker Room
-   **Python List:** Value-based. "Go to locker #42". You have to remember *what* is inside #42. If you move the contents, the number doesn't help you find it.
-   **Pandas Series:** Label-based. "Go to 'Tim's Locker'". You don't need to know the number; you just look for the name tag. Even if Tim moves to a different physical locker, his name tag moves with him.


![Anatomy of a Pandas Series](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-1-series-anatomy.webp)

## 3. Key Concepts
-   **Series:** A 1D labeled array. It is the fundamental building block of Pandas. (A DataFrame is just a bunch of Series glued together).
-   **Index:** The labels. Unlike lists, these can be integers, strings, dates, or anything else. The index is "immutable" (safer) and "hashable" (faster).
-   **Values:** The actual data, stored efficiently as a NumPy array.
-   **Dtype (Data Type):** Pandas enforces a single data type per Series (e.g., all integers) to optimize memory usage.

## 4. Structure of a Series
A Series object consists of four key components:
1.  **Values**: The data array (backed by NumPy).
2.  **Index**: The labels for the data.
3.  **Name**: (Optional) Name of the Series (becomes the column name when converted to DataFrame).
4.  **dtype**: The data type (int64, float64, object, datetime64, etc.).

## 5. Creating Series (Code Examples)

### Basic: Lists and Arrays
```python
import pandas as pd

# From List (Default Index 0, 1, 2...)
data = [10, 20, 30]
s = pd.Series(data)
# 0    10
# 1    20
# dtype: int64
```

### Intermediate: Custom Indexing
```python
# Context: Monthly Sales Data
sales = [1500, 2000, 1800]
months = ['Jan', 'Feb', 'Mar']
s = pd.Series(sales, index=months)
# Jan    1500
# Feb    2000
# ...
```

### Advanced: From Scalar
```python
# Broadcasting a single value
s = pd.Series(0, index=['A', 'B', 'C'])
# A    0
# B    0
# ...
```

## 6. Under the Hood: The NumPy Connection
Pandas is built *on top* of NumPy. When you create a Series `pd.Series([1, 2, 3])`, Pandas actually creates a NumPy array `np.array([1, 2, 3])` to store the values.
-   **Why care?** Because NumPy arrays are contiguous blocks of memory (C-style), making operations 100x-1000x faster than standard Python lists which store pointers to objects scattering around memory.

## 7. Common Pitfalls
-   **Pitfall:** Mixing types in a list (e.g., `[1, 'A', 3.5]`) forces Pandas to use the `object` dtype.
-   **Consequence:** You lose the performance benefits of NumPy. Using `object` dtype is as slow as standard Python lists.
-   **Best Practice:** Keep your data homogeneous (all numbers or all strings) whenever possible.


---

# Create DataFrame from CSV Files

## 1. Why CSV?
CSV (Comma Separated Values) is the **Universal Language** of data transfer. It is simple text, human-readable, and supported by every data tool since the 1970s (Excel, SQL, Legacy Systems).
`pd.read_csv()` is arguably the most important function in the entire Pandas library. It is robust enough to handle messy, broken, or gigabyte-sized files.

## 2. Analogy: The Universal Translator
-   **CSV File:** A book written in a simple but rigid dialect ("Comma Language").
-   **`pd.read_csv()`:** Your **Translator**.
    -   *Dialects:* "This book uses Semicolons!" $\rightarrow$ `sep=';'`.
    -   *No Title:* "This book starts directly with the story!" $\rightarrow$ `header=None`.
    -   *Dates:* "Translate these strings into Calendars!" $\rightarrow$ `parse_dates=['DateCol']`.


![Reading a CSV File into a DataFrame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-7-csv-to-dataframe.png)

## 3. Key Concepts
-   **Path:** Can be a local file (`data.csv`) or a URL (`https://...`).
-   **Separator (`sep`):** Default is comma `,`. Common alternatives are Tab (`\t`) or Pipe (`|`).
-   **Header:** Default is row 0. If data starts immediately, use `header=None`.
-   **Index Column:** You can pick a specific column to become the Index (Label) immediately upon load.

## 4. Code Examples

### Basic: The Standard Load
```python
df = pd.read_csv('sales_data.csv')
# Pandas automatically uses the first row as headers.
# Pandas automatically adds a default 0,1,2 index.
```

### Intermediate: Customizing Structure
```python
# File has no headers, and uses '|' as separator
df = pd.read_csv('log_file.txt', 
                 sep='|', 
                 header=None, 
                 names=['ID', 'Timestamp', 'Message'])
```

### Advanced: The "Index Col" Shortcut
Instead of loading integer index 0, 1, 2... use the ID column.
```python
df = pd.read_csv('employees.csv', index_col='EmployeeID')
# Now you can immediately use df.loc[501]
```

## 5. Under the Hood: C-Engine Speed
Why is `pd.read_csv()` so fast?
-   It uses a specialized parser written in **C**, not Python.
-   It reads the file in binary chunks (Memory Mapping).
-   It guesses data types by sampling the first N rows (Type Inference).
-   *Result:* It can read a 1GB file in seconds, whereas a manual Python `for` loop would take minutes.

## 6. Common Pitfalls
-   **Encoding Errors:** Python expects UTF-8 (Modern Standard). Excel sometimes saves as "CP1252" or "Latin-1" (Windows Standard).
    -   *Error:* `UnicodeDecodeError`
    -   *Fix:* `pd.read_csv(..., encoding='cp1252')`
-   **ParserTokenError:** Usually means your separator is wrong (e.g., using comma notation for a tab-separated file).
    -   *Fix:* Check `sep='\t'` or `sep='|'`.


---

# Understand DataFrame Structure

## 1. Why Structure Matters?
A DataFrame isn't just a blob of data. It has a precise anatomy consisting of three distinct components: **Index**, **Columns**, and **Values**.
If you confuse the **Index** (Labels) with the **Values** (Data), your analysis will fail. You need to know exactly which part of the map you are looking at.

## 2. Analogy: The City Map
-   **Index (Rows):** The Street Names (1st St, 2nd St). These label the *horizontal* lines.
-   **Columns:** The Avenue Names (5th Ave, 6th Ave). These label the *vertical* lines.
-   **Values:** The Building at the intersection (The data).
-   **Shape:** The size of the city (10 blocks by 5 blocks).
-   *Crucial Insight:* If you pull out the **Values** (`.values`), you dissolve the map grid and just have a pile of bricks (NumPy Array) with no addresses.


![DataFrame Structure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-8-df-structure.png)

## 3. Key Concepts
-   **`.index`**: The Row Labels. Immutable object.
-   **`.columns`**: The Column Headers. Immutable object.
-   **`.values`**: The raw data. This is a NumPy array. It strips away all the friendly Pandas implementations.
-   **`.shape`**: A tuple `(n_rows, n_cols)`.
-   **`.dtypes`**: A Series describing the data type of each column.

## 4. Code Examples

### Inspection
```python
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

print(df.shape)   # (2, 2)
print(df.columns) # Index(['A', 'B'], dtype='object')
print(df.index)   # RangeIndex(start=0, stop=2, step=1)
```

### Accessing the Raw Array
```python
raw_matrix = df.values
# [[1, 3]
#  [2, 4]]
# Note: The column names 'A' and 'B' are GONE.
```

## 5. Under the Hood: Shared Pointers
Here is a secret: The Index is often shared.
-   If you slice a DataFrame (`df2 = df.iloc[0:5]`), `df2` does not necessarily copy the Index string labels in memory. It might point to the *same* Index object in memory as `df`.
-   **Why?** This saves massive amounts of RAM when working with millions of rows.
-   **Side Effect:** This is why Indexes are **immutable**. If `df2` changed the Index, it would break `df`!

## 6. Common Pitfalls & Best Practices
-   **Pitfall: Modifying Index/Columns Directly**
    -   You cannot do `df.index[0] = 5`. The Index object is **immutable** (cannot be changed in place) for safety.
    -   **Fix:** You must replace the *entire* index: `df.index = [5, 1]`.
-   **Best Practice: Check `df.info()`**
    -   Before starting analysis, always run `df.info()`. It summarizes Index, Columns, Dtypes, and Memory usage in one command. It is your diagnostic dashboard.


---

# Inspect Data Quickly

## Core Concept: Initial Reconnaissance
Data inspection is the mandatory first step of Exploratory Data Analysis (EDA). These 5 methods (`head`, `tail`, `sample`, `shape`, `info`) form the standard operating procedure for loading any new dataset.

---

## 1. Visual Inspection
Never assume the data loaded correctly just because Pandas didn't throw an error.

```python
import pandas as pd
df = pd.read_csv('employees.csv')

# 1. Check the top 5 rows (default) to verify headers mapped correctly
df.head()

# 2. Check the last 10 rows to ensure file integrity at the EOF marker
df.tail(10)

# 3. Check 5 random rows to verify data isn't uniquely structured at the edges
df.sample(5, random_state=42) # random_state ensures reproducibility
```

---


![Quick DataFrame Inspection Methods](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-61-inspection-map.png)

## 2. Dimensionality with `.shape`
`.shape` is not a method; it is a DataFrame attribute derived from the underlying NumPy architecture. Therefore, it does not use parentheses `()`.

```python
dimensions = df.shape
print(f"The dataset has {dimensions[0]} rows and {dimensions[1]} columns.")
```

---

## 3. Deep Dive with `.info()`
`df.info()` is the diagnostic x-ray of your DataFrame. You must learn to read its output fluently.

```python
df.info()

# Expected output breakdown:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99                <- Validates exact row count
# Data columns (total 3 columns):                 <- Validates exact column count
#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   ID       100 non-null    int64             <- Perfect column, no missing data
#  1   Name     98 non-null     object            <- String column, 2 missing values!
#  2   Salary   100 non-null    float64           <- Decimal column
```
*(Cruciual takeaway: Comparing the `Non-Null Count` against the `RangeIndex` immediately exposes columns with missing `NaN` data).*

---

## Pro-Tip: Memory Usage
By default, `df.info()` estimates memory. To get the exact RAM usage of the DataFrame (crucial for large files), pass `memory_usage='deep'`.

```python
df.info(memory_usage='deep')
```


---

# Select Columns from DataFrame

## 1. Why Select?
We rarely analyze *everything* at once. Datasets can have hundreds of columns. Selecting columns is how we filter the "Noise" to see the "Signal".
It is also a memory optimization technique: extracting just the 2 columns you need into a new variable frees up resources compared to dragging the whole table around.

## 2. Analogy: The Jukebox
-   **The DataFrame:** The full Jukebox with 100 songs (Columns).
-   **Selecting One (`df['Song A']`)**: You press a button, and the song starts playing. You get the **Audio Stream** (The Series). It's no longer a list; it's the raw content.
-   **Selecting a List (`df[['Song A', 'Song B']]`)**: You create a **Playlist**. Even if the playlist has only 1 song, it is still a *list* of songs (A DataFrame), not the audio stream itself.


![Selecting Columns from a DataFrame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-9-select-columns.webp)

## 3. Key Concepts
-   **Bracket `['Col']`**: Returns a **Series**. Use this for analysis (math, stats).
-   **Double Bracket `[['Col']]`**: Returns a **DataFrame**. Use this for structural operations (filtering, merging) where you want to keep the table format.
-   **Dot `df.Col`**: A convenient shorthand helper, but limited.

## 4. Code Examples

## Sample Dataset
```python
import pandas as pd

df = pd.DataFrame({
    'Name':       ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Age':        [28, 34, 45, 29, 38],
    'Department': ['HR', 'Engineering', 'Finance', 'Engineering', 'HR'],
    'Salary':     [55000, 82000, 91000, 78000, 61000],
    'Email':      ['alice@co.com', 'bob@co.com', 'carol@co.com', 'david@co.com', 'eva@co.com'],
})
```

### 1. The Standard Selection
```python
# Returns Series
ages = df['Age']
avg_age = ages.mean()
```

### 2. The Subset Selection (Double Brackets)
```python
# Returns DataFrame (Sub-table)
contact_info = df[['Name', 'Email']]
```

### 3. The Dot Notation Shortcut
```python
# Fast to type, easy to read
names = df.Name
```

## 5. Under the Hood: View vs Copy
When you select a column (`df['A']`), Pandas usually returns a **View**, not a Copy.
-   **View:** It points to the *exact same memory* as the original DataFrame.
-   **Consequence:** If you modify this view (`s[0] = 0`), it *might* change the original DataFrame.
-   This makes Pandas fast (no copying gigabytes of data), but it introduces the risk of "Side Effects".

## 6. Common Pitfalls: The Dot Notation Trap
Dot notation (`df.Column`) looks clean, but it is dangerous:
1.  **Spaces:** `df.First Name` is a syntax error. Must use `df['First Name']`.
2.  **Conflicts:** If you have a column named `sum`, `df.sum` calls the *method* `sum()`, preventing you from accessing the data!
3.  **Assignment:** You **cannot** create new columns with dot notation. `df.NewCol = 10` does nothing to the DataFrame (it just creates a temporary attribute).
    -   **Rule:** Always use brackets `df['NewCol'] = 10` for assignment.


---

# Select Rows using loc

## 1. Why `loc`?
Standard Python lists use integer positions (0, 1, 2). But in Business, we use **Names**. 
-   "Find Q3 Revenue" (Date Index).
-   "Find Employee #5501" (ID Index).
-   "Find Japan's GDP" (Country Index).
`loc` allows us to look up data by its human-readable label. It aligns the code with the business question.

## 2. Analogy: The Music Request
-   **`iloc` (Position):** "Play Track #3". You need to memorize the tracklist order. If a new song is inserted at #1, your request plays the wrong song.
-   **`loc` (Label):** "Play *Bohemian Rhapsody*". You just need the name. It works regardless of where the song sits in the playlist.
-   **Slicing (`loc['A':'C']`):** "Play everything from Abba (A) to Coldplay (C)".
    -   *Crucial difference:* In Python lists (`0:2`), the stop is excluded. In `loc` (and music playlists), you expect to hear the last artist too. **Inclusive Slicing**.


![Selecting with .loc[ ]](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-10-loc-flow.png)

## 3. Key Concepts
-   **Label-Based:** Must use exact index labels.
-   **Inclusive Slicing:** `start:stop` includes *both* start and stop.
-   **KeyError:** Raised if the label is not found.
-   **Syntax:** `df.loc[Row_Label, Column_Label]` (Optional Column Label allows specific cell access).

## 4. Code Examples

## Sample Dataset
```python
import pandas as pd

df = pd.DataFrame({
    'Name':       ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Finance', 'Engineering', 'Marketing'],
    'Salary':     [55000, 82000, 91000, 78000, 61000],
}, index=['EMP_001', 'EMP_002', 'EMP_003', 'EMP_004', 'EMP_005'])
```

### 1. Single Row (Returns Series)
```python
# Context: DataFrame index is Employee IDs
emp = df.loc['EMP_001']
# Returns all columns for that employee
```

### 2. Multi-Row Selection (Returns DataFrame)
```python
# Context: Compare two specific employees
comparison = df.loc[['EMP_001', 'EMP_005']]
```

### 3. Slicing with Columns
```python
# Context: Get specific fields for a range of employees
# Rows: From A to B (Inclusive)
# Cols: Just 'Name' and 'Salary'
subset = df.loc['EMP_001':'EMP_010', ['Name', 'Salary']]
```

## 5. Under the Hood: Optimizing Lookups
How does Pandas find "Alice" in 1 million rows instantly?
-   It uses **Hash Maps** (similar to Python Dictionaries). It calculates the hash of the string 'Alice', finds the memory address, and jumps straight there (`O(1)`).
-   If you used a Loop to search, you'd check every row (`O(N)`).
-   **Caveat:** If your index is *not* unique (two Alices), Pandas falls back to a slower search. `loc` is fastest on unique indexes.

## 6. Common Pitfalls
-   **Type Mismatch:** If your index is strings (`'100'`) and you ask for an integer (`100`), `loc` will fail (KeyError). The types must match exactly.
-   **Slicing Unsorted Index:** If you try to slice `df.loc['A':'Z']` but your index is unsorted (Z comes before A), older versions of Pandas might return garbage or fail. 
-   **Best Practice:** Sort your index (`df.sort_index()`) before doing heavy slicing.


---

# Select Rows using iloc

## 1. Why Position?
Sometimes data doesn't have good labels. Or maybe the labels are messy/unknown. 
Sometimes you just want:
-   "The first 5 rows" (Head).
-   "The last row" (Tail).
-   "Every 10th row" (Sampling).
`iloc` (Integer Location) allows you to access data by its integer position (0, 1, 2...), treating the DataFrame exactly like a standard Python list or matrix.

## 2. Analogy: Address vs GPS
-   **`.loc` (Address):** "123 Main St". Relies on the assigned name. If the city renames the street, the address breaks.
-   **`.iloc` (GPS):** "34.05° N, 118.24° W". Relies on the absolute physical position. Even if the street name changes, the coordinates point to the same physical spot.


![Selecting with .iloc[ ]](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-11-iloc-flow.svg)

## 3. Key Concepts
-   **Integer-Based:** Must use integers (0, 1, 2...). No strings allowed.
-   **Exclusive Slicing:** `0:3` returns rows 0, 1, 2 (Stops *before* 3). This is standard Python behavior (0-indexed, upper-bound exclusive), which makes it consistent with lists `my_list[0:3]`.
-   **Syntax:** `df.iloc[row_position, col_position]`.

## 4. Code Examples

### 1. Basic Positional Access
```python
first_row = df.iloc[0]       # Position 0 (Series)
last_row = df.iloc[-1]       # Last Position (Series)
```

### 2. Slicing Ranges
```python
first_five = df.iloc[0:5]    # Rows 0,1,2,3,4 (Exclusive)
```

### 3. Advanced Stepping (Sampling)
```python
# Start at 0, go the end, step by 10
sample = df.iloc[::10]       # Every 10th row
```

### 4. 2D Slicing (Matrix Style)
```python
# First 3 Rows, First 2 Columns
subset = df.iloc[0:3, 0:2]
```

## 5. Under the Hood: Direct Memory Access
`iloc` is generally faster than `loc` for single-item access because it bypasses the Index Hash Map.
-   **Mechanism:** It jumps directly to the memory offset. `Row 0` is at `Start_Address + 0`. `Row 5` is at `Start_Address + 5 * Row_Size`.
-   **No Search:** There is no "Looking up" of labels. It is pure pointer arithmetic.

## 6. Common Pitfalls: The Integer Index Trap
The most confusing edge case in Pandas occurs when you have an Index that consists of Integers.
**Scenario:**
```python
df = pd.DataFrame(['A', 'B', 'C'], index=[10, 20, 30])
```
-   **`df.loc[0]`**: Fails! (Looking for label 0. It doesn't exist).
-   **`df.iloc[0]`**: Success! Returns 'A' (The item at position 0).
-   **`df[0]`**: Ambiguous.
**Rule:** When Index is integers, `[]` is dangerous. Always explicit use `.iloc` if you mean position.

## 7. Comparison Table
| Feature | `.loc` | `.iloc` |
| :--- | :--- | :--- |
| **Input** | Labels / Strings | Integers |
| **Slicing** | **Inclusive** (Start to End) | **Exclusive** (Start to End-1) |
| **Column Access** | By Name (`'Age'`) | By Position (`3`) |
| **Use Case** | Business Logic | Iteration / Sampling |


---

# Reset and set index using reset_index() and set_index()

## Core Concept: Shifting Data Hierarchies
The Pandas Index is the backbone of data alignment and retrieval (via `.loc[]`). Manipulating the index allows you to reorganize data for specific analytical tasks, particularly Time-Series analysis or Multi-Index aggregations.

---

## 1. Promoting a Column: `set_index()`

This method extracts a column (or multiple columns) from the DataFrame body and establishes it as the new row identifier.

```python
import pandas as pd

df = pd.DataFrame({
    'Employee_ID': [49201, 49202, 49203, 49204, 49205],
    'First_Name':  ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Department':  ['Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary':      [72000, 95000, 68000, 74000, 102000]
})

# Assume a DataFrame with columns: ['Employee_ID', 'First_Name', 'Salary']
# Promote the Unique Employee ID to be the index
df_indexed = df.set_index('Employee_ID')

# Now you can instantly retrieve an employee without using a boolean mask
salary = df_indexed.loc[49201, 'Salary']
```

### Important Traits of `set_index`:
*   **Destructive by default**: The original index (e.g., 0, 1, 2) is completely deleted.
*   **Column Removal**: The promoted column is removed from the list of standard `df.columns`. It now belongs exclusively to `df.index`. 

---


![set_index() vs reset_index()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-67-index-reset-set.png)

## 2. Demoting the Index: `reset_index()`

When the current index is no longer optimal (e.g., after a `groupby` operation that moves grouping keys into the index), you reset it to push those values back into standard columns.

```python
# Assume 'Department' is currently acting as the index
# Demote 'Department' back to a standard column, and insert a fresh 0,1,2 index
flattened_df = df_indexed.reset_index()
```

### Controlling the Demoted Data: `drop=True`
If the current index is just a broken sequence of row numbers from a previous filter (e.g., `4, 19, 42`), saving those numbers as a column is useless clutter. 

```python
# The messy numbers are deleted entirely. The new index is clean (0,1,2...)
clean_filter_df = df_filtered.reset_index(drop=True)
```


---

# Filter DataFrame using Boolean Conditions

## 1. Why Filter?
Data analysis is rarely about summarizing the *whole* dataset. It's about comparing segments.
-   "How do *High Value* customers compare to *Low Value* ones?"
-   "Show me the error logs where status is *Critical*."
Filtering (or "Boolean Indexing") is the mechanism to slice the data based on its **content**, not its position.

## 2. Analogy: The Nightclub Bouncer
-   **The Condition:** "Are you over 21?" (`Age >= 21`).
-   **The Mask:** The ID check. The bouncer looks at every person in line and assigns a status: "Yes" (True) or "No" (False).
-   **The Filter:** The velvet rope. Only the "Yes" crowd gets inside. The "No" crowd is left on the street. The result is a smaller group of people, but they all share the trait of being > 21.


![Filtering with Boolean Conditions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-12-boolean-filter.png)

## 3. Key Concepts
-   **Boolean Mask:** A Series of `True`/`False` values that has the exact same length as your DataFrame.
-   **Application:** `df[mask]`. Pandas overlays the mask on the DataFrame. It keeps rows where the mask is `True` and discards `False`.
-   **Comparators:** Standard Python operators work: `==`, `!=`, `>`, `<`, `>=`.

## 4. Code Examples

### 1. The Explicit Mask (Step-by-Step)
```python
# Step 1: Create the boolean series
mask = df['Score'] > 90
# mask is: [True, False, True...]

# Step 2: Apply it
top_students = df[mask]
```

### 2. The One-Liner (Best Practice)
```python
# More concise, standard industry syntax
passed = df[df['Grade'] == 'Pass']
```

### 3. String Filtering
```python
# Filter where City is Paris
paris_data = df[df['City'] == 'Paris']
```

## 5. Under the Hood: Bitmaps
When you assign a Boolean value (`True`/`False`), Pandas/NumPy stores it as a single byte (or even a single bit in packed structures).
-   This makes "Masks" incredibly small in memory compared to the original data.
-   Applying the mask is a low-level "Bitmap" operation. The CPU scans the mask and selectively copies memory addresses where the bit is 1. This is why filtering 10 million rows takes milliseconds.

## 6. Troubleshooting & Pitfalls
-   **Empty Result:** If `filtered_df` is empty, check your condition. Did you check `City == 'paris'` (lowercase) when the data is `'Paris'` (Title case)? String comparison is case-sensitive!
-   **NaN Values:** `NaN` comparisons are tricky. `NaN == NaN` is False. If you want to filter *for* missing values, usage `df[df['Col'].isna()]`.
-   **Assignment Warning:** If you try to modify your filtered data: `df[mask]['A'] = 10`, you might get a `SettingWithCopyWarning`. This is because Pandas isn't sure if you want to change the *original* df or just the *copy* you just made.


---

# Filter with Multiple Conditions

## 1. Why Complex Logic?
Real questions are rarely simple. We don't just ask "Who is rich?".
We ask "Who is rich AND lives in NY OR has a VIP status, but is NOT an employee?".
Complex logic allows us to refine our cohorts to extreme precision.

## 2. Analogy: Venn Diagrams
-   **AND (`&`):** The Intersection. You must be in the overlap of Circle A and Circle B. It is **Strict** (Excludes more people).
-   **OR (`|`):** The Union. You can be in Circle A, Circle B, or both. It is **Inclusive** (Includes more people).
-   **NOT (`~`):** The Inverse. Everything *outside* the circle.


![Combining Multiple Filter Conditions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-13-multi-condition.svg)

## 3. Key Concepts
-   **Bitwise Operators:** Pandas uses `&`, `|`, `~`.
    -   *Why?* Because Python's `and`/`or` keywords only work on single booleans (`True and False`). They panic when they see a Series of booleans.
-   **Parentheses:** You **MUST** wrap conditions in parentheses `(A) & (B)`.
    -   *Why?* Because in Python, `&` has higher precedence than `>`. Without parens, `df['A'] > 5 & df['B'] < 10` is read as `5 & df['B']`, which is nonsense.

## 4. Code Examples

### 1. The AND Condition
*Find Items that are Expensive AND In Stock.*
```python
mask = (df['Price'] > 100) & (df['InStock'] == True)
premium_items = df[mask]
```

### 2. The OR Condition
*Find Customers from NY OR NJ.*
```python
mask = (df['State'] == 'NY') | (df['State'] == 'NJ')
local_customers = df[mask]
```

### 3. The `.isin()` Shortcut
Writing multiple ORs is tedious (`State == 'NY' | State == 'NJ' | State == 'CT'`).
`.isin()` is cleaner and faster.
```python
states_of_interest = ['NY', 'NJ', 'CT']
local_customers = df[df['State'].isin(states_of_interest)]
```

## 5. Under the Hood: No Short-Circuiting
In standard Python `if A and B:`, if A is False, Python stops checking B (Short-circuiting).
In Pandas `(A) & (B)`, there is **No Short-Circuiting**.
-   Pandas evaluates Condition A for *all* rows.
-   Pandas evaluates Condition B for *all* rows.
-   Then it combines them.
-   *Implication:* You cannot use logic like `(x != 0) & (1/x > 5)` to prevent division by zero errors, because `1/x` will be calculated for *everyone* index first, causing a crash before the check happens.

## 6. Common Pitfalls
-   **Using `and`/`or`:** `ValueError: The truth value of a Series is ambiguous`. This error ALWAYS means you used the wrong keyword. Switch to `&`/`|`.
-   **Forgetting Parentheses:** `df['A'] > 5 & df['B'] < 5`. This usually results in a generic `TypeError` or random wrong results.
-   **Chaining too much:** If you have 5 conditions, your code becomes unreadable. Break it down into intermediate masks.


---

# Sort DataFrame by Values

## 1. Why Sort by Values?
Data analysis often begins with ranking. Whether it's finding the most profitable region or the oldest customer, `sort_values()` is the primary tool for re-ordering the physical rows of your DataFrame based on the data they contain.

## 2. Analogy: The Warehouse Manager
- **The Mapper (`by`)**: Choosing which column dictates the order.
- **The Flow (`ascending`)**: Deciding if the data should "Climb up" (Low to High) or "Fall down" (High to Low).
- **The Rulebook (`inplace=False`)**: In modern Pandas, we don't change the "Labels on the shelf" directly; we create a new, perfectly organized list and replace the old one.


![Sorting by Column Values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-21-sort-values.png)

## 3. Key Concepts
- **`.sort_values(by='Col')`**: Sorts by a single column.
- **`.sort_values(by=['Col1', 'Col2'])`**: Sorts by multiple columns. 'Col2' acts as the "Tie-breaker" for duplicates in 'Col1'.
- **`ascending=[True, False]`**: You can provide a list of Booleans to specify a different direction for each column in a multi-sort.
- **`inplace=False`**: Modern best practice is to assign the result back (`df = df.sort_values(...)`). This is safer for data integrity.

## 4. Under the Hood: Timsort
What happens when Pandas re-orders 1 million rows?
1.  **The Engine**: Pandas uses **Timsort**, a highly efficient and stable sorting algorithm (hybrid of Merge and Insertion Sort).
2.  **Stability**: Timsort is stable, meaning that if two rows have the same value, their relative original order is preserved.
3.  **The Index Trade-off**: When you sort by values, your **Index labels** (0, 1, 2...) move along with the rows. This results in a "Scrambled Index" (e.g., 5, 2, 0). 
    - *Industry Tip*: Analysts often follow a sort with `.reset_index(drop=True)` to restack the row labels numerically.

## 5. Detailed Examples

### 1. Single Column Sort
```python
import pandas as pd
df = pd.DataFrame({'City': ['NYC', 'London', 'Tokyo'], 'Sales': [500, 800, 300]})

# Most sales first (Descending)
df = df.sort_values(by='Sales', ascending=False)
```

### 2. Multi-Level Sorting (Tie-Breaker)
*Scenario: Sort by 'Department', and within each department, sort by 'Salary' (Highest first).*
```python
# Dept (A-Z), Salary (High-Low)
df = df.sort_values(by=['Department', 'Salary'], ascending=[True, False])
```

### 3. Handling Nulls
By default, `NaN` (Missing Data) is put at the **bottom** of the sort, regardless of direction. 
```python
# To put missing values at the top
df = df.sort_values(by='Score', na_position='first')
```

## 6. Common Pitfalls
- **The "Lost" Operation**: Running `df.sort_values(...)` without re-assigning it to `df`. The original table remains unsorted.
- **Sorting Strings as Numbers**: Ensure columns are the correct type. Sorting a column of strings `['10', '2']` will put `'10'` before `'2'`.
- **Case Sensitivity**: By default, strings are sorted ASCII-style (`A-Z` before `a-z`).


---

# Handle Missing Data with isna and notna

## 1. Why Identify Missing Data?
Missing data is invisible. You can't "see" a null value in a 1-million-row CSV easily. 
If 10% of your price data is missing, any total revenue calculation will be 10% wrong. We use `isna()` and `notna()` to bring these "invisible gaps" to light.

## 2. Analogy: The Crime Scene Detective
- **The Floorplan**: The DataFrame structure.
- **`isna()`**: Looking for the "holes" (Missing furniture).
- **`notna()`**: Looking for the "evidence" (Furniture present).


![Detecting Missing Values with .isna()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-18-isna-flow.png)

## 3. Key Concepts
- **`NaN`**: Stands for "Not a Number". It's the standard missing data marker in Pandas.
- **`df.isna()`**: Returns a DataFrame of Booleans (`True` where data is missing). **Note**: `.isnull()` is an exact alias; you will see both in the industry.
- **`df.notna()`**: The opposite; returns `True` where data exists.
- **`isna().sum()`**: The standard way to count nulls per column.

## 4. Under the Hood: The IEEE 754 Mystery
Why do we have a special function like `isna()`? Why can't we just write `df['col'] == np.nan`?
1.  **Identity Crisis**: In the computer's logic (IEEE 754 standard), `NaN` is not equal to anything, including itself. 
    ```python
    import numpy as np
    print(np.nan == np.nan) # Output: False
    ```
2.  **Special Logic**: Because `NaN` refuses to identify itself using `==`, Pandas provides `isna()` to scan the memory patterns and identify the "null" state directly.
3.  **Floating Point**: In Pandas, `NaN` is technically a **Float**. This is why if you add a `NaN` to a column of Integers, the whole column "upcasts" to Floats.

## 5. Detailed Examples

### 1. Finding the Holes
```python
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3]})

# This returns a Boolean mask
mask = df['A'].isna()
print(df[mask]) # Shows only the missing rows
```

### 2. Counting the Damage
```python
# Returns a summary of nulls per column
print(df.isna().sum())
```

## 6. Common Pitfalls
- **The "Equal to NaN" Trap**: Writing `if x == np.nan` will always return False. Always use `pd.isna(x)`.
- **String "NaN"**: Sometimes data comes in with the literal String `"NaN"` or `"NULL"`. Pandas might not recognize these as actual missing values. You must replace them with `np.nan` first.
- **Mixed Data Types**: Adding a `NaN` to a Boolean column will convert it to an Object (True/False/None), which makes calculations slower.


---

# Fill Missing Values with fillna

## 1. Why Fill?
Dropping data is easy, but it's expensive—you lose all the other valuable information in that row. 
Filling (Imputation) allows us to maintain the size of our dataset while mitigating the impact of missing values. It's about maintaining **Statistical Continuity**.

## 2. Analogy: The Restoration Artist
- **Constant Value**: Patching with a single color.
- **`ffill` (Forward Fill)**: Patching based on the "Previous" known state (The Neighbor to the left/above).
- **`bfill` (Backward Fill)**: Patching based on the "Next" known state (The Neighbor to the right/below).


![Choosing a fillna() Strategy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-19-fillna-strategy.png)

## 3. Key Concepts
- **`.fillna(x)`**: Replaces all `NaN` with the value `x`.
- **Method-based Filling**:
    - `.ffill()` (Forward Fill): Recommended for **Time Series** data (Assume today is like yesterday).
    - `.bfill()` (Backward Fill): Using future information to fill the past.
    - *Note: Older code used `df.fillna(method='ffill')`, but modern Pandas 2.1+ prefers the direct `.ffill()` method.*
- **`inplace=True`**: Like renaming, `fillna()` returns a copy by default. Use `inplace` or assignment to save.

## 4. Under the Hood: Memory Pointers
What happens in memory during a `.fillna(0)`?
1.  **Scanning**: Pandas identifies the memory addresses of the `NaN` objects.
2.  **Replacement**: Because `NaN` is a specific float object, Pandas simply updates the "pointer" in that row's memory slot to look at the integer `0` instead.
3.  **No Structural Change**: Unlike dropping rows, filling doesn't require Pandas to rewrite the entire index or shift data around. This makes `fillna()` very computationally cheap for large datasets.

## 5. Detailed Examples

### 1. Filling with a Constant
```python
import pandas as pd
df = pd.DataFrame({'Score': [90, None, 85]})
df['Score'] = df['Score'].fillna(0) # Replaces None with 0
```

### 2. Time-Series Forward Fill
```python
prices = pd.Series([10.5, None, None, 11.0])
# Modern practice: Use df.ffill() instead of fillna(method='ffill')
prices = prices.ffill()
```

### 3. Smart Filling (Mean)
```python
avg = df['Age'].mean()
df['Age'] = df['Age'].fillna(avg)
```

## 6. Common Pitfalls
- **The Zero Trap**: Filling missing 'Salary' with `0` will crash your "Average Salary" calculation. Filling with the **Mean** is usually safer.
- **Filling Strings with Numbers**: In a column of Names, filling a `NaN` with `0` will turn the whole column into a "Mixed Object" type, making it slow. Use `"Unknown"` instead.
- **Chained Assignment**: `df['col'].fillna(0, inplace=True)` often works but can sometimes trigger a `SettingWithCopyWarning`. Assignment (`df['col'] = ...`) is always safer.


---

# Drop Missing Values with dropna

## 1. Why Drop?
In data science, "Dirty Data" is worse than "No Data". 
If you include rows with missing values in a complex machine learning model, the model might learn wrong patterns. Dropping is the most conservative and safest way to ensure your analysis is based on **Facts**, not guesses.

## 2. Analogy: The Quality Control Bouncer
- **`how='any'`**: Zero tolerance for missing data.
- **`how='all'`**: Deleting only the "Ghost" rows (entirely empty).
- **`subset`**: Protecting the critical columns (The "VIP" data).


![Removing Missing Values with .dropna()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-20-dropna-strategy.png)

## 3. Key Concepts
- **`df.dropna()`**: The primary tool for removal.
- **`axis`**: Usually `0` (Rows), but can be `1` (Columns) if a specific feature is too messy to keep.
- **`subset=['Col1', 'Col2']`**: Tells the bouncer exactly which columns to check before deciding to drop a row.
- **`thresh=n`**: A more advanced bouncer. "Keep the row if it has at least `n` non-null values."

## 4. Under the Hood: Garbage Collection
What happens when you drop 50% of your rows?
1.  **Index Fragmentation**: The original indices stay. If you had 0, 1, 2, 3 and you drop 1, the DataFrame now goes 0, 2, 3. 
2.  **Memory Release**: Pandas doesn't immediately "shrink" the physical memory used by the DataFrame in some cases, but it marks those rows as "Available" for Python's **Garbage Collector**.
3.  **The Pointer Shift**: A new internal map is created that skips the dropped rows. This is why dropping many rows can actually speed up future calculations—the computer has less to skip over.

## 5. Detailed Examples

### 1. The Default Drop (Any)
```python
import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, None]})
df.dropna(inplace=True) # Bob is gone because Age is missing
```

### 2. Dropping Messy Columns
```python
# If the 'Middle_Name' column is 90% null, drop the whole column
df.dropna(axis=1, inplace=True)
```

### 3. Using Subset (The VIP Filter)
```python
# Keep Bob even if Age is missing, as long as Name exists
df.dropna(subset=['Name'], inplace=True)
```

## 6. Common Pitfalls
- **The "Over-Cleaning" Disaster**: Running `df.dropna()` without arguments on a large dataset often deletes way more data than you intended. Always check the shape `df.shape` before and after.
- **Ignoring Axis**: Forgetting that `dropna()` defaults to rows (`axis=0`). If you wanted to drop a column, you must be explicit.
- **The Index Gap**: After dropping, your row numbers will have gaps (0, 2, 5). Use `.reset_index(drop=True)` to re-order the boxes on the shelf.


---

