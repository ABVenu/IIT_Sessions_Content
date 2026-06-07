# ML Workshop: Model Selection & Comparison

## Context of This Session

In the previous session, you worked with **time series** — data where **order matters**. You learned **trend** and **seasonality**, **chronological splits** (never shuffle dated rows), **rolling windows**, and forecast evaluation with **MAE**, **RMSE**, and **MAPE** — always checked against a **naive baseline**.

Across this module you have also trained **regression** models, **classifiers** (Logistic Regression, Decision Trees, Random Forest), and **unsupervised** tools (**K-Means**, **PCA**). Each demo showed a metric moving in the right direction. A real project asks a harder question: *"I tried three models — which one do I actually use, and how do I hand it over for production?"*

This workshop answers that. You will build **metric tables**, judge **complexity**, **save and load** the winner, and follow a **selection checklist** you can reuse on any new problem.

**In this session, you will:**

- Build a **metric comparison table** — all models and scores side by side
- Compare models by **complexity** — and spot **overfitting** vs **underfitting**
- **Save and load** trained models with **joblib** (model persistence)
- Apply a **6-question selection checklist** to pick the right algorithm

---

## Metric Tables: Comparing Models Side by Side

You already know individual metrics — **MAE, RMSE, R²** for regression; **Accuracy, Precision, Recall, F1** for classification; **MAPE** for time-series forecasts. In a real project you train **multiple models** and compare them in one view.

**Metric Table (Model Comparison Table):**

- **Official Definition:** A structured summary showing performance scores of multiple models across multiple evaluation metrics — side by side in one table.
- **In Simple Words:** A school marksheet for models — every model's scores in every subject on one page.
- **Real-Life Example:** A cricket selector comparing three bowlers — economy, wickets, consistency — without opening three separate files. Same idea for ML models.

![Metric comparison table — models and scores side by side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_metric_comparison_table.png)

**Rules for a fair comparison:**

- Same **train/test split** (or same chronological holdout for time series).
- Same **preprocessing** — scale with `fit` on train only, `transform` on test.
- Same **metrics** — do not compare accuracy on one model with F1 on another without reason.
- For time series: compare on the **future holdout**, not shuffled rows.

### Quick Activity — Pick the Right Metrics

Match the problem to the metric set:

1. Loan default (Pass/Fail) → **Accuracy, Precision, Recall, F1**
2. House price prediction → **MAE, RMSE, R²**
3. Daily sales forecast (time series) → **MAE, RMSE, MAPE** on chronological test

**Key idea:** The metric must match the **business question** — not just the highest number on any chart.

---

### Code: Classification Metric Table

```python
import pandas as pd  # tables and DataFrames
import numpy as np  # numeric helpers
from sklearn.datasets import load_breast_cancer  # sample classification data
from sklearn.model_selection import train_test_split  # train/test split
from sklearn.preprocessing import StandardScaler  # scale features
from sklearn.linear_model import LogisticRegression  # simple classifier
from sklearn.ensemble import RandomForestClassifier  # complex classifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # metrics

data = load_breast_cancer()  # 569 rows, 30 features
X, y = data.data, data.target  # features and labels (0/1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # 80% train, 20% test
)

scaler = StandardScaler()  # create scaler object
X_train = scaler.fit_transform(X_train)  # fit on train, transform train
X_test = scaler.transform(X_test)  # only transform test — never fit on test

models = {  # dictionary of models to compare
    "Logistic Regression": LogisticRegression(max_iter=1000),  # simple linear classifier
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)  # ensemble classifier
}

results = []  # list to collect one row per model
for model_name, model in models.items():  # train and score each candidate
    model.fit(X_train, y_train)  # train on training data
    y_pred = model.predict(X_test)  # predict on held-out test
    results.append({  # store metrics for this model
        "Model": model_name,  # model label for the table row
        "Accuracy": round(accuracy_score(y_test, y_pred), 4),  # overall correct rate
        "Precision": round(precision_score(y_test, y_pred), 4),  # positive prediction quality
        "Recall": round(recall_score(y_test, y_pred), 4),  # positive class capture rate
        "F1-Score": round(f1_score(y_test, y_pred), 4)  # balance of precision and recall
    })

comparison_df = pd.DataFrame(results).set_index("Model")  # build comparison table
print(comparison_df)  # print side-by-side scores
```

**How the code works:**

- `load_breast_cancer()` — real medical data with 30 tumour features.
- `StandardScaler` — mandatory for Logistic Regression; large-valued features would otherwise dominate.
- Models stored in a **dictionary** — one loop trains, predicts, and scores both.
- `pd.DataFrame(results)` turns the list of dicts into a readable comparison table.

**Sample output:**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.9737 | 0.9726 | 0.9859 | 0.9792 |
| Random Forest | 0.9649 | 0.9589 | 0.9859 | 0.9722 |

- Logistic Regression wins on F1 here despite being **simpler** — the table makes that visible instantly.
- Without the table, you would jump between separate printouts to reach the same conclusion.

---

### Code: Regression Metric Table

Same pattern — swap in regression models and metrics (**lower MAE/RMSE = better**, **R² closer to 1 = better**).

```python
import pandas as pd  # tables
import numpy as np  # sqrt for RMSE
from sklearn.datasets import fetch_california_housing  # house price data
from sklearn.model_selection import train_test_split  # split
from sklearn.preprocessing import StandardScaler  # scale
from sklearn.linear_model import LinearRegression  # simple regressor
from sklearn.ensemble import RandomForestRegressor  # complex regressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # regression metrics

data = fetch_california_housing()  # 20,640 rows, target = house price
X, y = data.data, data.target  # features and continuous target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80/20 split
scaler = StandardScaler()  # create scaler for regression features
X_train = scaler.fit_transform(X_train)  # fit scaler on train only
X_test = scaler.transform(X_test)  # transform test with train-fitted scaler

models = {  # regression models to compare
    "Linear Regression": LinearRegression(),  # simple linear model
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)  # ensemble model
}

results = []  # collect one metrics row per model
for model_name, model in models.items():  # loop through each candidate
    model.fit(X_train, y_train)  # train on training data
    y_pred = model.predict(X_test)  # predict on held-out test
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # RMSE = sqrt of MSE
    results.append({  # store metrics for this model
        "Model": model_name,  # model label for the table row
        "MAE": round(mean_absolute_error(y_test, y_pred), 4),  # mean absolute error
        "RMSE": round(rmse, 4),  # root mean squared error
        "R²": round(r2_score(y_test, y_pred), 4)  # variance explained score
    })

print(pd.DataFrame(results).set_index("Model"))  # print comparison table
```

**How the code works:**

- `fetch_california_housing()` — realistic regression task (predict house price from 8 features).
- `np.sqrt(mean_squared_error(...))` — sklearn returns MSE; RMSE needs the square root.
- Random Forest often wins on tabular regression — but always verify on **your** test set, not assumptions.

---

## Comparison by Complexity

A metric table shows **who scored highest**. Complexity asks **whether that win is worth the cost** — training time, interpretability, overfitting risk.

**Model Complexity:**

- **Official Definition:** How flexible a model is when fitting patterns — simple models have few parameters and strong assumptions; complex models have many parameters and can fit intricate non-linear shapes.
- **In Simple Words:** A one-size-fits-all shirt vs a custom-tailored shirt — custom fits one person perfectly but is expensive and fails if measurements were wrong.
- **Real-Life Example:** Essay grading by word count (simple) vs deep literary analysis (complex). Sometimes the simple rule is good enough for a quick placement test.

![Model complexity spectrum — from simple assumptions to flexible models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_complexity_spectrum.png)

| Model | Complexity | Speed | Interpretability | Typical use |
|---|---|---|---|---|
| Logistic / Linear Regression | Very Low | Very Fast | Very High | Baseline, explainable |
| Decision Tree | Medium | Fast | High | Explainable rules |
| Random Forest | High | Moderate | Medium | General-purpose |
| Gradient Boosting / Neural Nets | Very High | Slow | Low | Max accuracy, big data |

- **Interpretability** — can a non-technical person understand *why* the model said yes or no? Banks and hospitals often need this. Recommendation engines often do not.

---

### Overfitting vs Underfitting

The core tension when comparing by complexity.

**Overfitting:**

- **Official Definition:** Model is so complex it **memorises** training data including noise — high train score, much lower test score.
- **In Simple Words:** Student who memorised past exam papers word-for-word — fails when questions change slightly.

**Underfitting:**

- **Official Definition:** Model is too simple to capture real patterns — low scores on **both** train and test.
- **In Simple Words:** Student who studied only 2 of 10 chapters — weak everywhere.

![Underfitting vs good fit vs overfitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_overfitting_underfitting.png)

**Detection rule:** Compare **train accuracy vs test accuracy**. A **large gap** = overfitting red flag. Never judge a model on training score alone.

### Code: Spotting Overfitting with Tree Depth

```python
from sklearn.tree import DecisionTreeClassifier  # tree model
from sklearn.metrics import accuracy_score  # accuracy metric
import pandas as pd  # table output

# Uses X_train, X_test, y_train, y_test from the classification example above
results = []  # store train/test gap for each depth setting
for depth in [1, 5, None]:  # 1 = very simple, None = unlimited depth
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)  # set complexity
    model.fit(X_train, y_train)  # train tree on training data
    train_acc = accuracy_score(y_train, model.predict(X_train))  # score on train
    test_acc = accuracy_score(y_test, model.predict(X_test))  # score on test
    results.append({  # add one row for this depth
        "Max Depth": str(depth) if depth else "Unlimited",  # readable depth label
        "Train Accuracy": round(train_acc, 4),  # training-set accuracy
        "Test Accuracy": round(test_acc, 4),  # test-set accuracy
        "Gap (Train-Test)": round(train_acc - test_acc, 4)  # large gap = overfitting
    })

print(pd.DataFrame(results).set_index("Max Depth"))  # print train vs test table
```

**How the code works:**

- `max_depth` controls tree complexity — 1 is a stump; `None` grows until training points are perfectly separated.
- **Gap column** is the key signal — unlimited depth often hits 100% train but drops on test.

**Sample output:**

| Max Depth | Train Accuracy | Test Accuracy | Gap |
|---|---|---|---|
| 1 | 0.9253 | 0.9123 | 0.0130 |
| 5 | 0.9714 | 0.9474 | 0.0240 |
| Unlimited | 1.0000 | 0.9035 | 0.0965 |

- Depth 5 is the **sweet spot** here — good test score, small gap.
- Unlimited = classic **overfitting** — memorised training noise.

### Quick Activity — Read the Gap

A model shows **99% train accuracy** and **72% test accuracy**. What is happening?

- **Overfitting** — huge train–test gap. The model memorised training data; do not deploy it.
- **Fix:** Simpler model, less depth, more data, or stronger regularization.

### The Golden Rule

**Prefer simpler when:**

- Small dataset (< 1,000 rows), interpretability required, simple model already scores well, or real-time speed matters.

**Go complex when:**

- Large dataset, accuracy is top priority, clear non-linear patterns, and you have compute budget.

**Occam's Razor in ML:** *The simplest model that fits the data well is usually the best.* Start simple; add complexity only when the metric table proves you need it.

---

## Model Persistence: Saving and Loading

You picked a winner. Now you must **reuse it without retraining every time**.

**Model Persistence:**

- **Official Definition:** Saving a trained model to disk so it can be loaded later and used for predictions without retraining.
- **In Simple Words:** Save-game for ML — train once, load anytime.
- **Real-Life Example:** Your email spam filter was trained on millions of emails, then saved. Each new email loads the saved model and scores it in milliseconds.

![Model persistence — train, save to disk, load, predict](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_persistence_save_load.png)

### Code: Save and Load with joblib

`joblib` is the **recommended** way to save scikit-learn models.

```python
import joblib  # save/load sklearn models efficiently
from sklearn.ensemble import RandomForestClassifier  # model to train

# Uses X_train, X_test, scaler from earlier classification example
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # create model
rf_model.fit(X_train, y_train)  # train on training data
print("Model trained!")

joblib.dump(rf_model, 'random_forest_model.joblib')  # save trained model to disk
joblib.dump(scaler, 'scaler.joblib')  # save fitted scaler alongside model
print("Model and scaler saved!")

loaded_model = joblib.load('random_forest_model.joblib')  # reload model from file
loaded_scaler = joblib.load('scaler.joblib')  # reload same fitted scaler
predictions = loaded_model.predict(loaded_scaler.transform(X_test))  # predict with loaded objects
print(f"First 10 predictions: {predictions[:10]}")  # sanity-check output
```

**How the code works:**

- `joblib.dump(object, 'file.joblib')` — writes the full trained model (parameters, trees, etc.) to disk.
- `joblib.load('file.joblib')` — reconstructs the model; call `.predict()` immediately.
- **Always save the scaler** — a fresh `StandardScaler()` on new data produces different values → wrong predictions. This is the most common beginner mistake.

### joblib vs pickle

| | **joblib** | **pickle** |
|---|---|---|
| sklearn recommendation | **Yes** | Works, not optimised |
| Speed on large models | Faster | Slower |
| Typical extension | `.joblib` | `.pkl` |

- Use **`joblib`** for sklearn models. `pickle` is Python's general-purpose option for other objects.

**Production tips:**

- Save **all preprocessing** (scaler, encoders) with the model.
- Use versioned filenames — e.g. `rf_model_v1_2024-06-01.joblib`.
- **Test the loaded model** on a small batch before deployment.
- Never load `.joblib` / `.pkl` files from **untrusted sources** — they can execute malicious code.

---

## Model Selection Checklist

Metric tables, complexity, and persistence answer *"which trained model wins?"* The checklist answers *"which algorithms should I even try first?"*

**Model Selection Checklist:**

- **Official Definition:** A step-by-step decision guide for choosing the right algorithm based on problem type, data size, interpretability, speed, and noise.
- **In Simple Words:** A doctor's intake form before prescribing medicine — symptoms and constraints first, drug second.
- **Real-Life Example:** Picking a phone by battery and camera needs — not by the flashiest benchmark ad.

![Model selection checklist — structured decision path](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_model_selection_checklist_flow.png)

### The 6 Questions

**1. Problem type?**

| Type | Go-to models |
|---|---|
| Binary classification | Logistic Regression, Decision Tree, Random Forest |
| Regression (number) | Linear Regression, Random Forest Regressor |
| No labels (clustering) | K-Means |
| Many columns, need 2D view | PCA |
| Time series forecast | Rolling features + Regression; chronological split + MAPE |

**2. How much data?**

- **Small (< 1,000 rows):** Logistic Regression, shallow Decision Tree — complex models overfit.
- **Medium (1K–100K):** Random Forest, Gradient Boosting.
- **Large (100K+):** Gradient Boosting, Neural Networks.

**3. Need interpretability?**

- **Yes** (bank, hospital, legal): Logistic Regression, Decision Tree, Linear Regression.
- **No** (recommendations, fraud at scale): Random Forest, boosting, neural nets.

**4. Speed requirements?**

- **Fast train + predict:** Linear / Logistic Regression.
- **Slow train, fast predict:** Random Forest.
- **Accuracy over everything:** Gradient Boosting, deep models.

**5. Linear relationship?**

- **Yes:** Linear or Logistic Regression may be enough.
- **No / unsure:** Start linear; if residuals look curved, try trees.

**6. Outliers or noisy features?**

- **Yes:** Trees / Random Forest (threshold splits) beat plain Linear Regression.
- **No:** Start with the simplest model.

### Quick Activity — Walk the Checklist

A **fintech team** predicts **loan default** (yes/no) on **800 labelled rows**. Auditors need a written reason for every rejection.

- Problem type → **binary classification**
- Data size → **small** → start Logistic Regression or shallow tree
- Interpretability → **required** → Logistic Regression or Decision Tree (depth 3–7)
- First step → train simple model, build **metric table**, compare F1 — do not jump to Random Forest first

### The "Start Simple, Go Complex" Protocol

1. **Baseline** — simplest relevant model (Logistic / Linear Regression). Record metrics in a table.
2. **Medium** — Decision Tree or SVM. Add to table.
3. **Complex** — Random Forest or boosting. Add to table.
4. **Complexity filter** — if the simple model is within **~2%** of the best F1 or R², pick the **simple** one.
5. **Save** — `joblib.dump()` the winner **and** the scaler.

```python
import joblib  # persistence
from sklearn.linear_model import LogisticRegression  # simple model
from sklearn.ensemble import RandomForestClassifier  # complex model
from sklearn.metrics import f1_score  # selection metric

# Uses X_train, X_test, y_train, y_test, scaler from classification example
models = {  # ordered simple → complex for selection rule
    "Logistic Regression (Simple)": LogisticRegression(max_iter=1000),  # baseline classifier
    "Random Forest (Complex)": RandomForestClassifier(n_estimators=100, random_state=42)  # complex option
}

results = {}  # store model object and score
for name, model in models.items():  # train and evaluate each candidate
    model.fit(X_train, y_train)  # train each candidate
    f1 = f1_score(y_test, model.predict(X_test))  # score on same test set
    results[name] = {"model_object": model, "F1-Score": round(f1, 4)}  # keep model and metric
    print(f"{name}: F1 = {f1:.4f}")  # print score for this candidate

best_f1 = max(v["F1-Score"] for v in results.values())  # find top F1 score
selected_name = None  # will hold the chosen model name
for name, info in results.items():  # dict order = simple first
    if best_f1 - info["F1-Score"] <= 0.02:  # within 2 points of best?
        selected_name = name  # pick simplest qualifying model
        break  # stop at first simple enough model

selected_model = results[selected_name]["model_object"]  # get trained model object
print(f"\nSelected: {selected_name}")  # show which model won

joblib.dump(selected_model, 'selected_model.joblib')  # save winner to disk
joblib.dump(scaler, 'scaler.joblib')  # save scaler used in training
print("Model and scaler saved!")  # confirm persistence step completed
```

**How the code works:**

- Dictionary order puts **simple model first** — the loop picks the first model within 2% of the best F1.
- If Logistic Regression is close enough to Random Forest, you keep the simpler, faster, more explainable model.
- Both model and scaler saved — ready for deployment without retraining.

---

## Key Takeaways

- **Metric tables** are the professional standard — same split, same preprocessing, all models and metrics in one DataFrame. For time series, that means **chronological holdout** and metrics like **MAPE**, not shuffled rows.
- **Complexity matters** as much as the headline score — check **train vs test gap** for overfitting; prefer the **simplest model within ~2%** of the best.
- **Model persistence** with `joblib.dump()` / `joblib.load()` lets you train once and predict many times — always save the **fitted scaler** with the model.
- The **6-question checklist** (problem type → data size → interpretability → speed → linearity → noise) narrows choices before you waste hours on the wrong algorithm family.
- **Start simple, go complex** — baseline first, metric table second, save the winner third. This closes Module 2's ML toolkit and prepares you for end-to-end workflows ahead.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means |
|---|---|
| **Metric table** | DataFrame comparing multiple models across metrics side by side |
| **Model complexity** | How flexible a model is — more parameters = usually more complex |
| **Overfitting** | High train score, much lower test score — memorised noise |
| **Underfitting** | Low scores on both train and test — too simple |
| **Train–test gap** | Train accuracy minus test accuracy — large gap signals overfitting |
| **Occam's Razor** | Prefer the simplest adequate model |
| **Model persistence** | Save trained model to disk for reuse |
| **Model selection checklist** | 6-question guide to pick algorithm family |
| `joblib.dump(model, 'file.joblib')` | Save object to disk |
| `joblib.load('file.joblib')` | Load saved object |
| `pd.DataFrame(list_of_dicts)` | Build table from list of row dicts |
| `.set_index("Model")` | Use model name as row label |
| `f1_score()` | Classification metric — balance of precision and recall |
| `mean_absolute_error()` | Regression error — lower is better |
| `r2_score()` | Regression fit quality — closer to 1 is better |
| `max_depth` | Tree depth limit — controls complexity |
| `n_estimators` | Number of trees in Random Forest |
| `.fit_transform(X_train)` | Fit scaler on train and transform |
| `.transform(X_test)` | Apply fitted scaler to test/new data |
