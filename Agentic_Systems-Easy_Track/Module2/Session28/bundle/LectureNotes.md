# Regression: Linear Regression Fundamentals

**Lecture title:** Regression — Linear Regression Fundamentals  
**Target audience:** Absolute beginners (zero coding or technical background)  
**Session duration:** 2 Hours 15 Minutes  
**Objective:** Understand how machine learning models predict continuous numeric values

---

## Executive Overview

Every day, decisions hang on a single number: *How much will this house sell for? What will tomorrow's demand be? How many units should we stock?* These are not questions about categories or labels — they are questions about **quantities**. Machine learning has a dedicated branch for exactly this kind of question, and it is called **regression**.

In this session, we will build up a complete mental picture of how regression works — starting from the simplest possible version and progressing through the ideas that actually make it useful in real-world applications. We begin by establishing *why* regression exists and what kind of problems it solves. We then zoom into **linear regression**, arguably the most important and interpretable model in all of machine learning — not because it is the most powerful, but because understanding it deeply unlocks almost every other concept you will ever encounter.

From there, we walk through the process of **training a model**: how does a machine actually *learn* from examples? We confront the most important tension in applied machine learning — the tug-of-war between a model that memorises too well (overfitting) versus one that generalises to the real world. Finally, we study **residuals**: the humble prediction errors that, when read carefully, contain more information than the predictions themselves.

By the time this session ends, you will be able to explain all of these ideas to someone who has never heard of machine learning — using plain language, clear analogies, and one complete, fully annotated Python script as evidence that these concepts live in actual code.

---

## Module 1 — Regression Basics: Predicting Continuous Values

### Context Bridge

Before we touch any algorithm, we need to be precise about the *type* of question we are answering. Machine learning broadly divides prediction tasks into two families: **classification** (predict which bucket or label something belongs to) and **regression** (predict a number on a scale). Most beginners encounter classification first — "Is this email spam or not?" — but in business and science, the more common and more financially significant question is not "which one?" but **"how much?"** That is the world regression lives in.

---

### The "Why" Factor

Why does regression exist as a distinct discipline? Because human beings have always needed to forecast measurable outcomes. Ancient farmers predicted crop yield from rainfall. Early economists tried to relate wages to productivity. Engineers in the 20th century built predictive formulas for material stress. Statisticians formalised all of this into **regression analysis**, and machine learning inherited, generalised, and automated the process.

The real-world cases are everywhere:
- A bank estimates your **credit risk score** (a number from 300 to 850) based on your history.
- A logistics company predicts **delivery time** in hours based on distance, traffic, and weather.
- A doctor's tool estimates a patient's **blood pressure** given age, BMI, and activity level.
- A retail chain forecasts next week's **sales volume** based on seasonality and promotions.

In each case, the answer is not a label — it is a **measurement on a continuous scale**. Regression is the framework that produces those measurements.

---

### Core Ideas (Trinity Rule)

---

**Regression (supervised learning for continuous outputs)**

- **Blueprint (real definition):** In supervised machine learning, **regression** is the task of learning a function that maps a set of input features to a **continuous real-valued output**, typically by minimising a loss function (a mathematical measure of how wrong predictions are) on a labelled training set.
- **Translation (plain English):** You show the computer hundreds or thousands of past examples — "when these inputs looked like *this*, the real-world answer was *this number*" — and the computer finds a formula that reproduces those answers reasonably well and can extend that formula to new inputs it has never seen.
- **Anchor (real-life story):** Imagine a restaurant owner who has tracked daily revenue for two years along with factors like day of the week, whether it rained, and whether a local festival was happening. Regression is the process of finding a formula that turns today's weather forecast and calendar data into a *predicted revenue figure* for tonight — not a category like "good day" or "bad day," but a specific dollar amount.

---

**The target variable (what we are predicting)**

- **Blueprint:** In regression, the **target variable** (also called the dependent variable or response variable) is the continuous numeric outcome that the model is trained to estimate. It is the "answer column" in the training data.
- **Translation:** The single number you wish you could see into the future to know. Everything else in the dataset is a clue; the target is the answer you need.
- **Anchor:** In a house price prediction task, the target is the **sale price** — that one column that says what the house actually sold for. The model's job is to learn to predict that column from all the other columns.

---

**Features (the inputs / clues)**

- **Blueprint:** **Features** (also called independent variables, predictors, or input variables) are the measurable quantities or attributes used as inputs to the model. In structured tabular data, they are typically the columns of the dataset excluding the target.
- **Translation:** Features are the clues the model is allowed to use when making a prediction. The more relevant, accurate, and well-chosen the clues, the better the prediction.
- **Anchor:** When predicting a student's final exam score, features might be: hours studied per week, attendance percentage, assignment completion rate, and previous exam scores. The model learns how to weigh each clue in arriving at its forecast.

---

**Continuous value (what makes regression different from classification)**

- **Blueprint:** A **continuous variable** is a numeric quantity that can take any value within a range — it is not restricted to a finite set of named categories. Unlike discrete variables (number of children: 0, 1, 2, 3…) or categorical labels (colour: red/blue/green), a continuous variable like temperature or price can in principle take infinitely many values.
- **Translation:** The difference between answering "which one?" (like sorting mail into labelled bins) and "how much or how many?" (like reading a thermometer). Regression answers the thermometer question.
- **Anchor:** Predicting the temperature tomorrow is regression — the answer could be 18.4°C or 22.7°C or 31.1°C, not just "hot" or "cold." Predicting whether tomorrow will be "hot," "mild," or "cold" is classification.

---

**Labelled training data (the foundation of supervised learning)**

- **Blueprint:** In supervised learning, **labelled training data** consists of input–output pairs \((x_i, y_i)\) where \(x_i\) is a feature vector and \(y_i\) is the known target value. The model learns by adjusting its parameters to reduce the discrepancy between \(y_i\) and its own predictions.
- **Translation:** "Labelled" means each past example comes with the answer attached. We know what the house sold for. We know what the patient's blood pressure was. We use these known answers to teach the model, then take away the answer sheet for new examples.
- **Anchor:** Think of a teacher marking practice exams — the student (model) sees both the questions (features) and the correct answers (labels) during training. During a real exam (inference on new data), only the questions are provided.

---

### Mental Models

**The number line vs. the labelled boxes**
Imagine two games. In the first, you are given an object and must place it in one of four labelled boxes: "apple," "banana," "grape," "mango." That is classification. In the second game, you are handed an object and must say exactly where it falls on a long measuring tape — any reading from 0 to 1000 cm is valid. That is regression. Both use clues (features), but the output is fundamentally different: a box vs. a position on a scale.

**Examples as anchors to a hidden rule**
Each labelled training example is a data point in a space. The model's job is not to memorise those points but to infer the **underlying rule** they are instances of. Think of connect-the-dots, except the dots are noisy and the "picture" is a smooth function that passes *near* most of them without touching every one exactly.

---

### Pro-Tips & Pitfalls

- **Pitfall — treating coded categories as continuous:** A dataset might encode customer tier as 1, 2, or 3. These are integers but they encode *categories*, not measurements. Running regression on them as if "tier 2 is twice tier 1" will produce misleading coefficients. Always inspect whether a numeric column is truly continuous.
- **Pitfall — forgetting the unit of measurement:** If your target is revenue in millions and you report RMSE of 2.3, that means ±2.3 million per prediction — a very different story from ±2.3 rupees. Always carry units through your analysis.
- **Pro-tip — write the problem statement in one sentence first:** Before building any model, finish this sentence: "We want to predict _____ (target) using _____ (features), measured in _____ (unit), from data that covers _____ (domain/time range)." If you cannot fill in all blanks clearly, the model will not be useful no matter how technically correct.

---

## Module 2 — Linear Regression: Intuition of the Best-Fit Line

### Context Bridge

We now know what regression is for and what it is trying to produce. The next question is: *how* does a model actually encode the relationship between features and target? There are many possible model shapes — curves, trees, neural networks — but we begin with the simplest and most revealing: the **straight line**. Linear regression assumes that the relationship between features and the target can be captured, at least approximately, by a **weighted sum**. This is a strong assumption, and it will not always hold, but it produces a model that is transparent, inspectable, and mathematically well-understood — an ideal starting point.

---

### The "Why" Factor

Linear regression has been in use since the early 19th century — Francis Galton used it to study inheritance in the 1880s, which is where the word "regression" comes from (he noted that children of very tall parents tended to "regress" toward the average height). It endures not because it is the most powerful model but because it is the most **legible** one. When a linear model says "for every additional year of experience, salary increases by approximately ₹1.2 lakh," that is a direct, auditable, and explainable statement. Stakeholders in business, medicine, economics, and policy trust models they can read and challenge — and linear regression delivers that trust through its simplicity.

---

### Core Ideas (Trinity Rule)

---

**Linear regression (the model)**

- **Blueprint:** **Linear regression** models the relationship between a set of features \(x_1, x_2, \ldots, x_p\) and a continuous target \(y\) as a **linear function**: \(\hat{y} = w_0 + w_1 x_1 + w_2 x_2 + \ldots + w_p x_p\). The parameters \(w_0\) (intercept) and \(w_1, \ldots, w_p\) (coefficients or weights) are estimated from training data by minimising a loss function, classically the **sum of squared residuals**.
- **Translation:** Each feature gets its own multiplier (a coefficient), and the prediction is simply: start from a fixed baseline, then add each feature's value multiplied by its weight. The learning algorithm's job is to find the set of multipliers that makes predictions as close as possible to the real answers in the training data.
- **Anchor:** A simple salary estimator: "Base salary = ₹3,00,000 + (₹1,20,000 × years of experience) + (₹50,000 × whether you hold a postgraduate degree)." The numbers 1,20,000 and 50,000 are the coefficients — the model's estimate of how much each factor "contributes" to salary on average.

---

**The intercept (w₀ / bias term)**

- **Blueprint:** The **intercept** (also called the bias term) is the constant added to the weighted sum regardless of feature values. It represents the model's predicted output when all features equal zero.
- **Translation:** The "starting point" before any clues are factored in. Think of it as the baseline prediction in the absence of any information.
- **Anchor:** In a rent prediction model, the intercept might be ₹8,000 — the model's estimate of rent when square footage is zero and all other features are at their zero values. In practice, "zero square footage" is nonsensical, so the intercept is more of a mathematical anchor than a real-world quantity; what matters is how the coefficients shift the prediction around it.

---

**Ordinary least squares (OLS) — how the best-fit line is found**

- **Blueprint:** **Ordinary least squares** is the most common method for fitting a linear regression model. It finds the parameters \(w_0, w_1, \ldots, w_p\) that minimise the **sum of squared residuals** (SSR): the sum of the squared differences between each true target value and the model's prediction for the same input.
- **Translation:** Imagine stretching rubber bands vertically from each data point to the line. OLS finds the line position that makes the total *squared* stretch as small as possible. Squaring means that large deviations hurt much more than small ones — the algorithm is especially motivated to avoid extreme misses.
- **Anchor:** You have 20 data points plotting "hours of sleep" vs. "cognitive test score." OLS finds the one straight line through that scatter plot for which, if you measured the vertical gap at every point and squared each gap, the total would be lower than for any other line. There is a provably unique answer, and with standard linear algebra it can be computed in a single step — no trial and error required.

---

**Coefficients / weights (what the model learns)**

- **Blueprint:** After fitting, the **coefficients** (or weights) \(w_1, \ldots, w_p\) quantify the **marginal relationship** between each feature and the target, holding all other features constant. A positive coefficient means "more of this feature is associated with a higher target value"; a negative coefficient means the opposite.
- **Translation:** Each coefficient is the model's best estimate of "how much does the target change, on average, when this one input goes up by one unit and everything else stays the same?"
- **Anchor:** In a model predicting daily website traffic: if the coefficient for "ad spend (₹)" is 12.5, the model says "every additional rupee of ad spend is associated with about 12.5 more visitors per day, all else equal." A manager can read that number directly and decide whether the return justifies the spend.

---

**The equation of a line (single-feature case)**

- **Blueprint:** With one feature \(x\), the linear regression model is \(\hat{y} = w_1 x + w_0\), where \(w_1\) is the **slope** (rate of change of \(\hat{y}\) per unit of \(x\)) and \(w_0\) is the **intercept** (value of \(\hat{y}\) when \(x = 0\)).
- **Translation:** Two numbers describe the entire straight line: the slope says "how steeply does the line climb (or fall)?" and the intercept says "where does the line cross the vertical axis?"
- **Anchor:** Temperature conversion is a perfect linear relationship: \(\text{Celsius} = 1.8 \times \text{Fahrenheit} - 32\). Slope = 1.8 (every 1°F increase means 1.8°C more), intercept = −32.

---

**Correlation vs. regression (an important distinction)**

- **Blueprint:** **Correlation** (specifically Pearson correlation) measures the *strength and direction* of a linear association between two variables — it is a single number between −1 and +1. **Regression** produces a *predictive equation* and quantifies how much the target changes per unit of input. Correlation is symmetric (X correlates with Y as much as Y correlates with X); regression is directional (predicting Y from X is different from predicting X from Y).
- **Translation:** Correlation says "these two things tend to move together." Regression says "given this input, here is my best estimate of the output." Knowing that A and B are correlated does not tell you how to predict one from the other in practical units — regression gives you the actual formula.
- **Anchor:** Ice cream sales and sunscreen sales are highly correlated (both spike in summer). But correlation does not mean ice cream causes sunscreen purchase. Regression into causation requires domain knowledge, not just numbers.

---

### Mental Models

**The rubber band on a straightedge**
Place a straightedge (ruler) on a scatter plot. Now imagine tiny rubber bands stretched vertically from each data point to the ruler. OLS finds the ruler position that minimises the total *squared* tension across all bands. This is why it is called "least squares" — you are minimising squares of vertical distances.

**The dial board**
Imagine a control room with one dial per feature. Each dial has a label ("square footage," "number of bedrooms," "distance to metro") and a value. Beside each dial is a multiplier written in pen — that multiplier is the coefficient. You multiply each dial reading by its coefficient, sum everything up, and add the intercept. The total is the prediction. Training is the process of *figuring out what to write in pen next to each dial* so the outputs match reality as closely as possible.

**Extending to multiple features**
With two features, the "line" becomes a flat plane tilted in 3D space. With three features, it is a flat surface in 4D. With 50 features, you cannot visualise it — but the math works exactly the same way: it is always a **weighted sum**, always minimising squared error, always producing a single coefficient per feature. The geometry gets hard to imagine, but the recipe stays the same.

---

### Pro-Tips & Pitfalls

- **Pitfall — assuming linearity without checking:** Linear regression will produce a result on *any* data, even if the true relationship is strongly curved. A model of "years of experience vs. salary" that ignores the levelling-off at very high seniority will underestimate senior salaries and overestimate mid-level ones. Always plot feature vs. target before choosing a model.
- **Pitfall — confusing correlation with prediction accuracy:** Two variables can be strongly correlated (r ≈ 0.9) yet the regression model may have large absolute errors if the target's range is small relative to noise. Always inspect both \(R^2\) and absolute error metrics.
- **Pro-tip — feature scaling matters for some extensions:** Vanilla OLS does not require feature scaling (it finds the same line regardless of units). But if you later add regularisation (Ridge, Lasso) or compare coefficient sizes, always scale features to comparable ranges first.

---

## Module 3 — Model Training: Fitting Regression Models and Generating Predictions

### Context Bridge

We have established *what* a linear regression model looks like — a weighted sum with an intercept and one coefficient per feature. But we have been speaking loosely about "finding" those coefficients. It is time to make this precise. **Training** is the mechanical, repeatable process by which a model moves from "I have no idea what the weights should be" to "I have found the best weights for this dataset." And **prediction** is what happens once those weights are locked in.

---

### The "Why" Factor

Before automated training algorithms existed, analysts would eyeball scatter plots, draw trend lines by hand, and hard-code formulas based on intuition and domain expertise. This worked for small, slow-changing problems, but it does not scale. Modern datasets have tens or hundreds of features; no human can manually tune hundreds of coefficients. Training algorithms replaced this manual process with a principled, reproducible, objective procedure: minimise the loss on the training data, and the weights follow automatically.

---

### Core Ideas (Trinity Rule)

---

**Training (fitting the model)**

- **Blueprint:** **Training** (or fitting) a supervised learning model is the computational process of estimating model parameters by minimising a **loss function** over the labelled training set. For linear regression, this is typically achieved in closed form via the **normal equations** or iteratively via **gradient descent**; the result is the set of coefficients that minimise total squared prediction error on training examples.
- **Translation:** Training is the computer solving a very large arithmetic problem: "What combination of weights, when plugged into the formula, makes the predictions as close as possible to the real answers I already know?" It is done automatically in milliseconds on most modern computers.
- **Anchor:** Calibrating a postal weighing scale using 20 packages of known weight. You adjust the scale until its reading best matches all known weights simultaneously. That process of adjustment-to-minimise-error is training.

---

**The loss function (what training minimises)**

- **Blueprint:** A **loss function** (also called a cost function or objective function) quantifies the discrepancy between the model's predictions and the true labels. In linear regression, the standard loss is **Mean Squared Error (MSE)**: the average of the squared differences between true and predicted values across all training examples. \[\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2\]
- **Translation:** A single number that summarises "how wrong the model is, overall." The training algorithm's only goal is to push this number as low as possible. Big mistakes are penalised more than small ones because of the squaring.
- **Anchor:** Imagine a talent show judge who awards a penalty for every off-note a singer hits. Slightly off notes get a small penalty; wildly off notes get a disproportionately large one (because errors are squared). The singer (model) tries to minimise total penalties (minimise loss) across the whole performance.

---

**The normal equations (exact solution for OLS)**

- **Blueprint:** For linear regression, the optimal weights \(\mathbf{w}\) have an **exact, closed-form solution**: \(\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}\), where \(\mathbf{X}\) is the matrix of training features and \(\mathbf{y}\) is the vector of true targets. This means the solution is computed in one algebraic step — no iterative search required.
- **Translation:** Unlike some other models that learn through thousands of small adjustments, ordinary least squares can find the *perfect* answer (given the data and the linear assumption) in a single mathematical operation. It is one of the few cases in machine learning where "we are done in one shot" is literally true.
- **Anchor:** Solving a system of balance-scale puzzles. If you have enough puzzles and each one shows a different configuration of weights, you can write out the equations and solve for the unknown weights all at once — no trial and error.

---

**Gradient descent (the iterative alternative — important for later models)**

- **Blueprint:** **Gradient descent** is an iterative optimisation algorithm that starts with random weights and repeatedly updates them in the direction that reduces the loss most steeply (the negative gradient of the loss with respect to the weights) by a small step called the **learning rate**, until convergence.
- **Translation:** Imagine standing on a hilly landscape in thick fog. You cannot see the whole landscape, so you feel the ground under your feet and take a small step downhill. You repeat this — always stepping in whichever direction is steepest downward — until you reach a valley. The valley is the lowest loss; the steps are weight updates.
- **Anchor:** For linear regression, gradient descent and the normal equations reach the same answer. But gradient descent becomes essential for neural networks and large models where direct algebraic solution is computationally impractical.

---

**Prediction / inference**

- **Blueprint:** After training, **prediction** is the application of the learned function \(f(x) = w_0 + w_1 x_1 + \ldots + w_p x_p\) to new input feature vectors \(x_{\text{new}}\) to produce output estimates \(\hat{y}_{\text{new}}\). The model parameters are fixed; no learning occurs during prediction.
- **Translation:** Once the dials are locked in with the right multipliers, you can feed in any new situation's features and instantly get a predicted number out. The machine does not need to look up past examples or re-learn anything — the knowledge is encoded in the coefficients.
- **Anchor:** A trained rent estimator is like a printed formula card given to a real estate agent. For any apartment, the agent plugs in area, location score, and floor number, and reads off the model's estimated rent — no internet connection, no database lookup, just the formula.

---

**Train–test split (how we measure generalisation)**

- **Blueprint:** A **train–test split** partitions the labelled dataset into a **training set** (used to fit model parameters) and a **test set** (withheld entirely during training, used only to evaluate the trained model on unseen examples). Common splits are 80%/20% or 70%/30%.
- **Translation:** We intentionally hide some of the answer sheet during study, then test the model on those hidden answers to see how well it actually learned the pattern vs. memorised the examples.
- **Anchor:** A school divides a question bank of 100 past exam problems into 80 for practice and 20 that students never see. The teacher uses performance on the unseen 20 to judge whether students understood the concepts, not just repeated the 80 practice answers.

---

**Evaluation metrics for regression**

- **Blueprint:** **RMSE (Root Mean Squared Error)** is \(\sqrt{\text{MSE}}\); it reports error in the same units as the target, giving a "typical size of mistake." **MAE (Mean Absolute Error)** is the average absolute difference; it is less sensitive to large outliers. **\(R^2\) (coefficient of determination)** measures what fraction of target variance is explained by the model; 1 is perfect, 0 means the model is no better than predicting the mean, negative means it is worse.
- **Translation:** RMSE answers "how far off, on average, in real units?" MAE answers the same with a simpler formula but is gentler on outliers. \(R^2\) answers "what fraction of the variation in the answer is captured by the model?"
- **Anchor:** If you are predicting apartment rents and RMSE = ₹4,500, that means your typical prediction is about ₹4,500 away from the actual rent — enough to matter. If \(R^2\) = 0.82, the model explains 82% of why different apartments command different rents.

---

### Mental Models

**Compression, not memorisation**
A linear regression model with 10 features stores exactly 11 numbers (10 weights + 1 intercept). It was trained on perhaps 10,000 rows. Training "compressed" 10,000 data rows into 11 numbers that summarise the pattern. Prediction is then just an arithmetic operation on those 11 numbers. This is fundamentally different from a lookup table — the model does not store the data, it stores a *formula*.

**The study-and-exam loop**
Training = the study phase. The model sees the examples with answers attached and adjusts its formula. Testing = the exam phase. New examples arrive without answers; the model applies its formula and receives a grade (RMSE, \(R^2\), etc.). A good student (model) scores well on both. A bad student memorises only specific questions and fails on new ones.

---

### Pro-Tips & Pitfalls

- **Pitfall — evaluating on training data only:** Reporting RMSE or \(R^2\) only on the training set is like marking your own homework. It always looks better than deserved. Always evaluate on a held-out test set.
- **Pitfall — target leakage:** If a feature in your dataset is derived from the target (e.g., "total bill including tip" as a feature when predicting "tip"), the model sees the answer hidden in its inputs. This produces unrealistically low training error and collapses in deployment.
- **Pro-tip — scale matters when communicating RMSE:** Always state RMSE alongside the target's average and range. RMSE of ₹4,500 on rent predictions is impressive if the average rent is ₹50,000 (9% error) but terrible if the average rent is ₹6,000 (75% error).

---

## Module 4 — Model Complexity: Understanding Overfitting and Generalization

### Context Bridge

Training minimises error on examples the model has already seen. But the entire *point* of building a model is to use it on data it has *not* seen — future customers, new properties, tomorrow's traffic. The jump from "works on training data" to "works in the real world" is not automatic. This gap is where **overfitting** and **generalization** live, and navigating it is arguably the central skill of applied machine learning.

---

### The "Why" Factor

Early machine learning practitioners celebrated any model that reduced training error. But they repeatedly discovered a painful pattern: models that performed brilliantly during development would underperform badly once deployed. The training data, no matter how large, is a finite sample from a larger (or evolving) reality. Any model complex enough to fit the training sample *exactly* will also fit its **noise** — the random fluctuations, measurement errors, and one-off coincidences that happen to appear in that particular dataset but do not represent the true underlying relationship. The field gradually developed a vocabulary — overfitting, variance, regularisation, cross-validation — to diagnose and fix this problem. Understanding it at a conceptual level is the single most important thing a beginner can take from a machine learning course.

---

### Core Ideas (Trinity Rule)

---

**Generalization (the real goal)**

- **Blueprint:** **Generalization** is a trained model's ability to produce accurate predictions on **unseen data** drawn from the same distribution as the training data. It is measured on a held-out test set and is the primary criterion for real-world usefulness.
- **Translation:** Does the lesson the model learned from past examples actually apply when new, previously unseen examples arrive? Training performance is a practice score; generalization is the real-world grade.
- **Anchor:** A chef who learns recipes from one restaurant's kitchen should be able to cook well in a different kitchen with a slightly different oven. If the chef only memorised exact oven settings and cannot adapt, they will not generalise. A chef who understood the *principles* (timing, temperature, technique) will.

---

**Overfitting (too much complexity, chasing noise)**

- **Blueprint:** **Overfitting** occurs when a model learns spurious patterns in the training data — including noise and coincidences — resulting in very low training error but significantly higher error on unseen data. The model has too many degrees of freedom relative to the signal in the data.
- **Translation:** The model studied only the specific practice problems, memorised the quirks of those problems, and gets tripped up when a slightly different version appears on the real exam. It learned noise as if it were signal.
- **Anchor:** A student memorises 200 past exam questions word for word — including the misprints, accidental hints, and unusual phrasings. When the real exam uses different wording, the student struggles. Another student who understood the *concepts* does better despite having "seen" less.

**What does overfitting look like in practice?**
The telltale sign is a significant gap between training error and test error. Training RMSE = 2.1, test RMSE = 8.7? The model has overfitted. It has fitted the noise in its training examples so well that those patterns do not repeat on new data.

In the context of linear regression specifically, overfitting becomes more likely when:
- You have **many features** relative to the number of training examples.
- You add **polynomial features** (squares, cubes, cross-products) to increase flexibility.
- Your data is **noisy** and the model has enough parameters to follow every wiggle.

---

**Underfitting (too little complexity, missing real patterns)**

- **Blueprint:** **Underfitting** occurs when the model is too simple to capture the underlying relationship in the data, resulting in high error on *both* training and test sets. The model's capacity is insufficient to represent the true patterns.
- **Translation:** The model is trying to describe a complex situation with rules that are too blunt to capture what is actually happening. Both its study performance and its real exam performance are poor.
- **Anchor:** Predicting quarterly revenue using only the current month's weekday count — ignoring seasonality, promotions, competition, and economic conditions. The model is so underpowered that it fails even on training data.

---

**The bias–variance tradeoff (the governing tension)**

- **Blueprint:** In learning theory, the expected prediction error of a model can be decomposed into three components: **bias** (error from overly simplistic assumptions), **variance** (error from sensitivity to fluctuations in the training set), and irreducible noise. High-bias models underfit; high-variance models overfit. Reducing one typically increases the other — this is the **bias–variance tradeoff**.
- **Translation:** Simple models make consistent but wrong guesses (high bias, low variance — like a compass that always points north instead of toward true north). Complex models make different guesses each time you change the training data slightly (low bias, high variance — like a compass that spins randomly). The goal is a model in the sweet spot: consistent *and* approximately correct.
- **Anchor:** Blurry photograph vs. noisy, over-sharpened photograph. The blurry one (high bias) has clearly lost information. The over-sharpened one (high variance) has invented details that are not in the scene. A perfect photo (low bias + low variance) is what training aims to produce.

---

**Cross-validation (a robust way to measure generalization)**

- **Blueprint:** **K-fold cross-validation** splits the training data into K equal parts (folds), trains the model K times (each time using K−1 folds as training and the remaining fold as validation), and averages the K validation scores. This gives a more reliable estimate of generalization performance than a single train/test split.
- **Translation:** Instead of using one batch of 20% of data as the "test," you rotate through all the data systematically, so every example gets to be in the "test" batch exactly once. The average score is a better estimate of how the model will do in practice.
- **Anchor:** Instead of asking one person to review a job application, a company uses a panel of five reviewers and averages their scores. Any single reviewer's quirks or biases average out; the panel's score is more reliable.

---

### Mental Models

**The two-curve diagram**
Imagine drawing two curves on a graph where the x-axis is "model complexity" and the y-axis is "prediction error." The training-error curve goes down monotonically as complexity increases — more complex models always fit training data better. The test-error curve starts high (underfitting), falls as complexity increases to a sweet spot, then rises again (overfitting). The sweet spot — where test error is lowest — is the model complexity to target. Linear regression sits on the left part of this diagram; its simplicity is also its protection against overfitting in most practical scenarios.

**The student analogy revisited**
- Student A (underfitting): did not study at all. Fails everything.
- Student B (just right): studied principles and practised varied examples. Passes reliably on new questions.
- Student C (overfitting): memorised 1,000 specific answers word for word. Does perfectly on practice sets, but fails when questions are phrased differently.

You are trying to train Student B.

**Occam's razor as engineering philosophy**
In the absence of strong evidence for a complex model, start with the simplest possible model that captures the signal. For tabular data with a continuous target, that almost always means linear regression first. Add complexity only when you have clear evidence — from held-out data — that the simpler model is leaving substantial predictive power on the table.

---

### Pro-Tips & Pitfalls

- **Pitfall — the training-accuracy trap:** Optimising a model until its training RMSE is impressively low is not an achievement — it can always be achieved by adding enough complexity. The metric that matters is **test error**, measured on data the model never saw.
- **Pitfall — test set contamination:** If you repeatedly look at test set results to guide model design decisions (which features to add, which hyperparameters to choose), you are implicitly fitting the model to the test set. Save the test set for one final, honest evaluation.
- **Pro-tip — visualise both error curves:** When experimenting with model variants, keep a log of both training and test error. If test error starts diverging upward from training error as you add features or complexity, you have entered overfitting territory. Stop and regularise.

---

## Module 5 — Residuals: Interpreting Prediction Errors Conceptually

### Context Bridge

Our model is now trained and evaluated. But a single number — RMSE, \(R^2\) — tells an incomplete story. The model is not equally wrong across all inputs; it may systematically underpredict in one range and overpredict in another. It may be precise for small values but wildly inaccurate for large ones. To understand *where and how* the model fails, we examine **residuals**: the individual prediction errors for each example in the dataset. Residuals are the model's conscience — they reveal everything the aggregate metrics politely conceal.

---

### The "Why" Factor

Before residual analysis became standard, analysts would simply report their model's overall error and move on. This led to deployed systems that were embarrassingly wrong for specific subpopulations, specific value ranges, or specific conditions — while looking acceptable on average. A model that overpredicts expensive houses and underpredicts cheap ones has RMSE of, say, ₹5,000. But a model that is randomly ±₹5,000 across all price ranges has the same RMSE — and is far more trustworthy. Residual plots expose the difference.

---

### Core Ideas (Trinity Rule)

---

**Residual (the per-observation prediction error)**

- **Blueprint:** For observation \(i\), the **residual** is \(e_i = y_i - \hat{y}_i\) — the difference between the true target value and the model's predicted value. A positive residual means the model underpredicted; a negative residual means it overpredicted.
- **Translation:** For each example, the residual answers "by how much, and in which direction, was the model wrong?" It is the individual-level error underneath the aggregate RMSE statistic.
- **Anchor:** A weather service predicts 28°C; the actual temperature is 31°C. Residual = 31 − 28 = +3°C. The model was too low by 3 degrees. If the next day's prediction is 25°C and actual is 23°C, residual = 23 − 25 = −2°C. The model was too high by 2 degrees.

---

**Random vs. systematic residuals (the diagnostic lens)**

- **Blueprint:** **Random residuals** show no discernible pattern when plotted against predicted values or against any feature — they look like a horizontal band of noise centred around zero. **Systematic residuals** form curves, wedges, trends, or clusters indicating that the model is making a *predictable kind of mistake*, which means unmodelled structure remains.
- **Translation:** If your residuals look like scattered confetti around zero, the linear model has captured all available structure and the remaining errors are genuine noise. If your residuals form a U-shape or a tilted band or clusters, there is a pattern the model missed — more features, a transformation, or a more complex model could help.
- **Anchor:** A delivery tracking app predicts arrival time. Random residuals: sometimes 5 minutes early, sometimes 7 minutes late, no pattern. Systematic residuals: the app consistently underestimates by 20 minutes on Friday evenings (traffic not modelled). The pattern is an engineering signal.

---

**Residual plots (the primary diagnostic tool)**

- **Blueprint:** A **residual plot** graphs residuals on the y-axis against either predicted values or a specific feature on the x-axis. In a well-specified linear model, residuals should be **homoscedastic** (constant spread) and **centred around zero** across the full range of the x-axis.
- **Translation:** Plot the errors. If the error cloud drifts, fans out, curves, or clusters, the model needs work. A flat, symmetric band around zero is the target.
- **Anchor:** Plotting "predicted rent vs. residual" for an apartment model: if cheap apartments have residuals scattered near zero but expensive apartments have residuals ranging from −₹30,000 to +₹50,000, the fan-shaped cloud says the model is unreliable at high rent values.

---

**Heteroscedasticity (non-constant error variance)**

- **Blueprint:** **Heteroscedasticity** refers to the condition in which the variance of the residuals is not constant across the range of predicted values or features. It violates one of the classical assumptions of OLS linear regression and can lead to unreliable confidence intervals and significance tests.
- **Translation:** The model's mistakes are bigger in some regions than others. It might be quite reliable for mid-range predictions but wildly uncertain for extreme values.
- **Anchor:** A food delivery app estimating order time is reliable for small orders (±5 minutes) but wildly inconsistent for very large catering orders (±45 minutes). The error variance grows with order size — classic heteroscedasticity.

**What to do about it?**
- Transform the target variable (e.g., take the log of price, which compresses the upper range).
- Add features that explain the higher-error region.
- Use models that explicitly account for changing variance (generalised least squares, or robust regression).

---

**Outlier residuals (the extreme errors)**

- **Blueprint:** An **outlier** in regression is an observation whose residual is substantially larger (in absolute value) than typical residuals. Outliers may indicate measurement error, data entry mistakes, unusual real-world events, or genuine extreme cases that the model's assumptions do not cover.
- **Translation:** The cases where the model was very badly wrong. Some deserve investigation; others deserve a note in the model card; very few should be silently discarded.
- **Anchor:** A salary prediction model is trained on job postings but one data point represents a founder who earned ₹50 crore in a single year via an IPO. No linear model based on job-level features will predict that — the residual will be enormous, but it is a legitimate data point, not a mistake. Understanding whether large residuals are errors vs. genuine extremes requires domain knowledge.

---

### Mental Models

**The error compass for each data point**
For every single prediction, draw an arrow from the prediction to the true value. The arrow's length is the residual magnitude; its direction (up = underpredict, down = overpredict) is the sign. If you look at all the arrows together and they point randomly in all directions with similar lengths, the model is well-calibrated. If all arrows point the same way in some region of the feature space, the model has a blind spot there.

**The cloud around the line**
When you have one feature, you can draw the fitted line and show actual data points around it. The vertical gap from each point to the line is its residual. A healthy residual picture: data points scattered symmetrically and roughly evenly above and below the line along the full length of the line. Unhealthy: the points are close to the line in the middle but far away at the ends (nonlinearity), or increasingly spread out as you move to the right (heteroscedasticity).

**Residuals as the model's "to-do list"**
Whatever pattern remains in the residuals is a map of what the model has not yet explained. If residuals correlate with a feature you did not include, including it will reduce those residuals. If residuals show a U-shape against the fitted values, adding a quadratic term may flatten it. Analysing residuals is not a postmortem — it is a guide for the next iteration of model improvement.

---

### Pro-Tips & Pitfalls

- **Pitfall — reporting only aggregate metrics:** RMSE of ₹4,200 sounds good — but if the model has residuals of −₹40,000 on properties above ₹1 crore, it will embarrass the team in production for that market segment. Always inspect residuals by subgroup or feature range, not just overall.
- **Pitfall — removing outlier residuals without investigation:** Large residuals may be data entry errors (fix or remove) or genuine extreme cases the model cannot handle (document as a known limitation). Silently removing them to improve metrics is misleading.
- **Pro-tip — the mean of OLS residuals is always zero on training data:** This is a mathematical guarantee of OLS: the sum of residuals on training data is always zero. If you compute the mean of test residuals and it is far from zero, the model has a **systematic bias** on the test set — often a sign of distribution shift or target leakage to investigate.

---

## End-to-End Example: Training and Evaluating a Linear Regression Model in Python

The script below is complete — from the very first import line to the very last printed diagnostic. There are no partial snippets. Every single line has a plain-English comment explaining what it does, so you can read the comments as a story and treat the code as the precise technical version of the same story.

```python
# ──────────────────────────────────────────────────────────────────────────────
# SETUP: Import every tool we will need before writing any logic.
# ──────────────────────────────────────────────────────────────────────────────

# Import numpy: a Python library for fast, efficient math on arrays of numbers.
# We use it to generate synthetic data and to compute the mean of residuals.
import numpy as np

# Import train_test_split: a utility that randomly divides a dataset into a
# training portion (used to fit the model) and a test portion (used to evaluate it).
from sklearn.model_selection import train_test_split

# Import LinearRegression: sklearn's implementation of ordinary least squares
# linear regression. It will find the best-fit weights automatically.
from sklearn.linear_model import LinearRegression

# Import mean_squared_error and r2_score: standard functions for measuring
# how accurate a regression model is on a given set of predictions.
from sklearn.metrics import mean_squared_error, r2_score

# ──────────────────────────────────────────────────────────────────────────────
# STEP 1: CREATE SYNTHETIC DATA
# We simulate a dataset instead of loading a real one so that we know the
# "ground truth" and can confirm the model learns approximately the right answer.
# ──────────────────────────────────────────────────────────────────────────────

# Create a reproducible random number generator seeded at 42.
# Using a fixed seed means anyone who runs this script gets identical data.
rng = np.random.default_rng(seed=42)

# Decide how many data rows (students) to simulate.
n_samples = 150

# Generate 150 random "study hours per week" values between 1 and 10.
# The result is a 2D array with shape (150, 1) — required by sklearn.
X_raw = rng.uniform(low=1.0, high=10.0, size=(n_samples, 1))

# Define the "true" relationship we are simulating:
# test_score = 45 + 8 × study_hours (the formula we want the model to discover).
TRUE_INTERCEPT = 45.0   # The baseline score even with minimal study.
TRUE_SLOPE = 8.0        # Each extra hour of study adds about 8 points on average.

# Calculate the "perfect" (noiseless) score for each student using the true formula.
# X_raw.ravel() converts the 2D array into a 1D array for easy arithmetic.
scores_noiseless = TRUE_INTERCEPT + TRUE_SLOPE * X_raw.ravel()

# Add realistic noise: not every student achieves exactly their predicted score —
# exam-day nerves, topic luck, and external factors create random variation.
# loc=0 means the noise is centred at zero (no systematic bias in the noise itself).
# scale=9.0 means typical noise is about ±9 score points.
noise = rng.normal(loc=0.0, scale=9.0, size=n_samples)

# The observed score = noiseless trend + random noise.
y = scores_noiseless + noise

# ──────────────────────────────────────────────────────────────────────────────
# STEP 2: SPLIT DATA INTO TRAINING AND TEST SETS
# ──────────────────────────────────────────────────────────────────────────────

# Split: 80% of rows become training data, 20% become the held-out test set.
# random_state=42 ensures the same split every time this script is run.
X_train, X_test, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.20, random_state=42
)

# Print how many rows landed in each set so we can confirm the split.
print(f"Training examples: {len(X_train)}")   # Should be ~120.
print(f"Test examples    : {len(X_test)}")     # Should be ~30.

# ──────────────────────────────────────────────────────────────────────────────
# STEP 3: CREATE AND TRAIN THE LINEAR REGRESSION MODEL
# ──────────────────────────────────────────────────────────────────────────────

# Create a LinearRegression object. At this point it has no learned weights —
# it is just an empty model ready to be fitted to data.
model = LinearRegression()

# Fit the model to the training data.
# sklearn internally solves the normal equations and stores:
#   model.intercept_  → the learned baseline (w₀)
#   model.coef_       → the learned slope(s) (w₁, w₂, ...)
model.fit(X_train, y_train)

# Print the learned parameters and compare to the true values we defined above.
print("\n── Learned vs. True Parameters ──────────────────────────────────")
print(f"True intercept : {TRUE_INTERCEPT:.1f}   |  Learned intercept : {model.intercept_:.3f}")
print(f"True slope     : {TRUE_SLOPE:.1f}   |  Learned slope     : {model.coef_[0]:.3f}")
# Because of noise, learned values will be close but not identical to true values.

# ──────────────────────────────────────────────────────────────────────────────
# STEP 4: GENERATE PREDICTIONS
# ──────────────────────────────────────────────────────────────────────────────

# Apply the learned formula to the TRAINING inputs to get in-sample predictions.
# These predictions are compared to y_train to compute training error.
y_train_pred = model.predict(X_train)

# Apply the learned formula to the TEST inputs to get out-of-sample predictions.
# These predictions are compared to y_test to compute the generalization error.
y_test_pred = model.predict(X_test)

# ──────────────────────────────────────────────────────────────────────────────
# STEP 5: COMPUTE EVALUATION METRICS
# ──────────────────────────────────────────────────────────────────────────────

# Compute RMSE on training data.
# RMSE = sqrt(mean of squared differences between actual and predicted).
# It reports error in the same units as the target (exam score points here).
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))

# Compute RMSE on test data (the more important metric for real-world usefulness).
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

# Compute MAE on test data (mean absolute error; less sensitive to large outliers).
test_mae = np.mean(np.abs(y_test - y_test_pred))

# Compute R² on test data.
# R² = 1 means perfect predictions; R² = 0 means the model is no better than
# always predicting the mean score; negative R² means the model is actively harmful.
test_r2 = r2_score(y_test, y_test_pred)

# ──────────────────────────────────────────────────────────────────────────────
# STEP 6: PRINT ALL METRICS
# ──────────────────────────────────────────────────────────────────────────────

print("\n── Evaluation Metrics ───────────────────────────────────────────")
print(f"Training RMSE : {train_rmse:.2f} score points")
print(f"Test RMSE     : {test_rmse:.2f} score points")
print(f"Test MAE      : {test_mae:.2f} score points")
print(f"Test R²       : {test_r2:.4f}")

# If test RMSE >> training RMSE, the model may be overfitting (unusual for
# simple linear regression but common with many features or polynomial terms).

# ──────────────────────────────────────────────────────────────────────────────
# STEP 7: RESIDUAL ANALYSIS
# ──────────────────────────────────────────────────────────────────────────────

# Compute residuals for the test set: actual minus predicted, one value per row.
# Positive residual = model underpredicted.
# Negative residual = model overpredicted.
test_residuals = y_test - y_test_pred

# Print summary statistics of residuals.
print("\n── Residual Diagnostics ─────────────────────────────────────────")
print(f"Mean of test residuals   : {np.mean(test_residuals):.4f}  (should be near 0)")
print(f"Std dev of test residuals: {np.std(test_residuals):.4f}  (spread of errors)")
print(f"Max residual (underpredict): {np.max(test_residuals):.2f} score points")
print(f"Min residual (overpredict) : {np.min(test_residuals):.2f} score points")

# ──────────────────────────────────────────────────────────────────────────────
# STEP 8: MAKE A SINGLE NEW PREDICTION (inference on one new student)
# ──────────────────────────────────────────────────────────────────────────────

# Define a hypothetical new student who studies 6.5 hours per week.
new_student_hours = np.array([[6.5]])   # Must be 2D for sklearn's predict().

# Ask the trained model for a predicted score for this new student.
predicted_score = model.predict(new_student_hours)[0]

# Also compute what the "true" formula would give (ground truth for comparison).
true_expected_score = TRUE_INTERCEPT + TRUE_SLOPE * 6.5

print("\n── Single Prediction Example ────────────────────────────────────")
print(f"New student: 6.5 study hours/week")
print(f"Model prediction    : {predicted_score:.2f} score points")
print(f"True expected score : {true_expected_score:.2f} score points")
print(f"Difference          : {abs(predicted_score - true_expected_score):.2f} score points")
```

---

### Logic Walkthrough: Following Data Through the Entire Script

**Stage 1 — Building the synthetic world**
We begin by *manufacturing* data rather than loading it from a file. This is a deliberate teaching choice: by constructing a dataset where we know the true formula (score = 45 + 8 × hours + noise), we can verify that the model's learned parameters approximate the ground truth. In real projects, the truth is hidden; here, we have the cheat sheet and can test whether the model's educated guess is close.

The random number generator produces 150 "study hour" values scattered between 1 and 10. We apply the true formula to get noiseless scores, then add Gaussian noise to simulate the fact that real exam performance is not perfectly deterministic — two students with identical study hours may score differently due to factors not captured in the features.

**Stage 2 — Protecting the test set**
`train_test_split` shuffles the rows randomly, then assigns 80% (120 rows) to training and 20% (30 rows) to testing. From this moment forward, the model is *not allowed to see* the test rows until evaluation. This simulates the real-world scenario where the model is trained on historical data and then tested on future observations it has never encountered.

**Stage 3 — Fitting the model**
`model.fit(X_train, y_train)` is the training step. Internally, sklearn solves the normal equations — a linear algebra operation that returns the unique set of weights minimising squared error on the training data. After this line, `model.intercept_` and `model.coef_[0]` hold the learned baseline and slope, respectively. Because we know the true values (45.0 and 8.0), we can immediately check how close the learning process came.

**Stage 4 — Generating predictions**
`model.predict()` is pure arithmetic: multiply each input by the learned slope, add the intercept. There is no randomness, no lookup, no memory of training rows — just the formula applied row by row. We generate predictions for both training and test rows to compare in-sample vs. out-of-sample error.

**Stage 5 — Metrics as compressed summaries**
RMSE translates the abstract "squared error" into something readable: "on average, predictions are off by about X score points." Comparing training RMSE and test RMSE is the primary overfitting diagnostic. \(R^2\) contextualises this: "What fraction of the variation in scores does the model explain?" A value near 0.7–0.8 is typical for a single-feature noisy model; near 1.0 would indicate near-perfect prediction (often a sign of overfitting or data leakage).

**Stage 6 — Residual diagnostics**
Printing summary statistics of residuals gives a first-pass diagnostic: a mean near zero confirms no systematic directional bias; the standard deviation quantifies typical error spread; the extreme values flag potential outliers. In a production model, you would also *plot* these (residuals vs. predicted values, residuals vs. study hours) to check for nonlinearity or heteroscedasticity — patterns invisible in summary numbers alone.

**Stage 7 — Single-prediction inference**
The final block demonstrates the model as a deployment artefact: given one new student's study hours, produce one predicted score. This is the operational mode — the model has already learned; now it simply computes. The comparison to the known true expected score is a sanity check only possible in synthetic teaching scenarios.

---

## Session Synthesis: From Real Questions to Honest Forecasts

We covered a lot of ground. Let us compress it into a mental model you can carry forward.

**Regression** answers "how much?" questions by learning a formula from labelled examples. **Linear regression** is the simplest and most interpretable version of that formula: a weighted sum of input features, with one coefficient per feature and an intercept. **Training** is the process of finding the coefficient values that minimise prediction error on known examples — for linear regression, this is solved exactly in one algebraic step.

But training error is not the goal; **generalization** is. A model that overfits the training data memorises noise and fails on new data. A model that is too simple underfits and fails everywhere. The sweet spot is a model with just enough complexity to capture real patterns without chasing random fluctuations.

Finally, **residuals** are the microscope for model quality. Aggregate metrics like RMSE are useful summaries, but the residuals reveal whether the model is wrong in a *structured, predictable way* (which can be fixed) or in a *random, patternless way* (which is irreducible noise). A practitioner who reads residuals carefully is a practitioner who continuously improves their models.

One habit to carry into every future project: whenever you receive a model output, ask three questions — *What is the error in real units? Was it measured on held-out data? Do the residuals look random?* If all three answers are satisfying, you have an honest forecast.

---

## Framework & Library Cheat Sheet

| Concept / Tool | Formal Blueprint | Plain-Language Role |
|---|---|---|
| **Regression** | Supervised learning task: map features to a continuous real-valued target | Answers "how much / how many?" questions |
| **Linear regression** | Model: \(\hat{y} = w_0 + w_1 x_1 + \ldots + w_p x_p\); fitted by minimising SSR | Transparent, interpretable baseline model |
| **Target variable** | Continuous scalar output to be predicted | The "answer column" in training data |
| **Features** | Input variables / predictors | The clues given to the model |
| **Continuous value** | Real-valued quantity on an unrestricted scale | Any measurable number (not a category) |
| **Labelled data** | Input–output pairs \((x_i, y_i)\) used for supervised training | Past examples with known answers |
| **Ordinary least squares (OLS)** | Minimises sum of squared residuals; solved by normal equations | How sklearn's `LinearRegression` fits the line |
| **Intercept / bias term** | Constant \(w_0\) in the linear equation | Baseline prediction when all features = 0 |
| **Coefficients / weights** | Learned multipliers per feature | How much each input shifts the prediction |
| **Gradient descent** | Iterative weight update in direction of steepest loss decrease | Alternative fitting method used in neural nets |
| **Loss function / MSE** | Average squared error over training examples | Single number guiding the training algorithm |
| **Training / fitting** | Estimating weights to minimise loss on training data | Teaching the model from examples |
| **Prediction / inference** | Applying trained weights to new inputs | Using the model in practice |
| **Train–test split** | Partition data into disjoint training and evaluation sets | Simulates generalisation to unseen data |
| **Generalization** | Model performance on unseen data from the same distribution | The real-world usefulness metric |
| **Overfitting** | Low training error, high test error — model learned noise | Complexity trap; fix with simpler model or regularisation |
| **Underfitting** | High error on both training and test — model too simple | Capacity trap; fix with richer features or more complexity |
| **Bias–variance tradeoff** | Error decomposition: bias (wrong assumptions) + variance (noise sensitivity) | Governing tension in all model complexity decisions |
| **Cross-validation (K-fold)** | Rotate K validation folds over training data; average performance | More reliable generalisation estimate than one split |
| **RMSE** | \(\sqrt{\text{MSE}}\); error in target units | "Typical" prediction error in real units |
| **MAE** | Mean absolute error; less outlier-sensitive than RMSE | Robust typical error |
| **\(R^2\)** | Fraction of target variance explained by the model | Proportional fit quality (1 = perfect, 0 = no better than mean) |
| **Residual** | \(e_i = y_i - \hat{y}_i\); actual minus predicted | Per-example error; positive = underpredicted |
| **Residual plot** | Graph of residuals vs. predicted values or a feature | Primary visual diagnostic for model quality |
| **Heteroscedasticity** | Non-constant residual variance across feature/prediction range | Error spread grows in some regions; requires model revision |
| **Outlier (in regression)** | Observation with an unusually large absolute residual | May be data error, data entry issue, or genuine extreme case |
| **`numpy`** | Numerical computing library; array operations and math | Synthetic data generation, residual arithmetic |
| **`sklearn.model_selection.train_test_split`** | Splits arrays into random train and test subsets | Partitions data to simulate generalisation |
| **`sklearn.linear_model.LinearRegression`** | OLS linear regression estimator | Fits the model and stores learned weights |
| **`sklearn.metrics.mean_squared_error`** | Computes MSE between true and predicted arrays | Foundation for RMSE computation |
| **`sklearn.metrics.r2_score`** | Computes coefficient of determination | Reports proportional explanatory power |

---

*End of lecture notes — Session 28: Regression / Linear Regression Fundamentals.*
