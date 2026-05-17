# Pre-read: Leakage & Imbalance

Imagine your college announces a **surprise mock test** tomorrow. You open last year’s paper, study hard, and score **92%**. On the real exam day, the questions are completely different—and you barely pass. You did not suddenly become weaker overnight. You accidentally **studied with the answer key in your bag**. The high score felt real, but it was **misleading**.

Now picture a **fraud detection team** at a bank. Out of one million transactions in a month, only **fifty** are actual fraud. A lazy system that labels *everything* as “not fraud” would still be **99.995% accurate**—and completely useless. The rare cases are exactly what matter, yet they are drowned out by the crowd.

These two stories sit at the heart of today’s session. You have already learned how to **clean messy data** and **hold some rows aside** to check whether a model is learning properly. The next step is learning why models can still **look brilliant on paper and fail in real life**—and what to do when the world is **unfairly stacked** toward one outcome.

---

## When Good Scores Lie

Last session, you saw how important it is to **split data before you “teach” your cleanup rules** to the training portion only. That was an early taste of **data leakage**—letting information from the **test** side sneak into **training**, like revising from tomorrow’s question paper.

But leakage has other disguises too:

> **What if** you scale every column using the **average of the full dataset**—including rows you promised to hide for testing?  
> **What if** you remove duplicates **before** splitting, and the same customer appears in both train and test?  
> **What if** a column secretly contains the answer—like “loan approved = yes” sitting next to “defaulted = no” when your job is to predict default **before** approval?

Each mistake can make a model look like a genius in the lab and a fool on the shop floor. Today you will learn a **guard workflow**: split first, preprocess with rules learned only from training data, lock away the test set, and simulate **real prediction conditions**—as if the future has not happened yet.

---

## When “Accurate” Is Not Enough

Think of a village health camp screening for a **rare disease** that affects 1 in 500 people. A screening tool that always says “healthy” is **correct 499 times out of 500**—and **misses every sick person**. Doctors care about **who got wrongly cleared** and **who got wrongly alarmed**, not just the headline percentage.

That skew—when one class heavily outnumbers another—is called **class imbalance**. Models trained on such data often **chase the majority** because that is the easy way to look good on simple accuracy. You will see why **accuracy alone** can fool managers and why we need gentler ideas like **precision** (when we say “fraud,” how often are we right?) and **recall** (of all real fraud cases, how many did we catch?)—explained with everyday stories, not formulas.

We will also peek at practical responses: **oversampling** (giving the rare group more voice), **undersampling** (trimming the loud majority), and **synthetic data**—creating **new, artificial but realistic** examples so the minority is not ignored (the intuition behind methods like **SMOTE**, without diving into heavy code). Each choice has trade-offs, and you will learn to discuss them like a thoughtful builder, not just a button-clicker.

---

## One Split Is Not the Whole Truth

Finally, imagine judging a cricket player’s form from **a single match** on a tricky pitch. Maybe they were unlucky once—or the conditions were odd. **Cross-validation** is the idea of **playing several short matches** (different train-test splits), checking performance each time, and **averaging** the results so you trust the score more. One lucky split should not decide your entire faith in a model.

Together, **leakage guards**, **imbalance awareness**, and **cross-validation** form a triangle: if any corner is weak, you may celebrate a model that **cannot be trusted** when real users depend on it.

---

Think of building a trustworthy model like **preparing for a board exam with sealed mock papers**. You prepare using **old papers only**. You never peek at the **final exam paper** while studying. If one subject has very few questions in your practice set, you **add more practice** for that subject instead of ignoring it. And you do **more than one mock test** before you tell your parents you are “fully ready.” That is the spirit of today’s tools—fair splits, honest evaluation, and respect for rare but important cases.

---

**In this pre-read, you'll discover:**

- **Why** data leakage creates **fake success**—and how everyday choices (scaling, deduplication, feature selection) can leak the answer without you noticing
- **How** class imbalance skews learning toward the majority—and why **accuracy** can hide dangerous blind spots in fraud, medicine, and quality checks
- **What** precision and recall mean in plain language—linking them to **false alarms** vs **missed catches** you already understand from daily life
- **How** oversampling, undersampling, and **synthetic** balancing ideas help—and why **cross-validation** gives a steadier picture than a single lucky split

---

## Ideas Worth Knowing Before We Go Live

**Data leakage** — Using information during training that would **not be available** at real prediction time (future facts, test-set statistics, or columns that encode the answer). It inflates scores and breaks trust.

**Split before preprocess** — Decide which rows are for learning vs checking **first**, then fit cleaning and scaling **only on the training portion**, and apply the same learned rules to the test portion—like writing mock papers before the final.

**Class imbalance** — When one label (e.g., “not fraud”) appears far more often than another (e.g., “fraud”). The model may learn to **always guess the crowd favourite**.

**Precision (intuition)** — Of everything we flagged as positive, **how many were truly positive?** Fewer false alarms.

**Recall (intuition)** — Of all real positives in the world, **how many did we find?** Fewer missed cases.

**Oversampling / undersampling** — Adding copies of rare rows or reducing common rows so both sides get a fair hearing—each with costs (noise vs lost information).

**Synthetic data (high level)** — Generating **new, similar** minority examples rather than only duplicating existing ones—helping balance without pretending the dataset never had a skew.

**Cross-validation** — Repeating train-test evaluation across **multiple splits** and averaging performance—so one odd split does not fool you.

---

## Questions We Will Answer in the Live Session

1. **The leakage trap:** You scale numeric columns using the mean of **all** rows, then split into train and test. Why might your test score look **too good**—and what is the correct order of operations?

2. **The fraud puzzle:** Out of 10,000 transactions, only 20 are fraud. A model predicts “not fraud” every time and reports **99.8% accuracy**. Why is this model **useless**—and which matters more for the bank: catching fraud or avoiding false alarms?

3. **The stability check:** Model A scores 95% on one random split and 62% on another; Model B scores 78% on five different splits. Why might **cross-validation** make you trust Model B more—even though 95% sounds higher?

---

## After This Session, You Will Be Able To

- **Explain** data leakage in your own words and **spot** common leakage scenarios in a typical ML workflow  
- **Apply** a split-first, train-only preprocessing mindset that mirrors **real-world prediction**  
- **Describe** class imbalance with relatable examples and **why** accuracy alone can mislead stakeholders  
- **Discuss** precision and recall as trade-offs between **false positives** and **false negatives**—without relying on formulas  
- **Compare** basic imbalance strategies (oversampling, undersampling, synthetic balancing) at a **conceptual** level  
- **Introduce** cross-validation as a way to **stabilise** performance estimates and connect leakage, imbalance, and evaluation into one honest story  

See you in class. The gap between a model that **impresses in a notebook** and one that **works for real people** often comes down to the guardrails you build today—not the fanciest algorithm name on the slide.
