# In-Class Quiz

## Question 1
What is the primary difference between a NumPy array and a Pandas Series?

A. NumPy arrays can hold mixed data types, while Series cannot.

B. Series have a labeled index, while NumPy arrays use integer indices only.

C. Series are multidimensional, while NumPy arrays are always 1D.

D. There is no difference.

**Answer:** B

## Question 2
Which of the following creates a Pandas Series from a Python list `[10, 20]` with index `['a', 'b']`?

A. `pd.Series([10, 20], index=['a', 'b'])`

B. `pd.Series({'a': 10, 'b': 20})`

C. `pd.Series(index=['a', 'b'], data=[10, 20])`

D. All of the above

**Answer:** D (Technically A and C are explicit list constructors, B is dict which results in same structure. D is the best fit as all produce the desired Series output effectively).

## Question 3
If you run `pd.Series(5, index=[1, 2, 3])`, what is the result?

A. An error because data is scalar and index is list.

B. A Series with values [5, 5, 5] and index [1, 2, 3].

C. A Series with value [5] and index [1].

D. A Series with values [1, 2, 3] and index [5, 5, 5].

**Answer:** B


---

# In-Class Quiz

## Question 1
What is the default delimiter used by `pd.read_csv()`?

A. Tab (`\t`)

B. Semicolon (`;`)

C. Comma (`,`)

D. Space (` `)

**Answer:** C

## Question 2
If your CSV file DOES NOT have a header row, which parameter should you pass to avoid using the first row of data as headers?

A. `header=None`

B. `header=False`

C. `skiprows=1`

D. `names=None`

**Answer:** A

## Question 3
Which parameter would you use to set the first column of the CSV as the DataFrame index?

A. `set_index=0`

B. `index_col=0`

C. `use_col=0`

D. `key=0`

**Answer:** B


---

# In-Class Quiz

## Question 1
Which attribute returns a tuple representing the dimensionality of the DataFrame (rows, columns)?

A. `df.size`

B. `df.dim`

C. `df.shape`

D. `df.length`

**Answer:** C

## Question 2
What data type does `df.values` return?

A. A List of Lists.

B. A Dictionary.

C. A NumPy Array.

D. A Series.

**Answer:** C

## Question 3
If `df` has columns `['A', 'B']`, what will `df.columns` return?

A. A list `['A', 'B']`.

B. An Index object containing `['A', 'B']`.

C. A Series of column names.

D. A dictionary of column names.

**Answer:** B (It returns an immutable Index object, which behaves like a list but is optimized).


---

# In-Class Quiz

## Question 1
What is the primary difference between `df.head()` and `df.sample()`?

A. `head()` returns the largest values in the DataFrame, while `sample()` returns the smallest.

B. `head()` returns the first 5 rows, while `sample()` returns 1 randomly selected row.

C. `head()` returns the first 5 rows, while `sample()` returns the last 5 rows.

D. `head()` only works on numerical data, while `sample()` works on all data types.

**Answer:** B

## Question 2
You want to quickly check if any columns in your newly imported DataFrame contain missing (`NaN`) values. Which method provides the most direct summary for this?

A. `df.shape`

B. `df.sample()`

C. `df.info()`

D. `df.head(100)`

**Answer:** C

## Question 3
Which of the following commands will return a tuple representing the total number of rows and columns, such as `(5000, 10)`?

A. `df.shape()`

B. `df.size`

C. `df.dimensions()`

D. `df.shape`

**Answer:** D


---

# In-Class Quiz

## Question 1
Which syntax will successfully select a column named `"First Name"` (with a space)?

A. `df.First Name`

B. `df.'First Name'`

C. `df['First Name']`

D. `df.items('First Name')`

**Answer:** C

## Question 2
If you run `df[['Price']]` (note the double brackets), what is the type of the result?

A. Series

B. DataFrame

C. List

D. NumPy Array

**Answer:** B

## Question 3
Why should you generally avoid using `df.column_name` in production code?

A. It is slower.

B. It breaks if column names change to include spaces or special characters.

C. It is deprecated.

D. It returns a copy instead of a view.

**Answer:** B


---

# In-Class Quiz

## Question 1
If you slice using `.loc['a':'c']`, which labels are included in the result?

A. `a`, `b`

B. `a`, `b`, `c`

C. `a` only

D. Error (`loc` doesn't support slicing)

**Answer:** B

## Question 2
To access the cell value at row `"r1"` and column `"c1"`, which syntax is efficient and correct?

A. `df['c1']['r1']`

B. `df.loc['r1']['c1']`

C. `df.loc['r1', 'c1']`

D. `df.items('r1', 'c1')`

**Answer:** C (Single-shot access is faster than chained indexing).

## Question 3
If `df.loc['X']` raises a `KeyError`, what does it mean?

A. The column 'X' does not exist.

B. The DataFrame is empty.

C. The row index does not contain the label 'X'.

D. You should use `iloc` instead.

**Answer:** C


---

# In-class Quiz

## Question 1
What does `iloc` stand for?

A. Index Location

B. Integer Location

C. Internal Location

D. Iterative Location

**Answer:** B

## Question 2
If you run `df.iloc[0:2]`, how many rows are selected?

A. 1 row (row 0)

B. 2 rows (row 0 and row 1)

C. 3 rows (row 0, row 1, row 2)

D. It depends on the index labels.

**Answer:** B

## Question 3
Which of the following creates an error when used with `.iloc`?

A. `df.iloc[0]`

B. `df.iloc[-1]`

C. `df.iloc['Row_A']`

D. `df.iloc[[0, 1]]`

**Answer:** C


---

# In-Class Quiz

## Question 1
Which of the following best describes the core function of `df.set_index('Column_A')`?

A. It creates a brand new sequence of numeric identifiers (0, 1, 2) and assigns them to 'Column_A'.

B. It automatically sorts the entire DataFrame alphabetically based on the values in 'Column_A'.

C. It extracts 'Column_A' from the main statistical body of the dataset and converts it into the primary row-lookup identifier for the DataFrame.

D. It drops 'Column_A' entirely from memory.

**Answer:** C

## Question 2
You have a DataFrame where the `City` column is currently acting as the Index. You execute `df.reset_index()`. What precisely happens to the `City` data?

A. It is permanently deleted from the DataFrame.

B. It is moved back into the main body of the DataFrame as a standard column.

C. All values inside the index are reset to `NaN`.

D. An error is thrown because only numeric indexes can be reset.

**Answer:** B

## Question 3
You have filtered a massive dataset. The resulting row index is broken and disjointed (`45, 102, 599`). Because these numbers are meaningless to your analysis, you want to build a fresh `(0, 1, 2)` index and completely throw away the old broken numbers. Which keyword argument achieves this?

A. `df.reset_index(inplace=True)`

B. `df.reset_index(delete=True)`

C. `df.set_index(drop=True)`

D. `df.reset_index(drop=True)`

**Answer:** D


---

# In-class Quiz

## Question 1
What does the expression `df['Age'] > 18` return?

A. A new DataFrame with only adults.

B. A Series of True/False values.

C. A list of integers.

D. An error.

**Answer:** B

## Question 2
How do you filter `df` to keep only rows where the 'Status' column is 'Active'?

A. `df['Status' is 'Active']`

B. `df.filter('Status' == 'Active')`

C. `df[df['Status'] == 'Active']`

D. `df.loc['Status' == 'Active']`

**Answer:** C

## Question 3
If `mask` is a boolean Series where **all** values are `False`, what does `df[mask]` return?

A. The original DataFrame.

B. An empty DataFrame.

C. Use of `False` raises an Error.

D. A DataFrame full of `NaN` values.

**Answer:** B


---

# In-class Quiz

## Question 1
Which operator represents logical **AND** in Pandas filtering?

A. `and`

B. `&&`

C. `&`

D. `+`

**Answer:** C

## Question 2
What is the primary reason for wrapping conditions in parentheses? e.g., `(A > 1) & (B < 2)`.

A. To make the code look cleaner.

B. To force Python to evaluate comparisons (`>`) before the logical operator (`&`).

C. To prevent SyntaxErrors.

D. It is optional, not mandatory.

**Answer:** B

## Question 3
Which code selects rows where `Col` is either 10 OR 20?

A. `df[df['Col'] == 10 or 20]`

B. `df[(df['Col'] == 10) | (df['Col'] == 20)]`

C. `df[df['Col'] == 10 & df['Col'] == 20]`

D. `df[df['Col'].is(10, 20)]`

**Answer:** B


---

# In-class Quiz: Sort DataFrame by Values

## Question 1
Which argument in `.sort_values()` is used to specify which column should dictate the order?

A. `on`

B. `col`

C. `by`

D. `target`

**Answer: C**

## Question 2
What is the default sorting direction in Pandas?

A. Ascending (Smallest to Largest)

B. Descending (Largest to Smallest)

C. Random

D. Chronological

**Answer: A**

## Question 3
If you sort a DataFrame and the index labels become scrambled (e.g., 5, 1, 3), which method is used to reset them to a clean 0, 1, 2... sequence?

A. `.clean_index()`

B. `.sort_index()`

C. `.reset_index(drop=True)`

D. `.reindex_rows()`

**Answer: C**


---

# In-Class Quiz

## Question 1
Which of the following is the standard representation for missing data in Pandas?

A. `None`

B. `NaN` (Not a Number)

C. `0`

D. `""` (Empty String)

**Answer: B**

## Question 2
What does `df.isna().sum()` calculate?

A. The total sum of all numeric values in the DataFrame.

B. The sum of all values that are NOT missing.

C. The count of missing (NaN) values for each column.

D. The average number of missing values.

**Answer: C**

## Question 3
True or False: In Python, the comparison `np.nan == np.nan` returns `True`.

A. True

B. False

C. True, but only for strings

D. Depends on the Python version

**Answer: B (NaN is not equal to anything, not even itself).**


---

# In-Class Quiz

## Question 1
Which method is used to replace `NaN` values with a specific constant?

A. `.replace_na()`

B. `.fix_nulls()`

C. `.fillna()`

D. `.put_data()`

**Answer: C**

## Question 2
What is the modern Pandas method for "Forward Filling" missing values?

A. `.fill_forward()`

B. `.fillna(method='ffill')` (Note: This is old syntax)

C. `.ffill()`

D. `.copy_previous()`

**Answer: C (Pandas 2.1+ prefers the direct .ffill() method).**

## Question 3
If you run `df.fillna(0)` without `inplace=True` or assignment, what happens?

A. The column is updated in the original DataFrame.

B. A new DataFrame is returned with the zeros, but the original `df` is unchanged.

C. An error is raised.

D. The zeros are added at the end of the DataFrame.

**Answer: B**


---

# In-Class Quiz

## Question 1
By default, what does `df.dropna()` do?

A. Drops any ROW containing at least one missing value.

B. Drops any COLUMN containing at least one missing value.

C. Drops only rows that are completely empty.

D. Asks the user which row to delete.

**Answer: A**

## Question 2
If you want to drop a row ONLY if every single value in that row is missing, which argument should you use?

A. `how='any'`

B. `how='all'`

C. `subset='all'`

D. `thresh=0`

**Answer: B**

## Question 3
How do you tell the "Bouncer" to only check the 'Email' column for missing values before dropping a row?

A. `df.dropna(column='Email')`

B. `df.dropna(axis=1)`

C. `df.dropna(subset=['Email'])`

D. `df.dropna(target='Email')`

**Answer: C**


---

