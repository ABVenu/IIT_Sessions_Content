# **Data Prep: Handling Messy Data**

---

# **1. Why Data Preparation Matters**

In any machine learning project, the quality of the data directly determines the quality of the model. Real-world data is rarely clean or perfectly structured. It often contains missing values, duplicate entries, inconsistent formats, and even incorrect or unrealistic values.

If such issues are ignored, the model does not learn meaningful patterns. Instead, it starts learning errors and noise present in the dataset. This leads to poor predictions, even if the algorithm itself is correct.

A useful way to think about this is through a simple analogy: preparing data is like preparing ingredients before cooking. If the ingredients are spoiled, repeated, or missing, the final dish will not turn out well — no matter how good the recipe is. Similarly, clean and well-prepared data is the foundation of every reliable machine learning model.

---

## **Dataset Used in This Session**

We will work with a small used car dataset:

| Brand   | Year | Fuel   | KMs_Driven | Price   |
| ------- | ---- | ------ | ---------- | ------- |
| Maruti  | 2018 | Petrol | 30000      | 400000  |
| Hyundai | 2017 | Diesel | 40000      | 500000  |
| Maruti  | 2018 | Petrol | 30000      | 400000  |
| Honda   | 2016 | Petrol |            | 450000  |
| Toyota  | 2019 | Diesel | 20000      | 800000  |
| Honda   | 2015 | Petrol | 70000      | -200000 |

This dataset intentionally contains common issues:

* A missing value
* A duplicate row
* Categorical data
* An unrealistic value (negative price)
* Features with different scales

The goal of this session is to clean this dataset step by step and make it ready for modelling.

---

# **2. Load and Inspect the Dataset**

Before making any changes to the data, it is important to first understand what the dataset looks like. This step is known as data inspection, and it helps identify problems early.

When the dataset is loaded into Google Colab, the first task is not to clean, but to observe. This involves looking at the structure of the dataset, understanding the types of values present, and spotting obvious issues.

```python
import pandas as pd

data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000]
}

df = pd.DataFrame(data)
df
```

While observing the dataset, a few issues become immediately visible. One of the rows has a missing value in the mileage column. Another row is duplicated. There is also a negative price, which is not realistic in this context.

This step builds awareness. Without clearly identifying what is wrong, it is not possible to clean the data correctly.

---

# **3. Handling Missing Data**

In most real-world datasets, some values are often missing. This happens due to various reasons such as incomplete data collection, human error, or system failures during recording.

A missing value simply means that for a particular row and column, no valid data is available. In the dataset used here, the `KMs_Driven` column has one missing value. This creates a problem because machine learning models expect complete numerical input and cannot process empty entries.

Instead of removing the entire row immediately, a more practical approach is to estimate a reasonable value based on existing data. This process is known as **imputation**, where missing values are replaced with meaningful substitutes.

A commonly used method is to fill the missing value with the **median** of the column. The median represents the middle value and is less affected by extreme values compared to the average.

```python
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
```

This approach ensures that the dataset remains complete without introducing unrealistic values. Choosing the correct method depends on the nature of the data. For example, the mean works well for evenly distributed data, while the median is preferred when there are outliers.

---

# **4. Removing Duplicates and Fixing Inconsistencies**

Another common issue in datasets is duplicate records. These occur when the same data entry appears more than once, often due to data collection or merging processes.

In this dataset, the first and third rows are identical. If duplicates are not removed, the model may give extra importance to those repeated entries, leading to biased learning.

Duplicates can be removed using:

```python
df = df.drop_duplicates()
```

In addition to duplicates, datasets may also contain inconsistent or incorrect values. For example, the dataset includes a price of `-200000`, which is not logically possible. Such values are referred to as outliers or data errors.

These need to be handled carefully, usually by removing or correcting them:

```python
df = df[df["Price"] > 0]
```

This step ensures that the dataset reflects realistic and meaningful information.

---

# **5. Preparing Categorical Data**

Not all data in a dataset is numerical. Some columns represent categories or labels, such as brand names or fuel types.

In the dataset, columns like `Brand` and `Fuel` contain text values. These are known as **categorical variables**, as they represent categories rather than quantities.

Machine learning models cannot directly interpret text values. They require numerical input to perform calculations and identify patterns. Therefore, categorical data must be converted into numerical form before being used in a model.

---

# **6. Encoding Categorical Data**

The process of converting categorical data into numerical values is called **encoding**.

One simple approach is **label encoding**, where each category is assigned a number:

```python
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
```

However, this approach may introduce an unintended order between categories. For example, assigning Petrol = 0 and Diesel = 1 may incorrectly suggest that Diesel is “greater” than Petrol.

To avoid this, **one-hot encoding** is often used. It creates separate columns for each category:

```python
df = pd.get_dummies(df, columns=["Brand"])
```

This method ensures that categories are treated independently without implying any order.

---

# **7. Feature Scaling**

Different features in a dataset can have very different ranges. For example, the `Year` column ranges between 2015 and 2019, while `Price` ranges in lakhs.

If these values are used directly, features with larger values can dominate the learning process. This can negatively affect models that rely on distances or magnitudes.

To address this, features are scaled to bring them into a similar range.

**Normalization** rescales values between 0 and 1:

```python
df["Price"] = (df["Price"] - df["Price"].min()) / (df["Price"].max() - df["Price"].min())
```

**Standardization** adjusts values so they have a mean of 0 and a standard deviation of 1:

```python
df["Year"] = (df["Year"] - df["Year"].mean()) / df["Year"].std()
```

Scaling ensures that all features contribute equally to the model.

---

# **8. Preventing Data Leakage**

While preparing data, it is important to ensure that no information from the test dataset influences the training process. This issue is known as **data leakage**.

If preprocessing steps like imputation or scaling are applied before splitting the data, the model indirectly gains access to information from the test set. This results in overly optimistic performance during evaluation but poor real-world performance.

The correct approach is to split the dataset first and then apply preprocessing only on the training data.

```python
from sklearn.model_selection import train_test_split

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

After this, all transformations should be learned from `X_train` and applied to `X_test`.

---

# **9. Evaluating the Impact of Data Preparation**

After completing all preprocessing steps, it is important to step back and observe how the dataset has changed. Data preparation is not just about applying techniques — it is about improving the quality of data in a way that directly supports better learning.

To understand this, compare the dataset before and after cleaning.

---

## **Before Data Preparation**

The dataset initially contained several issues:

* Missing values in important columns
* Duplicate records that repeated the same information
* Incorrect values such as negative prices
* Categorical text values that models cannot process
* Features with very different scales

These problems make it difficult for a machine learning model to learn correctly. The model may treat incorrect values as valid patterns or give too much importance to repeated entries.

---

## **After Data Preparation**

After applying cleaning steps, the dataset now has:

* No missing values (all entries are complete)
* No duplicate rows (each record is unique)
* Only valid and realistic values
* All categorical data converted into numerical form
* Features scaled to comparable ranges

At this stage, the dataset is structured, consistent, and ready for modelling.

---

## **Making the Impact Visible**

The difference can be observed directly by comparing the dataset:

```python
print("Shape before cleaning:", df_before.shape)
print("Shape after cleaning:", df.shape)

print("\nCleaned Dataset Preview:")
print(df.head())
```

By observing the number of rows, columns, and values, it becomes clear how much unnecessary or incorrect data has been removed or corrected.

---

## **Why This Matters for Machine Learning**

A machine learning model learns patterns based on the data it receives. If the data contains errors, the model learns incorrect relationships. After cleaning:

* The model trains on accurate and consistent data
* Predictions become more reliable
* Training becomes more stable and efficient

---

## **Analogy: Before vs After Preparation**

Consider preparing for an exam:

* Studying from incomplete or incorrect notes leads to confusion
* Studying from clean, well-organized notes improves understanding

Data preparation plays the same role for machine learning models. It ensures that the model learns from correct and meaningful information.

---

## **Final Insight**

Data cleaning is not just a technical step — it is a transformation process that turns raw data into usable knowledge.

> The better the preparation, the better the learning outcome.

---


# **10. Why This Matters for Agentic Systems Design**

So far, the focus has been on cleaning and preparing data for machine learning. However, this step becomes even more important when building **agentic systems**.

An **agentic system** is a system that can make decisions, take actions, and adapt based on data and feedback. These systems rely heavily on machine learning models to understand inputs and decide what to do next.

---

## **Role of Clean Data in Agentic Systems**

In an agentic system, decisions are made automatically. For example:

* A recommendation system suggests products
* A chatbot responds to user queries
* A pricing system adjusts prices dynamically

All of these decisions depend on the data provided to the model.

If the data is messy:

* The agent may make incorrect decisions
* It may respond in unexpected or unreliable ways
* Errors can propagate across multiple steps in the system

---

## **Connecting Data Preparation to Agent Behavior**

Consider a simple scenario:

An agent is designed to recommend used cars based on price and usage.

* If duplicate data exists → the agent may over-recommend certain cars
* If missing values are ignored → the agent may fail to evaluate some options
* If incorrect values exist (like negative price) → the agent may produce meaningless recommendations
* If data is not scaled → some features may dominate decisions unfairly

This shows that data preparation is not just a preprocessing step — it directly affects how an agent behaves.

---

## **Analogy: Training a Decision-Maker**

Think of an agent as a decision-maker trained using past data.

* If the training material is clean and accurate → decisions are reliable
* If the training material is messy or incorrect → decisions become inconsistent

In this sense, data preparation is equivalent to ensuring that the agent is trained on **correct knowledge**.

---

## **Why This Learning Is Foundational**

The concepts covered in this session — handling missing data, removing duplicates, encoding categories, scaling features, and preventing leakage — form the foundation for building reliable systems.

Without these steps:

* Models cannot generalize well
* Evaluation becomes misleading
* Agent behavior becomes unpredictable

With proper data preparation:

* Models learn meaningful patterns
* Predictions become stable
* Agents behave consistently and reliably

---

## **Final Insight**

Agentic systems are only as reliable as the data they are built on.

> Clean data does not just improve models — it ensures that intelligent systems make correct and trustworthy decisions.

---