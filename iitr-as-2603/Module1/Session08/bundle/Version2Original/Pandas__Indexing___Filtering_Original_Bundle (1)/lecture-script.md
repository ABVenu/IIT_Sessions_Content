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

# Inspect Data Quickly

## 1. The "Recon Scout" Analogy (Why)

### Why
If a general marches an entire army into a valley without sending a scout to look at it first, they might walk right into a trap.

In Data Science, if you start crunching numbers, filtering, and grouping a 1-million row CSV immediately after importing it, you will fall into traps. Half the data might be missing. The numbers might actually be stored as text strings. The file might have corrupted at row 500,000. 

### What
You execute a basic "Recon" sequence using 5 core Pandas functions. These functions give you the exact perimeter (shape), the visual landscape (head/tail/sample), and the structural integrity (info) of the data before you waste time analyzing bad data.

### How
```python
import pandas as pd
df = pd.read_csv("client_data.csv")

# The Recon Sequence takes less than 30 seconds
print(df.shape)
df.info()
df.head(3)
```

## 2. Breaking Down the Visuals (What)

### Why
Looking at the top of the file guarantees the headers loaded correctly. But many times, Excel files append "Totals" or "Disclaimers" to the very bottom row, which ruins your statistical averages. 

### What
You use `.head()` and `.tail()` to verify the boundaries. You use `.sample()` to pull random chunks from the middle of the dataset, looking for generalized formatting inconsistencies that don't appear in row 1.

### How
```python
# Check for weird headers
display(df.head())

# Check for appended garbage data at the end (e.g. "CONFIDENTIAL 2024")
display(df.tail(2))

# Verify the core logic of the data
display(df.sample(5))
```

## 3. Reading the Vitals (How)

### Why
A column might look like numbers visually `[1, 2, 3]`, but if it is stored as text `['1', '2', '3']`, running `.sum()` will concatenate the strings into `123`, destroying your analysis. 

### What
`df.info()` is the most important command. It forces Pandas to confess exactly what data types it assigned to every column. It also compares the total number of rows against the number of `Non-Null` values, instantly highlighting any columns that contain missing `NaN` data.

### How
```python
# The diagnostic X-Ray
df.info()

# Look at the output:
# If row count is 100, but 'Age' says 95 non-null, you know exactly 
# where your missing data problem is before you even start coding!
```

"Always scout the perimeter before you commit the troops."


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

# Reset and Set Index

## 1. The "Library Card Catalog" Analogy (Why)

### Why
Imagine a massive library. By default, Pandas numbers the books based on the order they arrived on the loading dock: Book 0, Book 1, Book 2. This is useless if you are trying to find a specific author. You need a way to change *how* the data is organized without changing the data itself.

### What
The `set_index()` and `reset_index()` methods allow you to swap out the Card Catalog system. The books (the columns) stay exactly the same, but the way you look them up (the Index) changes. 

## 2. Setting the Index (How)

### Why
You realize that looking up shipping records by row number is inefficient. You want to look them up by `Tracking_Number`.

### What
You use `set_index()`. You tell Pandas: "Take this specific column out of the main body, and bolt it to the left wall. This is my new lookup key." 

### How
```python
import pandas as pd

df = pd.DataFrame({
    'Tracking_Number': ['1Z9999999999999999', '1Z8888888888888888', '1Z7777777777777777', '1Z6666666666666666'],
    'Destination':     ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Weight_kg':       [2.5, 0.8, 5.1, 3.3],
    'Status':          ['Delivered', 'In Transit', 'Delivered', 'Pending']
})

# The original index is destroyed, and Tracking_Number takes over.
shipping_df = df.set_index('Tracking_Number')

# Now .loc works instantly using the tracking number
package_status = shipping_df.loc['1Z9999999999999999']
```

## 3. Resetting the Index (What)

### Why
Sometimes the card catalog gets ruined. If you delete 500 books from the library (filtering data), your default index will look broken: `0, 2, 503, 504...`. If you try to loop over this list by index, Python will crash on row `1` because it no longer exists.

### What
You use `reset_index()`. Pandas will wipe out the broken left wall, and build a brand new, perfectly sequential wall of numbers starting from 0. 

### How
What happens to the old, broken index? There are two options:

**Option 1: Demote it.**
Pandas assumes the old index was important data, so it demotes it, moving it *back* into the main body as a standard column.

```python
# The old broken index becomes a column named 'index'
clean_df = broken_df.reset_index() 
```

**Option 2: Destroy it.**
If the old index was just garbage row numbers, you don't want to save them. You tell Pandas to drop them in the trash during the reset.

```python
# The most common command used after filtering datasets
super_clean_df = broken_df.reset_index(drop=True)
```

"The data is the building. The index is just the front door. You can move the door whenever you need better access."


---

# Filter DataFrame using Boolean Conditions

## 1. Motivation
Accessing by ID or Position is useful, but usually we access by **Content**.
-   "Show me students who Passed." (Score > 50).
-   "Show me products out of stock." (Qty == 0).
We need to ask the data questions.

## 2. Overview
**Boolean Indexing**.
1.  Ask a question: `df['Score'] > 50`
2.  Get an answer: A mask of `True`/`False` values.
3.  Apply the mask: `df[mask]` returns only the True rows.

## 3. Live Coding Walkthrough

### Step 1: The Nightclub Queue
*Context: We have a list of people and their ages.*
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Kid', 'Teen', 'Adult', 'Senior'],
    'Age': [10, 19, 25, 70]
})
```

### Step 2: The Bouncer's Check (The Condition)
*Context: Who is allowed in? (Age >= 21)*
```python
mask = df['Age'] >= 21
print(mask)
# 0    False
# 1    False
# 2     True
# 3     True
# This is our "Velvet Rope".
```

### Step 3: Letting them In (The Filter)
```python
allowed = df[mask]
print(allowed)
# Only Adult and Senior remain.
```

### Step 4: The One-Liner (Pro way)
```python
# Doing it all at once
teens = df[df['Age'] < 20]
print(teens)
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

