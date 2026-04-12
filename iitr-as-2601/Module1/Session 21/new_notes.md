# The EDA Checklist

## Learning Objective

Master the process of **Exploratory Data Analysis (EDA)** — the systematic process of understanding a dataset before building machine learning models.

In real-world data science projects, a large portion of time is spent **exploring and understanding the data** rather than immediately training models.

A typical AI workflow looks like this:

![AI Workflow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-ai-workflow.png)

```
Data Collection
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
```

EDA helps analysts understand:

* what information exists in the dataset
* whether the data is clean and usable
* whether unusual or extreme values exist
* which features might influence the target variable

Without proper EDA, machine learning models may learn **incorrect or misleading patterns**.

---

# Dataset Used in This Session

We will use the **Titanic passenger dataset**, a well-known dataset used for learning data analysis and machine learning.

Goal:
Understand which passenger characteristics influenced **survival on the Titanic**.

Possible useful features:

* Age
* Sex
* Passenger class
* Fare paid

Target variable:

* Survived (0 = No, 1 = Yes)

---

# Loading the Dataset

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.head()
```

---

# Standard EDA Steps

Data scientists typically follow a structured process when exploring a new dataset.

A common EDA workflow includes:

![EDA Workflow Steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-workflow-steps.png)

```
1. Understand the dataset structure
2. Inspect data quality
3. Study distributions
4. Detect unusual values (outliers)
5. Analyze relationships between variables
6. Build insights and data stories
```

---

# Inspecting the Dataset

The first step after loading data is **quick inspection** to confirm the dataset loaded correctly.

### Viewing Sample Records

```python
df.head()
```

Shows the first rows of the dataset.

```python
df.tail()
```

Shows the last rows of the dataset.

```python
df.sample(5, random_state=42)
```

Displays random rows to verify that the dataset structure is consistent.

---

### Understanding Dataset Dimensions

```python
df.shape
```

Example output:

```
(891, 12)
```

This means:

* 891 rows (passengers)
* 12 columns (features)

---

### Inspecting Column Information

```python
df.info()
```

This command shows:

* column names
* data types
* number of non-null values

Example interpretation:

```
Age: 714 non-null values
```

This means **177 values are missing**.

Missing values must be handled before training machine learning models.

---

# Distribution Analysis

Understanding the **distribution of values** helps reveal patterns in the dataset.

For example, we can analyze the **age distribution of passengers**.

```python
fig = px.histogram(
    df,
    x="Age",
    nbins=30,
    title="Passenger Age Distribution"
)

fig.show()
```

![Passenger Age Distribution](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-age-distribution-histogram.png)

A histogram shows:

* where most values are concentrated
* whether data is skewed
* whether extreme values exist

For example, if most passengers are between **20–40 years old**, the dataset may have fewer examples of children or elderly passengers.

---

# Identifying Outliers

Outliers are values that are **very different from the rest of the data**.

Example:

```
21, 22, 23, 24, 200
```

![Outlier Example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-outlier-example.png)

The value **200** is clearly far away from the others.

Outliers may appear because of:

* data entry errors
* measurement errors
* rare but valid events

Outliers are important because they can strongly affect:

* averages
* regression models
* clustering algorithms

---

## Detecting Outliers with a Box Plot

Box plots visually show the distribution of data and highlight extreme values.

```python
fig = px.box(
    df,
    y="Fare",
    title="Fare Distribution and Possible Outliers"
)

fig.show()
```

![Fare Distribution Box Plot](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-boxplot-fare.png)

The box plot displays:

* the middle range of the data
* typical values
* extreme points that may be unusual

If we observe **very high ticket prices**, those points may represent luxury cabins or rare cases.

Not all outliers should be removed.
Sometimes rare values represent **important real-world events**.

---

# Correlation Analysis

After understanding individual variables, the next step is exploring **relationships between variables**.

Correlation measures how strongly two variables move together.

Correlation values range from:

![Correlation Scale](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-correlation-scale.png)

| Value | Meaning                      |
| ----- | ---------------------------- |
| +1    | Strong positive relationship |
| 0     | No relationship              |
| -1    | Strong negative relationship |

Example relationships:

| Variable 1  | Variable 2   | Relationship |
| ----------- | ------------ | ------------ |
| Study hours | Exam score   | Positive     |
| Temperature | Jacket sales | Negative     |

---

## Computing the Correlation Matrix

```python
corr = df.corr(numeric_only=True)

corr
```

The correlation matrix compares every numerical feature with every other feature.

---

# Correlation Heatmap

A **heatmap** converts correlation numbers into colors, making patterns easier to interpret.

```python
fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap of Titanic Features"
)

fig.show()
```

![Correlation Heatmap](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-correlation-heatmap.png)

Heatmaps help quickly identify:

* features that strongly relate to the target
* variables that move together

For example:

* Passenger class may correlate with survival
* Fare may correlate with passenger class

These relationships help guide **feature selection for machine learning models**.

---

# Building a Data Story

EDA is not only about generating charts.
The goal is to turn raw data into **clear insights**.

A useful structure for communicating insights is:

![Data Story Structure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-data-story-structure.png)

```
Context
Observation
Explanation
Implication
```

---

## Example Data Story

Context
The Titanic carried passengers from different social classes.

Observation
Female passengers had a much higher survival rate than male passengers.

Explanation
Evacuation policies prioritized women and children.

Implication
Gender may be a strong feature for predicting survival.

---

# Investigation Exercise

### Question 1 — Passenger Class vs Survival

```python
fig = px.histogram(
    df,
    x="Pclass",
    color="Survived",
    barmode="group",
    title="Passenger Class vs Survival"
)

fig.show()
```

![Passenger Class vs Survival](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-pclass-vs-survival.png)

Observation:

```
________________________
```

Explanation:

```
________________________
```

---

### Question 2 — Age vs Survival

```python
fig = px.box(
    df,
    x="Survived",
    y="Age",
    title="Age Distribution by Survival"
)

fig.show()
```

![Age Distribution by Survival](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/eda-checklist/eda-age-vs-survival.png)

Observation:

```
________________________
```

Explanation:

```
________________________
```

---

### Question 3 — Feature Selection

Which features might be useful for predicting survival?

Example answers:

```
1.
2.
3.
4.
```

Explain your reasoning:

```
________________________
```

---

# Key Takeaways

Exploratory Data Analysis is the foundation of every machine learning project.

Through EDA we:

* understand dataset structure
* detect missing values
* identify unusual values
* analyze relationships between features
* generate meaningful insights

Effective EDA improves both **model quality and decision-making**.

---

