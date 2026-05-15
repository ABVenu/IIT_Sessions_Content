# Data Prep: Handling Messy Data

## What We Covered Last Time & What's Coming Today

Last session, we got a clear picture of how a Machine Learning project flows from start to finish. We learned how to frame a real-world problem in ML terms, understood the difference between **features** (inputs) and **labels** (outputs), and practised splitting data into training, validation, and test sets. We also set up simple **baselines** to measure whether our model is actually learning anything useful.

Today, we pick up exactly where we left off — but now we focus on the data itself. Before any ML model can learn, the data it trains on must be clean, consistent, and in the right format. This session is all about that cleanup work:

- Opening a dataset and spotting what's wrong with it
- Fixing values that break common sense before you impute or encode
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

### Starting with the Session DataFrames

We start every data project by loading the dataset and taking a good look at it. You can't fix what you haven't seen.

In this session we worked with three sample tables in the class notebook — **`df_car`** (used-car listings with brand, year, fuel, kilometres driven, and price), **`df_student`** (student marks, attendance, and grades), and **`df_ecom`** (simple e-commerce orders with product, quantity, and price). The same inspection ideas apply whether you open a notebook locally or in a cloud environment such as Google Colab.

```python
# Import the pandas library — our main tool for handling data tables
import pandas as pd

# Load a CSV file into a DataFrame (think of it as a spreadsheet in Python)
df_car = pd.read_csv('car_data.csv')

# Show the first 5 rows to get a quick look at the data
df_car.head()
```

**How the code works:**
- `import pandas as pd` — We bring in pandas and nickname it `pd` so we don't have to type the full name every time.
- `pd.read_csv(...)` — This reads your CSV file and stores it as a table (called a **DataFrame**).
- `df_car.head()` — Shows the first 5 rows. It's like peeking into the file before reading the whole thing.

### Getting a Quick Summary

After loading, we run a few commands to understand the shape and health of the data.

```python
# How many rows and columns does the dataset have?
print(df_car.shape)

# What are the column names and what type of data is in each?
print(df_car.info())

# Basic statistics — min, max, average, etc. for number columns
print(df_car.describe())
```

**How the code works:**
- `df_car.shape` — Returns `(rows, columns)`. For example, `(500, 8)` means 500 rows and 8 columns.
- `df_car.info()` — Lists each column, how many values are non-null, and the data type (integer, float, object/text).
- `df_car.describe()` — Gives you quick stats like average, minimum, and maximum for all numeric columns.

**What to look for during inspection:**
- **Missing values** — Gaps in the data (shown as `NaN`).
- **Wrong data types** — A column that should have numbers but shows up as text.
- **Obvious outliers** — A person's age listed as 500, or a salary listed as -1000.
- **Duplicated rows** — Identical entries repeated more than once.

Think of this step like a doctor's initial check-up — you're taking the patient's pulse before deciding on treatment.

![Load and inspect first — zoom into the table to spot missing cells, odd types, outliers, and duplicate rows before you change anything](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-02-inspect-dataset.png)

---

## Fix Logically Incorrect Values First

Before you fill missing cells or build a model, fix values that **cannot be true** in the real world. Data cleaning is iterative — you often spot one layer of problems, fix them, and then move to the next step.

- **In simple words:** A negative car price or a grade of `-10` is not a "missing number" problem yet — it is a **logic** problem.
- **Real-life example:** On a used-car marketplace, price and kilometres driven must be non-negative. A grade column should only hold labels like A, B, or C.

```python
# Car data: a negative price is likely a sign error — take the absolute value
df_car['price'] = df_car['price'].abs()

# Student data: an impossible grade becomes unknown, so replace with NaN for later imputation
import numpy as np
df_student['grade'] = df_student['grade'].replace(-10, np.nan)

# E-commerce data: same idea for a negative product price
df_ecom['price'] = df_ecom['price'].abs()
```

**How the code works:**
- `.abs()` — Turns negative numbers positive while leaving valid positive values unchanged.
- `replace(-10, np.nan)` — Marks a value that does not belong in the column as missing so you can impute it later.
- This **level-one cleaning** uses domain sense; only after it do we run systematic missing-value and duplicate steps.

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
print(df_car.isnull().sum())

# See the percentage of missing values per column
print(df_car.isnull().mean() * 100)
```

**How the code works:**
- `df_car.isnull()` — Creates a table of True/False. True means the value is missing.
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
# Fill missing values in the 'kilometers_driven' column with the median
median_km = df_car['kilometers_driven'].median()
df_car['kilometers_driven'] = df_car['kilometers_driven'].fillna(median_km)

# Fill missing values in a numeric marks column with the mean
mean_marks = df_student['marks'].mean()
df_student['marks'] = df_student['marks'].fillna(mean_marks)

# Fill missing values in the 'grade' column with the most common grade (mode)
most_common_grade = df_student['grade'].mode()[0]
df_student['grade'] = df_student['grade'].fillna(most_common_grade)

# Confirm no missing values remain in the columns you treated
print(df_car.isnull().sum())
```

**How the code works:**
- `.median()` / `.mean()` / `.mode()` — Each calculates the respective statistic for that column.
- `.fillna(value)` — Replaces all NaN entries in the column with the given value.
- `mode()[0]` — `.mode()` can return multiple values if there's a tie; `[0]` picks the first one.

**Common doubt:** "Why not just delete rows with missing data?" You can, but if you have a small dataset, deleting rows wastes valuable information. Imputation lets you keep the row while making a sensible guess.

### When Mean Imputation Is Not Enough

For a column like **offered salary**, filling every blank with the column mean can distort the story when experience and exam marks also matter. In practice, teams sometimes **predict** the missing salary from other features (for example experience and marks) using a simple model, then use that prediction as the imputed value. That idea is more advanced than mean or median fill, but it shows why imputation is a design choice — not a single button.

![Mean, median, and mode as three sensible ways to fill gaps — pick the statistic that matches numeric versus categorical columns and the presence of outliers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-03-imputation-strategies.png)

---

## Remove Duplicates and Ensure Consistency

### What are Duplicates?

**Duplicate rows** are records that appear more than once in the dataset with the exact same values.

- **Real-life example:** If the same customer filled out a feedback form twice and both entries got saved, you now have one customer counted as two. This inflates your data and misleads the model.

```python
# Check how many duplicate rows exist
print("Duplicate rows:", df_car.duplicated().sum())

# Remove all duplicate rows (keep only the first occurrence)
df_car = df_car.drop_duplicates()

# Confirm duplicates are gone
print("After removal:", df_car.duplicated().sum())
```

**How the code works:**
- `df_car.duplicated()` — Returns True for every row that is an exact copy of a previous row.
- `.sum()` — Counts the duplicates.
- `df_car.drop_duplicates()` — Removes all duplicate rows, keeping the first occurrence by default.

### Spotting Bad Values During Consistency Checks

**Outliers** are values that are unrealistically extreme compared to the rest of the data. In class we did not run a separate outlier-removal recipe; we **spotted** odd values during inspection and fixed impossible entries with domain rules (such as negative prices) before modelling.

- **In simple words:** If 99 car listings show sensible prices but one row shows a negative price, treat it as a data-quality issue first — not as a value to average into the model.
- **Real-life example:** A grade of `-10` is not an outlier to clip — it is invalid text stored in the wrong place, so it becomes `NaN` and is handled in the imputation step.

![Drop duplicate rows, clip impossible values, and standardise text so the same category is spelled one way — cleaning before modelling](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-04-duplicates-outliers-consistency.png)

---

## Prepare Categorical Data

### What is Categorical Data?

**Categorical data** is data that represents groups or categories — like brand, fuel type, or product name.

- **In simple words:** It's text labels, not numbers.
- **Real-life example:** In a shop's customer database, the "Payment Method" column might have entries like "Cash", "UPI", "Credit Card". These are categories.

The problem is that **ML models only understand numbers**. They cannot do maths with the word "Cash". So we must convert these text categories into numerical values before feeding the data to a model.

This conversion is called **Encoding**. Columns with a **natural order** (ordinal) are handled differently from columns that are just labels (nominal).

```python
# See which columns have text/categorical data
print(df_car.select_dtypes(include='object').columns)

# Count unique values in a categorical column to understand variety
print(df_car['fuel'].value_counts())
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

**When to use:** Best for **ordinal** columns where categories have a natural order — like "Low", "Medium", "High".

```python
# Import the LabelEncoder tool from scikit-learn (sklearn)
from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder object
le = LabelEncoder()

# Apply label encoding to an ordered education column (Low=0, Medium=1, High=2)
df_student['education_encoded'] = le.fit_transform(df_student['education'])

# See how the encoding looks
print(df_student[['education', 'education_encoded']].head())
```

**How the code works:**
- `LabelEncoder()` — Creates an encoder object that will learn the categories.
- `fit_transform(df_student['education'])` — Learns the unique values and immediately converts them to numbers.
- The result is stored in a new column so the original is preserved for reference.

### One-Hot Encoding

**One-Hot Encoding** creates a separate column for each category and marks it with 0 or 1.

- **Official Definition:** A technique that creates binary (0/1) indicator columns for each category in a feature.
- **In simple words:** Instead of one "fuel" column with values like Petrol or Diesel, you get a separate column for each fuel type. A Petrol row gets 1 in the Petrol column and 0 elsewhere.
- **Real-life example:** A restaurant menu checkbox — instead of writing "Pizza" in one box, you have separate checkboxes for "Pizza: Yes/No", "Burger: Yes/No", "Pasta: Yes/No".

**When to use:** Best for **nominal** columns where categories have **no natural order** — like brand or fuel type.

```python
# Apply one-hot encoding to nominal columns such as brand and fuel
df_car = pd.get_dummies(df_car, columns=['brand', 'fuel'], drop_first=True)

# See the new columns created
print(df_car.head())
```

**How the code works:**
- `pd.get_dummies(df_car, columns=['brand', 'fuel'])` — Creates a new binary column for each unique category in those columns.
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

**Feature Scaling** brings all numerical columns to a comparable range so the model doesn't get biased by the size of numbers. Apply scaling to **numeric features only** — not to raw text categories before encoding.

### Normalisation (Min-Max Scaling)

**Normalisation** squeezes all values into a range of 0 to 1.

- **Official Definition:** A scaling technique that transforms data to fit within [0, 1] by subtracting the minimum and dividing by the range.
- **In simple words:** The smallest value becomes 0, the largest becomes 1, and everything else falls in between proportionally.
- **Real-life example:** Converting exam marks from a 1000-mark scale to a 10-point GPA scale.

The formula used in class was:

**scaled value = (value − min) ÷ (max − min)**

```python
# Import MinMaxScaler from scikit-learn
from sklearn.preprocessing import MinMaxScaler

# Create a scaler object
scaler = MinMaxScaler()

# Apply normalisation to numeric columns such as age and salary
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

# Check the result — all values should now be between 0 and 1
print(df[['age', 'salary']].describe())
```

**How the code works:**
- `MinMaxScaler()` — Creates a scaler that learns each column's minimum and maximum.
- `fit_transform(...)` — Learns those bounds from the data and rescales in one step.
- After scaling, compare the table **before and after** so you can see every value sitting on the 0–1 range.

### Standardisation (Z-Score Scaling)

**Standardisation** transforms data so it has a mean of 0 and a standard deviation of 1.

- **Official Definition:** A scaling technique that subtracts the mean and divides by the standard deviation.
- **In simple words:** It tells you how far each value is from the average — values above average are positive, values below are negative.
- **Real-life example:** UPSC rank percentiles — your rank is expressed relative to the average performance, not as an absolute number.

In class we focused on **min–max scaling** with the formula above and `MinMaxScaler`. **`StandardScaler`** is the other common scikit-learn option when you want z-score scaling instead of a fixed 0–1 range.

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

### The Correct Way to Preprocess Without Leakage

```python
# Import the train_test_split function
from sklearn.model_selection import train_test_split

# Split the data FIRST, before any fitting
X = df.drop('target', axis=1)   # Features (all columns except the label)
y = df['target']                  # Label column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the scaler (MinMaxScaler or StandardScaler — same fit/transform pattern)
scaler = MinMaxScaler()

# ONLY fit on training data — learn min/max (or mean/std) from training set only
X_train_scaled = scaler.fit_transform(X_train)

# ONLY transform (do not re-fit) on test data — use the training statistics
X_test_scaled = scaler.transform(X_test)
```

**How the code works:**
- `train_test_split` — Splits features and labels into training and testing portions (for example 80% train, 20% test).
- `scaler.fit_transform(X_train)` — The scaler **learns** from training data only and scales it.
- `scaler.transform(X_test)` — Applies the **same learned transform** to the test data. We do NOT call `fit` again on test data.

**Why this matters:** If you fit the scaler on test data too, the scaler learns from test data, and your evaluation metrics will be falsely optimistic. Clean and scale **feature columns (X)** after the split, not the label.

![Split train and test first, then fit preprocessors only on training — apply the same learned transform to test so evaluation stays honest](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session14/session14-07-data-leakage-split.png)

---

## Evaluate the Impact of Data Preparation

After all the cleaning, it's important to see whether the work actually made a difference. In class we compared tables **before and after** each major step — fixing impossible values, imputing, dropping duplicates, encoding, and scaling — rather than running a separate modelling benchmark.

```python
# Store a snapshot before cleaning (or keep the original DataFrame aside)
rows_before = df.shape[0]

# ... run your cleaning, imputation, duplicate removal, encoding, and scaling steps ...

# Compare row count and missing values after the pipeline
print("Rows before cleaning:", rows_before)
print("Rows after cleaning:", df.shape[0])
print("Missing values remaining:", df.isnull().sum().sum())
print(df.describe())
```

A simple side-by-side comparison tells you:
- How many rows were lost (for example after duplicate removal)
- Whether missing values are fully handled in the columns you targeted
- Whether your numerical columns are now on a reasonable scale

Think of this as the "before and after" photo of your dataset. A clean dataset means the model starts its training on a solid foundation.

---

## Key Takeaways

- **Messy data is the norm, not the exception.** Real-world data always comes with missing values, duplicates, and inconsistencies. Data prep is not optional — it is the foundation of any ML project.
- **Fix impossible values before you impute.** Use domain sense (for example absolute value for a negative price, or `NaN` for an invalid grade) so later steps work on trustworthy inputs.
- **Imputation preserves your data.** Use mean, median, or mode based on column type; advanced cases can predict a missing target from other features.
- **Encoding converts language into numbers.** Use label encoding for ordered categories and one-hot encoding for unordered ones — because ML models only speak numbers.
- **Scaling levels the playing field.** Min–max scaling to 0–1 was our main technique; fit preprocessors only on training data after a train–test split so evaluation stays honest.

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
| `.abs()` | Returns the absolute (non-negative) value of a number |
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
