# Pre-read: The ML Workflow & Habits

## When the Numbers Stop Being Just Numbers

Imagine you are a loan officer at a bank. Every day, hundreds of people walk in asking for a loan. Your job? Decide — quickly — who will repay it and who will not. You cannot meet them all. You cannot read minds. But you *do* have data — their income, credit history, employment years, and past loan behaviour. The question is: **how do you turn that data into a reliable decision?**

This is not a hypothetical. Banks, hospitals, streaming platforms, and e-commerce companies make millions of such decisions every single day — automatically, at scale, without a human reviewing each case. The technology behind this is **Machine Learning (ML)**. And starting today, you will learn exactly how it works.

---

## What If You Had to Do It All by Hand?

Picture this: a hospital gives you a spreadsheet of 50,000 past patients — their age, weight, blood sugar, family history — and asks you to predict which of the next 10,000 patients will develop diabetes. By hand.

You could try to spot patterns. Maybe older patients with high sugar levels tend to be at risk. But what about the 47 other columns? What about rare combinations? What about the 10,000 new patients arriving tomorrow? Doing this manually is impossible — slow, inconsistent, and error-prone at scale.

**This is exactly the problem Machine Learning was built to solve.** Instead of you writing the rules, you give the computer thousands of labelled examples — and it figures out the rules itself.

---

## The Workflow That Makes It All Work

Here is the catch — you cannot just dump data into a computer and hope it learns correctly. Without a proper plan, things go wrong *silently*. A model might look like it is performing brilliantly — 95% accuracy — but fail completely the moment it meets real-world data it has never seen before.

This is why every serious ML practitioner follows a **structured workflow**: a step-by-step process that ensures the computer learns genuinely, not just memorises. Think of it like a recipe. A chef does not throw all ingredients into a pot at once. There is an order — prep, cook, taste, adjust. The ML workflow is your recipe for building models that actually work.

In this session, you will follow the same workflow that data scientists at Google, Amazon, and every major tech company use — from the very first question all the way to a working baseline model.

---

## In this pre-read, you'll discover:

- **What Machine Learning actually is** — and why it is fundamentally different from writing regular code
- **How to frame a real-world problem** so a computer can understand and solve it
- **The difference between Features and Labels** — the two most important building blocks of any ML dataset
- **Why splitting your data into three parts** (Training, Validation, and Test) is the single most important habit you will build in this course

---

## The Exam Analogy That Makes Everything Click

Think about how students prepare for a board exam:

- They study from a **textbook** — this is the *Training Set*. The model learns from it.
- They take **mock tests** every week — this is the *Validation Set*. It tells them where they are going wrong, before the real exam.
- On the final day, they sit for the **actual board exam** — this is the *Test Set*. It is seen exactly once, at the very end.

A good student never peeks at the actual exam paper during preparation. A good ML practitioner never lets their model "see" the test set until training is completely done.

This separation is what makes an ML result trustworthy. Without it, you are essentially grading yourself on a paper you already saw — and calling it success.

---

## One More Concept Worth Knowing Before You Join

Before any complex model is built, a smart ML practitioner always asks: *"What is the simplest possible prediction I can make — and how good is it?"*

This is called a **Baseline**. If 80% of your bank's customers never defaulted on their loans, then a model that simply predicts "No default" for everyone will be **80% accurate** — without learning anything at all. Any real ML model must beat this number to be considered useful.

The **Baseline** is your benchmark — your *par score*. Think of it like a cricket team setting a target. You know what you need to beat. Without it, a 78% accuracy sounds impressive until you realise that doing nothing at all gives you 80%.

---

## What You Will Be Able to Do After the Session

By the end of this session, you will be able to:

- Set up and navigate **Google Colab** — the cloud-based Python workspace used by data scientists worldwide
- Translate a vague business question (like *"Why are customers leaving?"*) into a clear, solvable **ML problem**
- Look at any dataset and correctly identify which column is the **Label (y)** and which columns are the **Features (X)**
- Split a dataset into **Training, Validation, and Test** sets using Python — without contaminating any set
- Build and evaluate a **Baseline model** that becomes your performance benchmark for every future model

---

## Questions You Will Solve in the Live Session

These questions may seem tricky right now — but by the end of the session, you will answer them with confidence:

> **1.** A company wants to predict whether a job applicant will resign within 6 months of joining. What is the **Label**? What could be the **Features**? And what type of ML problem is this — Classification, Regression, or Clustering?

> **2.** You build a model to detect fraudulent credit card transactions. Your model scores **98% accuracy**. Should you celebrate? What would the **Baseline accuracy** tell you that accuracy alone does not?

> **3.** A colleague scales all the data *before* splitting it into training and test sets. Why is this a problem? What rule were they violating — and what could go wrong in production?

---

Come to the session ready to open **Google Colab** in your browser. Everything else, we will build together — step by step.
