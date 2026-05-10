# Install Pandas

## 1. Why Pandas?
Pandas bridges the gap between simple lists and manual Excel spreadsheets by providing data context, speed (via NumPy), and usability for tables you load, clean, and analyze in Python.

![Anatomy of a Pandas Series](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-1-series-anatomy.webp)

## 2. Installation and import
Install once in your environment (terminal or notebook):

```bash
pip install pandas
```

In code, the usual entry point is:

```python
import pandas as pd
```

You will use `pd` for reading files, selecting rows and columns, and working with missing values in the rest of this session.

# What is CSV?

## 1. What is CSV?
**CSV** stands for **Comma-Separated Values**. It is a **plain text** format: each **line** in the file is one **row** of a table, and **commas** separate **columns** within that row. Often the **first line** holds **column names** (a header row).

## 2. Why is CSV used?
-   **Simple and portable:** Any editor can open it; no proprietary binary format.
-   **Lightweight:** Good for medium-sized tabular exports and logs.
-   **Universal:** Spreadsheets (Excel, Google Sheets), databases, web APIs, and survey tools routinely export or accept CSV.
-   **Easy to version in Git:** Text diffs are readable compared to `.xlsx` binary files.

## 3. How CSV fits into data work
Teams use CSV to **move rectangular data** between systems: save an extract from a database, download survey responses, export from Excel for Python analysis, or share a small dataset with collaborators. In Python, Pandas reads that text into a **DataFrame** so you can filter, aggregate, and plot.

## 4. Format at a glance
Typical layout:

-   **Header row (optional but common):** names for each column, separated by commas.
-   **Data rows:** one record per line; fields separated by commas.
-   **Text with commas:** fields are wrapped in **double quotes** (e.g. `"New York, NY"`).
-   **Other separators:** some files use tabs (**TSV**) or pipes; Pandas can read those with a different `sep=` argument.

**Example file contents** (`people.csv`):

```text
Name,Age,City
Alice,28,Delhi
Bob,35,Mumbai
```

Here there are three columns (`Name`, `Age`, `City`) and two data rows below the header.

## 5. Simple example: create a CSV file in Python
You can create a CSV from scratch to see the format on disk:

```python
# Build the same table as plain text, then write to a file
csv_text = """Name,Age,City
Alice,28,Delhi
Bob,35,Mumbai
"""

with open("people.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)
# Now people.csv exists next to your script; open it in a text editor to verify.
```

After this, `pd.read_csv("people.csv")` (next section) will load that file into a DataFrame.

# Create DataFrame from CSV Files

## 1. Why `pd.read_csv()`?
Now that you know what a CSV file is, `pd.read_csv()` is the standard way to **parse** that text into a **DataFrame**: column names from the header, one row per line, types inferred automatically when possible.

## 2. Analogy: The Universal Translator
`pd.read_csv()` is like a translator that can handle different CSV dialects (separators, headers, date formats).

![Reading a CSV File into a DataFrame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-7-csv-to-dataframe.png)

## 3. Key Concepts
-   **Path:** Can be a local file or a URL.
-   **Separator (`sep`):** Default is comma `,`. Alternatives are Tab (`\t`) or Pipe (`|`).
-   **Header:** Default is row 0. Use `header=None` if no headers.
-   **Index Column:** You can pick a specific column to become the Index.

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
`pd.read_csv()` is fast due to a C-based parser, memory mapping, and type inference.

## 6. Common Pitfalls
-   **Encoding Errors:** Fix `UnicodeDecodeError` with `pd.read_csv(..., encoding='cp1252')`.
-   **ParserTokenError:** Usually means the separator is wrong; check `sep='\t'` or `sep='|'`.

# Understand DataFrame Structure

## 1. Why Structure Matters?
A DataFrame's structure, consisting of Index, Columns, and Values, is critical for accurate data analysis.

## 2. Analogy: The City Map
The DataFrame structure is analogous to a city map, with the Index as street names, Columns as avenue names, and Values as the buildings at the intersections.

![DataFrame Structure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-8-df-structure.png)

## 3. Key Concepts
-   **`.index`**: The Row Labels.
-   **`.columns`**: The Column Headers.
-   **`.values`**: The raw data (NumPy array).
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
The Index is often shared between DataFrames to save RAM.

## 6. Common Pitfalls & Best Practices
-   You cannot modify the Index or Columns directly; replace the entire index instead: `df.index = [5, 1]`.
-   Always check `df.info()` to summarize the DataFrame's structure, dtypes, and memory usage.

# Inspect Data Quickly

## Core Concept: Initial Reconnaissance
Data inspection with `head`, `tail`, `sample`, `shape`, and `info` is the mandatory first step of Exploratory Data Analysis (EDA).

## 1. Visual Inspection
Always visually inspect data after loading to ensure headers are mapped correctly and data integrity is maintained.

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

![Quick DataFrame Inspection Methods](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-61-inspection-map.png)

## 2. Dimensionality with `.shape`
`.shape` provides the number of rows and columns as a tuple.

```python
dimensions = df.shape
print(f"The dataset has {dimensions[0]} rows and {dimensions[1]} columns.")
```

## 3. Deep Dive with `.info()`
`df.info()` summarizes the DataFrame's Index, Columns, Dtypes, and Non-Null counts, crucial for identifying missing data.

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

## Pro-Tip: Memory Usage
To get the exact RAM usage, pass `memory_usage='deep'` to `df.info()`.

```python
df.info(memory_usage='deep')
```

# Select Columns from DataFrame

## 1. Why Select?
Selecting columns filters noise, focuses on relevant data, and optimizes memory usage.

## 2. Analogy: The Jukebox
Selecting a column is like playing a song from a Jukebox.

![Selecting Columns from a DataFrame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-9-select-columns.webp)

## 3. Key Concepts
-   **Bracket `['Col']`**: Returns a **Series**. Use for analysis (math, stats).
-   **Double Bracket `[['Col']]`**: Returns a **DataFrame**. Use for structural operations.
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
Selecting a column usually returns a View, not a Copy, which can lead to unintended side effects.

## 6. Common Pitfalls: The Dot Notation Trap
Dot notation is dangerous due to potential conflicts with method names, inability to handle spaces in column names, and inability to create new columns. Always use brackets for assignment: `df['NewCol'] = 10`.

# Select Rows using loc

## 1. Why `loc`?
`loc` allows data lookup by human-readable labels (index) rather than integer position.

## 2. Analogy: The Music Request
`loc` (Label) is like requesting a song by name, whereas `iloc` (Position) is like requesting a track by number.

![Selecting with .loc[ ]](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-10-loc-flow.png)

## 3. Key Concepts
-   **Label-Based:** Must use exact index labels.
-   **Inclusive Slicing:** `start:stop` includes both start and stop.
-   **KeyError:** Raised if the label is not found.
-   **Syntax:** `df.loc[Row_Label, Column_Label]`

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
Pandas uses Hash Maps for fast label lookups (`O(1)` complexity).

## 6. Common Pitfalls
-   Type mismatch between index and lookup value (KeyError).
-   Slicing an unsorted index might return garbage; sort the index first (`df.sort_index()`).

# Select Rows using iloc

## 1. Why Position?
`iloc` accesses data by integer position (0, 1, 2...), treating the DataFrame like a standard Python list.

## 2. Analogy: Address vs GPS
`iloc` (GPS) relies on absolute physical position, whereas `loc` (Address) relies on assigned names.

![Selecting with .iloc[ ]](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-11-iloc-flow.svg)

## 3. Key Concepts
-   **Integer-Based:** Must use integers (0, 1, 2...).
-   **Exclusive Slicing:** `0:3` returns rows 0, 1, 2 (Stops *before* 3).
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
`iloc` is generally faster than `loc` for single-item access due to direct memory access.

## 6. Common Pitfalls: The Integer Index Trap
When the index consists of integers, be explicit and always use `.iloc` if you mean position.

## 7. Comparison Table
| Feature | `.loc` | `.iloc` |
| :--- | :--- | :--- |
| **Input** | Labels / Strings | Integers |
| **Slicing** | **Inclusive** (Start to End) | **Exclusive** (Start to End-1) |
| **Column Access** | By Name (`'Age'`) | By Position (`3`) |
| **Use Case** | Business Logic | Iteration / Sampling |

# Reset and set index using reset_index() and set_index()

## Core Concept: Shifting Data Hierarchies
Manipulating the index allows you to reorganize data for specific analytical tasks.

## 1. Promoting a Column: `set_index()`
This method extracts a column and establishes it as the new row identifier.

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
*   **Destructive by default**: The original index is completely deleted.
*   **Column Removal**: The promoted column is removed from the list of standard `df.columns`.

![set_index() vs reset_index()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-67-index-reset-set.png)

## 2. Demoting the Index: `reset_index()`
When the current index is no longer optimal, reset it to push those values back into standard columns.

```python
# Assume 'Department' is currently acting as the index
# Demote 'Department' back to a standard column, and insert a fresh 0,1,2 index
flattened_df = df_indexed.reset_index()
```

### Controlling the Demoted Data: `drop=True`
To delete a messy index instead of saving it as a column, use `drop=True`.

```python
# The messy numbers are deleted entirely. The new index is clean (0,1,2...)
clean_filter_df = df_filtered.reset_index(drop=True)
```

# Filter DataFrame using Boolean Conditions

## 1. Why Filter?
Filtering slices data based on content, allowing comparison of segments.

## 2. Analogy: The Nightclub Bouncer
Filtering is like a nightclub bouncer who only lets in people who meet a specific condition.

![Filtering with Boolean Conditions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-12-boolean-filter.png)

## 3. Key Concepts
-   **Boolean Mask:** A Series of `True`/`False` values that has the same length as the DataFrame.
-   **Application:** `df[mask]`.
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
Boolean values are stored efficiently, and applying the mask is a low-level Bitmap operation.

## 6. Troubleshooting & Pitfalls
-   An empty result may indicate a case-sensitive string comparison issue.
-   `NaN` comparisons are tricky; use `df[df['Col'].isna()]` to filter for missing values.

# Filter with Multiple Conditions

## 1. Why Complex Logic?
Complex logic refines cohorts to extreme precision.

## 2. Analogy: Venn Diagrams
AND (`&`): The Intersection. OR (`|`): The Union. NOT (`~`): The Inverse.

![Combining Multiple Filter Conditions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-13-multi-condition.svg)

## 3. Key Concepts
-   **Bitwise Operators:** Pandas uses `&`, `|`, `~`.
-   **Parentheses:** You MUST wrap conditions in parentheses `(A) & (B)`.

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
`.isin()` is cleaner and faster for multiple OR conditions.
```python
states_of_interest = ['NY', 'NJ', 'CT']
local_customers = df[df['State'].isin(states_of_interest)]
```

## 5. Under the Hood: No Short-Circuiting
Pandas evaluates all conditions fully, without short-circuiting.

## 6. Common Pitfalls
-   Using `and`/`or` instead of `&`/`|` results in a `ValueError`.
-   Forgetting parentheses leads to `TypeError` or incorrect results.

# Sort DataFrame by Values

## 1. Why Sort by Values?
`sort_values()` re-orders the physical rows of a DataFrame based on data for ranking.

## 2. Analogy: The Warehouse Manager
The column to sort by is the mapper, the sort direction is the flow, and `inplace=False` creates a new list.

![Sorting by Column Values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-21-sort-values.png)

## 3. Key Concepts
-   **.sort_values(by='Col')**: Sorts by a single column.
-   **.sort_values(by=['Col1', 'Col2'])**: Sorts by multiple columns.
-   **ascending=[True, False]**: Specifies sort direction for each column.
-   **inplace=False**: Assign the result back (`df = df.sort_values(...)`).

## 4. Under the Hood: Timsort
Pandas uses Timsort, a stable sorting algorithm. Sorting shuffles the index labels; analysts often use `.reset_index(drop=True)` afterward.

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
By default, `NaN` is put at the bottom; use `na_position='first'` to put it at the top.

```python
# To put missing values at the top
df = df.sort_values(by='Score', na_position='first')
```

## 6. Common Pitfalls
-   Forgetting to re-assign the sorted DataFrame.
-   Sorting strings as numbers requires ensuring correct data types.

# Handle Missing Data with isna and notna

## 1. Why Identify Missing Data?
Identifying missing data with `isna()` and `notna()` is essential for accurate analysis.

## 2. Analogy: The Crime Scene Detective
`isna()`: Looking for the "holes" (Missing furniture). `notna()`: Looking for the "evidence" (Furniture present).

![Detecting Missing Values with .isna()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-18-isna-flow.png)

## 3. Key Concepts
-   **`NaN`**: Stands for "Not a Number".
-   **`df.isna()`**: Returns a DataFrame of Booleans (`True` where data is missing). `.isnull()` is an alias.
-   **`df.notna()`**: Returns `True` where data exists.
-   **`isna().sum()`**: Counts nulls per column.

## 4. Under the Hood: The IEEE 754 Mystery
`NaN` is not equal to itself; `isna()` scans memory patterns to identify null states.

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
-   `x == np.nan` always returns False; use `pd.isna(x)`.
-   Replace string `"NaN"` or `"NULL"` with `np.nan` before processing.

# Fill Missing Values with fillna

## 1. Why Fill?
Filling (Imputation) maintains the size of the dataset while mitigating the impact of missing values.

## 2. Analogy: The Restoration Artist
Constant Value: Patching with a single color. `ffill` (Forward Fill): Patching based on the "Previous" known state. `bfill` (Backward Fill): Patching based on the "Next" known state.

![Choosing a fillna() Strategy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-19-fillna-strategy.png)

## 3. Key Concepts
-   **.fillna(x)**: Replaces all `NaN` with the value `x`.
-   **Method-based Filling**: `.ffill()` (Forward Fill), `.bfill()` (Backward Fill).
-   **inplace=True**: Use `inplace` or assignment to save changes.

## 4. Under the Hood: Memory Pointers
`fillna()` updates memory pointers to replace `NaN` objects, making it computationally cheap.

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
-   Filling 'Salary' with `0` will skew calculations; the **Mean** is safer.
-   Use `"Unknown"` instead of numbers for string columns.

# Drop Missing Values with dropna

## 1. Why Drop?
Dropping is the safest way to ensure analysis is based on facts.

## 2. Analogy: The Quality Control Bouncer
`how='any'`: Zero tolerance. `how='all'`: Delete only entirely empty rows. `subset`: Protect critical columns.

![Removing Missing Values with .dropna()](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-20-dropna-strategy.png)

## 3. Key Concepts
-   **`df.dropna()`**: The primary tool for removal.
-   **`axis`**: Usually `0` (Rows), but can be `1` (Columns).
-   **`subset=['Col1', 'Col2']`**: Specifies which columns to check.
-   **`thresh=n`**: Keeps rows with at least `n` non-null values.

## 4. Under the Hood: Garbage Collection
Dropping creates index fragmentation and marks rows for garbage collection, potentially speeding up future calculations.

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
-   `df.dropna()` without arguments can delete too much data; check `df.shape` before and after.
-   Forgetting that `dropna()` defaults to rows (`axis=0`).
-   Use `.reset_index(drop=True)` to re-order row numbers after dropping.