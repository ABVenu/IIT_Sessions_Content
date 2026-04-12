# Pre-read: Predicting Real Numbers — Linear Regression in Plain Words

## The hook

Apps and businesses constantly need a **specific number**, not just a yes/no label: the cab fare in rupees, minutes until delivery, next month’s electricity bill, or a flat’s asking price. Those answers live on a scale—you are not only sorting things into boxes, you are **measuring** something. Making that kind of prediction from past examples is a core data-science skill and shows up in analytics roles, product decisions, and anywhere people ask, “What value should we expect next?”

## The problem

**What if** you had to set **hundreds** of fares, scores, or prices by gut feeling alone—or by staring at a spreadsheet until your eyes hurt? **What if** each case had several clues (distance, time of day, study hours) and you had to combine them **fairly** so new situations still worked? Doing it by hand does not scale, and guessing the “right” weights for each clue is exactly where humans get tired and inconsistent. You need a simple, repeatable rule that **learns from history** and still behaves sensibly on **new** rows you have never seen.

## The solution preview

The hero of this session is **linear regression**—the idea that we can predict a number using a **straight-line style rule**: start from a **baseline**, then add a bit for each clue, where the computer learns those “bits” from data. We will see how this differs from **classification** (pick a category like spam vs not spam). We will name the **target** (the number you want) and **features** (the clues). We will train a model with **scikit-learn**—`fit` to learn, `predict` to use—and talk honestly about **overfitting**, **underfitting**, and **generalisation**. We will end with **residuals** (gap between actual and predicted) as a way to read whether the model is fair or biased.

## A simple analogy from the session

The notes use a **taxi meter**: a **base fare** plus so many rupees **per kilometre**. Linear regression learns something similar from data—a **starting level** (**intercept**) and a **rate per unit** for each feature (**coefficient**), like “about this many extra marks per study hour.” Another image from class: plot students as dots (hours vs score) and imagine a **straight line** through the cloud—the **best-fit line** is the one where the **vertical gaps** from dots to line are as small as possible overall. Those gaps are the **errors** the model tries to shrink when it trains.

## In plain words

- **Regression:** Predict a **continuous number** (price, marks, minutes)—not just a label from a fixed list.
- **Classification:** Pick a **category** (“this” or “that”). If the answer must be a measurement on a scale, you are in regression territory.
- **Target:** The **answer column** you want to predict. **Features:** The **input clues** the model may use.
- **Overfitting:** The model **memorised** training noise; it looks great on old rows and worse on fresh ones—like memorising past papers instead of the idea.
- **Underfitting:** The rule is **too simple**; it misses real patterns even on training data.
- **Residual:** For one row, **actual minus predicted**—whether you were too high or too low. Patterns in residuals tell you if something is wrong.

If we use a technical word in class, we will pin it down with examples like these.

## Questions we will crack in class

1. How does the computer find the **intercept** and **coefficients** from many past examples, and what is really happening inside **`.fit()`** before **`.predict()`** runs on a new student or new house?
2. How can a **train–test split** show whether the model **generalises** or has slipped into **overfitting**—and why is “perfect on training data” not the real goal?
3. What story do **residuals** tell—balanced noise versus systematic bias, outliers, and clues that your straight-line model might be missing?

## After this session, you will be able to

- Tell **regression** apart from **classification** and spot when a “number” column is really a **disguised category**.
- Explain **target**, **features**, **intercept**, and **coefficient** using the taxi-meter or marks-per-hour picture.
- Outline the **train → fit → predict** workflow in **scikit-learn** and why feature tables are shaped the way the library expects.
- Describe **underfitting**, the **sweet spot**, and **overfitting**, and why practitioners split data to check **generalisation**.
- Compute and interpret **residuals** at a high level and list the **three diagnostic questions** the notes give for reading them.

Bring a fresh notebook mindset—we connect intuition, a few lines of Python, and the habit of checking whether predictions hold up beyond the rows the model already saw.
