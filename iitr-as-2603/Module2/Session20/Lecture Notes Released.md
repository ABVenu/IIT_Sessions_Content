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
| Examples | Spam detection, loan default | Customer segments, recommendations, anomaly flags |
| Evaluation | Compare to true labels | Harder — no single “correct” label |

- Supervised = student with an **answer key**. Unsupervised = explorer drawing regions on a map with **no legend**.
- In clustering you typically use **`model.fit(X)`** only — there is **no `y`**, and there is **no train/test split** in the same way as supervised models.
- Labels are expensive or impossible in many domains — unsupervised is the practical starting point.

![Supervised learning uses labels and a clear target; unsupervised learning finds hidden groups in unlabeled data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-supervised-vs-unsupervised.png)

**Common uses in practice:**

- **Customer segmentation** — group shoppers by spend, visits, or product mix for targeted campaigns.
- **Recommendation systems** — Netflix or Spotify group similar movies/songs so “users who liked X also liked Y” feels natural.
- **Anomaly detection** — flag unusual transactions or logins when no fraud labels exist yet.

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
- **Real-Life Example:** Retail customers plotted by **time spent** vs **money spent** — three blobs become three segments for marketing (budget shoppers, regulars, high spenders).

**Cluster** — points close to each other, far from other groups. **Centroid** — average position of the cluster (may not be an actual row); it summarizes “typical” behaviour in that group.

![Each cluster is a group of similar points; the centroid (often marked with an X) is the mean position of that group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-clusters-centroids.png)

**Why K-Means:** Fast and scalable for segmentation at scale. **Limitation:** you must choose **K** in advance.

---

## K-Means Workflow

![K-Means loop: pick K, initialize centroids, assign each point to the nearest center, recompute the mean, repeat until stable](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-workflow-loop.png)

| Step | What happens |
|---|---|
| 1. Choose **K** | How many segments you want (e.g. 3 customer types) |
| 2. **Initialize** centroids | Random starting positions (algorithm refines them) |
| 3. **Assign** each point | Label = nearest centroid (usually **Euclidean distance**) |
| 4. **Update** centroids | Move each center to the **mean** of its points |
| 5. **Repeat** 3–4 | Until assignments/centroids stop moving (**convergence**) |

- Wrong **K** too small → unlike things lumped together; too large → tiny, meaningless groups.
- Distance needs comparable feature scales — **scale before K-Means**.

**Choosing K — two practical approaches:**

1. **Domain knowledge** — if the business needs “budget / regular / premium” segments, start with **K = 3**.
2. **Elbow method** — plot **WCSS** (within-cluster sum of squares; called **inertia** in sklearn) vs K and pick where the curve **bends** and gains flatten.

**Elbow Method:**

- **Official Definition:** Plot **WCSS** vs K; the **elbow** is where adding clusters barely helps.
- **In Simple Words:** More K always shrinks WCSS — pick K where the curve bends and gains flatten.
- **Mistake:** K = number of rows → each point its own cluster, WCSS = 0, useless.

![Elbow method: plot WCSS (inertia) vs K; the bend (elbow) suggests a good trade-off before gains flatten out](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-elbow-method-wcss.png)

### Quick Activity — Nearest Centroid

Point **P** at (2, 3). Centroids: **A** (1, 1), **B** (5, 5). Which cluster?

**Answer:** **A** — Euclidean distance to A is smaller.

---

## Code: K-Means with Elbow and Customer Segmentation

Each row is a **customer**; features are **time spent** (minutes) and **money spent** (rupees). There is **no target column** — only **X**.

```python
import numpy as np  # numeric arrays for features
import matplotlib.pyplot as plt  # plots for elbow and clusters
import pandas as pd  # table of customer features
from sklearn.cluster import KMeans  # K-Means clustering model
from sklearn.preprocessing import StandardScaler  # scale features before distance

# Build a small customer table (replace with your CSV in practice)
data = pd.DataFrame({
    "time_spent": [12, 45, 8, 30, 55, 10, 48, 52, 9, 40, 15, 50],
    "money_spent": [200, 1500, 180, 900, 1600, 220, 1400, 1550, 190, 1100, 250, 1450],
})
X = data[["time_spent", "money_spent"]].values  # features only — no y
X_scaled = StandardScaler().fit_transform(X)  # fair scale for distance

wcss = []  # store inertia for each K
for k in range(1, 11):  # try K from 1 to 10 (elbow search)
    km = KMeans(n_clusters=k, random_state=42)  # build model with k clusters
    km.fit(X_scaled)  # fit on X only — no labels
    wcss.append(km.inertia_)  # WCSS = within-cluster sum of squares

plt.figure(figsize=(7, 4))  # elbow plot
plt.plot(range(1, 11), wcss, marker="o")  # inertia vs K
plt.xlabel("K")  # number of clusters
plt.ylabel("WCSS (inertia)")  # error within clusters
plt.title("Elbow Method")  # find the bend
plt.tight_layout()
plt.show()

kmeans_final = KMeans(n_clusters=3, random_state=42)  # optimal K from elbow (example: 3)
labels = kmeans_final.fit_predict(X_scaled)  # cluster id per customer
centroids = kmeans_final.cluster_centers_  # final cluster centers

plt.figure(figsize=(7, 5))  # scatter of segments
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap="viridis", s=80, alpha=0.8)
plt.scatter(centroids[:, 0], centroids[:, 1], s=250, c="red", marker="X", label="Centroids")
plt.xlabel("Scaled time spent")
plt.ylabel("Scaled money spent")
plt.legend()
plt.title("K-Means customer segments (K=3)")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **`StandardScaler`** — puts features on comparable scale so distance is fair.
- **`km.fit(X_scaled)`** — no **`y`**; clustering learns only from features.
- **`inertia_`** — WCSS for that K; used in the elbow loop (inertia and WCSS mean the same thing here).
- **`labels_` / `fit_predict`** — cluster id (0, 1, 2, …) per row; **`cluster_centers_`** — final centroids.

---

## Interpreting Clusters for Business Decisions

After K-Means, each row gets a **cluster label** — not a prediction of Pass/Fail, but a **group id**.

- Look at **centroids** on the original scale (or plot): e.g. cluster 0 = low time & low money (budget), cluster 1 = high on both (premium).
- Name segments for stakeholders: “occasional shoppers,” “loyal mid-tier,” “high-value” — this turns math into **actionable marketing**.
- **Recommendation angle:** items or songs in the same cluster get suggested together (Netflix rows, Spotify playlists).

### Quick Activity — Read a Segment

Cluster centroid averages: **A** — time 15 min, money ₹300; **B** — time 50 min, money ₹1,400. Which label fits **B**?

**Answer:** High-engagement, high-spend segment (e.g. “premium” or “loyal high-value”).

---

## PCA: Fewer Features, Most of the Information

When data has **many columns** (e.g. 10 customer metrics or 30 medical measurements), you cannot plot or reason in all dimensions at once. **PCA** compresses many original features into **a few summary directions** so you can see structure in 2D.

**High-dimensional intuition:** A digit image can be **784 pixels** (28×28) — each pixel is a feature. PCA can compress that into 2–3 summary directions so similar digits cluster visually (same idea as reducing 30 credit-card features to 2 for a scatter plot).

**PCA (Principal Component Analysis):**

- **Official Definition:** A method to **reduce the number of feature columns** by building new **summary directions** from standardized data that keep the main patterns in the rows.
- **In Simple Words:** Replace many correlated measurements with 2–3 combined “summary lines” that still separate groups when you plot them.
- **Real-Life Example:** A detailed photo saved as a smaller file — it looks almost the same but is easier to share. PCA compresses **feature columns**, not pixels.

- The **first summary direction** catches the biggest spread in the data; the **second** catches the next biggest pattern, at a right angle to the first.
- Before you trust a 2D plot, look at the scatter: do groups still form clear clouds? Heavy overlap often means the 2D view dropped too much detail.
- Summary directions are **mixtures** of original columns — you usually cannot say “this axis = age only.”
- Always **scale** first (same rule as K-Means).

![PCA turns many original features into a few summary directions so you can plot in 2D](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-highd-to-2d.png)

- You do **not** need to do the math by hand — `PCA()` in sklearn builds the summary directions for you.

---

## Code: PCA on Many Features and 2D Plot

**Part A — simulated 10-feature data** (matches the in-class demo: compress 10 columns → 2 for plotting).

```python
import numpy as np  # random feature matrix
import pandas as pd  # table with 10 feature columns
import matplotlib.pyplot as plt  # 2D scatter after PCA
from sklearn.preprocessing import StandardScaler  # scale before PCA
from sklearn.decomposition import PCA  # dimensionality reduction

np.random.seed(42)  # reproducible demo data
n_rows = 200  # number of samples
X = np.random.randn(n_rows, 10)  # 10 features per row
df = pd.DataFrame(X, columns=[f"feature_{i+1}" for i in range(10)])  # named columns

X_scaled = StandardScaler().fit_transform(df.values)  # scale every feature
pca_2d = PCA(n_components=2)  # keep 2 summary directions
X_pca = pca_2d.fit_transform(X_scaled)  # reduced table for plotting

plt.figure(figsize=(7, 5))  # explore structure in 2D
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7, s=40)
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.title("10 features → 2D summary plot")
plt.tight_layout()
plt.show()
```

**Part B — breast cancer dataset (30 features):** same pattern; **labels used only to color the plot**, not to fit PCA (supervised labels for **visual check** only).

```python
from sklearn.datasets import load_breast_cancer  # built-in 30-feature dataset

data = load_breast_cancer()
X = data.data
y = data.target  # malignant vs benign — for colors only, not for fitting PCA
X_scaled = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_scaled)

plt.figure(figsize=(7, 5))
plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], c="red", alpha=0.6, label="Malignant")
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], c="blue", alpha=0.6, label="Benign")
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.legend()
plt.title("30 features → 2D (check class separation)")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **`StandardScaler`** — fair scaling before PCA (same idea as before K-Means).
- **`PCA(n_components=2).fit_transform`** — returns a new table with 2 summary columns for plotting.
- **Breast cancer `y`** — colors show if malignant/benign **separate** in 2D; PCA itself did not use labels.

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

**Typical pipeline:** Scale → PCA (e.g. to 2 components) → K-Means → plot in 2D. K-Means on fewer, denoised dimensions is often faster and more stable.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.random.randn(300, 10)  # 10 features — cannot plot raw
df = pd.DataFrame(X, columns=[f"feature_{i+1}" for i in range(10)])

X_scaled = StandardScaler().fit_transform(df.values)
X_pca = PCA(n_components=2).fit_transform(X_scaled)  # df_pca-style reduced data
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])

labels = KMeans(n_clusters=3, random_state=42).fit_predict(df_pca.values)  # cluster in 2D

plt.figure(figsize=(7, 5))
plt.scatter(df_pca["PC1"], df_pca["PC2"], c=labels, cmap="tab10", s=50, alpha=0.8)
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.title("K-Means on PCA-reduced data (10D → 2D)")
plt.colorbar(label="Cluster")
plt.tight_layout()
plt.show()
```

**How the code works:**

- **10 features** — simulates “many columns, can’t plot raw.”
- **`fit_predict` on `df_pca`** — clusters in 2D space found by PCA (same flow as in-class: PCA first, then K-Means).
- **Color = cluster id** — sanity check that groups look separated.

---

## Key Takeaways

- **Unsupervised learning** finds structure **without labels** — segmentation, recommendations, and anomaly exploration when tagging is costly.
- **K-Means** alternates **assign to nearest centroid** and **recompute mean** until stable; choose **K** with **domain knowledge** and/or the **elbow** on **inertia (WCSS)**; use **`fit(X)`** only; always **scale** first.
- **Interpret clusters** with centroid stories (time vs money, product mix) so results are usable for business and recommendations.
- **PCA** turns many columns into **summary directions** for plotting; check whether groups still separate in 2D before you trust the picture.
- **PCA + K-Means + 2D plot** is a common workflow: compress, cluster, visualize.

Next you will connect these ideas to broader ML workflows and upcoming topics on agents and embeddings.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What it means | Why it matters |
|---|---|---|
| **Unsupervised learning** | No target labels | Discovery and segmentation |
| **Cluster** | Group of similar points | Output of K-Means |
| **Centroid** | Mean position of a cluster | Assignment target; business “average customer” |
| **K** | Number of clusters | Domain knowledge or elbow |
| **WCSS / inertia** | Within-cluster sum of squared distances | Elbow plot y-axis; same idea as inertia in sklearn |
| **Elbow method** | Pick K at curve bend | Practical K selection |
| **Domain knowledge** | Business sense of how many segments | First way to set K |
| **Convergence** | Centroids/labels stop changing | K-Means stopping condition |
| **Recommendation system** | Suggest similar items/users | Classic unsupervised-style grouping |
| **Anomaly detection** | Find rare/outlier points | Unsupervised when labels missing |
| **PCA** | Principal Component Analysis | Reduce many columns to few summary directions |
| **Summary direction** | Combined axis from original features | Used for 2D plots and clustering |
| **`KMeans(n_clusters=K)`** | Clustering model | `sklearn.cluster`; `fit(X)` only |
| **`kmeans.labels_` / `cluster_centers_`** | Assignments and centers | After `fit` or `fit_predict` |
| **`kmeans.inertia_`** | WCSS | Elbow method |
| **`PCA(n_components=n)`** | Keep n summary directions | `sklearn.decomposition` |
| **`fit_transform`** | Fit PCA and return reduced table | One-step compression for plotting |
| **`StandardScaler`** | Mean 0, std 1 | Required before K-Means & PCA |

---
