# Pandas: Aggregation & Combining Data

Welcome to the session. In our last class, we learned how to load data, clean missing values, and filter rows. Today, we take the next big step: we will **summarise** huge datasets into meaningful numbers and **combine** information from different tables, just like a manager prepares a report from many Excel sheets.

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
import pandas as pd

# Create a small DataFrame of employees with their salaries
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],  # Employee names
    "Department": ["Sales", "HR", "Sales", "IT", "IT"],          # Which team they belong to
    "Salary":     [40000, 55000, 60000, 75000, 90000]            # Monthly salary in rupees
})

# Print the whole table on screen so we can see it
print(df)

# Find the total salary the company is paying every month
total_salary = df["Salary"].sum()
print("Total Salary:", total_salary)

# Find the average salary across all employees
average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)

# Count how many employees we have in total
total_employees = df["Name"].count()
print("Total Employees:", total_employees)

# Find the minimum and maximum salary in the company
print("Lowest Salary :", df["Salary"].min())
print("Highest Salary:", df["Salary"].max())
```

**How the code works:**

- First we **import pandas as pd**, which loads the library into our program.
- Then we **create a DataFrame** which is like an Excel table with rows and columns.
- `df["Salary"].sum()` picks the Salary column and adds **all** the values together.
- `df["Salary"].mean()` adds all values and divides by how many there are, giving the average.
- `df["Name"].count()` simply counts how many names are present (ignoring empty ones).
- `min()` and `max()` give the smallest and largest salary in the column.

A small doubt students often have: **"What if some values are empty (NaN)?"** By default, pandas **ignores NaN** while doing sum/mean/count, which is very safe behaviour.

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
import pandas as pd

# Create the same employee DataFrame as before
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sneha"],  # Employee names
    "Department": ["Sales", "HR", "Sales", "IT", "IT", "HR"],              # Their team
    "Salary":     [40000, 55000, 60000, 75000, 90000, 50000],              # Monthly salary
    "Experience": [2, 5, 3, 7, 9, 4]                                       # Years of experience
})

# Step 1: Split the table by Department (Sales / HR / IT)
grouped = df.groupby("Department")

# Step 2+3: Apply mean on Salary and combine the results
avg_salary_per_dept = grouped["Salary"].mean()
print("Average Salary per Department:")
print(avg_salary_per_dept)

# Count how many employees are in each department
headcount = df.groupby("Department")["Name"].count()
print("\nHeadcount per Department:")
print(headcount)

# Total salary the company spends in each department
total_cost = df.groupby("Department")["Salary"].sum()
print("\nTotal Salary Cost per Department:")
print(total_cost)

# Group by TWO columns at the same time (Department + Experience bucket is also possible)
multi_group = df.groupby("Department")[["Salary", "Experience"]].mean()
print("\nAverage Salary and Experience per Department:")
print(multi_group)
```

**How the code works:**

- `df.groupby("Department")` creates a **special grouped object**. It does nothing visible yet; it is just waiting for an aggregation.
- `grouped["Salary"].mean()` tells pandas to take **only the Salary column** from each group and calculate its mean.
- `df.groupby("Department")["Name"].count()` counts how many rows belong to each department. This is how we get **headcount**.
- In the last example, we pass **two columns** inside `[["Salary", "Experience"]]`, so pandas computes the mean for **both** columns in every group.
- The output is a small, clean table where the **Department becomes the new index**.

Important small points to keep in mind while using groupby.

- The column we group by becomes the **index** of the output. If you want it as a normal column again, use **`.reset_index()`**.
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
import pandas as pd

# Same employee data
df = pd.DataFrame({
    "Name":       ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Sneha"],
    "Department": ["Sales", "HR", "Sales", "IT", "IT", "HR"],
    "Salary":     [40000, 55000, 60000, 75000, 90000, 50000],
    "Experience": [2, 5, 3, 7, 9, 4]
})

# Apply THREE aggregations on the Salary column for each department
salary_report = df.groupby("Department")["Salary"].agg(["sum", "mean", "count", "min", "max"])

# Print the final report
print(salary_report)
```

**How the code works:**

- We first do `groupby("Department")` which splits the table department-wise.
- Then `["Salary"]` picks only the salary column for aggregation.
- Inside `.agg([...])` we pass a **list of function names as strings**: sum, mean, count, min, max.
- Pandas runs **each function** on each group and builds a small table with one row per department and one column per function.

### Using a Dictionary for Different Functions on Different Columns

Sometimes we need **different aggregations for different columns**. For example: **sum of Salary**, but **mean of Experience**. For this, we pass a **dictionary** to `agg()`.

```python
# Different aggregation on different columns
report = df.groupby("Department").agg({
    "Salary":     "sum",      # Total salary paid by each department
    "Experience": "mean",     # Average experience in years
    "Name":       "count"     # Number of employees in each department
})

print(report)
```

**How the code works:**

- The **key** of the dictionary is the **column name**.
- The **value** is the **function** we want to apply on that column.
- Pandas runs each function on its own column and combines everything into one neat report.

### Naming the Output Columns (Named Aggregation)

By default, the output columns are named `sum`, `mean`, `count`, which is not very user-friendly. We can give our own meaningful names using **named aggregation**.

```python
# Named aggregation: give clear, business-friendly column names
final_report = df.groupby("Department").agg(
    Total_Salary=("Salary", "sum"),       # Sum of Salary → Total_Salary
    Average_Salary=("Salary", "mean"),    # Mean of Salary → Average_Salary
    Headcount=("Name", "count"),          # Count of Name → Headcount
    Avg_Experience=("Experience", "mean") # Mean of Experience → Avg_Experience
)

print(final_report)
```

**How the code works:**

- Every line inside `agg()` follows the format `NewColumnName = (existing_column, function)`.
- This is a **tuple** of two things: the column to use, and the function to apply.
- The output looks like a **real management report** with clean column names like Total_Salary, Headcount, etc.

A very common doubt: **"Why does my output have two levels of column names?"** That happens when you use a list of functions. Named aggregation (shown above) avoids that problem because we give a **single clean name** to each output.

## Data Cleanup: Renaming Columns

Real data rarely comes with clean names. You will often see columns like `emp_id`, `EMP NAME`, `sal_$`, or even `Unnamed: 0`. Before showing reports to anyone, we must **rename** them.

- **Official Definition:** **`rename()`** is a method that changes the names of rows (index) or columns of a DataFrame using a dictionary of old-to-new names.
- **In Simple Words:** It helps us give **proper, readable names** to our columns.
- **Real-Life Example:** It is like labelling boxes while shifting to a new house. Instead of "Box 1, Box 2", you write "Kitchen", "Books", "Clothes", so you can find things easily later.

```python
# Import pandas
import pandas as pd

# Create a messy DataFrame with bad column names
df = pd.DataFrame({
    "emp_id":  [101, 102, 103],
    "EMP NAME": ["Aarav", "Diya", "Kabir"],
    "sal_$":   [40000, 55000, 60000]
})

# Print the original messy columns
print("Before renaming:")
print(df.columns)

# Rename the columns using a dictionary: {old_name: new_name}
df = df.rename(columns={
    "emp_id":   "EmployeeID",
    "EMP NAME": "EmployeeName",
    "sal_$":    "Salary"
})

# Print the cleaned-up columns
print("\nAfter renaming:")
print(df.columns)
print(df)
```

**How the code works:**

- `df.rename(columns={...})` does **not** change the original DataFrame by default; it returns a **new** one.
- That is why we do `df = df.rename(...)` to save the change back into `df`.
- If you want to change the original directly, you can pass `inplace=True`.
- Only the columns you **mention** in the dictionary are renamed. The rest stay as they are.

A small best practice: use **short, lowercase, underscore-separated names** like `employee_id`, `employee_name`, `salary`. They are easier to type and never break your code.

## Data Cleanup: Dropping Columns

Sometimes a dataset has columns we simply do not need, like `Unnamed: 0`, blank columns, or sensitive columns we want to hide. We use **`drop()`** to remove them.

- **Official Definition:** **`drop()`** is a method that removes specified rows or columns from a DataFrame.
- **In Simple Words:** It deletes the columns (or rows) that are useless so our table looks clean.
- **Real-Life Example:** It is like **cleaning your WhatsApp** — you delete old forwarded messages and keep only what matters.

```python
# Import pandas
import pandas as pd

# Create a DataFrame with a few extra useless columns
df = pd.DataFrame({
    "EmployeeID":   [101, 102, 103],
    "EmployeeName": ["Aarav", "Diya", "Kabir"],
    "Salary":       [40000, 55000, 60000],
    "Temp_Col":     ["x", "y", "z"],      # Not useful, just junk data
    "Old_Flag":     [0, 0, 0]             # Old flag column no longer needed
})

# Show the full DataFrame before dropping
print("Before dropping:")
print(df)

# Drop a SINGLE column using axis=1 (1 means column, 0 means row)
df = df.drop("Temp_Col", axis=1)

# Drop MULTIPLE columns at once by passing a list
df = df.drop(["Old_Flag"], axis=1)

# Show the DataFrame after cleanup
print("\nAfter dropping:")
print(df)
```

**How the code works:**

- `axis=1` tells pandas we want to drop **columns**. If we wrote `axis=0` it would try to drop a row with that label.
- We can pass a **single column name** as a string, or a **list of column names** to drop many in one shot.
- Just like rename, `drop()` also returns a **new** DataFrame by default, so we reassign it using `df = df.drop(...)`.
- You can also use `inplace=True` if you want to modify the original DataFrame directly.

A very common beginner mistake: they write `df.drop("Temp_Col")` **without `axis=1`**, and pandas raises an error saying the label is not found in index. Always remember **`axis=1` for columns**.

## Introduction to Combining Data

So far we worked with only **one table**. But real companies store data in **multiple tables**. For example, one table for Employees, another for Departments, another for Salaries. To get a full picture, we must **combine** these tables. This is where `merge` and `join` come in.

- **Official Definition:** **Merging / Joining** is the process of combining two DataFrames into one based on a common column or index.
- **In Simple Words:** It is like **matching rows** from two tables using a shared column (like EmployeeID) and then putting them side by side.
- **Real-Life Example:** Think of an Aadhaar card and a PAN card. Both belong to the same person (shared column = Name or DOB). If we join them on "Name", we get **full details** of the person in a single view.

This idea is exactly how SQL JOINs work, and pandas borrows the same concept.

## Combining Data with merge

**`pd.merge()`** is the main tool in pandas to combine two tables. It is powerful, flexible, and works just like SQL joins.

### The Four Types of Joins

The real skill in merge is choosing the **right type of join**. There are mainly 4.

- **inner join** → Keeps only rows that match in **both** tables (intersection).
- **left join** → Keeps **all** rows of the left table, plus matching rows from the right.
- **right join** → Keeps **all** rows of the right table, plus matching rows from the left.
- **outer join** → Keeps **all** rows from both tables (union), fills missing with NaN.

Think of it like two circles in a Venn diagram: inner is the overlap, outer is the full picture, and left/right keep one full circle intact.

![SQL-style joins: inner, left, right, and outer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session09/sql_joins_types.png)

### Inner Join Example

```python
# Import pandas
import pandas as pd

# First table: Employees and their Department IDs
employees = pd.DataFrame({
    "EmployeeID":   [101, 102, 103, 104],
    "Name":         ["Aarav", "Diya", "Kabir", "Meera"],
    "DepartmentID": [1, 2, 1, 3]                           # Foreign key to Departments
})

# Second table: Department IDs and their Names
departments = pd.DataFrame({
    "DepartmentID":   [1, 2, 4],                           # Note: 3 is missing, 4 is extra
    "DepartmentName": ["Sales", "HR", "Finance"]
})

# INNER JOIN: Only employees whose DepartmentID exists in departments table
inner = pd.merge(employees, departments, on="DepartmentID", how="inner")
print("Inner Join:")
print(inner)
```

**How the code works:**

- `pd.merge(left, right, on="DepartmentID", how="inner")` takes both tables and matches rows where **DepartmentID is the same**.
- Because `how="inner"`, only matching rows stay. Meera (Dept 3) is dropped because Dept 3 is missing in the departments table.
- The extra row (Dept 4 = Finance) is also dropped because no employee belongs to it.
- The common column `DepartmentID` appears **only once** in the output.

### Left Join Example

```python
# LEFT JOIN: Keep ALL employees, even if their Department is missing
left = pd.merge(employees, departments, on="DepartmentID", how="left")
print("Left Join:")
print(left)
```

**How the code works:**

- All 4 employees are kept, because the **left** table is given priority.
- Meera's DepartmentName will be **NaN** because Dept 3 is not present in the departments table.
- This is the **most commonly used join in real projects**, because we usually want to keep the main table complete.

### Right Join and Outer Join

```python
# RIGHT JOIN: Keep ALL departments, even those without employees
right = pd.merge(employees, departments, on="DepartmentID", how="right")
print("Right Join:")
print(right)

# OUTER JOIN: Keep EVERYTHING from both tables
outer = pd.merge(employees, departments, on="DepartmentID", how="outer")
print("\nOuter Join:")
print(outer)
```

**How the code works:**

- **Right join** keeps every department. Finance has no employee, so Name and EmployeeID become **NaN** for that row.
- **Outer join** is the **biggest possible result**. It includes every employee and every department. Missing matches are filled with NaN on either side.
- Outer join is useful when we want to **find what is missing** in either table.

### Merging on Columns with Different Names

Sometimes the common column has **different names** in the two tables. For that, we use `left_on` and `right_on`.

```python
# Suppose employees has 'DeptID' but departments has 'DepartmentID'
employees2 = employees.rename(columns={"DepartmentID": "DeptID"})

# Use left_on and right_on to match columns with different names
merged = pd.merge(
    employees2, departments,
    left_on="DeptID",           # Column name in the left table
    right_on="DepartmentID",    # Column name in the right table
    how="inner"
)

print(merged)
```

**How the code works:**

- `left_on` tells pandas which column to use from the **first (left)** DataFrame.
- `right_on` tells pandas which column to use from the **second (right)** DataFrame.
- Both columns will appear in the output; you can drop one later using `.drop()` if not needed.

## Introduction to join

Apart from `merge()`, pandas also gives us another handy method called **`.join()`**. We will not go deep into it today — just understand the **basic idea**, because we will explore it more in future sessions that is in the SQL session.

- **Official Definition:** **`DataFrame.join()`** is a method that combines two DataFrames by aligning them on their **index** (row labels) by default.
- **In Simple Words:** If two tables already share the **same row labels** (like the same EmployeeIDs as index), `join()` is a quick, short way to glue them **side by side**.
- **Real-Life Example:** It is like two notebooks with the **same page numbers**. If you hold them together page-wise, every page of Notebook A automatically pairs up with the same page of Notebook B.

A very small peek at how it looks in code:

```python
# info and salary are two DataFrames, both indexed by EmployeeID
combined = info.join(salary)   # Glues them side by side on the index
```

That is all you need to know about `join()` for now. Just remember:

- **`merge()`** is used when we combine tables using a **column** (most common case, and what we focused on today).
- **`join()`** is a shortcut mainly used when we combine tables using the **index**.

We will see detailed examples and differences between `merge` and `join` in the upcoming sessions.

## Putting It All Together — A Mini Mini Project

Let us combine everything we learned today into one small, realistic workflow. This is how a Data Analyst would actually work in an office.

```python
# Import pandas
import pandas as pd

# Step 1: Create the Employees table
employees = pd.DataFrame({
    "emp_id":       [101, 102, 103, 104, 105],
    "emp_name":     ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],
    "dept_id":      [1, 2, 1, 3, 2],
    "sal_$":        [40000, 55000, 60000, 75000, 90000],
    "temp_flag":    [1, 1, 1, 1, 1]                                # Useless column
})

# Step 2: Create the Departments table
departments = pd.DataFrame({
    "dept_id":   [1, 2, 3],
    "dept_name": ["Sales", "HR", "IT"]
})

# Step 3: Clean up the employees table
employees = employees.rename(columns={nowd
    "emp_id":   "EmployeeID",
    "emp_name": "EmployeeName",
    "sal_$":    "Salary"
})
employees = employees.drop("temp_flag", axis=1)   # Remove useless column

# Step 4: Merge employees with departments to get department names
merged = pd.merge(employees, departments, on="dept_id", how="left")

# Step 5: Aggregate — final management report per department
report = merged.groupby("dept_name").agg(
    Headcount=("EmployeeID", "count"),
    Total_Salary=("Salary", "sum"),
    Average_Salary=("Salary", "mean")
)

# Step 6: Print the final report
print("FINAL MANAGEMENT REPORT")
print(report)
```

**How the code works:**

- **Step 1 & 2:** We create two raw tables, just like they would come from a database.
- **Step 3:** We clean bad column names using `rename`, and drop the useless `temp_flag` column using `drop`.
- **Step 4:** We `merge` the two tables on `dept_id` using a **left join**, so every employee gets a department name.
- **Step 5:** We `groupby` the department name and use `agg` with **named aggregation** to create a clean report with Headcount, Total_Salary, and Average_Salary.
- **Step 6:** We print the final report that a manager can directly read and take decisions on.

This small flow — **Clean → Combine → Aggregate** — is literally **80% of the daily work** of a Data Analyst.

## Common Doubts and Mistakes to Avoid

Let us quickly go through the mistakes that beginners almost always make in these topics.

- **Forgetting `axis=1` in `drop()`:** Without it, pandas thinks you want to drop a row.
- **Using `and` / `or` instead of `&` / `|`:** Only bitwise operators work on pandas Series.
- **Not reassigning the result:** Most pandas methods (`rename`, `drop`, `sort_values`) return a **new** DataFrame. Either use `df = df.rename(...)` or pass `inplace=True`.
- **Mixing up `merge` and `concat`:** `merge` matches on a **key column** (horizontal join), while `concat` just **stacks** tables on top of each other.
- **Getting NaN after a left join:** This is **not an error**. It means the key did not exist in the right table. Use `fillna()` or investigate the data.
- **Forgetting `reset_index()` after groupby:** The grouped column becomes the index. If you want it as a normal column again, use `.reset_index()`.

## Important Commands & Libraries (Quick Revision)

Use this table as a one-page cheat sheet before your assignments and exams.

| Command | What It Does | Simple Example |
| :--- | :--- | :--- |
| `df["Col"].sum()` | Adds all values in a column | `df["Salary"].sum()` |
| `df["Col"].mean()` | Gives the average of a column | `df["Salary"].mean()` |
| `df["Col"].count()` | Counts non-null values | `df["Name"].count()` |
| `df["Col"].min()` / `.max()` | Smallest / largest value | `df["Salary"].max()` |
| `df.groupby("Col")` | Splits data into groups by a column | `df.groupby("Department")` |
| `df.groupby("Col")["X"].mean()` | Average of X per group | `df.groupby("Dept")["Salary"].mean()` |
| `df.groupby("Col").agg([...])` | Multiple aggregations at once | `df.groupby("Dept")["Salary"].agg(["sum","mean"])` |
| `df.groupby("Col").agg(New=("X","sum"))` | Named aggregation with clean names | `agg(Total=("Salary","sum"))` |
| `df.rename(columns={old: new})` | Renames columns | `df.rename(columns={"sal_$":"Salary"})` |
| `df.drop("Col", axis=1)` | Drops a column | `df.drop("Temp_Col", axis=1)` |
| `df.drop(["C1","C2"], axis=1)` | Drops multiple columns | `df.drop(["A","B"], axis=1)` |
| `pd.merge(df1, df2, on="Key", how="inner")` | Matches rows in both tables | Inner join |
| `how="left"` | Keeps all rows of left table | Most common join |
| `how="right"` | Keeps all rows of right table | Used for reference data |
| `how="outer"` | Keeps all rows of both tables | Used to find missing data |
| `pd.merge(..., left_on=, right_on=)` | Merge when key names differ | `left_on="DeptID", right_on="DepartmentID"` |
| `df1.join(df2)` | Shortcut to combine tables on the **index** (introduction only) | `info.join(salary)` |
| `.reset_index()` | Turns index back into a column | After groupby |
| `import pandas as pd` | Loads pandas (always the first line) | Standard import |

With this, you are now ready to **clean**, **combine**, and **summarise** any real-world dataset in pandas — which is exactly what a professional Data Analyst does every single day.
