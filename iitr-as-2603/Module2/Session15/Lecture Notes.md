# Leakage & Imbalance

## Context of This Session

In the previous session, you learned how to **clean messy data** for machine learning — filling missing values, removing duplicates, encoding categories, and scaling numbers so columns sit on a fair scale. You also practised **splitting** data into training and test portions and saw an early rule: **fit preprocessing on training data only**, then apply the same rules to the test set so evaluation stays honest.

Today you go deeper into **why models still fool us** even after good cleaning. You will study **data leakage** in full — the sneaky ways test information enters training — and **class imbalance**, when one outcome dominates and **accuracy** becomes a trap. You will meet **precision** and **recall** in plain language, explore **oversampling**, **undersampling**, and **synthetic balancing**, and finish with **cross-validation** so one lucky split does not decide your faith in a model.

**In this session, you will:**

- Define **data leakage** and apply a **guard checklist** (split first, train-only fit, lock test data, simulate real prediction time)
- Spot common leakage scenarios: preprocess-before-split, target-derived features, duplicates across splits, and test-set statistics in transforms
- Explain **class imbalance** with everyday examples and why models chase the majority class
- Compare **precision** vs **recall** using false alarms and missed catches — without formulas
- Discuss **oversampling**, **undersampling**, and **synthetic data** (e.g., SMOTE intuition) at a conceptual level
- Understand **cross-validation** as repeated train–test evaluation with averaged scores
- Connect leakage, imbalance, and evaluation into one honest story before you train more advanced models

---

## Why Good Scores Can Still Lie

After cleaning data, the natural next step is to train a model and check **accuracy** — how many predictions were correct. A score of **95%** feels like success. In real projects, that number is often **misleading**.

Think of a student who scores **92%** on a mock test because they had already seen the exact questions. On the real exam, different questions appear — and they barely pass. The high mock score did not measure true learning; it measured **cheating by preview**.

Machine learning models fall into the same trap in two quiet ways:

- They were given **information they should not have** at training time (**data leakage**).
- The dataset is **skewed** so guessing the common answer looks brilliant (**class imbalance**).

Neither problem throws an error on screen. Both can make a notebook look like a win while production fails. The rest of this session gives you guardrails so your numbers mean something.

![Training vs real prediction time: leakage gives the model information that will not exist at deployment](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-01-data-leakage-overview.png)

### Quick Activity — Honest or Misleading?

For each situation, write **H** if the score is likely **honest** or **M** if it is likely **misleading**.

1. A fraud model scores **99.8%** on a dataset where only **0.2%** of rows are fraud, and the model predicts “not fraud” every time.  
2. You split first, scale using **training-only** statistics, and get **78%** accuracy on the locked test set.  
3. You scale using the **full dataset mean**, then split, and get **94%** test accuracy.

**Answer key:** 1 → M (imbalance + useless majority guess). 2 → H (fair workflow). 3 → M (leakage from full-data scaling).

---

## Data Leakage — Definition, Scenarios, and Guards

You already met leakage briefly when you learned **split before scale**. Now we widen the lens: leakage is any path where **test or future information** influences training or preprocessing.

**Data Leakage:**

- **Official Definition:** Using information during model training or preprocessing that would **not be available** at the moment you make a real prediction in production.
- **In Simple Words:** The model peeks at answers or test-set secrets while “studying,” so exam scores look great but real-life performance collapses.
- **Real-Life Example:** Predicting whether a loan will **default** — but your features include **“loan approved = yes”**, which is decided **after** the risk check you are trying to automate.

### The Core Assumption of ML

A model should learn patterns from **past** rows and apply them to **new** rows it has never seen. Leakage breaks that wall. The model shortcuts through forbidden clues instead of learning durable patterns.

Before keeping any column, ask:

> **Would I genuinely know this value at prediction time?**

If the answer is **no** or **maybe**, drop or redesign that feature.

### Scenario 1 — Preprocessing Before Split

This is the most common leakage in beginner pipelines.

**Wrong order (leaky):**

1. Load data  
2. Fill missing values using **column mean of all rows**  
3. Scale using **min/max of all rows**  
4. **Then** split train and test  

**Why it hurts:** Test rows helped compute the mean and scale. The model indirectly “saw” the test set during cleanup — like averaging exam marks using tomorrow’s answer sheet.

**Right order (guard):**

1. Load data  
2. **Split first**  
3. Learn imputation and scaling **only on training rows**  
4. Apply the **same learned rules** to test rows with `transform` only — never `fit` again on test  

![Wrong order (leaky): preprocess on all data before split. Correct order: split first, then fit transforms on training data only](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-02-split-first-workflow.png)

This connects directly to your previous workflow: **StandardScaler** on train with `fit_transform`, on test with `transform` only.

### Scenario 2 — Target-Related or Future Features

Sometimes a column is not missing — it is **too honest**.

| Domain | Valid at prediction time? | Leaky feature example |
|---|---|---|
| Car price | Yes: year, mileage | **Final negotiated price** (that *is* what you predict) |
| Student pass/fail | Yes: attendance, assignments | **Final exam marks** when predicting pass before exams |
| E-commerce purchase | Yes: pages viewed, time on site | **Order confirmation ID** before checkout completes |
| Loan default | Yes: income, credit score | **“Approved = yes”** when predicting default **before** approval |

**Common doubt:** *“The column is numeric — is it safe?”* Safety depends on **timing**, not data type. If the value exists only **after** the event you predict, it is leakage.

### Scenario 3 — Duplicates Across Train and Test

If the **same customer**, **same transaction**, or **near-duplicate row** appears in both train and test, the model may **memorise** that row in training and “predict” it again in testing.

- **Fix mindset:** Deduplicate or group by entity **in a way that keeps one person’s rows entirely in train or entirely in test** when duplicates represent the same real-world case.
- **Why it matters:** Evaluation looks strong; deployment on truly new users does not.

### Scenario 4 — Test Statistics Inside Transforms

Any step that **learns from all rows** leaks: global mean imputation, global scaling, feature selection using the **full** label distribution, or tuning on test performance repeatedly.

**Guard rule:** Anything that **learns** (means, categories, scaling bounds, encoders) learns from **training only**.

### Data Leakage Guard Checklist

Use this checklist before you trust any score:

| Step | Guard action |
|---|---|
| 1 | **Split first** — lock away the test set immediately after load |
| 2 | **Fit preprocessing on training only** — imputers, encoders, scalers |
| 3 | **Transform test** — apply training statistics; never refit on test |
| 4 | **Isolate test mentally** — no peeking, no tuning decisions driven by test |
| 5 | **Simulate real time** — features must exist **before** the outcome you predict |
| 6 | **Check duplicates** — same entity should not straddle train and test unfairly |

When leakage is removed, accuracy often **drops**. That drop is **good news** — the score is finally honest.

### Full Code — Split First, Then Scale (No CSV Needed)

```python
# Import pandas for tables
import pandas as pd

# Import train_test_split to divide rows fairly
from sklearn.model_selection import train_test_split

# Import StandardScaler to scale numeric columns
from sklearn.preprocessing import StandardScaler

# Build a small student-style dataset in memory (20 rows)
data = pd.DataFrame(
    {
        "attendance_pct": [
            92, 78, 95, 65, 88, 72, 90, 85, 91, 76,
            82, 94, 68, 89, 74, 96, 71, 87, 93, 79,
        ],
        "assignment_avg": [
            82, 58, 90, 45, 75, 62, 88, 70, 85, 55,
            78, 92, 48, 80, 60, 91, 52, 77, 89, 63,
        ],
        "target": [
            1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
            1, 1, 0, 1, 0, 1, 0, 1, 1, 0,
        ],
    }
)

# Features = all columns except the label
X = data.drop("target", axis=1)

# Label = the column we want to predict
y = data["target"]

# Step 1: SPLIT FIRST — before any scaling or imputation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a scaler object (empty until we fit it)
scaler = StandardScaler()

# Step 2: Learn mean/std from TRAINING rows and scale training data
X_train_scaled = scaler.fit_transform(X_train)

# Step 3: Apply SAME mean/std to test — do NOT call fit on test
X_test_scaled = scaler.transform(X_test)

# Print shapes to confirm split sizes
print("Training rows:", X_train_scaled.shape[0])
print("Test rows:", X_test_scaled.shape[0])
```

**How the code works:**

- `train_test_split` holds out **20%** as test; `random_state=42` keeps the same split when you re-run.
- `fit_transform` on **train** learns mean and standard deviation, then scales train rows.
- `transform` on **test** uses training statistics only — test rows never change what the scaler learned.
- Calling `fit` or `fit_transform` on test would be leakage.

### Quick Activity — Order the Pipeline

Number these steps **1–4** in the **correct** order for a leakage-safe workflow.

- [ ] Apply `scaler.transform(X_test)`  
- [ ] `train_test_split(X, y, ...)`  
- [ ] `scaler.fit_transform(X_train)`  
- [ ] Load dataset into a DataFrame  

**Answer key:** Load → split (2) → fit_transform train (3) → transform test (1).

---

## Class Imbalance — When One Label Dominates

Leakage is about **when** information appears. Imbalance is about **how often** each label appears. Both can destroy trust in evaluation — for different reasons.

**Class Imbalance:**

- **Official Definition:** A classification dataset where one **class** (label) has far more examples than another, so the model sees one outcome much more often during training.
- **In Simple Words:** The dataset is lopsided — like a classroom where 95 students passed and only 5 failed.
- **Real-Life Example:** In **one million** bank transactions, only **fifty** might be fraud. “Normal” is the crowd; fraud is the rare guest.

### Everyday Skewed Datasets

| Situation | Majority class | Minority class (often what we care about) |
|---|---|---|
| Fraud detection | Legitimate transactions | Fraud |
| Rare disease screening | Healthy patients | Diseased |
| Manufacturing QC | Good units | Defective units |
| Marketing conversion | Did not buy | Purchased |

Imbalance is usually **not a data entry mistake**. It mirrors the real world — serious events are rare. The danger is training **without noticing** the skew.

![Class imbalance: the majority class dominates what the model sees during training](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-03-class-imbalance.png)

### How the Model Behaves on Skewed Data

If the model sees **“not fraud”** thousands of times and **“fraud”** only a few times, the easy way to minimise errors is to predict **“not fraud”** almost always.

- It looks **accurate** on paper.
- It **fails the business goal** — catching the rare but costly cases.

**Analogy:** An assistant marks every student **“pass”** in a class where 95% actually passed. The assistant is **95% accurate** but useless for finding the five students who need help.

### Quick Activity — Count the Classes

A dataset has **9,800** “safe” logins and **200** “hacked” logins.

1. What percentage is **hacked**?  
2. If a model always predicts **“safe”**, what is its accuracy?  
3. How many hacked cases does it catch?

**Answers:** 1 → 2%. 2 → 98%. 3 → **zero** hacked cases caught — accuracy hides total failure on the minority.

---

## Why Accuracy Misleading on Imbalanced Data

**Accuracy:**

- **Official Definition:** The fraction of all predictions that are correct — (correct predictions) ÷ (total predictions).
- **In Simple Words:** “Out of 100 guesses, how many were right overall?”
- **Real-Life Example:** A gatekeeper who lets everyone in without checking IDs might still report **“100% allowed correctly”** if nobody was supposed to be stopped — missing every real intruder.

### Worked Example — The Fraud Puzzle

- **10,000** transactions  
- **20** are fraud (**0.2%**)  
- Model predicts **“not fraud”** every time  

**Accuracy = 9,980 / 10,000 = 99.8%** — sounds elite.  
**Fraud caught = 0 / 20 = 0%** — the model is **useless** for the bank’s real job.

![High accuracy can hide zero recall on the rare class when the model always predicts the majority label](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-04-accuracy-misleading.png)

### What Accuracy Hides

Accuracy does not tell you:

- How many **rare but critical** cases you found  
- Whether errors hurt more on one class than another  
- Whether the model is just **voting with the crowd**

**Integrated insight:** In imbalance problems, **not all mistakes cost the same**. Missing fraud or disease is often far worse than a false alarm — accuracy treats every mistake equally.

### Quick Activity — Stakeholder Question

A hospital screening tool has **99% accuracy** but misses most real cases of a rare illness.

Write **two sentences** you would tell a non-technical manager: one about **accuracy**, one about **what patients are actually at risk from**.

**Sample answer:** Accuracy counts all correct answers together, so a rare disease can be almost invisible. We need measures that ask how many sick patients we **catch**, not only how often the tool says “healthy.”

---

## Precision and Recall — Plain-Language Intuition

When accuracy fails, we need lenses that focus on the **important class** and on **two types of mistakes**.

**False positive:** Model shouts **“yes, important!”** but reality says **no** — a **false alarm**.  
**False negative:** Model says **“no, all fine”** but reality says **yes** — a **missed catch**.

We will not use formulas today — only the questions each metric answers.

### Precision — Trust When We Flag “Yes”

**Precision:**

- **Official Definition:** Among all cases the model labelled **positive**, the proportion that were truly positive.
- **In Simple Words:** When we ring the alarm, how often is the alarm **fair**?
- **Real-Life Example:** A spam filter marks 10 emails as spam; only 6 are real spam — 4 important mails were **wrongly hidden** (low precision → too many false alarms).

**Low precision hurts when:** False alarms waste money, stress patients, or block good customers.

### Recall — Did We Catch the Real Cases?

**Recall:**

- **Official Definition:** Among all **truly positive** cases in the data, the proportion the model successfully flagged.
- **In Simple Words:** Of everyone who really needed help, how many did we **find**?
- **Real-Life Example:** 20 fraud cases exist; the model catches 5 — 15 slip through (**low recall** → dangerous misses).

**Low recall hurts when:** Missing fraud, disease, or defects is unacceptable.

![Precision (quality of positive predictions) vs recall (coverage of actual positives)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-05-precision-recall.png)

### Precision vs Recall — The Trade-Off

- **Stricter model** → fewer false alarms (**higher precision**) but more misses (**lower recall**).  
- **Looser model** → catches more real cases (**higher recall**) but more false alarms (**lower precision**).

| If this hurts more… | You usually care more about… |
|---|---|
| Crying wolf (false alarms) | **Precision** |
| Missing the real problem | **Recall** |

**Fraud at a bank:** Missing fraud is costly → teams often push **recall** up (catch more fraud), accepting some extra checks.  
**Spam in inbox:** Wrongly hiding real email is painful → teams often push **precision** up.

### Quick Activity — Match the Metric

| Story | Precision or recall? |
|---|---|
| Out of 100 flagged defects, 90 were real defects | ? |
| Out of 50 real defects on the line, we found 40 | ? |
| Doctor wants fewer healthy people told they are sick | ? |
| Security wants fewer real threats ignored | ? |

**Answers:** Row 1 → precision focus. Row 2 → recall focus. Row 3 → precision. Row 4 → recall.

---

## Handling Imbalance — Oversampling, Undersampling, and Trade-offs

Once you **measure** imbalance honestly, you can **adjust training data** so the model pays attention to the minority — without pretending the real world is balanced.

### Oversampling — Give the Minority More Voice

**Oversampling:**

- **Official Definition:** Increasing the number of training examples from the **minority class**, often by **duplicating** existing minority rows.
- **In Simple Words:** Let the rare class “speak” more often in class so the model cannot ignore it.
- **Real-Life Example:** You have 10 fraud records among 990 normal ones — you copy those 10 fraud rows many times so training sees fraud more evenly.

**Trade-off:** Simple duplication can cause **overfitting** — the model memorises those few rows instead of learning general fraud patterns.

### Undersampling — Quieten the Majority

**Undersampling:**

- **Official Definition:** **Removing** some majority-class examples so class counts are closer.
- **In Simple Words:** Turn down the volume on the common label so the rare label gets heard.
- **Real-Life Example:** Randomly keep 100 normal transactions instead of 990, to pair more fairly with 10 fraud cases.

**Trade-off:** You **throw away** real data the model might have learned from — risky when data is already small.

![Oversampling (more minority examples) vs undersampling (fewer majority examples)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-06-over-under-sampling.png)

| Technique | Idea | Main risk |
|---|---|---|
| **Oversampling** | Add minority examples (copies) | Memorising duplicates |
| **Undersampling** | Remove majority examples | Losing useful patterns |
| **Combined** | Mix both | Must still evaluate on **real** imbalance in test |

**Important:** Balance **training** if needed — but report test metrics on the **true** distribution unless your product goal says otherwise.

### Quick Activity — Pick a Strategy (Conceptual)

| Dataset size | Imbalance | Which first step might you *discuss* with your team? |
|---|---|---|
| Huge (millions of rows) | 99% vs 1% | Undersample majority **or** use synthetic minority |
| Tiny (500 rows total) | 95% vs 5% | Oversample minority carefully — undersampling may hurt more |
| Medium | 80% vs 20% | Try class weights or mild oversampling before extreme cuts |

There is no single button — the table builds **judgement**, not memorisation.

---

## Synthetic Data and SMOTE — Intuition Only

Copying the same minority row ten times adds **quantity**, not **variety**. **Synthetic data** tries to create **new, plausible** minority points.

**Synthetic data (for balancing):**

- **Official Definition:** Artificial examples generated to resemble the **minority class**, usually based on patterns among real minority points — not exact duplicates.
- **In Simple Words:** Instead of photocopying one fraud case, you sketch **new cases that look like fraud** but are not identical to any one row.
- **Real-Life Example:** You only have two shades of green paint — you **mix** them to show many similar shades so someone learns “green family,” not just two swatches.

### SMOTE — High-Level Idea

**SMOTE** (Synthetic Minority Over-sampling Technique):

- **Official Definition:** An algorithm that creates synthetic minority samples by interpolating between **neighbouring** minority points in feature space.
- **In Simple Words:** Draw a new point **between** two similar fraud rows — a blend, not a clone.
- **Real-Life Example:** Two fraud transactions look alike (amount, time, merchant type) — SMOTE imagines a third transaction **between** them that still feels like fraud.

![Synthetic minority points as plausible blends between neighbouring real minority points](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-07-synthetic-data.png)

**Benefits vs plain duplication:**

- More **variety** → less memorisation of a handful of rows.  
- Model may **generalise** better on rare classes.

**Risks:**

- Bad blends between **unrelated** neighbours create nonsense rows.  
- Quality depends on **clean features** and enough real minority examples.

**Scope today:** Understand the **idea** and trade-offs. Deep implementation comes with practice libraries later — after you master honest splits and metrics.

### Quick Activity — Duplicate vs Synthetic

| Approach | What the model sees | Risk |
|---|---|---|
| Copy the same fraud row 50 times | Same story repeated | Memorise one case |
| SMOTE-style blend between two fraud rows | A **new** similar story | Nonsense blend if neighbours are wrong |

In one sentence each, say which risk worries you more for a **tiny** dataset (only 8 fraud rows).

**Sample answer:** Duplication → memorisation. Synthetic → unrealistic blends when neighbours are not truly similar.

---

## Cross-Validation — Why One Split Is Not Enough

Even with **no leakage** and **honest metrics**, a **single** train–test split can flatter or punish you by luck.

**Cross-validation:**

- **Official Definition:** A evaluation strategy that repeats training and testing on **multiple different splits** (folds) and **averages** performance across them.
- **In Simple Words:** Play several short mock matches instead of judging a player from **one** odd pitch.
- **Real-Life Example:** Model A scores **95%** on one random split and **62%** on another; Model B scores **78%, 77%, 79%, 76%, 78%** across five splits — you trust B’s **average** more than A’s one lucky **95%**.

![k-fold cross-validation: each chunk serves as the test set once; average scores for a stable estimate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-08-k-fold-cv.png)

### k-Fold Walkthrough (Verbal)

Suppose you split data into **5 equal folds**:

1. **Round 1:** Train on folds 2–5, test on fold 1 → score₁  
2. **Round 2:** Train on 1,3–5, test on fold 2 → score₂  
3. Continue until **each fold was test exactly once**  
4. **Average** score₁…score₅ and check **spread** (stable vs wild)

**Low spread** → model behaves consistently. **High spread** → performance depends heavily on which rows were held out — be cautious.

### When to Use It (Conceptual)

- **Small or medium** datasets where one split is noisy.  
- **Comparing** two models fairly.  
- **Not a substitute** for a final held-out test set you never touched during experiments — in industry you still often keep one **locked** test set for the very end.

### Full Code — 5-Fold Cross-Validation on Imbalanced Synthetic Data

```python
# Import function to create a fake imbalanced dataset
from sklearn.datasets import make_classification

# Import cross-validation helper
from sklearn.model_selection import cross_val_score

# Import a simple classification model
from sklearn.linear_model import LogisticRegression

# Build 200 rows, 4 features, ~92% class 0 and ~8% class 1 (imbalanced)
X, y = make_classification(
    n_samples=200,
    n_features=4,
    n_informative=2,
    n_redundant=0,
    weights=[0.92, 0.08],
    random_state=42,
)

# Create logistic regression model (needs enough iterations to converge)
model = LogisticRegression(max_iter=500)

# Run 5-fold cross-validation; scoring defaults to accuracy here
scores = cross_val_score(model, X, y, cv=5)

# Print score from each fold
print("Scores per fold:", scores)

# Print average score across folds
print("Average score:", scores.mean())

# Print how much scores swing (optional stability check)
print("Spread (max - min):", scores.max() - scores.min())
```

**How the code works:**

- `make_classification` builds features `X` and labels `y` with a **rare** positive class — like fraud in miniature.
- `cross_val_score` trains and tests **5 times**, each time holding out a different fifth of the data.
- `scores` is an array of **five** accuracies — compare them, not only the max.
- `scores.mean()` is your **stable-ish** headline number; large gaps between folds mean “be careful.”

**Note:** Fold values can shift slightly with library versions; the **pattern** (similar folds vs wild swings) matters more than memorising one number.

### Quick Activity — Read the Folds

Suppose `scores = [0.76, 0.74, 0.78, 0.75, 0.77]`.

1. What is the approximate **average**?  
2. Is performance **stable** or **wild**?  
3. Would you trust this more than a **single** test score of **0.95** from one lucky split?

**Answers:** 1 → ~0.76. 2 → stable (narrow band). 3 → yes — the single 0.95 might be luck; the averaged folds tell a steadier story.

---

## Connecting Leakage, Imbalance, and Evaluation

These three ideas form one triangle. Weakness in any corner can make you ship a model that **fails real users**.

![Honest evaluation combines guarding leakage, handling imbalance and metrics, and cross-validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-09-evaluation-pillars.png)

| Problem | What goes wrong | What honest practice looks like |
|---|---|---|
| **Leakage** | Scores **too high**; model fails live | Split first; fit only on train; real-time features only |
| **Imbalance** | Accuracy **misleading**; minority ignored | Check class counts; use precision/recall stories; balance training thoughtfully |
| **Single split** | One lucky/unlucky test misleads | Cross-validate or repeat splits; average and check spread |

### Chain of Failure (What to Avoid)

1. **Leakage present** → inflated test score → false confidence → production collapse.  
2. **Imbalance ignored** → “99% accurate” model that never catches fraud or disease.  
3. **One split only** → celebrate or panic based on noise, not signal.

### Chain of Trust (What to Build)

1. **Guard leakage** so the test set stays unseen during learning and preprocessing.  
2. **Report the right question** — precision/recall language when the rare class matters.  
3. **Stabilise evaluation** with cross-validation or careful repeated splits before you celebrate.

In upcoming work you will train models that predict **numbers** (regression) and revisit **classification** with new algorithms. The habits from today — **fair splits**, **honest metrics**, and **stable evaluation** — stay non-negotiable no matter how advanced the model name sounds.

### Quick Activity — Audit a Notebook Story

Read this short pipeline claim:

> “We filled missing values using the full dataset mean, trained on 80%, and got 96% accuracy on the remaining 20%. Ready to deploy.”

List **three questions** you would ask before trusting it (one per theme: leakage, imbalance, evaluation).

**Sample questions:**

- Did you **split before** imputing and scaling, and fit imputation on **train only**?  
- What are the **class counts** — could 96% be majority-class guessing?  
- Was there **only one split** — would cross-validation show stable scores?

---

## Key Takeaways

- **Data leakage** means training or preprocessing used information that would not exist at real prediction time — it creates **fake success** until deployment exposes the truth.
- **Split first, fit on train only, transform test** is the guard workflow that extends your previous data-prep habits into every scaler, imputer, and encoder.
- **Class imbalance** makes models chase the majority; **accuracy alone** can hide total failure on the rare cases that matter most.
- **Precision** focuses on false alarms; **recall** focuses on missed catches — choose which pain matters more in your problem.
- **Oversampling**, **undersampling**, and **synthetic** methods (e.g., SMOTE intuition) adjust training balance with different risks; **cross-validation** averages performance across folds so one lucky split does not fool you.
- Upcoming modelling topics build on this foundation: honest evaluation is what separates a notebook demo from a system people can rely on.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Data leakage** | Test/future/label information enters training or preprocessing | Inflates scores; fails in production |
| **Split first** | `train_test_split` before impute/scale/encode | Core guard against preprocessing leakage |
| `fit_transform` | Learn parameters from data and apply transform | Use on **training** data only |
| `transform` | Apply already-learned parameters | Use on **test** — never refit |
| **Target-derived feature** | Column built using the answer you predict | Looks predictive but is cheating |
| **Duplicate across splits** | Same entity in train and test | Inflates evaluation; weak generalisation |
| **Class imbalance** | One label far more common than another | Models ignore minority; accuracy misleads |
| **Accuracy** | Overall fraction correct | Unreliable when classes are skewed |
| **False positive** | Predicted positive, actually negative | Drives precision pain (false alarms) |
| **False negative** | Predicted negative, actually positive | Drives recall pain (missed catches) |
| **Precision** | When we say “yes,” how often right? | Fewer false alarms |
| **Recall** | Of all real “yes,” how many found? | Fewer missed critical cases |
| **Oversampling** | Add minority examples (often copies) | Balances training; overfitting risk |
| **Undersampling** | Remove majority examples | Balances training; information loss risk |
| **Synthetic data** | New artificial minority-like points | More variety than duplication |
| **SMOTE** | Synthetic minority oversampling between neighbours | Common balancing idea — intuition level today |
| **Cross-validation** | Multiple train–test rounds, averaged scores | Stable performance estimate |
| `cross_val_score` | Runs k-fold evaluation in sklearn | Quick stability check in code |
| `make_classification` | Generates synthetic imbalanced data for practice | Safe playground without real PII |
| `train_test_split` | Holds out test rows | Same tool as in data prep — order matters |
| `StandardScaler` | Scales features using mean and std | Must fit on train only after split |
| `LogisticRegression` | Simple classifier for demos | Used here only to illustrate CV, not as the focus algorithm |
