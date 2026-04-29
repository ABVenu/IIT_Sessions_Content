# ML Workshop: Model Selection & Comparison

## What You Will Learn in This Session

In the previous session, we explored **Time Series** — a special category of data where the order of records matters. We learned how to identify **Trend and Seasonality**, how to split time series data correctly using **chronological splits**, how to create **Rolling Window** features, and how to evaluate time series models with metrics like **MAPE**.

By now in this module, you have trained multiple types of models — regression, classification, clustering, and time series. But a very common question at this stage is: *"I have tried three different models — how do I know which one to actually use and how do I hand it over for real use?"*

This session answers exactly that. You will learn:

- How to build a **Metric Comparison Table** — a structured side-by-side view of multiple models
- How to compare models by their **complexity** — understanding when a simpler model is actually the better choice
- How to **save and load a trained model** (Model Persistence) so it can be used later without retraining
- A practical **Model Selection Checklist** to make confident, structured decisions on which model to deploy

---

## Metric Tables: Comparing Models Side by Side

Before this session, you learned several individual metrics — **MAE, RMSE, R²** for regression, and **Accuracy, Precision, Recall, F1-Score** for classification. You know what each metric means in isolation.

But in a real ML project, you never train just one model. You train multiple — maybe a Decision Tree, a Random Forest, and a Logistic Regression — and then you compare them. A **Metric Table** is how you do that comparison in one clear, structured view.

**Official Definition:** A **Metric Table** (also called a **Model Comparison Table**) is a structured summary that displays the performance scores of multiple models across multiple evaluation metrics — all in one place, side by side.

**In Simple Words:** It is like a school marksheet. Instead of each student's marks being on a separate sheet, all students' marks in all subjects are shown in one table. You can instantly see who performed best overall and who is strongest in which subject.

**Real-Life Example:** Imagine a cricket team selector comparing three bowlers. Bowler A has the best economy rate, Bowler B has the most wickets, and Bowler C is consistent in both. A comparison table immediately shows you this without looking at each bowler's stats separately. A metric comparison table does exactly the same for your ML models.

![Metric comparison table — models and scores side by side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_metric_comparison_table.png)

---

### Building a Metric Table in Python — Classification Example

```python
# ============================================================
# ML Workshop: Building a Metric Comparison Table (Classification)
# ============================================================

import pandas as pd                                          # For creating DataFrames and tables
import numpy as np                                           # For numerical operations
from sklearn.datasets import load_breast_cancer             # A built-in binary classification dataset
from sklearn.model_selection import train_test_split        # For splitting data into train and test
from sklearn.preprocessing import StandardScaler            # For scaling features to the same range

from sklearn.linear_model import LogisticRegression         # Simple, linear classification model
from sklearn.tree import DecisionTreeClassifier             # Tree-based classification model
from sklearn.ensemble import RandomForestClassifier         # Ensemble of many decision trees

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # Metric functions

# ---- Step 1: Load a real dataset ----
data = load_breast_cancer()                                  # 569 patient records, 30 medical features
X    = data.data                                             # Feature matrix (measurements)
y    = data.target                                           # Target (0 = malignant, 1 = benign)

# ---- Step 2: Train-test split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42                     # 80% train, 20% test, fixed seed for reproducibility
)

# ---- Step 3: Scale features — essential for Logistic Regression ----
scaler  = StandardScaler()                                   # Create a scaler object
X_train = scaler.fit_transform(X_train)                     # Fit on train data, then transform it
X_test  = scaler.transform(X_test)                          # Only transform test — never fit on test data

# ---- Step 4: Define all models in a dictionary for easy looping ----
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),          # max_iter ensures the solver converges
    "Decision Tree":       DecisionTreeClassifier(random_state=42),    # Fixed seed for reproducible tree structure
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42)  # 100 trees in the forest
}

# ---- Step 5: Train each model, predict, and collect all metrics ----
results = []                                                 # Empty list to collect one row per model
for model_name, model in models.items():                    # Loop through each model name and object
    model.fit(X_train, y_train)                             # Train the model on training data
    y_pred = model.predict(X_test)                          # Predict labels for the test set
    results.append({                                        # Append a dictionary with all metric values
        "Model":     model_name,
        "Accuracy":  round(accuracy_score(y_test, y_pred),  4),
        "Precision": round(precision_score(y_test, y_pred), 4),
        "Recall":    round(recall_score(y_test, y_pred),    4),
        "F1-Score":  round(f1_score(y_test, y_pred),        4)
    })

# ---- Step 6: Convert to DataFrame and display the comparison table ----
comparison_df = pd.DataFrame(results)                       # Convert list of dicts into a DataFrame
comparison_df = comparison_df.set_index("Model")            # Use model name as row label
print(comparison_df)                                        # Display the final side-by-side table
```

**How the code works:**

- `load_breast_cancer()` provides a real medical dataset — no need to build our own. It has 569 patient records and 30 features like tumour radius and texture.
- `StandardScaler` normalises all features to the same scale. This is mandatory for Logistic Regression — without it, features with larger numbers (like tumour area) would dominate and distort the model.
- Storing models in a **dictionary** is a clean pattern — one `for` loop handles training, predicting, and metric calculation for all three models.
- `results.append(...)` collects one row per model. Each row is a dictionary mapping metric names to values.
- `pd.DataFrame(results)` converts this list of rows into a neat, readable table.

**Sample Output — Metric Comparison Table:**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.9737 | 0.9726 | 0.9859 | 0.9792 |
| Decision Tree | 0.9474 | 0.9577 | 0.9577 | 0.9577 |
| Random Forest | 0.9649 | 0.9589 | 0.9859 | 0.9722 |

- **Logistic Regression** achieves the highest F1-Score despite being the simplest model — an important insight.
- **Decision Tree** trails slightly. In the next section, you will understand exactly why.
- **Random Forest** sits between the two — better than Decision Tree but very close to Logistic Regression.
- Without this table, you would have to jump between three separate outputs to reach the same conclusion.

---

### Building a Metric Table for Regression

The same pattern works for regression. The only difference is the metrics used — MAE, RMSE, and R².

```python
# ============================================================
# ML Workshop: Building a Metric Comparison Table (Regression)
# ============================================================

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing        # Built-in regression dataset (house prices)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression            # Simple linear regression model
from sklearn.tree import DecisionTreeRegressor               # Tree-based regression model
from sklearn.ensemble import RandomForestRegressor           # Ensemble regression model

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # Regression metrics

# ---- Step 1: Load California housing dataset ----
data     = fetch_california_housing()                        # 20,640 rows, 8 features, target = house price
X, y     = data.data, data.target                           # Features and target (median house value)

# ---- Step 2: Split and scale ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler   = StandardScaler()
X_train  = scaler.fit_transform(X_train)                    # Fit on train data only
X_test   = scaler.transform(X_test)                         # Apply same scaling to test data

# ---- Step 3: Define regression models ----
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree":     DecisionTreeRegressor(random_state=42),
    "Random Forest":     RandomForestRegressor(n_estimators=100, random_state=42)
}

# ---- Step 4: Train, predict, and compute metrics ----
results = []
for model_name, model in models.items():
    model.fit(X_train, y_train)                             # Train the model
    y_pred = model.predict(X_test)                          # Predict on test set
    rmse   = np.sqrt(mean_squared_error(y_test, y_pred))    # Compute RMSE (sklearn gives MSE, we take square root)
    results.append({
        "Model": model_name,
        "MAE":   round(mean_absolute_error(y_test, y_pred), 4),   # Lower is better
        "RMSE":  round(rmse, 4),                                   # Lower is better
        "R²":    round(r2_score(y_test, y_pred), 4)                # Closer to 1.0 is better
    })

# ---- Step 5: Display table ----
comparison_df = pd.DataFrame(results).set_index("Model")
print(comparison_df)
```

**How the code works:**

- `fetch_california_housing()` gives us a large, realistic regression dataset — house price prediction using 8 features like average rooms and location.
- `np.sqrt(mean_squared_error(...))` manually computes RMSE because scikit-learn's function returns MSE (the square), not RMSE.
- For regression metrics: **lower MAE and RMSE = better**; **R² closer to 1.0 = better** (R² of 1.0 means perfect predictions).

**Sample Output:**

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| Decision Tree | 0.4744 | 0.7296 | 0.5951 |
| Random Forest | 0.3277 | 0.5022 | 0.8052 |

- **Random Forest** clearly dominates — lowest MAE, lowest RMSE, and highest R².
- The table makes the winner obvious at a glance. This is the power of a well-built metric table.

---

## Comparison by Complexity

Looking at the comparison tables above, you might wonder: *"Why does a simple model like Logistic Regression sometimes beat a complex Random Forest, and sometimes lose?"* The answer lies in understanding **model complexity** — one of the most important ideas in all of machine learning.

**Official Definition:** **Model Complexity** refers to how flexible a model is when fitting patterns in data. Simple models have fewer parameters and make stronger assumptions about the data; complex models have many parameters and can fit highly intricate, non-linear patterns.

**In Simple Words:** Think of a simple model as a one-size-fits-all shirt. It fits most people reasonably well, but not perfectly for anyone. A complex model is a custom-tailored shirt — it can fit one specific person perfectly, but it is expensive, time-consuming, and if the measurements were taken wrong, it will fit nobody well.

**Real-Life Example:** A school teacher evaluating essays. A simple rule like "more than 300 words = Pass" is fast and transparent but misses nuance. A teacher who reads every essay carefully, checking vocabulary, grammar, argument structure, and originality — that is a complex evaluation. Sometimes the complex approach gives better grades. But for a quick placement test, the simple rule is surprisingly good.

![Model complexity spectrum — from simple assumptions to flexible models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_complexity_spectrum.png)

---

### The Complexity Scale of Common Models

| Model | Complexity Level | Training Speed | Interpretability | Typical Use Case |
|---|---|---|---|---|
| Logistic Regression | Very Low | Very Fast | Very High | Binary classification, baseline |
| Linear Regression | Very Low | Very Fast | Very High | Regression, baseline |
| Decision Tree | Medium | Fast | High | Explainable decisions |
| SVM | Medium-High | Moderate | Low | Text classification, small datasets |
| Random Forest | High | Moderate | Medium | General-purpose, robust |
| Gradient Boosting | Very High | Slow | Low | Competitions, high accuracy |
| Neural Networks | Highest | Slowest | Very Low | Images, text, large datasets |

- **Interpretability** means: can a non-technical person understand why the model made a particular prediction?
- A **bank loan officer** needs high interpretability (must explain rejection). A **Netflix recommendation engine** does not — users just want good suggestions.

---

### Overfitting vs. Underfitting — The Core Tension of Complexity

This is the single most important concept when comparing models by complexity.

**Official Definition:**

- **Overfitting** — When a model is so complex that it memorises the training data, including its noise and random quirks. It scores very high on training data but performs poorly on new, unseen test data.
- **Underfitting** — When a model is too simple to capture the real underlying patterns. It scores poorly on both training data and test data.

**In Simple Words:**

- **Overfitting:** A student who memorises all past exam questions word-for-word. When a new exam arrives with slightly different questions, they score badly — because they memorised, not understood.
- **Underfitting:** A student who studied only 2 chapters out of 10. They cannot answer questions from the old exam or the new one.

**Real-Life Example:** A weather prediction model. An underfitting model always predicts "25°C, sunny" regardless of the season — far too simple. An overfitting model has memorised the exact weather for every date in last year's data, but next year's patterns are slightly different — it fails. A well-fitted model captures general seasonal patterns and adapts reliably to new data.

![Underfitting vs good fit vs overfitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_overfitting_underfitting.png)

---

### Detecting Overfitting and Underfitting with Code

The most reliable way to detect these problems is to compare **training accuracy vs. test accuracy** — and measure the gap between them.

```python
# ============================================================
# Detecting Overfitting vs. Underfitting by Varying Complexity
# ============================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier             # We will test this at different depths
from sklearn.metrics import accuracy_score
import pandas as pd

# ---- Prepare data ----
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ---- Test Decision Trees at five different complexity levels ----
results = []
for depth in [1, 3, 5, 10, None]:                          # None = unlimited depth = maximum complexity
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)                             # Train on training data

    train_acc = accuracy_score(y_train, model.predict(X_train))   # Score on training data
    test_acc  = accuracy_score(y_test,  model.predict(X_test))    # Score on test data (what really matters)

    results.append({
        "Max Depth":      str(depth) if depth else "Unlimited",
        "Train Accuracy": round(train_acc, 4),
        "Test Accuracy":  round(test_acc, 4),
        "Gap (Train-Test)": round(train_acc - test_acc, 4)  # Large gap = overfitting signal
    })

print(pd.DataFrame(results).set_index("Max Depth"))
```

**How the code works:**

- `max_depth` controls how deep the decision tree grows. A depth of 1 makes a very simple tree with a single decision; `None` allows the tree to grow until every training point is perfectly classified.
- We compute accuracy on **both** training and test data for each depth level — this is the key to spotting overfitting.
- The `Gap (Train-Test)` column is the red-flag indicator: a **large gap means the model is overfitting**.

**Sample Output:**

| Max Depth | Train Accuracy | Test Accuracy | Gap (Train-Test) |
|---|---|---|---|
| 1 | 0.9253 | 0.9123 | 0.0130 |
| 3 | 0.9538 | 0.9386 | 0.0152 |
| 5 | 0.9714 | 0.9474 | 0.0240 |
| 10 | 0.9956 | 0.9123 | 0.0833 |
| Unlimited | 1.0000 | 0.9035 | 0.0965 |

- At **depth 1**, the model **underfits** — it is too shallow to learn the data's real patterns, so both scores are moderate.
- At **depth 5**, training and test scores are both solid, and the gap is small — this is the **sweet spot**.
- At **Unlimited depth**, the training score hits 100% — perfect — but the test score drops back to 90%. The tree has memorised every training point, including noise. This is classic **overfitting**.
- **The lesson:** Never judge a model only by its training score. A suspiciously perfect training score with a much lower test score is always a red flag.

---

### The Golden Rule of Model Complexity

**Choose a simpler model when:**
- Your dataset is small (fewer than 1,000 rows) — complex models need lots of data to generalise well.
- You need to explain the model's decisions to non-technical stakeholders such as doctors, bank managers, or legal teams.
- A simple model is already achieving good test scores — there is no reason to add complexity.
- You need fast, real-time predictions in production.

**Choose a complex model when:**
- Your dataset is large (tens of thousands of rows or more).
- Accuracy is the top priority and interpretability is not required.
- The relationship between features and target is clearly non-linear.
- You have the time and computing resources for longer training.

> **Key Insight — Occam's Razor in ML:** A well-known principle in data science says: *"The simplest model that fits the data well is usually the best."* Always start with the simplest relevant model and only increase complexity if the simpler model genuinely cannot meet your accuracy target. This saves time, reduces costs, and produces more reliable, deployable models.

---

## Model Persistence: Saving and Loading Your Trained Model

Now that you know how to build and select a model, there is one essential practical skill left — **what do you do with the trained model once you are satisfied with it?**

Imagine you spent 3 hours training a complex Random Forest on 100,000 rows of data. Do you retrain it from scratch every single time a user makes a request? Absolutely not. You **save** the trained model to a file and **load** it whenever you need to make predictions.

**Official Definition:** **Model Persistence** is the process of saving a trained machine learning model to a file on disk so that it can be loaded and used later — without needing to retrain.

**In Simple Words:** It is like saving your game progress. You play for hours, reach Level 10, and click Save. The next time you play, you load your save file and continue from Level 10 — you do not restart from Level 1 every single time. Saving a trained model works exactly the same way.

**Real-Life Example:** Think about the spam filter in your email inbox. That model was trained once on millions of emails, then saved. Every time a new email arrives, the email server **loads** the saved model and runs the email through it in milliseconds. If it had to retrain from scratch for each email, your inbox would never load.

![Model persistence — train, save to disk, load, predict](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_persistence_save_load.png)

---

### Method 1: Saving with `joblib` — The Recommended Approach for Scikit-Learn

`joblib` is the **officially recommended** library for saving scikit-learn models. It is fast and efficient, especially for models that contain large arrays internally — like Random Forests with hundreds of trees.

```python
# ============================================================
# Model Persistence: Saving and Loading with joblib
# ============================================================

import joblib                                                # The official recommended library for sklearn models
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ---- Step 1: Train the model as usual ----
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)   # Create the model
model.fit(X_train, y_train)                                          # Train the model
print("Model trained successfully!")

# ---- Step 2: Save the trained model to a file ----
joblib.dump(model, 'random_forest_model.joblib')            # Serialise and write the model to disk
print("Model saved as 'random_forest_model.joblib'")

# ---- CRITICAL: Also save the scaler! ----
joblib.dump(scaler, 'scaler.joblib')                        # Save the fitted scaler separately
print("Scaler saved as 'scaler.joblib'")

# ============================================================
# In a completely different script or a later session:
# ============================================================

# ---- Step 3: Load the model back from disk ----
loaded_model  = joblib.load('random_forest_model.joblib')   # Reconstruct the model object from file
loaded_scaler = joblib.load('scaler.joblib')                # Load the same scaler that was used during training
print("Model and scaler loaded successfully!")

# ---- Step 4: Use the loaded model to make predictions on new data ----
X_test_scaled = loaded_scaler.transform(X_test)             # Scale new data using the loaded (pre-fitted) scaler
predictions   = loaded_model.predict(X_test_scaled)         # Make predictions using the loaded model
print(f"First 10 predictions: {predictions[:10]}")
```

**How the code works:**

- `joblib.dump(model, 'filename.joblib')` **serialises** (converts) the entire trained model — including all its learned parameters and tree structures — and writes it as a binary file to your disk.
- `joblib.load('filename.joblib')` reads the file and **reconstructs** the model object exactly as it was after training. You can call `.predict()` on it immediately.
- **Saving the scaler is critical** — this is the most common mistake beginners make. When you load the model later and get new data, you must scale it using the **exact same scaler** that was fitted on training data. A freshly created `StandardScaler()` has not been fitted yet and would produce completely different scaling values, giving your model incorrect inputs and garbage predictions.

---

### Method 2: Saving with `pickle` — Python's Built-In Option

`pickle` is Python's built-in serialisation library. It works for any Python object, including ML models.

```python
# ============================================================
# Model Persistence: Saving and Loading with pickle
# ============================================================

import pickle                                               # Python's built-in serialisation library
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ---- Train a model ----
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
model   = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ---- Save the model using pickle ----
with open('logistic_model.pkl', 'wb') as f:                # 'wb' = write binary — model data is not plain text
    pickle.dump(model, f)                                  # Serialise and write the model into the file
print("Model saved with pickle!")

# ---- Load the model back using pickle ----
with open('logistic_model.pkl', 'rb') as f:                # 'rb' = read binary — open for reading
    loaded_model = pickle.load(f)                          # Deserialise and reconstruct the model object
print("Model loaded with pickle!")
```

**How the code works:**

- `'wb'` stands for "write binary." We always use binary mode because serialised model data is not human-readable text — it is a structured byte sequence.
- `'rb'` stands for "read binary." Same reason — we open the file in binary mode to read the byte sequence back.
- `pickle.dump(object, file)` writes the object to the file; `pickle.load(file)` reads it back and reconstructs it.

---

### `joblib` vs. `pickle` — Which One to Use?

| Feature | joblib | pickle |
|---|---|---|
| Recommended for sklearn models? | **Yes — official recommendation** | Works, but not optimised |
| Speed for models with large arrays | Faster | Slower |
| Compression support | Built-in optional compression | None |
| Ease of use | Simple `dump/load` calls | Requires explicit file open/close |
| Common file extension | `.joblib` | `.pkl` |

**The simple answer:** Use **`joblib`** for any scikit-learn model. Use **`pickle`** only for general custom Python objects.

---

### Practical Tips for Saving Models in Real Projects

- **Always save preprocessing objects alongside the model.** If you used `StandardScaler`, `LabelEncoder`, or `OneHotEncoder` during preprocessing, save those too. Predictions will be wrong without them.
- **Version your saved model files.** Instead of `model.joblib`, use descriptive names like `rf_model_v1_2024-01-15.joblib`. If you retrain next month with new data, you can still go back to the previous version.
- **Test your loaded model** before deploying it. After loading, run predictions on a small test batch and verify the output matches what you expect.
- **Never load `.pkl` or `.joblib` files from untrusted sources.** Loading a serialised file executes Python code — if the file was tampered with, it can run malicious code on your machine.

---

## Model Selection Checklist

You now know how to compare models in a table, how complexity creates overfitting and underfitting, and how to save the final model. But the question still remains for the start of a new project: *"Which model do I even try first?"*

The **Model Selection Checklist** is your answer — a structured set of questions to ask before you begin training, which will narrow down your choices quickly and confidently.

**Official Definition:** A **Model Selection Checklist** is a step-by-step decision guide that helps you choose the most appropriate machine learning algorithm based on your problem's specific constraints — such as data size, problem type, interpretability requirements, and performance targets.

**In Simple Words:** It is like a doctor asking a patient: "How old are you? Any allergies? What are the symptoms?" before prescribing medicine. Without this checklist, you might prescribe a complex Random Forest for a problem that a 3-line Logistic Regression would solve in seconds.

![Model selection checklist — structured decision path](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_selection_checklist_flow.png)

---

### The 6-Question Checklist

**Question 1: What type of problem is it?**

| Problem Type | Go-To Models |
|---|---|
| Binary Classification (2 outcomes) | Logistic Regression, Decision Tree, Random Forest, SVM |
| Multi-class Classification (3+ outcomes) | Decision Tree, Random Forest |
| Regression (predict a continuous number) | Linear Regression, Decision Tree Regressor, Random Forest Regressor |
| Clustering (no labels at all) | K-Means |
| Dimensionality Reduction | PCA |
| Time Series Forecasting | Rolling Window + Regression, ARIMA |

This question alone eliminates most irrelevant models before you even look at data size.

---

**Question 2: How much data do you have?**

| Dataset Size | Recommended Approach |
|---|---|
| Small (fewer than 1,000 rows) | Logistic Regression, SVM, shallow Decision Tree |
| Medium (1,000 – 100,000 rows) | Random Forest, Gradient Boosting |
| Large (more than 100,000 rows) | Gradient Boosting, Neural Networks |

- Complex models like Random Forest need enough data to avoid overfitting. With too little data, they simply memorise training examples.
- Simple models are actually **more reliable on small datasets** — they generalise better when data is scarce.

---

**Question 3: Do you need to explain the model's decisions to a non-technical person?**

- **Yes (interpretability required):** Use Logistic Regression, Decision Tree, or Linear Regression. Doctors prescribing treatments, banks rejecting loan applications, and insurance companies assessing claims all require models whose decisions can be explained in plain language.
- **No (accuracy is all that matters):** Random Forest, Gradient Boosting, or Neural Networks are acceptable. Streaming platforms, recommendation systems, and fraud detection can use black-box models.

---

**Question 4: How fast does training and prediction need to be?**

- **Training and prediction must both be very fast:** Logistic Regression, Linear Regression.
- **Training can be slower, but predictions must be instant:** Random Forest — training takes minutes, but predictions are fast.
- **Training can be very slow, accuracy is paramount:** Gradient Boosting, Neural Networks — these can take hours to train but are worth it for the highest accuracy.

---

**Question 5: Is the relationship between features and target likely linear?**

- **Yes (a straight line fits well):** Linear or Logistic Regression is sufficient — no need for anything more complex.
- **No (the relationship is complex and non-linear):** Decision Tree, Random Forest, or Gradient Boosting.
- **Not sure?** Start with a linear model. If the residuals show clear non-linear patterns, then move to a tree-based model.

---

**Question 6: Does the data have many outliers or noisy features?**

- **Yes:** Avoid models sensitive to outliers, such as plain Linear Regression. Use Decision Tree or Random Forest, which split data by thresholds and are naturally more robust to extreme values.
- **No:** Any model works — proceed with the simplest first.

---

### The Model Selection Decision Flow

```
START
  ↓
Is it a supervised problem?
  → No  → Use Clustering (K-Means) or PCA
  → Yes ↓
Is the target a category (classification)?
  → No  → Use Regression models
  → Yes ↓
Is the dataset small (< 1,000 rows)?
  → Yes → Use Logistic Regression or shallow Decision Tree
  → No  ↓
Do you need interpretability?
  → Yes → Use Decision Tree (depth 3–7)
  → No  ↓
Is accuracy the top priority?
  → Yes → Use Random Forest or Gradient Boosting
  → No  → Start with Random Forest and compare via Metric Table
```

---

### The "Start Simple, Go Complex" Protocol

No matter what the checklist recommends, always follow this sequence inside every project:

1. **Establish a baseline** — Train the simplest relevant model (Logistic Regression for classification, Linear Regression for regression). Record all metrics in a table.
2. **Train a medium-complexity model** — Decision Tree or SVM. Add to the metric table.
3. **Train a high-complexity model** — Random Forest or Gradient Boosting. Add to the metric table.
4. **Apply the complexity filter** — If the simple model is within 2–3% of the best model's F1-Score or R², choose the simple model. The small accuracy gain does not justify the added complexity, slower predictions, and harder maintenance.
5. **Save the winner** — Use `joblib.dump()` to save the selected model and its scaler.

```python
# ============================================================
# The Full Selection Protocol: Compare → Select → Save
# ============================================================

import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression            # Step 1: simplest model
from sklearn.tree import DecisionTreeClassifier                # Step 2: medium complexity
from sklearn.ensemble import RandomForestClassifier            # Step 3: highest complexity
from sklearn.metrics import f1_score

# ---- Prepare data ----
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ---- Define models in increasing order of complexity ----
models = {
    "Logistic Regression (Simple)": LogisticRegression(max_iter=1000),
    "Decision Tree (Medium)":       DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest (Complex)":      RandomForestClassifier(n_estimators=100, random_state=42)
}

# ---- Train all models and collect F1 scores ----
results = {}                                                   # Store name → {model, F1}
for name, model in models.items():
    model.fit(X_train, y_train)                               # Train the model
    f1 = f1_score(y_test, model.predict(X_test))             # Compute F1-Score on test set
    results[name] = {"model_object": model, "F1-Score": round(f1, 4)}
    print(f"{name}: F1 = {f1:.4f}")

# ---- Apply complexity filter: pick the simplest model within 2% of the best ----
best_f1       = max(v["F1-Score"] for v in results.values())  # Identify the highest F1 across all models
selected_name = None
for name, info in results.items():                            # Loop from simplest to most complex (dict insertion order)
    if best_f1 - info["F1-Score"] <= 0.02:                   # Is this model within 2 percentage points of best?
        selected_name = name                                  # Yes — pick it (first match = simplest qualifying model)
        break

selected_model = results[selected_name]["model_object"]       # Retrieve the actual model object
print(f"\nSelected Model: {selected_name}")

# ---- Save the selected model and scaler ----
joblib.dump(selected_model, 'selected_model.joblib')          # Save chosen model to disk
joblib.dump(scaler,         'scaler.joblib')                  # Save scaler — never forget this step
print("Selected model and scaler saved successfully!")
```

**How the code works:**

- The models dictionary is defined in order — **simplest to most complex**. Python dictionaries preserve insertion order, so when we loop through them the first match of the complexity filter is always the simplest qualifying model.
- `best_f1 - info["F1-Score"] <= 0.02` checks: "Is this model's F1-Score within 2 percentage points of the absolute best?" If yes, it qualifies as "good enough."
- The loop hits Logistic Regression first. If it satisfies the 2% condition, it is immediately selected and the loop stops — no need to choose a more complex model.
- Both the selected model and the fitted scaler are saved. The project is now ready for deployment.

---

## Key Takeaways

- **Metric Tables** are the professional standard for comparing models — build a DataFrame showing all models and all metrics side by side. Never rely on a single number to make a model selection decision.
- **Model Complexity is a spectrum** — from very simple (Logistic Regression) to very complex (Neural Networks). Always check both training accuracy and test accuracy together; a large gap between them is the clearest signal of **overfitting**.
- **Start Simple, Go Complex** — always establish a simple baseline first, then only increase complexity if the performance improvement genuinely justifies it. A simple model that is 1–2% less accurate is often the better real-world choice.
- **Model Persistence** with `joblib` is essential for every real project — `joblib.dump()` to save, `joblib.load()` to reload. Always save your **scaler and all preprocessing objects** alongside the model, or predictions on new data will be wrong.
- **The 6-Question Checklist** (problem type → data size → interpretability → speed → linearity → noise) condenses all your ML knowledge into a structured decision process. Using it at the start of every project saves hours of wasted experimentation.
- In the sessions ahead, these skills will feed directly into building **end-to-end ML pipelines** — where data flows from raw input through preprocessing, model prediction, and output, all packaged together automatically.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | What It Means |
|---|---|
| **Metric Table** | A DataFrame comparing multiple models across multiple evaluation metrics side by side |
| **Model Complexity** | How flexible a model is in fitting patterns — simple models have fewer parameters, complex ones have more |
| **Overfitting** | Model memorises training data; very high train accuracy but much lower test accuracy |
| **Underfitting** | Model too simple to learn patterns; low accuracy on both train and test |
| **Train-Test Gap** | Difference between training accuracy and test accuracy — a large gap signals overfitting |
| **Occam's Razor** | ML principle: prefer the simplest model that adequately fits the data |
| **Model Persistence** | Saving a trained model to disk for reuse without retraining |
| **Model Selection Checklist** | A 6-question decision guide for choosing the right ML algorithm |
| `joblib.dump(model, 'file.joblib')` | Saves a trained model (or any object) to a binary file on disk |
| `joblib.load('file.joblib')` | Loads and reconstructs a previously saved model from a file |
| `pickle.dump(obj, f)` | Saves a Python object to an open binary file using pickle |
| `pickle.load(f)` | Loads a Python object from an open binary pickle file |
| `pd.DataFrame(list_of_dicts)` | Converts a list of dictionaries into a structured DataFrame (comparison table) |
| `.set_index("Model")` | Sets the "Model" column as the row label in a DataFrame |
| `f1_score()` | Computes F1-Score from `sklearn.metrics` |
| `mean_absolute_error()` | Computes MAE from `sklearn.metrics` — lower is better |
| `r2_score()` | Computes R² coefficient of determination — closer to 1.0 is better |
| `max_depth` | Decision Tree hyperparameter controlling how deep (complex) the tree grows |
| `n_estimators` | Random Forest hyperparameter: the number of trees in the forest |
| `StandardScaler` | Normalises features to zero mean and unit variance |
| `.fit_transform(X_train)` | Fits the scaler on training data and transforms it — use only on training data |
| `.transform(X_test)` | Applies the already-fitted transformation — use on test and new data |
