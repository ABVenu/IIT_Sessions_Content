# Pre-read: Unsupervised Learning — Clustering and Dimensionality Reduction

Imagine you just joined a new company as a data analyst. On your very first day, your manager drops a spreadsheet on your desk — 5,00,000 rows of customer records. Purchase history, browsing time, how much money they spend, when they log in, what they click on. And your manager says: **"Tell me who our customers really are."**

There is no cheat sheet. No one has gone through these 5 lakh rows and tagged each customer as "budget buyer" or "premium buyer." Nobody has labelled anything. It is just raw, unlabelled data sitting there, waiting to be understood.

Now ask yourself — how would you even begin to make sense of it?

---

## The Challenge Nobody Talks About

In the sessions so far, we have been working with data that already had answers attached to it. You had a set of house features → and the price was already there. You had emails → and someone had already marked them spam or not spam. The machine's job was to learn from those existing answers and predict new ones.

But the real world is messier than that.

Most data in the world has **no labels**. Think about it:

- A hospital has lakhs of patient scans — but nobody has sat down and classified each one.
- A music app has crores of songs — but no human has manually grouped them by "mood."
- A bank has millions of transactions — but nobody has marked every single one as "normal" or "suspicious."

Labelling data is expensive. It takes time, money, and human expertise. So what happens when you have to find patterns in data where nobody has done the labelling for you?

That is the exact problem this session is built to solve.

---

## Enter the Machine That Figures Things Out on Its Own

What if you could hand all 5,00,000 customer records to a computer program and say: **"You figure out who is similar to whom"** — and the computer actually did it, accurately, in seconds?

That is not science fiction. That is **Unsupervised Learning** — a branch of machine learning where the algorithm discovers hidden groupings and patterns in data **without any labels or pre-defined answers**.

Think of it like walking into a brand new grocery store. Nobody gives you a map or a guide. But within minutes, you naturally figure out where things are — fruits near the entrance, dairy at the back, snacks in the middle. Your brain grouped things together based on similarity. Unsupervised learning teaches a machine to do exactly this, but at a scale no human ever could.

In this session, we focus on two specific tools that make this possible.

The first is **K-Means Clustering** — an algorithm that automatically splits your data into groups (called clusters) based on how similar data points are to each other. Imagine a wedding event manager who has to arrange 500 guests into tables. He groups family members together, college friends together, office colleagues together — without being told who belongs where. K-Means does this for data, automatically, using math.

The second is **PCA (Principal Component Analysis)** — which stands for a technique that compresses data with too many details into a simpler form, without losing what matters most. Think of it like compressing a 48-megapixel photograph into a smaller file. The photo still looks almost identical, but it takes far less space and is much easier to work with. PCA does the same thing to data — it compresses 30 or 50 features down to 2 or 3, so you can actually visualize and understand what is happening.

---

## Why This Is a Game-Changer for Your Career

Every major company running today — Swiggy, Amazon, Spotify, Netflix, your bank — uses unsupervised learning in the background, every single day.

- When Netflix recommends shows you did not know you would love — that is clustering.
- When your bank flags a weird transaction at 3 AM — that is anomaly detection powered by clustering.
- When Spotify builds a "Daily Mix" playlist that feels eerily perfect — that is grouping similar songs together without anyone manually labelling them.
- When a hospital uses AI to group patient scans for research — PCA helps compress thousands of measurements into something a model can actually learn from.

Understanding these two tools puts you in a position where you can work with real, unlabelled, messy data — which is honestly 90% of what the data world actually looks like.

---

## In this pre-read, you'll discover:

- What **Unsupervised Learning** is and how it is fundamentally different from everything we have done before
- How **K-Means Clustering** works step by step — from randomly placing starting points to finally converging on stable groups
- How to find the **right number of clusters** without guessing, using a technique called the Elbow Method
- What **PCA** does, why high-dimensional data is a problem, and how PCA compresses information without throwing away what matters
- How **PCA and K-Means work together** as a pipeline — one reduces complexity, the other finds structure, and together they turn messy data into clear insights

---

## What You Will Be Able to Do After This Session

- Take any unlabelled dataset and use K-Means to automatically group similar records together
- Use the Elbow Method to smartly choose how many groups to create
- Apply PCA to compress a dataset with 30 or 50 features into 2D so you can actually see it on a graph
- Combine PCA + K-Means in a single workflow — a technique used in real data science projects at top companies
- Look at a customer dataset and identify meaningful segments, ready to present to a business team

---

## Think About These Before the Session

The live session will answer these — but try to think about them first. They will make the concepts click much faster when you see them explained:

1. **The Sorting Puzzle:** You have 1,000 songs and zero information about their genre or mood — just raw audio features like tempo, loudness, and rhythm. How would you group similar songs together? What would "similar" even mean here, and how many groups would you make?

2. **The Compression Question:** A student's academic profile has 40 different test scores — math, physics, chemistry, English, history, and 35 more subjects. If you had to summarise this student using just 2 numbers that still captured most of what makes them unique, what would those 2 numbers represent? Is it even possible to do this without losing important information?

3. **The K Problem:** Imagine you are running K-Means to segment customers. You try K = 2 groups, then K = 5, then K = 20. At what point are you creating too many groups that are meaningless? How would you know when to stop?

These are not trick questions — they are exactly the problems K-Means and PCA were designed to solve. Come to the session ready to see how the algorithm cracks each one.
