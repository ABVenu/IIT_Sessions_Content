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

# Create Series from Different Data Structures

## 1. Why Multiple Inputs?
Data is messy. It comes in JSON (Dicts), CSVs (Lists), or constants (Scalars). The Series constructor `pd.Series()` acts as a **Universal Adapter**. It standardizes all these inputs into one common format (Index + Values), so that downstream analysis doesn't care where the data came from.

## 2. Analogy: The Cookie Cutter
-   **Scalar Creation:** Imagine a **Cookie Cutter**. You have one shape (the value `5`), and you stamp it out 10 times (the index). Result: 10 identical cookies. This is "Broadcasting".
-   **Dictionary Creation:** Imagine a **Pre-Assorted Chocolate Box**. The box has labeled slots ("Caramel", "Nut"). The input data has labeled chocolates. Pandas just drops the "Caramel" chocolate into the "Caramel" slot. If a slot is missing a chocolate, it remains empty (NaN).


![Creating a Series from Different Structures](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-2-series-from-structures.webp)

## 3. Key Concepts
-   **Dict $\rightarrow$ Series:** Keys become Index. Values become Data. This is the most natural mapping.
-   **Scalar $\rightarrow$ Series:** Value is **broadcasted** (repeated) to fill the length of the index. Efficient because it doesn't duplicate memory until modified.
-   **Array $\rightarrow$ Series:** Direct, "Zero-Copy" conversion where possible.

## 4. Code Examples

### Scenario A: The JSON Data (Dictionary)
*Context: You receive a API response with user settings.*
```python
user_settings = {'Theme': 'Dark', 'Notifs': True, 'Volume': 80}
s = pd.Series(user_settings)
# Theme     Dark
# Notifs    True
# Volume    80
```

### Scenario B: The Default Value (Scalar)
*Context: You need to initialize a scoreboard for 5 players with 0 points.*
```python
players = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
scores = pd.Series(0, index=players)
# Alice      0
# Bob        0
# ...
```

### Scenario C: The Index Override (Dict + Index)
*Context: You have data for 3 cities, but you want to report on 4 specific cities.*
```python
data = {'NY': 8.4, 'LA': 3.9, 'Chicago': 2.7}
cities_to_report = ['NY', 'Chicago', 'SF'] # SF is new

s = pd.Series(data, index=cities_to_report)
# NY         8.4
# Chicago    2.7
# SF         NaN  <-- Note this!
```

## 5. Under the Hood: Zero-Copy & Broadcasting
Pandas is smart about memory.
1.  **Broadcasting (Scalars):** When you create `pd.Series(0, index=[...1000 items...])`, Pandas does *not* create 1000 integers in memory immediately. It uses a "stride" trick to repeat the value virtualy. This makes initialization instant.
2.  **Zero-Copy (Arrays):** When you create a Series from a **NumPy Array**, Pandas tries to reference the *existing* array memory instead of copying it.
    -   **Benefit:** Instant creation, even for 10 million rows.
    -   **Risk:** If you modify the original NumPy array, the Pandas Series *also changes*.

## 6. Common Pitfalls: The "NaN" Surprise
When creating a Series from a Dictionary *and* providing an explicit `index`:
-   **Pitfall:** Users assume Pandas will just append the dictionary data.
-   **Reality:** Pandas uses the `index` as the **source of truth**. It looks for those specific keys in the dictionary.
-   **The Trap:** If a key in your `index` doesn't exist in the `dict`, Pandas inserts `NaN` (Not a Number/Missing). It does *not* throw an error! This "silent failure" can lead to bugs if you aren't checking for nulls.
-   **Fix:** Always check `s.isnull().sum()` after creation if you suspect mismatch.


---

# Access Series Elements by Index

## 1. Why Indexes Matter?
In data analysis, we rarely want "the 3rd item". We want "The Revenue for January". Pandas indexes let us speak the language of the data (Business Logic) rather than the language of the computer (Memory Address).
Using labels makes code **readable** and **robust**. `s['GDP']` is self-explanatory; `s[4]` is a mystery number.

## 2. Analogy: The Library System
-   **Positional Access (`iloc`):** "Go to the 3rd Shelf, 5th Book". You need to know the physical layout. If the librarian moves the books, your instruction fails.
-   **Label Access (`loc`):** "Find *Harry Potter*". You rely on the unique identifier. The system finds the location for you. This is resilient to reordering.


![Series Access Methods](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-3-series-access.png)

## 3. Key Concepts
-   **`[]` Operator:** The "Smart" operator. Use it for quick access, but beware—it guesses whether you mean label or position.
-   **`.loc[]`:** The "Explicit" operator. ALWAYS looks for **Labels**. Supports inclusive slicing (`A:C` includes `C`).
-   **`.iloc[]`:** The "Integer" operator. ALWAYS looks for **Positions** (0, 1, 2...). Supports exclusive slicing (`0:2` excludes `2`).

## 4. Detailed Examples

### 1. Label Access (Business Logic)
```python
# Stock Prices
s = pd.Series([150, 2800, 300], index=['AAPL', 'GOOG', 'MSFT'])

print(s.loc['GOOG'])        # 2800 (Single)
print(s.loc['AAPL':'GOOG']) # Returns Series (Slice includes GOOG!)
```

### 2. Positional Access (Algo Logic)
```python
# Get the top 2 stocks, whatever they are
print(s.iloc[0:2])          # Returns first 2 items (Exclusive of index 2)
print(s.iloc[-1])           # Returns the last item (300)
```

### 3. Safe Access (The `.get` method)
Just like Python dictionaries, `[]` raises an error if a key is missing.
```python
# s['TSLA'] -> KeyError
print(s.get('TSLA', 0))     # Returns 0 if TSLA is missing
```

## 5. Under the Hood: Optimization
Pandas indexes are backed by **Hash Tables** (for Objects/Strings) or **Trees** (for Datetime/Ranges).
-   Searching a list of 1 million items by value takes time proportional to the list size (`O(N)`). You have to check every item.
-   Searching a Pandas index by label takes almost zero time (`O(1)`) because it calculates the memory address directly using the hash of the label. *This is why we set indexes!*

## 6. Common Pitfalls: The Integer Index Trap
The most confusing part of Pandas for beginners is when the Index *is* integers.
**Scenario:** You have a Series with an index `[10, 20, 30]`.
```python
s = pd.Series(['A', 'B', 'C'], index=[10, 20, 30])
```
-   `s[10]`: Pandas thinks, "10 is in the index". Returns 'A'.
-   `s.iloc[0]`: Pandas thinks, "Position 0". Returns 'A'.
-   `s.iloc[10]`: Pandas thinks, "Position 10". **Error!** (There are only 3 items).

**Best Practice:** Stop using the `[]` operator for production code. Always use `.loc` (for labels) or `.iloc` (for position) to make your intent explicit to both Pandas and your future self.


---

# Perform Vectorized Operations on Series

## 1. Why Vectorization?
Loops are slow. In Big Data, iterating through 1 million rows one-by-one takes forever. **Vectorization** does it all at once.
It treats the entire array as a single object. Instead of saying "Add 1 to row 1, then Add 1 to row 2...", you say "Add 1 to the Column". This leverages CPU optimizations (SIMD) to process data in parallel chunks.

## 2. Analogy: The Payroll Department
-   **Looped Approach (Python Lists):** The manager calls every employee into the office one by one to hand them a bonus check. It takes all day. (Slow, Serial).
-   **Vectorized Approach (Pandas):** The manager hits one button, and a direct deposit is sent to **everyone's** bank account simultaneously. The result is the same, but it happened instantly. (Fast, Parallel-like).


![Loop vs Vectorized Operations](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-4-vectorized-flow.svg)

## 3. Key Concepts
-   **Element-wise Ops:** Basic math (`+`, `-`, `*`, `/`) is applied to every item independently.
-   **Broadcasting:** If you add a scalar (`s + 10`) to a Series, that 10 is "broadcast" (stretched) to fit the Series shape.
-   **Index Alignment:** The "Killer Feature". When working with two Series, Pandas automatically matches them by **Label**, not by position.

## 4. Detailed Examples

### 1. Scalar Operations (Broadcasting)
*Context: Converting Prices from USD to EUR.*
```python
prices_usd = pd.Series([10, 20, 30])
exchange_rate = 0.85

prices_eur = prices_usd * exchange_rate
# [8.5, 17.0, 25.5] - Happens instantly for 1M rows.
```

### 2. Series Alignment (The Magic)
*Context: Calculating Revenue (Price * Quantity) where order differs.*
```python
prices = pd.Series({'Apple': 2.0, 'Banana': 1.0})
quantities = pd.Series({'Banana': 50, 'Apple': 100}) # Note mixed order!

revenue = prices * quantities
# Apple     200.0  (Matches Apple-Apple)
# Banana    50.0   (Matches Banana-Banana)
# Result is sorted by index automatically.
```

## 5. Under the Hood: SIMD (Single Instruction, Multiple Data)
How is Vectorization so fast? It relies on hardware-level optimization called **SIMD**.
-   **Scalar (Loop):** The CPU loads one number, adds 1, saves it. Repeats 4 times.
-   **Vector (SIMD):** The CPU loads **four** numbers into a special "wide" register. It issues a single "ADD" command. All four numbers are added to 1 simultaneously.
-   *Result:* Math happens 4x to 8x faster purely due to CPU architecture, before even considering Python overhead.

## 6. Common Pitfalls: NaN Propagation
What happens if the indices don't match perfectly during an operation?
-   **Scenario:** Series A has keys `['X', 'Y']`. Series B has keys `['Y', 'Z']`.
-   **Operation:** `A + B`
-   **Result:**
    -   `Y`: Matches. Value is `A['Y'] + B['Y']`.
    -   `X`: Exists in A, not B. Result is `NaN` (Missing).
    -   `Z`: Exists in B, not A. Result is `NaN` (Missing).
-   **Takeaway:** Pandas assumes that if a value is missing, the result of any math on it is unknown (`NaN`).
-   **The Fix:** Use the method version `.add(B, fill_value=0)` if you want to treat missing keys as zero.


---

# Create DataFrame from Dictionary

## 1. Why DataFrames?
Series are 1D arrays (Lists on steroids). DataFrames are 2D tables (Excel Sheets on steroids).
Most real-world data is tabular (Rows & Cols). DataFrames allow us to group related Series together (e.g., a "Name" Series, an "Age" Series, and a "Salary" Series) into a single cohesion object where they share an Index.

## 2. Analogy: The Spreadsheet
-   **Column-Oriented (Dict of Lists):** You fill out the "Names" column top-to-bottom. Then you fill out the "Ages" column. This is how Pandas thinks naturally (Series tied together).
-   **Row-Oriented (List of Dicts):** You fill out one "Form" per person. (Name: Alice, Age: 25). Then you grab the next form. Pandas can stack these forms into a table.


![Creating a DataFrame from a Dictionary](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-5-dataframe-anatomy.png)

## 3. Key Concepts
-   **Dict Keys** → **Column Headers**. (Unless you use `orient='index'`).
-   **Dict Values** → **Column Data**.
-   **Homogeneity:** A single *column* usually has one data type (e.g., all Integers).
-   **Heterogeneity:** Different *columns* can have different types (Name=String, Age=Int). This is the main difference between a DataFrame and a 2D NumPy Matrix (which must be all one type).

## 4. Syntax & Examples

### Method A: Dict of Lists (Standard)
*Best for: Hardcoded data, testing.*
```python
data = {
    'Student': ['Alice', 'Bob'],
    'Score': [85, 90]
}
df = pd.DataFrame(data)
#   Student  Score
# 0   Alice     85
# 1     Bob     90
```

### Method B: List of Dicts (JSON-style)
*Best for: Ingesting API responses or row-by-row logs.*
```python
log_data = [
    {'Timestamp': '10:00', 'Event': 'Login'},
    {'Timestamp': '10:05', 'Event': 'Logout'}
]
df = pd.DataFrame(log_data)
```

## 5. Under the Hood: Columnar Storage
Pandas stores DataFrames in **Columnar Layout**.
-   It doesn't store Row 1, then Row 2.
-   It stores Column A (as a continuous array), then Column B (as a continuous array).
-   **Why?** Analytical queries usually ask "What is the average Score?" (scanning one column). Columnar storage makes this incredibly fast because the CPU can pre-fetch just that column's memory into its cache, minimizing slow RAM access.

## 6. Common Pitfalls & Best Practices
-   **Pitfall: Unequal Lists**
    -   If you use Method A (Dict of Lists), all lists *must* be the same length.
    -   `{'A': [1, 2], 'B': [1]}` → **ValueError: arrays must all be same length**.
-   **Best Practice: Missing Data**
    -   If you use Method B (List of Dicts), keys can be missing.
    -   `[{'A': 1}, {'B': 2}]` → Pandas automatically fills the gaps with `NaN`.
    -   Use Method B if your data is "ragged" or inconsistent.


---

# Create DataFrame from Lists and Arrays

## 1. Why Lists/Arrays?
Sometimes we don't have nice dictionaries with keys. We have "raw" data matrices (like from a sensor, image pixels, or an old C++ database). 
Pandas allows us to ingest this raw, unlabeled data and *assign* meaning (column names) to it during creation. This is the bridge between the "Mathematical World" (Matrices) and the "Business World" (DataFrames).

## 2. Analogy: The Seating Chart
-   **List of Lists:** Imagine a classroom seating chart. You have Row 1 (Students A, B), Row 2 (Students C, D). You hand this list to the teacher.
-   **Missing Labels:** The list doesn't say "Name" or "Grade". It's just positions. You have to attach a separate sticky note (`columns=['Name', 'Grade']`) so the teacher knows how to interpret the data.


![DataFrame from Lists and Arrays](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-6-df-from-lists.png)

## 3. Key Concepts
-   **List of Lists:** Treated as a sequence of **Rows**. (Top-down construction).
-   **NumPy Array:** Treated as a matrix. Very fast conversion because Pandas just wraps the array without copying data (if types match).
-   **Column Mapping:** Unlike dicts, lists don't carry names. You must map them by position (Column 0 = 'Date', Column 1 = 'Price').

## 4. Code Examples

### Scenario A: The Raw Matrix (List of Lists)
*Context: You scraped a simple HTML table row by row.*
```python
raw_data = [
    ['2024-01-01', 100],
    ['2024-01-02', 110]
]
# We MUST supply columns, otherwise they default to 0, 1
df = pd.DataFrame(raw_data, columns=['Date', 'Sales'])
```

### Scenario B: The Scientific Data (NumPy)
*Context: You ran a simulation in NumPy and crave Pandas analysis tools.*
```python
import numpy as np
arr = np.random.rand(5, 3) # 5x3 Matrix of random numbers
df = pd.DataFrame(arr, columns=['Sens_1', 'Sens_2', 'Sens_3'])
```

## 5. Under the Hood: Type Inference & Upcasting
When you pass a List of Lists (Python Objects), Pandas has to guess the data type.
-   **Scanning:** It scans the values. `['Alice', 25]` looks like `[String, Integer]`.
-   **Upcasting Risk:** If Column 2 has `[1, 2, 3.5]`, Pandas sees the float `3.5` and forced the *entire column* to become Float (`1.0, 2.0, 3.5`).
-   **Object Fallback:** If Column 3 has `[10, 'Error']`, the entire column becomes `object` (String). This kills performance.
-   **Performance:** Creating from Lists is slower than NumPy arrays because Pandas has to inspect every single item.

## 6. Common Pitfalls & Best Practices
-   **Pitfall: Jagged Lists**
    -   If Row 1 has 2 items, and Row 2 has 3 items:
    -   Pandas will technically accept this but will fill the missing spots with `None`/`NaN`.
    -   However, it usually indicates a data quality issue source-side.
-   **Best Practice: Explicit Columns**
    -   Always provides the `columns` argument.
    -   If you don't, you get columns `0, 1, 2`. This is called "RangeIndex" and makes code unreadable (`df[0]` vs `df['Sales']`).


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

# Add New Columns to DataFrame

## 1. Why Add Columns?
Raw data is just the starting point. The value of analysis is often **Derived Features**:
-   Calculating "Profit" from "Revenue - Cost".
-   Parsing "Year" from "Date".
-   Categorizing "Age" into "Age Buckets".
Feature Engineering is where data science actually hits the data.

## 2. Analogy: Warehouse Labeling
-   **Scalar Assignment:** The manager walks down the aisle and slaps a "Fragile" sticker on **every** box. (`df['Status'] = 'Fragile'`). It applies to everything equally.
-   **Vector Assignment:** The manager calculates the Total Weight for each shipment by adding the Item Weight (on Box A) to the Padding Weight (on Box B) and writes it on a new label. (`df['Total'] = df['Item'] + df['Pad']`). The calculation is specific to each box (row).


![Adding a New Column](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-14-add-column.jpg)

## 3. Key Concepts
-   **Assignment:** `df['New_Col'] = Value`.
-   **Vectorization:** Math operations (`+`, `-`, `*`) on columns happen row-by-row automatically.
-   **Broadcasting:** Assigning a single number fills the whole column.

## 4. Code Examples

## Sample Dataset
```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['Widget A', 'Widget B', 'Gadget X', 'Gadget Y', 'Accessory Z'],
    'Price':   [120.00, 95.50, 340.00, 275.00, 45.00],
    'Tax':     [12.00,   9.55,  34.00,  27.50,   4.50],
    'Sales':   [1200,    850,   1500,    430,    2200],
})
```

### 1. Constant Value (Initialization)
```python
# Set a default status for everyone
df['Is_Active'] = True
```

### 2. Math Operation (Derived Feature)
```python
# Calculate Total Price (Price + Tax)
df['Total'] = df['Price'] + df['Tax']
```

### 3. Boolean Flag
```python
# Create a True/False column for filtering later
df['High_Value'] = df['Sales'] > 1000
```

### 4. Copying a Column
```python
# Keep a backup before modifying
df['Sales_Original'] = df['Sales']
```

## 5. Under the Hood: Memory Layout
When you add a new column `df['New'] = ...`, Pandas allocates a new block of memory for that array and adds a "pointer" in the DataFrame's Column Manager.
-   **Cheap Operation:** Adding a column is generally efficient ($O(1)$) because existing columns don't need to be moved.
-   **Expensive Operation:** Inserting a column *in the middle* (`df.insert()`) is slower because it might require shifting internal references.
-   **Broadcasting:** When you assign `df['A'] = 0`, Pandas doesn't create a list of a million zeros in Python. It uses NumPy's broadcasting to virtually project the value across the array, saving massive memory.

## 6. Common Pitfalls: The `SettingWithCopyWarning`
This is the most famous warning in Pandas.
**Scenario:**
```python
subset = df[df['Age'] > 50]  # subset is a VIEW or COPY (Pandas decides)
subset['Status'] = 'Senior'  # Warning!
```
**Why?** Pandas says: "Hey, `subset` might be a temporary copy. You are modifying this copy, but maybe you thought you were modifying the original `df`? I'm warning you that your change might be lost."
**Fix:** Explicitly copy if you want a separate object: `subset = df[...].copy()`.


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

# Delete Columns and Rows

## 1. Why Delete?
Data cleaning is subtraction. We remove:
-   **Irrelevant Features:** Columns like "Internal_DB_ID" that add noise.
-   **Bad Data:** Rows with nulls or duplicates.
-   **Privacy Risks:** Columns like "SSN" or "Password".
Making the dataset smaller makes all subsequent analysis faster and cleaner.

## 2. Analogy: Editing a Document
-   **`df.drop()` (Default):** Like "Save As...". You create a *new* copy of the document with the paragraph deleted. The original file is safe on your hard drive. This is safer but uses more memory temporarily.
-   **`inplace=True`:** Like hitting "Delete" then "Save". The original file is changed forever. Use this if you are sure and want to save memory.


![Deleting Rows and Columns with .drop()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-15-drop-axis.png)

## 3. Key Concepts
-   **`.drop()`:** The universal deleter.
-   **Axis:** You must specify what to drop.
    -   `axis=0` or `index=...` for Rows.
    -   `axis=1` or `columns=...` for Columns.
-   **Immutability:** By default, Pandas returns a new object. It does not touch the original.

## 4. Code Examples

## Sample Dataset
```python
import pandas as pd

df = pd.DataFrame({
    'Name':     ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Salary':   [55000, 82000, 91000, 78000, 61000],
    'Notes':    ['On leave', None, 'Remote', None, 'Part-time'],
    'Temp_ID':  ['T01', 'T02', 'T03', 'T04', 'T05'],
    'Metadata': ['v1', 'v1', 'v2', 'v2', 'v3'],
}, index=['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5'])
```

### 1. Dropping Columns
```python
# Drop 'Notes' column.
# Result is assigned to a NEW variable (or overwrites the old one)
df_clean = df.drop(columns=['Notes'])
```

### 2. Dropping Rows (by Label)
```python
# Drop the row with label 'Row_5'
df_clean = df.drop(index=['Row_5'])
```

### 3. Dropping Multiple Items
```python
# Drop multiple columns at once
df_clean = df.drop(columns=['Notes', 'Temp_ID', 'Metadata'])
```

### 4. The `del` keyword (Columns only)
```python
# This is Python's native delete. It works IN PLACE immediately.
del df['Notes'] 
```

## 5. Under the Hood: Garbage Collection
When you run `df = df.drop(...)`, you are creating a new object in memory and assigning the label `df` to it.
-   **What happens to the old object?** It becomes "orphaned" (no variable points to it).
-   **Python's Collector:** Python's Garbage Collector eventually finds this orphan and frees up the RAM.
-   **Inplace:** `inplace=True` modifies the memory block directly. It avoids creating the orphan in the first place, which is crucial when your dataset is 50GB and you don't have enough RAM to copy it.

## 6. Common Pitfalls
-   **The "Silent" Bug:**
    ```python
    df.drop(columns=['A'])  # You didn't assign this to anything!
    print(df)               # 'A' is still there. Result was calculated and thrown away.
    ```
    *Fix:* `df = df.drop(...)`
-   **Axis Confusion:** `df.drop(['A'])` defaults to `axis=0` (Rows). It looks for a Row named 'A'. If 'A' is a column, it errors. ALWAYS use explicit `columns=['A']` to avoid this.


---

# Rename Columns and Index

## 1. Why Rename?
Data follows the "Garbage In, Garbage Out" rule. Most raw data comes with messy, cryptic, or inconsistent headers. 
Renaming converts **Machine Data** (e.g., `temp_k_01`) into **Human Insights** (e.g., `Boiler_Temperature`). It is the first step in making a dataset "Self-Documenting".

## 2. Analogy: Changing the Signage
- **Columns (`axis=1`)**: Renaming columns is like changing the signs above the aisles in a supermarket. You aren't moving the groceries; you are just making it easier for the customers to find them.
- **Index (`axis=0`)**: Renaming the index is like updating the room numbers in a hotel. The rooms (data rows) stay where they are; you are just changing the labels on the doors.


![Renaming Columns and Index Labels](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-16-rename-flow.png)

## 3. Key Concepts
- **`.rename()`**: The primary tool for selective renaming. Uses a dictionary `{'old': 'new'}`.
- **`columns=` vs `index=`**: Explicit arguments to target only the horizontal or vertical labels.
- **`inplace=True` vs Assignment**: By default, `.rename()` returns a **new** DataFrame. While `inplace=True` exists, the industry standard is moving towards explicit assignment (`df = df.rename(...)`) for better code clarity and compatibility with Pandas' new "Copy-on-Write" mode.
- **`.set_axis()`**: The "Power Tool" for replacing the *entire* list of names at once. It's more readable than `df.columns = list` when used in a chain.

## 4. Detailed Examples

### 1. Selective Renaming (Columns)
*Context: We only want to fix the 'Mkt_Val' column.*
```python
import pandas as pd
df = pd.DataFrame({'Mkt_Val': [100], 'Volume': [500]})

# Renaming one column, leaving others alone
df = df.rename(columns={'Mkt_Val': 'Market_Value'})
```

### 2. Selective Renaming (Index)
*Context: Changing numeric IDs to labels.*
```python
df.index = [0, 1]
df = df.rename(index={0: 'A', 1: 'B'})
```

### 3. Mass Renaming (List replacement)
*Context: You know exactly what the 5 columns should be.*
```python
df.columns = ['ID', 'Name', 'Score'] 
# WARNING: This overwrites everything. Length must match exactly.
```

## 5. Under the Hood: The Index Object
What actually happens when you rename?
- **Immutability**: Pandas Index objects are **immutable**. You cannot change `df.columns[0] = 'New'` directly.
- **Pointer Swap**: When you rename, Pandas creates a **new** Index object in memory and updates the DataFrame's "pointer" to look at this new object instead of the old one.
- **Memory Efficiency**: Since the **Values** (the actual data) aren't changing, the operation is very light. You are only replacing the meta-data "labels", not the gigabytes of data.

## 6. Common Pitfalls
- **The "Silent" Rename**:
    ```python
    df.rename(columns={'A': 'B'}) # Calculated but not saved!
    print(df) # column is still 'A'
    ```
    *Fix*: Use `df = df.rename(...)`. Even if you use `inplace=True`, explicit assignment is often considered a "Safe Practice" in modern data engineering.
- **Dictionary Key Mismatch**: If you try to rename `{'Apple': 'Fruit'}` but the column is actually `'apple'` (lowercase), Pandas will do nothing. It won't error; it just won't find a match.
- **Duplicate Names**: Pandas *allows* you to have two columns named 'Total'. This is dangerous and causes logic errors later. Always ensure renamed columns are unique.


---

# Group Data with groupby

## 1. Why Group?
Data is only valuable if it tells a story. Raw data is often too noisy. 
By grouping data, we find patterns across categories. We move from looking at individual "data points" to looking at "segment behavior".

## 2. Analogy: The Laundry Service
The "Split-Apply-Combine" pattern is the industry standard for grouped operations:
- **Split**: Subdividing the data based on a key (e.g., Color).
- **Apply**: Calculating something for each group (e.g., counting items).
- **Combine**: Merging results back into a clean summary table.


![GroupBy: Split-Apply-Combine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-17-groupby-sac.png)

## 3. Key Concepts
- **`df.groupby('Col')`**: Returns a `DataFrameGroupBy` object (The "Lazy" object).
- **Aggregation Functions**: Tools like `.sum()`, `.mean()`, `.count()`, and `.min()/max()`.
- **Selecting Columns**: Using `df.groupby('Col')['Value_Col']` to target specific data. 
- **The `numeric_only` Rule**: In modern Pandas (2.0+), if you calculate a mean or sum on a group with text columns, you **must** specify `numeric_only=True` or Pandas will throw a `TypeError`.

## 4. Under the Hood: The "Lazy" GroupBy
What happens when you run `grouped = df.groupby('City')`?
1.  **No Calculation (Yet)**: Pandas does **not** calculate anything initially. It simply scans the 'City' column and creates a "map" of which rows belong to which city.
2.  **The Metadata Map**: It creates a hash table where the keys are the cities and the values are lists of row numbers (indices).
3.  **Efficiency**: This "Lazy Evaluation" is incredibly fast because Pandas waits until you specify the math (like `.mean()`) before it actually looks at the numeric data.

## 5. Detailed Examples

### 1. Basic Summation
```python
import pandas as pd
data = {'Region': ['North', 'South', 'North', 'South'], 'Sales': [1000, 2000, 1500, 3000]}
df = pd.DataFrame(data)

# Total sales per region
region_totals = df.groupby('Region')['Sales'].sum()
```

### 2. Multi-column Selection
```python
# Multiple metrics for one group (e.g., Sales and Units)
stats = df.groupby('Region')[['Sales', 'Units']].mean()
```

## 6. Common Pitfalls
- **The "Lost" Columns**: When you group by 'Department', any column that isn't the group key OR a numeric value will be dropped by default aggregation (like `.mean()`) because you can't find the "average" of a String.
- **The Forgotten Aggregation**:
    ```python
    res = df.groupby('City') 
    print(res) # Output: <pandas.core.groupby.generic.DataFrameGroupBy object...>
    ```
    *Fix*: Always follow groupby with an action like `.sum()` or `.mean()`.
- **Numeric vs. Non-numeric**: Attempting to `.mean()` on a column of Strings will result in an error or an empty result in newer Pandas versions (Numeric-only rule).


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

# Sort DataFrame by Index

## 1. Why Sort by Index?
In Pandas, the Index is the "Metadata" that uniquely identifies each row. While we often sort by data values (to find top performers), we sort by index to restore logical flow. This is especially critical after operations that drop or reorder rows, or when using a time-series index.

## 2. Analogy: The Filing Cabinet
- **Labels (Index)**: The identifier on the tab of each folder.
- **The Drawer (The DataFrame)**: The container holding the rows.
- **Ordering**: ensure Folder 1 is before Folder 2, or "A" is before "B".


![Sorting by Index](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-22-sort-index.jpg)

## 3. Key Concepts
- **`.sort_index()`**: The primary method to reorder rows based on labels.
- **`axis`**: Defaults to `0` (Rows). You can sort column names alphabetically by setting `axis=1`.
- **`ascending`**: Defaults to `True`. Set to `False` to sort from Z to A or 10 to 1.
- **`inplace=False`**: Consistent with modern Pandas, we usually assign the result back: `df = df.sort_index()`.

## 4. Under the Hood: The Pointer Map
What happens inside the computer when you sort the index?
1.  **Metadata Management**: Unlike `sort_values()`, which has to look at every piece of data, `sort_index()` only looks at the Index object. 
2.  **Pointer Shuffling**: Pandas doesn't necessarily move the data in your RAM; it simply updates an internal "Map" (Index pointers) so that the computer knows the "New first row" is the one labeled 0.
3.  **Efficiency**: Sorting by index is generally faster than sorting by values because the Index is often pre-optimized for lookup and ordering.

## 5. Detailed Examples

### 1. Restoring Numerical Order
```python
import pandas as pd
df = pd.DataFrame({'Sales': [100, 200]}, index=[1, 0])

# Restore to 0, 1 order
df = df.sort_index()
```

### 2. Sorting Columns Alphabetically
*Scenario: Your columns are out of order (e.g., 'Zip', 'Name', 'Age'). Sort them to ('Age', 'Name', 'Zip').*
```python
# Sort headers (axis=1)
df = df.sort_index(axis=1)
```

### 3. Case Sensitivity in Indexes
If your index is strings ('apple', 'Banana'), `sort_index()` will use ASCII order (Capital letters come before lowercase).
```python
df = pd.DataFrame({'Data': [1, 2]}, index=['apple', 'Banana'])
print(df.sort_index()) # 'Banana' will be first!
```

## 6. Common Pitfalls
- **The "Missing" Sort**: Forgetting to assign `df = df.sort_index()`. 
- **Confusing with reset_index**: 
    - `sort_index()`: Reorders rows to match the labels. (Label 2 goes to the bottom).
    - `reset_index()`: Throws away the labels and gives you new ones (0, 1, 2...).
- **Mixed Objects**: Sorting an index that contains both integers and strings will cause an error.


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

