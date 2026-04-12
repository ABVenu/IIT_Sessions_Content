# **The ML Workflow & Habits**

# **1. Introduction to Google Colab Notebook**

## **What is Google Colab?**

Google Colab (short for Colaboratory) is a cloud-based platform for writing and executing Python code in the browser. It avoids local installation of Python, Jupyter, and many common libraries.

It provides:

* A preconfigured Python runtime  
* Computational resources (CPU by default; optional GPU/TPU runtimes for heavier workloads)  
* Execution in **cells** for incremental runs and debugging  
* Sharing via URL (useful for collaboration and versioned submissions)  

### **Notebooks and iterative work**

Machine learning is iterative: inspect data, run an experiment, read metrics or errors, then adjust. Notebooks support **short experiments** and **visible outputs**, aligned with typical project workflows—**observe → modify → execute** cycles rather than a single opaque batch script.

Colab reduces local setup variance and yields a consistent runtime across machines.

---

## **Setup**

1. Open [https://colab.research.google.com](https://colab.research.google.com) in a browser.  
2. Authenticate with a Google account.  
3. Select **New Notebook**.

The default notebook name is often `Untitled.ipynb`. Renaming (e.g., `session25_ml_basics.ipynb`) is recommended for file organization.

---

## **Interface**

* A **cell** is a unit of code or prose.  
* **Code cells** execute Python; **Markdown cells** hold narrative, headings, and embedded media.  
* Cells run via the **Run (▶)** control or shortcuts such as **Shift+Enter**.  
* Output appears immediately below the executing cell.  

**Practice:** After substantive changes (data load, aggregate statistics, training step), re-run the cell and inspect output; discrepancies often surface at these boundaries.

---

## **First execution**

```python
print("Hello, Machine Learning")
```

Execution dispatches the statement to the interpreter and renders **stdout** below the cell.

**Convention:** Keep edit–run cycles tight—small logical changes, then verify output.

---

## **Illustrative variables**

Numeric attributes can be held in variables prior to tabular or model APIs:

```python
size_sqft = 1200
bedroom_count = 2
location_score = 3

print(size_sqft, bedroom_count, location_score)
```

This pattern maps physical or qualitative measurements to values the runtime can operate on.

---

# **2. Define the ML Workflow**

## **What is Machine Learning (ML)?**

Machine learning is the construction of systems that **improve with data**. Instead of encoding exhaustive rules (e.g., fixed price adjustments by square footage), the system is shown many labeled examples and **estimates** a mapping from inputs to outputs.

### **Core vocabulary (model, parameters, training)**

These terms appear in workflow diagrams and data-split figures. **Features** (inputs) and **labels** (targets) are defined again with examples in §4—here, *features* means measurable inputs and *label* means what you predict.

* **Model** — The procedure in code that maps **features** to a **prediction** (number, category, etc.). After training it behaves like a callable rule: features in, prediction out. *Parallel:* a **menu price lookup**—given order details, it returns a price; the lookup rule is the model.

* **Parameters** — Internal numbers (or equivalent) that training **adjusts using training data** so predictions align better with known labels. They are not typed in for each row; the **algorithm** estimates them from the training split. *Parallel:* the **exact spice levels** you lock in after calibrating a dish many times; the recipe template stays, the numbers are the parameters.

* **Hyperparameters** — Knobs fixed **before** each training run (e.g., how many layers, maximum tree depth, how long to train). They shape **how** learning runs rather than being the bulk numbers learned inside a run. *Parallel:* **how many** practice tests before exam day—you choose the count; that count is not “discovered” from one exam paper.

* **Training (fitting)** — Running the algorithm on the **training split** to set **parameters**.

* **Algorithm** — The coded update rule that searches for good **parameters** from examples. The **trained model** is the artifact you keep; the algorithm is the training machinery.

At a high level:

* A **task** is chosen (e.g., predict a numeric outcome).  
* **Data** supplies historical inputs and known outcomes.  
* A learning **algorithm** fits **parameters** so the **model** maps features to the label.  
* **Evaluation** quantifies behavior on data not used for fitting.

The program still runs defined algorithms; **parameters** and learned **structure** (e.g., which branches exist in a decision tree) come from data instead of hand-written rules for every case.

---

## **What is an ML Workflow?**

An ML workflow is an ordered set of stages for delivering a learning-based solution.

It promotes solutions that are:

* **Coherent** — each stage has an explicit purpose  
* **Reproducible** — configuration and data processing can be replayed  
* **Measurable** — performance is assessed on appropriate held-out data  

---

## **Core stages of the ML workflow**

Illustration (**regression** — sale price from structural and location attributes):

1. **Problem definition**  
   Specify the prediction target and the decisions it supports.  
   → Sample target: **sale price** from size, bedroom count, and location score.

2. **Data understanding**  
   Document provenance, field semantics, and data-quality issues (missing values, outliers).  
   → Includes attributes listed above and historical prices for supervised training.

3. **Data preparation**  
   Clean, join, turn categories into numbers the algorithm can use (**encoding**), rescale columns if needed (**scaling**), and shape a **feature matrix** (table of inputs) plus **label vector** (list or column of targets).  
   → **Imputation** = filling missing values (e.g., median area); encode location; drop or fix bad rows.

4. **Model building**  
   Select a model family, fit on **training** data, and select hyperparameters using **validation** data where applicable.

5. **Evaluation**  
   Report metrics on **held-out** data; compare to baselines and stakeholder thresholds.

Additional enterprise stages (experiment tracking, governance, deployment, monitoring) extend this core sequence.

![End-to-end ML workflow: problem definition through evaluation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-ml-workflow-stages.png)

---

## **Rationale for a defined workflow**

Without explicit stages:

* Objectives stay vague (“improve intelligence”) and success criteria disagree  
* Wrong targets or units propagate into training and deployment  
* Demonstration metrics diverge from production behavior  

A shared workflow yields common vocabulary: problem statement, features, label, split policy, metric, baseline.

---

## **Analogy (workflow mapping)**

| ML stage        | Cooking analogy                          |
| --------------- | ---------------------------------------- |
| Problem         | Dish and constraints (diet, occasion)   |
| Data            | Ingredients and quality                |
| Model / recipe  | Transformation steps                    |
| Evaluation      | Sensory and timing criteria vs. goal      |

Omitting definition or evaluation stages in either domain degrades outcomes.

---

# **3. Frame ML problems effectively**

## **Role of problem framing**

Ambiguous framing produces incorrect solutions even when implementation is sound. Distinct targets—e.g., **asking price** vs. **closed transaction price**— imply different labels; mixing them induces systematic error.

Effective framing specifies:

* **Output type** — scalar, class label, rank, etc.  
* **Consumption** — decision thresholds, asymmetric error cost  
* **Latency** — batch vs. **online inference** (**inference** = using the trained **model** on new rows to obtain predictions, without changing its **parameters**)  

---

## **Sample problem statement (regression)**

“Predict **sale price** from **floor area**, **bedroom count**, and **location score**.”

This statement fixes:

* Feature set  
* Label  
* Problem class (regression)  

---

## **Problem decomposition**

* **Inputs (features):** floor area, bedrooms, location score  
* **Output (label):** price  

---

## **Supervised problem classes**

1. **Regression**  
   Predicts a **continuous** quantity (price, load, temperature).  
   **Example:** dwelling sale price.

2. **Classification**  
   Predicts a **discrete** label (spam / not spam, defect classes).  
   **Example:** email spam detection.

3. **Other paradigms** (clustering, ranking, generative modeling) are out of scope here; supervised regression and classification cover a large share of introductory applications.

---

### **Sample tabular specification (classification)**

| Word count | Contains “free” | Sender reputation | Label (spam) |
| ---------- | --------------- | ------------------ | ------------ |
| 120        | Yes             | Low                | Spam         |
| 40         | No              | High               | Not spam     |
| 200        | Yes             | Medium             | Spam         |

* **Features:** word count, boolean subject term, reputation score  
* **Label:** spam vs. not spam  

The workflow stages are unchanged; only the label type and primary metrics differ (e.g., classification error vs. price error).

---

## **Problem metadata in code**

```python
problem = "Predict sale price"
features = ["size", "bedrooms", "location_rating"]
label = "price"

print(problem)
print(features)
print(label)
```

Declarative structure before data loading reduces ambiguity in downstream scripts.

---

# **4. Features and labels**

## **Definitions**

* **Features** — inputs available (or engineered) at inference time. They must not incorporate information unavailable when the prediction is required (see **leakage**).  
* **Label** — the quantity or class to predict. Known for training rows; unknown at inference for those rows.

One **row** corresponds to one observation; **columns** are features or the label.

---

## **Sample dataset (regression)**

| Size | Bedrooms | Location | Price |
| ---- | -------- | -------- | ----- |
| 1000 | 2        | 3        | 50    |
| 1500 | 3        | 4        | 75    |
| 2000 | 4        | 5        | 100   |

* **Features:** size, bedrooms, location  
* **Label:** price  

---

## **Input–output mapping**

The fitted function approximates:

**(Size, Bedrooms, Location) → Price**

The objective is **generalization**: acceptable error on units drawn from the same distribution but absent from the training file.

![Features as inputs and label as target (illustrative regression scenario)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-features-vs-labels.png)

---

## **Column-wise representation (Python lists)**

```python
sizes = [1000, 1500, 2000]
bedrooms = [2, 3, 4]
locations = [3, 4, 5]
prices = [50, 75, 100]
```

* **Model inputs:** the feature columns (or arrays built from them).  
* **Model output:** a predicted label—often a single number (regression) or a predicted class (classification); some models also output confidence scores.  

---

# **5. Data splitting**

## **Motivation**

Training and evaluating on the **same** rows:

* Encourages **memorization** of noise  
* **Inflates** reported metrics  
* **Understates** error on future data  

Held-out partitions approximate **out-of-sample** behavior (performance on examples the training procedure did not use, standing in for future data).

---

## **Partitions**

1. **Training** — Data used to update **model parameters** via the learning **algorithm**. Concretely, **weights** are numeric strengths attached to inputs (and similar internal terms); **tree splits** are if–then thresholds in tree-shaped models (“if size > 1500, go left…”). Those pieces are **learned from the training split only**.  
2. **Validation** — Data used to compare candidate setups—different **models** or **hyperparameters**—**without** using the test partition for those choices.  
3. **Test** — Final reporting after tuning; use should be minimal and one-directional (no feedback into tuning).

![Training, validation, and test split: roles of each partition](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-train-val-test-split.png)

### **Reading the split diagram**

Figures often label **model** or **parameters**. Here, **model** means the trained mapping from features to predictions; **parameters** means the values **learned during training** (weights, split points, etc.). **Hyperparameters** are **not** shown as a block of numbers inside the figure—they are choices you try while watching **validation** performance. **Training** updates parameters; **validation** helps you pick between hyperparameter settings and competing models; **test** is the last blind check.

---

## **Typical allocation**

Common splits include **70 / 15 / 15** or **80 / 10 / 10** (train / validation / test) for moderate datasets. Small-sample regimes may use **k-fold cross-validation** (reuse data in several train/validation rotations; saves detail for a later unit).

**Procedure:** Randomly **shuffle** rows before splitting when rows are **interchangeable**—no special order (sometimes written *i.i.d.*: each row is treated as an independent draw from the same kind). Retain **time order** when predicting the future from the past.

---

## **Analogy (assessment design)**

| Split       | Role                                      |
| ----------- | ----------------------------------------- |
| Training    | Core study material                       |
| Validation  | Formative checks; informs revision        |
| Test        | Summative measure; repeated peering invalidates it |

---

## **Manual holdout (illustrative)**

```python
sizes = [1000, 1200, 1500, 1800, 2000]
prices = [50, 60, 75, 90, 100]

train_sizes = sizes[:3]
test_sizes = sizes[3:]

train_prices = prices[:3]
test_prices = prices[3:]
```

Production pipelines add randomization, **stratification** for classification (split so each partition keeps roughly the same **class** mix—e.g., similar spam vs. ham ratio), and a validation block; this fragment only demonstrates **contiguous partition** of aligned arrays.

---

## **Data leakage**

**Leakage** occurs when training or tuning sees information that would be **unavailable at inference** or that **originates from the test partition**.

![Train/test boundary and forbidden information flow (data leakage)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-data-leakage.png)

Examples:

* Global statistics computed **including test rows**, applied **before** splitting during imputation  
* **Future** outcomes used as **inputs** for predicting an earlier state  
* **Duplicates** shared between train and test  

Effects:

* Overstated accuracy or underestimated error  
* Deployment failure when leaked channels vanish  

**Guideline:** Fit **preprocessors**—anything that learns from data before training (**scaling** fits mean/variance; **imputers** learn fill rules)—on **training** data only; apply the same fitted object to validation and test. Decisions that require test statistics belong **after** model selection or should be avoided.

---

# **6. Baselines**

## **Definition**

A **baseline** is a simple, interpretable predictor used as a **reference**:

> Before adding model complexity, what performance does a trivial rule achieve?

Common baselines:

* **Mean or median** label for all predictions (regression)  
* **Majority class** for every instance (classification)  
* **Persistence** (previous value) in some time-series settings  

![Baseline as reference before comparing to a trained model](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-baseline-reference.png)

---

## **Reference implementation (mean label)**

```python
prices = [50, 60, 75, 90, 100]

avg_price = sum(prices) / len(prices)
print(avg_price)
```

If every prediction equals `avg_price`, the resulting error quantifies difficulty **without** feature use.

---

## **Purpose**

* Establishes a **floor** for meaningful improvement  
* Discourages **complex models** that barely exceed trivial rules  
* Demonstrates whether **learning** from features adds measurable value  

---

## **Baseline vs. fitted model**

Illustrative interpretation (units depend on the chosen metric):

* Baseline behavior centered near **70**  
* Model near **72** — marginal gain; deployment cost may dominate  
* Model near **90** (on a comparable quality scale) — strong evidence of signal in features  

The **metric** must be fixed before comparing—e.g., **MAE** (*mean absolute error*: average size of prediction minus actual, ignoring sign). **Early and repeated baseline comparison** is standard practice.

---

## **Summary**

Prefer the simplest defensible baseline first. If a complex model fails to **materially** exceed the baseline on honest splits, inspect features, framing, and leakage before scaling model capacity.

---

# **Workflow checklist**

1. Configure environment (e.g., Colab).  
2. Specify problem, features, and label.  
3. Ingest and document data.  
4. Split into train / validation / test per policy.  
5. Define and compute baselines.  
6. Fit candidate models; compare to baselines on held-out data.  

Stages are sequential dependencies: later steps assume earlier artifacts.

---

# **Recommended practices**

* Define the problem and metric **before** implementation.  
* Maintain strict **input / output** separation; audit for leakage.  
* Avoid tuning against the **test** set; reserve it for final evaluation.  
* Establish **baselines** before elaborate architectures.  
* Use **incremental** notebook execution with explicit output review.  
