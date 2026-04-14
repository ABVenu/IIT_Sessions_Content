# Install Pandas and Create Series

## 1. The "Why": Beyond Python Lists
Imagine you are tracking daily revenue for a lemonade stand. You have a list of revenues: `[100, 150, 120]`.
-   **The Problem:** If I ask, "What was the revenue on Tuesday?", you have to know that Tuesday is Index `1`.
-   **The Risk:** If you insert a holiday on Monday, all your index positions shift, and you might report the wrong revenue. 
-   **The Solution:** We need a tool that binds **Data** (Revenue) to **Context** (Day). That tool is **Pandas**.


![Anatomy of a Pandas Series](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-1-series-anatomy.webp)

## 2. Analogy: The Locker Room
Think of a standard Python List like a row of **numbered lockers**. You have to remember: "My gym bag is in locker #42". If the locker numbers change, you are lost.
Think of a **Pandas Series** like **named cubbies**. You just look for the sticker that says "Tim". It doesn't matter if Tim's cubby is first or last; you find it by **Label**, not position.

## 3. The Core Concept: Series
A **Series** is Pandas' building block. It is a **One-Dimensional Labeled Array**.
-   **1D:** It’s a single list of data (like a column in Excel).
-   **Labeled:** Every value has a corresponding name (the Index).
-   **Array:** It is built on **NumPy**, meaning it is incredibly fast (C-speed) compared to standard Python lists.

## 4. Real-World Application
Data Scientists use Series to hold:
-   **Time Series:** Dates as Index, Temperatures as Values.
-   **Financial Data:** Tickers ('AAPL', 'GOOG') as Index, Prices as Values.
-   **Survey Results:** User IDs as Index, Responses as Values.

## 5. Quick Syntax
```python
import pandas as pd
# Creating a Series is like upgrading a List
prices = pd.Series([100, 200], index=['Mon', 'Tue'])
```


---

# Create DataFrame from CSV Files

## 1. The "Why": The Universal Standard
Data doesn't live in code; it lives in files.
-   **Excel** exports to CSV.
-   **SQL Databases** dump to CSV.
-   **Salesforce/CRMs** report in CSV.
**CSV** (Comma-Separated Values) is the industry standard for moving tabular data between systems because it is simple text. Pandas is the tool that reads this text and brings it to life.


![Reading a CSV File into a DataFrame](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/pandas/14-2-7-csv-to-dataframe.png)

## 2. Analogy: The Universal Translator
Think of CSV as the **Lingua Franca** (Common Language) of the data world.
-   Your database speaks "SQL".
-   Your analysis tool speaks "Python".
-   They can't talk directly.
-   **CSV is the bridge.** The database writes a CSV. Pandas reads that CSV and translates it into a DataFrame. `pd.read_csv()` is your Universal Translator.

## 3. The `pd.read_csv()` Powerhouse
This single function is the workhorse of Pandas. It is smart enough to:
-   **Detect Types:** "This column looks like a date."
-   **Handle Headers:** "The first row contains names."
-   **Skip Junk:** "Ignore the first 3 lines of metadata files."

## 4. Key Parameters
-   `filepath`: Path to the file (`data.csv`) or even a URL (`http://...`).
-   `sep`: Using tabs instead of commas? set `sep='\t'`.
-   `index_col`: Want to use 'Date' as the index immediately? set `index_col='Date'`.

```python
# The one line you will write 10,000 times
df = pd.read_csv('sales_data.csv')
```


---

# Understand DataFrame Structure

## 1. The "Why": Anatomy Class
Before you can perform surgery (Analysis), you must understand anatomy (Structure).
A DataFrame isn't just a grid of numbers. It is a precise system of 3 parts.
-   If you don't know the difference between the **Index**, **Columns**, and **Values**, you will make selection errors.
-   *Example:* Trying to select a row by "Name" when the index is actually "ID".

## 2. Analogy: The City Grid
Think of a DataFrame like a **City Map**:
1.  **Index (Y-axis):** The names of the streets (Row labels).
    -   *Role:* Identifies the "Who" (Which observation?).
2.  **Columns (X-axis):** The names of the avenues (Column headers).
    -   *Role:* Identifies the "What" (Which variable?).
3.  **Values (The Buildings):** The actual brick-and-mortar data at the intersection.
    -   *Role:* The raw content numbers.

## 3. The "Trinity" Components
Every DataFrame is a container for these three distinct objects:
-   `.index`: The immutable row labels.
-   `.columns`: The column names.
-   `.values`: The raw NumPy array of data (stripping away all labels).

## 4. Inspection Tools
Before analyzing, always inspect your tools:
-   `df.shape`: How big is it? `(Rows, Cols)`.
-   `df.dtypes`: Is the data numbers or text?
-   `df.head()`: Show me the first few rows.
```python
df.info() # The medical chart summaries everything.
```


---

# Inspect Data Quickly

When you load a new dataset, you should never start analyzing or transforming it immediately. The first step is always **Data Reconnaissance**. You need to know the shape, the data types, and what the actual data looks like. 

Pandas provides five fundamental tools to help you inspect a DataFrame in less than 30 seconds.

## 1. Viewing the Data (`head`, `tail`, `sample`)

Printing an entire 1-million row DataFrame will crash your notebook. Instead, you extract small glimpses of the data.

*   **`df.head(n)`**: Returns the first `n` rows (default is 5). Useful to see the column headers and the starting data.
*   **`df.tail(n)`**: Returns the last `n` rows. Useful to check if the data at the bottom of the file is corrupted.
*   **`df.sample(n)`**: Returns `n` random rows. Highly recommended to catch anomalies that hide in the middle of standard alphabetical lists.

```python
import pandas as pd
df = pd.read_csv("sales.csv")

# Look at 3 random rows
print(df.sample(3))
```

## 2. Understanding the Structure (`shape`, `info`)

Once you know what the data looks like, you need to know how big it is, and what types of data it holds.

*   **`df.shape`**: This is an attribute (no parentheses). It returns a tuple `(rows, columns)`. E.g., `(10000, 5)` means 10,000 rows and 5 columns.
*   **`df.info()`**: The most powerful inspection tool. It prints a concise summary including the total row count, every column name, the data type (`dtype`) of every column, and how many non-null values exist in each column.

```python
# Check how many rows are missing data (null) and what the datatypes are
df.info()
```

## External Resources
- [Pandas Intro to Data Structures](https://pandas.pydata.org/docs/user_guide/dsintro.html)
- [Exploratory Data Analysis in Pandas](https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce)


---

# Select Columns from DataFrame

## 1. The "Why": Signal vs Noise
A typical industry dataset (e.g., Salesforce export) might have 150 columns (`User_ID`, `Log_Date`, `IP_Address`...).
Your analysis might only need 2 columns: `User_ID` and `Revenue`.
Selecting columns is the first step in **Data Cleaning**: you discard the 148 columns of "Noise" to focus on the 2 columns of "Signal".

## 2. Analogy: The Restaurant Menu
Think of a DataFrame like a **Giant Menu**:
-   **The Full Table:** The entire menu with 100 items (Appetizers, Mains, Drinks).
-   **Single Selection `['Burger']`:** You order one specific dish. The waiter brings you *just* the plate (A Series).
-   **List Selection `[['Burger', 'Fries']]`:** You order a combo. The waiter brings you a smaller *trany* with just those items (A new DataFrame).

## 3. Syntax Options
### Bracket Notation `[]` (The Standard)
-   `df['Column Name']`
-   **Pros:** Works with spaces, special characters, and numbers.
-   **Cons:** Slightly more typing.

### Dot Notation `.` (The Shortcut)
-   `df.ColumnName`
-   **Pros:** Fast to type.
-   **Cons:** Fails on spaces (`df.First Name` crashes). Fails if column name conflicts with a method (e.g., a column named `count`).

## 4. Quick Syntax
```python
# Returns a Series (1D)
email_series = df['Email']

# Returns a DataFrame (2D) - Note double brackets!
contact_info = df[['Name', 'Email']]
```


---

# Select Rows using loc

## 1. The "Why": Names over Numbers
In business, we rarely say "Pull Record #492". We say:
-   "Find the record for **Employee 101**".
-   "Find the Revenue for **January**".
Standard Python lists only understand positions (0, 1, 2). Pandas `loc` allows us to query data using these **Meaningful Labels**.

## 2. Analogy: The Employee Directory
Think of `loc` as an **Company Directory**:
-   **By Position `iloc`:** "Go to the 3rd cubicle on the left."
    -   *Risk:* If the team rearranges desks, you talk to the wrong person.
-   **By Label `loc`:** "Go to **Alice's** desk."
    -   *Benefit:* Alice is Alice, no matter where she sits.

## 3. Syntax Rules
`df.loc[Row_Label, Column_Label]`
-   **Exact Match:** `df.loc['Alice']` gets Alice's whole row.
-   **Cross Section:** `df.loc['Alice', 'Salary']` gets just her salary.

## 4. The Slicing Superpower
Unlike normal Python, **`loc` slicing is INCLUSIVE**.
`df.loc['Jan':'Mar']` returns Jan, Feb, **AND** Mar.
-   *Why?* Because labels are not numbers. If you ask for files "A through Z", you expect Z to be part of the pile.


---

# Select Rows using iloc

## 1. The "Why": Structure over Semantics
Sometimes you don't care *who* the data belongs to (Labels). You care about *where* it sits (Position).
-   "Give me the first 5 rows for a preview."
-   "Split the dataset: First 80% for training, last 20% for testing."
-   "Grab every 10th row for a random sample."
For these algorithmic tasks, we use `iloc` (Integer Location).

## 2. Analogy: The Global Positioning System (GPS)
Think of `iloc` like **GPS Coordinates**:
-   **Structure-Based:** It doesn't care if the building at `(34N, 118W)` is a Starbucks or a Library. It just points to that physical spot.
-   **Robust to Renaming:** If "Main St" is renamed to "Broadway", the GPS coordinate (0, 0) stays the same.
-   **Fragile to Reordering:** If you shuffle the list, `iloc[0]` points to a totally different person.

## 3. Syntax Rules
`df.iloc[row_int, col_int]`
-   **Zero-Indexed:** Starts at 0, not 1.
-   **Exclusive Slicing:** `0:5` returns rows 0, 1, 2, 3, 4. It **excludes** 5.
    -   *Why?* To be consistent with Python Lists `my_list[0:5]`.

## 4. Quick Syntax
```python
# First Row
df.iloc[0]

# First 5 Rows (0, 1, 2, 3, 4)
df.iloc[0:5]

# Last Row
df.iloc[-1]
```


---

# Reset and set index using reset_index() and set_index()

The Pandas Index determines how you look up rows of data. By default, Pandas assigns a numeric index (0, 1, 2, 3...) to every DataFrame. However, this is often arbitrary and not useful for analysis. 

If you are analyzing stock data, the date is far more useful as the lookup key than an arbitrary row number. Pandas allows you to dynamically change which column acts as the index.

## 1. Setting a New Index (`set_index()`)

You can promote any existing column to become the new index. Doing so moves it out of the main data block and firmly anchors it to the left side as the primary lookup key.

```python
import pandas as pd

df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Stock_Price': [150, 152, 149]
})

# The 'Date' column is promoted to the Index.
# The original row numbers (0, 1, 2) are destroyed.
time_series_df = df.set_index('Date')

# Now you can easily look up January 2nd!
print(time_series_df.loc['2023-01-02'])
```

## 2. Resetting the Index (`reset_index()`)

Often, after performing aggressive groupby operations or filtering, the index becomes a jumbled mess of missing numbers (e.g., `[0, 5, 23, 102]`). 

You use `reset_index()` to fix this. It does two things:
1. It creates a brand new, clean sequence of numbers (`0, 1, 2, 3...`) to act as the index.
2. It takes whatever the *old* index was, and demotes it back into a standard column so you don't lose the data.

```python
# Assume we have an ugly filtered DataFrame
filtered_df = df.head(3) # Indexes might be 45, 92, 103

# Reset the index. The old keys (45, 92) become a new column named 'index'.
clean_df = filtered_df.reset_index()
```

### The `drop=True` Parameter
If the old index was just arbitrary garbage numbers that you don't want to save as a column, you can outright destroy it while generating the new clean sequence.

```python
# Erase the messy index entirely and replace with 0, 1, 2...
clean_df = filtered_df.reset_index(drop=True)
```

## External Resources
- [Pandas set_index() Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)
- [Pandas reset_index() Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)


---

# Filter DataFrame using Boolean Conditions

## 1. The "Why": Questions over Coordinates
Finding data by "Where it is" (`iloc`) is useful for machines.
Finding data by "What it is" (`df['Sales'] > 1000`) is useful for **Humans**.
-   "Show me all transactions from France."
-   "Who scored above 90%?"
-   "Which servers are offline?"
We call this **Boolean Filtering** because the answer to every question is True (Keep) or False (Discard).

## 2. Analogy: The Nightclub Bouncer
Think of Boolean Filtering like a **Nightclub Queue**:
1.  **The Question:** "Are you over 21?" (`df['Age'] >= 21`).
2.  **The Mask (ID Check):** The Bouncer looks at every person and assigns a status.
    -   Person A (19): `False` (Denied).
    -   Person B (25): `True` (Allowed).
3.  **The Filter (Velvet Rope):** `df[mask]` keeps only the `True` people and removes the rest.

## 3. The Mechanism: The Mask
The intermediate step is the **Boolean Mask**.
```python
mask = df['Age'] > 25
# result: [True, False, True, True...]
```
Pandas overlays this mask on your DataFrame.
-   **True:** Visible.
-   **False:** Invisible (Dropped).

## 4. Cheat Sheet
-   `==`: Exact match (`City == 'NY'`).
-   `!=`: Not equal (`Status != 'Fail'`).
-   `>`: Greater than (`Price > 100`).
-   `~`: The "Not" operator (inverts the mask).


---

# Filter with Multiple Conditions

## 1. The "Why": Compound Logic
Real-world questions are rarely simple. We don't just ask "Show me Fruits."
We ask:
-   "Show me Fruits **AND** Price < \$1." (Deal Hunting).
-   "Show me Customers from NY **OR** NJ." (Regional Analysis).
-   "Show me Products that are **NOT** Out of Stock." (Validation).
We need Logic Operators to combine these questions.

## 2. Analogy: The Inventory Filter
Think of shopping on Amazon. You don't just click "Shoes". You click:
1.  **Category:** Shoes
2.  **AND Price:** < \$50
3.  **AND Rating:** > 4 Stars
You are building a **Compound Mask**. Only items that satisfy *all* criteria pass through the filter.

## 3. The Operators
Pandas uses **Bitwise Operators**, not Python keywords.
-   `&` (AND): Both conditions must be True.
-   `|` (OR): At least one condition can be True.
-   `~` (NOT): Inverses the condition.

## 4. The Parentheses Rule
You **MUST** wrap every condition in parentheses!
-   *Wrong:* `df['A'] > 5 & df['B'] < 10`
-   *Right:* `(df['A'] > 5) & (df['B'] < 10)`
*Why?* Because of Order of Operations. Python tries to calculate `5 & df['B']` first if you don't use parentheses, which causes a crash.


---

# Sort DataFrame by Values

## 1. The "Why": Organizing Chaos
Imagine you manage a **Warehouse** with 5,000 different products. 
- Some items are selling out fast, and some are just gathering dust.
- If you want to know which items are your "Top Sellers" or which are "Most Expensive", you can't look at them in a random pile.
- You need a way to **rank** them so that the most important information is always at the top.

In Pandas, we use `sort_values()` to transform a "Random Pile of Data" into a "Ranked Report".

## 2. Analogy: The Warehouse Manager
Think of your DataFrame as the **Warehouse Inventory**.
- **Picking the Aisle (`by`)**: The manager decides which characteristic to sort by. Is it "Total Sales", "Price", or "Quantity"?
- **Ascending vs. Descending (`ascending`)**: 
    - **Ascending**: Lowest to Highest (e.g., finding the cheapest items).
    - **Descending**: Highest to Lowest (e.g., finding the top earners).
- **The Tie-Breaker**: If two items have the exact same price, the manager uses a second rule, like "Alphabetical Name", to decide who goes first.

## 3. The Core Concept: Ranking
Sorting isn't just about order; it's about **visibility**. By sorting, we bring focus to:
- **Outliers**: The extremely large or small values.
- **Trends**: Highs and Lows in a time series.
- **Quality**: The best vs. the worst performers.

## 4. Real-World Application
- **Retail**: Sorting products by "Best Selling" for website recommendations.
- **HR**: Sorting employees by "Years of Service" for anniversary awards.
- **Logistics**: Sorting shipments by "Delivery Deadline" to prioritize the morning fleet.

## 5. Quick Syntax
```python
import pandas as pd
df = pd.DataFrame({'Product': ['Laptop', 'Mouse', 'Monitor'], 'Price': [1200, 25, 300]})

# Sorting by Price (Most expensive first)
df_sorted = df.sort_values(by='Price', ascending=False)
print(df_sorted)
```


---

# Handle Missing Data with isna and notna

## 1. The "Why": Data is Rarely Perfect
In the real world, data is full of gaps. Sensors fail, customers skip optional questions on a form, and machines lose connection. 
As a Data Scientist, you cannot build a model on "Empty" data. If you try to calculate the average height of a class but 5 students didn't provide their height, your calculation will fail or be misleading.

Identifying these gaps is the first step in "Data Cleaning".

## 2. Analogy: The Crime Scene Detective
Imagine you are a detective examining a **Floorplan** (your DataFrame).
- **The Evidence**: Most rooms have furniture (values), but some rooms are completely empty (Missing Data / NaN).
- **The Search**: You walk through the house with a specialized **"Gap Detector"**.
    - **`isna()`**: Your detector beeps `True` every time you find an empty room.
    - **`notna()`**: Your detector beeps `True` every time you find a room with furniture.

Before you can solve the case (analyze the data), you must know exactly where the "evidence" is missing.

## 3. The Core Concept: NaN
In Pandas, missing data is represented by **`NaN`** (Not a Number). 
`NaN` is a technical placeholder that tells the computer: *"Someone was supposed to put a value here, but they didn't."*

## 4. Real-World Application
- **Surveys**: Finding how many people skipped the "Income" question.
- **Logistics**: Identifying which shipments missed their "Delivery Date".
- **Marketing**: Counting which leads gave an email but no phone number.

## 5. Quick Syntax
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'Name': ['Alice', np.nan, 'Charlie']})

# Find the holes
print(df.isna()) 

# Count the total number of holes
print(df.isna().sum())
```


---

# Fill Missing Values with fillna

## 1. The "Why": Continuity, not Perfection
In our previous lesson, we identified "holes" in our data (NaNs). But a hole is a problem. 
- If you have a list of stock prices and one day is missing, your line chart will have a "break" in it.
- If you are calculating the total cost of groceries and one item has a missing price, the total becomes "unknown".

Sometimes, we can't just delete the missing rows; we have to **estimate** or **guess** what should have been there to keep our calculations moving.

## 2. Analogy: The Restoration Artist
Imagine you are restoring an **Ancient Painting**. There are spots where the paint has flaked off (Missing Data).
How do you fix it?

1.  **Fixed Restoration (Constant)**: You decide to paint all missing spots with a neutral "Grey" to acknowledge they are fixed but unknown.
2.  **Neighborly Restoration (ffill/bfill)**: You look at the paint color right next to the hole and duplicate it. "If the sky was blue a millimeter to the left, it was probably blue here too."
3.  **Statistical Restoration (Mean/Median)**: You look at the average color of the whole painting and use that to fill the gaps.

In Pandas, the **`.fillna()`** method is your brush.

## 3. The Core Concept: The Safety Net
`fillna()` acts as a **Safety Net**. It ensures that when your code runs, it never trips over a `NaN`. It replaces the "unknown" with a "logical placeholder" so that your math functions (`.sum()`, `.mean()`) don't return `NaN` as a result.

## 4. Real-World Application
- **IoT Sensors**: If a temperature sensor skips a minute, use the temperature from the previous minute (`ffill`).
- **User Profiles**: If a user didn't enter their City, fill it with `"Unknown"` or `"Global"`.
- **Financial Trends**: Filling missing stock prices with the average of the week.

## 5. Quick Syntax
```python
import pandas as pd
df = pd.DataFrame({'Sales': [100, None, 150]})

# Fill with a constant zero
df['Sales'] = df['Sales'].fillna(0)

# Fill with the "sky" color from above (Forward Fill)
df['Sales'] = df['Sales'].fillna(method='ffill')
```


---

# Drop Missing Values with dropna

## 1. The "Why": Quality over Quantity
Sometimes, a record is so broken that it's useless. 
- If you are building a Login System and a user record has no **Username** and no **Password**, that row is just noise. 
- If a scientist is measuring the effect of a drug and the "Dosage" value is missing, the entire row's "Result" is scientifically invalid.

In these cases, filling with a guess (`fillna`) is dangerous. We must **Drop** the data to maintain high quality.

## 2. Analogy: The Quality Control Bouncer
Imagine a **Conveyor Belt** carrying boxes (Rows) into your factory. Some boxes are missing items (NaNs). You hire a **Bouncer** (the `dropna()` method) to stand at the end of the belt.

1.  **The Strict Bouncer (`how='any'`)**: "If even one item is missing from the box, throw the entire box into the trash!" 
    *(This is the default setting in Pandas).*
2.  **The Patient Bouncer (`how='all'`)**: "Only throw the box away if it is completely empty. If there is at least one good item, keep it."
3.  **The Focused Bouncer (`subset`)**: "I don't care if the 'Stickers' are missing, but if the 'Battery' is missing, the box goes in the bin!"

## 3. The Core Concept: Axis and Thresholds
Dropping data is a permanent decision. You can drop:
- **Rows (`axis=0`)**: Throwing away the box.
- **Columns (`axis=1`)**: Getting rid of the entire "Sticker" department because too many stickers are missing.

## 4. Real-World Application
- **Medical Trials**: Removing patients who missed their primary checkup.
- **Banking**: Rejecting loan applications that didn't provide a Credit Score.
- **Scientific Research**: Discarding sensor readings from a day where the power was out.

## 5. Quick Syntax
```python
import pandas as pd
df = pd.DataFrame({'A': [1, None], 'B': [None, None]})

# Drop any row with a hole
clean_rows = df.dropna()

# Drop rows ONLY if they are completely empty
empty_dropped = df.dropna(how='all')

# Drop rows only if the important column 'A' is missing
important_only = df.dropna(subset=['A'])
```


---

