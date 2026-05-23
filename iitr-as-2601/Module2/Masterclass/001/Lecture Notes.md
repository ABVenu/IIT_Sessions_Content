# ML Workshop: Credit Card Fraud Detection with Anomaly Detection

## What You Will Learn in This Session

In the previous part of the course, you moved from **Colab habits and the ML workflow** through **data preparation**, **correct train-test splitting**, **regression**, **classification**, **unsupervised learning**, and **time series**. You saw how models are trained, how errors are measured, and why a high **accuracy** score can still hide a useless model when one class is very rare.

This session brings those ideas together on one realistic job: **catching credit card fraud**. You will work on a large transaction dataset (**50,000 rows**), build an **anomaly detection** pipeline, and evaluate it the way a bank team would — using **precision**, **recall**, and a **confusion matrix**, not accuracy alone.

By the end of this session, you will be able to:

- Revisit the core **Module 2** ideas — workflow, prep, modelling, and evaluation — as one connected story.
- Explain the **PayGuard** business problem and why **anomaly detection** fits fraud.
- Load and explore a **large transaction dataset** in Google Colab from the course S3 link.
- Clean, encode, and split data **without leakage**.
- Train an **Isolation Forest** on normal transactions and flag suspicious ones.
- Measure performance with **precision**, **recall**, and **F1**, and interpret trade-offs for banking.

---

## Module 2 at a Glance — Quick Revision

Before you build the PayGuard pipeline, let us quickly revisit the **gist of Module 2**. This section is a **revision reference**, not new theory. Each term below uses the same pattern you have seen earlier: **Official Definition**, **In Simple Words**, and **Real-Life Example**. Work through it at your own pace, then move to the hands-on steps.

**How to use this section:** Read each block in order. If a term already feels familiar, skip to the next one. Keep your Colab notebook open so you can start Step 1 when you are ready.

---

### Google Colab and the ML Workflow

**Google Colab**
- **Official Definition:** A browser-based notebook environment to write and run Python in cells.
- **In Simple Words:** You type code in boxes, press Run, and see the answer below — no heavy setup on your laptop.
- **Real-Life Example:** Like trying recipes in a shared kitchen where ingredients are already on the shelf.

**Machine Learning Workflow**
- **Official Definition:** The ordered stages from business problem → data → prepare → split → train model → evaluate → improve.
- **In Simple Words:** A checklist so you do not train on dirty data or test on data the model already “saw.”
- **Real-Life Example:** Like preparing for boards — syllabus, notes, practice tests, then the real exam (not the other way around).

![Machine learning workflow — business problem through data preparation, train-test split, model training, and evaluation as one connected checklist](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-01-ml-workflow.png)

**Setup check:** Open a blank Colab notebook and rename it `payguard_fraud_detection.ipynb`. Run `print("PayGuard ready")` once. If you see the text below the cell, your environment is ready for Step 1.

---

### Data, Features, Target, and Model

**Dataset / Features / Target**
- **Official Definition:** A **dataset** is a table of examples; **features** are input columns; the **target** is the outcome you care about.
- **In Simple Words:** Features are clues; the target is the answer you want the machine to learn or check against.
- **Real-Life Example:** Predicting rain — features = humidity, clouds; target = did it rain yes/no.

**Model / Training / Prediction**
- **Official Definition:** A **model** is the learned rule; **training** fits it on past data; **prediction** applies it to new rows.
- **In Simple Words:** Training is practice; prediction is the real test match.
- **Real-Life Example:** A cricket coach studies old match videos (train), then advises on a new opponent (predict).

---

### Regression vs Classification

**Regression**
- **Official Definition:** Predicting a **continuous number** (amount, score, temperature).
- **In Simple Words:** The answer is “how much,” not “which bucket.”
- **Real-Life Example:** Predicting tomorrow’s temperature in °C.

**Classification**
- **Official Definition:** Predicting a **category** (fraud / not fraud, pass / fail).
- **In Simple Words:** The answer is a label from a fixed list.
- **Real-Life Example:** Spam vs not spam in your inbox.

**Check your understanding:** Fraud detection is **classification** because the label is fraud or not fraud — even when you use an **unsupervised** method to flag unusual rows first.

---

### Data Preparation

**Missing Values / Duplicates / Scaling / Encoding**
- **Official Definition:** Cleaning steps so the table is complete, unique, on comparable scales, and numeric where needed.
- **In Simple Words:** Fix blanks, remove copies, and put columns on fair footing before training.
- **Real-Life Example:** Before a group photo, everyone stands in a line (scale) and name tags use the same format (encode categories).

**Common doubt:** If you fill missing values using the **whole** dataset before splitting, information from the test set leaks into training. **Fix:** split first, then compute averages only on the train split.

---

### Train-Test Split and Data Leakage

**Train-Test Split**
- **Official Definition:** Holding out a portion of data so the model is evaluated on unseen rows.
- **In Simple Words:** Study from some papers; write the exam on different papers.
- **Real-Life Example:** Practising with 2024 papers and testing on a 2025 paper.

**Data Leakage**
- **Official Definition:** Using information in training that would not exist at real prediction time.
- **In Simple Words:** The model peeks at the answer key during “practice.”
- **Real-Life Example:** Predicting exam marks but training with the final marks already filled in the homework sheet.

![Split first, then scale — wrong order leaks test statistics into training; correct order fits the scaler on train only and transforms test](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-05-split-first-no-leakage.png)

**Class Imbalance**
- **Official Definition:** When one class is much rarer than the other (e.g. 2% fraud).
- **In Simple Words:** Almost everyone is “normal,” so a lazy model can look accurate while catching zero fraud.
- **Real-Life Example:** 98 students pass and 2 fail — always guessing “pass” gives 98% accuracy but helps no one who failed.

![Class imbalance trap — ~98% legitimate vs ~2% fraud means high accuracy can hide a model that catches zero fraud](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-02-class-imbalance.png)

---

### Regression Metrics (When the Target Is a Number)

**MAE / RMSE / R-squared**
- **Official Definition:** **MAE** = average absolute error; **RMSE** = penalises large errors more; **R²** = how much variance the model explains.
- **In Simple Words:** They tell you how far numeric predictions are from truth.
- **Real-Life Example:** Guessing a friend’s height — MAE is average cm you were wrong.

**Regularization (Ridge / Lasso)**
- **Official Definition:** Penalties that stop the model from overfitting by keeping weights small or sparse.
- **In Simple Words:** A gentle brake so the model does not memorise noise.
- **Real-Life Example:** A teacher says “explain in five bullet points max” so you focus on main ideas.

---

### Classification Basics

**Logistic Regression / Sigmoid / Probability / Threshold**
- **Official Definition:** A classifier that outputs **probability** of class 1, then applies a **threshold** (often 0.5) to decide the label.
- **In Simple Words:** The model says “78% chance fraud” — you choose where to cut off “fraud” vs “safe.”
- **Real-Life Example:** A gate opens only if security confidence is above 70%, not 50%.

**Confusion Matrix (TP, TN, FP, FN)**
- **Official Definition:** A table comparing actual vs predicted labels for both classes.
- **In Simple Words:** Four buckets — right fraud, right safe, false alarm, missed fraud.
- **Real-Life Example:** Fire alarm: true fire + alarm, no fire + silent, false alarm, real fire but no alarm.

![Confusion matrix for fraud detection — true negatives, false positives (false alarms), false negatives (missed fraud), and true positives (caught fraud)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-03-confusion-matrix.png)

---

### Tree Models and Advanced Classification Metrics

**Decision Tree / Random Forest**
- **Official Definition:** **Tree** = yes/no rules; **Forest** = many trees vote together for stability.
- **In Simple Words:** A flowchart of questions, or many flowcharts averaged.
- **Real-Life Example:** Loan desk asks income, then credit score, then decides.

**Precision / Recall / F1 / ROC-AUC**
- **Official Definition:** **Precision** = of all “fraud” alerts, how many were real; **Recall** = of all real fraud, how many you caught; **F1** balances both; **ROC-AUC** measures ranking ability across thresholds.
- **In Simple Words:** Precision = trust the alarm; Recall = do not miss thieves; F1 = both matter.
- **Real-Life Example:** Airport security — loud false alarms (low precision) vs missed threats (low recall).

![Precision vs recall for PayGuard — trust in fraud alerts versus fraction of real fraud caught; F1 balances both when missing fraud is costly](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-04-precision-recall.png)

**Activity:** Write one sentence: “For PayGuard, missing fraud is usually worse than blocking one real customer briefly — so we care about **recall** as much as **precision**.”

---

### Unsupervised Learning, Clustering, PCA, and Anomaly Detection

**Unsupervised Learning**
- **Official Definition:** Learning patterns **without** using a label column during training.
- **In Simple Words:** The machine groups or scores rows by similarity alone.
- **Real-Life Example:** Sorting WhatsApp forwards into themes without pre-labelled folders.

**K-Means / PCA**
- **Official Definition:** **K-Means** groups similar points; **PCA** compresses many columns into fewer summary columns for plotting.
- **In Simple Words:** K-Means = seating guests by similarity; PCA = summarising a long form into two main scores.
- **Real-Life Example:** Shopper segments (K-Means); drawing a 2D map of customers with many habits (PCA).

**Anomaly Detection**
- **Official Definition:** Flagging data points that do not match “normal” behaviour.
- **In Simple Words:** Find the odd transaction that does not look like the customer’s usual pattern.
- **Real-Life Example:** Your bank SMS: “Was this ₹85,000 purchase at 2 AM in another city — you?”

![Anomaly detection — learn normal spending patterns, then flag transactions that sit far outside the usual cluster](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-07-anomaly-detection.png)

---

### Time Series — Quick Link

**Time Series / Trend / Seasonality / Time-Aware Split**
- **Official Definition:** Data where **order in time** matters; splits must respect chronology.
- **In Simple Words:** Do not shuffle months of sales like a deck of cards.
- **Real-Life Example:** Diwali sales spike every year — that pattern has a calendar rhythm.

**Link to fraud:** Fraud spikes at odd hours or before holidays. Today we use an **hour** column as a feature; a full time-series model is optional stretch reading after class.

---

## The PayGuard Problem Statement

You join **PayGuard**, a payment security team. Every second, card swipes arrive: amount, merchant type, location distance, and more. **Fraud is about 2%** of transactions — rare but costly.

**Business goal:** Flag suspicious swipes **before** money leaves the account, without blocking every genuine customer.

**Why anomaly detection here?**
- Fraud often looks like a **weird** row compared to normal spending — high amount, odd hour, far from home, many swipes in one hour.
- Banks also use supervised models when labels exist. In the steps below, you train **Isolation Forest** on **normal-only** training rows, then check alerts against fraud labels on the test set (labels used only for **evaluation**, not for fitting the anomaly model).

![PayGuard problem — rare fraudulent card swipes (~2% of 50,000 rows), transaction features, and the goal to flag suspicious activity without blocking every genuine customer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-06-payguard-problem.png)

**Dataset you will use:** `payguard_transactions.csv` — **50,000 transactions**, 10 columns, **~1,000 fraud** rows (2%). The file is hosted on the course S3 bucket. In the next step you will load it with one `read_csv` line — no manual upload needed.

**Dataset URL (hosted on S3):**  
`https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/payguard_transactions.csv`

| Column | Meaning |
|--------|---------|
| `transaction_id` | Unique ID (not used as a feature) |
| `amount` | Transaction amount in ₹ |
| `hour` | Hour of day (0–23) |
| `day_of_week` | Mon–Sun |
| `merchant_category` | Type of merchant |
| `distance_from_home_km` | Distance from customer’s usual city |
| `transactions_last_1hr` | Count of swipes in the last hour |
| `is_international` | 1 if international, else 0 |
| `card_age_months` | How old the card is |
| `is_fraud` | 1 = fraud, 0 = legitimate (for evaluation) |

**Activity:** In your notebook, add a Markdown cell with your own one-line problem statement: *“PayGuard must detect rare fraudulent card swipes without relying only on accuracy.”*

![PayGuard end-to-end pipeline — load from S3, explore imbalance, encode features, split and scale, train Isolation Forest on normal rows, evaluate with precision/recall, review flagged transactions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-09-payguard-pipeline.png)

---

## Step 1 — Open Colab and Load the Dataset from S3

Run the full cell below from top to bottom. Copy-paste it as-is into one Colab code cell. The PayGuard CSV (~2.4 MB, 50,000 rows) downloads directly from the course S3 bucket into your notebook — no file picker, no manual upload.

```python
# Import pandas for tables and csv reading
import pandas as pd

# Import numpy for numeric arrays and conditions
import numpy as np

# Import matplotlib for quick charts during exploration
import matplotlib.pyplot as plt

# Import train_test_split to separate train and test data
from sklearn.model_selection import train_test_split

# Import StandardScaler to scale numeric features fairly
from sklearn.preprocessing import StandardScaler

# Import IsolationForest for anomaly detection
from sklearn.ensemble import IsolationForest

# Import LogisticRegression for optional supervised comparison
from sklearn.linear_model import LogisticRegression

# Import metrics to evaluate fraud detection properly
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    accuracy_score,
)

# Store the public S3 URL for the PayGuard transaction dataset (50,000 rows)
DATA_URL = "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/payguard_transactions.csv"

# Load the CSV directly from S3 into a DataFrame named df
df = pd.read_csv(DATA_URL)

# Print how many rows and columns you received
print("Dataset loaded from S3.")
print("Shape (rows, columns):", df.shape)

# Show the first five rows so you can eyeball the data
print(df.head())
```

**How the code works:**

- **`DATA_URL`** points to `payguard_transactions.csv` on the course **S3** bucket (`s13n-curr-images-bucket`, region `ap-south-1`).
- **`pd.read_csv(DATA_URL)`** downloads and parses the file in one step — works in **Google Colab**, local Jupyter, or any environment with internet access.
- **`df.shape`** should show **(50000, 10)** when the load succeeds.

**Common doubt:** The cell fails with a connection or timeout error. **Fix:** Run the cell again; check your internet. If the institute network blocks S3, ask your instructor for an offline copy from the course `data` folder and use `df = pd.read_csv("payguard_transactions.csv")` after uploading that file once to Colab.

---

## Step 2 — Explore the Data Like an Analyst

Understanding the table before modelling prevents silly mistakes (wrong column types, surprise imbalance).

```python
# Print column names and non-null counts using df.info()
print("=== Column info ===")
print(df.info())

# Print basic statistics for numeric columns (amount, hour, distance, etc.)
print("\n=== Numeric summary ===")
print(df.describe())

# Count how many fraud vs legitimate rows exist
print("\n=== Fraud counts ===")
print(df["is_fraud"].value_counts())

# Compute fraud percentage — expect around 2%
fraud_pct = df["is_fraud"].mean() * 100
print(f"Fraud percentage: {fraud_pct:.2f}%")

# Count transactions per merchant category
print("\n=== Merchant category counts ===")
print(df["merchant_category"].value_counts())

# Build a simple bar chart of fraud vs not fraud
df["is_fraud"].value_counts().plot(kind="bar", color=["green", "red"])
plt.title("Legitimate vs Fraud Transactions")
plt.xlabel("is_fraud (0 = legit, 1 = fraud)")
plt.ylabel("Count")
plt.show()

# Compare average amount for fraud vs non-fraud (fraud is usually higher on average)
avg_amount = df.groupby("is_fraud")["amount"].mean()
print("\n=== Average amount by class ===")
print(avg_amount)
```

**How the code works:**

- **`value_counts()`** on `is_fraud` shows the **class imbalance** — most rows are 0.
- **`groupby`** proves fraud rows often have different **average amount** — a clue your model can use later.
- In the bar chart, the fraud bar is **tiny** compared to legitimate transactions — that visual imbalance is why accuracy alone is misleading.

**Activity:** Note the fraud percentage in your notebook. If accuracy later is ~98%, say whether that number alone proves the model is good — answer: **no**, because guessing “not fraud” every time would also score ~98%.

---

## Step 3 — Prepare Features (No Leakage)

We drop the ID column, encode categories, and keep the target separate. We do **not** scale yet — scaling statistics must come **after** the split.

```python
# Copy the dataframe so the original S3 load stays untouched
data = df.copy()

# Remove transaction_id — it is just a name tag, not a behaviour signal
data = data.drop(columns=["transaction_id"])

# Separate feature matrix X and target vector y
X = data.drop(columns=["is_fraud"])
y = data["is_fraud"]

# Convert day_of_week and merchant_category from text to numbers using one-hot encoding
# drop_first=True avoids duplicate columns that confuse some models
X_encoded = pd.get_dummies(X, columns=["day_of_week", "merchant_category"], drop_first=True)

# Print the new feature column count after encoding
print("Number of feature columns after encoding:", X_encoded.shape[1])
print("First few column names:", list(X_encoded.columns[:8]))
```

**How the code works:**

- **`get_dummies`** turns `merchant_category = travel` into columns like `merchant_category_travel` with 0/1 values.
- **`drop_first=True`** keeps categories without perfect duplication (standard trick for linear models).
- **`y`** stays aside until evaluation — the anomaly model will train **without** using `y` inside `fit` for the Isolation Forest on normal rows only.

---

## Step 4 — Train-Test Split First, Then Scale

This order matches what you practised earlier: **split → fit scaler on train → transform test**.

```python
# Split 80% train and 20% test; stratify=y keeps ~2% fraud in both sets
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Create a scaler object (empty until we fit it)
scaler = StandardScaler()

# Learn mean and std from TRAINING rows only
scaler.fit(X_train)

# Transform both train and test using training statistics only
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Print shapes to confirm sizes (~40,000 train, ~10,000 test)
print("Train size:", X_train_scaled.shape[0])
print("Test size:", X_test_scaled.shape[0])
print("Fraud in train:", y_train.sum(), "| Fraud in test:", y_test.sum())
```

**How the code works:**

- **`stratify=y`** keeps fraud rate similar in train and test — important for fair evaluation.
- **`scaler.fit(X_train)`** learns scaling only from training data — **no leakage**.
- Test rows are scaled with train means/stds — exactly what happens in production when new swipes arrive.

---

## Step 5 — Train Isolation Forest on Normal Transactions Only

**Isolation Forest** builds random trees that isolate points quickly; **weird** points need fewer splits to stand alone.

```python
# Select only LEGITIMATE rows from the training set for fitting the anomaly model
normal_mask = y_train == 0
X_train_normal = X_train_scaled[normal_mask]

# Print how many normal rows we train on
print("Normal training rows:", X_train_normal.shape[0])

# Create the Isolation Forest model
# n_estimators=100 builds 100 random trees for stable scoring
# contamination=0.02 hints that about 2% of data may be outliers (matches our fraud rate)
# random_state=42 gives reproducible results each time you run the notebook
iso_model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42,
)

# Fit ONLY on normal behaviour — the model learns what typical swipes look like
iso_model.fit(X_train_normal)

# Predict on the TEST set: sklearn returns 1 = normal, -1 = anomaly
iso_pred_raw = iso_model.predict(X_test_scaled)

# Convert to 1 = flagged as fraud, 0 = predicted normal (easier to compare with y_test)
y_pred_iso = np.where(iso_pred_raw == -1, 1, 0)

# Show how many transactions we flagged as suspicious on the test set
print("Test rows flagged as anomaly:", y_pred_iso.sum())
```

**How the code works:**

- **`X_train_normal`** teaches “usual” spending — amounts, hours, distances for honest customers.
- **`contamination=0.02`** tells the algorithm roughly how aggressive to be — aligned with 2% fraud rate.
- **`predict`** on test does **not** use test labels — labels come only in the next evaluation step.

**Integrated “why”:** Banks often retrain on recent **normal** weeks, then flag deviations. New fraud types may look anomalous even before analysts label them.

![Isolation Forest intuition — random splits isolate odd points quickly; train only on normal transactions, then flag test rows that do not fit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-08-isolation-forest.png)

---

## Step 6 — Evaluate Like a Bank (Not Like a Exam Percentage)

```python
# Accuracy — include for contrast, but do NOT trust it alone on imbalanced data
acc = accuracy_score(y_test, y_pred_iso)
print(f"Accuracy: {acc * 100:.2f}%")

# Precision — of all fraud alerts, how many were real fraud
prec = precision_score(y_test, y_pred_iso, zero_division=0)
print(f"Precision: {prec:.3f}")

# Recall — of all real fraud in test, how many we caught
rec = recall_score(y_test, y_pred_iso, zero_division=0)
print(f"Recall: {rec:.3f}")

# F1 — balance between precision and recall
f1 = f1_score(y_test, y_pred_iso, zero_division=0)
print(f"F1 Score: {f1:.3f}")

# Confusion matrix with labels [legit, fraud]
cm = confusion_matrix(y_test, y_pred_iso)
print("\nConfusion Matrix (rows = actual, cols = predicted):")
print(cm)

# Pretty text report with precision/recall per class
print("\nClassification Report:")
print(classification_report(y_test, y_pred_iso, target_names=["Legit", "Fraud"], zero_division=0))

# Baseline: always predict "not fraud"
baseline_acc = (y_test == 0).mean()
print(f"\nBaseline 'always legit' accuracy: {baseline_acc * 100:.2f}%")
print("If model accuracy is close to baseline but recall is low, the model is not doing its job.")
```

**How the code works:**

- **`confusion_matrix`** shows **false positives** (customer blocked wrongly) and **false negatives** (fraud missed).
- **`classification_report`** prints precision/recall for each class in one view.
- Comparing **`acc`** to **`baseline_acc`** shows why fraud teams stress **recall** and **F1**, not accuracy alone.

**Activity:** In your notebook, write one sentence: how many **false negatives** (missed fraud) your confusion matrix shows, and whether that number would worry PayGuard.

---

## Step 7 — Inspect Flagged Transactions (Analyst View)

Numbers are not enough — analysts open flagged rows and look for patterns.

```python
# Put test features, true label, and prediction into one table for inspection
inspect_df = X_test.copy()
inspect_df["actual_fraud"] = y_test.values
inspect_df["predicted_fraud"] = y_pred_iso

# Keep rows where the model raised an alert
flagged = inspect_df[inspect_df["predicted_fraud"] == 1]

# Show ten flagged rows sorted by amount (high amounts often dominate fraud stories)
print("Sample of flagged transactions (top 10 by amount):")
print(
    flagged.sort_values("amount", ascending=False).head(10)[
        [
            "amount",
            "hour",
            "distance_from_home_km",
            "transactions_last_1hr",
            "is_international",
            "actual_fraud",
        ]
    ]
)

# Count how many flagged rows were actually fraud (true positives) vs false alarms
print("\nAmong flagged rows:")
print("Actually fraud (true alerts):", ((flagged["actual_fraud"] == 1)).sum())
print("Actually legit (false alarms):", ((flagged["actual_fraud"] == 0)).sum())
```

**How the code works:**

- **`flagged`** is what a human analyst would review each morning.
- Sorting by **`amount`** surfaces dramatic cases for class discussion (night-time, far distance, burst swipes).

---

## Step 8 — Optional Supervised Comparison (Same Split, Same Metrics)

This short block connects anomaly detection to **classification** you practised earlier. It is optional if time is short.

```python
# Train logistic regression on the TRAINING set with real labels (supervised approach)
log_model = LogisticRegression(max_iter=1000, random_state=42)
log_model.fit(X_train_scaled, y_train)

# Predict fraud labels on the test set
y_pred_log = log_model.predict(X_test_scaled)

# Print the same metrics for side-by-side discussion
print("=== Logistic Regression (supervised) ===")
print(f"Precision: {precision_score(y_test, y_pred_log, zero_division=0):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred_log, zero_division=0):.3f}")
print(f"F1:        {f1_score(y_test, y_pred_log, zero_division=0):.3f}")

print("\n=== Isolation Forest (anomaly) ===")
print(f"Precision: {precision_score(y_test, y_pred_iso, zero_division=0):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred_iso, zero_division=0):.3f}")
print(f"F1:        {f1_score(y_test, y_pred_iso, zero_division=0):.3f}")
```

**How the code works:**

- **Logistic Regression** uses **labels** during training — strong when labels are trustworthy and balanced enough.
- **Isolation Forest** learned only **normal** patterns — useful when fraud is rare or new patterns appear.
- Compare which model achieved higher **recall** on your test split, and note whether extra false alarms would be acceptable for PayGuard.

![Isolation Forest (unsupervised, normal-only training) vs logistic regression (supervised with labels) — same split and same precision, recall, and F1 metrics for side-by-side comparison](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/masterclass001-10-unsupervised-vs-supervised.png)

---

## Step 9 — Simple Visual Check (Amount vs Hour)

A quick plot helps non-coders see separation between normal and fraud points.

```python
# Build a small sample for plotting so the chart stays readable (5000 random test indices)
rng = np.random.default_rng(42)
sample_size = min(5000, len(y_test))
idx = rng.choice(len(y_test), size=sample_size, replace=False)

# Plot amount vs hour; colour by actual fraud label
plt.figure(figsize=(8, 5))
for label, color, name in [(0, "green", "Legit"), (1, "red", "Fraud")]:
    mask = y_test.values[idx] == label
    plt.scatter(
        X_test["hour"].values[idx][mask],
        X_test["amount"].values[idx][mask],
        alpha=0.4,
        s=10,
        c=color,
        label=name,
    )
plt.xlabel("Hour of day")
plt.ylabel("Amount (₹)")
plt.title("PayGuard sample: amount vs hour (actual labels)")
plt.legend()
plt.show()
```

**How the code works:**

- Fraud points (red) often sit at **unusual hours** or **high amounts** — the same patterns Isolation Forest exploits in many dimensions at once.

---

## How This Document Is Organised

Follow the sections in this order for a complete end-to-end build:

1. **Module 2 at a Glance** — revision reference for key terms and ideas.
2. **The PayGuard Problem Statement** — business context, dataset description, and S3 link.
3. **Steps 1–9** — load data, explore, prepare, model, evaluate, inspect, compare, and visualise.
4. **Key Takeaways** — summary of what matters for fraud detection and what comes next in the course.

---

## Key Takeaways

- **Module 2** gave you a full toolbox — workflow, prep, splits, regression, classification, unsupervised ideas, and time-aware thinking; this session **applied** them on **PayGuard** fraud data.
- **Fraud is imbalanced** (~2% in 50,000 rows) — high **accuracy** can mislead; use **precision**, **recall**, **F1**, and the **confusion matrix**.
- **Anomaly detection** with **Isolation Forest** learns **normal** swipes, then flags rows that do not fit — a realistic bank pattern when fraud is rare or new.
- Always **split before scaling**, and fit the scaler only on **train** — the same **leakage** rules you practised earlier still apply.
- In upcoming work you will **compare and save models** for deployment — today’s metric habits (especially **recall** for fraud) carry straight into that step.

---

## Important Commands, Libraries, and Terminologies

| Term / Library | Quick meaning |
|----------------|---------------|
| `pandas` / `DataFrame` | Table toolkit — load CSV, explore, slice rows |
| `train_test_split` | Hold out test data; use `stratify` for rare fraud |
| `StandardScaler` | Scale numbers using train means/stds only |
| `pd.get_dummies` | Turn text categories into 0/1 columns |
| `IsolationForest` | Unsupervised anomaly detector (isolates odd points) |
| `LogisticRegression` | Supervised classifier with probabilities |
| `confusion_matrix` | TP, TN, FP, FN table |
| `precision_score` | Trust in “fraud” alerts |
| `recall_score` | Fraction of real fraud caught |
| `f1_score` | Balance precision and recall |
| `contamination` | Expected outlier rate hint for Isolation Forest |
| **Anomaly** | Row that does not match normal training pattern |
| **Class imbalance** | One label much rarer than the other |
| **Data leakage** | Test information sneaking into training steps |
| **Stratified split** | Keep fraud % similar in train and test |
| **`DATA_URL` / S3 CSV** | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/payguard_transactions.csv` |
| **`pd.read_csv(DATA_URL)`** | Load 50,000-row PayGuard dataset directly in Colab (no manual upload) |

**Local copy (optional):** `data/payguard_transactions.csv` in the course repo — same file as on S3.
