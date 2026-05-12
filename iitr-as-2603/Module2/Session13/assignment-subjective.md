# Assignment: Subjective — Session 13: The ML Workflow & Habits

**Total Questions: 1 | Format: Practical Coding Task | Difficulty: Medium**

---

## Question 1 — End-to-End ML Workflow: Subscription Churn Baseline

**Scenario:**

StreamNow, a music streaming platform, is worried about users cancelling their subscriptions. The product team wants to know: *"Based on a user's listening behaviour this month, will they cancel their subscription next month?"*

You have been given a synthetic dataset representing StreamNow's user behaviour. Your task is to build the **complete ML Workflow** in a Google Colab notebook — from framing the problem all the way to establishing and interpreting a baseline.

---

### Dataset Description

The dataset `streamnow_users.csv` has the following columns:

| Column | Description |
|---|---|
| `user_id` | Unique user identifier |
| `avg_daily_listening_mins` | Average minutes of music listened to per day this month |
| `unique_artists_played` | Number of unique artists the user played this month |
| `skips_per_session` | Average number of skips per listening session |
| `days_app_opened` | Number of days the user opened the app this month |
| `playlist_saves` | Number of new playlists saved this month |
| `subscription_months` | How many months the user has been subscribed |
| `will_cancel` | Whether the user cancelled next month (Yes / No) — **this is the label** |

> **Note:** A code cell to generate this synthetic dataset is provided below — run it first before doing anything else. You do not need to download any external file.

---

### Your Tasks (Complete in a Google Colab Notebook)

**Cell 1 — Generate the Dataset**

Copy and run the following code cell exactly as provided to create the `streamnow_users.csv` file in your Colab environment:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 1200

data = {
    "user_id": [f"USR{1000+i}" for i in range(n)],
    "avg_daily_listening_mins": np.round(np.random.normal(45, 20, n).clip(5, 120), 1),
    "unique_artists_played": np.random.randint(3, 80, n),
    "skips_per_session": np.round(np.random.uniform(0.5, 8.0, n), 1),
    "days_app_opened": np.random.randint(1, 31, n),
    "playlist_saves": np.random.randint(0, 15, n),
    "subscription_months": np.random.randint(1, 48, n),
}

# generate label: users with low engagement are more likely to cancel
cancel_prob = (
    (data["avg_daily_listening_mins"] < 20).astype(int) * 0.4 +
    (data["days_app_opened"] < 10).astype(int) * 0.3 +
    np.random.uniform(0, 0.3, n)
)
cancel_prob = cancel_prob / cancel_prob.max()
data["will_cancel"] = np.where(cancel_prob > 0.55, "Yes", "No")

df = pd.DataFrame(data)
df.to_csv("streamnow_users.csv", index=False)

print("Dataset created! Shape:", df.shape)
print(df.head())
```

---

**Cell 2 — Problem Framing (Markdown Cell)**

In a **Markdown cell**, write out the problem frame for this scenario using the template below. Fill in the blanks with the correct values for this dataset:

> "Given **[list the feature columns]**, I want to predict **[label column]**, and I will measure success using **[metric — choose one: Accuracy, F1-score, MAE]**."
>
> **ML Problem Type:** [Classification / Regression] — because [one-sentence reason].

Also answer in the same Markdown cell: *Why is F1-score likely more appropriate than accuracy alone for this problem?*

---

**Cell 3 — Load and Inspect**

Write code to:
1. Load `streamnow_users.csv` into a DataFrame
2. Print the shape (rows, columns)
3. Display the first 5 rows
4. Print the data types of all columns
5. Check for and print any missing values

---

**Cell 4 — Separate Features and Label**

Write code to:
1. Separate the feature matrix `X` and label series `y` correctly
   - Remember to exclude `user_id` from features (it is an identifier, not a predictive signal)
2. Print the shape of `X` and `y`
3. Print the label distribution using `value_counts()` and the percentage breakdown using `value_counts(normalize=True)`

---

**Cell 5 — Train / Validation / Test Split**

Write code to:
1. Perform a **60 / 20 / 20** train/validation/test split using `train_test_split`
   - Use `random_state=42`
2. Print the number of rows in each split (training, validation, test)

---

**Cell 6 — Build and Evaluate the Baseline**

Write code to:
1. Build a `DummyClassifier(strategy="most_frequent")` baseline
2. Train it on the training set
3. Make predictions on the **test set**
4. Print the baseline accuracy using `accuracy_score`
5. Print the full `classification_report`

---

**Cell 7 — Interpret Results (Markdown Cell)**

In a **Markdown cell**, write 3–4 sentences answering the following:
- What does the baseline accuracy tell you about this dataset?
- What does the "Yes" (will cancel) class recall in the classification report reveal?
- What must a real ML model achieve (in terms of accuracy AND the "Yes" recall) to be considered genuinely useful for StreamNow?

---

### Submission Instructions

- Open [colab.research.google.com](https://colab.research.google.com) and create a new notebook
- Rename it to `Session13_StreamNow_ML_Workflow.ipynb`
- Complete all 7 cells in order — each cell as a separate Colab cell
- Once done, click **Share** (top-right) → **Change to Anyone with the link** → set permission to **Viewer**
- Copy the shareable link and paste it as your submission
- Make sure the sharing setting is set to `Anyone with the link can view` (submissions with restricted access will not be evaluated)

---

### Answer Explanation

#### Ideal Solution Walkthrough

The solution follows the 6-step ML Workflow taught in the session. Below is the complete, cell-by-cell ideal solution with explanations.

---

**Cell 1 — Generate Dataset** *(provided in the question — run as-is)*

The code uses `numpy.random.seed(42)` for reproducibility, generates 1,200 synthetic user records, and engineers the `will_cancel` label so that low-engagement users (low listening time + few days active) have a higher probability of cancelling. This creates a realistic, mildly imbalanced dataset.

---

**Cell 2 — Problem Framing** *(Markdown — ideal answer)*

```
"Given avg_daily_listening_mins, unique_artists_played, skips_per_session,
days_app_opened, playlist_saves, and subscription_months,
I want to predict will_cancel (Yes / No),
and I will measure success using F1-score (especially for the 'Yes' class)."

ML Problem Type: Classification — because the output is a discrete category (Yes or No),
not a continuous number.
```

**Why F1-score over accuracy?**
The dataset is likely imbalanced (more "No" than "Yes" since most users don't cancel). A model that always predicts "No" would achieve high accuracy without catching a single actual churner. F1-score combines precision and recall, forcing the model to prove it can actually detect cancellations — which is StreamNow's real business need.

---

**Cell 3 — Load and Inspect** *(ideal code)*

```python
import pandas as pd

df = pd.read_csv("streamnow_users.csv")

print("Shape:", df.shape)           # expected: (1200, 8)
print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())            # expected: all zeros — synthetic data has no nulls
```

**Key points:**
- Always inspect shape first to confirm 1,200 rows and 8 columns loaded correctly.
- `dtypes` reveals that `user_id` and `will_cancel` are `object` (string), while all numeric features are `float64` or `int64` — no unexpected type issues.
- `isnull().sum()` should return all zeros for this synthetic dataset.

---

**Cell 4 — Separate Features and Label** *(ideal code)*

```python
# exclude user_id (identifier) and will_cancel (label) from features
X = df.drop(columns=["user_id", "will_cancel"])
y = df["will_cancel"]

print("Features shape:", X.shape)   # expected: (1200, 6)
print("Label shape:", y.shape)      # expected: (1200,)

print("\nLabel distribution (count):")
print(y.value_counts())

print("\nLabel distribution (%):")
print(y.value_counts(normalize=True).mul(100).round(1))
# expected approximate output:
# No     ~70–75%
# Yes    ~25–30%
# slight imbalance — accuracy alone will be misleading
```

**Key points:**
- `user_id` must be dropped along with `will_cancel`. It is a unique identifier — if kept, the model could memorise specific users rather than learn patterns.
- `X.shape` should be `(1200, 6)` — confirming 6 feature columns remain.
- The label distribution reveals the class imbalance and tells us the baseline accuracy floor before training anything.

---

**Cell 5 — Train / Validation / Test Split** *(ideal code)*

```python
from sklearn.model_selection import train_test_split

# Step 1: carve out 20% for the final test set
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Step 2: split remaining 80% into 75% train (=60% total) and 25% val (=20% total)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

print(f"Training rows:   {X_train.shape[0]}")   # expected: ~720 (60%)
print(f"Validation rows: {X_val.shape[0]}")     # expected: ~240 (20%)
print(f"Test rows:       {X_test.shape[0]}")    # expected: ~240 (20%)
```

**Key points:**
- The split is done in two steps because `train_test_split` only does binary splits.
- `random_state=42` ensures the same split every time — essential for reproducibility.
- Always print the row counts after splitting to verify the math is correct.

---

**Cell 6 — Build and Evaluate the Baseline** *(ideal code)*

```python
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report

# build the simplest possible model — always predicts the most common class
baseline = DummyClassifier(strategy="most_frequent", random_state=42)

# train on training data only — it just records the most frequent label
baseline.fit(X_train, y_train)

# predict on the test set — every prediction will be "No" (the majority class)
baseline_preds = baseline.predict(X_test)

# measure accuracy
baseline_acc = accuracy_score(y_test, baseline_preds)
print(f"Baseline Accuracy: {baseline_acc:.2%}")
# expected output: ~70–75% (matches the "No" class proportion)

# full report showing per-class precision, recall, F1
print("\nBaseline Classification Report:")
print(classification_report(y_test, baseline_preds))
# expected: "Yes" class will show recall = 0.00 and F1 = 0.00
# the baseline catches zero actual cancellations
```

**Key points:**
- The baseline never predicts "Yes" — its recall for the cancellation class is exactly 0%.
- The high accuracy (~70–75%) is misleading — it is entirely due to the class imbalance.
- The classification report is the critical output: it exposes that the baseline is useless for catching churners.

---

**Cell 7 — Interpret Results** *(Markdown — ideal answer)*

```
The baseline accuracy of ~70–75% simply reflects the proportion of "No" (non-cancellation)
cases in the dataset. This means a model that ignores all features and always predicts
"No" already achieves this score — it has learned nothing.

The recall of 0% for the "Yes" class in the classification report reveals that the baseline
misses every single actual cancellation. For StreamNow, this is a complete failure —
the entire goal is to identify users who are about to cancel so the team can intervene.

A genuinely useful real model must:
(1) Beat the ~70–75% accuracy baseline, AND
(2) Achieve meaningful recall for the "Yes" class (ideally above 60%)
so that StreamNow can actually act on the predictions and reduce churn.
```

---

#### Alternative Approaches

- **Alternative baseline strategy:** Instead of `strategy="most_frequent"`, you could use `strategy="stratified"` — this randomly predicts classes proportional to their training distribution. It is slightly more informative but typically performs worse than `most_frequent` on imbalanced data.
- **Alternative split ratio:** A 70/15/15 or 80/10/10 split would also be valid. The 60/20/20 used here gives a larger validation set, which is appropriate for a 1,200-row dataset.
- **Alternative metric:** Instead of `accuracy_score`, you could use `f1_score(y_test, baseline_preds, pos_label="Yes")` to directly compute the F1 for the cancellation class — this would immediately return 0.0 and make the baseline's failure even more explicit.
- **Checking imbalance before splitting:** An alternative good practice is to use `stratify=y` inside `train_test_split` — this ensures the class distribution in each split mirrors the full dataset, which is especially important when the minority class is small.
