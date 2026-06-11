# ML Workshop: Model Selection & Comparison

## Context of This Session

In the previous session, you worked with **time series** — data where **order matters**. You learned **trend** and **seasonality**, **chronological splits** (never shuffle dated rows), **rolling windows**, and forecast evaluation with **MAE**, **RMSE**, and **MAPE**.

Across this module you have also trained **regression** models, **classifiers** (Logistic Regression, Decision Trees, Random Forest), and **unsupervised** tools (**K-Means**, **PCA**). Each demo showed a metric moving in the right direction. A real project asks a harder question: *"I tried three models — which one do I actually use, and how do I hand it over for production?"*

This workshop answers that. You will build **metric tables**, judge **complexity**, bundle steps in **pipelines**, **save and load** the winner, deploy it with a simple **web UI**, and follow a **selection checklist** you can reuse on any new problem.

**In this session, you will:**

- Build a **metric comparison table** — all models and scores side by side
- Understand when **accuracy alone misleads** — and why **F1** matters for imbalanced classes
- Bundle preprocessing and models in **sklearn Pipelines**
- Compare models by **complexity** — spot **overfitting** vs **underfitting**, and tune with **GridSearchCV**
- **Save and load** trained pipelines with **joblib** (model persistence)
- Wrap a saved model in a **Gradio** web interface for end-user predictions
- Apply a **6-question selection checklist** to pick the right algorithm

---

## Metric Tables: Comparing Models Side by Side

You already know individual metrics — **MAE, RMSE, R²** for regression; **Accuracy, Precision, Recall, F1** for classification. In a real project you train **multiple models** and compare them in one view.

**Metric Table (Model Comparison Table):**

- **Official Definition:** A structured summary showing performance scores of multiple models across multiple evaluation metrics — side by side in one table.
- **In Simple Words:** A school marksheet for models — every model's scores in every subject on one page.
- **Real-Life Example:** A cricket selector comparing three bowlers — economy, wickets, consistency — without opening three separate files. Same idea for ML models.

![Metric comparison table — models and scores side by side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session34/session34_metric_comparison_table.png)

**Rules for a fair comparison:**

- Same **train/test split** on every model.
- Same **preprocessing** — scale with `fit` on train only, `transform` on test.
- Same **metrics** — do not compare accuracy on one model with F1 on another without reason.
- Place **train and test scores** together when checking for overfitting.

### When Accuracy Alone Misleads

A model can show **high accuracy** but still fail on the class that matters most.

- **Example:** A loan-default model shows **78% accuracy** — looks acceptable.
- But the **confusion matrix** reveals **0% F1** for the "default" class — the model never catches actual defaulters.
- **Why?** Accuracy counts correct negatives and positives together. If negatives dominate, a lazy model that always predicts "no default" still scores well.
- **Fix:** Read **F1, Precision, and Recall** alongside accuracy — especially in healthcare, fraud, and loan decisions where one class is critical.

**F1 Score:**

- **Official Definition:** The harmonic mean of precision and recall — balances both in one number.
- **In Simple Words:** Class-level accuracy — how well the model handles the positive class you care about.
- **Real-Life Example:** A cancer screening test — you care how often real cases are caught (recall) and how often alarms are false (precision). F1 combines both.

### Quick Activity — Pick the Right Metrics

Match the problem to the metric set:

1. Loan default (Pass/Fail) → **Accuracy, Precision, Recall, F1**
2. House price prediction → **MAE, RMSE, R²**
3. Hospital tumour classification (benign vs malignant) → **Accuracy, Precision, Recall, F1** — prioritise **F1** over raw accuracy

**Key idea:** The metric must match the **business question** — not just the highest number on any chart.

---

### Code: Classification Metric Table

```python
import pandas as pd  # tables and DataFrames
import numpy as np  # numeric helpers
from sklearn.datasets import load_breast_cancer  # sample classification data
from sklearn.model_selection import train_test_split  # train/test split
from sklearn.preprocessing import StandardScaler  # scale features
from sklearn.pipeline import Pipeline  # bundle preprocessing + model
from sklearn.linear_model import LogisticRegression  # simple classifier
from sklearn.tree import DecisionTreeClassifier  # medium-complexity classifier
from sklearn.ensemble import RandomForestClassifier  # complex classifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # metrics

data = load_breast_cancer()  # 569 rows, 30 features
X, y = data.data, data.target  # features and labels (0/1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # 80% train, 20% test
)

models = {  # dictionary of pipelines to compare
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),  # step 1: scale features
        ("model", LogisticRegression(max_iter=1000))  # step 2: simple classifier
    ]),
    "Decision Tree": Pipeline([
        ("scaler", StandardScaler()),  # step 1: scale (good practice even for trees)
        ("model", DecisionTreeClassifier(random_state=42))  # step 2: tree classifier
    ]),
    "Random Forest": Pipeline([
        ("scaler", StandardScaler()),  # step 1: scale features
        ("model", RandomForestClassifier(n_estimators=100, random_state=42))  # step 2: ensemble
    ])
}

results = []  # list to collect one row per model
for model_name, pipeline in models.items():  # train and score each candidate
    pipeline.fit(X_train, y_train)  # fit scaler on train, then train model
    y_pred = pipeline.predict(X_test)  # predict on held-out test
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

- `load_breast_cancer()` — real medical data with 30 tumour features (same domain as the Wisconsin dataset used in class).
- Each entry in `models` is a **Pipeline** — scaler and model trained as one unit.
- Three candidates: **Logistic Regression** (simple), **Decision Tree** (medium), **Random Forest** (complex).
- `pd.DataFrame(results)` turns the list of dicts into a readable comparison table.
- Compare **F1** carefully — it reveals class-level performance that accuracy can hide.

---

### Code: Regression Metric Table

Same pattern — swap in regression models and metrics (**lower MAE/RMSE = better**, **R² closer to 1 = better**).

```python
import pandas as pd  # tables
import numpy as np  # sqrt for RMSE
from sklearn.datasets import fetch_california_housing  # house price data
from sklearn.model_selection import train_test_split  # split
from sklearn.preprocessing import StandardScaler  # scale
from sklearn.pipeline import Pipeline  # bundle preprocessing + model
from sklearn.linear_model import LinearRegression  # simple regressor
from sklearn.ensemble import RandomForestRegressor  # complex regressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # regression metrics

data = fetch_california_housing()  # 20,640 rows, target = house price
X, y = data.data, data.target  # features and continuous target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80/20 split

models = {  # regression pipelines to compare
    "Linear Regression": Pipeline([
        ("scaler", StandardScaler()),  # step 1: scale features
        ("model", LinearRegression())  # step 2: simple linear model
    ]),
    "Random Forest": Pipeline([
        ("scaler", StandardScaler()),  # step 1: scale features
        ("model", RandomForestRegressor(n_estimators=100, random_state=42))  # step 2: ensemble model
    ])
}

results = []  # collect one metrics row per model
for model_name, pipeline in models.items():  # loop through each candidate
    pipeline.fit(X_train, y_train)  # fit scaler + model on training data
    y_pred = pipeline.predict(X_test)  # predict on held-out test
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

## sklearn Pipelines: Bundle Preprocessing and Model

Once you compare models fairly, you need a reliable way to keep preprocessing and training **locked together**. That is what a **Pipeline** does.

**Pipeline:**

- **Official Definition:** An sklearn object that chains preprocessing steps and a model into a single estimators — fit and predict run through every step in order.
- **In Simple Words:** A fixed recipe — wash the vegetables, then cook — always in the same order, every time.
- **Real-Life Example:** A bank loan form that always runs identity check → income check → credit score before the final decision. You never skip a step.

**Why pipelines matter for model selection:**

- Every model in your comparison table gets the **same preprocessing**.
- When you save the winner, you save **scaler + model together** — no mismatch at prediction time.
- Steps can include `StandardScaler`, encoders, and the final estimator in one object.

```python
from sklearn.pipeline import Pipeline  # chain steps
from sklearn.preprocessing import StandardScaler  # numeric scaling
from sklearn.ensemble import RandomForestClassifier  # final model

pipeline_rf = Pipeline([
    ("scaler", StandardScaler()),  # step name + transformer class
    ("model", RandomForestClassifier(n_estimators=100, random_state=42))  # step name + model
])

pipeline_rf.fit(X_train, y_train)  # fit scaler on train, then fit model
y_pred = pipeline_rf.predict(X_test)  # scale test data with fitted scaler, then predict
```

**How the code works:**

- `Pipeline([...])` takes a list of `(name, object)` pairs — names are labels for debugging.
- `.fit()` runs each step in order — the scaler learns from train; the model trains on scaled data.
- `.predict()` applies the **same fitted scaler** to new data before the model predicts.
- This is the pattern used for every model in the workshop demos.

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
| Gradient Boosting | Very High | Slow | Low | Max accuracy, big data |

- **Interpretability** — can a non-technical person understand *why* the model said yes or no? Banks and hospitals often need this. Recommendation engines often do not.
- A **1% accuracy gain** from a complex model may cost **10× more compute** — always ask if the gain is worth it.

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
for depth in [1, 3, 5, None]:  # 1 = stump, 3-5 = moderate, None = unlimited
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
- Depth **3** often balances test score and gap on small datasets — exactly the pattern explored in the live demo.

### Hyperparameter Tuning with GridSearchCV

Manually trying `max_depth = 1, 2, 3...` works for learning — but in production you automate the search.

**GridSearchCV:**

- **Official Definition:** A sklearn tool that trains models across a grid of hyperparameter combinations and picks the best using cross-validation.
- **In Simple Words:** Try every combination on a menu automatically — pick the dish that scores highest.
- **Real-Life Example:** Testing 6 different oven temperatures and 4 baking times — GridSearchCV runs all 24 combos and reports the winner.

```python
from sklearn.model_selection import GridSearchCV  # automated hyperparameter search
from sklearn.ensemble import RandomForestRegressor  # model to tune
from sklearn.pipeline import Pipeline  # pipeline with scaler + model
from sklearn.preprocessing import StandardScaler  # scaling step

pipe_rf = Pipeline([
    ("scaler", StandardScaler()),  # preprocessing step
    ("model", RandomForestRegressor(random_state=42))  # model to tune
])

param_grid = {
    "model__n_estimators": [50, 100, 200, 300, 400]  # try these tree counts
}

grid_search = GridSearchCV(
    estimator=pipe_rf,  # pipeline to search over
    param_grid=param_grid,  # hyperparameter grid
    cv=3,  # 3-fold cross-validation
    n_jobs=-1,  # use all CPU cores
    verbose=1  # print progress
)

grid_search.fit(X_train, y_train)  # run all combinations — takes time
print("Best n_estimators:", grid_search.best_params_)  # winning hyperparameters
print("Best CV score:", grid_search.best_score_)  # best cross-validated score

best_rf_pipeline = grid_search.best_estimator_  # full fitted pipeline — ready to save
```

**How the code works:**

- `param_grid` keys use `model__` prefix because `n_estimators` lives inside the `"model"` pipeline step.
- `GridSearchCV` trains every combination, scores with cross-validation, and stores the winner in `best_estimator_`.
- `n_jobs=-1` uses all CPU cores — important because grid search is **computationally expensive**.
- The output `best_rf_pipeline` is the final model used for persistence and deployment in the California housing demo.

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

### Code: Save and Load the Full Pipeline with joblib

`joblib` is the **recommended** way to save scikit-learn models. Save the **entire fitted pipeline** — scaler, encoders, and model together.

```python
import joblib  # save/load sklearn models efficiently
from sklearn.ensemble import RandomForestRegressor  # model inside pipeline
from sklearn.pipeline import Pipeline  # bundle preprocessing + model
from sklearn.preprocessing import StandardScaler  # scaling step

# Uses X_train, y_train from earlier examples
best_rf_pipeline = Pipeline([
    ("scaler", StandardScaler()),  # preprocessing step
    ("model", RandomForestRegressor(n_estimators=400, random_state=42))  # tuned winner
])
best_rf_pipeline.fit(X_train, y_train)  # train the full pipeline once
print("Pipeline trained!")

joblib.dump(best_rf_pipeline, 'best_rf_pipeline.joblib')  # save entire pipeline to disk
print("Pipeline saved!")

loaded_pipeline = joblib.load('best_rf_pipeline.joblib')  # reload from file on any machine
predictions = loaded_pipeline.predict(X_test)  # predict — scaler applied automatically
print(f"First 10 predictions: {predictions[:10]}")  # sanity-check output
```

**How the code works:**

- `joblib.dump(pipeline, 'file.joblib')` — writes the **full pipeline** (fitted scaler + trained model) to disk.
- `joblib.load('file.joblib')` — reconstructs everything; call `.predict()` immediately on raw input features.
- **Save the pipeline, not just the model** — a fresh `StandardScaler()` on new data produces different values → wrong predictions. This is the most common beginner mistake.
- In the live demo, the developer notebook trains and saves; a **separate inference notebook** on another machine loads and predicts — no retraining needed.

### joblib vs pickle

| | **joblib** | **pickle** |
|---|---|---|
| sklearn recommendation | **Yes** | Works, not optimised |
| Speed on large models | Faster | Slower |
| Typical extension | `.joblib` | `.pkl` |

- Use **`joblib`** for sklearn models and pipelines. `pickle` is Python's general-purpose option for lists, dicts, and other native objects.

**Production tips:**

- Save the **full fitted pipeline** (preprocessing + model) — not separate files unless you have a strong reason.
- Use versioned filenames — e.g. `rf_pipeline_v1_2024-06-01.joblib`.
- **Test the loaded model** on a small batch before deployment.
- Never load `.joblib` / `.pkl` files from **untrusted sources** — they can execute malicious code on your machine.

---

## Deploying with Gradio: A Simple Web Interface

Saving a model is step one. Step two is letting a **non-technical user** enter inputs and get a prediction — without opening a notebook.

**Gradio:**

- **Official Definition:** A Python library that wraps a prediction function in a shareable web UI with input fields and output display.
- **In Simple Words:** A ready-made form for your model — users type values, click submit, see the result.
- **Real-Life Example:** A house-price estimator on a bank website — enter income, rooms, location; get an estimated price instantly.

```python
import joblib  # load saved pipeline
import gradio as gr  # web UI library

loaded_pipeline = joblib.load('best_rf_pipeline.joblib')  # load persisted pipeline

def predict_price(med_inc, house_age, avg_rooms, avg_bedrooms, population, latitude, longitude):
    import numpy as np  # build input array
    features = np.array([[med_inc, house_age, avg_rooms, avg_bedrooms, population, latitude, longitude]])
    prediction = loaded_pipeline.predict(features)  # pipeline handles scaling + prediction
    return f"Estimated price: ${prediction[0]:,.0f}"  # format result for display

demo = gr.Interface(
    fn=predict_price,  # function to call on submit
    inputs=[
        gr.Number(label="Median Income"),  # input field 1
        gr.Number(label="House Age"),  # input field 2
        gr.Number(label="Avg Rooms"),  # input field 3
        gr.Number(label="Avg Bedrooms"),  # input field 4
        gr.Number(label="Population"),  # input field 5
        gr.Number(label="Latitude"),  # input field 6
        gr.Number(label="Longitude")  # input field 7
    ],
    outputs=gr.Textbox(label="Prediction"),  # where result appears
    title="California Housing Price Estimator"  # page title
)

demo.launch(share=True)  # start web app — share=True gives a public link
```

**How the code works:**

- `joblib.load()` brings back the saved pipeline — only **Gradio** needs to be installed in the inference environment.
- `predict_price()` takes user inputs, builds a feature array, and calls `loaded_pipeline.predict()`.
- `gr.Interface` maps input widgets to function arguments and displays the return value.
- `demo.launch(share=True)` opens a browser UI — the same pattern used to demo the housing model to a "client team" in class.
- **Development notebook ≠ inference notebook** — train and tune in one place; load and deploy in another.

---

## Model Selection Checklist

Metric tables, complexity, pipelines, persistence, and deployment answer *"which trained model wins and how do I ship it?"* The checklist answers *"which algorithms should I even try first?"*

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

**2. How much data?**

- **Small (< 1,000 rows):** Logistic Regression, shallow Decision Tree — complex models overfit.
- **Medium (1K–100K):** Random Forest, Gradient Boosting.
- **Large (100K+):** Gradient Boosting, ensemble methods with tuning.

**3. Need interpretability?**

- **Yes** (bank, hospital, legal): Logistic Regression, Decision Tree, Linear Regression.
- **No** (recommendations, fraud at scale): Random Forest, boosting.

**4. Speed requirements?**

- **Fast train + predict:** Linear / Logistic Regression.
- **Slow train, fast predict:** Random Forest.
- **Accuracy over everything:** Gradient Boosting with GridSearchCV.

**5. Linear relationship?**

- **Yes:** Linear or Logistic Regression may be enough.
- **No / unsure:** Start linear; if residuals look curved, try trees or Random Forest.

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
2. **Medium** — Decision Tree. Add to table.
3. **Complex** — Random Forest with GridSearchCV. Add to table.
4. **Complexity filter** — if the simple model is within **~2%** of the best F1 or R², pick the **simple** one.
5. **Save** — `joblib.dump()` the winning **pipeline**.

```python
import joblib  # persistence
from sklearn.linear_model import LogisticRegression  # simple model
from sklearn.ensemble import RandomForestClassifier  # complex model
from sklearn.pipeline import Pipeline  # bundle steps
from sklearn.preprocessing import StandardScaler  # scaling
from sklearn.metrics import f1_score  # selection metric

# Uses X_train, X_test, y_train, y_test from classification example
models = {  # ordered simple → complex for selection rule
    "Logistic Regression (Simple)": Pipeline([
        ("scaler", StandardScaler()),  # preprocessing
        ("model", LogisticRegression(max_iter=1000))  # baseline classifier
    ]),
    "Random Forest (Complex)": Pipeline([
        ("scaler", StandardScaler()),  # preprocessing
        ("model", RandomForestClassifier(n_estimators=100, random_state=42))  # complex option
    ])
}

results = {}  # store pipeline object and score
for name, pipeline in models.items():  # train and evaluate each candidate
    pipeline.fit(X_train, y_train)  # train full pipeline
    f1 = f1_score(y_test, pipeline.predict(X_test))  # score on same test set
    results[name] = {"pipeline": pipeline, "F1-Score": round(f1, 4)}  # keep pipeline and metric
    print(f"{name}: F1 = {f1:.4f}")  # print score for this candidate

best_f1 = max(v["F1-Score"] for v in results.values())  # find top F1 score
selected_name = None  # will hold the chosen model name
for name, info in results.items():  # dict order = simple first
    if best_f1 - info["F1-Score"] <= 0.02:  # within 2 points of best?
        selected_name = name  # pick simplest qualifying model
        break  # stop at first simple enough model

selected_pipeline = results[selected_name]["pipeline"]  # get trained pipeline
print(f"\nSelected: {selected_name}")  # show which model won

joblib.dump(selected_pipeline, 'selected_pipeline.joblib')  # save winning pipeline to disk
print("Pipeline saved!")  # confirm persistence step completed
```

**How the code works:**

- Dictionary order puts **simple model first** — the loop picks the first model within 2% of the best F1.
- If Logistic Regression is close enough to Random Forest, you keep the simpler, faster, more explainable model.
- The **full pipeline** is saved — preprocessing and model travel together, ready for deployment.

---

## Key Takeaways

- **Metric tables** are the professional standard — same split, same preprocessing, all models and metrics in one DataFrame. Always read **F1** alongside accuracy for classification — high accuracy can hide failure on the class that matters.
- **Pipelines** lock preprocessing and model together — fair comparisons, correct persistence, and safe inference on new machines.
- **Complexity matters** as much as the headline score — check **train vs test gap** for overfitting; use **GridSearchCV** to tune hyperparameters programmatically; prefer the **simplest model within ~2%** of the best.
- **Model persistence** with `joblib.dump()` / `joblib.load()` lets you train once and predict many times — always save the **full fitted pipeline**.
- **Gradio** turns a saved pipeline into a shareable web UI — separate your training notebook from your inference/deployment notebook.
- The **6-question checklist** (problem type → data size → interpretability → speed → linearity → noise) narrows choices before you waste hours on the wrong algorithm family.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means |
|---|---|
| **Metric table** | DataFrame comparing multiple models across metrics side by side |
| **Confusion matrix** | Table of true/false positives and negatives — reveals hidden accuracy traps |
| **F1 score** | Harmonic mean of precision and recall — class-level performance |
| **Pipeline** | sklearn object chaining preprocessing steps and a model |
| **Model complexity** | How flexible a model is — more parameters = usually more complex |
| **Overfitting** | High train score, much lower test score — memorised noise |
| **Underfitting** | Low scores on both train and test — too simple |
| **Train–test gap** | Train accuracy minus test accuracy — large gap signals overfitting |
| **GridSearchCV** | Automated search over a hyperparameter grid with cross-validation |
| **Occam's Razor** | Prefer the simplest adequate model |
| **Model persistence** | Save trained pipeline to disk for reuse |
| **Gradio** | Python library for building a web UI around a prediction function |
| **Model selection checklist** | 6-question guide to pick algorithm family |
| `joblib.dump(obj, 'file.joblib')` | Save object (pipeline) to disk |
| `joblib.load('file.joblib')` | Load saved object |
| `Pipeline([("name", step), ...])` | Chain preprocessing and model steps |
| `GridSearchCV(estimator, param_grid)` | Search hyperparameters automatically |
| `gr.Interface(fn, inputs, outputs)` | Build a Gradio web form |
| `pd.DataFrame(list_of_dicts)` | Build table from list of row dicts |
| `.set_index("Model")` | Use model name as row label |
| `f1_score()` | Classification metric — balance of precision and recall |
| `mean_absolute_error()` | Regression error — lower is better |
| `r2_score()` | Regression fit quality — closer to 1 is better |
| `max_depth` | Tree depth limit — controls complexity |
| `n_estimators` | Number of trees in Random Forest |
| `n_jobs=-1` | Use all CPU cores (common in GridSearchCV) |
