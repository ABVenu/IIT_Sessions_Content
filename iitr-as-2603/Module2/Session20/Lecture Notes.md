# Unsupervised Learning: Clustering and Dimensionality Reduction

## Context of This Session

In the previous session, you worked in **supervised learning** — labeled targets (Pass/Fail), **Decision Trees**, **Random Forest**, and metrics like **precision**, **recall**, and **ROC-AUC**. The model always had an answer key to learn from.

Many real datasets have **no labels** — only features. This session introduces **unsupervised learning**: finding **groups** with **K-Means** and compressing many columns with **PCA** so you can see structure in 2D.

**In this session, you will:**

- Contrast **unsupervised** vs **supervised** learning
- Run **K-Means** (centroids, assign–update loop, choosing **K**)
- Use **PCA** to reduce dimensions and **visualize** high-dimensional data
- Combine **scale → PCA → K-Means** in a short pipeline

---

## Unsupervised Learning Basics

**Unsupervised Learning:**

- **Official Definition:** Machine learning on data **without labeled outputs**; the algorithm discovers structure (groups, patterns, compression).
- **In Simple Words:** You give rows of features only — the model finds who looks similar, without being told Pass/Fail.
- **Real-Life Example:** 10,000 shoppers with purchase history but no “segment” label — the algorithm groups night electronics buyers vs sale-day buyers for marketing.

| | **Supervised** | **Unsupervised** |
|---|---|---|
| Labels? | Yes (target column) | No |
| Goal | Predict known output | Discover hidden structure |
| Examples | Spam detection, loan default | Customer segments, anomaly flags |
| Evaluation | Compare to true labels | Harder — no single “correct” label |

- Supervised = student with an **answer key**. Unsupervised = explorer drawing regions on a map with **no legend**.
- Labels are expensive or impossible in many domains — unsupervised is the practical starting point.

![Supervised learning uses labels and a clear target; unsupervised learning finds hidden groups in unlabeled data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-supervised-vs-unsupervised.png)

**Common uses:** customer segmentation, fraud/anomaly outliers, document topic grouping, image compression summaries.

### Quick Activity — Supervised or Unsupervised?

Write **S** or **U**:

1. Group news articles by topic with no topic labels given  
2. Predict house price from size and location  
3. Find unusual credit-card transactions with no fraud labels  
4. Predict student Pass/Fail from study hours  

**Answers:** 1 → U, 2 → S, 3 → U, 4 → S.

---

## K-Means Clustering: Group Similar Points

**K-Means:**

- **Official Definition:** Partitions data into **K** non-overlapping clusters by assigning each point to the nearest **centroid** (cluster center), then updating centroids as the mean of assigned points, until stable.
- **In Simple Words:** Pick K group “headquarters,” assign everyone to the nearest HQ, move HQ to the group average, repeat until assignments stop changing.
- **Real-Life Example:** Wedding seating — family, office, college friends end up at tables where people are most alike. K-Means does that for numeric features.

**Cluster** — points close to each other, far from other groups. **Centroid** — average position of the cluster (may not be an actual row).

![Each cluster is a group of similar points; the centroid (often marked with an X) is the mean position of that group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-clusters-centroids.png)

**Why K-Means:** Fast and scalable for segmentation at scale. **Limitation:** you must choose **K** in advance.

---

## K-Means Workflow

![K-Means loop: pick K, initialize centroids, assign each point to the nearest center, recompute the mean, repeat until stable](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-workflow-loop.png)

| Step | What happens |
|---|---|
| 1. Choose **K** | How many segments you want (e.g. 3 customer types) |
| 2. **Initialize** centroids | Random positions ( **`k-means++`** spreads starts better) |
| 3. **Assign** each point | Label = nearest centroid (usually **Euclidean distance**) |
| 4. **Update** centroids | Move each center to the **mean** of its points |
| 5. **Repeat** 3–4 | Until assignments/centroids stop moving (**convergence**) |

- Wrong **K** too small → unlike things lumped together; too large → tiny, meaningless groups.
- Distance needs comparable feature scales — **scale before K-Means**.

**Elbow Method (choosing K):**

- **Official Definition:** Plot **WCSS** (within-cluster sum of squares, called **inertia** in sklearn) vs K; the **elbow** is where adding clusters barely helps.
- **In Simple Words:** More K always shrinks WCSS — pick K where the curve bends and gains flatten.
- **Mistake:** K = number of rows → each point its own cluster, WCSS = 0, useless.

![Elbow method: plot WCSS (inertia) vs K; the bend (elbow) suggests a good trade-off before gains flatten out](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-elbow-method-wcss.png)

### Quick Activity — Nearest Centroid

Point **P** at (2, 3). Centroids: **A** (1, 1), **B** (5, 5). Which cluster?

**Answer:** **A** — Euclidean distance to A is smaller.

---

## Code: K-Means with Elbow and Plot

`make_blobs` builds synthetic grouped points (good for learning — no CSV needed).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=42)
X_scaled = StandardScaler().fit_transform(X)

wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, init="k-means++", random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("K")
plt.ylabel("WCSS (inertia)")
plt.title("Elbow Method")
plt.tight_layout()
plt.show()

kmeans_final = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=42)
kmeans_final.fit(X_scaled)
labels = kmeans_final.labels_
centroids = kmeans_final.cluster_centers_

plt.figure(figsize=(7, 5))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap="viridis", s=50, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], s=250, c="red", marker="X", label="Centroids")
plt.legend()
plt.title("K-Means (K=3)")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **`StandardScaler`** — puts features on comparable scale so distance is fair.
- **`inertia_`** — WCSS for that K; used in the elbow loop.
- **`labels_`** — cluster id (0, 1, 2, …) per row; **`cluster_centers_`** — final centroids.
- **`n_init=10`** — runs multiple random inits, keeps best result.

---

## PCA: Fewer Features, Most of the Information

When data has **many columns** (e.g. 30 tumour measurements), you cannot plot or reason in all dimensions at once. **PCA** compresses many original features into **a few summary directions** so you can see structure in 2D.

**PCA (Principal Component Analysis):**

- **Official Definition:** A method to **reduce the number of feature columns** by building new **summary directions** from standardized data that keep the main patterns in the rows.
- **In Simple Words:** Replace 30 correlated measurements with 2–3 combined “summary lines” that still separate patients when you plot them.
- **Real-Life Example:** A detailed photo saved as a smaller file — it looks almost the same but is easier to share. PCA compresses **feature columns**, not pixels.

- The **first summary direction** catches the biggest spread in the data; the **second** catches the next biggest pattern, at a right angle to the first.
- Before you trust a 2D plot, look at the scatter: do groups still form clear clouds? Heavy overlap often means the 2D view dropped too much detail.
- Summary directions are **mixtures** of original columns — you usually cannot say “this axis = age only.”
- PCA works best when relationships are roughly straight; very curved patterns may need other tools later.
- Always **scale** first (same rule as K-Means).

![PCA turns many original features into a few summary directions so you can plot in 2D](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-highd-to-2d.png)

- You do **not** need to do the math by hand — `PCA()` in sklearn builds the summary directions for you.

---

## Code: PCA on Many Features and 2D Plot

Breast cancer dataset (built into sklearn): **569 rows**, **30 features**, labels only for **coloring** the plot (supervised labels used for visualization, not for fitting PCA).

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset: many feature columns per patient
data = load_breast_cancer()
X = data.data
y = data.target  # labels used only for plot colors, not for fitting PCA
print(f"Original shape: {X.shape}")

# Scale every feature column to mean 0 and std 1
X_scaled = StandardScaler().fit_transform(X)

# Keep 2 summary directions so we can plot in 2D
pca_2d = PCA(n_components=2)
X_pca = pca_2d.fit_transform(X_scaled)

# Scatter plot: color by true class to see if groups separate
plt.figure(figsize=(7, 5))
plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], c="red", alpha=0.6, label="Malignant")
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], c="blue", alpha=0.6, label="Benign")
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.legend()
plt.title("30 features → 2D summary plot")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **`load_breast_cancer()`** — 569 rows and 30 feature columns; too many to plot directly.
- **`StandardScaler`** — fair scaling before PCA (same idea as before K-Means).
- **`PCA(n_components=2).fit_transform`** — returns a new table with 2 summary columns for plotting.
- **Colors use `y`** only to see if malignant/benign **separate** in 2D — PCA itself did not use labels.

### Quick Activity — Read the PCA Plot

If malignant (red) and benign (blue) form two clouds with little overlap, what does that suggest?

**Answer:** The main signal in 30 features is preserved in 2D — a classifier on original or PCA features may work well; heavy overlap means the problem stays hard even after PCA.

---

## PCA Visualization and PCA + K-Means Pipeline

**Reading a 2D PCA scatter:**

- **Close points** were similar in the original high-dimensional space.
- **Separated clouds** → strong structure; **overlap** → hard to separate classes or clusters.
- Use PCA for **exploration** and sometimes **speed** before clustering — not a replacement for thinking about business meaning of raw features.

![Typical pipeline: scale high-dimensional data, use PCA to reduce dimensions, then run K-Means and visualize in 2D](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-kmeans-pipeline.png)

**Typical pipeline:** Scale → PCA (e.g. to 2 or 10 components) → K-Means → plot in 2D. K-Means on fewer, denoised dimensions is often faster and more stable.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=500, centers=4, n_features=5, random_state=42)
X_scaled = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_scaled)

labels = KMeans(n_clusters=4, init="k-means++", random_state=42).fit_predict(X_pca)

plt.figure(figsize=(7, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="tab10", s=50, alpha=0.8)
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.title("K-Means on 2D summary plot (5D data)")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **5D `make_blobs`** — simulates “many columns, can’t plot raw.”
- **`fit_predict` on `X_pca`** — clusters in 2D space found by PCA.
- **Color = cluster id** — check if four groups look separated (sanity check when true K is 4).

---

## Key Takeaways

- **Unsupervised learning** finds structure **without labels** — segmentation, anomalies, exploration when tagging is costly.
- **K-Means** alternates **assign to nearest centroid** and **recompute mean** until stable; choose **K** with the **elbow** on **inertia (WCSS)**; always **scale** first.
- **PCA** turns many columns into **summary directions** for plotting and faster work; check whether groups still separate in 2D before you trust the picture.
- **PCA + K-Means + 2D plot** is a common workflow: compress, cluster, visualize.
- Next you will connect these ideas to broader ML workflows (pipelines, feature work, and more model families).

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Unsupervised learning** | No target labels | Discovery and segmentation |
| **Cluster** | Group of similar points | Output of K-Means |
| **Centroid** | Mean position of a cluster | Assignment target |
| **K** | Number of clusters | Must be chosen (elbow helps) |
| **WCSS / inertia** | Sum of squared distances to centroids | Elbow plot y-axis |
| **Elbow method** | Pick K at curve bend | Practical K selection |
| **Convergence** | Centroids/labels stop changing | K-Means stopping condition |
| **PCA** | Principal Component Analysis | Reduce many columns to a few summary directions |
| **Summary direction** | Combined axis built from original features | Used for 2D plots and clustering |
| **`KMeans(n_clusters=K)`** | Clustering model | `sklearn.cluster` |
| **`kmeans.labels_` / `cluster_centers_`** | Assignments and centers | After `fit` |
| **`kmeans.inertia_`** | WCSS | Elbow method |
| **`PCA(n_components=n)`** | Keep n summary directions | `sklearn.decomposition` |
| **`fit_transform`** | Fit PCA and return reduced table | One-step compression for plotting |
| **`StandardScaler`** | Mean 0, std 1 | Required before K-Means & PCA |
| **`make_blobs`** | Synthetic clustered data | Teaching / demos |

---
