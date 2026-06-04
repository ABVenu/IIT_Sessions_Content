# Objective Assignment - Unsupervised Learning: Clustering and Dimensionality Reduction

## Instructions
- Total questions: 10
- Question types: 6 MCQs (single correct), 4 MSQs (multiple correct)
- Difficulty progression: Easy → Moderate → Hard

---

## MCQs (Single Correct)

### Q1 (Easy)
QuickMart has purchase data for 8,000 shoppers (features only, no segment labels). The marketing team wants natural buyer groups for targeted offers. Which learning type fits this task?

A. Supervised classification  
B. Unsupervised clustering  
C. Reinforcement learning  
D. Semi-supervised regression  

**Correct Answer:** B  
**Explanation:** Grouping unlabeled data by similarity is unsupervised clustering (e.g. K-Means). Supervised methods need a known target column (A). Reinforcement (C) and regression (D) do not match this segmentation goal.

---

### Q2 (Easy)
In K-Means, what does a **centroid** represent?

A. The row with the highest feature value in the dataset  
B. The mean position of all points assigned to that cluster  
C. The label column used during training  
D. The distance between two different clusters  

**Correct Answer:** B  
**Explanation:** A centroid is the average of points in its cluster and is updated each iteration. It is not necessarily an actual data row (A), not a label (C), and not inter-cluster distance (D).

---

### Q3 (Easy)
Before running K-Means on features like `time_spent` (minutes) and `money_spent` (rupees), why is **StandardScaler** recommended?

A. It adds a target column automatically  
B. It puts features on comparable scales so distance is fair  
C. It guarantees the elbow always occurs at K = 3  
D. It removes the need to choose K  

**Correct Answer:** B  
**Explanation:** Features on different units can dominate Euclidean distance without scaling. Scaling does not create labels (A), fix K (C), or remove the K choice (D).

---

### Q4 (Easy)
Which scenario is a valid **unsupervised** use case?

A. Predict loan default using past default labels  
B. Group similar songs for playlist recommendations without genre labels  
C. Train a model to predict exam Pass/Fail from study hours  
D. Maximize click reward in an ad-bidding game  

**Correct Answer:** B  
**Explanation:** Recommendation-style grouping without item labels is unsupervised. A and C need labeled targets (supervised). D describes reinforcement learning.

---

### Q5 (Moderate)
A delivery app plots drivers at point **P (2, 3)**. Centroids are **A (1, 1)** and **B (5, 5)** (Euclidean distance). Which centroid is **P** assigned to in the assign step?

A. A  
B. B  
C. Both equally  
D. Neither until the next epoch only  

**Correct Answer:** A  
**Explanation:** Distance to A: √[(2−1)² + (3−1)²] = √5 ≈ 2.24. Distance to B: √[(2−5)² + (3−5)²] = √18 ≈ 4.24. P is closer to A.

---

### Q6 (Moderate)
In sklearn, `kmeans.inertia_` after fitting is best described as:

A. The number of features in the dataset  
B. Within-cluster sum of squared distances (WCSS) for that clustering  
C. The accuracy compared to hidden labels  
D. The learning rate used during optimization  

**Correct Answer:** B  
**Explanation:** Inertia is WCSS — total squared distance of points to their assigned centroids. It is not feature count (A), supervised accuracy (C), or a learning rate (D).

---

## MSQs (Multiple Correct)

### Q7 (Moderate)
Which statements about the **K-Means** loop are correct?

A. Each point is assigned to the nearest centroid.  
B. Centroids are updated to the mean of points in their cluster.  
C. The algorithm requires a labeled target column `y` during `fit`.  
D. Steps assign and update repeat until convergence.  

**Correct Answers:** A, B, D  
**Explanation:** K-Means uses only features: `fit(X)` without `y`, so C is wrong. A, B, and D describe the standard assign–update loop.

---

### Q8 (Moderate)
A data scientist clusters credit-card customers with **no fraud labels**. Which statements are correct?

A. `KMeans.fit(X)` uses features only.  
B. Train/test split in the supervised sense is not the primary evaluation pattern here.  
C. Precision/recall against a hidden `y` is mandatory to run clustering.  
D. Anomaly detection can be related to finding unusual points in unlabeled data.  

**Correct Answers:** A, B, D  
**Explanation:** Clustering does not need labels (C is false). A and B match unsupervised practice; D aligns with anomaly use cases mentioned for unlabeled data.

---

### Q9 (Hard)
QuickMart runs an **elbow plot** of WCSS vs K (K = 1 to 10). Which conclusions are valid?

A. WCSS generally decreases as K increases.  
B. Setting K equal to the number of rows gives WCSS = 0 but is not useful.  
C. The elbow suggests where adding more clusters gives diminishing improvement.  
D. A flat WCSS curve from K = 1 to K = 10 always means K = 1 is optimal.  

**Correct Answers:** A, B, C  
**Explanation:** More clusters reduce WCSS (A). One cluster per point gives zero WCSS but no meaningful segments (B). The elbow is the practical bend (C). A flat drop is unrealistic; D is wrong.

---

### Q10 (Hard)
A team has **10 customer metrics** per row and wants a **2D scatter** plus **K-Means** on compressed data. Which steps are appropriate?

A. Apply `StandardScaler` before PCA.  
B. Fit PCA with `n_components=2` on scaled data.  
C. Pass the original 10 raw columns directly to PCA without scaling when units differ widely.  
D. Run `KMeans` on the 2D PCA output, then visualize clusters in that plane.  

**Correct Answers:** A, B, D  
**Explanation:** Scale → PCA(2) → K-Means on reduced data is the taught pipeline. Skipping scaling when features have different scales (C) can distort PCA and distances.

---
