# Pre-read: Pandas Indexing, Filtering, and Missing Data in Real Work

When people start working with data in Python, loading a file feels like the main task. In real work, that is only the starting point.  
The real value comes from how confidently you inspect, filter, and clean data before making any conclusions.

Most business datasets are messy by default. One column has missing values, one field has mixed formats, and some rows are not useful for your objective.  
If this early data handling is weak, even a well-written model or dashboard can produce unreliable output.

Imagine your manager asks for a quick salary analysis from a CSV file.  
Now imagine that file has missing ages, extra rows, and inconsistent columns.  
If you manually scan row by row, you lose time and still risk reporting wrong insights.

This session gives you a reliable workflow for handling exactly these situations using Pandas.

You will learn how to:

- read CSV files correctly
- inspect DataFrame structure quickly
- select rows and columns precisely
- filter with one or multiple conditions
- sort and manage index flow
- detect and handle missing values with clear logic

Think of a DataFrame like a city map:

- the **index** works like row addresses
- the **columns** are named routes for each data field
- the **values** are the actual points you need to analyze

If you do not understand the map structure, you can still move - but you can easily take wrong turns.  
Pandas helps you navigate with two important tools:

- **`loc`**: select by labels (names/index labels)
- **`iloc`**: select by positions (row number/column number)

This difference looks small, but it prevents many silent errors when datasets grow.

You will also practice fast inspection checks that professionals run immediately after loading data:

- `head()`, `tail()`, `sample()` for quick visual sanity checks
- `shape` for row-column dimensions
- `info()` for types and non-null counts

These checks answer practical questions early:

- Are headers mapped correctly?
- Are numeric columns truly numeric?
- Where are missing values concentrated?

Filtering is another core skill in this session, because most business queries are filter queries:

- which records meet a performance threshold?
- which users belong to specific segments?
- which rows satisfy multiple conditions together?

You will apply boolean logic cleanly using `&`, `|`, and parentheses, and avoid common logic mistakes that lead to wrong subsets.

You will also learn how sorting and index control improve analysis readability:

- `sort_values()` for ranking and ordering
- `set_index()` to promote a meaningful identifier
- `reset_index()` to flatten index when needed

Then we move to one of the most common real-world data issues: missing values.

You will learn three practical strategies:

- **identify** missing values (`isna`, `notna`)
- **fill** missing values (`fillna`, `ffill`, mean-based fill)
- **drop** missing records when required (`dropna`)

There is no one universal rule here.  
The right strategy depends on column meaning, data context, and how the output will be used.

By the end of this session, your process should become structured and repeatable:

1. Load data correctly.
2. Inspect before transforming.
3. Select and filter with precision.
4. Handle missing values intentionally.
5. Validate structure again before analysis.

## Questions we will crack in class

1. When should you use `loc` vs `iloc`, and how can mixing them create hidden errors?
2. How do you combine multiple filter conditions without breaking logic?
3. How do you decide whether to fill missing data or drop it?
4. How do quick checks like `shape` and `info()` prevent downstream mistakes?

## After this session, you will be able to

- Load CSV files into Pandas with the right parsing options.
- Inspect DataFrame structure confidently using shape, columns, index, and dtypes.
- Select rows and columns accurately using brackets, `loc`, and `iloc`.
- Apply single and multi-condition filters using reliable boolean logic.
- Sort and re-index data for cleaner and more interpretable workflows.
- Detect and handle missing values using `isna`, `fillna`, and `dropna` with reasoning.

Come with one mindset: not just to run Pandas commands, but to build clean, trustworthy data tables that support correct decisions.