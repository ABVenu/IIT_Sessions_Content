# Data Prep: Handling Messy Data

## What We Covered Last Time & What's Coming Today

Last session, we got a clear picture of how a Machine Learning project flows from start to finish. We learned how to frame a real-world problem in ML terms, understood the difference between **features** (inputs) and **labels** (outputs), and practised splitting data into training, validation, and test sets. We also set up simple **baselines** to measure whether our model is actually learning anything useful.

Today, we pick up exactly where we left off — but now we focus on the data itself. Before any ML model can learn, the data it trains on must be clean, consistent, and in the right format. This session is all about that cleanup work:

- Opening a dataset and spotting what's wrong with it
- Fixing missing values using smart techniques
- Removing duplicates and fixing inconsistent entries
- Converting text categories into numbers
- Scaling numbers so they're on the same level
- Making sure our cleanup doesn't accidentally cheat the model
- Measuring the difference our cleanup actually made

---

## Why Data Prep is the Real Work in ML

Here is a truth that surprises most beginners: **data scientists spend about 70–80% of their time cleaning data**, not building models.

Think of it like cooking. Before you cook a meal, you have to wash the vegetables, remove the rotten parts, cut them to the right size, and measure the spices. If you skip that, even the best recipe will produce a bad dish.

In ML, **messy data = bad model predictions**, no matter how fancy your algorithm is. This session gives you the tools to clean your "vegetables" properly.

![Messy raw inputs versus neatly prepped data — data scientists spend most of their time on preparation, like a chef before cooking](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-01-data-prep-foundation.png)

---

## Load and Inspect a Dataset

### Opening the Dataset in Google Colab

We start every data project by loading the dataset and taking a good look at it. You can't fix what you haven't seen.

```python
# Import the pandas library — our main tool for handling data tables
import pandas as pd

# Load the CSV file into a DataFrame (think of it as a spreadsheet in Python)
df = pd.read_csv('sample_data.csv')

# Show the first 5 rows to get a quick look at the data
df.head()
```

**How the code works:**
- `import pandas as pd` — We bring in pandas and nickname it `pd` so we don't have to type the full name every time.
- `pd.read_csv(...)` — This reads your CSV file and stores it as a table (called a **DataFrame**).
- `df.head()` — Shows the first 5 rows. It's like peeking into the file before reading the whole thing.

### Getting a Quick Summary

After loading, we run a few commands to understand the shape and health of the data.

```python
# How many rows and columns does the dataset have?
print(df.shape)

# What are the column names and what type of data is in each?
print(df.info())

# Basic statistics — min, max, average, etc. for number columns
print(df.describe())
```

**How the code works:**
- `df.shape` — Returns `(rows, columns)`. For example, `(500, 8)` means 500 rows and 8 columns.
- `df.info()` — Lists each column, how many values are non-null, and the data type (integer, float, object/text).
- `df.describe()` — Gives you quick stats like average, minimum, and maximum for all numeric columns.

**What to look for during inspection:**
- **Missing values** — Gaps in the data (shown as `NaN`).
- **Wrong data types** — A column that should have numbers but shows up as text.
- **Obvious outliers** — A person's age listed as 500, or a salary listed as -1000.
- **Duplicated rows** — Identical entries repeated more than once.

Think of this step like a doctor's initial check-up — you're taking the patient's pulse before deciding on treatment.

![Load and inspect first — zoom into the table to spot missing cells, odd types, outliers, and duplicate rows before you change anything](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-02-inspect-dataset.png)

---

## Handle Missing Data

### What is Missing Data?

**Missing data** refers to empty cells in a dataset — places where a value should exist but doesn't.

- **In simple words:** It's like a form where someone left a question blank.
- **Real-life example:** Imagine a school attendance register. If a student was absent, their score for that day is blank. You can't just leave it blank forever — you need to decide what to put there.

In Python/pandas, missing values show up as `NaN` (Not a Number).

### Detecting Missing Values

```python
# Count how many values are missing in each column
print(df.isnull().sum())

# See the percentage of missing values per column
print(df.isnull().mean() * 100)
```

**How the code works:**
- `df.isnull()` — Creates a table of True/False. True means the value is missing.
- `.sum()` — Adds up the Trues per column to give you the count of missing values.
- `.mean() * 100` — Converts to a percentage so you know how bad the problem is.

### Filling Missing Values — Imputation

**Imputation** means replacing missing values with a reasonable substitute instead of just deleting the row.

- **Official Definition:** The process of substituting missing data with estimated values derived from the available data.
- **In Simple Words:** Guessing a sensible value to fill the blank.
- **Real-life Example:** If a student missed one exam, you might fill in their score with the class average rather than giving them a zero.

There are three common imputation strategies:

| Strategy | When to Use | Example |
|---|---|---|
| **Mean** | For numeric data with no extreme outliers | Average salary fills a missing salary |
| **Median** | For numeric data with outliers | Middle-value age fills a missing age |
| **Mode** | For categorical (text) data | Most common city fills a missing city |

```python
# Fill missing values in the 'Age' column with the median age
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# Fill missing values in the 'Salary' column with the mean salary
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)

# Fill missing values in the 'City' column with the most common city (mode)
most_common_city = df['City'].mode()[0]
df['City'] = df['City'].fillna(most_common_city)

# Confirm no missing values remain
print(df.isnull().sum())
```

**How the code works:**
- `.median()` / `.mean()` / `.mode()` — Each calculates the respective statistic for that column.
- `.fillna(value)` — Replaces all NaN entries in the column with the given value.
- `mode()[0]` — `.mode()` can return multiple values if there's a tie; `[0]` picks the first one.

**Common doubt:** "Why not just delete rows with missing data?" You can, but if you have a small dataset, deleting rows wastes valuable information. Imputation lets you keep the row while making a sensible guess.

![Mean, median, and mode as three sensible ways to fill gaps — pick the statistic that matches numeric versus categorical columns and the presence of outliers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-03-imputation-strategies.png)

---

## Remove Duplicates and Ensure Consistency

### What are Duplicates?

**Duplicate rows** are records that appear more than once in the dataset with the exact same values.

- **Real-life example:** If the same customer filled out a feedback form twice and both entries got saved, you now have one customer counted as two. This inflates your data and misleads the model.

```python
# Check how many duplicate rows exist
print("Duplicate rows:", df.duplicated().sum())

# Remove all duplicate rows (keep only the first occurrence)
df = df.drop_duplicates()

# Confirm duplicates are gone
print("After removal:", df.duplicated().sum())
```

**How the code works:**
- `df.duplicated()` — Returns True for every row that is an exact copy of a previous row.
- `.sum()` — Counts the duplicates.
- `df.drop_duplicates()` — Removes all duplicate rows, keeping the first occurrence by default.

### Handling Outliers and Inconsistencies

**Outliers** are values that are unrealistically extreme compared to the rest of the data.

- **In simple words:** If 99 people in your dataset earn between ₹20,000 and ₹1,00,000 but one record shows ₹99,00,00,000 — that's an outlier. It could be a genuine billionaire or a data entry mistake.
- **Real-life example:** A person's age listed as 350 years is clearly a mistake, not a billionaire.

```python
# Check for unrealistic values in the 'Age' column
print(df['Age'].describe())

# Remove rows where Age is less than 0 or more than 100
df = df[df['Age'].between(0, 100)]

# Check for negative salaries (which make no sense)
df = df[df['Salary'] >= 0]

# Standardise text inconsistencies in a column (e.g., 'male', 'Male', 'MALE' → 'male')
df['Gender'] = df['Gender'].str.lower().str.strip()
```

**How the code works:**
- `df['Age'].between(0, 100)` — Filters rows where Age is within a logical range.
- `df['Salary'] >= 0` — Keeps only rows with a valid (non-negative) salary.
- `.str.lower()` — Converts all text to lowercase so `'Male'` and `'male'` are treated the same.
- `.str.strip()` — Removes accidental spaces at the start or end of a text value.

![Drop duplicate rows, clip impossible values, and standardise text so the same category is spelled one way — cleaning before modelling](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-04-duplicates-outliers-consistency.png)

---

## Prepare Categorical Data

### What is Categorical Data?

**Categorical data** is data that represents groups or categories — like gender, city, or product type.

- **In simple words:** It's text labels, not numbers.
- **Real-life example:** In a shop's customer database, the "Payment Method" column might have entries like "Cash", "UPI", "Credit Card". These are categories.

The problem is that **ML models only understand numbers**. They cannot do maths with the word "Cash". So we must convert these text categories into numerical values before feeding the data to a model.

This conversion is called **Encoding**.

```python
# See which columns have text/categorical data
print(df.select_dtypes(include='object').columns)

# Count unique values in each categorical column to understand variety
print(df['City'].value_counts())
```

**How the code works:**
- `select_dtypes(include='object')` — Selects only the columns that contain text (object type in pandas).
- `.value_counts()` — Shows how many times each unique value appears in a column.

---

## Apply Encoding Techniques

Now that we know which columns need encoding, let's apply the two most common techniques.

### Label Encoding

**Label Encoding** assigns a unique number to each category.

- **Official Definition:** A technique that converts each unique category value into a unique integer.
- **In simple words:** It's like giving roll numbers to students. "Delhi" becomes 0, "Mumbai" becomes 1, "Chennai" becomes 2.
- **Real-life example:** Imagine a colour-coding system at a hospital where "Emergency" = 1, "Normal" = 2, "Routine" = 3.

**When to use:** Best for columns where categories have a natural order — like "Low", "Medium", "High".

```python
# Import the LabelEncoder tool from sklearn
from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder object
le = LabelEncoder()

# Apply label encoding to the 'Education' column (Low=0, Medium=1, High=2)
df['Education_encoded'] = le.fit_transform(df['Education'])

# See how the encoding looks
print(df[['Education', 'Education_encoded']].head())
```

**How the code works:**
- `LabelEncoder()` — Creates an encoder object that will learn the categories.
- `fit_transform(df['Education'])` — Learns the unique values and immediately converts them to numbers.
- The result is stored in a new column `Education_encoded` so the original is preserved for reference.

### One-Hot Encoding

**One-Hot Encoding** creates a separate column for each category and marks it with 0 or 1.

- **Official Definition:** A technique that creates binary (0/1) indicator columns for each category in a feature.
- **In simple words:** Instead of one "City" column with values like Delhi or Mumbai, you get a separate column for each city. A row for Delhi gets 1 in the "City_Delhi" column and 0 everywhere else.
- **Real-life example:** A restaurant menu checkbox — instead of writing "Pizza" in one box, you have separate checkboxes for "Pizza: Yes/No", "Burger: Yes/No", "Pasta: Yes/No".

**When to use:** Best for columns where categories have **no natural order** — like City, Gender, Payment Method.

```python
# Apply one-hot encoding to the 'City' column
df = pd.get_dummies(df, columns=['City'], drop_first=True)

# See the new columns created
print(df.head())
```

**How the code works:**
- `pd.get_dummies(df, columns=['City'])` — Creates a new binary column for each unique city.
- `drop_first=True` — Drops the first category column to avoid a statistical problem called **multicollinearity** (having two columns that are perfectly predictable from each other).

**Common doubt:** "Which encoding should I use?" Use **Label Encoding** when there's a ranking/order. Use **One-Hot Encoding** when categories are just labels with no ranking.

![Label encoding maps ordered categories to a single number line; one-hot encoding gives each category its own binary column for unordered labels](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-05-label-vs-onehot.png)

---

## Apply Feature Scaling

### Why Does Scale Matter?

Imagine your dataset has two columns:
- `Age` — values between 20 and 60
- `Salary` — values between ₹20,000 and ₹1,00,000

The Salary column has numbers 1000 times larger than Age. If you feed this to an ML model, the model might assume Salary is "more important" simply because its numbers are bigger — not because it actually carries more information.

**Feature Scaling** brings all numerical columns to a comparable range so the model doesn't get biased by the size of numbers.

### Normalisation (Min-Max Scaling)

**Normalisation** squeezes all values into a range of 0 to 1.

- **Official Definition:** A scaling technique that transforms data to fit within [0, 1] by subtracting the minimum and dividing by the range.
- **In simple words:** The smallest value becomes 0, the largest becomes 1, and everything else falls in between proportionally.
- **Real-life example:** Converting exam marks from a 1000-mark scale to a 10-point GPA scale.

```python
# Import MinMaxScaler from sklearn
from sklearn.preprocessing import MinMaxScaler

# Create a scaler object
scaler = MinMaxScaler()

# Apply normalisation to the 'Age' and 'Salary' columns
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# Check the result — all values should now be between 0 and 1
print(df[['Age', 'Salary']].describe())
```

### Standardisation (Z-Score Scaling)

**Standardisation** transforms data so it has a mean of 0 and a standard deviation of 1.

- **Official Definition:** A scaling technique that subtracts the mean and divides by the standard deviation.
- **In simple words:** It tells you how far each value is from the average — values above average are positive, values below are negative.
- **Real-life example:** UPSC rank percentiles — your rank is expressed relative to the average performance, not as an absolute number.

```python
# Import StandardScaler from sklearn
from sklearn.preprocessing import StandardScaler

# Create a scaler object
std_scaler = StandardScaler()

# Apply standardisation to 'Age' and 'Salary' columns
df[['Age', 'Salary']] = std_scaler.fit_transform(df[['Age', 'Salary']])

# Check the result — mean should be close to 0, std close to 1
print(df[['Age', 'Salary']].describe())
```

**How the code works:**
- `StandardScaler()` — Creates a scaler that uses mean and standard deviation.
- `fit_transform(...)` — Learns the mean and std from the data, then transforms it in one step.

| Technique | Output Range | Use When |
|---|---|---|
| **Normalisation** | 0 to 1 | You need values in a fixed range (e.g., neural networks) |
| **Standardisation** | No fixed range, centred at 0 | You have outliers or need relative comparison |

![Feature scaling balances columns so a huge numeric range does not drown out a small one — the model compares signal, not digit size](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-06-feature-scaling.png)

---

## Prevent Data Leakage in Preprocessing

### What is Data Leakage?

**Data leakage** happens when information from the test set "leaks" into the training process — giving the model an unfair advantage during evaluation.

- **In simple words:** It's like a student seeing the exam paper before the exam. Their marks will be great, but they haven't actually learned anything.
- **Real-life example:** If you calculate the average salary using the entire dataset (including test data) and use that to fill missing values, the model has indirectly "seen" the test data during training.

### The Correct Way to Scale Without Leakage

```python
# Import the train_test_split function
from sklearn.model_selection import train_test_split

# Split the data FIRST, before any fitting
X = df.drop('Target', axis=1)   # Features (all columns except the label)
y = df['Target']                  # Label column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the scaler
scaler = StandardScaler()

# ONLY fit on training data — learn the mean and std from training set only
X_train_scaled = scaler.fit_transform(X_train)

# ONLY transform (do not re-fit) on test data — use the training mean and std
X_test_scaled = scaler.transform(X_test)
```

**How the code works:**
- `train_test_split` — Splits features and labels into training and testing portions.
- `scaler.fit_transform(X_train)` — The scaler **learns** statistics (mean, std) from training data and scales it.
- `scaler.transform(X_test)` — Applies the **same statistics learned from training** to the test data. We do NOT call `fit` again on test data.

**Why this matters:** If you fit the scaler on test data too, the scaler learns from test data, and your evaluation metrics will be falsely optimistic.

![Split train and test first, then fit preprocessors only on training — apply the same learned transform to test so evaluation stays honest](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-07-data-leakage-split.png)

---

## Evaluate the Impact of Data Preparation

After all the cleaning, it's important to see whether the work actually made a difference.

```python
# Compare shape before and after
print("Rows before cleaning: 500")
print("Rows after cleaning:", df.shape[0])

# Check that no missing values remain
print("Missing values remaining:", df.isnull().sum().sum())

# Summary statistics after cleaning
print(df.describe())
```

A simple side-by-side comparison tells you:
- How many rows were lost (due to duplicate removal or outlier filtering)
- Whether missing values are fully handled
- Whether your numerical columns are now on a reasonable scale

Think of this as the "before and after" photo of your dataset. A clean dataset means the model starts its training on a solid foundation.

---

## Key Takeaways

- **Messy data is the norm, not the exception.** Real-world data always comes with missing values, duplicates, and inconsistencies. Data prep is not optional — it is the foundation of any ML project.
- **Imputation preserves your data.** Instead of deleting rows with missing values, use mean, median, or mode to fill gaps intelligently based on the type of data.
- **Encoding converts language into numbers.** Use Label Encoding for ordered categories and One-Hot Encoding for unordered ones — because ML models only speak numbers.
- **Scaling levels the playing field.** Normalisation and standardisation ensure that columns with large numeric ranges don't dominate columns with smaller ones.
- **Always split before you scale.** Fitting your scaler or imputer only on training data prevents data leakage and keeps your model evaluation honest.

In the next sessions, we move on to actually training ML models on this clean, well-prepared data — and you'll see firsthand why clean data leads to better predictions.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Means |
|---|---|
| `pandas` (`pd`) | Python library for handling and analysing tabular data |
| `df.head()` | Displays the first 5 rows of the DataFrame |
| `df.info()` | Shows column names, data types, and non-null counts |
| `df.describe()` | Summary statistics for numerical columns |
| `df.isnull().sum()` | Counts missing values per column |
| `df.fillna(value)` | Fills missing values with a specified value |
| `df.drop_duplicates()` | Removes duplicate rows from the DataFrame |
| `df.duplicated()` | Returns True for rows that are duplicates |
| `LabelEncoder` | Converts categorical text into integer labels |
| `pd.get_dummies()` | Applies one-hot encoding to categorical columns |
| `MinMaxScaler` | Scales values to the range [0, 1] |
| `StandardScaler` | Scales values to have mean=0 and std=1 |
| `fit_transform()` | Learns from data and transforms it in one step |
| `transform()` | Applies a previously learned transformation (no learning) |
| `train_test_split` | Splits dataset into training and testing portions |
| **Imputation** | Filling in missing data with a calculated substitute |
| **Label Encoding** | Assigning a unique number to each category |
| **One-Hot Encoding** | Creating binary columns for each category value |
| **Normalisation** | Scaling values to fall between 0 and 1 |
| **Standardisation** | Scaling values to have mean 0 and standard deviation 1 |
| **Data Leakage** | When test data information accidentally influences training |
| **Outlier** | A value that is unrealistically far from the rest of the data |
| **NaN** | "Not a Number" — Python's representation of a missing value |
| **DataFrame** | A table-like data structure in pandas |
