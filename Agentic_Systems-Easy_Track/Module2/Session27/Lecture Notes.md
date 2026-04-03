
## 1. Why Model Evaluation Can Be Misleading

After preparing a dataset, the next natural step in machine learning is to train a model and evaluate how well it performs. The model makes predictions, and those predictions are compared against the actual outcomes. Based on how many predictions are correct, we calculate a performance score — most commonly, accuracy.

At first glance, this process seems perfectly reliable. If the model scores 95% accuracy, it appears that the model has learned well and is ready to be trusted.

However, in real-world scenarios, this assumption is often dangerously incorrect.

To understand why, consider a simple everyday situation. Imagine evaluating a student based on an exam. If the student scores 95 out of 100, we naturally assume the student understands the subject well. But what if the student had already seen the exact same questions before the exam? In that case, the high score does not reflect understanding at all — it only reflects prior exposure to the answers.

Now consider another situation. Suppose the exam is extremely easy — every question has an obvious answer that most people would guess correctly. The majority of students may score above 90%, even if their actual understanding of the subject is shallow. Again, the score looks impressive, but it does not meaningfully measure knowledge.

Machine learning models fall into exactly the same traps. A model may show high performance during evaluation not because it has genuinely learned meaningful patterns from the data, but because of one of two hidden problems:

- The model was given access to information it should never have seen during training
- The dataset is structured in a way that heavily favors one outcome, making it easy to score well without truly learning

These two problems are called **data leakage** and **class imbalance**.

What makes both problems particularly dangerous is that they are subtle. They do not produce visible errors or warnings. Instead, they silently create a situation where the model looks highly accurate during evaluation but completely fails when used in the real world.

Understanding these two issues is foundational — because if either problem is present, you cannot trust any performance number the model produces.

![Training vs real prediction time: leakage gives the model information that will not exist at deployment](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-01-data-leakage-overview.png)

---

## 2. Understanding Data Leakage

A machine learning model is built on one core assumption: it learns patterns from past data, and then it applies that learning to new data it has never seen before. This separation between what the model learns from and what it is tested on is absolutely fundamental.

Data leakage occurs when this assumption is broken.

### What Data Leakage Means in Practice

Data leakage happens when the model is trained using information that would not actually be available at the time of making a real prediction. In other words, the model is given a sneak peek — either into the future, or into the answer itself — during training.

This causes the model to perform extraordinarily well during evaluation, but when it is deployed in the real world, it fails because that extra information is no longer available.

### Understanding Through Analogy

Think of three students preparing for the same exam:

- The first student studies concepts from textbooks and practices solving problems on their own
- The second student practises using previous years' exam papers to understand the pattern of questions
- The third student somehow obtains the actual answer sheet of this year's exam before the test

All three students may score high marks. But only the first student has genuinely learned. The third student has not learned anything — they have simply memorised answers they should never have had access to.

Data leakage causes a machine learning model to behave exactly like the third student. The model has not learned genuine patterns. It has simply exploited information that will not exist when it faces the real world.

### Examples Across Different Domains

To make this concrete, consider how leakage might appear across different real-world datasets.

**Car Price Dataset**

Suppose the goal is to predict the selling price of a car based on its features. Valid inputs that would be available before the sale include the manufacturing year, mileage, and fuel type. A leakage input would be the final negotiated sale price — because that value only exists after the prediction was supposed to have been made. Including it makes the model look perfect, but it is useless in practice.

**Student Performance Dataset**

Suppose the goal is to predict a student's final marks based on their engagement throughout the semester. Valid inputs include attendance percentage and assignment scores. A leakage input would be the final exam marks themselves — because you cannot know the final marks before they are awarded. If those marks are included in training, the model is effectively reading the answer.

**E-commerce Dataset**

Suppose the goal is to predict whether a user will make a purchase. Valid inputs include browsing history and time spent on product pages. A leakage input would be the order confirmation record — because that only exists after the purchase has already happened. Including it means the model already knows the outcome.

### What Happens Internally

When a model is trained without leakage, it must work hard to find genuine relationships between inputs and outputs. It learns that higher mileage tends to lower car prices, or that poor attendance correlates with lower marks. These are real, useful patterns.

When a model is trained with leakage, it does not need to find those relationships. It simply learns a shortcut — a direct path to the answer through information that should not have been available. The model becomes lazy and brittle.

### Consequences

The consequences of data leakage are particularly deceptive. During training, performance is high. During testing, performance is also high — because the test data was likely contaminated by the same leakage. But when the model is deployed in the real world, where the leaked information no longer exists, performance collapses.

This is why leakage is so dangerous. It does not announce itself with errors. It silently produces an illusion of success.

### A Useful Thinking Question

Before including any feature in your model, always ask:

> "Would this information genuinely exist at the moment I need to make this prediction?"

If the answer is no, or even uncertain, that feature should not be used.

---

## 3. How Data Leakage Happens in Practice

Data leakage is rarely introduced deliberately. It almost always happens because of the order in which data processing steps are carried out. Understanding the exact mechanisms helps you prevent it.

### Scenario 1 — Preprocessing Before Splitting

This is the most common and most overlooked source of leakage. Consider the following workflow, which looks perfectly reasonable at first:

1. Load the dataset
2. Fill missing values using the column average
3. Scale all features to a standard range
4. Split the data into training and test sets

The problem is in steps 2 and 3. When you calculate the average for filling missing values, you are calculating it using the entire dataset — including the data that will later become the test set. Similarly, when you scale features, the scaling parameters are computed from the full dataset.

This means the test data has quietly influenced the training process. The model has indirectly "seen" information from the test set before evaluation even begins.

**Student Dataset Example**

Suppose some students have missing marks records. If you calculate the average mark using all students — including the students who will later be used for testing — and use that average to fill in the missing values, then the test students have shaped the training data. The two sets are no longer truly independent.

**Car Dataset Example**

If you scale car prices using the minimum and maximum values from the entire dataset, the test cars contribute to that scaling range. When the model is later evaluated on those test cars, it is not seeing truly unseen data — it has influenced its own evaluation.

**E-commerce Dataset Example**

If you normalise order values using a statistic calculated from all orders, test orders are embedded in the transformation that was applied during training. The separation between training and testing is illusory.

### Scenario 2 — Feature Engineering Using the Target

Sometimes leakage is introduced when new features are created using the outcome variable itself. For example, if the goal is to predict house prices and someone creates a feature called "is expensive" by looking at the actual price and labelling houses above a threshold as expensive — that feature is simply a restatement of the answer. The model will learn to use this feature perfectly because it is derived directly from what it is trying to predict. This is not learning; it is cheating.

### Scenario 3 — Duplicate Records Across Splits

If the same data point, or a very similar one, appears in both the training set and the test set, the model may effectively have memorised that record during training and then encounter it again during evaluation. This makes the evaluation look impressive, but it does not reflect how the model would perform on genuinely new data.

### What Happens If These Are Not Fixed

If leakage is present and undetected, the model will report high accuracy during development. Teams will celebrate the result. The model will be deployed. And then, in production, it will quietly fail — because the information it relied upon does not exist in the real world.

### What Happens When Fixed Properly

When leakage is removed, evaluation scores may initially drop. This can feel discouraging, but it is actually a sign of progress. The scores are now honest. A model with 78% accuracy without leakage is far more valuable than a model with 97% accuracy that was built on leaked information.

---

## 4. Data Leakage Guard — The Correct Workflow

![Wrong order (leaky): preprocess on all data before split. Correct order: split first, then fit transforms on training data only](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-02-split-first-workflow.png)

Preventing data leakage requires following a strict and deliberate order of operations. It is not complicated, but it requires discipline.

### Core Principle

The model should only ever learn from information that would realistically be available at the time of prediction. The test set must remain completely untouched and unseen until the very final step of evaluation.

### Correct Workflow — Step by Step

**Step 1 — Split the data first, before doing anything else**

The very first action after loading your data should be to separate it into a training set and a test set. This split must happen before any filling of missing values, before any scaling, before any transformation of any kind. Once this split is made, the test set is set aside and must not be touched again until final evaluation.

**Step 2 — Learn all transformations exclusively from training data**

Any statistics you need — the average for filling missing values, the minimum and maximum for scaling, the categories for encoding — must be calculated only from the training data. The test data has no role in these calculations whatsoever.

**Step 3 — Apply those learned transformations to the test data**

Once you have calculated your transformation parameters from the training data, you apply those same parameters to the test data. You do not recalculate anything using test data. You simply apply what was learned from training.

### Why This Works

When you follow this order, the test data behaves exactly like genuinely new, unseen data from the real world. It was not involved in any calculation during training. It is not contaminated. When the model is evaluated on it, the results reflect how the model would truly perform in production.

### Code Implementation

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("data.csv")
X = data.drop("target", axis=1)
y = data["target"]

# Step 1: Split FIRST — before any transformation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Learn transformation parameters from training data only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Step 3: Apply the same transformation to test data — do not refit
X_test_scaled = scaler.transform(X_test)
```

Notice that `fit_transform` is used on the training set — this means the scaler learns from training data and applies the transformation in one step. On the test set, only `transform` is used — the scaler applies the already-learned parameters without recalculating anything.

### Key Reminder

The test dataset must behave like completely unseen future data. It should have zero influence on anything that happens during training. If it does, you have leakage.

---

## 5. Understanding Class Imbalance

![Class imbalance: the majority class dominates what the model sees during training](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-03-class-imbalance.png)

Once leakage is addressed, there is another important issue that affects how well a model can learn — not from how data is processed, but from how data is distributed.

### What Class Imbalance Means

Class imbalance occurs when one category in your outcome variable has significantly more data points than another. The model is therefore trained on a lopsided dataset, where it sees one type of outcome far more frequently than the other.

### Understanding Through Real Data

**Fraud Detection Dataset**

In a typical bank transaction dataset, the vast majority of transactions are completely normal. Fraudulent transactions are rare — perhaps only 1 in 100, or even 1 in 1000. This means the dataset might contain 99% normal transactions and just 1% fraudulent ones.

**Healthcare Dataset**

In a dataset of medical records, most patients are healthy. Those with a specific rare disease form a small minority. The model sees overwhelmingly more healthy cases than diseased ones.

**E-commerce Dataset**

Most website visitors browse without making a purchase. Those who actually complete a transaction are a small fraction. The majority class is "did not purchase" and the minority class is "purchased."

### Why This Happens Naturally

Imbalance is not a data quality problem — it reflects reality. Fraud really is rare. Serious diseases really are uncommon relative to the healthy population. Machine failures really do happen far less often than normal operations. The imbalance in data mirrors the imbalance in the real world.

The problem is not that imbalance exists. The problem is that when a model is trained on imbalanced data without any correction, it does not learn to handle both classes equally. It learns to favour the majority class because that is what it sees most of the time.

### How the Model Interprets Imbalanced Data

When a model repeatedly encounters one class far more than another, it begins to treat that class as the "default" safe answer. From the model's perspective, simply predicting the majority class most of the time results in a high number of correct predictions. The model has no incentive to learn the minority class because ignoring it still gives a good overall score.

### Analogy

Imagine a class of 100 students, where 95 students pass the exam and only 5 fail. If a teacher's grading assistant simply predicts "pass" for every single student, it will be correct 95% of the time. But it will have completely failed to identify the 5 students who needed help. The assistant appears effective, but it is useless for its actual purpose.

### What Happens If Imbalance Is Ignored

If imbalance is not addressed, the model learns to ignore the minority class almost entirely. It may detect almost no fraud cases, miss most disease diagnoses, or fail to flag the rare but critical events it was specifically designed to identify. The model performs well in aggregate but fails precisely where it matters most.

---

## 6. Why Accuracy Is Misleading With Imbalanced Data

![High accuracy can hide zero recall on the rare class when the model always predicts the majority label](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-04-accuracy-misleading.png)

Standard accuracy counts the total number of correct predictions and divides by the total number of samples. In balanced datasets, this is a fair measure. In imbalanced datasets, it becomes deeply misleading.

### A Detailed Example

Consider a dataset of 100 transactions:
- 99 are normal
- 1 is fraudulent

A model that simply predicts "normal" for every single transaction, without doing any real learning, will be correct 99 times out of 100. Its accuracy is 99%.

On paper, this looks outstanding. In reality, the model has never once correctly identified a fraud case. It has a 0% detection rate for the only thing it was built to detect.

### What Is Hidden Behind the Number

Accuracy only tells you how many predictions were correct overall. It does not tell you:

- How many of the rare, important cases were correctly identified
- Whether the model is performing differently across different classes
- Whether it is making dangerous misses in the minority class

A model with 99% accuracy that never detects fraud is not a 99% model. It is a completely failed model dressed in impressive numbers.

### Real-World Consequences

In healthcare, a model that misses most disease diagnoses is not a 95% accurate model — it is a dangerous model. In fraud detection, a model that lets most fraud through is not a high-performing model — it is creating financial loss at scale. In manufacturing, a model that misses most defects is not reliable — it is a liability.

This is why accuracy alone can never be trusted when working with imbalanced data. We need evaluation metrics that reveal the full picture.

### The Core Insight

Not all errors are equal. Predicting "normal" when it is actually "fraud" is a far more serious error than predicting "fraud" when it is actually "normal." Accuracy treats all errors identically. Better metrics do not.

---

## 7. Precision and Recall — Understanding What Accuracy Misses

![Precision (quality of positive predictions) vs recall (coverage of actual positives)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-05-precision-recall.png)

When accuracy fails to capture what matters, we turn to two more informative metrics: precision and recall. These metrics look at the model's behaviour on the important class specifically, rather than across all predictions.

### Understanding the Need First

In many real-world problems, the goal is not just to be mostly correct on average. The goal is to be correct in the cases that matter most. This is especially true in fraud detection, medical diagnosis, safety monitoring, and quality control — scenarios where missing a critical case has serious consequences, and where raising a false alarm is merely inconvenient rather than catastrophic, or vice versa.

Precision and recall give us two different views of exactly this question.

### Precision — The Quality of Positive Predictions

Precision focuses on the reliability of the model's predictions when it claims something is important.

It answers the question: When the model says "this is the important case," how often is it actually right?

**Step-by-Step Example — Email Spam Detection**

Suppose a spam filter marks 10 emails as spam. You check those 10 emails and find that 6 of them are genuinely spam, but 4 of them are actually legitimate emails that were wrongly flagged.

The filter's precision is imperfect. It is generating false alarms. Important emails are being incorrectly classified as spam and hidden from the user.

**What Low Precision Means in Practice**

Low precision means the model is overly aggressive in its predictions. It is flagging too many things as important when they are not. This leads to false alarms and unnecessary actions.

**Examples Across Domains**

In healthcare, low precision means patients are being told they might have a disease when they do not. This causes stress, unnecessary follow-up tests, and wasted medical resources.

In e-commerce, low precision in a recommendation engine means users are constantly shown irrelevant products, eroding trust in the platform.

In hiring, low precision in a candidate screening model means unqualified candidates are being shortlisted, wasting recruiters' time.

### Recall — The Coverage of Important Cases

Recall focuses on how comprehensively the model is identifying all important cases that actually exist.

It answers the question: Out of all the cases that are genuinely important, how many did the model successfully find?

**Step-by-Step Example — Fraud Detection**

Suppose there are 20 genuine fraud cases in your test data. Your model successfully flags 5 of them as fraud, but the remaining 15 fraud cases are predicted as normal and pass through undetected.

The model's recall is poor. Fifteen out of twenty fraud cases were completely missed.

**What Low Recall Means in Practice**

Low recall means the model is too conservative. It is missing many cases that should have been flagged. The consequences depend heavily on the domain.

**Examples Across Domains**

In healthcare, low recall means patients with a real disease are being told they are healthy. These missed diagnoses can have serious or fatal consequences.

In manufacturing, low recall in a defect detection system means faulty products are being approved and shipped to customers, leading to complaints, returns, and safety risks.

In security, low recall in a threat detection system means genuine threats are passing through undetected because the model was too cautious about raising alerts.

### Precision vs Recall — The Fundamental Trade-Off

Precision and recall exist in tension with each other. Improving one typically reduces the other, and the right balance depends entirely on the consequences in your specific situation.

If you increase the model's caution so that it only flags cases it is extremely confident about, precision improves — but recall suffers, because many genuine cases will not meet the high confidence threshold and will be missed.

If you relax the model's threshold so that it flags anything remotely suspicious, recall improves — but precision suffers, because many normal cases will be incorrectly flagged as important.

The practical question is always: which error is more costly in this situation? Is it worse to raise a false alarm, or is it worse to miss a real case? The answer determines which metric to prioritise.

### What Happens If These Metrics Are Ignored

If you rely on accuracy alone, you may confidently deploy a model that never catches fraud, misses most disease cases, or ships defective products — while its accuracy number continues to look high. Precision and recall prevent this by revealing what is happening within each class separately.

---

## 8. Handling Class Imbalance — Practical Techniques

![Oversampling (more minority examples) vs undersampling (fewer majority examples)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-06-over-under-sampling.png)

Once you understand the problem of class imbalance and why it causes the model to ignore the minority class, the next step is to adjust the training data so the model has a fairer opportunity to learn from both classes.

### Why Handling Is Necessary

If you train a model on heavily imbalanced data without any adjustment, the model will develop a strong bias toward the majority class. This is not a flaw in the algorithm — it is the algorithm doing exactly what it is designed to do, which is to minimise errors. On imbalanced data, the easiest way to minimise errors is to predict the majority class most of the time. Handling imbalance disrupts this shortcut and forces the model to pay genuine attention to the minority class.

### Oversampling — Increasing Minority Class Representation

Oversampling is a technique where you artificially increase the number of minority class examples in the training data so that the model sees them more frequently.

**How It Works**

The simplest form of oversampling is to duplicate existing minority class records. If you have 10 fraud cases and 990 normal cases, you might duplicate the fraud cases 99 times so that each class now has approximately 990 examples. The model now encounters fraud cases just as frequently as normal cases during training.

**Example**

In a fraud detection dataset with very few fraud records, those records are copied and added to the training data multiple times. The model, which previously saw fraud cases only once for every hundred normal cases, now sees them far more evenly.

**Effect on the Model**

Because the model now encounters the minority class far more often, it is forced to learn its patterns properly rather than treating it as an occasional curiosity. The model develops a more balanced understanding of both classes.

**Side Effects to Be Aware Of**

The main risk with simple oversampling is overfitting. When the same records are duplicated many times, the model may start to memorise those specific records rather than learning generalised patterns. It learns the exact features of those duplicated examples rather than the underlying characteristics of the class as a whole.

### Undersampling — Reducing Majority Class Representation

Undersampling takes the opposite approach. Instead of adding more minority class data, you reduce the amount of majority class data until both classes are represented more evenly.

**How It Works**

Records from the majority class are randomly removed until the dataset is more balanced. If you have 1000 normal transactions and 10 fraud cases, you might reduce the normal transactions to 100, creating a 10:1 ratio instead of 100:1.

**Effect on the Model**

With fewer majority class examples, the model can no longer take the easy path of always predicting the majority class. It must learn from the minority class as well.

**Side Effects to Be Aware Of**

The main risk with undersampling is loss of information. The records you remove from the majority class may contain valuable patterns that the model would have benefited from learning. By discarding a large portion of your data, you reduce the total amount of learning material available to the model, which can limit its ability to generalise.

### The Thinking Layer

The goal of balancing is not to make both classes have identical counts for its own sake. The goal is to give the model a fair opportunity to learn from both classes equally. Whether you achieve this through oversampling, undersampling, or a combination of both depends on the size of your dataset, the degree of imbalance, and the specific problem you are solving.

---

## 9. Synthetic Data Concepts

![Synthetic minority points as plausible blends between neighbouring real minority points](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-07-synthetic-data.png)

Simple oversampling — duplicating existing minority records — is better than doing nothing, but it has a fundamental limitation: it does not add any new information. The model is simply seeing the same data points multiple times. A more powerful approach is to generate entirely new, artificial data points that resemble the minority class but are not exact copies of any existing record.

### Why Simple Duplication Is Not Enough

When you duplicate data, you are not enriching the model's understanding. The model sees the same patterns repeated many times, which increases the risk of memorisation. What you actually want is for the model to learn the underlying shape and variety of the minority class — not just a handful of specific examples repeated endlessly.

### What Synthetic Data Is

Synthetic data consists of artificial data points that are created based on the patterns found in the real data. These new points are not copies of any existing record, but they are designed to be plausible and realistic representations of the minority class.

### How It Works — Step by Step

The core idea behind synthetic data generation for imbalanced datasets can be understood through the following steps:

1. Identify the existing minority class data points
2. For any given minority data point, find other minority data points that are similar to it — these are called neighbours
3. Create a new, artificial data point somewhere between those two similar points — not identical to either, but a plausible blend of both

This process produces data points that are varied and realistic rather than repetitive copies.

### Analogy

Imagine you are trying to teach someone to recognise a specific shade of green, but you only have two green paint samples. Rather than simply showing those two samples repeatedly, you mix them in different proportions to create a range of slightly different shades. Now the person can recognise the family of that colour, not just those two exact samples. Synthetic data generation works in the same spirit — creating variation within a class so the model learns the concept, not just specific instances.

### Examples Across Domains

In healthcare, synthetic data generation might create new patient records that represent plausible variations of known disease cases, giving the model a broader understanding of how the disease manifests.

In finance, synthetic fraud records might represent new variations of transaction patterns that resemble known fraud but with slight differences in amount, timing, and merchant category.

In e-commerce, synthetic purchase records might represent additional plausible user journeys that end in conversion, helping the model learn the variety of paths that lead to a sale.

### Side Effects to Be Aware Of

If the synthetic data generation process is applied carelessly, the resulting data points may be unrealistic — blends between very different records that produce combinations that would never occur in the real world. This can introduce noise into the model and reduce rather than improve its performance. The quality of synthetic data depends entirely on the quality and diversity of the original minority class records.

### The Benefit of Synthetic Data Over Simple Duplication

The key advantage of synthetic data is that it introduces genuine variety. The model is exposed to a wider range of minority class patterns, which helps it generalise better. Rather than memorising a few repeated records, it learns the broader characteristics of the class.

---

## 10. Cross-Validation — Can We Trust the Evaluation Result?

![k-fold cross-validation: each chunk serves as the test set once; average scores for a stable estimate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-08-k-fold-cv.png)

Even after carefully guarding against leakage and handling class imbalance, one important question remains: can we trust a single evaluation result?

### The Problem With a Single Train-Test Split

When you split your data once — say, 80% for training and 20% for testing — the result of the evaluation depends heavily on which records happened to land in the test set. If, by chance, the test set contains unusually easy cases, the accuracy will be artificially high. If the test set happens to contain unusually difficult cases, the accuracy will be artificially low.

In either case, you are judging the model based on a single, potentially unrepresentative sample. This is not reliable.

### Analogy

Imagine evaluating a teacher's effectiveness based on the performance of a single class of students. If that class happened to be exceptionally motivated, the results would look impressive. If the class happened to be unusually disengaged, the results would look poor. To get a reliable picture of the teacher's effectiveness, you would need to observe them across many different classes, and then look at the average outcome.

Cross-validation applies exactly this logic to model evaluation.

### What Cross-Validation Does

Cross-validation repeats the training and testing process multiple times, each time using a different portion of the data as the test set. In each round, a different subset of the data is held out for testing while the rest is used for training. This process continues until every part of the data has served as the test set exactly once.

### Step-by-Step Process

1. Divide the full dataset into a number of equal parts — commonly five or ten
2. In the first round, use parts 2 through 5 for training and part 1 for testing
3. In the second round, use parts 1 and 3 through 5 for training and part 2 for testing
4. Continue until each part has been used for testing once
5. Calculate the average performance across all rounds

### What This Gives You

Instead of a single performance score, you now have multiple scores from multiple independent evaluations. You can see not only the average performance, but also how much the performance varies across different splits. Low variation suggests the model is stable and generalises well. High variation suggests the model's performance is sensitive to which data it sees, which may indicate it needs more data or further tuning.

### Why It Matters

Cross-validation reduces the influence of randomness on your evaluation. No single lucky or unlucky split can distort the overall picture. The average across multiple rounds gives a much more reliable estimate of how the model will truly perform on new data.

### Code Implementation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# Perform 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5)

# View individual fold scores
print("Scores per fold:", scores)
# Example output: [0.82, 0.79, 0.85, 0.80, 0.83]

# View the average — this is your reliable performance estimate
print("Average score:", scores.mean())
# Example output: 0.818
```

Each value in `scores` represents the accuracy from one fold. The fact that they are similar to each other — ranging from 0.79 to 0.85 — suggests the model is stable. The mean of 0.818 is a far more trustworthy performance estimate than any single fold result would have been on its own.

---

## 11. Connecting Leakage, Imbalance, and Evaluation

![Honest evaluation combines guarding leakage, handling imbalance and metrics, and cross-validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/agentic-systems-easy-track/module2/session27/session27-09-evaluation-pillars.png)

The three concepts covered in this session — data leakage, class imbalance, and evaluation reliability — are not independent problems. They are interconnected, and mishandling any one of them leads to the same ultimate outcome: incorrect conclusions about how good your model actually is.

### How They Connect

**Data leakage inflates evaluation scores.** When the model has access to information it should not have, it performs far better during testing than it ever will in the real world. The evaluation score is fictional — it reflects not how much the model has learned, but how much it was able to cheat. A developer looking only at this score will believe the model is ready for deployment when it is not.

**Class imbalance makes accuracy meaningless.** When one class dominates the dataset, a model can achieve high accuracy simply by predicting the majority class for everything. The number looks good, but the model is blind to the minority class — which is often the entire reason the model was built. A developer relying on accuracy alone will believe the model is working when it is, in fact, missing the most important cases entirely.

**Without cross-validation, the evaluation is unreliable.** Even when leakage is prevented and imbalance is addressed, a single train-test split may give a misleading picture. The split may be unusually easy or unusually hard for the model, and a single score does not reveal this. A developer who evaluates on a single split may build false confidence or false pessimism based on a result that does not represent average real-world performance.

### The Chain of Consequences

If leakage is present → scores are inflated → you deploy a model that fails in production.

If imbalance is unaddressed → accuracy looks high but minority class is ignored → the model misses fraud, disease, or defects.

If cross-validation is skipped → one lucky or unlucky split shapes your entire understanding of the model → you make decisions based on noise rather than signal.

Each problem, on its own, is enough to produce a model that cannot be trusted. Together, they represent the three most common ways that model evaluation becomes a lie dressed as a success metric.

### The Right Approach Connects All Three

When you guard against leakage, handle imbalance, and use cross-validation, you create an evaluation process that is honest. The scores reflect genuine learning. The metrics reflect true performance on the cases that matter. And the results are stable enough to trust.

This is not about making your model look good. It is about making your model actually be good — and knowing the difference.

---

## Quick Reference — Cheat Sheet

### Core Libraries

```python
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
```

### Key Functions

| Function | Purpose |
|---|---|
| `pd.read_csv()` | Load dataset from a CSV file |
| `train_test_split()` | Split data into training and test sets |
| `StandardScaler()` | Create a scaler object |
| `scaler.fit_transform(X_train)` | Learn scaling from training data and apply it |
| `scaler.transform(X_test)` | Apply learned scaling to test data (no refitting) |
| `LogisticRegression()` | Create a classification model |
| `cross_val_score()` | Evaluate model across multiple splits |

### Core Concepts at a Glance

| Concept | What It Is | Why It Matters |
|---|---|---|
| Data Leakage | Model trained on information unavailable at prediction time | Inflates performance; fails in production |
| Class Imbalance | One outcome far outnumbers another in the dataset | Model ignores rare class; accuracy becomes meaningless |
| Precision | Of all positive predictions, how many were correct | Measures false alarm rate |
| Recall | Of all actual positives, how many were found | Measures miss rate |
| Oversampling | Duplicating minority class records | Balances training data; risk of overfitting |
| Undersampling | Removing majority class records | Balances training data; risk of losing information |
| Synthetic Data | Generating new, artificial minority class points | Adds variety; reduces overfitting from duplication |
| Cross-Validation | Repeating evaluation across multiple splits | Produces reliable, stable performance estimates |