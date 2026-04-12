# **Data Prep: Handling Messy Data**

---

# **1. Why Data Preparation Matters**

Machine learning models do not understand meaning the way humans do. They do not know what a “car”, “student”, or “order” represents. They only work with numbers and patterns. This means that whatever data we provide becomes the only source from which the model learns.

In real-world scenarios, data is rarely clean. It often contains missing values, repeated entries, incorrect information, and inconsistent formats. If these issues are not handled properly, the model does not recognize them as mistakes. Instead, it treats them as valid patterns and learns from them.

To understand this more clearly, imagine preparing for an exam using notes that are incomplete or contain incorrect formulas. Even if you study sincerely, your answers will reflect those errors. The problem is not your effort — it is the quality of the material. In the same way, the performance of a machine learning model depends heavily on the quality of the data it is trained on.

Data preparation ensures that the data is complete, consistent, and meaningful before it is used for learning. It is not just a preliminary step — it directly determines how reliable the final system will be.

![Why data preparation matters — from messy inputs to reliable learning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-01-why-data-prep.png)

---

## **Datasets Used in This Session**

To understand the concepts clearly, we will use three datasets from different domains.

### **Car Dataset**

(Used to predict car price)

| Brand   | Year | Fuel   | KMs_Driven | Price   |
| ------- | ---- | ------ | ---------- | ------- |
| Maruti  | 2018 | Petrol | 30000      | 400000  |
| Hyundai | 2017 | Diesel | 40000      | 500000  |
| Maruti  | 2018 | Petrol | 30000      | 400000  |
| Honda   | 2016 | Petrol | *missing*  | 450000  |
| Toyota  | 2019 | Diesel | 20000      | 800000  |
| Honda   | 2015 | Petrol | 70000      | -200000 |

Issues highlighted in this session: duplicate row (Maruti), missing mileage, negative price, categorical columns (`Brand`, `Fuel`), and features on different scales (`Year` vs `Price`).

### **Student Dataset**

(Used to understand student performance)

| Student_ID | Marks | Attendance | Grade |
| ---------- | ----- | ---------- | ----- |
| S01        | 85    | 90         | A     |
| S02        | 72    | 88         | B     |
| S01        | 85    | 90         | A     |
| S03        | *missing* | 95    | C     |
| S04        | 90    | 92         | -10   |

Issues: duplicate student row, missing marks, invalid grade (`-10`), plus categorical `Grade` for encoding examples.

### **E-commerce Dataset**

(Used to analyze orders and pricing)

| OrderID | Product | Quantity | Price  |
| ------- | ------- | -------- | ------ |
| O100    | Phone   | 1        | 20000  |
| O101    | Laptop  | 2        | 60000  |
| O100    | Phone   | 1        | 20000  |
| O102    | Phone   | *missing* | 15000 |
| O103    | Laptop  | 1        | -5000  |

Issues: duplicate order, missing quantity, negative price, categorical `Product`.

Although these datasets belong to different domains, they share similar issues. This helps us understand that data preparation is a universal process.

![Three domains (car, student, e-commerce) — the same data-quality ideas apply everywhere](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-02-three-domains.png)

---

# **2. Load and Inspect the Dataset**

Before making any changes, the first step is to understand what the dataset looks like. This is called inspection.

In Google Colab, the dataset is loaded and viewed. The examples in Sections 3–8 use the **car** table below; student and e-commerce tables match the same kinds of issues and can be loaded the same way.

**Car dataset (main running example):**

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}

df = pd.DataFrame(data)
df
```

**Student and e-commerce datasets (same session, other domains):**

```python
data_student = {
    "Student_ID": ["S01", "S02", "S01", "S03", "S04"],
    "Marks": [85, 72, 85, None, 90],
    "Attendance": [90, 88, 90, 95, 92],
    "Grade": ["A", "B", "A", "C", -10],
}

data_ecommerce = {
    "OrderID": ["O100", "O101", "O100", "O102", "O103"],
    "Product": ["Phone", "Laptop", "Phone", "Phone", "Laptop"],
    "Quantity": [1, 2, 1, None, 1],
    "Price": [20000, 60000, 20000, 15000, -5000],
}

df_student = pd.DataFrame(data_student)
df_ecommerce = pd.DataFrame(data_ecommerce)

print("Student dataset:")
print(df_student, "\n")
print("E-commerce dataset:")
print(df_ecommerce)
```

At this stage, we are not trying to fix anything. Instead, we carefully observe the data.

In the car dataset, we notice that one value in mileage is missing, one row is repeated, and one price is negative. In the student dataset, marks are missing for one student, and a grade appears as -10, which is clearly incorrect. In the e-commerce dataset, quantity is missing for one order, and one price is negative.

This observation step is important because it helps us identify all the problems before attempting to solve them.

If we skip this step and directly start cleaning, we may apply incorrect transformations. For example, we might replace a value that was actually correct or miss an issue entirely. Inspection ensures that every action taken later is based on understanding.

![Inspect the data first — spot missing values, duplicates, and invalid entries before fixing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-03-inspect-data.png)

---

# **3. Handling Missing Data**

Missing values occur when information is not recorded. This can happen due to human error, incomplete forms, or system issues.

In the car dataset, the mileage of one car is missing. In the student dataset, marks are missing for one student. In the e-commerce dataset, the quantity of an order is missing.

Machine learning models cannot process missing values. They require complete numerical data. Therefore, missing values must be handled before training.

One common approach is imputation, where missing values are replaced with a reasonable estimate.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)

df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df
```

For `df_student`, you would impute on `Marks`; for `df_ecommerce`, on `Quantity` — same idea, different column name.

The median is used because it represents the middle value and is not affected by extreme values.

![Handling missing values — imputation fills gaps with a sensible estimate (e.g. median)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-04-missing-imputation.png)

---

## **What Changes After This Step**

Before handling missing values, the dataset contains gaps. Some rows cannot be used because they are incomplete. After replacing missing values, the dataset becomes complete. Every row now contains usable information.

In the student dataset, instead of leaving marks empty or assigning 0, we replace it with a realistic estimate. In the e-commerce dataset, the missing quantity is also filled with a reasonable value.

---

## **Understanding the Decision**

If we remove rows with missing values, we lose data. If we replace them incorrectly, we introduce false information. The goal is to balance completeness and accuracy.

This step ensures that the dataset remains usable without distorting reality.

---

# **4. Removing Duplicates and Fixing Inconsistencies**

Duplicate records occur when the same data appears multiple times.

In the car dataset, one car entry appears twice. In the student dataset, the same student appears twice. In the e-commerce dataset, the same order ID appears more than once.

If duplicates are not removed, the model may treat those entries as more important simply because they appear more frequently.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)

df = df.drop_duplicates()
df
```

---

## **Outliers and Incorrect Values**

Sometimes, data is present but clearly incorrect.

For example:

* A car price cannot be negative
* A student grade cannot be -10
* An order price cannot be negative

These values are called outliers.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()

df = df[df["Price"] > 0]
df
```

![Remove duplicates and filter invalid values so each row is unique and realistic](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-05-duplicates-outliers.png)

---

## **What Changes After This Step**

Before cleaning, the dataset contains repeated and incorrect values. After cleaning, each row represents a unique and valid record.

The dataset now reflects real-world conditions more accurately.

---

## **Understanding the Impact**

If duplicates remain, the model becomes biased toward repeated entries. If incorrect values remain, the model learns patterns that do not exist in reality.

This step ensures fairness and correctness.

---

# **5. Preparing Categorical Data**

Not all data is numerical. Some columns contain categories, such as fuel type, grade, or product.

These are called categorical variables because they represent labels rather than quantities.

Machine learning models cannot understand text directly. They require numerical input.

---

## **Understanding the Need**

If we provide text values to a model, it cannot process them. This is similar to giving instructions in a language the system does not understand.

Therefore, categorical data must be converted into numbers.

---



# **6. Encoding Categorical Data**

After handling missing values, duplicates, and incorrect entries, the dataset becomes cleaner and more consistent. However, there is still an important challenge — some columns contain **text-based values**, also known as categorical data.

In the car dataset, columns like `Fuel` and `Brand` contain values such as “Petrol”, “Diesel”, or “Maruti”. In the student dataset, the `Grade` column contains values like “A”, “B”, and “C”. In the e-commerce dataset, the `Product` column contains values such as “Phone” and “Laptop”.

These values are meaningful to humans, but machine learning models cannot interpret text directly. They require numerical input because all computations inside the model are based on numbers.

---

## **Understanding the Problem Through Examples**

Consider the car dataset:

| Fuel   |
| ------ |
| Petrol |
| Diesel |

To a human, these are two categories. But to a model, these are just strings with no numerical meaning. The model cannot compare “Petrol” and “Diesel” or perform calculations with them.

Similarly, in the student dataset:

| Grade |
| ----- |
| A     |
| B     |
| C     |

A human understands that grade A is better than B, but the model does not know this unless we represent it numerically.

In the e-commerce dataset:

| Product |
| ------- |
| Phone   |
| Laptop  |

Again, the model cannot interpret these categories without conversion.

---

## **What is Encoding**

Encoding is the process of converting categorical (text-based) data into numerical form so that it can be used by machine learning models.

This step does not change the meaning of the data — it only changes how it is represented.

---

## **Method 1: Label Encoding**

In label encoding, each category is assigned a number.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()
df = df[df["Price"] > 0]

df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
df
```

After encoding:

| Fuel   | Encoded |
| ------ | ------- |
| Petrol | 0       |
| Diesel | 1       |

---

### **What Happens After Label Encoding**

* Text values are replaced with numbers
* Dataset becomes numerical
* Model can now process the column

This can also be applied in the student dataset:

| Grade | Encoded |
| ----- | ------- |
| A     | 3       |
| B     | 2       |
| C     | 1       |

---

## **Understanding the Hidden Problem**

At first, this seems correct. However, label encoding introduces an **order**.

For example:

* Diesel = 1
* Petrol = 0

This may unintentionally suggest that Diesel is “greater” than Petrol, even though there is no such relationship.

Similarly, in grades:

* A > B > C

This ordering might be meaningful, but in some cases (like product categories), no order exists.

---

## **Method 2: One-Hot Encoding**

To avoid unintended ordering, we use one-hot encoding.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()
df = df[df["Price"] > 0]
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})

df = pd.get_dummies(df, columns=["Brand"])
df
```

After encoding:

| Brand_Maruti | Brand_Honda | Brand_Toyota |
| ------------ | ----------- | ------------ |
| 1            | 0           | 0            |
| 0            | 1           | 0            |

Each category becomes its own column.

---

## **What Happens After One-Hot Encoding**

* No ordering is introduced
* Each category is treated independently
* Model can distinguish categories clearly

This can be applied across datasets:

**Student dataset (Grade):**

| Grade_A | Grade_B | Grade_C |
| ------- | ------- | ------- |
| 1       | 0       | 0       |

**E-commerce dataset (Product):**

| Product_Phone | Product_Laptop |
| ------------- | -------------- |
| 1             | 0              |

---

## **Comparing the Two Methods**

![Label encoding vs one-hot encoding — avoiding a false sense of “order” between categories](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-06-encoding.png)

Label encoding:

* Simple and compact
* May introduce unintended order

One-hot encoding:

* More accurate representation
* Increases number of columns

---

## **How the Dataset Changes Overall**

Before encoding:

* Dataset contains text values
* Model cannot process these columns

After encoding:

* All columns become numerical
* Dataset becomes fully usable

Across all three datasets:

* Car dataset → Fuel and Brand converted
* Student dataset → Grade converted
* E-commerce dataset → Product converted

---

## **Thinking Layer**

At this stage, it is important to reflect on how the representation of data affects learning.

If we choose the wrong encoding method, the model may learn relationships that do not exist. For example, assigning numbers to categories may make the model think that one category is “larger” or “better” than another.

On the other hand, using one-hot encoding avoids this issue but increases the number of columns, which can make the dataset larger.

This means encoding is not just a technical step — it is a design decision that affects how the model understands the data.

---



---

# **7. Feature Scaling**

After cleaning missing values, duplicates, and categorical data, the dataset is now complete and numerical. However, one important issue still remains — **different features exist on very different scales**.

In the car dataset, the `Price` column contains values like 400000 and 800000, while the `Year` column contains values like 2015–2019. In the student dataset, marks range between 0 and 100, while attendance is also a percentage but behaves differently. In the e-commerce dataset, price values are large, while quantity is usually very small (1 or 2).

To a human, this difference is natural. But to a machine learning model, these are just numbers. The model does not understand what “price” or “year” means — it only sees their magnitude.

---

## **Understanding the Problem Through Examples**

Consider the car dataset:

* Car A → Year = 2018, Price = 400000
* Car B → Year = 2017, Price = 800000

The difference in year is just 1, while the difference in price is 400000. If the model tries to compare these two cars, it will focus almost entirely on price because the numerical difference is much larger.

Now look at the student dataset:

* Student A → Marks = 85, Attendance = 90
* Student B → Marks = 75, Attendance = 88

Marks difference = 10
Attendance difference = 2

Again, marks dominate.

In the e-commerce dataset:

* Order 1 → Price = 20000, Quantity = 1
* Order 2 → Price = 60000, Quantity = 2

Price dominates the comparison.

---

## **Why This is a Problem**

The model starts giving importance to features based on their numerical size, not their actual relevance. This leads to biased learning, where some features are ignored completely.

---

## **What is Feature Scaling**

Feature scaling is the process of transforming all features so that they are on a similar scale. This ensures that each feature contributes fairly to the model.

![Feature scaling — bring features to comparable ranges so one column does not dominate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-07-feature-scaling.png)

---

## **Method 1: Normalization**

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()
df = df[df["Price"] > 0]
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
df = pd.get_dummies(df, columns=["Brand"])

df["Price"] = (df["Price"] - df["Price"].min()) / (df["Price"].max() - df["Price"].min())
df
```

### **What Happens After Normalization**

* All values are converted between 0 and 1
* The smallest value becomes 0
* The largest value becomes 1

For example:

| Before | After |
| ------ | ----- |
| 400000 | 0.25  |
| 800000 | 1.0   |

Now, price is no longer dominating — it is comparable with other features.

---

## **Method 2: Standardization**

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()
df = df[df["Price"] > 0]
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
df = pd.get_dummies(df, columns=["Brand"])
df["Price"] = (df["Price"] - df["Price"].min()) / (df["Price"].max() - df["Price"].min())

df["Year"] = (df["Year"] - df["Year"].mean()) / df["Year"].std()
df
```

### **What Happens After Standardization**

* Values are centered around 0
* Positive values → above average
* Negative values → below average

For example:

| Year | Standardized |
| ---- | ------------ |
| 2015 | -1.2         |
| 2018 | 0.3          |
| 2019 | 1.0          |

Now the model understands relative position instead of absolute value.

---

## **Final Dataset After Scaling**

Across all datasets:

* Car dataset → Price and Year now comparable
* Student dataset → Marks and Attendance balanced
* E-commerce dataset → Price and Quantity balanced

---

## **Thinking Layer (Embedded Understanding)**

If scaling is not applied, the model does not fail immediately. It still produces results — but those results are biased. The model is not making intelligent decisions; it is being influenced by the size of numbers.

Scaling ensures fairness in learning. It allows the model to focus on patterns rather than magnitudes.

---

## **Key Insight**

Feature scaling does not change the meaning of data — it changes how the model *perceives* it.

---

# **8. Preventing Data Leakage**

After cleaning and scaling, one critical mistake can still occur — **data leakage**.

---

## **What is Data Leakage**

Data leakage happens when information from the test dataset is used during training.

At first, this might not seem like a problem. In fact, the model may perform extremely well. However, this performance is misleading because the model has already seen information it should not have access to.

---

## **Understanding Through Analogy**

Imagine preparing for an exam:

* If you practice using sample questions → fair learning
* If you see the actual exam paper beforehand → you score high

But that score does not reflect your real understanding.

This is exactly what happens in data leakage.

![Prevent data leakage — split train and test first, then fit preprocessing only on training data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-08-data-leakage.png)

---

## **How Leakage Happens in Practice**

A common mistake is:

1. Take full dataset
2. Fill missing values using full data
3. Scale using full data
4. Then split into train and test

This means:

* The model indirectly uses test data
* Evaluation becomes unrealistic

---

## **Correct Approach**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
df = pd.DataFrame(data)
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
df = df.drop_duplicates()
df = df[df["Price"] > 0]
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
df = pd.get_dummies(df, columns=["Brand"])
df["Price"] = (df["Price"] - df["Price"].min()) / (df["Price"].max() - df["Price"].min())
df["Year"] = (df["Year"] - df["Year"].mean()) / df["Year"].std()

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

The cell above rebuilds a fully preprocessed `df` so the split can be run on its own. In real projects, split into train and test **first**, then fit imputers, encoders, and scalers on **training data only** and apply them to the test set — that is how you avoid leakage.

Then:

* Compute all transformations using **only training data**
* Apply same transformations to test data

---

## **What Changes After Correct Handling**

Before:

* Model has indirect access to test data
* Evaluation looks very good

After:

* Test data remains unseen
* Evaluation becomes realistic

---

## **Across Examples**

* Car dataset → using future car prices to predict past
* Student dataset → using final exam data to predict earlier performance
* E-commerce dataset → using future orders to predict past behavior

---

## **Thinking Layer**

The key question to ask is:

> “Would this information be available at prediction time?”

If the answer is no, it should not be used during training.

---

## **Key Insight**

Data leakage creates **false confidence**.
A model that looks accurate with leakage often fails in real-world use.

---

# **9. Evaluating the Impact of Data Preparation**

After completing all preprocessing steps, it is important to step back and observe how the dataset has changed.

Data preparation is not just about applying steps — it is about transforming raw data into meaningful input.

![Before vs after data preparation — from unusable raw tables to model-ready numeric data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-09-before-after-prep.png)

---

## **Before Data Preparation**

Across all datasets:

* Missing values created incomplete records
* Duplicate rows caused repetition
* Incorrect values distorted patterns
* Text values could not be processed
* Different scales created imbalance

At this stage, the dataset was not suitable for machine learning.

---

## **After Data Preparation**

Now, after applying all steps:

* Missing values are filled
* Duplicate records are removed
* Incorrect values are filtered
* Categorical data is encoded
* Features are scaled

---

## **What Actually Changed (Important)**

The transformation is not just visual:

* Dataset is now complete → no missing values
* Dataset is now fair → no duplicate bias
* Dataset is now realistic → no incorrect values
* Dataset is now usable → all numerical
* Dataset is now balanced → equal feature contribution

---

## **Across All Three Examples**

This transformation happens in:

* Car dataset → ready for price prediction
* Student dataset → ready for performance analysis
* E-commerce dataset → ready for order insights

This shows that the same preprocessing steps apply across domains.

---

## **Thinking Layer**

At this stage, students should reflect:

* What problems existed initially?
* What steps were applied?
* How did each step improve the dataset?

This reflection helps connect actions to outcomes.

---

## **Why This Matters**

A model trained on messy data learns incorrect patterns.
A model trained on clean data learns meaningful relationships.

---

## **Final Insight**

Data preparation is not a technical formality —
it is the process that makes learning possible.

---

## **📌 Cheatsheet (Session Summary)**

### **Libraries Used**

* pandas → handling data
* sklearn → splitting data

---

### **Functions Used**

* `pd.DataFrame()` → create dataset
* `.fillna()` → handle missing values
* `.median()` → compute median
* `.drop_duplicates()` → remove duplicates
* `.map()` → label encoding
* `pd.get_dummies()` → one-hot encoding
* `.min()` / `.max()` → normalization
* `.mean()` / `.std()` → standardization
* `train_test_split()` → split dataset

---

### **Concepts Covered**

* Missing values (Imputation)
* Duplicate removal
* Outlier handling
* Categorical encoding
* Feature scaling
* Data leakage prevention

---

# **10. Why This Matters for Agentic Systems Design**

So far, the focus has been on cleaning data for machine learning. However, this becomes even more important when building **agentic systems**.

---

## **What is an Agentic System**

An agentic system is a system that can:

* Observe data
* Make decisions
* Take actions

Examples include:

* Recommendation systems
* Chatbots
* Pricing systems

![Agentic systems observe, decide, and act — they rely on clean data as their foundation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems/module2/session26/session26-10-agentic-systems.png)

---

## **Role of Data in Agentic Systems**

These systems rely entirely on data to function. They do not have human intuition. They depend on patterns learned from data.

---

## **Understanding Through Examples**

In the car dataset:

* If prices are incorrect → agent recommends wrong prices

In the student dataset:

* If marks are missing or incorrect → agent gives wrong feedback

In the e-commerce dataset:

* If order data is messy → agent gives wrong recommendations

---

## **What Happens Without Data Preparation**

* Decisions become unreliable
* Errors propagate across system
* User trust decreases

---

## **What Happens With Clean Data**

* Decisions become accurate
* System behaves consistently
* Predictions improve

---

## **Thinking Layer**

An agent is only as intelligent as the data it learns from.

If the data is messy, the agent behaves unpredictably.
If the data is clean, the agent behaves reliably.

---

## **Final Insight**

Data preparation is not just about cleaning data —
it is about ensuring that intelligent systems make correct decisions.

> Clean data → Reliable models → Reliable agents

---


