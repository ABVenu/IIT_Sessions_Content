### **Q1. Why is data preparation important in machine learning?**

A. It increases dataset size
B. It ensures data is clean and meaningful
C. It reduces computation time only
D. It removes the need for models

**Answer:** B

---

### **Q2. What is the first step before cleaning a dataset?**

A. Encoding
B. Scaling
C. Inspection
D. Training

**Answer:** C

---

### **Q3. Which of the following is a common method to handle missing values?**

A. Duplication
B. Encoding
C. Imputation
D. Scaling

**Answer:** C

---

### **Q4. Why should duplicate records be removed?**

A. To increase data size
B. To reduce computation cost only
C. To avoid bias in the model
D. To improve visualization

**Answer:** C

---

### **Q5. Which of the following is an example of an invalid/outlier value?**

A. Price = 500000
B. Grade = A
C. Price = -200000
D. Year = 2018

**Answer:** C

---

### **Q6. Why is encoding required for categorical data?**

A. To remove duplicates
B. To convert text into numbers
C. To reduce missing values
D. To normalize data

**Answer:** B

---

### **Q7. What is a drawback of label encoding?**

A. Increases dataset size
B. Introduces unintended order
C. Removes important data
D. Cannot handle numbers

**Answer:** B

---

### **Q8. What is data leakage?**

A. Loss of data during cleaning
B. Using test data during training
C. Removing too many rows
D. Incorrect encoding

**Answer:** B

---


## **Subjective Question**

### **Scenario:**

You have just joined a used car dealership as a data analyst. Your manager hands you a raw dataset and asks you to prepare it before it can be used for price prediction.

Work through the following tasks in order.

---

## **Task 1 — Load and Inspect the Data**

Create the dataset below as a pandas DataFrame and print it. Identify at least three data quality issues you can spot just by looking at it.

```python
data = {
    "Brand": ["Maruti", "Hyundai", "Maruti", "Honda", "Toyota", "Honda"],
    "Year": [2018, 2017, 2018, 2016, 2019, 2015],
    "Fuel": ["Petrol", "Diesel", "Petrol", "Petrol", "Diesel", "Petrol"],
    "KMs_Driven": [30000, 40000, 30000, None, 20000, 70000],
    "Price": [400000, 500000, 400000, 450000, 800000, -200000],
}
```

---

## **Task 2 — Clean the Data**

Fix all the issues you identified in Task 1 by applying the following steps in order:

* Fill the missing value in **KMs_Driven** with the column median
* Remove any row where **Price** is zero or negative
* Remove duplicate rows

---

## **Task 3 — Encode Categorical Columns and Mark Features and Label**

* The **Fuel** column has two categories — encode it using `.map()`
* Apply one-hot encoding to the **Brand** column using `pd.get_dummies()`
* After encoding, separate the cleaned DataFrame into:

  * Features **X** (all columns except **Price**)
  * Label **y** (**Price**)
* Print both

---

### **Submission Instructions**

* Go to the folder **“agentic systems”** in the Google Drive (created in Module 1)
* Inside that, create a new folder named:

  ```
  Module 2
  ```
* Inside **Module 2**, create a Google Colab notebook named:

  ```
  Handling Messy Data
  ```

### In the notebook:

* Solve all the above tasks:

  * Run all **code cells**
  * Write all **theory answers in Markdown cells**

---

#### **Final Submission**

* Share the **Google Colab link** in the answer box
* Ensure:

  * Sharing is **ON**
  * Access is set to **“Anyone with the link can view”**

---
### Solution

## **Task 1 — Load and Inspect the Data**

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
print(df)
```

### 🔍 **Data Quality Issues Identified**

1. Missing value in **KMs_Driven**
2. Negative value in **Price** (-200000)
3. Duplicate row (Maruti, 2018, Petrol, 30000, 400000 appears twice)

---

## **Task 2 — Clean the Data**

### 1. Fill missing values with median

```python
df["KMs_Driven"].fillna(df["KMs_Driven"].median(), inplace=True)
```

### 2. Remove rows with zero or negative price

```python
df = df[df["Price"] > 0]
```

### 3. Remove duplicate rows

```python
df = df.drop_duplicates()
```

### ✔️ Cleaned Data

```python
print(df)
```

---

## **Task 3 — Encoding and Feature Separation**

### 1. Encode Fuel column

```python
df["Fuel"] = df["Fuel"].map({"Petrol": 0, "Diesel": 1})
```

### 2. One-hot encode Brand

```python
df = pd.get_dummies(df, columns=["Brand"])
```

### 3. Split into Features (X) and Label (y)

```python
X = df.drop("Price", axis=1)
y = df["Price"]
```

### ✔️ Final Output

```python
print("Features (X):")
print(X)

print("\nLabel (y):")
print(y)
```

---

