# Pre-read: Classification Models and Evaluation Metrics

## The "Why" — A Story From the Real World

Imagine a hospital uses an AI model to screen patients for a serious disease. The model claims **95% accuracy** — and everyone is thrilled. But when the doctors look closer, they realise something terrifying: the model is simply telling *every single patient* they are healthy.

Because 95 out of 100 patients genuinely are healthy, the model scores 95% by doing absolutely nothing useful. The 5 sick patients? Sent home undetected.

This is not a made-up scenario. It is a real and dangerous problem in machine learning — and it happens whenever we trust a single number, like accuracy, without asking deeper questions.

---

## The Problem — What If "Good Enough" Is Not Actually Good?

Think about these real situations:

- A bank's loan approval model says it is **92% accurate** — but it quietly approves loans for customers who will default, because defaults are rare and the model learned to ignore them.
- A spam filter claims **98% accuracy** — but it is letting every phishing email through because spam is only 2% of all mail.
- A student performance model says **88% accurate** — but it never flags a single at-risk student, because most students pass anyway.

The question is not just *"How many did we get right?"*

The real questions are:
- Of all the students we predicted would **fail** — how many actually failed? *(Were our warnings correct?)*
- Of all the students who **actually failed** — how many did we catch? *(Did we miss anyone?)*

Accuracy cannot answer these. Today's session builds the tools that can.

---

## The Solution — A Better Toolkit and Smarter Models

This session does two things at once.

First, we introduce two powerful new classification models — **Decision Tree** (a model that thinks in clear, step-by-step rules, like a flowchart) and **Random Forest** (imagine 100 experts each giving their opinion and then taking a vote — the majority wins).

Then, we build a complete set of evaluation tools — **Precision, Recall, F1 Score, and ROC-AUC** — that reveal exactly *how* a model is failing, not just *whether* it is failing. These are the same metrics used by data scientists at hospitals, banks, and tech companies before any model goes live.

---

## The Simple Analogy — The Court of Law

Picture a judge in a courtroom. Their job is to decide: Guilty or Not Guilty.

Two types of mistakes can happen:
- **False Alarm** — They convict an innocent person. *(The model predicted Fail, but the student actually passed.)*
- **Missed Criminal** — They let a guilty person go free. *(The model predicted Pass, but the student actually failed.)*

A good judge — and a good model — must manage *both* mistakes carefully. Sometimes, missing a criminal is the bigger problem (cancer screening: never miss a sick patient). Other times, a false alarm is worse (wrongful conviction: don't punish the innocent).

**Precision** measures how often your "Guilty" verdict is correct. **Recall** measures how many actual criminals you caught. **F1 Score** tells you if you've struck the right balance between the two.

Today, you will learn to read this balance and tune it for any real-world situation.

---

## What's Next — After This Session, You Will Be Able To

- Explain why **accuracy is a misleading metric** on its own, and give a real example of when it completely fails.
- Build and interpret a **Decision Tree** — read its rules, understand which features it relies on most, and control its complexity using `max_depth`.
- Understand why a **Random Forest** (many trees voting together) almost always outperforms a single tree.
- Compute **Precision, Recall, and F1 Score** from scratch and know exactly which one matters most in a given business problem.
- Read a **ROC-AUC curve** and use the AUC score to compare models without choosing any threshold at all.
- **Tune the decision threshold** to meet a specific business requirement — like "we must catch at least 90% of failing students, even if it means some extra false alerts."
- Produce a **full model comparison table** across three classifiers — Logistic Regression, Decision Tree, and Random Forest — using five metrics at once.

---

## The Curiosity Gap — Questions We Will Answer in the Live Session

1. **A model has 95% accuracy but an AUC score of exactly 0.50 — how is that possible, and what does it mean about the model?** The answer will permanently change how you evaluate any model you build.

2. **If you lower a model's decision threshold from 0.5 to 0.3, what happens to Precision and Recall — and why would a doctor or a banker ever want to do that?**

3. **Why does a Random Forest with 100 trees almost always beat a single Decision Tree — even when that single tree has perfect training accuracy?** The answer connects to one of the most important ideas in all of machine learning.

Come to the session ready to compare three models side by side, read a ROC curve, and make your first threshold tuning decision. By the end, you will never look at an accuracy score the same way again.
