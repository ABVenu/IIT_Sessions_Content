# Post Class Quiz — Session 32: Unsupervised Learning: Clustering and Dimensionality Reduction

---

**Q1 (Multiple Choice — Single Correct)**

Which of the following best describes unsupervised learning?

- A) Training a model on labeled data to predict a known output
- B) Using reward signals to train an agent through trial and error
- C) Finding hidden patterns and groupings in data that has no predefined labels
- D) Building a classifier using human-annotated examples

**Answer:** C

---

**Q2 (Multiple Choice — Single Correct)**

In K-Means clustering, what is a centroid?

- A) The data point with the largest feature value in a cluster
- B) The boundary line drawn between two clusters
- C) A randomly chosen data point that stays fixed throughout training
- D) The calculated mean position of all points currently assigned to a cluster

**Answer:** D

---

**Q3 (Multiple Choice — Single Correct)**

The Elbow Method is used to determine the optimal value of K in K-Means. What does the "elbow" point on the WCSS vs K curve indicate?

- A) The K value at which WCSS is highest
- B) The K value beyond which adding more clusters gives diminishing improvement in WCSS
- C) The K value where all data points are equidistant from their centroids
- D) The K value equal to the number of features in the dataset

**Answer:** B

---

**Q4 (Multiple Choice — Single Correct)**

If PC1 in a PCA analysis has an explained variance ratio of 0.72, what does this mean?

- A) 72% of all data points were assigned to the first principal component
- B) PC1 was computed using 72% of the original features
- C) PC1 alone captures 72% of the total information (variance) present in the original dataset
- D) The model achieves 72% accuracy after dimensionality reduction

**Answer:** C

---

**Q5 (Multiple Choice — Multiple Correct)**

Which of the following are correct steps in the K-Means clustering algorithm? *(Select all that apply)*

- A) Choose the number of clusters K before the algorithm starts
- B) Assign each data point to the nearest centroid using Euclidean distance
- C) Recalculate each centroid as the mean of all points currently in that cluster
- D) Use labeled class information to guide the cluster assignments

**Answer:** A, B, C

> D is incorrect — K-Means is unsupervised and does not use labels.

---

**Q6 (Multiple Choice — Multiple Correct)**

Which of the following statements about Principal Component Analysis (PCA) are correct? *(Select all that apply)*

- A) PCA requires features to be standardized before it is applied
- B) The first principal component (PC1) captures the least variance in the data
- C) Each principal component is orthogonal (perpendicular) to all other principal components
- D) PCA reduces the number of features while preserving as much variance as possible

**Answer:** A, C, D

> B is incorrect — PC1 captures the *most* variance; each subsequent component captures progressively less.

---

**Q7 (Multiple Choice — Multiple Correct)**

Why is combining PCA with K-Means considered a powerful approach? *(Select all that apply)*

- A) PCA removes noisy and redundant features, making K-Means distance calculations more meaningful
- B) PCA assigns cluster labels to each data point before K-Means runs
- C) After clustering, reducing data further to 2D with PCA allows the clusters to be visualized on a standard scatter plot
- D) Running K-Means on PCA-reduced data is faster than on the original high-dimensional data

**Answer:** A, C, D

> B is incorrect — PCA does not assign cluster labels. Cluster label assignment is the job of K-Means.

---
