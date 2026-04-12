# Regression: Linear Regression Fundamentals

---

## Predicting Numbers, Not Labels: The Nature of Regression

Every meaningful question in data science ultimately falls into one of two camps. The first camp asks *which category* — is this email spam or not? Is this tumour benign or malignant? The second camp asks *how much* — what will this apartment rent for? How many units will we sell next quarter? What exam score will this student earn? Machine learning built a dedicated discipline to answer that second kind of question, and that discipline is called **regression**.

**Regression:**
- **Blueprint:** The supervised machine learning task of learning a function that maps input features to a **continuous real-valued output**, by minimising a mathematical measure of prediction error over a labelled training set.
- **Translation:** You show the computer hundreds of past situations where you already know the answer — "when the inputs looked like *this*, the real outcome was *this number*" — and the computer builds a formula that extends that pattern to new, unseen situations.
- **Anchor:** Think of a restaurant owner with two years of daily records. Revenue varied based on day of the week, weather, and nearby events. Regression is the process of using all those past records to derive a formula that turns tonight's weather forecast and the calendar into a specific predicted revenue — not "good night or bad night," but an actual rupee amount.

The most important distinction to lock in immediately is the difference between **classification** and **regression**. Classification produces a label from a fixed list — it assigns things to boxes. Regression produces a position on a continuous measuring tape — it estimates a specific numeric value. The moment your question ends with "how much?" or "how many?" rather than "which one?", you are in regression territory.

---

**Why does "regression" even have that name?**

The word has a fascinating historical origin that ties directly to the concept. In the 1880s, the British scientist **Francis Galton** studied the heights of parents and their children. He discovered that children of very tall parents tended to be tall — but slightly shorter than their parents, drifting back toward the population average. He called this phenomenon **"regression to the mean."** The mathematical technique he built to quantify this drift became the foundation of everything we now call regression analysis — one of the oldest and most battle-tested tools in all of data science.

---

**Common real-world examples of regression problems:**

- **House price prediction:** Given the area, location, age, and floor number of a property — predict its market price in rupees.
- **Student exam score prediction:** Given weekly study hours, attendance rate, and prior grades — predict the final exam score.
- **Delivery time estimation:** Given order size, distance, and time of day — predict how many minutes until delivery arrives.
- **Energy consumption forecasting:** Given outdoor temperature, number of occupants, and time of day — predict kilowatt-hours consumed.
- **Salary estimation:** Given years of experience, job role, and city — predict the monthly compensation.

In every example, the answer is not a box to tick — it is a specific number. That is the defining characteristic of a regression problem.

---

**The two core vocabulary terms you will use in every regression problem:**

- **Target variable** (also called: dependent variable, response variable, or simply "y"):
  - **Blueprint:** The single continuous numeric output the model is trained to predict — the "answer column" in your labelled dataset.
  - **Translation:** The number you are trying to guess — actual sale price of a house, actual delivery time, actual exam score.
  - **Anchor:** In a salary prediction system, the target variable is the rupee amount of the salary itself — the one column you're trying to forecast.

- **Feature** (also called: independent variable, predictor, or input):
  - **Blueprint:** Any measurable input variable available to the model at prediction time, used to form its estimate of the target.
  - **Translation:** The clues the model is allowed to use when guessing — the more relevant the clues, the better the guesses.
  - **Anchor:** In the salary system, features might be years of experience, job title level, city, and whether the person has a postgraduate degree.

**Pitfall:** A very common beginner mistake is treating a numerically coded category as a regression target. A dataset might represent customer tiers as the numbers 1, 2, and 3 — but "tier 2" is not twice "tier 1." Always verify that a numeric column represents a genuine measurement on a continuous scale before treating it as a regression target.

---

**What makes a variable "continuous"?**

- **Blueprint:** A variable is continuous if it can, in principle, take any value within a range, with no fixed list of allowed values.
- **Translation:** Think of temperature, revenue, time, weight, or pressure — the value could be 18°C, or 18.4°C, or 18.413°C. There is no natural list of permitted slots; the answer is a point on an infinite measuring tape.
- **Anchor:** Predicting *how hot* tomorrow will be in degrees is regression. Predicting whether tomorrow will be "hot," "mild," or "cold" is classification. The difference is a number vs. a label.

The engine that makes regression possible is **labelled training data**: past examples where every input situation already has its real-world numeric outcome attached. In machine learning notation, this is written as pairs $(x_i, y_i)$ — where $x_i$ is the full set of input features for example $i$, and $y_i$ is the known, verified, real-world answer. The model learns by seeing thousands of these pairs, adjusting its internal formula until its guesses for each $y_i$ are as close as possible to reality.

---

## The Straight-Line Formula: Understanding Linear Regression

Now that we know what regression is for, the next question is: *how does a model actually capture the relationship between features and target?* There are many possible shapes a predictive formula could take — curves, branching trees, layered neural networks. But we begin with the most elegant, interpretable, and instructive: the **straight line**. Linear regression is the bet that the relationship between inputs and output can be described, at least approximately, by a **weighted sum** — multiply each feature by its own personal multiplier, add all the products together, and you have a prediction.

**Linear regression:**
- **Blueprint:** A model of the form $\hat{y} = w_0 + w_1 x_1 + w_2 x_2 + \cdots + w_p x_p$, where $\hat{y}$ is the predicted output, $x_1$ through $x_p$ are the feature values, and $w_0$ through $w_p$ are the **coefficients** the model learns during training.
- **Translation:** Each feature gets its own personal multiplier. To make a prediction, multiply every feature by its multiplier and add all the results together — plus a fixed starting number. Training means finding the right multipliers automatically.
- **Anchor:** A salary estimator that says "Start from ₹3,00,000 as a base. Add ₹1,20,000 for every year of experience. Add ₹50,000 if the person has a postgraduate degree." The 1,20,000 and 50,000 are learned coefficients — the model's estimate of how much each factor contributes to salary on average.

---

**The best-fit line — visualising what linear regression is doing:**

When you have a single feature, the model is literally a straight line drawn through a scatter plot of your data. Imagine plotting 200 students — study hours on the horizontal axis, exam score on the vertical axis. The data forms a cloud of dots with an upward trend: students who study more tend to score higher. Linear regression finds the one specific straight line that passes through this cloud in the "best" possible position — the position that minimises the total gap between the line and all the dots simultaneously.

- **The slope of the line** is the coefficient $w_1$: it tells you how much the predicted score changes for every one extra hour of studying per week.
- **The intercept** is where the line crosses the vertical axis: the model's predicted score when study hours equals zero.
- **Every dot's vertical distance to the line** is a prediction error — the model was off by that much for that student. The best-fit line is the one that makes those distances as small as possible across all students at once.

**Mental Model — The Control Room:** Imagine a control room with one dial per feature. Each dial shows a current reading: "study hours: 7," "distance to school: 2 km," "prior GPA: 3.4." Next to each dial is a number written in pen — that is the coefficient. To make a prediction, you multiply each dial reading by its written number, add all the products, and add the intercept. Training is the process of figuring out what numbers to write in pen next to each dial, by finding the combination that minimises total prediction error across all training examples.

---

**The intercept $w_0$:**
- **Blueprint:** The constant term in the linear model — added to the weighted sum regardless of feature values. Formally, it represents the model's prediction when all features are zero.
- **Translation:** It is the model's permission to start at whatever baseline height best fits the data, before factoring in any features.
- **Anchor:** Without an intercept, a salary prediction line would be forced to pass through zero — implying someone with zero experience, zero education, and zero skills earns nothing. That may be technically true, but it forces an unrealistic constraint on the formula. The intercept gives the line room to sit at the right height.

---

**How the best-fit line is found: Ordinary Least Squares**

Every time the model makes a prediction, it may be slightly wrong. That error — the actual answer minus the predicted answer for one example — is called a **residual**. **Ordinary Least Squares (OLS)** is the algorithm that finds the specific set of coefficients making the **sum of all squared residuals** as small as possible across the entire training set.

**Ordinary Least Squares (OLS):**
- **Blueprint:** The fitting procedure that minimises the sum of squared prediction errors $\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ over all training examples to find the optimal weights.
- **Translation:** Think of it as finding the line position where the total "tension" between the data points and the line is minimised — with large errors penalised disproportionately more than small ones, because of the squaring.
- **Anchor:** Imagine rubber bands stretched vertically from each data point to your line. OLS finds the line placement that minimises the total squared tension across all those rubber bands simultaneously.

**Why squaring the errors?** Squaring serves two purposes simultaneously. First, it prevents positive errors (model undershot) and negative errors (model overshot) from cancelling each other out — a prediction wrong by +10 and one wrong by −10 both contribute positively to the total. Second, it punishes large errors far more than small ones, pushing the algorithm to especially avoid catastrophic misses.

**Pitfall:** Just because OLS always produces a result does not mean the result is meaningful. If the true relationship between features and target is strongly curved, the best straight line may look reasonable on paper while systematically misrepresenting the actual pattern. Always plot your feature against your target before committing to a linear model.

---

**The relationship between features and target — and what coefficients tell you:**

- **Coefficient:** The learned multiplier for one specific feature in a linear regression model — it tells you how much the predicted target changes per one-unit increase in that feature, *holding all other features constant*.
- **Positive coefficient:** Feature and target move in the same direction. More study hours → higher predicted score.
- **Negative coefficient:** Feature and target move in opposite directions. More distance from school → lower predicted attendance.
- **Coefficient near zero:** That feature has little predictive relationship with the target — it barely moves the needle.

**Pitfall:** Beginners often confuse **correlation** with a regression coefficient. Correlation measures the strength of a linear relationship symmetrically — X correlates with Y just as much as Y correlates with X. A regression coefficient is directional and in real-world units. More critically: neither correlation nor regression tells you about *causation*. Ice cream sales and sunscreen sales are strongly correlated — both spike in summer heat — but buying ice cream does not cause sunscreen purchases. Regression can quantify associations; only carefully designed experiments can establish cause.

---

## Teaching the Machine: How Model Training Works

We now know what linear regression looks like. But it is worth being precise about what "training" actually means mechanically. **Training** — also called **fitting** — is the computational process of estimating model parameters by minimising a **loss function** over the labelled training set. Before this was automated, analysts drew trend lines by hand and hard-coded formulas from intuition — a process that worked for small, slow-changing problems but becomes completely impractical with tens or hundreds of features.

**Loss function (also: cost function, objective function):**
- **Blueprint:** A single scalar value that summarises the total discrepancy between all of the model's predictions and all of the real target values in the training set. The training algorithm's sole explicit goal is to drive this number as low as possible.
- **Translation:** The loss function is the judge that scores every wrong prediction. The algorithm's entire job during training is to earn the lowest possible score from this judge.
- **Anchor:** Imagine a talent-show judge who awards a penalty for every off-note a singer hits. Slightly off notes earn small penalties. Wildly off notes earn disproportionately large ones. The singer (the model) tries to minimise total penalties — but only on the rehearsal rounds the judge witnessed, not on the actual live performance.

For linear regression, the standard loss function is **Mean Squared Error (MSE)**:
- **Blueprint:** $\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ — the average squared difference between true target values and model predictions across all training examples.
- **Translation:** Compute the error for each training example, square it, and take the average. The training algorithm searches for the weights that make this average as small as possible.
- **Anchor:** If your model predicts apartment rents and you compute the squared error for each apartment in the training set, then average them all — that single average number is MSE. Training is the process of finding the weights that push this average as low as it can go.

---

**What actually happens during training — step by step:**

- **Step 1 — Start with a guess:** The model begins with some initial set of weights — typically all zeros or small random numbers. These produce terrible predictions at first.
- **Step 2 — Measure how wrong it is:** The loss function (MSE) computes the total error across all training examples using the current weights.
- **Step 3 — Adjust the weights:** The algorithm figures out in which direction changing each weight would reduce the loss, and nudges each weight in that direction.
- **Step 4 — Repeat:** Steps 2 and 3 repeat many times, with the loss getting smaller and smaller each time, until the improvements become negligibly small and the algorithm stops.
- **Step 5 — Weights are locked:** Training is complete. The final weights are stored and used for all future predictions.

**Mental Model:** Think of training as a dial-tuning process. Imagine 50 dials — one per feature — and each dial's current position is a coefficient. You have a score board showing the current total error. You turn dial 1 slightly and check: did the error go down or up? You adjust accordingly. You do the same for every dial, over and over, until the score stops improving. That is the essence of how the learning algorithm finds the best coefficients.

---

**Generating predictions — using the trained model:**

Once training is complete and the weights are locked in, the model can make **predictions** on any new input — also called **inference**. Prediction is pure arithmetic: multiply each feature by its learned weight, sum everything up, add the intercept, and read off the result. The model does not re-access training data or re-run any algorithm. All of the knowledge from training is compressed entirely into those learned coefficients.

**Prediction (inference):**
- **Blueprint:** Applying the frozen, learned coefficients to a new input vector to produce an estimated target value. No learning happens at prediction time — only arithmetic.
- **Translation:** The training phase is "studying." The prediction phase is "taking the exam." All the work happened during studying; during the exam, you just apply what you learned.
- **Anchor:** A trained rent estimator is like a formula card: the real estate agent plugs in area, floor number, and location score, reads off the result. No internet, no files, no computation beyond multiplication and addition.

**Pitfall:** A model trained on apartment data from one city should not be used to predict rents in a very different city without retraining. The weights the model learned are specific to the patterns in the training data — they may not transfer to a completely different context.

---

## When More Becomes Less: Model Complexity and Overfitting

Every concept up to this point has been about making a model that fits training data well. But one of the most painful and important lessons in machine learning is that fitting training data well is not the same as being useful in the real world. In fact, *too much* fitting to the training data actively destroys real-world performance. This tension — between fitting what you have seen and performing on what you haven't — is the central challenge in all applied machine learning.

**Generalization:**
- **Blueprint:** A model's ability to produce accurate predictions on new, previously unseen data drawn from the same general distribution as the training set.
- **Translation:** Does the model understand the underlying patterns, or did it just memorise the specific training examples? A model that genuinely understands the patterns will work on new data; one that memorised will fail.
- **Anchor:** A chef who learned recipes understands timing, temperature, and technique — she performs in any kitchen. A chef who memorised exact dial positions for one specific oven is helpless in a different kitchen. Generalisation is the difference between understanding principles and memorising specifics.

---

**Overfitting — the central trap:**

**Overfitting:**
- **Blueprint:** The condition where a model's training error becomes very low because the model has learned to reproduce the training examples nearly perfectly — including their noise, coincidences, and measurement errors — at the cost of genuine pattern capture.
- **Translation:** The model followed the quirks of the specific training set so faithfully that those quirks don't repeat on new data. It learned the noise as if it were signal.
- **Anchor:** A student who memorises 200 past exam questions word-for-word — including misprints and unusual phrasings — does brilliantly on those exact questions. But when the real exam rephrases them slightly, the student is derailed. Another student who understood the underlying concepts handles any version of the exam. The first student overfit the practice set.

**When does overfitting happen in linear regression?**
- When you have **many features relative to few training examples** — the model has enough parameters to fit every training point nearly exactly, following noise instead of signal.
- When you add **polynomial terms** (squares, cubes, cross-products of features) to make the model more flexible — flexibility is powerful but must be controlled.
- When your training data is **particularly noisy** and the model has enough degrees of freedom to chase every random wiggle.

---

**Underfitting — the other extreme:**

**Underfitting:**
- **Blueprint:** The condition where the model is too simple to capture the patterns that genuinely exist in the data, producing high error on *both* the training data and on new unseen data.
- **Translation:** The model's assumptions are too blunt. It fails not just on unseen data, but even on the data it was trained on.
- **Anchor:** A student who barely studied fails both the practice problems and the real exam. High error everywhere — that is underfitting.

With linear regression, underfitting typically occurs when the true relationship is strongly nonlinear and the model is kept as a simple straight line, or when crucial features have been omitted from the dataset entirely.

---

**The Bias-Variance Tradeoff — the governing mental model:**

**Bias-variance tradeoff:**
- **Blueprint:** A model's expected prediction error can be understood as coming from two competing sources: **bias** (error from incorrect simplifying assumptions — the underfitting problem) and **variance** (error from being too sensitive to the specific training set — the overfitting problem).
- **Translation:** A model that is too simple is consistently wrong in the same direction — high bias. A model that is too complex changes its answers dramatically depending on which training examples it happened to see — high variance. The goal is a model that is approximately right *and* stable.
- **Anchor:** A compass that always points slightly north of true north has high bias — consistently wrong, but predictably so. A compass that spins erratically depending on which city it was calibrated in has high variance — unpredictable. A perfect compass is what training aims to produce.

**Mental Model — Photography Analogy:**
- A **blurry photograph** (high bias) has lost real detail — the image is smoother than reality.
- An **over-sharpened, digitally manipulated photograph** (high variance) has invented detail that wasn't in the original scene.
- A perfect, faithful photograph is what good modelling produces — the right amount of detail, neither blurred nor fabricated.

**The practical implication:** There is a sweet spot of model complexity where both bias and variance are acceptably small. Going below that sweet spot (too simple a model) increases bias. Going above it (too complex a model) increases variance. Understanding this tradeoff is what separates a practitioner who knows when to stop adding complexity from one who blindly adds more features until training error reaches zero.

---

## Reading the Errors: Residual Analysis

A trained model never predicts perfectly. Every prediction comes with some degree of error, and understanding those errors is just as important as making the predictions in the first place. To do this, we study **residuals**: the individual prediction errors for each training (or new) example. Residuals are the model's conscience — they show you exactly where and how the model is wrong, in a way that guides every improvement going forward.

**Residual:**
- **Blueprint:** For a single observation $i$, the residual is defined as $e_i = y_i - \hat{y}_i$ — the true target value minus the model's predicted value.
- **Translation:** How wrong was the model on this specific example, and in which direction? A positive residual means the model undershot (the real answer was higher). A negative residual means the model overshot (the real answer was lower). The size of the residual tells you how badly; the sign tells you which way.
- **Anchor:** A weather app predicts 28°C. Actual temperature is 31°C. Residual = +3°C — the model was too low by 3 degrees. Next day: predicts 25°C, actual is 23°C. Residual = −2°C — the model was too high by 2 degrees.

---

**Interpreting residuals — what they tell you conceptually:**

- **A residual of zero:** The model predicted this example perfectly. This is rare in practice.
- **A small positive residual:** The model slightly underestimated — the real value was a little higher than guessed.
- **A large positive residual:** The model significantly underestimated — the real value was much higher than guessed.
- **A small negative residual:** The model slightly overestimated — the real value was a little lower than guessed.
- **A large negative residual:** The model significantly overestimated — the real value was much lower than guessed.

The distribution of residuals across all your examples tells a story about the model's overall quality. If most residuals are small and scattered randomly around zero, the model is doing well — it makes roughly symmetrical small mistakes. If the residuals are large, or systematically skewed in one direction, the model is missing something important.

---

**The key question about residuals — patterns vs. randomness:**

The most important thing to ask about a set of residuals is not "how large are they?" but "do they have a **pattern**?" There are two fundamentally different situations:

- **Healthy model — random residuals:** Residuals are scattered randomly around zero across all predictions. The errors look like confetti tossed in the air — no trend, no curve, no clustering. This is the signature of a well-specified model: it has captured all available signal, and what remains is genuine, irreducible noise.

- **Problematic model — patterned residuals:** Residuals form a recognisable shape. Each specific pattern points to a specific structural problem:
  - **Residuals that are consistently positive in one range and consistently negative in another** → the true relationship may be curved, and the straight line is missing a bend.
  - **Residuals that grow larger as predictions grow larger** → the model is less reliable at higher values; something about the high-value range is systematically harder to predict.
  - **Residuals that shift suddenly at a certain feature value** → there may be an important variable the model is not using.

---

**The residual plot — the primary visual diagnostic:**

**Residual plot:**
- **Blueprint:** A scatter plot with predicted values on the horizontal axis and residuals on the vertical axis. Used to visually inspect whether prediction errors are random or patterned.
- **Translation:** Plot every prediction error against the corresponding prediction. If the cloud of points forms a flat, symmetric band around zero — the model is healthy. If the cloud forms any recognisable shape — the model has missed something structural.
- **Anchor:** A delivery time prediction app: random residuals mean it is sometimes early and sometimes late with no predictable pattern — the model is doing its job. Residuals that are consistently large on Friday evenings mean there is a modellable pattern (Friday traffic) that has been left on the table.

**Mental Model — Residuals as a Map:** Think of residuals as a map of everything the model has not yet explained. If residuals correlate with a feature you didn't include, including it will reduce those residuals. If residuals consistently curve upward at certain prediction ranges, the model's formula shape does not match the true relationship. Residual analysis is not a postmortem — it is an active, iterative engineering guide for improving the model.

---

**One important mathematical fact about residuals in OLS:**

When a linear regression model is trained using OLS, the **mean of the training-set residuals is always exactly zero**. This is a provable consequence of how OLS minimises squared error — the best-fit line always passes through the centroid (mean point) of the training data, ensuring that positive and negative training errors cancel out perfectly. This is a useful sanity check: if you compute the mean of all residuals on your training data and it is not close to zero, something has gone wrong in the fitting process.

---

## End-to-End Python Code: Fitting a Linear Regression Model and Analysing Residuals

The script below is complete in every respect — from the first import to the final printed line. There are no partial snippets and no gaps. Every single line carries a plain-English comment explaining precisely what it does and why it is there. Read the comments as a guided story; treat the code as the precise technical rendering of the same narrative.

```python
# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 0 — IMPORTS
# All tools (libraries) are loaded here at the very top, before any logic runs.
# This is standard Python convention: all imports belong at the start.
# ═══════════════════════════════════════════════════════════════════════════════

# numpy is the foundational library for fast numerical computing in Python.
# We use it to create arrays of numbers, do math on them, and generate
# the synthetic dataset we will train on.
import numpy as np

# LinearRegression is scikit-learn's implementation of ordinary least squares.
# When we call .fit() on it, it automatically solves for the best-fit weights
# using the OLS algorithm — no manual math required from us.
from sklearn.linear_model import LinearRegression


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — CREATE SYNTHETIC TRAINING DATA
# We manufacture a dataset rather than loading a file. This lets us define
# the "ground truth" relationship ourselves so we can verify that the model
# learns approximately the right answer after training.
# ═══════════════════════════════════════════════════════════════════════════════

# Create a reproducible random number generator by seeding it with 42.
# Any fixed seed works; the point is that everyone who runs this script
# gets identical data, making results reproducible across machines and reruns.
rng = np.random.default_rng(seed=42)

# Decide the total number of student observations to simulate.
n_samples = 200

# Generate 200 "study hours per week" values spread uniformly between 1 and 12.
# The result is a 2D array of shape (200, 1) — scikit-learn always expects
# the feature matrix to be two-dimensional (rows = examples, columns = features).
X = rng.uniform(low=1.0, high=12.0, size=(n_samples, 1))

# Define the true underlying formula we are simulating:
# test_score = 40 + 7.5 × study_hours
# These are the "ground truth" parameters we want the model to rediscover.
TRUE_INTERCEPT = 40.0   # Baseline score even with minimal study.
TRUE_SLOPE     = 7.5    # Each extra weekly study hour adds ~7.5 score points.

# Compute the noiseless (perfect) score for each student using the true formula.
# .ravel() converts the 2D (200, 1) array to a 1D (200,) array so the
# arithmetic works element-by-element without shape-mismatch errors.
y_clean = TRUE_INTERCEPT + TRUE_SLOPE * X.ravel()

# Add realistic noise to simulate real-world variation — exam-day nerves,
# topic luck, unmeasured factors. loc=0 centres the noise at zero (no bias).
# scale=10.0 means typical noise is about ±10 score points.
noise = rng.normal(loc=0.0, scale=10.0, size=n_samples)

# The observed score is the clean trend plus the random noise.
# This is what real-world data looks like: a true signal buried in noise.
y = y_clean + noise

# Print a summary of the dataset to confirm dimensions and value ranges.
print("=== Dataset Summary ===")
print(f"Feature matrix shape : {X.shape}")     # Expected: (200, 1)
print(f"Target vector shape  : {y.shape}")     # Expected: (200,)
print(f"Study hours range    : {X.min():.2f} – {X.max():.2f} hours/week")
print(f"Score range          : {y.min():.2f} – {y.max():.2f} points\n")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — INSTANTIATE AND TRAIN (FIT) THE MODEL
# At instantiation, the model object exists but knows nothing — no weights,
# no learned patterns. After .fit(), OLS has solved for the optimal weights
# that minimise total squared error across all 200 training examples.
# ═══════════════════════════════════════════════════════════════════════════════

# Create an empty LinearRegression model object. No learning has happened yet.
# Think of this as hiring a blank-slate analyst who has not yet seen any data.
model = LinearRegression()

# Train the model: scikit-learn reads X and y, runs the OLS fitting algorithm,
# and stores the result in model.intercept_ (the learned w₀) and model.coef_
# (the array of learned feature weights [w₁, w₂, ...]). This single line
# is where all the learning happens.
model.fit(X, y)

# Print the learned parameters alongside the true values we used to generate data.
# Because of noise in the training data, the learned values won't be identical
# to the true values, but they should be very close.
print("=== Learned vs. True Parameters ===")
print(f"True intercept  : {TRUE_INTERCEPT:.2f}  |  Learned intercept  : {model.intercept_:.4f}")
print(f"True slope      : {TRUE_SLOPE:.2f}  |  Learned slope      : {model.coef_[0]:.4f}\n")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — GENERATE PREDICTIONS
# The model's learned formula is now applied to the training inputs to produce
# a predicted score for every student. No learning happens here — this is pure
# arithmetic using the locked weights from Section 2.
# ═══════════════════════════════════════════════════════════════════════════════

# Produce predicted scores for all 200 students.
# model.predict() multiplies each student's study hours by the learned slope,
# adds the learned intercept, and returns the predicted score.
y_pred = model.predict(X)

# Print a few side-by-side comparisons: actual score vs. predicted score.
print("=== Sample Predictions (first 5 students) ===")
print(f"{'Study Hours':>12}  {'Actual Score':>13}  {'Predicted Score':>16}  {'Difference':>11}")
print("-" * 58)
for i in range(5):
    diff = y[i] - y_pred[i]
    sign = "+" if diff >= 0 else ""
    print(f"{X[i][0]:>12.2f}  {y[i]:>13.2f}  {y_pred[i]:>16.2f}  {sign}{diff:>10.2f}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — RESIDUAL ANALYSIS
# Residuals are the per-example prediction errors: actual minus predicted.
# Examining them reveals whether the model's mistakes are random (acceptable)
# or patterned (a sign that structural signal has been missed).
# ═══════════════════════════════════════════════════════════════════════════════

# Compute residuals: actual score minus predicted score for every student.
# A positive residual = model underpredicted (actual was higher than the guess).
# A negative residual = model overpredicted (actual was lower than the guess).
residuals = y - y_pred

# ── Basic residual statistics ─────────────────────────────────────────────────

# Mean residual: should be exactly (or very close to) zero for OLS.
# This is a mathematical guarantee of OLS — the best-fit line always passes
# through the centroid of the training data.
mean_resid = np.mean(residuals)

# Standard deviation of residuals: the typical spread of individual errors.
# This reflects how noisy the data is — how much real-world variation exists
# beyond what study hours alone can explain.
std_resid = np.std(residuals)

# Count how many residuals are positive vs. negative.
# Roughly equal counts confirm the model is not systematically biased.
n_positive = np.sum(residuals > 0)   # Model underestimated for these students.
n_negative = np.sum(residuals < 0)   # Model overestimated for these students.

print("=== Residual Analysis ===")
print(f"Mean residual (should be ≈ 0) : {mean_resid:.6f}")
print(f"Std dev of residuals          : {std_resid:.3f} score points")
print(f"Positive residuals (underest) : {n_positive} students")
print(f"Negative residuals (overest)  : {n_negative} students\n")

# Print a few individual residuals to build intuition for what they mean.
print("=== Sample Residuals (first 5 students) ===")
print(f"{'Student':>8}  {'Actual':>8}  {'Predicted':>10}  {'Residual':>10}  {'Interpretation':>25}")
print("-" * 68)
for i in range(5):
    r = residuals[i]
    if r > 0:
        interp = "model underestimated"
    elif r < 0:
        interp = "model overestimated"
    else:
        interp = "perfect prediction"
    print(f"{i+1:>8}  {y[i]:>8.2f}  {y_pred[i]:>10.2f}  {r:>+10.2f}  {interp:>25}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — SINGLE NEW PREDICTION (INFERENCE / DEPLOYMENT MODE)
# Shows the model in its real-world operational mode: given one new student's
# study hours, produce one predicted score. No training data, no algorithm —
# just the learned formula applied to a single new input.
# ═══════════════════════════════════════════════════════════════════════════════

# Define a new student who studies 7.0 hours per week.
# The double brackets create the required 2D array shape (1 row, 1 column)
# that scikit-learn's predict() method expects.
new_student = np.array([[7.0]])

# Apply the trained model to produce a predicted score.
# model.predict() returns an array; [0] extracts the single scalar value.
predicted = model.predict(new_student)[0]

# Compute what the true formula would give as a teaching benchmark.
# In a real project, we would never have this — it is a teaching comparison only.
true_expected = TRUE_INTERCEPT + TRUE_SLOPE * 7.0

print("=== Single New Prediction ===")
print(f"New student study hours : 7.0 hours/week")
print(f"Model prediction        : {predicted:.2f} score points")
print(f"True formula gives      : {true_expected:.2f} score points")
print(f"Residual (if known)     : {true_expected - predicted:+.2f} score points")
print()
print("The small discrepancy reflects noise absorbed during training — not a model flaw.")
```

---

### Logic Walkthrough: The Journey of Data Through the Script

**Constructing a known world.** The script begins by manufacturing its own dataset rather than loading a file. This is a deliberate teaching strategy: by designing a dataset where the true formula is known — score = 40 + 7.5 × hours + noise — we can verify after training whether the algorithm rediscovered approximately the right answer. In any real project, the truth is permanently hidden. The `rng.normal` call adds Gaussian noise to simulate the realistic fact that two students who study the same number of hours may score differently due to many unmeasured factors.

**Training as a single learning act.** `model.fit(X, y)` is the one line where all learning happens. Internally, scikit-learn forms the feature matrix, appends a column of ones to handle the intercept, and runs the OLS fitting algorithm. The result is stored in `model.intercept_` (the learned baseline, which should be near 40) and `model.coef_[0]` (the learned slope, which should be near 7.5). Comparing learned to true values confirms the algorithm is working — they won't be identical due to noise, but the discrepancy should be small.

**Prediction as frozen arithmetic.** `model.predict()` is not an act of learning — it is multiplication and addition applied to locked-in weights. For each student, scikit-learn multiplies the study-hour value by the learned slope, adds the learned intercept, and returns the result. The model no longer needs the training data — all of the learned knowledge is compressed into those two numbers.

**Residuals as the model's per-example error report.** Computing `y - y_pred` produces 200 individual numbers — one per student — representing exactly how wrong the model was for each. A mean near zero confirms OLS's mathematical guarantee is working correctly. The breakdown into positive and negative counts tells us whether the model is symmetrically wrong (good) or systematically biased in one direction (a concern). Reading individual residuals builds intuition: the sign tells you the direction of the error, the magnitude tells you the severity.

**Single-prediction as the deployment use case.** The final block strips away all training infrastructure and shows what the model does in production: receive one new set of feature values, return one predicted number. No training data, no network, no computation beyond arithmetic. The knowledge from training lives entirely in `model.intercept_` and `model.coef_` — two stored numbers that define the entire learned formula.

---

## Closing Synthesis

This session built a complete, foundational understanding of regression from the ground up. We began with the core question: what kind of problem calls for regression? Any question that demands a specific number rather than a category label — and where that number can be learned from labelled historical examples. We then established **linear regression**: the weighted-sum model where each feature gets its own learned multiplier, and the best set of multipliers is found by **Ordinary Least Squares** — the algorithm that minimises total squared prediction error across all training examples. We traced the **training lifecycle**: the loss function measures how wrong the model is, the fitting algorithm adjusts weights to reduce that measurement, and the result is a locked-in formula that generates **predictions** for any new input through pure arithmetic. We confronted the central tension in all modelling — **overfitting vs. generalisation** — and built the vocabulary to reason about it: bias, variance, and the sweet spot of complexity that avoids both extremes. And we closed by studying **residuals**: the individual prediction errors that, when examined for patterns, reveal precisely what the model has captured and what it has not yet explained.

**Three questions to always ask after building a regression model:**
- Do the learned coefficients make intuitive sense — do the signs and magnitudes match domain knowledge?
- Are the residuals scattered randomly around zero, or do they form a pattern pointing to something the model missed?
- Is the model fitting noise (overfitting) or genuinely capturing the underlying relationship?

These three questions form the foundation of honest, rigorous regression modelling.

---

## Framework and Library Cheat Sheet

| Term / Tool | Formal Definition | Plain-Language Role in This Session |
|---|---|---|
| **Regression** | Supervised ML task: learn $f: \mathbf{x} \to y$ where $y$ is a continuous scalar | Answers "how much / how many?" — predicts a number, not a category |
| **Target variable (y)** | The continuous real-valued output to be predicted | The "answer column" — the specific number the model is trying to forecast |
| **Feature (x)** | An input variable / predictor available at prediction time | The clues given to the model when forming its estimate |
| **Continuous variable** | A numeric quantity that can take any value in a range | Anything measured on a scale: temperature, revenue, time, exam score |
| **Labelled training data** | Input–output pairs $(x_i, y_i)$ where $y_i$ is the known real-world answer | Past examples with answers attached — what the model learns from |
| **Linear regression** | Model $\hat{y} = w_0 + w_1 x_1 + \ldots + w_p x_p$; fit by minimising sum of squared residuals | The simplest interpretable regression model — a learned weighted sum |
| **Intercept / bias term $w_0$** | Constant term added regardless of feature values | The model's baseline prediction before any feature information is used |
| **Coefficients / weights** | Learned multipliers per feature; quantify each feature's marginal relationship to the target | How much the prediction shifts per one-unit increase in each input |
| **Ordinary Least Squares (OLS)** | Minimises $\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ — the sum of squared prediction errors | The standard algorithm for fitting a linear regression model |
| **Loss function / MSE** | $\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ — average squared prediction error | The single number the training algorithm minimises during fitting |
| **Training / fitting** | Estimating model weights to minimise loss on labelled training data | Teaching the model from past examples with known answers |
| **Prediction / inference** | Applying frozen learned weights to new inputs — no learning, pure arithmetic | Using the finished model in practice to generate estimates |
| **Generalisation** | Model performance on unseen data from the same distribution | The real-world usefulness criterion — fitting training data is not enough |
| **Overfitting** | Low training error because the model learned noise as if it were signal | Complexity trap: too many parameters chasing too few genuine patterns |
| **Underfitting** | High error on training data — model too simple to capture real patterns | Capacity trap: the model's assumptions are too blunt for the data |
| **Bias** | Error from incorrect simplifying assumptions — the underfitting source | The model is consistently wrong in the same direction |
| **Variance** | Error from oversensitivity to the specific training set — the overfitting source | The model's answers change dramatically with small training set changes |
| **Residual** | $e_i = y_i - \hat{y}_i$ per example; positive = underpred., negative = overpred. | Per-example error; raw material of all model diagnostics |
| **Residual plot** | Scatter of residuals vs. predicted values or a feature | Primary visual diagnostic — reveals systematic patterns the model missed |
| **`numpy`** | Numerical Python library; fast array operations and mathematical functions | Synthetic data generation, residual arithmetic, numeric summaries |
| **`numpy.random.default_rng`** | Constructs a reproducible random number generator from a fixed seed | Ensures identical data every time the script is run |
| **`sklearn.linear_model.LinearRegression`** | OLS linear regression estimator; stores learned weights in `.intercept_` and `.coef_` | Fits the model and exposes the `predict()` interface for inference |

---

*End of Lecture Notes — Session 28: Regression / Linear Regression Fundamentals*
