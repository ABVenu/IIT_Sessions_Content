# **Assignment: The EDA Checklist**

---

## **Question 1. (MCQ)**

What is the primary goal of Exploratory Data Analysis (EDA)?

A) Train machine learning models
B) Understand and investigate the dataset before modeling
C) Deploy models to production
D) Optimize algorithms

**Correct answer:** B

**Explanation:**
EDA is performed before modeling to understand the dataset’s structure, detect anomalies, inspect distributions, and identify relationships between variables. This helps avoid incorrect assumptions and modeling errors.

---

## **Question 2. (MCQ)**

Which Pandas command is commonly used to preview the first few rows of a dataset?

A) `df.describe()`
B) `df.head()`
C) `df.info()`
D) `df.shape()`

**Correct answer:** B

**Explanation:**
`df.head()` displays the first five rows by default. This helps quickly inspect the structure and values of the dataset.

---

## **Question 3. (MCQ)**

What information does `df.info()` primarily provide?

A) Graphical plots of the dataset
B) DataFrame structure including column types and non-null counts
C) Summary statistics
D) Correlation values

**Correct answer:** B

**Explanation:**
`df.info()` displays the number of rows, column names, data types, and counts of non-null values, helping identify missing data and incorrect types.

---

## **Question 4. (MCQ)**

What does the command `df.isnull().sum()` help identify?

A) Duplicate rows
B) Missing values per column
C) Correlation between variables
D) Data distribution

**Correct answer:** B

**Explanation:**
`df.isnull()` produces a Boolean DataFrame identifying missing values. Applying `.sum()` counts them per column, which is critical for assessing dataset completeness.

---

## **Question 5. (MCQ)**

Which visualization is commonly used to inspect missing values across a dataset?

A) Scatter plot
B) Heatmap
C) Bar chart
D) Line chart

**Correct answer:** B

**Explanation:**
A heatmap of missing values helps visualize where missing data occurs and whether it clusters within certain columns.

---

## **Question 6. (MCQ)**

What is the main purpose of plotting a histogram of a variable?

A) Identify correlations between variables
B) Examine the distribution of values
C) Remove missing values
D) Sort data

**Correct answer:** B

**Explanation:**
Histograms show how values are distributed across ranges. They help detect skewness, unusual spikes, and potential outliers.

---

## **Question 7. (MCQ)**

Which plot type is commonly used to detect potential outliers?

A) Line plot
B) Pie chart
C) Box plot
D) Heatmap

**Correct answer:** C

**Explanation:**
Box plots highlight the median, quartiles, and extreme values. Points outside the whiskers often represent potential outliers.

---

## **Question 8. (MCQ)**

What does a correlation matrix represent?

A) The number of rows in a dataset
B) Pairwise relationships between numeric variables
C) Missing value counts
D) Data types of columns

**Correct answer:** B

**Explanation:**
A correlation matrix shows how strongly pairs of variables move together. It is often visualized with a heatmap to identify patterns and relationships useful for feature engineering.

---

## **Question 9. (Subjective)**

### **EDA Pipeline for Dataset Investigation**

You are given a dataset named `sales_data.csv`. Your task is to perform a basic Exploratory Data Analysis following the workflow described in the lecture.

### **Tasks**

Write a Python script that performs the following steps:

1. Load the dataset using Pandas.
2. Inspect the dataset using:

   * `df.head()`
   * `df.info()`
   * `df.describe()`
3. Check missing values using:

   * `df.isnull().sum()`
4. Visualize missing values using a **Seaborn heatmap**.
5. Plot the **distribution of the `revenue` column** using a histogram.
6. Detect potential outliers in `revenue` using a **box plot**.
7. Compute the **correlation matrix**.
8. Visualize the correlation matrix using a **heatmap**.

Ensure each visualization includes a **title**.

---

# ✅ **Solution**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Inspect dataset structure
print(df.head())
print(df.info())
print(df.describe())

# Step 3: Check missing values
print(df.isnull().sum())

# Step 4: Visualize missing data
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Data Map")
plt.show()

# Step 5: Distribution of revenue
df["revenue"].hist()
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# Step 6: Outlier detection with boxplot
sns.boxplot(x=df["revenue"])
plt.title("Revenue Outlier Detection")
plt.show()

# Step 7: Correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# Step 8: Correlation heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```