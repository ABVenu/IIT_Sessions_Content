# Assignment: Unsupervised Learning — Clustering and Dimensionality Reduction

## Objective Assignment

**Total Questions: 10 | Format: MCQ (Single Correct) and MSQ (Multiple Correct)**
**Order: Easy → Moderate → Hard**

---

### Question 1 — MCQ (Easy)

Riya, a data analyst at a food delivery startup, has 50,000 order records but no category labels attached to them. She wants the system to automatically identify patterns and groupings in this data. Which type of machine learning is best suited for her task?

- A) Supervised Learning — because it is faster and more accurate
- B) Reinforcement Learning — because it rewards good groupings
- C) Unsupervised Learning — because the data has no labels and she wants to discover hidden patterns
- D) Semi-supervised Learning — because the orders are partially labeled

**Correct Answer: C**

**Answer Explanation:**
Unsupervised Learning is specifically designed for datasets that have no labels. The goal is to discover hidden patterns, structures, and groupings in unlabeled data — exactly what Riya needs. Supervised learning requires labeled data with a known target output. Reinforcement learning works through reward signals in interactive environments. Semi-supervised learning uses a mix of labeled and unlabeled data, which doesn't apply here since Riya has no labels at all.

---

### Question 2 — MCQ (Easy)

In K-Means clustering, after all data points are assigned to their nearest centroid, the algorithm needs to update the centroid positions. Which mathematical operation is used to recalculate each centroid?

- A) Median of all feature values across the cluster
- B) Maximum of all feature values across the cluster
- C) Mean (average) of all feature values across the cluster
- D) Mode of the most frequent feature values in the cluster

**Correct Answer: C**

**Answer Explanation:**
The name "K-Means" itself encodes the answer — K clusters, each updated using the **mean**. In Step 4 of the K-Means workflow, every centroid is moved to the arithmetic mean (average) position of all data points currently assigned to it. This is why centroids gradually drift to the true center of their group with each iteration. Options A, B, and D (median, maximum, mode) are not used in standard K-Means and would give incorrect centroid positions.

---

### Question 3 — MCQ (Easy)

A K-Means model is trained on a retail dataset with K=3. After 15 iterations, the centroids stop moving and no data point switches to a different cluster. What has occurred?

- A) The model has overfit to the training data
- B) The model ran out of memory during computation
- C) The model has converged
- D) The model reached its iteration limit before completing training

**Correct Answer: C**

**Answer Explanation:**
**Convergence** in K-Means is the state where centroids no longer shift between iterations and every data point remains in its current cluster assignment. This is the natural, successful stopping condition of the algorithm. Overfitting is a concept from supervised learning (not applicable here). Running out of memory would cause an error. Reaching a maximum iteration limit is a safety stop — convergence is different because it means the algorithm has genuinely completed its job.

---

### Question 4 — MCQ (Easy)

A developer trains a K-Means model on 1,000 product records and notices that every time she reruns the code, the cluster assignments change slightly. Which approach best reduces this inconsistency?

- A) Using `init='random'` for maximum diversity across runs
- B) Increasing the number of clusters K to reduce variability
- C) Using `init='k-means++'` which intelligently places initial centroids far apart from each other
- D) Using a larger dataset so randomness has less impact

**Correct Answer: C**

**Answer Explanation:**
The inconsistency happens because K-Means randomly initializes centroid positions, which can lead to different local optima on different runs. **K-Means++** solves this by choosing initial centroids that are spread far apart from each other, making a poor random start far less likely. Using `init='random'` is precisely what causes the inconsistency. Increasing K or using more data does not address the initialization problem directly.

---

### Question 5 — MCQ (Moderate)

An e-commerce company applies the Elbow Method to their customer dataset and records the following WCSS values:

| K | WCSS |
|---|------|
| 1 | 950 |
| 2 | 520 |
| 3 | 210 |
| 4 | 190 |
| 5 | 185 |

Based on this data, which value of K should the company choose?

- A) K=1, because it has the highest WCSS and represents the full dataset
- B) K=5, because it gives the lowest WCSS and is therefore the most precise
- C) K=3, because the drop from K=3 to K=4 is very small (only 20), indicating the "elbow"
- D) K=2, because the largest single drop occurs between K=1 and K=2

**Correct Answer: C**

**Answer Explanation:**
The Elbow Method works by finding the **point of diminishing returns** — where adding more clusters gives almost no improvement in WCSS. Looking at the data: K=1→2 drops by 430, K=2→3 drops by 310, K=3→4 drops by only 20, K=4→5 drops by only 5. The sharp flattening after K=3 marks the "elbow." Choosing K=5 would over-segment the data into too many fine-grained, potentially meaningless groups. The lowest WCSS (option B) is always at K = number of data points, which is useless.

---

### Question 6 — MCQ (Moderate)

Arjun is building a K-Means clustering model on a hospital patient dataset with three features: `age (20–70 years)`, `blood_pressure (60–130 mmHg)`, and `blood_glucose (70–450 mg/dL)`. He skips feature scaling and runs K-Means directly. What is the most likely consequence?

- A) The clustering will work correctly since K-Means handles different scales internally
- B) The algorithm will throw a runtime error because features are not normalized
- C) The `blood_glucose` feature will dominate the distance calculations due to its larger numerical scale, skewing cluster assignments
- D) The model will always converge to exactly K=1 cluster

**Correct Answer: C**

**Answer Explanation:**
K-Means assigns points using **Euclidean distance**. A feature with large numerical values (blood_glucose: 70–450) will contribute far more to the distance calculation than a feature with small values (age: 20–70), regardless of actual importance. This creates a distorted "distance landscape" where clusters are shaped primarily by blood_glucose and largely ignore age and blood pressure. `StandardScaler` must be applied before K-Means to bring all features to mean=0 and std=1, ensuring equal contribution. The algorithm will not throw an error — it will silently produce biased results.

---

### Question 7 — MSQ (Moderate)

Which of the following statements about K-Means clustering are TRUE? (Select all that apply)

- A) K must be specified by the user before the algorithm begins training
- B) K-Means uses Euclidean distance to assign each data point to the nearest centroid
- C) Different random centroid initializations can lead to different final cluster assignments
- D) K-Means always finds the globally optimal clustering solution for any dataset

**Correct Answers: A, B, C**

**Answer Explanation:**
- **A — TRUE:** K is a hyperparameter that must be manually set before running K-Means. This is its well-known limitation — the user must decide K in advance.
- **B — TRUE:** Euclidean distance (straight-line distance between two points) is the standard distance metric used in K-Means to determine which centroid a point is closest to.
- **C — TRUE:** Since centroids are initialized randomly, different starting positions can lead to convergence at different local optima, producing slightly different cluster assignments.
- **D — FALSE:** K-Means converges to a **local optimum**, not necessarily the global best solution. The result heavily depends on how the initial centroids were placed. This is why strategies like K-Means++ and multiple restarts (`n_init`) exist.

---

### Question 8 — MSQ (Moderate)

A data science team is deciding whether to use supervised or unsupervised learning for several business problems. Which of the following problems are best addressed using **unsupervised learning**? (Select all that apply)

- A) Segmenting 80,000 users of a streaming app into groups based on listening patterns — no predefined category list exists
- B) Detecting network traffic anomalies that don't match any previously seen patterns in a system with no labeled attack data
- C) Predicting whether a bank customer will default on a loan using historical records labeled "defaulted" or "not defaulted"
- D) Automatically organizing 20,000 scientific research papers into topic clusters without manually reading them

**Correct Answers: A, B, D**

**Answer Explanation:**
- **A — CORRECT:** No predefined categories + discovering hidden groupings = unsupervised learning (customer segmentation use case).
- **B — CORRECT:** Anomaly detection without labeled examples of attacks is a classic unsupervised task — finding data points that don't fit known patterns.
- **C — INCORRECT:** Historical records with "defaulted / not defaulted" labels make this a **supervised** classification problem.
- **D — CORRECT:** Grouping thousands of documents by topic without pre-defined categories is document clustering — an unsupervised learning task.

---

### Question 9 — MSQ (Hard)

A data team runs the Elbow Method on a dataset of 600 customer records, testing K from 1 to 15. Which of the following statements about their analysis are correct? (Select all that apply)

- A) WCSS will always decrease (or stay the same) as K increases from 1 to 15
- B) If K is set to 600 — equal to the number of data points — WCSS will be 0, but the clustering result will be completely useless
- C) The optimal K is always the one that gives WCSS = 0
- D) The "elbow" in the WCSS plot represents the point where the benefit of adding more clusters becomes negligible

**Correct Answers: A, B, D**

**Answer Explanation:**
- **A — CORRECT:** As K increases, each cluster gets smaller and more concentrated around fewer points, so the total within-cluster distance (WCSS) can only decrease or stay the same — never increase.
- **B — CORRECT:** When K = number of data points, every point is its own cluster, giving a trivially perfect WCSS of 0. But this is meaningless — there is no grouping; you have just described every point individually.
- **C — INCORRECT:** WCSS = 0 occurs only at K = n_samples, which is the worst possible useful model. The optimal K balances low WCSS with meaningful, manageable clusters.
- **D — CORRECT:** The elbow is precisely the point of diminishing returns — beyond it, adding one more cluster barely reduces WCSS, meaning those extra clusters aren't worth the added complexity.

---

### Question 10 — MSQ (Hard)

Priya is working on a medical research dataset with **40 health features** collected from 3,000 patients. She decides to apply PCA before running K-Means clustering. Which of the following statements about PCA in this context are correct? (Select all that apply)

- A) PCA creates new features called Principal Components that are mathematical combinations of all the original 40 features
- B) After PCA, Priya can label the first Principal Component as "cholesterol" or "BMI" since PCA selects the most important original feature
- C) PCA helps address the Curse of Dimensionality by compressing 40 features into fewer representative dimensions
- D) Reducing the 40 features to 2 Principal Components allows Priya to visualize all 3,000 patients on a standard 2D scatter plot

**Correct Answers: A, C, D**

**Answer Explanation:**
- **A — CORRECT:** Principal Components are **linear combinations** of all original features — each PC blends information from every feature according to mathematically optimized weights.
- **B — INCORRECT:** This is a common misconception. PCA does **not** select or isolate individual original features. Principal Components are abstract mathematical summaries and cannot be named after original features like "cholesterol" or "BMI." They are not directly human-interpretable.
- **C — CORRECT:** Reducing 40 dimensions to a smaller set is a direct solution to the Curse of Dimensionality, where too many features make distances between points nearly meaningless.
- **D — CORRECT:** Reducing to 2 PCs allows plotting every data point on a 2D X-Y chart (PC1 on X-axis, PC2 on Y-axis) — making otherwise invisible high-dimensional structure visually accessible to humans.
