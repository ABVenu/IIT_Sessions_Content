#### Preread: The ML Workflow & Habits

## Why a notebook (Colab) shows up first

**Google Colab** is a browser environment where you work in **cells**: some cells run logic, others hold explanations and headings. You run a cell, read what appeared underneath, change something small, run again. That **observe → modify → execute** rhythm is how most ML work actually happens—not one long script you run once blindly.

Colab also reduces “it worked on my machine” friction: everyone gets a similar Python setup, and you can share a link. For heavier tasks, you can request stronger hardware from the menu; for this course track, the emphasis is on **habits** and **workflow**, not on tuning massive models.

**Practice habit:** after any meaningful change (loading data, summarizing it, training), re-run and **look at the output**—many bugs first appear as numbers or messages that “almost” look right.

---

## ML in plain terms

**Machine learning** here means: you **do not** hand-write a separate rule for every situation. You collect **historical examples**: each row has **what was known** at the time and **what turned out to be true** (the outcome you care about). A **learning procedure** adjusts internal numbers so that, for new rows where you only know the inputs, the system can **propose** a reasonable outcome.

The outcome might be:

- a **number** (price, load, temperature) → often called **regression**;
- a **category** (spam vs not spam, defect type) → often called **classification**.

The same **stage-by-stage workflow** applies to both; what changes is the type of answer and how you measure error.

---

## Core vocabulary (you’ll see these in diagrams)

These words are worth recognizing early; we’ll reuse them in figures and checklists.

- **Model** — the trained “if you give me these inputs, I give you a prediction” procedure. Think of it like a **price lookup** shaped by examples: same kind of question every time, but the rule was **fit** from data, not typed line by line for every house.

- **Parameters** — the internal quantities the learning step **updates from training data** so predictions line up better with known outcomes (examples: strengths attached to inputs, split thresholds in tree-like models). You don’t set these by hand for each row; the algorithm **estimates** them from the **training** split.

- **Hyperparameters** — choices you fix **before** a training run: how complex the model is allowed to be, how long to train, and similar **knobs**. They shape _how_ learning runs; they are **not** the bulk of numbers learned inside that single run. Parallel: **how many** practice tests you schedule—the schedule is your choice; it isn’t “discovered” from the final exam paper.

- **Training (fitting)** — running the learning procedure on the **training** data to set **parameters**.

- **Algorithm** — the coded update rule that searches for good **parameters**. After training, what you **keep** is the **trained model**; the algorithm is the machinery used to produce it.

At a high level: pick a **task** → gather **data** (inputs + known outcomes) → run an **algorithm** on the training portion to set **parameters** → **evaluate** on data that was **not** used to tweak those parameters unfairly.

---

## The ML workflow (ordered stages)

An **ML workflow** is a deliberate order of steps so the project stays **coherent** (each step has a job), **reproducible** (someone else could replay your choices), and **measurable** (you know what “good” means on held-out data).

![End-to-end ML workflow: problem definition through evaluation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-ml-workflow-stages.png)

Using the session’s running example (**predict sale price** from size, bedrooms, and a location score):

1. **Problem definition** — Name the prediction target and the decision it supports. Vague goals (“be smarter”) breed vague success.

2. **Data understanding** — Where did fields come from? What do they mean? Where are values missing or suspicious?

3. **Data preparation** — Clean joins, handle missing values sensibly, turn categories into numeric forms the learner can use, rescale when needed, and assemble a clear **table of inputs** plus a **column (or vector) of targets**. This stage is where many real projects spend a large share of time.

4. **Model building** — Choose a model family, **train** on the training split, and use **validation** data to compare setups (different models or hyperparameters) where applicable.

5. **Evaluation** — Report metrics on **held-out** data; compare to **baselines** and any agreed thresholds from stakeholders.

Larger organizations add tracking, governance, deployment, and monitoring on top of this **core** path—but the core sequence is still the spine.

**Why insist on stages?** Without them, teams argue past each other (“we improved intelligence”) while **measuring the wrong thing**, **training on the wrong target**, or **showing metrics that won’t match production**.

---

## Cooking analogy (same pattern, different domain)

| ML stage       | Cooking angle                                    |
| -------------- | ------------------------------------------------ |
| Problem        | Which dish, for whom, with what constraints      |
| Data           | Ingredients and their quality                    |
| Model / recipe | The transformation from inputs to plated outcome |
| Evaluation     | Taste, timing, and presentation vs the goal      |

Skipping “what are we making?” or “how will we judge it?” hurts both kitchens and ML projects.

---

## Framing the problem (small wording, big consequences)

**Problem framing** is specifying, without ambiguity: what is the **output type**, how the prediction will be **consumed** (thresholds, costs of different mistakes), and **when** it must be ready (batch vs near real time).

A classic pitfall: mixing targets that **sound** similar but aren’t—for example **asking price** vs **final closed price**. They are different labels; blending them creates systematic wrong answers even if the code is perfect.

**Supervised** setups (the focus of this session) always have, for training rows, both **inputs** and **known outcomes**. Two patterns cover many beginner applications:

- **Regression** — continuous quantity (house price, temperature).
- **Classification** — discrete label (spam or not, fault category).

A tiny **classification** table (same ideas as the notes): rows might have word count, whether the subject line contains a promotional word, sender reputation, and a **spam / not spam** label. Same workflow stages; the metric shifts from “how far off is the number?” to “how often is the wrong label picked?”

**Inference** (a term you’ll hear) means **using** the trained model on new inputs to get predictions **without** changing its learned parameters on those rows.

---

## Features and labels (what goes in vs what you predict)

- **Features** — Everything you are allowed to know **at prediction time** for that case, assembled as inputs. They must not smuggle in information you wouldn’t truly have when the prediction is needed (that tie to **leakage** below).

- **Label** — The quantity or category you want to predict. Known for training rows; unknown for the future rows you care about.

One **row** is one observation; **columns** are features and possibly the label.

![Features as inputs and label as target (illustrative regression scenario)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-features-vs-labels.png)

For the house example, the model tries to approximate: **(size, bedrooms, location) → price**. The north star is **generalization**: acceptable error on new units drawn from the **same kind of reality** as the training data, not perfect replay of training rows only.

---

## Splitting data: train, validation, test

If you train and **grade** on the **same** rows, metrics are **inflated**—the system can memorize noise—and future performance is **understated** in your reports. So the data is split into **partitions** with different jobs.

![Training, validation, and test split: roles of each partition](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module2/session25/session25-train-val-test-split.png)

**How to read the diagram:** **Training** updates **parameters** (learned weights, split points, etc.). **Validation** helps choose between **hyperparameters** and competing models **without** peeking at the final test set for those decisions. **Test** is the **last** gate: minimal use, one direction—no tuning directly to test scores.

**Typical shares** you’ll hear: something like **70 / 15 / 15** or **80 / 10 / 10** for train / validation / test when the dataset is moderate. When data is scarce, **k-fold cross-validation** (rotating which chunk is temporarily “validation”) is common—we’ll touch the idea in session.

**Order matters:** if rows are **exchangeable** (no special sequence), **shuffle before splitting**. If the task is **forecasting the future from the past**, preserve **time order** so you don’t train on tomorrow to predict yesterday.

**Assessment analogy:** training ≈ core study material; validation ≈ formative quizzes that **guide** what you revise; test ≈ a summative exam you **don’t** cram to and reuse as daily practice—repeated peering invalidates it as a fair final measure.

---

## Data leakage (the silent metric booster)

**Leakage** means training or tuning saw information that **would not be available** at real prediction time, or that **bled in** from the test side. Examples:

- Computing fill-in rules or scaling statistics **using the full dataset including test rows**, then applying them everywhere.
- Using **future** outcomes as **inputs** for an earlier timestamp.
- **Duplicate** rows appearing in both train and test so the model “saw the exam.”

Effects: accuracy looks stellar until deployment, then reality bites. **Habit:** fit anything that “learns from the data” before training—filling missing values, scaling, many encoders—on **training data only**, then **apply** the same fitted transform to validation and test. Don’t make model-selection decisions using **test** statistics.

---

## Baselines (prove the fancy part is worth it)

A **baseline** is a simple, understandable predictor used as a **reference line**: “Before we add complexity, what does a trivial strategy achieve?”

Common ones: for regression, predict the **mean or median** label every time; for classification, always predict the **most common class** (and other simple rules exist for time series).

**Why bother?** It sets a **floor** for meaningful improvement, discourages huge models that barely beat tie-one-hand-behind-your-back rules, and shows whether the **features** actually carry signal. In session you’ll see metrics such as **mean absolute error** (average size of mistake, ignoring direction)—the key is to **fix the metric** and **split policy**, then compare fairly.

If a rich model only **marginally** beats a baseline on honest held-out data, the next debugging pass is framing, features, and leakage—not only “bigger model.”

---

## Mini checklist (what “done” looks like before the fun stuff)

1. Environment you can run (e.g., Colab) with a clear notebook name.
2. Written **problem**, **feature list**, and **label**—no ambiguity.
3. Data ingested and **documented** (sources, gaps, weird cases).
4. **Train / validation / test** split policy chosen and applied with **no leakage**.
5. **Baseline** computed.
6. Candidate models compared to that baseline on **held-out** evaluation—not on the training set alone.

Later stages assume earlier ones; skipping a stage tends to **compound** confusion downstream.

---
