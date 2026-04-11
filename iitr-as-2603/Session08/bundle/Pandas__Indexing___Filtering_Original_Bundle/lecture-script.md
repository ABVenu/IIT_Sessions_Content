# Install Pandas and Create Series

## 1. Motivation
Imagine you are tracking daily revenue for a lemonade stand.
If you use a Python List: `revenue = [100, 150, 120]`.
-   **Problem:** If I ask "What was the revenue on Tuesday?", you have to remember that Tuesday is Index 1.
-   **Risk:** If you insert a holiday on Monday, all your index positions shift. The data loses its meaning.
We need a data structure that connects **Data** (150) to **Labels** (Tuesday).

## 2. Overview
**Pandas Series** is a "Labeled List".
-   It looks like a list: `[100, 150, ...]`
-   But it acts like a dictionary: `['Monday', 'Tuesday', ...]`
It gives us the best of both worlds: ordered data that can be accessed by name.

## 3. Live Coding Walkthrough

### Step 1: The Problem with Lists
```python
# Instructor: Let's try to track revenue with lists first.
revenue_list = [100, 150, 120]
days_list = ['Mon', 'Tue', 'Wed']

# Accessing Tuesday's revenue requires knowing the position
print(revenue_list[1])  
# Output: 150 (But we had to count manually!)
```

### Step 2: The Pandas Solution
```python
import pandas as pd

# Instructor: Let's create a Series. It binds the data to the labels.
revenue = pd.Series(data=[100, 150, 120], index=['Mon', 'Tue', 'Wed'])

print(revenue)
# Output:
# Mon    100
# Tue    150
# Wed    120
# dtype: int64
```

### Step 3: The Payoff (Label Access)
```python
# Instructor: Now ask for "Tue" directly. No counting needed.
print(revenue['Tue'])
# Output: 150
```


---

# Create Series from Different Data Structures

## 1. Motivation
In the real world, data comes from different sources:
-   **APIs:** Give us JSON (Dictionaries).
-   **Sensors/IoT:** Give us raw streams of numbers (Arrays).
-   **Forms:** Give us single default values (Scalars).
We need a "Universal Adapter" to turn all these messy inputs into a clean, analytical Pandas Series.

## 2. Overview
The `pd.Series()` constructor is that adapter. It intelligently detects the input type and converts it:
-   **Dict:** Keys becomes Index.
-   **Array:** Automatic 0, 1, 2 Index.
-   **Scalar:** Broadcasts value to all Index spots.

## 3. Live Coding Walkthrough

### Step 1: Ingesting API Data (Dictionary)
*Context: We fetched user settings from a web API.*
```python
import pandas as pd

user_settings = {'Theme': 'Dark', 'Volume': 80, 'Notifications': True}

# Convert dict to Series
s_settings = pd.Series(user_settings)
print(s_settings)
# Output explains: Keys are now the Index.
```

### Step 2: Ingesting Sensor Data (Array)
*Context: A thermometer dumping temperature readings every second.*
```python
import numpy as np
temps = np.array([22.5, 23.0, 22.8])

# Convert array to Series
s_temps = pd.Series(temps)
print(s_temps)
# Note the automatic 0, 1, 2 index.
```

### Step 3: Setting Defaults (Scalar)
*Context: Initializing a scoreboard for 3 new players.*
```python
# We have 3 players, everyone starts at 0
s_scores = pd.Series(0, index=['Alice', 'Bob', 'Charlie'])
print(s_scores)
# Output: Everyone has 0. This is "Broadcasting".
```


---

# Access Series Elements by Index

## 1. Motivation
Retrieving data is the most common task in analysis. 
But "Position" (Index 4) is fragile. If the list is sorted or filtered, "Index 4" changes completely.
"Label" (Index 'Jan') is robust. 'Jan' is always 'Jan', no matter where it sits in the list.

## 2. Overview
Pandas gives us two specialized accessors:
-   **`.iloc` (Integer Location):** Strictly uses position (0, 1, 2). Like a Python list.
-   **`.loc` (Label Location):** Strictly uses names ('A', 'B', 'C'). Like a Dictionary.

## 3. Live Coding Walkthrough

### Step 1: Setup the "Library Catalog"
```python
import pandas as pd
# Index = Book ISBN, Value = Book Title
books = pd.Series(['Harry Potter', 'Lord of the Rings', 'The Hobbit'], 
                  index=['978-1', '978-2', '978-3'])
print(books)
```

### Step 2: Positional Lookup (.iloc)
*Context: "Give me the first book on the shelf."*
```python
print(books.iloc[0])
# Output: 'Harry Potter'. 
# This relies on physical order.
```

### Step 3: Label Lookup (.loc)
*Context: "Give me the book with ISBN 978-2."*
```python
print(books.loc['978-2'])
# Output: 'Lord of the Rings'.
# This works even if we shuffle the shelf!
```

### Step 4: The Slicing Difference
```python
# .iloc is Exclusive (Standard Python)
print(books.iloc[0:2]) # Items 0 and 1 only.

# .loc is INCLUSIVE (Pandas Special)
print(books.loc['978-1':'978-2']) # Includes BOTH start and end.
```


---

# Perform Vectorized Operations on Series

## 1. Motivation
Loops are slow. If you have 1 million prices to convert from USD to EUR, writing a `for` loop in Python will take seconds.
In data science, we need milliseconds.
We want to treat the entire column as a "Vector" and apply math to all of it at once.

## 2. Overview
**Vectorization** is the ability to apply an operation (like `* 0.85`) to a whole array simultaneously.
Pandas also handles **Alignment**: it automatically matches data by Label index, ensuring you don't accidentally subtract "Apple's Price" from "Oranges' Cost".

## 3. Live Coding Walkthrough

### Step 1: The "Slow" Loop Way
```python
import pandas as pd
prices = pd.Series([10, 20, 30])
exchange_rate = 0.85

# Don't do this!
new_prices = []
for p in prices:
    new_prices.append(p * exchange_rate)
print(new_prices)
```

### Step 2: The Vectorized Way
*Context: Converting the entire store's pricing instantly.*
```python
# Do this!
new_prices_vec = prices * exchange_rate
print(new_prices_vec)
# Output is identical, but code is cleaner and 100x faster.
```

### Step 3: Alignment Magic
*Context: Calculating Revenue (Price * Quantity) where lists are jumbled.*
```python
# Note: Bananas are first in Quantity, but second in Price!
price = pd.Series({'Apple': 2.0, 'Banana': 0.5})
qty   = pd.Series({'Banana': 100, 'Apple': 50})

# Pandas matches 'Apple' to 'Apple' automatically. Use Labels, not Order.
revenue = price * qty
print(revenue)
# Apple     100.0
# Banana    50.0
```


---

# Create DataFrame from Dictionary

## 1. Motivation
Series are great for 1D data (just Temperatures).
But real world data is 2D: Temperatures, Dates, and Locations together.
We need a structure that holds multiple Series side-by-side, sharing a common Index.

## 2. Overview
**DataFrame** is a Table (Rows & Columns).
To create one, we usually pass a Dictionary to `pd.DataFrame()`:
-   **Keys** becomes Column Headers.
-   **Values** (Lists) become the Columns.

## 3. Live Coding Walkthrough

### Step 1: Building a Gradebook
*Context: We have data for Students and their Scores.*
```python
import pandas as pd

# Define the columns using a dictionary
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 85]
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)
```

### Step 2: Inspecting the Result
*Instructor: Point out that the keys (Student, Math) are now the headers.*
```python
# Check keys
print(df.keys()) 
# Index(['Student', 'Math', 'Science'], dtype='object')
```

### Step 3: Setting an Index
*Context: We want to use 'Student' as the lookup label, not 0, 1, 2.*
```python
df = df.set_index('Student')
print(df)
# Now 'Student' is the specific row identifier.
# We can find Alice's score easily.
print(df.loc['Alice'])
```


---

# Create DataFrame from Lists and Arrays

## 1. Motivation
Sometimes you don't have a nice dictionary with keys.
You have "Raw Data": a list of lists from a web scraper, or a matrix of numbers from a simulation.
This data has no column names. We need to assign meaning to it.

## 2. Overview
When creating a DataFrame from a List of Lists (or NumPy Array), Pandas processes it row-by-row.
Crucially, **we must provide the `columns=[]` argument** manually, otherwise our columns will be named `0`, `1`, `2`.

## 3. Live Coding Walkthrough

### Step 1: The Raw Data Dump
*Context: We scraped a website and got a list of rows.*
```python
import pandas as pd

raw_data = [
    ['2024-01-01', 100],
    ['2024-01-02', 150],
    ['2024-01-03', 120]
]
```

### Step 2: The "Wrong" Way (No Columns)
```python
df_bad = pd.DataFrame(raw_data)
print(df_bad)
# Columns are 0, 1. Not helpful!
```

### Step 3: The Correct Way (Assigning Meaning)
```python
df = pd.DataFrame(raw_data, columns=['Date', 'Revenue'])
print(df)
# Now we have readable headers.
```

### Step 4: From NumPy (Matrix)
*Context: A simulation generated random values.*
```python
import numpy as np
arr = np.random.rand(3, 2) # 3 rows, 2 cols

df_sim = pd.DataFrame(arr, columns=['Sensor_A', 'Sensor_B'])
print(df_sim)
```


---

# Create DataFrame from CSV Files

## 1. Motivation
CSV (Comma Separated Values) is the universal language of data.
It's how Excel, SQL databases, and web tools export data.
You will spend 90% of your career starting with `pd.read_csv()`.

## 2. Overview
`pd.read_csv()` is a function that:
1.  Opens a file.
2.  Parses the text (splitting by commas).
3.  Infers data types (Integers, Strings).
4.  Returns a DataFrame ready for analysis.

## 3. Live Coding Walkthrough

### Step 1: Loading a File (Simulation)
*Context: We have a file 'sales.csv'. Since we are in a script, we will simulate creating it first.*
```python
import pandas as pd
from io import StringIO

# Simulate a CSV file content
csv_content = """Product,Price,Quantity
Apple,1.00,50
Banana,0.50,100
Cherry,2.00,20"""

# Load it
df = pd.read_csv(StringIO(csv_content))
print(df)
```

### Step 2: Inspecting the Data types
*Instructor: Notice how Pandas correctly guessed that 'Price' is float and 'Quantity' is int.*
```python
print(df.dtypes)
```

### Step 3: Handling Messy Data (No Header)
*Context: Sometimes files don't have the top row.*
```python
csv_no_head = """Apple,1.00\nBanana,0.50"""
df_2 = pd.read_csv(StringIO(csv_no_head), header=None, names=['Product', 'Price'])
print(df_2)
# We manually assigned names.
```


---

# Understand DataFrame Structure

## 1. Motivation
Before analyzing data, you must understand its anatomy.
If you try to loop through a DataFrame like a list, you'll crash.
If you don't know the difference between the **Index** (Labels) and **Values** (Data), you will select the wrong rows.

## 2. Overview
A DataFrame has 3 components:
1.  **Index:** Row Labels (axis 0).
2.  **Columns:** Column Headers (axis 1).
3.  **Values:** The raw NumPy Matrix (The brick and mortar).

## 3. Live Coding Walkthrough

### Step 1: Create a DataFrame
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}, index=['ID_1', 'ID_2'])
print(df)
```

### Step 2: Dissect the Index (Rows)
```python
print("Index:", df.index)
# Index(['ID_1', 'ID_2'], dtype='object')
```

### Step 3: Dissect the Columns (Headers)
```python
print("Columns:", df.columns)
# Index(['Name', 'Age'], dtype='object')
```

### Step 4: Dissect the Values (Raw Data)
```python
print("Values:\n", df.values)
# [['Alice' 25]
#  ['Bob' 30]]
# Note: The headers and ID labels are GONE. This is just a raw matrix now.
```

### Step 5: Check Dimensions
```python
print("Shape:", df.shape)
# (2, 2) -> 2 Rows, 2 Columns.
```


---

# Select Columns from DataFrame

## 1. Motivation
Real datasets have 100+ columns. You usually only care about 2 or 3.
Selecting columns is how we filter out the noise.
Also, selecting a single column (`df['Age']`) is how we invoke statistical methods like `.mean()`.

## 2. Overview
-   **Single Brackets `['Col']`:** Returns a **Series** (1D). Use for math.
-   **Double Brackets `[['Col']]`:** Returns a **DataFrame** (2D). Use for presentation/formatting.

## 3. Live Coding Walkthrough

### Step 1: The "Playlist" Dataset
```python
import pandas as pd
df = pd.DataFrame({
    'Artist': ['Beatles', 'Led Zeppelin', 'Pink Floyd'],
    'Song': ['Hey Jude', 'Stairway', 'Time'],
    'Duration': [431, 482, 421]
})
```

### Step 2: Selecting Audio (Series)
*Context: We want to calculate average duration. We need the raw numbers.*
```python
durations = df['Duration']
print(type(durations)) 
# <class 'pandas.core.series.Series'>

print(durations.mean())
```

### Step 3: Selecting a Subset (DataFrame)
*Context: We want to display just the Artist and Song to the user.*
```python
# Note the Double Brackets!
playlist = df[['Artist', 'Song']]
print(type(playlist))
# <class 'pandas.core.frame.DataFrame'>
print(playlist)
```


---

# Select Rows using loc

## 1. Motivation
In Business, we lookup data by Name.
-   "Find Employee ID 50."
-   "Find Revenue for March."
Lists can't do this easily. `loc` allows us to communicate with our data using these human-readable labels.

## 2. Overview
`df.loc[row_label, col_label]`
-   It is **Label-based**. You must use names.
-   It supports **Slicing** (`'Jan':'Mar'`), and crucially, the slice is **Inclusive** (Start *and* End are included).

## 3. Live Coding Walkthrough

### Step 1: The Employee Database
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Dept': ['HR', 'IT', 'Sales']
}, index=[101, 102, 103]) # Employee IDs
print(df)
```

### Step 2: Lookup by ID (Scalar)
*Context: Find the Name of Employee 102.*
```python
print(df.loc[102, 'Name'])
# 'Bob'
```

### Step 3: Lookup by ID (Entire Row)
*Context: Get full profile for Employee 103.*
```python
print(df.loc[103])
# Name: Charlie, Dept: Sales
```

### Step 4: Slicing (Inclusive)
*Context: Get info for Employees 101 through 102.*
```python
print(df.loc[101:102])
# Returns BOTH 101 and 102.
# Note: Standard Python slices would exclude 102. Pandas loc includes it.
```


---

# Select Rows using iloc

## 1. Motivation
Sometimes you don't care about the labels (names). You care about the **Structure**.
-   "Get the first 5 rows."
-   "Get the last row."
-   "Get every 2nd row."
This is strictly about **Position**.

## 2. Overview
`df.iloc[row_pos, col_pos]` (Integer Location).
-   It is **Zero-Indexed** (0, 1, 2...).
-   It behaves exactly like a Python list slice.
-   It is **Exclusive** at the end (`0:3` returns 0, 1, 2).

## 3. Live Coding Walkthrough

### Step 1: Data Setup
```python
import pandas as pd
df = pd.DataFrame({'Val': [10, 20, 30, 40, 50]}, index=['A', 'B', 'C', 'D', 'E'])
```

### Step 2: First Row (Head)
```python
print(df.iloc[0])
# Returns 10 (Label A)
```

### Step 3: Last Row (Tail)
```python
print(df.iloc[-1])
# Returns 50 (Label E)
```

### Step 4: Slicing (The Trap)
*Instructor: Asking students, "iloc[0:3] gives how many rows?"*
```python
print(df.iloc[0:3])
# Returns Rows 0, 1, 2.
# It does NOT include Index 3. 
# This is standard Python list behavior.
```

### Step 5: Sampling (Step)
*Context: Grab every 2nd row.*
```python
print(df.iloc[::2])
# Returns A, C, E.
```


---

# Add New Columns to DataFrame

## 1. Motivation
Data Analysis isn't just looking at data; it's creating **New Insights**.
-   Calculating "Profit" from Revenue - Cost.
-   Flagging "High Risk" transactions.
These require adding new columns to our table.

## 2. Overview
Feature Engineering.
We use assignment syntax `df['New_Col'] = ...`.
Thanks to **Vectorization**, we can do math on entire columns at once (e.g., `Col_A + Col_B`).

## 3. Live Coding Walkthrough

### Step 1: Sales Data
```python
import pandas as pd
df = pd.DataFrame({
    'Item': ['A', 'B'],
    'Price': [100, 200],
    'Tax_Rate': [0.1, 0.05]
})
```

### Step 2: Math (Vectorized Addition)
*Context: Calculate the actual Tax amount.*
```python
# Price column * Tax_Rate column (Row by Row)
df['Tax_Amt'] = df['Price'] * df['Tax_Rate']
print(df)
# New column appears with [10.0, 10.0]
```

### Step 3: Total (Derived Feature)
```python
df['Final_Price'] = df['Price'] + df['Tax_Amt']
print(df)
```

### Step 4: Boolean Flags
*Context: Flag items that are expensive (> 150).*
```python
df['Is_Expensive'] = df['Final_Price'] > 150
print(df)
# Item B will be True.
```


---

# Filter with Multiple Conditions

## 1. Motivation
Real world logic is complex.
"Find me a house that is Cheap **AND** Big."
"Find me a customer who bought Apples **OR** Bananas."
We need to combine questions.

## 2. Overview
Pandas uses Bitwise Operators for logic:
-   `&` (AND): Both must be True.
-   `|` (OR): At least one must be True.
-   `~` (NOT): Reverse the condition.
**Crucial Rule:** You MUST wrap every condition in parentheses `(...) & (...)`.

## 3. Live Coding Walkthrough

### Step 1: Inventory Data
```python
import pandas as pd
df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Carrot', 'Donut'],
    'Category': ['Fruit', 'Fruit', 'Veg', 'Junk'],
    'Price': [1.0, 0.5, 0.8, 2.0]
})
```

### Step 2: The AND Condition
*Context: Find Healthy Fruits (Fruit AND Price < 1).*
```python
# Note the parentheses!
mask = (df['Category'] == 'Fruit') & (df['Price'] < 1.0)
print(df[mask])
# Only Banana. (Apple was 1.0, not < 1.0)
```

### Step 3: The OR Condition
*Context: Find Snacks (Fruit OR Junk).*
```python
mask = (df['Category'] == 'Fruit') | (df['Category'] == 'Junk')
print(df[mask])
# Apple, Banana, Donut.
```

### Step 4: The .isin() Shortcut
*Context: Writing many ORs is tedious.*
```python
# Check if product is in a list
targets = ['Apple', 'Donut']
print(df[df['Product'].isin(targets)])
```


---

# Delete Columns and Rows

## 1. Motivation
Datasets contain trash.
-   "Metadata" columns we don't need.
-   "Test" rows that aren't real users.
We need to clean the workspace to save memory and focus.

## 2. Overview
`df.drop()`.
-   It can drop Rows (`index=...`) or Columns (`columns=...`).
-   **Crucially:** It returns a **Copy** by default. It does not delete data from the original variable unless you ask it to.

## 3. Live Coding Walkthrough

### Step 1: The Bloated Dataset
```python
import pandas as pd
df = pd.DataFrame({
    'User': ['Alice', 'Bob', 'Test_User'],
    'Password': ['123', '456', '000'], # Security risk!
    'Age': [25, 30, 0]
})
```

### Step 2: Dropping a Column (Safety First)
*Context: Delete the Password column.*
```python
df_safe = df.drop(columns=['Password'])
print(df_safe)
# Password is gone in df_safe.
print(df)
# But Password is STILL here in df! (Immutability)
```

### Step 3: Dropping a Row (Cleaning)
*Context: Remove the Test User (Index 2).*
```python
df_clean = df_safe.drop(index=[2])
print(df_clean)
```

### Step 4: The `inplace` argument
*Context: Actually save the changes.*
```python
# Overwrite the variable
df = df.drop(columns=['Password'])
# Now it is gone forever.
```


---

# Rename Columns and Index

## 1. Motivation
Most datasets come from "Raw Exports". 
Databases often use short, cryptic codes like `UID`, `TS`, `VAL`. 
As analysts, we must rename these so that everyone understands what the data represents.

## 2. Overview
We will learn:
- How to selectively rename one or two columns.
- How to rename the Index.
- The importance of `inplace=True`.

## 3. Live Coding Walkthrough

### Step 1: The Merger Mess
*Instructor: Imagine SuperStore just bought MiniMart. We have their revenue data, but the column names are cryptic codes like 'm_val'.*
```python
import pandas as pd
data = {
    'm_val': [5000, 7500],
    'm_qty': [100, 150],
    'm_loc': ['NYC', 'London']
}
df = pd.DataFrame(data)
print("MiniMart Raw Data:")
print(df)
```

### Step 2: Selective Renaming (Putting up the Signs)
*Instructor: Let's 'rebrand' these columns so they match SuperStore's terminology.*
```python
# Pass a dictionary: {Old: New}
df = df.rename(columns={'m_val': 'Revenue', 'm_qty': 'Quantity', 'm_loc': 'City'})
print("\nAfter Renaming Columns:")
print(df.columns)
# Output: Index(['Revenue', 'Quantity', 'City'], dtype='object')
```

### Step 3: Renaming the Index
*Instructor: Let's change our numeric row labels to something more descriptive for our branches.*
```python
df = df.rename(index={0: 'Store_01', 1: 'Store_02'})
print("\nAfter Renaming Index:")
print(df.index)
# Output: Index(['Store_01', 'Store_02'], dtype='object')
```

### Step 4: The Inplace Shortcut
*Instructor: Instead of writing df = df.rename, we can save directly. Let's rename 'City' to 'Location'.*
```python
# Best practice is assignment, but let's see how inplace works for quick edits
df.rename(columns={'City': 'Location'}, inplace=True)
print("\nFinal Rebranded Data:")
print(df)
```


---

# Group Data with groupby

## 1. Motivation
Spreadsheets are for viewing data; GroupBy is for understanding it. 
Instead of looking at 100 rows of sales, we want to see 1 row per region.

## 2. Overview
`groupby()` is Pandas' implementation of the **Split-Apply-Combine** strategy. It splits a DataFrame into groups based on the unique values of a column, applies a calculation to each group independently, and then combines all results into a clean summary table.

## 3. Live Coding Walkthrough

### Step 1: The Raw Data
*Instructor: Here we have 4 sales records across two regions (North and South).*
```python
import pandas as pd
data = {
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [1000, 2000, 1500, 3000],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Dana']
}
df = pd.DataFrame(data)
print(df)
```

### Step 2: The "Lazy" Object
*Instructor: Watch what happens when we group. It doesn't actually do any math yet!*
```python
grouped = df.groupby('Region')
print(grouped)
# Output: <pandas.core.groupby.generic.DataFrameGroupBy object...>
```

### Step 3: Total Sales by Region
*Instructor: Now, let's apply the 'Apply' step. We want the SUM of Sales.*
```python
# Split (Region), Select (Sales), Apply (Sum), and Combine
region_totals = df.groupby('Region')['Sales'].sum()
print(region_totals)
# Output:
# Region
# North    2500
# South    5000
```

### Step 4: Average Sales (Multiple Columns)
*Instructor: What if we have more numbers? Pandas handles multiple columns automatically.*
```python
# Adding a Units column
df['Units'] = [10, 20, 12, 25]
region_averages = df.groupby('Region')[['Sales', 'Units']].mean()
print(region_averages)
# Notice 'Employee' is gone because you can't find the average of a string!
```


---

# Sort DataFrame by Values

## 1. Motivation
Spreadsheets allow you to sort with a click; Pandas gives you the power to sort millions of rows with a single line of code. 
We sort to find the most expensive products, the highest-selling regions, or to prioritize our workflow.

## 2. Overview
We will learn:
- How to sort by a single column.
- How to use multiple columns for a "Tie-breaker".
- The difference between Ascending and Descending order.

## 3. Live Coding Walkthrough

### Step 1: The Product Inventory
*Instructor: Imagine we are managing a warehouse. Here is our current inventory of electronics.*
```python
import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Price': [1200, 25, 300, 75],
    'Stock': [10, 50, 15, 50]
}
df = pd.DataFrame(data)
print("Original Inventory:")
print(df)
```

### Step 2: Sorting by Price (Descending)
*Instructor: Let's find our most expensive items first. We use sort_values and set ascending=False.*
```python
# We assign the result back to df to save the order
df = df.sort_values(by='Price', ascending=False)
print("\nSorted by Price (High to Low):")
print(df)
# Notice the row labels (Index) moved with the data!
```

### Step 3: Multi-Column Tie-Breaker
*Instructor: We have two items with a Stock of 50. Let's sort by Stock (Highest first), and if they match, use Product name as a tie-breaker (A-Z).*
```python
# Pass lists for both 'by' and 'ascending'
df = df.sort_values(by=['Stock', 'Product'], ascending=[False, True])
print("\nSorted by Stock (High) then Product (A-Z):")
print(df)
```

### Step 4: Fixing the Index
*Instructor: After sorting, our row numbers are all over the place. Let's 'restack the shelves' so the index starts from 0 again.*
```python
df = df.reset_index(drop=True)
print("\nFinal Sorted Inventory with Clean Index:")
print(df)
```


---

# Sort DataFrame by Index

## 1. Motivation
Indexes are like the "Address" of your data. 
After we filter out messy rows or sort by values, our addresses get jumbled.
We use `sort_index()` to put the house numbers back in order so we can easily find specific records.

## 2. Overview
We will learn:
- How to restore row order using `sort_index()`.
- How to sort the columns (headers) of a DataFrame.
- The difference between `sort_values` and `sort_index`.

## 3. Live Coding Walkthrough

### Step 1: The Scrambled Sensor Log
*Instructor: Imagine we have sensors recording temperature. Due to network delays, the entries arrived out of order. Look at the Index values.*
```python
import pandas as pd
data = {'Temp': [22.5, 23.0, 21.8, 22.1]}
# The index represents the Hour (0, 1, 2, 3) but they are scrambled
df = pd.DataFrame(data, index=[3, 0, 2, 1])
print("Scrambled Sensor Log:")
print(df)
```

### Step 2: Restoring Chronological Order
*Instructor: We can't analyze a trend if the hours are jumpy (3, 0, 2, 1). Let's sort by the Index.*
```python
# Restore numeric order
df = df.sort_index()
print("\nSorted by Index (Hour):")
print(df)
```

### Step 3: Sorting Column Headers
*Instructor: Sometimes our columns are disorganized. Let's add a few more and sort them alphabetically.*
```python
df['Humidity'] = [45, 47, 46, 48]
df['Battery'] = [90, 89, 88, 87]
print("\nUnsorted Columns:")
print(df)

# Sort the columns (axis=1) A-Z
df = df.sort_index(axis=1)
print("\nColumns Sorted Alphabetically (Battery, Humidity, Temp):")
print(df)
```

### Step 4: Descending Index
*Instructor: What if we want the most recent hour at the top?*
```python
df = df.sort_index(ascending=False)
print("\nIndex Sorted Descending (3, 2, 1, 0):")
print(df)
```


---

# Handle Missing Data with isna and notna

## 1. Motivation
Data in the wild is messy. 
Before we fill or drop data, we must "Visualize the Damage".
We need to know exactly which columns are missing values and how many.

## 2. Overview
We will learn:
- How to detect `NaN` values using `isna()`.
- How to count missing values per column.
- How to use `notna()` to filter for complete records.

## 3. Live Coding Walkthrough

### Step 1: The Incomplete Data
*Instructor: Here is a realistic dataset where some users didn't provide their Age or Email.*
```python
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Age': [25, np.nan, 30, np.nan],
    'Email': ['a@test.com', 'b@test.com', np.nan, 'd@test.com']
}
df = pd.DataFrame(data)
print(df)
```

### Step 2: The Boolean Mask
*Instructor: Let's use our "Detective Lens" to see the True/False gaps.*
```python
print(df.isna())
# True appears where data is missing
```

### Step 3: Counting the Gaps
*Instructor: This is the most common command you will use as an analyst. It summarizes the gaps per column.*
```python
null_counts = df.isna().sum()
print(null_counts)
# Output shows Age has 2 nulls, Email has 1 null.
```

### Step 4: Filtering for Quality
*Instructor: What if we only want to see people who have provided an Email? We use notna().*
```python
complete_emails = df[df['Email'].notna()]
print(complete_emails)
# Charlie is gone because their Email was NaN.
```


---

# Fill Missing Values with fillna

## 1. Motivation
In the last lesson, we found the holes. 
Now, we are going to fix them. 
We can't always delete rows because we might lose important data. 
So, we "Fill" the holes with logical guesses.

## 2. Overview
We will learn:
- How to fill with a specific number or text.
- How to use "Forward Fill" for trends.
- How to save our changes using `inplace=True`.

## 3. Live Coding Walkthrough

### Step 1: The Missing Pieces
*Instructor: Imagine a temperature sensor that stopped working for two hours.*
```python
import pandas as pd
data = {
    'Time': ['09:00', '10:00', '11:00', '12:00'],
    'Temp': [22.5, None, None, 24.0]
}
df = pd.DataFrame(data)
print(df)
```

### Step 2: The Constant Fill
*Instructor: If we fill with 0, it looks like it was freezing! This might be wrong for temperature.*
```python
# Create a copy to show the bad result
bad_fill = df['Temp'].fillna(0)
print(bad_fill)
```

### Step 3: The Restoration Artist (ffill)
*Instructor: Let's assume the temperature stayed at 22.5 until it changed at noon. We use ffill().*
```python
# Modern Pandas prefers the direct .ffill() method
df.ffill(inplace=True)
print(df)
# Output: Both missing values become 22.5
```

### Step 4: Descriptive Fill (Strings)
*Instructor: For text data, like 'City', we usually use a descriptive word.*
```python
df['Location'] = [None, 'NYC', 'London', None]
df['Location'].fillna('Unknown', inplace=True)
print(df)
```


---

# Drop Missing Values with dropna

## 1. Motivation
Sometimes data is beyond repair. 
If a record is missing its most important parts, we don't guess—we discard.
It's better to have 100 perfect rows than 1000 "maybe" rows.

## 2. Overview
We will learn:
- How to drop any row with a missing value.
- How to drop columns that are too messy.
- How to use `subset` to focus on VIP columns.

## 3. Live Coding Walkthrough

### Step 1: The Messy Shipment Log
*Instructor: Here is a log of physical shipments. Look at how many gaps there are.*
```python
import pandas as pd
import numpy as np

data = {
    'Shipment_ID': [101, 102, None, 104],
    'Status': ['Shipped', None, None, 'Delivered'],
    'Notes': [None, None, None, None] # This column is useless!
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
```

### Step 2: The Default (Over-Cleaning)
*Instructor: Watch what happens if we just use dropna(). It's too aggressive!*
```python
print("\nAggressive Drop (any):")
print(df.dropna())
# Output: Almost everything is gone because every row has at least one NaN.
```

### Step 3: Dropping Empty Columns
*Instructor: The 'Notes' column is 100% empty. Let's get rid of the whole department.*
```python
df.dropna(axis=1, how='all', inplace=True)
print("\nAfter dropping empty columns:")
print(df)
```

### Step 4: Using the Bouncer (Subset)
*Instructor: We only care if the Shipment_ID is missing. If it's missing, we can't track it.*
```python
df.dropna(subset=['Shipment_ID'], inplace=True)

### Step 5: Fixing the Index Gap
*Instructor: Notice the row numbers (0, 1, 3). Row 2 is missing! Let's re-order the boxes on our shelf.*
```python
df.reset_index(drop=True, inplace=True)
print("\nFinal Data with Clean Index:")
print(df)
```
```


---

