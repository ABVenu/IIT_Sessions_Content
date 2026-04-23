# Pandas: DataFrames, Aggregation & Data Cleanup

We learned how to load data, clean missing values, and filter rows. We begin by **revising how to create and read** DataFrames in pandas—the foundation for everything that follows. Then we **summarise** datasets with **groupby** and **`agg`**, and we **clean** tables by dropping columns we do not need. Combining multiple tables with **`merge`** and joins is planned for a later session.

## Basic CR on DataFrames using Pandas

**CR** here means **Create** and **Read**: building a table in memory, loading from a file, and inspecting or selecting data. (We also touch on updating and deleting rows or columns, because those operations often sit in the same workflow.)

- **Create:** Build a **`DataFrame`** with `pd.DataFrame({...})`, add a **new column** by assigning a list to `df["ColumnName"]`, and add or change rows using **`.loc`** with an index label.
- **Read:** **`print(df)`**, **`.head()`** / **`.tail()`** for a quick look, select **one or more columns** with `df["A"]` or `df[["A","B"]]`, and **filter rows** with boolean conditions on columns (e.g. `df[df["Age"] > 30]`).
- **From file:** Use **`pd.read_csv("file.csv")`** to turn comma-separated data into a DataFrame (rows and columns).
- **Naming your script:** Do **not** save your code file as `pandas.py`—Python may import **your file** instead of the real library (**circular import**). Use a different filename.
- **Drop:** Remove a **column** with **`df.drop("Col", axis=1)`** (or a list of names). Use **`inplace=True`** to change `df` in place; otherwise pandas returns a **copy** and you should assign back, e.g. `df = df.drop(...)`.

```python
import pandas as pd  # Load pandas; always use a filename other than pandas.py for your script

# Create — build a small employee table
df = pd.DataFrame({
    "Name":   ["Aarav", "Diya", "Kabir"],
    "Age":    [28, 34, 29],
    "Salary": [50000, 60000, 55000],
})

# Read — inspect and select
print(df.head())  # Show first few rows for a quick look
print(df["Salary"])  # Print the Salary column
adults = df[df["Age"] >= 30]  # Keep rows where Age is 30 or more (boolean filter)

# Create — add a column
df["Bonus"] = [5000, 6000, 5500]  # New column from a list (same length as rows)

# Update — change one cell with .loc (index label must exist or be assigned carefully)
df.loc[0, "Name"] = "Aarav S."  # Set one cell by row label and column name

# Delete — drop a column (returns new DataFrame unless inplace=True)
df = df.drop("Bonus", axis=1)  # axis=1 means column; assign back unless using inplace=True
```

**How the code works:**

- **`pd.DataFrame({...})`** builds a table from dictionaries: keys become **column names**, lists become **column values** (same length in each column).
- **`df["Salary"]`** selects one column; **`df[["Name","Age"]]`** selects several. **Boolean masks** like `df["Age"] >= 30` give a True/False Series; **`df[condition]`** keeps only rows where the condition is True.
- **`.loc[row_label, col_name]`** picks one cell or a slice for **label-based** access—useful for updates.
- **`drop(..., axis=1)`** removes **columns**; **`axis=0`** would refer to **rows** (by index label). Always set **`axis=1`** when dropping a column by name.
- **Two conditions at once:** Use **`&`** (and) and **`|`** (or) between boolean Series, and **wrap each condition in parentheses**—e.g. `df[(df["Age"] > 25) & (df["Salary"] > 50000)]`. Plain Python **`and` / `or`** do not work element-wise on columns.
- **Remember reassignment:** Methods like **`drop`** often return a **new** DataFrame—use **`df = df.drop(...)`** or **`inplace=True`** where supported, or your table will not change.

Once you are comfortable with **create, read, update, and drop** on a single table, you are ready for **aggregation** below.

## Introduction to Aggregation

Data by itself is just a big pile of numbers. **Aggregation** is the process of reducing that big pile into a few useful summary values so we can take decisions.

- **Official Definition:** **Aggregation** is the process of applying a function (like sum, mean, or count) to a group of values to produce a single summary value.
- **In Simple Words:** It means putting many rows together and taking out one final answer from them, like "total sales" or "average marks".
- **Real-Life Example:** Think of a class teacher. She has marks of 50 students, but when the principal asks her, she does not read every student's marks. She simply says **"Average marks of the class is 72."** That one number is aggregation.

Before we jump to groupby, let us first understand simple aggregation on a full column.

## Basic Aggregation Functions

Pandas gives us ready-made functions to summarise any column in one line. You do not have to write loops or formulas yourself.

- **`sum()`** → Adds all values of a column.
- **`mean()`** → Gives the average (total ÷ count).
- **`count()`** → Counts how many non-empty values are there.
- **`min()` and `max()`** → Smallest and largest value in the column.
- **`median()`** → The middle value when data is sorted.

Let us see all of them working on one small dataset.

```python
# Import the pandas library, which we always call 'pd' for short
import pandas as pd  # Standard import line for all pandas scripts

# Create a small DataFrame of employees with their salaries
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],  # Employee names
    "Department": ["Sales", "HR", "Sales", "IT", "IT"],          # Which team they belong to
    "Salary":     [40000, 55000, 60000, 75000, 90000]            # Monthly salary in rupees
})

# Print the whole table on screen so we can see it
print(df)  # Shows all rows and columns in the console

# Find the total salary the company is paying every month
total_salary = df["Salary"].sum()  # Scalar: sum of the Salary column
print("Total Salary:", total_salary)  # Label plus number

# Find the average salary across all employees
average_salary = df["Salary"].mean()  # Scalar: mean of Salary
print("Average Salary:", average_salary)  # Label plus number

# Count how many employees we have in total
total_employees = df["Name"].count()  # Non-null names
print("Total Employees:", total_employees)  # Label plus count

# Find the minimum and maximum salary in the company
print("Lowest Salary :", df["Salary"].min())  # Smallest value in Salary
print("Highest Salary:", df["Salary"].max())  # Largest value in Salary

# Middle salary when all salaries are sorted (median)
print("Median Salary :", df["Salary"].median())  # Middle order statistic
```

**How the code works:**

- First we **import pandas as pd**, which loads the library into our program.
- Then we **create a DataFrame** which is like an Excel table with rows and columns.
- `df["Salary"].sum()` picks the Salary column and adds **all** the values together.
- `df["Salary"].mean()` adds all values and divides by how many there are, giving the average.
- `df["Name"].count()` simply counts how many names are present (ignoring empty ones).
- `min()` and `max()` give the smallest and largest salary in the column.
- **`median()`** picks the **middle value** after sorting the column (for an even count, pandas averages the two middle values).

A small doubt students often have: **"What if some values are empty (NaN)?"** By default, pandas **skips NaN** for **`sum`**, **`mean`**, **`median`**, **`min`**, **`max`**, and **`count`** on a Series, which is usually what you want.

## Introduction to groupby

Basic aggregation gave us **one number for the whole column**. But in real life, managers want answers like "average salary **per department**", not just overall average. For this, we need **groupby**.

- **Official Definition:** **`groupby()`** is a pandas method that splits a DataFrame into groups based on unique values in one or more columns, and then lets us apply an aggregation on each group.
- **In Simple Words:** It first **groups similar rows together**, then does the calculation **separately for each group**.
- **Real-Life Example:** Imagine a teacher has marks of 300 students from Class 6, 7, 8, 9, 10. Instead of mixing everyone, she first **makes 5 piles by class**, then finds average marks in each pile. That is exactly what `groupby` does.

This "Split → Apply → Combine" idea is the heart of groupby.

### The Split → Apply → Combine Pattern

Every groupby works in 3 clear steps, so remember this pattern well.

- **Split:** Pandas breaks the big table into many smaller tables, one per unique value in the group column.
- **Apply:** It runs the aggregation (sum/mean/count) on each small table separately.
- **Combine:** It joins all the answers back into one clean summary table.

You can imagine it as sorting laundry: first you **split** clothes by colour (whites, darks, colours), then you **apply** washing to each pile separately, and finally you **combine** everything back into the cupboard.

![groupby: Split → Apply → Combine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session09/split_apply_combine.png)

## groupby with Basic Aggregations

Now let us actually do groupby on our employee data and find answers **per department**.

```python
# Import pandas as pd
import pandas as pd  # Standard short name for the pandas library

# Create the same employee DataFrame as before
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sneha"],  # Employee names
    "Department": ["Sales", "HR", "Sales", "IT", "IT", "HR"],              # Their team
    "Salary":     [40000, 55000, 60000, 75000, 90000, 50000],              # Monthly salary
    "Experience": [2, 5, 3, 7, 9, 4]                                       # Years of experience
})

# Step 1: Split the table by Department (Sales / HR / IT)
grouped = df.groupby("Department")  # Grouped object; no visible output until we aggregate

# Step 2+3: Apply mean on Salary and combine the results
avg_salary_per_dept = grouped["Salary"].mean()  # One mean per department
print("Average Salary per Department:")  # Label for the printed Series
print(avg_salary_per_dept)  # Shows index = Department, values = mean salary

# Count how many employees are in each department
headcount = df.groupby("Department")["Name"].count()  # Non-null names per group
print("\nHeadcount per Department:")  # Blank line prefix in the console output label
print(headcount)  # One count per department

# Total salary the company spends in each department
total_cost = df.groupby("Department")["Salary"].sum()  # Sum of salaries per department
print("\nTotal Salary Cost per Department:")
print(total_cost)  # Series: department → total pay

# Group by TWO columns at the same time (Department + Experience bucket is also possible)
multi_group = df.groupby("Department")[["Salary", "Experience"]].mean()  # Mean of each numeric column per dept
print("\nAverage Salary and Experience per Department:")
print(multi_group)  # DataFrame-style result with two value columns
```

**How the code works:**

- `df.groupby("Department")` creates a **special grouped object**. It does nothing visible yet; it is just waiting for an aggregation.
- `grouped["Salary"].mean()` tells pandas to take **only the Salary column** from each group and calculate its mean.
- `df.groupby("Department")["Name"].count()` counts how many rows belong to each department. This is how we get **headcount**.
- In the last example, we pass **two columns** inside `[["Salary", "Experience"]]`, so pandas computes the mean for **both** columns in every group.
- The output is a small, clean table where the **Department becomes the new index**.

Important small points to keep in mind while using groupby.

- The column we group by becomes the **index** of the output. If you need it as a normal column again (for CSV export, charts, or merges), use **`.reset_index()`**—easy to forget after the first groupby.
- Groupby is very fast even on lakhs of rows because pandas uses optimised C code behind the scenes.
- If the group column has missing values (NaN), those rows are **ignored** by default. You can include them with `dropna=False`.

## Advanced Aggregation with agg

Until now, we used **one aggregation at a time** (only mean, or only sum). But in the real world, a single report usually needs **many aggregations together**, like: "For each department, show me the **total salary, average salary, and number of employees**." For this we use **`agg()`**.

- **Official Definition:** **`agg()`** (short for aggregate) is a method that lets us apply **one or more** aggregation functions on **one or more** columns in a single call.
- **In Simple Words:** Instead of writing three separate groupby lines for sum, mean, and count, we can write **just one** line using `agg`.
- **Real-Life Example:** It is like ordering a **combo meal** at a restaurant. Instead of ordering burger, fries, and cold drink separately, you order one combo and get everything together.

### Using a List of Functions

The simplest form of `agg` is to pass a list like `['sum', 'mean', 'count']`.

```python
# Import pandas
import pandas as pd  # Library import; use any script name except pandas.py

# Same employee data
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sneha"],  # Who
    "Department": ["Sales", "HR", "Sales", "IT", "IT", "HR"],           # Team
    "Salary":     [40000, 55000, 60000, 75000, 90000, 50000],             # Pay
    "Experience": [2, 5, 3, 7, 9, 4]                                     # Years
})

# Apply several aggregations on Salary for each department in one call
salary_report = df.groupby("Department")["Salary"].agg(["sum", "mean", "count", "min", "max"])  # One row per dept

# Print the final report
print(salary_report)  # Columns = one per aggregation function
```

**How the code works:**

- We first do `groupby("Department")` which splits the table department-wise.
- Then `["Salary"]` picks only the salary column for aggregation.
- Inside `.agg([...])` we pass a **list of function names as strings**: sum, mean, count, min, max.
- Pandas runs **each function** on each group and builds a small table with one row per department and one column per function.

### Using a Dictionary for Different Functions on Different Columns

Sometimes we need **different aggregations for different columns**. For example: **sum of Salary**, but **mean of Experience**. For this, we pass a **dictionary** to `agg()`.

```python
# Different aggregation on different columns (reuse df from the previous cell or redefine it)
report = df.groupby("Department").agg({  # One function per column, same groups
    "Salary":     "sum",      # Total salary paid by each department
    "Experience": "mean",     # Average experience in years
    "Name":       "count"     # Number of employees in each department
})

print(report)  # One row per department; columns = Salary, Experience, Name summaries
```

**How the code works:**

- The **key** of the dictionary is the **column name**.
- The **value** is the **function** we want to apply on that column.
- Pandas runs each function on its own column and combines everything into one neat report.

### Naming the Output Columns (Named Aggregation)

By default, the output columns are named `sum`, `mean`, `count`, which is not very user-friendly. We can give our own meaningful names using **named aggregation**.

```python
# Named aggregation: give clear, business-friendly column names
final_report = df.groupby("Department").agg(  # Each kwarg = output column name
    Total_Salary=("Salary", "sum"),       # Sum of Salary → Total_Salary
    Average_Salary=("Salary", "mean"),    # Mean of Salary → Average_Salary
    Headcount=("Name", "count"),          # Count of Name → Headcount
    Avg_Experience=("Experience", "mean") # Mean of Experience → Avg_Experience
)

print(final_report)  # Flat column names; good for sharing with non-technical readers
```

**How the code works:**

- Every line inside `agg()` follows the format `NewColumnName = (existing_column, function)`.
- This is a **tuple** of two things: the column to use, and the function to apply.
- The output looks like a **real management report** with clean column names like Total_Salary, Headcount, etc.

A very common doubt: **"Why does my output have two levels of column names?"** That happens when you use a list of functions. Named aggregation (shown above) avoids that problem because we give a **single clean name** to each output.

## Data Cleanup: Dropping Columns

Sometimes a dataset has columns we simply do not need, like `Unnamed: 0`, blank columns, or sensitive columns we want to hide. We use **`drop()`** to remove them.

- **Official Definition:** **`drop()`** is a method that removes specified rows or columns from a DataFrame.
- **In Simple Words:** It deletes the columns (or rows) that are useless so our table looks clean.
- **Real-Life Example:** It is like **cleaning your WhatsApp** — you delete old forwarded messages and keep only what matters.

```python
# Import pandas
import pandas as pd  # Same import as in every other example

# Create a DataFrame with a few extra useless columns
df = pd.DataFrame({
    "EmployeeID":   [101, 102, 103],           # Primary-style id
    "EmployeeName": ["Aarav", "Diya", "Kabir"],  # Display name
    "Salary":       [40000, 55000, 60000],    # Monthly pay
    "Temp_Col":     ["x", "y", "z"],          # Not useful, just junk data
    "Old_Flag":     [0, 0, 0]                  # Old flag column no longer needed
})

# Show the full DataFrame before dropping
print("Before dropping:")  # Human-readable banner
print(df)  # Full table including junk columns

# Drop a SINGLE column using axis=1 (1 means column, 0 means row)
df = df.drop("Temp_Col", axis=1)  # Returns new frame; assign back to df

# Drop MULTIPLE columns at once by passing a list
df = df.drop(["Old_Flag"], axis=1)  # Could list several names in one go

# Show the DataFrame after cleanup
print("\nAfter dropping:")  # Shows trimmed columns only
print(df)  # EmployeeID, EmployeeName, Salary remain
```

**How the code works:**

- `axis=1` tells pandas we want to drop **columns**. If we wrote `axis=0` it would try to drop a row with that label.
- We can pass a **single column name** as a string, or a **list of column names** to drop many in one shot.
- Like most pandas methods, `drop()` returns a **new** DataFrame by default, so use `df = df.drop(...)` or pass **`inplace=True`** to change the original DataFrame in place.

A very common beginner mistake: they write `df.drop("Temp_Col")` **without `axis=1`**, and pandas raises an error saying the label is not found in index. Always remember **`axis=1` for columns** (or use **`df.drop(columns=["Temp_Col"])`** in newer pandas, which avoids the axis guess).

## Putting It All Together — A Mini Project

Let us combine what we covered into one small workflow on a **single table**: drop what we do not need, then aggregate by group.

```python
# Import pandas
import pandas as pd  # Needed once per script or notebook

# Step 1: Create one employee table (department name is already in the table)
employees = pd.DataFrame({
    "EmployeeID":   [101, 102, 103, 104, 105],                        # Ids
    "EmployeeName": ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],     # Names
    "Department":   ["Sales", "HR", "Sales", "IT", "HR"],              # Group key
    "Salary":       [40000, 55000, 60000, 75000, 90000],               # Pay
    "temp_flag":    [1, 1, 1, 1, 1],                                   # Useless column
})

# Step 2: Clean — remove the useless column
employees = employees.drop("temp_flag", axis=1)  # Lean table for reporting

# Step 3: Aggregate — final management report per department
report = employees.groupby("Department").agg(  # Named agg for readable output
    Headcount=("EmployeeID", "count"),    # Rows per department
    Total_Salary=("Salary", "sum"),       # Spend per department
    Average_Salary=("Salary", "mean"),    # Mean pay per department
)

# Step 4: Print the final report
print("FINAL MANAGEMENT REPORT")  # Title line for console or homework output
print(report)  # Index = Department
```

**How the code works:**

- **Step 1:** We build a DataFrame the usual way; **`Department`** holds the group we want to report on.
- **Step 2:** We **`drop`** the junk column with **`axis=1`**.
- **Step 3:** We **`groupby`** department and use **`agg`** with **named aggregation** for Headcount, Total_Salary, and Average_Salary.
- **Step 4:** We print the report.

Combining **clean** steps with **aggregation** on one table is a pattern you will use constantly; **merging** multiple tables will come in a later session.

## Key Takeaways

- **DataFrames are the core object:** **Create** with `pd.DataFrame`, **load** CSVs with **`pd.read_csv`**, **inspect** with **`head`** / **`tail`**, and **filter** with boolean conditions (use **`&`** / **`|`** with parentheses for multiple tests)—this is the base for all analysis.
- **Aggregation and `groupby`:** **`sum`**, **`mean`**, **`median`**, **`count`**, **`min`**, and **`max`** summarise columns (NaN skipped by default); **`groupby`** gives “per group” answers via **split → apply → combine**; **`agg`** combines several summaries and **named aggregation** keeps column names report-ready.
- **Cleanup and workflow:** Drop junk with **`df.drop(..., axis=1)`** and **reassign** (or **`inplace=True`**); after groupby, use **`.reset_index()`** when you need the group key as a normal column again.
- **What is next:** This session stayed on **one table**. A later session will add **`merge`** and joins so you can combine related tables; until then, practise **read → clean → groupby → agg** until it feels automatic.

## Important Commands, Libraries & Terminologies (Quick Revision)

Use this table as a one-page cheat sheet before your assignments and exams.

| Command | What It Does | Simple Example |
| :--- | :--- | :--- |
| `df["Col"].sum()` | Adds all values in a column | `df["Salary"].sum()` |
| `df["Col"].mean()` | Gives the average of a column | `df["Salary"].mean()` |
| `df["Col"].count()` | Counts non-null values | `df["Name"].count()` |
| `df["Col"].min()` / `.max()` | Smallest / largest value | `df["Salary"].max()` |
| `df["Col"].median()` | Middle value when sorted | `df["Salary"].median()` |
| `df.groupby("Col")` | Splits data into groups by a column | `df.groupby("Department")` |
| `df.groupby("Col")["X"].mean()` | Average of X per group | `df.groupby("Dept")["Salary"].mean()` |
| `df.groupby("Col").agg([...])` | Multiple aggregations at once | `df.groupby("Dept")["Salary"].agg(["sum","mean"])` |
| `df.groupby("Col").agg(New=("X","sum"))` | Named aggregation with clean names | `agg(Total=("Salary","sum"))` |
| `df.drop("Col", axis=1)` | Drops a column | `df.drop("Temp_Col", axis=1)` |
| `df.drop(["C1","C2"], axis=1)` | Drops multiple columns | `df.drop(["A","B"], axis=1)` |
| `pd.read_csv("file.csv")` | Loads a CSV into a DataFrame | After `import pandas as pd` |
| `.reset_index()` | Turns index back into a column | After groupby |
| `import pandas as pd` | Loads pandas (always the first line) | Standard import |

With this, you are ready to **build and inspect** DataFrames, **clean** them by dropping columns, and **summarise** with **groupby** and **`agg`** — a core part of day-to-day analysis in pandas.
