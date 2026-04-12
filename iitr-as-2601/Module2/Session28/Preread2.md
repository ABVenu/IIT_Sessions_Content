Think about the last time you booked a cab. Before you even confirmed the ride, the app told you the exact fare — ₹247, not "cheap" or "expensive." Or the food delivery app that promised your biryani in 32 minutes. Or the bank that approved your friend's personal loan in seconds.

None of those numbers came from a person sitting at a desk doing mental math. A machine studied thousands of past examples — and quietly figured out the formula on its own. That is the kind of intelligence you are about to build.

---

## The Problem: What If You Had to Predict 10,000 Salaries by Hand?

Imagine a company hiring 10,000 people next year. For each candidate, they have the years of experience, the job role, and the city. The HR team needs to give every single person a fair salary offer — a specific number in rupees.

How would you do it? You can't call each one individually. You can't create a rule for every possible combination of experience and role. Even the most experienced HR manager would run out of time and consistency.

This is not a made-up problem. Every major company, hospital, and e-commerce platform faces a version of this challenge every day.

---

## The Solution: Let the Computer Learn the Formula

This session introduces **Regression** — the branch of machine learning where the computer learns to predict a *specific number*, not just a yes/no or a category. And the simplest, most powerful starting point is **Linear Regression**.

You will give the computer hundreds of past examples where you already know the answer. It will study those examples, figure out its own formula, and then use that formula to predict numbers it has never seen before — instantly, at scale, consistently.

Three lines of Python code. That is all it takes to go from raw data to a working prediction engine.

---

## The Simple Analogy: It Works Exactly Like a Taxi Meter

Here is the one idea that unlocks everything in this session:

> A taxi meter starts at a **base fare** — say ₹30 — the moment you sit down. Then it adds ₹15 for every kilometre you travel. The formula is: *Base + (Rate × Distance)*.

**Linear Regression does the exact same thing.** Except instead of a taxi company deciding the base fare and rate manually, the *computer figures both numbers out on its own* by studying thousands of past trips.

That base fare is called the **intercept** — the model's starting prediction before any clues are considered. The rate per kilometre is called the **coefficient** — the multiplier the model learns for each input. The computer reads your historical data, reverse-engineers the best intercept and coefficient, and locks them in. From that point on, it can predict new numbers it has never encountered.

That is the entire core of this session. Everything else is built on top of this idea.

---

## What You Will Be Able to Do After This Session

- Instantly recognise a **regression problem** — you will know when a question calls for predicting a number versus picking a category, and why that distinction matters
- Understand what a model is actually **"learning"** — the two specific numbers it extracts from your data, and what they represent in plain English
- **Train your first prediction model in Python** — using `scikit-learn`, the industry-standard library used by data scientists worldwide
- **Catch a model that is cheating** — detect the difference between a model that genuinely learned a pattern versus one that just memorised past data
- **Read your model's mistakes like a diagnostic report** — and use those errors to understand what is missing, what is off, and how to improve

---

## Interesting Questions — Answered Only in the Live Session

Let these sit with you before class:

1. **The model is just a formula with two numbers.** Why can't you simply calculate those two numbers yourself with a calculator in five minutes? What is the computer actually *doing* during "training" that makes it indispensable?

2. **If a model scores perfectly on its own practice data — predicting every past example correctly — shouldn't that be the best possible result?** Why might a model with perfect training scores actually be *broken*, and dangerous to use?

3. **Every wrong prediction produces an error — a gap between what the model said and what actually happened.** What does the *pattern* of all those errors, taken together, tell you about your model? What hidden truth can you only see when you look at the mistakes as a whole?

---

*See you in the session.*
