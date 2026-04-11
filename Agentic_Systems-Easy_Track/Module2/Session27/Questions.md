### Q1. What is the main risk of relying only on accuracy for model evaluation?

A. It increases training time
B. It may hide poor performance on important cases
C. It reduces dataset size
D. It causes overfitting

**Answer: B**

---

### Q2. What is data leakage in machine learning?

A. Loss of dataset during training
B. Model forgetting learned patterns
C. Using information not available at prediction time
D. Reducing dataset size

**Answer: C**

---

### Q3. Which of the following is an example of data leakage?

A. Using attendance to predict student performance
B. Using final exam marks to predict final result
C. Using past purchase history for prediction
D. Using product category for recommendation

**Answer: B**

---

### Q4. What is the correct first step to prevent data leakage?

A. Scale the data
B. Fill missing values
C. Split the dataset into train and test sets
D. Train the model

**Answer: C**

---

### Q5. What is class imbalance?

A. Dataset with missing values
B. Dataset with equal distribution of classes
C. Dataset where one class dominates others
D. Dataset with duplicate records

**Answer: C**

---

### Q6. Why is accuracy misleading in imbalanced datasets?

A. It becomes too low
B. It ignores training data
C. It may appear high even if minority class is ignored
D. It increases computation time

**Answer: C**

---

### Q7. What does recall measure?

A. Total correct predictions
B. Correctness of positive predictions
C. Ability to find all actual positive cases
D. Model training speed

**Answer: C**

---

### Q8. What is the main purpose of cross-validation?

A. To increase dataset size
B. To reduce model complexity
C. To get a more reliable evaluation by using multiple splits
D. To remove outliers

**Answer: C**

----

# **Problem Statement**

You are a junior data scientist working on a classification problem. Your goal is to evaluate a model while ensuring that your workflow does not suffer from data leakage.

---

# **Tasks**

## **Task 1 — Identify Data Leakage**

Using the dataset below:

```python
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
```

* Apply feature scaling on the **entire dataset before splitting**
* Perform a train-test split
* Train a Logistic Regression model
* Report train and test accuracy

**Question:**
What is wrong with this approach and why does it cause data leakage?

---

## **Task 2 — Correct the Workflow**

* First split the data into train and test sets
* Apply scaling using `.fit()` only on training data
* Use `.transform()` on test data
* Train a Logistic Regression model

**Report:**

* Train accuracy
* Test accuracy

---

## **Task 3 — Concept Check**

Answer briefly:

* What is data leakage?
* Why should preprocessing be done only on training data?
* Can a feature derived from the target variable be used as input? Why or why not?

---

### **Submission Instructions**

* Go to the folder **“agentic systems”** in the Google Drive (created in Module 1)
* Inside that, create a new folder named:

  ```bash
  Module 2
  ```
* Inside **Module 2**, create a Google Colab notebook named:

  ```bash
  Leakage & Imbalance
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




# **Solution**

---

## **Task 1 — Identify Data Leakage**

### Incorrect Workflow (Leaky)

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Generate data
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)

# WRONG: Scaling before split
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
```

### **What is wrong?**

* Scaling was done on the **entire dataset before splitting**
* The scaler learned mean and variance using **test data as well**
* This causes **data leakage**

### **Why is this a problem?**

* The model indirectly gets information about the test set
* Test accuracy becomes **overly optimistic**
* The model may perform worse in real-world scenarios

---

## **Task 2 — Correct Workflow**

### Proper Approach

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Split FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit scaler ONLY on training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Apply same transformation on test data
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Accuracy
train_acc = model.score(X_train_scaled, y_train)
test_acc = model.score(X_test_scaled, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
```

---

## **Task 3 — Concept Answers**

### **1. What is data leakage?**

Data leakage occurs when the model has access to information during training that would not be available in real-world prediction scenarios.

---

### **2. Why should preprocessing be done only on training data?**

* Preprocessing steps (like scaling, imputation) learn patterns from data
* If test data is included, it contaminates the training process
* This breaks the assumption that test data is **unseen**

---

### **3. Can a feature derived from the target be used?**

No.

* It directly reveals information about the output
* The model will learn shortcuts instead of real patterns
* This leads to **artificially high accuracy** but poor real-world performance

---

# **Key Takeaways**

* Always **split before preprocessing**
* Use **fit on train, transform on test**
* Avoid any feature that contains **target information**
* High accuracy ≠ correct model (if leakage exists)


