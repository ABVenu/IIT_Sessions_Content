# The ML Workflow & Habits

## What We Did Before and Where We Are Heading

In the previous sessions, you built a solid foundation in working with data. You learned how to load, clean, filter, and aggregate datasets using **Pandas**, write structured queries using **SQL**, and finally, you practiced visualising data — creating charts with Matplotlib and Plotly to tell a story from raw numbers. In the last practice session, you put all of that together by inspecting a dataset, plotting charts, and writing short insights below each chart.

Now we are crossing into a brand-new territory — **Machine Learning (ML)**. Think of everything you did in Module 1 as preparing the ingredients. Machine Learning is where you actually start *cooking* — you teach a computer to make predictions and decisions on its own.

**In this session, you will learn:**
- How to set up and use **Google Colab** — the tool we will use for all our ML work
- What the standard lifecycle of an ML project looks like
- How to frame a problem so a machine can understand and solve it
- The difference between Features (inputs) and Labels (outputs)
- Why and how to split data into Training, Validation, and Test sets
- What a Baseline is and why every good ML practitioner starts with one

---

## Getting Started with Google Colab

Before we run any ML code, we need a workspace. **Google Colab** is that workspace — and it is the tool that every data scientist and ML beginner loves for one simple reason: it runs entirely in your browser, with zero installation.

- **Official Definition:** Google Colaboratory (Colab) is a free, cloud-based Jupyter Notebook environment provided by Google. It allows you to write and run Python code in your browser while giving you access to free GPUs and TPUs for heavy computation.
- **In Simple Words:** It is like Google Docs — but instead of writing essays, you write and run Python code. Everything is saved automatically to your Google Drive, and you do not need to install Python, pip, or any library on your laptop.
- **Real-Life Example:** Imagine a chemistry lab where all the equipment is already set up for you. You just walk in, wear a lab coat, and start experimenting. Colab is exactly that — a fully equipped Python lab, in the cloud, ready to use the moment you open it.

### Why Use Colab for ML?

- **Free GPU access** — Training ML models requires heavy computation. Colab provides free GPU/TPU access so your code runs much faster than on a regular laptop.
- **No setup needed** — Popular ML libraries like `scikit-learn`, `pandas`, `numpy`, and `matplotlib` come pre-installed. You do not spend an hour installing packages before starting.
- **Easy sharing** — Like Google Docs, you can share your notebook with a link. Teammates can view or run your code without any setup.
- **Persistent storage via Google Drive** — All your notebooks are saved directly to your Google Drive, so you never lose your work.

### Setting Up Google Colab — Step by Step

**Step 1: Open Colab**
- Go to [colab.research.google.com](https://colab.research.google.com) in any browser.
- Sign in with your Google account (the same one you use for Gmail or Drive).

**Step 2: Create a New Notebook**
- Click **"New Notebook"** — this opens a blank notebook in a new tab.
- A notebook is made up of **cells** — each cell holds either code or text.

**Step 3: Rename Your Notebook**
- Click on "Untitled0.ipynb" at the top left and type a meaningful name like `Session13_ML_Workflow.ipynb`.
- The file is automatically saved to your Google Drive under the folder "Colab Notebooks".

**Step 4: Connect to Runtime**
- Click the **"Connect"** button at the top-right corner of the notebook.
- Colab will connect to a cloud server (called a **Runtime**) — this is the machine that will execute your code.
- Once connected, the button changes to show RAM and Disk usage — this means you are live and ready to run code.

**Step 5 (Optional): Enable GPU for Faster Training**
- Go to **Runtime → Change runtime type → Hardware Accelerator → Select GPU → Save**.
- For today's session, a standard CPU runtime is fine. You will need GPU for heavier training later in the course.

### Navigating the Colab Interface

| Interface Element | What It Does |
|---|---|
| **Code Cell** | Where you type and run Python code. Press `Shift + Enter` to run. |
| **Text Cell (Markdown)** | Where you write notes, headings, and explanations in plain text. |
| **Toolbar** | Top bar with File, Edit, Runtime, Tools menus |
| **Run Button (▶)** | Click to run a single cell |
| **+ Code / + Text** | Buttons to add a new code or text cell below |
| **Runtime Menu** | Restart, reconnect, or change the runtime (CPU/GPU) |
| **Left Sidebar** | Browse files, view table of contents, see connected secrets |

### Running Your First Code Cells in Colab

```python
# this is your first code cell in Colab
# press Shift + Enter (or click the Run button) to execute this cell

# print a welcome message to confirm Colab is working
print("Hello from Google Colab!")

# check which version of Python is running
import sys
print("Python version:", sys.version)
```

**How the code works:**
- When you press `Shift + Enter`, Colab sends this code to the cloud runtime and runs it.
- The output appears directly below the cell — you will see "Hello from Google Colab!" printed.
- `sys.version` prints the exact Python version your runtime is using — useful for debugging.

### Importing Libraries in Colab

```python
# import the libraries we will use throughout this session
import pandas as pd            # for loading and manipulating data in tables
import numpy as np             # for numerical operations and array handling
import matplotlib.pyplot as plt  # for creating basic charts and plots

# sklearn (scikit-learn) is the main ML library — import specific tools as needed
from sklearn.model_selection import train_test_split  # for splitting data
from sklearn.dummy import DummyClassifier              # for building baseline models
from sklearn.metrics import accuracy_score             # for measuring model performance

# confirm all imports worked by printing a success message
print("All libraries imported successfully!")
```

**How the code works:**
- In Colab, all major libraries (`pandas`, `numpy`, `sklearn`, `matplotlib`) are pre-installed — no `pip install` needed before importing.
- We use `import ... as ...` to give libraries short aliases (`pd` for pandas, `np` for numpy, `plt` for matplotlib) — this is universal convention across all ML code in the world.
- If the final `print` statement runs without errors, all your imports are ready for the session.

**Common Colab Shortcuts to Remember:**
- `Shift + Enter` — Run the current cell and move to the next
- `Ctrl + Enter` — Run the current cell and stay on it
- `Ctrl + M B` — Add a new code cell below
- `Ctrl + M M` — Convert a code cell to a text (Markdown) cell
- `Ctrl + /` — Comment or uncomment a line of code

---

## What Machine Learning Actually Is

Before writing any ML code, it is important to understand *what machine learning actually is* and *how it differs from regular programming*.

- **Official Definition:** Machine Learning is a subfield of Artificial Intelligence where a computer learns patterns from data to make predictions or decisions — without being explicitly programmed with rules.
- **In Simple Words:** In regular programming, you tell the computer every rule it should follow. In ML, you give the computer lots of examples (data), and it *figures out the rules by itself*.
- **Real-Life Example:** Teaching a child to recognise a dog. You do not give them a 20-page rulebook. You show them 100 pictures — "this is a dog, this is not a dog" — and they learn. ML works the same way with data.

![Regular programming spells out every rule; machine learning discovers patterns from examples and labeled data instead](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-01-regular-programming-vs-machine-learning.png)

There are three main types of ML problems you will encounter:

| Type | What the Computer Does | Example |
|---|---|---|
| **Classification** | Predicts a category or label | Is this email spam or not? |
| **Regression** | Predicts a number | What will the house price be? |
| **Clustering** | Groups similar items together | Group customers by their buying habits |

Understanding *which type* your problem is will shape every decision you make — from how you prepare your data to which algorithm you choose.

---

## Defining the ML Workflow

Think of building an ML model the same way you would build a house. You do not start with the roof — you start with the foundation. The **ML workflow** is the step-by-step process that every data scientist and ML engineer follows to go from a raw business problem to a working model.

**The 6 Steps of the ML Workflow:**
1. **Frame the Problem** — Define exactly what you want the machine to predict or decide.
2. **Collect & Prepare Data** — Gather the right data and clean it up.
3. **Engineer Features** — Choose and transform the columns that will help the model learn.
4. **Split the Data** — Divide data into Training, Validation, and Test sets.
5. **Train a Baseline Model** — Start with the simplest possible model to set a benchmark.
6. **Evaluate & Improve** — Measure how well the model is doing and improve it step by step.

![The six-step ML workflow — from framing the problem and preparing data through splitting, baseline training, and evaluation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-02-six-step-ml-workflow.png)

Today's session covers Steps 1, 3, 4, and 5 in depth. Steps 2 and 6 will be covered in upcoming sessions. Each step matters — skipping one is like skipping a floor in a building; the structure above it will collapse.

### Why a Structured Workflow Matters

Without a workflow, most beginners make these costly mistakes:
- **Training on the full dataset** — The model memorises the data instead of learning from it, and fails on new real-world inputs.
- **Skipping the baseline** — They build a complex model, see 85% accuracy, and celebrate — without realising a simple rule also gives 85%.
- **Touching the test data early** — They tune their model based on test results and end up with a model that only works on that specific test, not in production.

The workflow is your protection against all of these traps. It is not bureaucracy — it is professional discipline.

---

## Framing ML Problems Effectively

The most common mistake beginners make in ML is jumping straight to coding without properly thinking about the problem. **Problem Framing** is the art of converting a business or real-world question into a clear ML task.

- **Official Definition:** Problem Framing is the process of defining the ML problem — deciding what to predict, what data is available, and how success will be measured.
- **In Simple Words:** You are basically writing a job description for the machine. You tell it: "Your job is to predict X, using data Y, and I will measure your performance using Z."
- **Real-Life Example:** Imagine a doctor wants to know "Is this patient at risk of diabetes?" You do not give the computer the vague question. You frame it as: "Given a patient's age, weight, sugar levels, and family history — predict whether they will develop diabetes (Yes/No)." Now it is a **Classification** problem.

**Three Questions to Always Ask When Framing a Problem:**

- **What do I want to predict?** — This becomes your **Label** (the output / target).
- **What information do I have available to predict it?** — These become your **Features** (the inputs).
- **How will I measure success?** — This is your **evaluation metric** (accuracy, error rate, etc.).

![Problem framing ties together what to predict (label), what inputs you have (features), and how you measure success (metric)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-03-problem-framing-label-features-metric.png)

### Translating Real-World Problems into ML Terms

The skill of framing a problem is what separates a data scientist from a data analyst. An analyst looks at what *happened* in the past — a data scientist frames a question about the *future*.

**Template for Framing Any ML Problem:**

> "Given **[available input data]**, I want to predict **[output / target]**, and I will measure success using **[metric]**."

**Examples of well-framed problems:**

| Business Question (Vague) | Well-Framed ML Problem |
|---|---|
| "Why are customers leaving?" | "Given a customer's usage history, subscription plan, and support tickets — predict whether they will cancel next month (Yes/No). Measure with F1-score." |
| "How do we price our products better?" | "Given product category, competitor price, and season — predict the optimal selling price. Measure with Mean Absolute Error." |
| "Who should we send this offer to?" | "Given customer demographics and past purchases — predict whether a customer will click the offer (Yes/No). Measure with Precision." |

**Common Problem Framing Mistakes to Avoid:**
- Trying to predict something that has no available data to support it
- Using future information as an input (e.g., using "sale date" to predict if a sale will happen — circular logic)
- Confusing the label with a feature (more on this below)
- Treating a regression problem (predicting numbers) as a classification problem (predicting categories)

**Quick Activity:** Look at the table below and decide — is it a Classification, Regression, or Clustering problem?

| Business Question | ML Problem Type |
|---|---|
| Will this customer churn (leave) next month? | Classification |
| How much will this product sell next quarter? | Regression |
| Which customer segment does this buyer belong to? | Clustering |
| Is this transaction fraudulent? | Classification |
| What price should we set for this apartment? | Regression |
| Which city should we open the next store in? | Regression / Clustering |

---

## Differentiating Features and Labels

Once the problem is framed, the next step is understanding your data in terms of **Features** and **Labels**. This is one of the most important concepts in all of Machine Learning — get this wrong and everything downstream will fail.

### What is a Label?

- **Official Definition:** A **Label** (also called the **Target Variable** or **Dependent Variable**) is the column in your dataset that the model is trying to predict.
- **In Simple Words:** It is the *answer* you want the machine to give you.
- **Real-Life Example:** In a student dataset, if you want to predict whether a student will pass or fail, the column `result` (pass/fail) is your **Label**.

### What are Features?

- **Official Definition:** **Features** (also called **Independent Variables** or **Predictors**) are the input columns that the model uses to learn patterns and make predictions.
- **In Simple Words:** Features are all the *clues* you give to the machine so it can guess the answer.
- **Real-Life Example:** For predicting student results — columns like `attendance`, `marks_in_mock_test`, `study_hours_per_day`, and `assignment_completion_rate` are all **Features**. They are the clues the machine uses to guess whether the student passed or failed.

### Features vs Labels — Side by Side

| Concept | Also Called | Role | Notation | Example Column |
|---|---|---|---|---|
| **Label** | Target, Output, Dependent Variable | What the model predicts | `y` | `passed` (Yes/No), `house_price` |
| **Feature** | Input, Predictor, Independent Variable | What the model learns from | `X` | `age`, `income`, `attendance` |

![Features (X) are the input columns the model learns from; the label (y) is the single outcome column you want to predict — keep them separate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-04-features-vs-label-columns.png)

### How to Identify Features and Labels in a Dataset

```python
# import pandas to load our dataset
import pandas as pd

# load the student performance dataset
df = pd.read_csv("student_performance.csv")

# always inspect the dataset first — see all column names
print("Columns:", df.columns.tolist())

# preview the first 5 rows of the dataset
print(df.head())

# output will look something like this:
#   attendance  study_hours  mock_score  assignment_done  result
# 0    85           4.5          72             Yes        Pass
# 1    60           1.5          45             No         Fail
# 2    91           6.0          88             Yes        Pass

# the column we want to predict is 'result' — this is our LABEL (y)
y = df["result"]

# all other columns are our FEATURES (X) — these are the inputs
X = df.drop(columns=["result"])

# always verify by checking shapes
print("Features shape:", X.shape)   # (rows, number_of_input_columns)
print("Label shape:", y.shape)      # (rows,) — a single column / series
```

**How the code works:**
- We start by listing all column names — this forces you to consciously read every column before deciding which is the label.
- `df["result"]` extracts the label column as a **Series** (a single column). We call it `y` — the universal ML convention for labels.
- `df.drop(columns=["result"])` removes the label from the table. What remains is your feature matrix — called `X` in all ML code worldwide.
- The shape check confirms: `X.shape` should be `(rows, features)` and `y.shape` should be `(rows,)` — one value per row.

### What is Data Leakage and Why Is It Dangerous?

**Common Doubt:** *"Can I accidentally put the label inside the features?"*

Yes — and this is called **Data Leakage**. It is one of the most dangerous and common mistakes in ML.

- **What it is:** Data leakage happens when information that would not be available at prediction time is accidentally included in the training features — including the label itself.
- **Why it is dangerous:** The model sees the answer during training. It learns to "cheat" — and scores 100% during practice but fails completely in the real world.
- **Example:** Imagine building a model to predict if a student will fail — and accidentally including the column `final_result` as a feature. The model just reads that column and gets 100% accuracy. But when used in January before results are out, it has no data to predict from.

**Always double-check your feature matrix has no version of the label in it** — especially watch out for derived columns (e.g., if `result` is "Pass/Fail", make sure columns like `is_passed`, `score_category`, or `grade_letter` are also removed if they encode the same information).

---

## Applying Data Splitting Strategies

Now that you know your features and label, the next question is: **which part of the data should the machine learn from, and which part should you use to check if it learned correctly?**

This is where **splitting the data** comes in — and it is the step most beginners get wrong.

- **Official Definition:** A **Train/Validation/Test Split** is the process of dividing your dataset into three separate portions — one for the model to learn from, one to tune and evaluate during development, and one for a final unbiased performance check.
- **In Simple Words:** Think of it like preparing a student for a board exam.
  - **Training Set** = the textbook the student studies from.
  - **Validation Set** = the practice tests the student takes every week during preparation.
  - **Test Set** = the actual board exam — the student sees it only once, at the very end.
- **Real-Life Example:** A coaching institute never reveals the actual exam paper to students during practice — they use mock tests (validation) to track progress, and keep the real exam (test) untouched until the final day.

### Why Three Splits — Not Just Two?

| Split | Purpose | Seen During Training? |
|---|---|---|
| **Training Set** | Model learns patterns from this | Yes — it trains on this |
| **Validation Set** | Tune the model, check overfitting | No — used only for checking during development |
| **Test Set** | Final unbiased performance check | No — seen only once at the very end |

Using only a training and test split is like using the board exam as your practice test — you corrupt the final evaluation. The **Validation Set** protects the Test Set from being misused.

![Train vs validation vs test — study material, practice checks during development, and a final exam you only take once](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-05-train-val-test-split.png)

### What is Overfitting — and Why Splits Prevent It?

- **Official Definition:** **Overfitting** happens when a model learns the training data *too well* — including all its noise and specific quirks — and fails to generalise to new, unseen data.
- **In Simple Words:** The student memorised last year's question paper word-for-word. When a new question with a slightly different wording appears in the actual exam, they are completely lost.
- **The split solves this:** By testing on data the model has *never seen*, you can detect overfitting early — the model scores high on training data but low on validation. This is your signal to simplify.

### Common Split Ratios

- **60 / 20 / 20** — 60% training, 20% validation, 20% test (widely used for small-to-medium datasets; this is the ratio used in the code examples below)
- **70 / 15 / 15** — 70% training, 15% validation, 15% test (a good balance for most projects)
- **80 / 10 / 10** — 80% training, 10% validation, 10% test (used when you want the model to see more training data)
- For very large datasets (millions of rows), even 95/2.5/2.5 is acceptable — because 2.5% of a million rows still gives 25,000 test samples, which is more than enough.

### How to Split Data in Python — With Colab

```python
# import the train_test_split function from scikit-learn
from sklearn.model_selection import train_test_split

# import pandas to load data
import pandas as pd

# load the student performance dataset
df = pd.read_csv("student_performance.csv")

# separate features (X) and label (y) — standard ML convention
X = df.drop(columns=["result"])   # all columns except the target
y = df["result"]                   # only the target column

# always print the shape before splitting — to verify your data is loaded correctly
print("Total rows:", X.shape[0])
print("Total features:", X.shape[1])

# STEP 1: Split off the test set first — keep 20% for final evaluation
# random_state=42 means the split will be identical every time you run the code
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# STEP 2: From the remaining 80%, split into training (75%) and validation (25%)
# 75% of 80% = 60% of total; 25% of 80% = 20% of total
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

# verify the sizes of each split
print("\nTraining rows:", X_train.shape[0])     # ~60% of total data
print("Validation rows:", X_val.shape[0])       # ~20% of total data
print("Test rows:", X_test.shape[0])             # ~20% of total data
```

**How the code works:**
- `train_test_split` from `sklearn.model_selection` handles both shuffling and splitting in one call — never split data manually using index slices.
- We split in **two steps** because the function only does binary splits. First carve out the test (20%), then divide what remains into training (60%) and validation (20%).
- `random_state=42` seeds the random number generator — so your split is reproducible. Use the same seed across your team so everyone works with the same data division.
- Always print the row counts after splitting — a quick sanity check that the math is right.

### Avoiding Data Leakage During Splitting

**Common Doubt:** *"Can the split itself cause data leakage?"*

Yes — and here is how:

- **Mistake 1 — Scaling before splitting:** If you compute the mean and standard deviation of a column on the full dataset and then split, the test set has "seen" some information from the training set through the scaler. Always fit scalers only on training data.
- **Mistake 2 — Filling missing values before splitting:** If you fill missing values using the column mean of the full dataset, the test set is contaminated. Compute fill values only from the training set.
- **The Rule:** Split first. Then fit any transformation (scaling, encoding, imputation) on the training set only. Apply the same fitted transformation to the validation and test sets.

---

## Establishing and Evaluating Baselines

You have your features, label, and split data. Now, before building any complex model, a seasoned ML practitioner always asks: **"What is the simplest possible prediction I can make — and how good is it?"**

This is called the **Baseline**.

- **Official Definition:** A **Baseline Model** is the simplest possible model or rule that gives a performance benchmark. Any real ML model must beat this benchmark to be considered useful.
- **In Simple Words:** It is the "do-nothing smart" answer. For example, if 80% of your customers did NOT churn, a baseline would simply predict "No churn" for everyone — and it would be 80% accurate without any ML at all.
- **Real-Life Example:** A cricket team's target in a match is not perfection — it is beating the *par score* set by the pitch conditions. In ML, the baseline is your par score. Any model you build must score above it to prove it is actually learning something useful.

### Why Baselines Matter

- **They prevent wasted effort.** If your complex model achieves 82% accuracy, but the baseline is 80%, you have only gained 2% — hardly worth the complexity or cost of deployment.
- **They catch deceptively easy problems.** If your baseline is 99% accurate (because 99% of cases belong to the same class), the problem may not need ML at all — a simple business rule will do.
- **They give you a reality check.** A baseline tells you the floor — how low can your model go before it is worse than doing nothing.
- **They set a north star.** Every time you try a new algorithm or tune a parameter, you compare against the baseline to see if you are making real progress.

![A baseline is the floor score from the dumbest usable rule — any real model should beat it to justify complexity](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module2/session13/session13-06-baseline-benchmark-floor.png)

### Types of Baselines

| Baseline Type | Best For | What It Does |
|---|---|---|
| **Most Frequent Class** | Classification | Always predicts the most common label in training data |
| **Mean / Median Prediction** | Regression | Always predicts the average (or median) target value |
| **Random Prediction** | Any | Randomly guesses the output — sets the absolute floor |
| **Simple Business Rule** | Any | Uses a human-defined rule (e.g., "If age > 60, predict disease") |

### Building a Classification Baseline in Python

```python
# import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# load the student performance dataset
df = pd.read_csv("student_performance.csv")

# separate features and label
X = df.drop(columns=["result"])
y = df["result"]

# always check the label distribution before building a baseline
print("Label distribution:")
print(y.value_counts())
print(y.value_counts(normalize=True).mul(100).round(1))
# example output:
# Pass    720   (72%)
# Fail    280   (28%)
# so a baseline that always predicts "Pass" will score 72% automatically

# split into training and test set (80/20 split for this example)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# create a DummyClassifier — scikit-learn's built-in baseline
# strategy="most_frequent" means it always predicts the most common label from training data
baseline_model = DummyClassifier(strategy="most_frequent", random_state=42)

# train the baseline — it does not actually learn; it just records the most frequent label
baseline_model.fit(X_train, y_train)

# make predictions on the unseen test data
baseline_predictions = baseline_model.predict(X_test)

# evaluate: measure accuracy — what % of predictions were correct?
baseline_accuracy = accuracy_score(y_test, baseline_predictions)
print(f"\nBaseline Accuracy: {baseline_accuracy:.2%}")
# example output: Baseline Accuracy: 72.00%
# this makes sense — 72% of students passed, so always predicting "Pass" hits 72%
# any real model MUST score above 72% to be considered useful

# print the full classification report — precision, recall, F1 per class
print("\nBaseline Classification Report:")
print(classification_report(y_test, baseline_predictions))
```

**How the code works:**
- We start with `value_counts()` — this shows the label distribution, which tells us what accuracy a "do-nothing" model would achieve before writing a single line of ML logic.
- `DummyClassifier(strategy="most_frequent")` is a special scikit-learn model that does not learn anything. It just records the most common label from training data and always predicts that.
- We still call `.fit()` and `.predict()` — the exact same workflow as a real model. This is intentional: it builds muscle memory for the train-predict-evaluate pattern.
- The `classification_report` shows **Precision**, **Recall**, and **F1-score** per class — critical when classes are imbalanced (e.g., 72% Pass vs 28% Fail). Accuracy alone can be misleading in such cases.

### Building a Regression Baseline in Python

```python
# import DummyRegressor for regression problems
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# load a house pricing dataset
df = pd.read_csv("house_prices.csv")

# always check the label distribution for regression problems too
print("Price stats:")
print(df["price"].describe())
# this shows min, max, mean, median — your baseline will predict the mean

# separate features and label (price is the label)
X = df.drop(columns=["price"])
y = df["price"]

# split into training and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# create a DummyRegressor — strategy="mean" means always predict the average price from training data
baseline_reg = DummyRegressor(strategy="mean")

# train on training data — it records the mean of y_train
baseline_reg.fit(X_train, y_train)

# make predictions — every prediction will be the same number (the training mean)
baseline_preds = baseline_reg.predict(X_test)

# measure Mean Absolute Error — average difference between predicted and actual price
mae = mean_absolute_error(y_test, baseline_preds)

# measure Root Mean Squared Error — penalises large errors more than MAE
rmse = np.sqrt(mean_squared_error(y_test, baseline_preds))

# print results
print(f"\nBaseline Mean Absolute Error: ₹{mae:,.0f}")
print(f"Baseline RMSE: ₹{rmse:,.0f}")
# example output:
# Baseline Mean Absolute Error: ₹12,45,000
# Baseline RMSE: ₹18,20,000
# any real model must have LOWER error values than these
```

**How the code works:**
- `DummyRegressor(strategy="mean")` records the mean of `y_train` and always predicts that single number for every test case — no learning involved.
- `mean_absolute_error` computes the average ₹ difference between actual and predicted price. It is easy to interpret — "on average, we are off by ₹12.45 lakhs."
- `RMSE` (Root Mean Squared Error) penalises large prediction errors more than MAE — useful when outliers (very high or very low prices) matter.
- These two numbers are now your **benchmark floor** — every algorithm you try must beat both these numbers to be considered a meaningful improvement.

### Comparing a Baseline vs a Real Model — Side by Side

```python
# compare baseline vs a simple real model on the same student performance data
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier     # a simple real ML model
from sklearn.metrics import accuracy_score
import pandas as pd

# load data
df = pd.read_csv("student_performance.csv")
X = df.drop(columns=["result"])
y = df["result"]

# split into training and test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# BASELINE: always predict most frequent class
baseline = DummyClassifier(strategy="most_frequent", random_state=42)
baseline.fit(X_train, y_train)
baseline_acc = accuracy_score(y_test, baseline.predict(X_test))

# REAL MODEL: a simple decision tree that actually learns from features
real_model = DecisionTreeClassifier(max_depth=3, random_state=42)   # max_depth=3 keeps it simple
real_model.fit(X_train, y_train)
real_acc = accuracy_score(y_test, real_model.predict(X_test))

# print the comparison
print(f"Baseline Accuracy:  {baseline_acc:.2%}")
print(f"Real Model Accuracy: {real_acc:.2%}")

# calculate the improvement over baseline
improvement = real_acc - baseline_acc
print(f"Improvement over baseline: {improvement:.2%}")
# example output:
# Baseline Accuracy:  72.00%
# Real Model Accuracy: 83.50%
# Improvement over baseline: 11.50%
# the model beat the baseline by 11.5 percentage points — this is meaningful progress
```

**How the code works:**
- We train both a baseline and a real model using the exact same training data and the exact same test data — so the comparison is fair.
- `DecisionTreeClassifier(max_depth=3)` is a simple real ML model (you will learn it in detail next session). For now, think of it as a model that actually reads the features and learns patterns.
- The improvement over baseline (11.5%) tells us the real model is genuinely learning from the features — it is not just guessing the most common answer.
- If the improvement had been 0% or negative, it would mean the model learned nothing useful — and we would need to revisit our features, data, or approach.

---

## Putting It All Together — End-to-End ML Workflow in Colab

Let us now run through the complete workflow using a single real-world scenario, exactly as you would in a Colab notebook from start to finish.

**Scenario:** A bank wants to know — *"Will this loan applicant default (fail to repay) or not?"*

```python
# ============================================================
# FULL ML WORKFLOW: Loan Default Prediction
# Run each block in a separate Colab cell for best experience
# ============================================================

# CELL 1: IMPORTS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Libraries loaded successfully!")

# CELL 2: PROBLEM FRAMING (written as comments — this is your planning cell)
# Question: Will this loan applicant default on their loan?
# ML Type: Classification (Yes = Default, No = Repaid)
# Label: 'default' column (Yes/No)
# Features: income, loan_amount, credit_score, employment_years, loan_purpose
# Metric: Accuracy + F1-score (because defaults are rare — class imbalance)

# CELL 3: LOAD AND INSPECT DATA
df = pd.read_csv("loan_applicants.csv")

print("Dataset shape:", df.shape)        # how many rows and columns?
print("\nFirst 5 rows:")
print(df.head())                          # preview the data
print("\nColumn data types:")
print(df.dtypes)                          # check if types are correct
print("\nMissing values:")
print(df.isnull().sum())                  # check for nulls

# CELL 4: CHECK LABEL DISTRIBUTION
print("Label distribution:")
print(df["default"].value_counts())
print(df["default"].value_counts(normalize=True).mul(100).round(1))
# example output:
# No     8200  (82%)  — majority did NOT default
# Yes    1800  (18%)  — minority DID default
# this is imbalanced — baseline will score 82% by always predicting "No"

# CELL 5: SEPARATE FEATURES AND LABEL
X = df.drop(columns=["default"])   # all input columns
y = df["default"]                   # the target column

print("Features shape:", X.shape)
print("Label shape:", y.shape)

# CELL 6: SPLIT DATA (60/20/20 split)
# first split: carve out 20% for final test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# second split: of remaining 80%, use 75% for training (=60% total) and 25% for validation (=20% total)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

print(f"Training rows:   {X_train.shape[0]}")   # ~60%
print(f"Validation rows: {X_val.shape[0]}")     # ~20%
print(f"Test rows:       {X_test.shape[0]}")    # ~20%

# CELL 7: ESTABLISH BASELINE
baseline = DummyClassifier(strategy="most_frequent", random_state=42)
baseline.fit(X_train, y_train)
baseline_preds = baseline.predict(X_test)

baseline_acc = accuracy_score(y_test, baseline_preds)
print(f"\nBaseline Accuracy: {baseline_acc:.2%}")
# output: Baseline Accuracy: 82.00%
# makes sense — 82% of applicants did not default
# always predicting "No" gives 82% without any learning

print("\nBaseline Classification Report:")
print(classification_report(y_test, baseline_preds))
# the report will show 0% recall for the "Yes" class
# meaning the baseline NEVER catches an actual defaulter — it misses every one of them
# any real model must not only beat 82% accuracy but also actually detect "Yes" cases
```

**How the code works:**
- Each `CELL` comment represents a separate Colab notebook cell — this is good Colab hygiene. Separate cells for imports, framing, loading, splitting, and baselining makes your notebook readable and easy to debug.
- The label distribution check reveals a critical insight — 82% vs 18% is a class imbalance. The baseline will score 82% but miss *every single defaulter* (recall = 0% for "Yes"). This is why the classification report matters more than accuracy alone.
- We split in two steps to correctly achieve a 60/20/20 distribution across training, validation, and test sets.
- The baseline now gives us a clear target: any real model must beat 82% accuracy AND show meaningful recall for the "Yes" (defaulter) class.

---

## Good ML Habits to Build from Day One

The ML Workflow is not just about steps — it is also about the **habits** that separate a careful ML practitioner from a careless one. These habits will save you hours of debugging later.

- **Always check your label distribution first.** If 99% of your data belongs to one class, accuracy is a useless metric — use precision, recall, or F1 instead.
- **Always set `random_state`.** Without a fixed random state, every run gives a different split — making your results impossible to reproduce or compare with a teammate.
- **Never touch the test set until you are done.** Looking at test data before your model is final is like peeking at the board exam answer sheet. It biases every decision you make afterward.
- **Start with the simplest model, not the most complex.** Complexity does not equal accuracy. A simple model that beats the baseline is always better than a complex model that merely matches it.
- **Document your problem frame in your Colab notebook.** Write in a Markdown cell: "I want to predict X using Y, measured by Z." This keeps your thinking clear and your notebook usable by others.
- **Commit your Colab notebooks to GitHub regularly.** Use File → Save a copy in GitHub to version-control your work. Never rely on just one cloud save.

---

## Key Takeaways

- **Google Colab** is your cloud-based Python lab for this course — no installation required. Set up your runtime, understand the cell-based interface, and import all libraries before starting any ML session.
- **The ML Workflow** is a 6-step process: Frame → Collect → Engineer Features → Split → Baseline → Evaluate. Following this workflow every time prevents costly, hard-to-trace mistakes.
- **Problem Framing** converts a real-world question into a clear ML task by defining: what to predict (Label), what to use as inputs (Features), and how to measure success (metric).
- **Features (X)** are the inputs the model learns from; the **Label (y)** is what the model is trying to predict. Confusing the two — or leaking the label into the features — is one of the most dangerous mistakes in ML.
- **The Train/Validation/Test Split** protects the integrity of your evaluation — split first, transform later. The test set is used exactly once, at the very end. A **Baseline** is your benchmark — any model you build must beat it to prove it is genuinely learning.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Is |
|---|---|
| **Google Colab** | Free cloud-based Python notebook environment with pre-installed ML libraries |
| `Shift + Enter` | Run a Colab cell and move to the next |
| `sklearn.model_selection` | scikit-learn module for splitting and cross-validating data |
| `train_test_split(X, y, test_size, random_state)` | Splits features and labels into training and test portions |
| `DummyClassifier(strategy="most_frequent")` | Baseline model that always predicts the most common class |
| `DummyRegressor(strategy="mean")` | Baseline model that always predicts the average target value |
| `accuracy_score(y_true, y_pred)` | Measures % of correct predictions |
| `mean_absolute_error(y_true, y_pred)` | Average absolute difference between actual and predicted values |
| `mean_squared_error(y_true, y_pred)` | Average squared difference — penalises large errors more |
| `classification_report(y_true, y_pred)` | Full precision, recall, and F1-score breakdown per class |
| **Label / Target (y)** | The column the model is trained to predict |
| **Features (X)** | The input columns the model learns from |
| **Training Set** | Data the model learns from (~60% of data) |
| **Validation Set** | Data used during development to tune and evaluate the model (~20%) |
| **Test Set** | Held-out data used for a final, unbiased evaluation (~20%) |
| **Baseline** | The simplest benchmark — any real model must beat it to be useful |
| **Data Leakage** | Accidentally including the label or future information inside the features |
| **Overfitting** | Model memorises training data and fails on new unseen data |
| **random_state** | A seed number to make random operations reproducible |
| **Classification** | ML task where the output is a category (e.g., Pass/Fail, Spam/Not Spam) |
| **Regression** | ML task where the output is a number (e.g., price, score, temperature) |
| **Clustering** | ML task where the model groups similar data points without labels |
| **Precision** | Of all "Yes" predictions, how many were actually "Yes"? |
| **Recall** | Of all actual "Yes" cases, how many did the model catch? |
| **F1-score** | Harmonic mean of precision and recall — use when classes are imbalanced |
