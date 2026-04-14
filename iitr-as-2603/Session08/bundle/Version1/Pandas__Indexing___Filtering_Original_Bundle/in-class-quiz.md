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
You want to create a Series of length 5 where every value is `0`. Which code is correct?

A. `pd.Series(0)`

B. `pd.Series(0, index=range(5))`

C. `pd.Series([0])`

D. `pd.Series(5, data=0)`

**Answer:** B

## Question 2
Given `d = {'a': 100, 'b': 200}` and `idx = ['b', 'c']`. What is the result of `pd.Series(d, index=idx)`?

A. `b: 200, c: 100`

B. `b: 200, c: NaN`

C. `b: 200, c: 0`

D. Error

**Answer:** B

## Question 3
When creating a Series from a NumPy array, what is the default behavior regarding memory?

A. It always copies the data.

B. It acts as a reference (view) where possible for efficiency.

C. It converts values to strings.

D. It reverses the array.

**Answer:** B


---

# In-Class Quiz

## Question 1
Given `s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])`. What does `s['b':'c']` return?

A. `b: 20`

B. `b: 20, c: 30`

C. `b: 20, c: NaN`

D. Error

**Answer:** B

## Question 2
Given `s = pd.Series([100, 200], index=[1, 0])`. What does `s[0]` return?

A. 100

B. 200

C. Error

D. It depends on the Pandas version.

**Answer:** B (Pandas prioritizes label lookups for integer indexes. Since `0` is a label in the index, it returns the value associated with label `0`, which is 200).

## Question 3
Which syntax is guaranteed to retrieve the **first** element of a Series by specific position, regardless of index labels?

A. `s[0]`

B. `s.loc[0]`

C. `s.iloc[0]`

D. `s.get(0)`

**Answer:** C


---

# In-Class Quiz

## Question 1
What is the result of `pd.Series([10, 20]) + 5`?

A. `[10, 20, 5]`

B. `[15, 25]`

C. `[15, 20]`

D. Error

**Answer:** B

## Question 2
Given `s1 = pd.Series([1, 2], index=['a', 'b'])` and `s2 = pd.Series([3, 4], index=['b', 'a'])`. What is `s1 + s2`?

A. `a: 4, b: 6`

B. `a: 5, b: 5`

C. `a: 13, b: 24`

D. `a: NaN, b: NaN`

**Answer:** B (Aligns 'a' with 'a': 1+4=5, 'b' with 'b': 2+3=5).

## Question 3
If you add two Series and one index label is present in `s1` but missing in `s2`, what is the result for that label?

A. It keeps the value from `s1`.

B. It acts as if `s2` had a 0.

C. It becomes `NaN`.

D. It throws an error.

**Answer:** C


---

# In-Class Quiz

## Question 1
When creating a DataFrame from a dictionary of lists (e.g., `{'a': [1, 2], 'b': [3, 4]}`), what do the dictionary keys represent?

A. The Index labels.

B. The Column data types.

C. The Column names.

D. The Row values.

**Answer:** C

## Question 2
What happens if you try to create a DataFrame from `{'A': [1, 2, 3], 'B': [1, 2]}`?

A. It pads column B with NaN.

B. It acts like a database join.

C. It throws a `ValueError` because arrays must be same length.

D. It truncates column A.

**Answer:** C (Standard behavior for Dict of Lists constructor implies strict length check).

## Question 3
If you create a DataFrame from a list of dictionaries `[{'a': 1}, {'b': 2}]`, what will the result look like?

A. Two columns 'a' and 'b', with `NaN` where data is missing.

B. One column 'a'.

C. An error.

D. Two rows, where 'a' is 1 and 'b' is 2, but indices are mismatched.

**Answer:** A


---

# In-Class Quiz

## Question 1
When creating a DataFrame from a list of lists `[[1, 2], [3, 4]]`, how does Pandas interpret the inner lists?

A. As Columns.

B. As Rows.

C. As Diagonals.

D. It depends on the `axis` parameter.

**Answer:** B

## Question 2
If you do not provide the `columns` argument when creating a DataFrame from a NumPy array of shape (3, 3), what will the column labels be?

A. 'A', 'B', 'C'

B. 1, 2, 3

C. 0, 1, 2

D. NaN, NaN, NaN

**Answer:** C (RangeIndex default).

## Question 3
You have a list `data = [10, 20, 30]`. `pd.DataFrame(data)` creates:

A. A 1-row, 3-column DataFrame.

B. A 3-row, 1-column DataFrame.

C. A Series.

D. An error.

**Answer:** B (Pandas treats a single flat list as a column in a DataFrame context).


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

# In-class Quiz

## Question 1
Which syntax matches the "Scalar Broadcasting" concept?

A. `df['Col'] = [1, 2, 3]`

B. `df['Col'] = 5`

C. `df['Col'] = df['OldCol'] + 1`

D. `df.Col = 5`

**Answer:** B

## Question 2
Why does `df.NewColumn = 10` fail to create a column?

A. Pandas does not support integer assignment.

B. Dot notation is restricted to reading data, not writing.

C. Dot notation creates a Python object attribute, not a DataFrame column.

D. It actually works fine.

**Answer:** C

## Question 3
If `df` has 10 rows, which assignment will raise a ValueError?

A. `df['A'] = range(10)`

B. `df['A'] = [1, 2]`

C. `df['A'] = 0`

D. `df['A'] = df['B'] * 2`

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

# In-class Quiz

## Question 1
What is the default behavior of `df.drop('ColA', axis=1)`?

A. It deletes 'ColA' from `df` immediately.

B. It returns a new DataFrame with 'ColA' removed, leaving `df` unchanged.

C. It raises a warning confirming the deletion.

D. It returns True if successful.

**Answer:** B

## Question 2
How do you delete the **first row** (index 0) of a DataFrame?

A. `df.drop(columns=0)`

B. `df.drop(index=0)`

C. `del df[0]`

D. `df.remove(0)`

**Answer:** B

## Question 3
Which command modifies the DataFrame **in-place**, without needing reassignment?

A. `df.drop('A', axis=1)`

B. `df = df.drop('A', axis=1)`

C. `del df['A']`

D. `df.delete('A')`

**Answer:** C


---

# In-Class Quiz

## Question 1
Which argument in the `.rename()` method is used to modify column headers?

A. `labels=`

B. `index=`

C. `columns=`

D. `names=`

**Answer: C**

## Question 2
True or False: By default, `df.rename(...)` modifies the original DataFrame permanently without needing to be assigned to a variable.

A. True

B. False

C. Only if the DataFrame is empty

D. Both A and B

**Answer: B (It returns a new copy unless `inplace=True` is used).**

## Question 3
If you want to rename a column named `'Score'` to `'Final_Grade'`, which dictionary is correct?

A. `{'Score': 'Final_Grade'}`

B. `{'Final_Grade': 'Score'}`

C. `['Score', 'Final_Grade']`

D. `('Score', 'Final_Grade')`

**Answer: A (Old Name is the Key, New Name is the Value).**


---

# In-Class Quiz

## Question 1
In the "Split-Apply-Combine" strategy, what does the "Apply" step usually refer to?

A. Applying a filter to the rows.

B. Applying an aggregation function (like .mean() or .sum()).

C. Applying a new name to the columns.

D. Applying the data to a chart.

**Answer:** B

## Question 2
What is returned immediately after calling `df.groupby('Column_Name')` without an aggregation function?

A. A summary DataFrame.

B. A Python list of groups.

C. A DataFrameGroupBy object (Lazy object).

D. An Error.

**Answer:** C

## Question 3
If you want to find the total sales for each 'City', which code is correct?

A. `df.groupby('Sales').sum('City')`

B. `df.groupby('City')['Sales'].sum()`

C. `df.groupby('City').Sales()`

D. `df.sum().groupby('City')`

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

# In-class Quiz: Sort DataFrame by Index

## Question 1
Which method is used to reorder a DataFrame based on its row labels?

A. `.sort_values()`

B. `.sort_index()`

C. `.reset_index()`

D. `.reorder()`

**Answer: B**

## Question 2
To sort column names alphabetically instead of row labels, which argument must you change?

A. `by=1`

B. `columns=True`

C. `axis=1`

D. `direction='horizontal'`

**Answer: C**

## Question 3
True or False: By default, `sort_index()` modifies the original DataFrame permanently without needing to assign it to a variable.

A. True

B. False

**Answer: B** (Modern Pandas returns a new sorted object; the original is unchanged unless you use `inplace=True` or reassign the result).


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

