# Pre-read: Regression — Linear Regression Fundamentals

Imagine you are helping a friend buy their first flat in Pune. The broker shows three similar 2BHK homes in the same society — same floor plan, same builder — but the prices are **₹48 lakh**, **₹52 lakh**, and **₹61 lakh**. Your friend asks the only question that matters: *"So what should **our** flat actually cost?"*

You cannot answer with a label like **"expensive"** or **"cheap."** They need a **number** — a specific amount in rupees they can plan for, negotiate around, and compare with their loan limit. That is not sorting mail into **Inbox** vs **Promotions**. That is guessing a **measurement on a scale** — and that shift in question shape is what today's session is built for.

You have already learned how to **split data honestly**, guard against **leakage**, and question **accuracy** when the world is unfairly stacked. Until now, most of your machine learning examples asked *which category* something belongs to. Today the question changes: *what number should we expect?*

---

## The Challenge of Guessing Numbers at Scale

Picture an HR team at a growing company. They have spreadsheets for **400 past hires**: years of experience, weekly hours spent on upskilling, and the **monthly salary** each person actually received. A new candidate walks in — **6 years** of experience, **10 hours** of learning per week. The manager turns to you:

> **What if** you had to predict fair salaries for **every new applicant** using only a calculator and gut feel — one row at a time, with no pattern to copy from?

You might average past salaries and say **"around ₹50,000"** for everyone. That is safe but lazy — it ignores that experience and learning hours clearly matter. You might squint at the spreadsheet and draw a mental trend line. But **400 rows**, noise, and two clues at once? Doing it by hand is slow, inconsistent, and impossible to repeat tomorrow when new data arrives.

The real world runs on these **"how much?"** questions all the time:

| Everyday question | Type of answer |
|---|---|
| What will this flat sell for? | A **rupee amount** |
| What salary should we offer this candidate? | A **monthly number** |
| How many minutes until the food arrives? | **32 minutes** — not just "late or on time" |

When the answer must be a **specific number**, we call the task **regression**. When the answer is a **named bucket** (spam or not spam, pass or fail), that is **classification** — the world you have been living in until now. Today you step into the numeric side — and meet the simplest hero for that job: **linear regression**.

---

## A Straight Line Through the Cloud of Dots

So how does a computer pick a number without guessing randomly? **Linear regression** learns a relationship you already understand from daily life — like a **taxi meter**.

The ride starts at a **base fare** (say ₹30) even before you move. Every extra kilometre adds a fixed amount (say ₹15 per km). The meter does not memorise every past trip; it follows a simple rule: **starting point + (rate × distance)**. Linear regression does the software version of that: it learns a **baseline** (called the **intercept**) and a **rate per clue** (called a **coefficient**) for each feature — experience, learning hours, area, distance, and so on.

Picture **200 students** on a chart: **study hours** left to right, **exam score** up and down. Each student is a dot. You could draw countless straight lines through that cloud — steep, flat, high, low. The **best-fit line** is the one where the **vertical gaps** from dots to the line are collectively as small as possible. The model finds that line from data — then uses it to predict scores for students it has never seen.

You will **train** this model in Google Colab on a clean salary table, **predict** held-out test rows, and compare your results to a **mean baseline** — the lazy rule that always guesses the average training salary. If your line cannot beat *"just say ₹50,000 for everyone,"* the features may not be helping yet. You will also peek at **train vs test error** (a quick overfitting check) and **residuals** — the gap between actual and predicted for each row — to see whether mistakes are random or hiding a pattern.

---

Think of linear regression like **adjusting a ceiling fan speed** with two dials — one for **base speed**, one for **how much each extra degree of heat adds**. You watch many past days (data), find the dial settings that best match what actually happened, then use those same settings on a **new hot afternoon** you have not seen yet. The formula is frozen; only the inputs change.

---

**In this pre-read, you'll discover:**

- **How** regression differs from classification — when the answer is a **number on a scale** vs a **category in a box**
- **Why** the **best-fit line**, **features**, **target**, **intercept**, and **coefficient** matter — explained with salary and taxi-meter stories, not heavy maths
- **How** to **fit** and **predict** with `LinearRegression` in Colab using the same **split-first** habit you already practise
- **How** a **mean baseline** sets a simple floor — and why **residuals** reveal mistakes that one average error number can hide

---

## Ideas Worth Knowing Before We Go Live

**Regression** — A supervised learning task where the model predicts a **continuous numeric output** (salary, price, minutes) from input **features**. In simple words: the answer is a number like ₹45,000 or 72 minutes, not a tick in a box.

**Classification (contrast)** — The answer is a **category** — spam or not spam, fraud or genuine. Same features, different shape of answer.

**Target (y)** — The numeric column you are trying to guess — the "answer column," e.g. `monthly_salary_inr`.

**Feature (x)** — The clues the model uses — years of experience, learning hours, flat area, delivery distance.

**Linear regression** — Predicts the target as a **weighted sum of features plus a constant**. Like: base ₹26,000 + ₹3,400 per year of experience + ₹750 per learning hour.

**Intercept** — The model's **starting point** before it looks at the clues — the base fare on the taxi meter.

**Coefficient** — How much the prediction **changes when one feature goes up by one unit** — the rate per kilometre.

**Best-fit line** — The line (or formula with many features) that keeps prediction gaps on training data as small as practical.

**Mean baseline** — Always predict the **average training salary** for every test row. A deliberately simple floor your real model should beat on the **same test split**.

**Overfitting (brief)** — Great on training rows, worse on locked-away test rows — like memorising last year's paper instead of learning the subject.

**Residual** — For one row: **actual minus predicted**. Positive means the model **under-predicted**; negative means it **over-predicted**.

**Residual plot** — A chart of predicted values vs residuals — helps spot bias, curves, or "fan" shapes that one average error hides.

---

## Questions We Will Answer in the Live Session

1. **Regression or classification?** For each problem — tomorrow's max temperature in °C, loan approved vs rejected, exact exam score out of 100, spam vs not spam, monthly electricity bill in rupees — which task type fits, and **why**? (Hint: is the answer a **measurement** or a **named category**?)

2. **The salary puzzle:** After training, intercept ≈ **₹26,000**, coefficient for experience ≈ **₹3,400**, coefficient for learning hours ≈ **₹750**. What salary would you predict for someone with **4 years** experience and **5 hours** of learning per week — and how does that compare to what `model.predict()` returns in Colab?

3. **The baseline showdown:** Linear regression's average test error is **₹4,200**; the mean baseline's is **₹9,800** on the **same** held-out rows. Did the features help? Why must the mean be computed from **training labels only** — never from the full dataset including test?

4. **Reading the gaps:** Train average error is **₹500** but test is **₹8,000** — vs train **₹3,000** and test **₹3,200**. What story does each pair tell about **generalization** — and what would you check next?

---

## After This Session, You Will Be Able To

- **Tell** regression apart from classification using everyday examples — house price, salary, delivery time vs spam and pass/fail  
- **Explain** intercept, coefficient, and best-fit line intuition without leaning on heavy formulas  
- **Train** and **predict** with `LinearRegression` in Colab on a pre-cleaned numeric dataset — **split first**, fit only on training data  
- **Compare** your model to a **mean baseline** on the same test split and discuss whether features are adding real value  
- **Spot** a possible overfitting warning by comparing **train vs test error** on the regression example  
- **Compute** residuals, interpret their **sign**, and read a simple **residual plot** for systematic mistakes — with a pointer to formal metrics like MAE and R² coming later  

See you in class. The jump from *"which bucket?"* to *"how much exactly?"* is where many real products live — from salary bands and rent estimates to delivery ETAs — and today you train your first model that speaks that language honestly.
