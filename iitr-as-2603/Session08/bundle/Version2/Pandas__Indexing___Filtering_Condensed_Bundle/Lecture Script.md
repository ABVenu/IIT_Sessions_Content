## LO–14.2.1: Install Pandas and Create Series (10 minutes)

### 1. Motivation (2 minutes)
Imagine tracking daily lemonade stand revenue. A Python List, `revenue = [100, 150, 120]`, requires remembering that Tuesday is Index 1. Inserting a holiday shifts indices, losing data meaning. We need a data structure linking **Data** (150) to **Labels** (Tuesday). Pandas Series solves this.

### 2. Overview (3 minutes)
A **Pandas Series** is a "Labeled List". It's like a list `[100, 150, ...]` but acts like a dictionary `['Monday', 'Tuesday', ...]`. It combines ordered data with named access.

### 3. Live Coding Walkthrough (5 minutes)
```python
# Step 1: The Problem with Lists
revenue_list = [100, 150, 120]
days_list = ['Mon', 'Tue', 'Wed']
print(revenue_list[1])  # Requires manual counting!
```

```python
# Step 2: The Pandas Solution
import pandas as pd
revenue = pd.Series(data=[100, 150, 120], index=['Mon', 'Tue', 'Wed'])
print(revenue)
# Output: Shows labeled data
```

```python
# Step 3: The Payoff (Label Access)
print(revenue['Tue']) # Direct access by label
```
Pandas Series link data to labels, enabling easy access without manual indexing.

## LO–14.2.7: Create DataFrame from CSV Files (10 minutes)

### 1. Motivation (2 minutes)
CSV is the universal data language used for Excel, SQL, and web exports. You'll likely start with `pd.read_csv()` in most projects.

### 2. Overview (3 minutes)
`pd.read_csv()` opens a file, parses comma-separated text, infers data types (Integers, Strings), and returns a DataFrame ready for analysis.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
from io import StringIO

# Simulate a CSV file content
csv_content = """Product,Price,Quantity
Apple,1.00,50
Banana,0.50,100
Cherry,2.00,20"""

df = pd.read_csv(StringIO(csv_content))
print(df)
```

```python
# Inspecting the Data types
print(df.dtypes)
```

```python
# Handling Messy Data (No Header)
csv_no_head = """Apple,1.00\nBanana,0.50"""
df_2 = pd.read_csv(StringIO(csv_no_head), header=None, names=['Product', 'Price'])
print(df_2)
# Manually assigned names.
```
`pd.read_csv()` simplifies importing data from CSV files into DataFrames, handling data types and missing headers.

## LO–14.2.8: Understand DataFrame Structure (index, columns, values) (10 minutes)

### 1. Motivation (2 minutes)
Understanding DataFrame anatomy is crucial. Incorrect looping leads to errors. Knowing the difference between **Index** (Labels) and **Values** (Data) prevents incorrect row selection.

### 2. Overview (3 minutes)
A DataFrame has 3 components:
1.  **Index:** Row Labels (axis 0).
2.  **Columns:** Column Headers (axis 1).
3.  **Values:** The raw NumPy Matrix (Data).

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}, index=['ID_1', 'ID_2'])
print(df)
```

```python
print("Index:", df.index)
```

```python
print("Columns:", df.columns)
```

```python
print("Values:\n", df.values)
# Raw matrix.
```

```python
print("Shape:", df.shape)
# Rows, Columns.
```
DataFrames consist of an Index (row labels), Columns (headers), and Values (raw data). `.shape` reveals the dimensions.

## LO–14.2.61: Inspect Data Quickly (head, tail, sample, info, shape) (10 minutes)

### 1. The "Recon Scout" Analogy (Why) (3 minutes)
Like a general sending a scout, you must inspect data before analysis. Don't crunch numbers on a 1-million row CSV immediately. There might be missing data, incorrect data types, or corrupted rows.

### 2. Breaking Down the Visuals (What) (4 minutes)
Use `.head()` and `.tail()` to verify boundaries and headers. Use `.sample()` to check for general formatting inconsistencies not visible in the first few rows.
```python
import pandas as pd
df = pd.read_csv("client_data.csv")

# Check for weird headers
display(df.head())

# Check for appended garbage data at the end
display(df.tail(2))

# Verify the core logic of the data
display(df.sample(5))
```

### 3. Reading the Vitals (How) (3 minutes)
`df.info()` is vital. It shows data types for each column and highlights missing values (NaN) by comparing total rows with non-null counts. If 'Age' has fewer non-null values than the total row count, you know you have missing data in the 'Age' column.

```python
df.info()
# If row count is 100, but 'Age' says 95 non-null...
```

Always inspect your data before analysis to avoid traps.

## LO–14.2.9: Select Columns from DataFrame (10 minutes)

### 1. Motivation (2 minutes)
Real datasets have 100+ columns. Selecting columns filters out noise. Selecting a single column (`df['Age']`) allows using statistical methods like `.mean()`.

### 2. Overview (3 minutes)
-   **Single Brackets `['Col']`:** Returns a **Series** (1D). Use for math.
-   **Double Brackets `[['Col']]`:** Returns a **DataFrame** (2D). Use for presentation.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({
    'Artist': ['Beatles', 'Led Zeppelin', 'Pink Floyd'],
    'Song': ['Hey Jude', 'Stairway', 'Time'],
    'Duration': [431, 482, 421]
})
```

```python
durations = df['Duration']
print(type(durations))
print(durations.mean())
```

```python
playlist = df[['Artist', 'Song']]
print(type(playlist))
print(playlist)
```
Single brackets return a Series, useful for calculations. Double brackets return a DataFrame, suitable for display.

## LO–14.2.10: Select Rows using loc (10 minutes)

### 1. Motivation (2 minutes)
In business, data is often looked up by name: "Employee ID 50", "Revenue for March". `loc` enables accessing data using human-readable labels.

### 2. Overview (3 minutes)
`df.loc[row_label, col_label]`
-   **Label-based**. Use names.
-   Supports **Inclusive Slicing** (`'Jan':'Mar'`).

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Dept': ['HR', 'IT', 'Sales']
}, index=[101, 102, 103]) # Employee IDs
print(df)
```

```python
print(df.loc[102, 'Name'])
```

```python
print(df.loc[103])
```

```python
print(df.loc[101:102]) # Inclusive slicing
```
`loc` selects data by labels, including both start and end points in slices.

## LO–14.2.11: Select Rows using iloc (10 minutes)

### 1. Motivation (2 minutes)
Sometimes structure (position) matters more than labels: "First 5 rows," "Last row," "Every 2nd row." This is about **Position**.

### 2. Overview (3 minutes)
`df.iloc[row_pos, col_pos]` (Integer Location).
-   **Zero-Indexed** (0, 1, 2...).
-   Like a Python list slice.
-   **Exclusive** at the end (`0:3` returns 0, 1, 2).

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({'Val': [10, 20, 30, 40, 50]}, index=['A', 'B', 'C', 'D', 'E'])
```

```python
print(df.iloc[0])
```

```python
print(df.iloc[-1])
```

```python
print(df.iloc[0:3]) # Exclusive slicing
```

```python
print(df.iloc[::2])
```
`iloc` selects data by integer position, behaving like Python list slices (exclusive at the end).

## LO–14.2.67: Reset and set index using reset_index() and set_index() (10 minutes)

### 1. The "Library Card Catalog" Analogy (Why) (3 minutes)
Pandas, by default, organizes books (rows) by arrival order (0, 1, 2). This is inefficient for specific author searches. `set_index()` and `reset_index()` change *how* data is organized without altering the data itself.

### 2. Setting the Index (How) (3 minutes)
`set_index()` takes a column and makes it the new lookup key.
```python
import pandas as pd

df = pd.DataFrame({
    'Tracking_Number': ['1Z999...', '1Z888...', '1Z777...', '1Z666...'],
    'Destination':     ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Weight_kg':       [2.5, 0.8, 5.1, 3.3],
    'Status':          ['Delivered', 'In Transit', 'Delivered', 'Pending']
})

shipping_df = df.set_index('Tracking_Number')
package_status = shipping_df.loc['1Z999...']
```

### 3. Resetting the Index (What) (4 minutes)
`reset_index()` rebuilds the index, making it sequential. The old index can be demoted to a column or dropped entirely.

**Option 1: Demote it.**
```python
clean_df = broken_df.reset_index()
```

**Option 2: Destroy it.**
```python
super_clean_df = broken_df.reset_index(drop=True)
```

The index is just the front door; you can move it for better access.

## LO–14.2.12: Filter DataFrame using Boolean Conditions (10 minutes)

### 1. Motivation (2 minutes)
Accessing by ID or Position is useful, but often you access by **Content**: "Students who Passed" (Score > 50), "Products out of stock" (Qty == 0).

### 2. Overview (3 minutes)
**Boolean Indexing**.
1.  Ask a question: `df['Score'] > 50`
2.  Get a `True`/`False` mask.
3.  Apply the mask: `df[mask]` returns True rows.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Kid', 'Teen', 'Adult', 'Senior'],
    'Age': [10, 19, 25, 70]
})
```

```python
mask = df['Age'] >= 21
print(mask)
```

```python
allowed = df[mask]
print(allowed)
```

```python
teens = df[df['Age'] < 20]
print(teens)
```
Boolean indexing filters rows based on conditions, using a True/False mask.

## LO–14.2.13: Filter with Multiple Conditions (10 minutes)

### 1. Motivation (2 minutes)
Real-world logic combines questions: "Cheap **AND** Big house," "Customer bought Apples **OR** Bananas."

### 2. Overview (3 minutes)
Pandas uses Bitwise Operators:
-   `&` (AND): Both True.
-   `|` (OR): At least one True.
-   `~` (NOT): Reverse.
**Rule:** Wrap every condition in parentheses `(...) & (...)`.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Carrot', 'Donut'],
    'Category': ['Fruit', 'Fruit', 'Veg', 'Junk'],
    'Price': [1.0, 0.5, 0.8, 2.0]
})
```

```python
mask = (df['Category'] == 'Fruit') & (df['Price'] < 1.0)
print(df[mask])
```

```python
mask = (df['Category'] == 'Fruit') | (df['Category'] == 'Junk')
print(df[mask])
```

```python
targets = ['Apple', 'Donut']
print(df[df['Product'].isin(targets)])
```
Combine filtering conditions with `&` (AND), `|` (OR). Use `.isin()` for multiple OR conditions.

## LO–14.2.21: Sort DataFrame by Values (10 minutes)

### 1. Motivation (2 minutes)
Pandas sorts millions of rows with code. Sort to find expensive products, high-selling regions, or prioritize workflow.

### 2. Overview (3 minutes)
We'll learn:
- Sorting by a single column.
- Using multiple columns (Tie-breaker).
- Ascending/Descending order.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Price': [1200, 25, 300, 75],
    'Stock': [10, 50, 15, 50]
}
df = pd.DataFrame(data)
print(df)
```

```python
df = df.sort_values(by='Price', ascending=False)
print(df)
```

```python
df = df.sort_values(by=['Stock', 'Product'], ascending=[False, True])
print(df)
```

```python
df = df.reset_index(drop=True)
print(df)
```
`sort_values` sorts by column values. Use multiple columns for tie-breakers. `reset_index` cleans up row numbers after sorting.

## LO–14.2.18: Handle Missing Data with isna and notna (10 minutes)

### 1. Motivation (2 minutes)
Data is often messy. Before filling or dropping, "Visualize the Damage." Know which columns have missing values and how many.

### 2. Overview (3 minutes)
We'll learn:
- Detecting `NaN` with `isna()`.
- Counting missing values.
- Using `notna()` to filter complete records.

### 3. Live Coding Walkthrough (5 minutes)
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

```python
print(df.isna())
```

```python
null_counts = df.isna().sum()
print(null_counts)
```

```python
complete_emails = df[df['Email'].notna()]
print(complete_emails)
```
`isna()` detects missing values. `isna().sum()` counts them per column. `notna()` filters for complete records.

## LO–14.2.19: Fill Missing Values with fillna (10 minutes)

### 1. Motivation (2 minutes)
We found the holes; now we fix them. Don't always delete rows; fill holes with logical guesses.

### 2. Overview (3 minutes)
We'll learn:
- Filling with a specific number/text.
- Using "Forward Fill" for trends.
- Saving changes with `inplace=True`.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
data = {
    'Time': ['09:00', '10:00', '11:00', '12:00'],
    'Temp': [22.5, None, None, 24.0]
}
df = pd.DataFrame(data)
print(df)
```

```python
bad_fill = df['Temp'].fillna(0) # Bad Example
print(bad_fill)
```

```python
df.ffill(inplace=True)
print(df)
```

```python
df['Location'] = [None, 'NYC', 'London', None]
df['Location'].fillna('Unknown', inplace=True)
print(df)
```
`fillna` fills missing values. `ffill` (forward fill) uses the previous value. `inplace=True` saves the changes.

## LO–14.2.20: Drop Missing Values with dropna (10 minutes)

### 1. Motivation (2 minutes)
Sometimes data is beyond repair. Discard records missing important parts. It's better to have perfect rows than "maybe" rows.

### 2. Overview (3 minutes)
We'll learn:
- Dropping rows with missing values.
- Dropping messy columns.
- Using `subset` to focus on VIP columns.

### 3. Live Coding Walkthrough (5 minutes)
```python
import pandas as pd
import numpy as np

data = {
    'Shipment_ID': [101, 102, None, 104],
    'Status': ['Shipped', None, None, 'Delivered'],
    'Notes': [None, None, None, None]
}
df = pd.DataFrame(data)
print(df)
```

```python
print(df.dropna()) # Too aggressive
```

```python
df.dropna(axis=1, how='all', inplace=True)
print(df)
```

```python
df.dropna(subset=['Shipment_ID'], inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)
```
`dropna` removes rows/columns with missing values. `subset` focuses on key columns. `axis=1` drops columns. `how='all'` drops if all values are NA. `reset_index` fixes the index.