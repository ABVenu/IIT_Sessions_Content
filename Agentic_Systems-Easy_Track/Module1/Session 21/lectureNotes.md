# The EDA Checklist

## What You’ll Learn

In this lesson, you’ll learn the structured process of **Exploratory Data Analysis (EDA)**. You’ll understand the standard steps used to investigate datasets, how to detect outliers, how to analyze relationships using correlation heatmaps, and how to translate raw observations into a coherent data story. EDA is one of the most important phases in any data science or AI project because it reveals how the data behaves before modeling begins.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/d3d70d7b-5e67-45b9-8906-199345da2386/LSupvjkM0ViLwGgj.png)


---

## 1. Why Exploratory Data Analysis Matters

Before building any machine learning model, you must understand the dataset. Models cannot compensate for flawed assumptions about the data.

EDA helps answer questions like:

- What does the dataset actually contain?
- Are there missing values or anomalies?
- How are variables distributed?
- Which variables are related?
- Are there patterns that might influence modeling?

In professional AI workflows, EDA prevents costly mistakes such as:
- training on corrupted data
- ignoring critical variables
- overlooking data leakage
- misinterpreting model results

EDA is not a single step—it is a **systematic investigation process**.

---

## 2. The Standard EDA Workflow

Most EDA processes follow a structured checklist. While the details vary, the core steps remain consistent.

### Step 1: Understand the Dataset

Start by inspecting the dataset structure.

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()
df.info()
df.describe()
````

These commands help answer:

* How many rows and columns exist?
* What are the data types?
* Are there missing values?
* What are the basic statistics?

Understanding the structure prevents incorrect assumptions later.

---

### Step 2: Inspect Missing Values

Missing values can bias analysis or break models.

```python
df.isnull().sum()
```

Visualization helps as well:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Data Map")
plt.show()
```

Key questions:

* Are missing values random?
* Do they cluster around certain columns?
* Should they be removed or filled?

---

### Step 3: Examine Distributions

Understanding how variables are distributed is critical.

```python
df["age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

Distributions reveal:

* skewness
* unusual spikes
* potential outliers
* scale differences

Many models perform better when variables follow reasonable distributions.

---

## 3. Identifying Outliers

Outliers are data points that differ significantly from others. They may represent:

* genuine rare events
* measurement errors
* data entry mistakes

Outliers can strongly influence models, especially regression models.

---

### Using Box Plots

```python
sns.boxplot(x=df["salary"])
plt.title("Salary Distribution")
plt.show()
```

Box plots highlight:

* median
* quartiles
* extreme values

Points outside the whiskers often indicate potential outliers.

---

### Statistical Detection

One common rule uses the **interquartile range (IQR)**.

```python
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["salary"] < Q1 - 1.5 * IQR) |
              (df["salary"] > Q3 + 1.5 * IQR)]
```

Outliers should not automatically be removed. Investigate them first.

---

## 4. Correlation Analysis

Understanding relationships between variables is essential for feature selection and model interpretation.

Correlation measures how strongly variables move together.

---

### Correlation Matrix

```python
corr_matrix = df.corr()
print(corr_matrix)
```

This produces pairwise correlation values between numeric columns.

---

### Correlation Heatmap

A heatmap visualizes correlations more clearly.

```python
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

Heatmaps help identify:

* strongly related variables
* redundant features
* potential predictors of the target variable

In AI workflows, correlation analysis helps guide feature engineering.

---

## 5. Building a Data Story

EDA is not just about producing charts. The goal is to **develop a narrative about the data**.

A strong data story answers:

* What patterns exist?
* What anomalies were discovered?
* What relationships are meaningful?
* What assumptions should models consider?

Example narrative:

> “Customer purchase frequency is strongly correlated with account age. However, high-value transactions contain significant outliers, likely representing enterprise clients.”

This interpretation guides modeling decisions and communicates insights to stakeholders.

---

## 6. A Complete EDA Example

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# Inspect structure
print(df.info())

# Check missing values
print(df.isnull().sum())

# Distribution
df["revenue"].hist()
plt.title("Revenue Distribution")
plt.show()

# Outlier detection
sns.boxplot(x=df["revenue"])
plt.show()

# Correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()
```

This simple pipeline reveals:

* dataset structure
* missing values
* distributions
* outliers
* relationships

These insights shape how models are built.

---

## 7. Common EDA Mistakes

* Jumping straight into modeling
* Ignoring missing values
* Overlooking outliers
* Misinterpreting correlations
* Producing charts without interpretation

EDA requires curiosity and critical thinking, not just code execution.

---

## Key Takeaways

Exploratory Data Analysis is a structured process for understanding datasets before modeling. It includes inspecting structure, identifying missing values, examining distributions, detecting outliers, and analyzing correlations. The ultimate goal is to develop a clear narrative about the data that informs modeling decisions and prevents analytical mistakes.

**Mental model:**
Inspect the data.
Clean the anomalies.
Understand relationships.
Tell the story.

---

## Additional Reading

* Google Machine Learning Crash Course (Data Exploration):
  [https://developers.google.com/machine-learning/crash-course/data-prep/feature-engineering](https://developers.google.com/machine-learning/crash-course/data-prep/feature-engineering)

* Pandas Data Exploration Guide:
  [https://pandas.pydata.org/docs/user_guide/basics.html](https://pandas.pydata.org/docs/user_guide/basics.html)

* Seaborn Statistical Visualization:
  [https://seaborn.pydata.org/tutorial.html](https://seaborn.pydata.org/tutorial.html)