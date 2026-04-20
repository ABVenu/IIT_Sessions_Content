# Pre-read: Classification: Logistic Regression Fundamentals

## The hook

So far, much of your machine learning practice has been about answering **“how much?”**—scores, prices, temperatures. In real jobs, an equally common question is **“which bucket?”**: pass or fail, spam or not spam, fraud or genuine. Banks, hospitals, and apps make millions of these **category** decisions every day. Knowing how a simple, trusted model turns inputs into a **yes/no** (or positive/negative) answer—and how confident it is—is a core skill, not a side topic.

## The problem

**What if** your data clearly supports a **label**, but a plain numeric model keeps outputting impossible answers—like “1.7” for pass/fail, or negative “scores” that do not map to any real decision?

Regression lines can shoot anywhere on the number line. Classification needs **clear outcomes** and often a sense of **risk**: two people might both get “approved,” but one approval might be a coin-toss while the other is almost certain. Without probability and a clear **cut-off**, you cannot explain decisions to a manager—or tune behaviour when false alarms are expensive, or misses are dangerous.

## The solution preview

This session introduces **classification**: predicting **categories** instead of continuous numbers, with **binary** problems (exactly two classes) as the main focus. The hero method is **logistic regression**—despite the word “regression,” it is built for labels. It uses an **S-shaped (sigmoid)** curve to turn internal scores into **probabilities between 0 and 1**, then applies a **decision threshold** (often 50%) to pick the class.

You will see **class predictions** versus **probability outputs**, learn how **changing the threshold** shifts mistakes, and read a **confusion matrix** so you know not only *accuracy*, but *what kind* of errors the model makes.

## A simple analogy

The lecture compares the **sigmoid** to a **water tap**: however you turn it, the flow stays between fully closed (0%) and fully open (100%)—it never goes “past 100%” or below zero. In the same way, the sigmoid squeezes raw model scores into a **valid probability**, so the numbers always fit what “chance” actually means.

## What you will be able to do after the session

- Tell **classification** apart from **regression** and name common **binary** use cases (fraud, spam, disease, pass/fail).
- Explain why **linear regression alone** is a poor fit when the answer must be a **category** with sensible **probabilities**.
- Describe **logistic regression** at a high level: **probability first**, then a **label**; role of the **sigmoid**.
- Use **predicted class** vs **predicted probabilities** and interpret why two rows can share a label but **not** the same **confidence**.
- Adjust the **decision threshold** and describe the trade-off between **false positives** and **false negatives** in plain language.
- Read a **confusion matrix**: **true/false positives and negatives**, and what each cell implies for real decisions.

## Questions we will answer in the live session

1. How does the model go from features (like study hours) to a **probability**, and then to a single **Pass/Fail** (or 0/1) answer?
2. Why might you **intentionally** move the cut-off away from 50%—and how does that change who gets flagged as “positive”?
3. If accuracy looks fine, why do we still need a **confusion matrix** to understand **where** the model fails?

Come ready to connect **math intuition** (sigmoid, threshold) to **stories you can tell** in an interview or a stakeholder meeting.
