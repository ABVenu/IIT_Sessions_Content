# Assignment: Objective — Session 13: The ML Workflow & Habits

**Total Questions: 10 | Format: 6 MCQs (Single Correct) + 4 MSQs (Multiple Correct)**
**Order: Easy → Moderate → Hard**

---

## MCQ 1 — Easy (Single Correct)

Zara just joined a data science bootcamp and her instructor asked her to open Google Colab. She notices that when she runs a code cell, the output appears almost instantly — even though her laptop is an old, basic budget model. What is the most accurate reason for this?

**A)** Her laptop has a hidden turbo-boost feature that activates when running Python code
**B)** Google Colab executes code on Google's cloud servers, not on her local laptop
**C)** Google Colab compresses the code before running it, making it faster on any machine
**D)** Python automatically detects the hardware and optimises itself on budget laptops

**Correct Answer: B**

**Answer Explanation:**
Google Colab runs code on Google's **cloud servers** (a remote Runtime), not on the user's local machine. This is why even a slow or budget laptop can run ML code smoothly — the heavy computation happens on Google's infrastructure, and only the inputs and outputs travel between the browser and the cloud. Options A, C, and D describe features that do not exist in Colab or Python.

---

## MCQ 2 — Easy (Single Correct)

A school teacher wants to build an ML model to predict whether a student will pass or fail their final exam. She has a dataset with the following columns:

| Column | Description |
|---|---|
| `attendance` | Percentage of classes attended |
| `study_hours` | Average study hours per day |
| `mock_score` | Score in the most recent mock exam |
| `assignment_done` | Whether all assignments were completed (Yes/No) |
| `result` | Whether the student passed or failed (Pass/Fail) |

Which column should she assign as the **label (y)** when writing her ML code?

**A)** `attendance`
**B)** `study_hours`
**C)** `mock_score`
**D)** `result`

**Correct Answer: D**

**Answer Explanation:**
The **label (y)** is the column the model is trying to predict — the output or target variable. Since the teacher's goal is to predict whether a student will pass or fail, the `result` column (Pass/Fail) is the label. All other columns (`attendance`, `study_hours`, `mock_score`, `assignment_done`) are **features (X)** — the input clues the model uses to learn patterns and make predictions.

---

## MCQ 3 — Easy (Single Correct)

Neha is building a smart home automation script in Python. Her script turns on the AC if the room temperature exceeds 26°C, switches on the lights if motion is detected after 7 PM, and sends a WhatsApp alert if the front door is open after midnight. Which AI paradigm does Neha's script best represent?

**A)** Supervised Machine Learning
**B)** Unsupervised Learning
**C)** Rule-based AI
**D)** Reinforcement Learning

**Correct Answer: C**

**Answer Explanation:**
Neha's script is a textbook example of **Rule-based AI** — it consists entirely of explicit `if-else` conditions written by a human programmer. Every action is triggered by a pre-defined rule. The script does not learn from data, does not adjust its behaviour based on experience, and cannot handle situations that were not anticipated in the rules. Supervised ML, Unsupervised Learning, and Reinforcement Learning all involve some form of learning from data — which this script does not do.

---

## MCQ 4 — Easy (Single Correct)

Rohit is building his first ML pipeline on a student performance dataset. He runs the following code and sees the output `Baseline Accuracy: 68.00%`. Before this, he had checked the label distribution and found that 68% of students passed and 32% failed.

```python
baseline = DummyClassifier(strategy="most_frequent", random_state=42)
baseline.fit(X_train, y_train)
print(f"Baseline Accuracy: {accuracy_score(y_test, baseline.predict(X_test)):.2%}")
```

What is the best explanation for this result?

**A)** The model has learned patterns from the 68% of training data it found most relevant
**B)** The model correctly identifies 68% of the difficult edge cases in the test set
**C)** The model always predicts "Pass" (the most frequent class) and achieves 68% accuracy simply by reflecting the class distribution — without learning anything
**D)** The model was evaluated on the 68% of data that was used for training

**Correct Answer: C**

**Answer Explanation:**
`DummyClassifier(strategy="most_frequent")` does **not learn anything**. It simply records the most common class from the training data ("Pass" at 68%) and predicts it for every single test sample. Since 68% of the actual test labels are "Pass," this trivial strategy achieves 68% accuracy automatically. This is the **performance floor** — any real ML model Rohit builds must exceed this to prove it is genuinely learning.

---

## MCQ 5 — Moderate (Single Correct)

A healthcare startup builds a disease screening model on a dataset where 96% of records are "Healthy" and 4% are "Disease Detected." Their `DummyClassifier(strategy="most_frequent")` baseline achieves 96% accuracy. A junior data scientist trains a new model that also achieves 96% accuracy and says "We matched the baseline — let's tune it a bit more and deploy." What should the senior data scientist advise?

**A)** Approve the model — 96% accuracy is excellent and sufficient for any healthcare application
**B)** Reject the model — healthcare models are required to achieve at least 99% accuracy by regulation
**C)** Examine the classification report — specifically the recall and F1-score for the "Disease" class, because accuracy alone is misleading with imbalanced datasets and the model may not be detecting any actual disease cases at all
**D)** Switch to a regression model — classification is inappropriate for medical screening datasets

**Correct Answer: C**

**Answer Explanation:**
With 96% "Healthy" cases, a model can achieve 96% accuracy simply by predicting "Healthy" for every patient — which is exactly what the baseline does. For a medical screening tool, **recall on the "Disease" class** is the critical metric: how many actual sick patients did the model catch? A model with 96% accuracy but 0% recall for "Disease" is not just useless — it is dangerous, as it misses every sick patient. The `classification_report` will expose this immediately. Options A, B, and D reflect incorrect reasoning and context.

---

## MCQ 6 — Moderate (Single Correct)

Priya has a dataset of 5,000 rows. She wants to create a 60/20/20 train/validation/test split and runs the following code:

```python
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)
```

How many rows will the **validation set (`X_val`)** contain?

**A)** 500
**B)** 750
**C)** 1,000
**D)** 1,250

**Correct Answer: C**

**Answer Explanation:**
**Step 1:** `test_size=0.20` splits 20% of 5,000 = **1,000 rows** into `X_test`. The remaining `X_temp` has 5,000 − 1,000 = **4,000 rows**.
**Step 2:** `test_size=0.25` splits 25% of 4,000 = **1,000 rows** into `X_val` (validation).
The remaining 3,000 rows become `X_train`.
**Final distribution:** 3,000 / 5,000 = 60% train | 1,000 / 5,000 = 20% validation | 1,000 / 5,000 = 20% test. ✓

---

## MSQ 7 — Moderate (Multiple Correct)

Aditya has just loaded his e-commerce customer dataset. He has printed the first 5 rows and confirmed the data looks right. He is now about to separate features from the label and proceed to training. Which of the following are **correct ML habits** to follow at this stage? (Select **all** that apply)

**A)** Use `y.value_counts()` to check the label distribution before building any model
**B)** Set `random_state=42` (or any fixed integer) in `train_test_split` so the split is identical every time and reproducible across teammates
**C)** Train the model on the full dataset first to get maximum accuracy, then split off a test set afterward just for the final report
**D)** Print `X.shape` and `y.shape` after separating features and label to verify the correct number of rows and columns
**E)** Preview a few test set samples before training to understand what kinds of real-world inputs the model will face

**Correct Answers: A, B, D**

**Answer Explanation:**
- **A — Correct:** Checking label distribution first reveals class imbalance, which directly determines which evaluation metric (accuracy vs F1 vs recall) is appropriate.
- **B — Correct:** A fixed `random_state` makes the split reproducible — essential so all teammates and future runs use the same data division.
- **C — Incorrect:** Training on the full dataset means the model has seen the test data during training. This corrupts evaluation — the reported accuracy will be artificially inflated and useless for measuring real-world performance.
- **D — Correct:** Shape checks after separating X and y are a quick sanity check to ensure no rows were accidentally dropped and the feature count is correct.
- **E — Incorrect:** The test set must remain completely untouched until the very final evaluation. Previewing test data biases every modelling decision made afterward.

---

## MSQ 8 — Moderate (Multiple Correct)

Which of the following statements about **Baseline Models** in machine learning are correct? (Select **all** that apply)

**A)** A baseline sets the performance floor — any real ML model that cannot beat the baseline is essentially not learning anything useful from the features
**B)** If a baseline already achieves 99% accuracy, it is a strong signal that the problem may not need complex ML — a simple business rule might be sufficient
**C)** A baseline model uses ensemble methods and advanced feature engineering to produce a reliable benchmark
**D)** `DummyClassifier(strategy="most_frequent")` from scikit-learn is a valid baseline for classification — it always predicts the most common class seen during `.fit()`
**E)** A baseline model must be fitted on the test set so it reflects the exact distribution the model will face in production

**Correct Answers: A, B, D**

**Answer Explanation:**
- **A — Correct:** The baseline is the floor — beating it is the minimum bar for a model to prove it is learning genuine patterns.
- **B — Correct:** A 99% baseline signals extreme class imbalance — 99% of cases belong to one class, so a trivial rule already covers almost everything. ML adds no meaningful value in such a scenario.
- **C — Incorrect:** A baseline must be the **simplest** possible model — deliberately no ensembles, no feature engineering. Its purpose is to set the floor, not to be a good model.
- **D — Correct:** `DummyClassifier(strategy="most_frequent")` is scikit-learn's built-in baseline for classification — it records the most common label during training and always predicts it.
- **E — Incorrect:** Like any model, the baseline must be fitted only on the **training set**. Fitting on the test set leaks test information and invalidates the evaluation.

---

## MSQ 9 — Hard (Multiple Correct)

A logistics company asks a data scientist: *"How long will it take for a package to be delivered after the order is placed?"*

The available dataset has these columns:

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `distance_km` | Distance from warehouse to delivery address (km) |
| `package_weight_kg` | Weight of the package |
| `carrier_type` | Type of courier (Express / Standard / Economy) |
| `city_tier` | Tier of the destination city (1 / 2 / 3) |
| `delivery_days` | Number of days taken from order to delivery |
| `delivery_date` | Actual calendar date the package was delivered |

Which of the following constitute **correct problem framing decisions** for this scenario? (Select **all** that apply)

**A)** The label (y) should be `delivery_days` — it is the numeric quantity the model is being asked to predict
**B)** `order_id` should be excluded from the features because it is a unique row identifier with no predictive value
**C)** `delivery_date` should be included as a feature since it captures useful timing information about deliveries
**D)** This is a **Regression** problem because the output (`delivery_days`) is a continuous numerical value
**E)** `distance_km`, `package_weight_kg`, `carrier_type`, and `city_tier` are the correct features (X) for this problem

**Correct Answers: A, B, D, E**

**Answer Explanation:**
- **A — Correct:** The business question asks *how many days* delivery takes — a number. `delivery_days` is the target/label.
- **B — Correct:** `order_id` is a unique row identifier — it carries zero signal and would only introduce noise or allow the model to memorise specific orders.
- **C — Incorrect:** `delivery_date` is the **actual date of delivery** — which is only known *after* the delivery happens. At prediction time (the moment the order is placed), this date is unknown. Including it is **circular logic** and would make the model completely useless in production since you cannot feed it a value you do not yet have.
- **D — Correct:** The output is a number (`delivery_days`), not a category — this is a classic **Regression** problem.
- **E — Correct:** These four columns are all known at the time an order is placed, have logical predictive relationships with delivery time, and contain no future information.

---

## MSQ 10 — Hard (Multiple Correct)

Samira is building a credit card fraud detection model. Her dataset has 98.5% "Not Fraud" transactions and only 1.5% "Fraud" transactions. She builds a `DummyClassifier(strategy="most_frequent")` baseline, evaluates it on the test set, and prints the `classification_report`. Which of the following will be true about the baseline's output? (Select **all** that apply)

**A)** The baseline's overall accuracy will be approximately 98.5% — because it always predicts "Not Fraud"
**B)** The recall for the "Fraud" class will be 0% — the baseline never correctly identifies a single actual fraud transaction
**C)** The precision for the "Fraud" class will be 100% — because on the rare occasions the baseline predicts "Fraud," it is always right
**D)** The F1-score for the "Fraud" class will effectively be 0 (or undefined) — making overall accuracy a deeply misleading metric for this problem
**E)** A real fraud detection model that achieves 98.5% accuracy has definitively outperformed the baseline and is ready for deployment

**Correct Answers: A, B, D**

**Answer Explanation:**
- **A — Correct:** With 98.5% "Not Fraud" cases, always predicting "Not Fraud" yields 98.5% accuracy without detecting a single fraud.
- **B — Correct:** The baseline **never** predicts "Fraud." Every actual fraud transaction in the test set goes undetected → recall for "Fraud" = 0%.
- **C — Incorrect:** The baseline never predicts "Fraud" — not even once. Precision for "Fraud" = (correctly predicted fraud) / (all fraud predictions) = 0 / 0, which is **undefined**, not 100%.
- **D — Correct:** F1-score is the harmonic mean of precision and recall. With recall = 0%, F1 = 0 for the fraud class. This immediately exposes that accuracy of 98.5% means absolutely nothing useful here.
- **E — Incorrect:** A real model achieving 98.5% could be doing the exact same thing as the baseline — predicting "Not Fraud" for every transaction. To genuinely outperform, the model must show meaningfully higher **recall** and **F1-score** for the "Fraud" class specifically.
