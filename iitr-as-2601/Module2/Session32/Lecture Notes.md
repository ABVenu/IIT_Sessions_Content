# Unsupervised Learning: Clustering and Dimensionality Reduction

## What You Will Learn in This Session

In the previous session, we explored **supervised learning** — specifically how machines learn to classify things when we already give them labeled data. We built **Decision Trees** and **Random Forests**, and we measured their performance using metrics like **Accuracy, Precision, Recall, F1 Score, and ROC-AUC**. We even learned how to tune the decision threshold to balance between catching true positives and avoiding false alarms.

But what happens when you don't have labels? What if you have a huge pile of data — customer records, images, medical scans — and nobody has sat down and tagged each row with an answer?

That is exactly where **Unsupervised Learning** comes in. In this session, you will learn:

- What unsupervised learning is and why it exists
- How **K-Means Clustering** works to group similar data points together
- The step-by-step workflow behind K-Means
- What **PCA (Principal Component Analysis)** is and why we need it
- How to use PCA to visualize high-dimensional data in 2D

---

## Introduction to Unsupervised Learning

Think about the last time you walked into a new grocery store. Nobody handed you a map with labels. You just started observing — fruits are near the entrance, dairy is at the back, snacks are in the middle aisle. You **grouped things in your mind** based on similarity without anyone telling you where each category was.

This is exactly what **Unsupervised Learning** does.

**Official Definition:** Unsupervised Learning is a type of machine learning where the model is trained on data that has **no labels or pre-defined outputs**. The algorithm finds hidden patterns, structures, or groupings in the data on its own.

**In Simple Words:** You give the machine a bunch of data without telling it what anything means. The machine figures out on its own which items are similar and groups them together.

**Real-Life Example:** Imagine you have 10,000 customer records from an e-commerce site — purchase history, browsing time, average spend. You do not know anything about these customers yet. An unsupervised algorithm will look at all these records and say: "These 3,000 people behave similarly — they buy electronics late at night. These 4,000 people buy during sales. Let us call them Group A, B, C." This is **customer segmentation** — a real business use case.

---

### Supervised vs. Unsupervised: The Key Difference

Before going deeper, let us understand the fundamental difference between the two types of learning.

| Feature | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Labels in data? | Yes | No |
| Goal | Predict a known output | Discover hidden patterns |
| Examples | Email spam detection, loan approval | Customer segmentation, anomaly detection |
| Evaluation | Easy — compare prediction to true label | Harder — no "correct" answer to compare |

- In **supervised learning**, you are like a student with an answer key. You study from solved examples.
- In **unsupervised learning**, you are like an explorer with a map but no legend. You discover the meaning of things yourself.
- This is why unsupervised learning is especially powerful when collecting labeled data is expensive or impossible.

![Supervised learning uses labels and a clear target; unsupervised learning finds hidden groups in unlabeled data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-supervised-vs-unsupervised.png)

---

### Where Is Unsupervised Learning Used?

Unsupervised learning is everywhere in the real world. Here are common applications:

- **Customer Segmentation:** Group customers into buckets based on buying behavior (used heavily in marketing).
- **Anomaly Detection:** Find transactions that don't fit any normal pattern (used in banking to detect fraud).
- **Document Grouping:** Automatically sort thousands of news articles into topics without reading them all.
- **Gene Expression Analysis:** In medical research, finding which genes behave similarly in patients.
- **Image Compression:** Reduce the complexity of images without losing important visual information.

---

## K-Means Clustering — Grouping Similar Data Points

Now that we understand what unsupervised learning is, let us meet its most popular algorithm: **K-Means Clustering**.

**Official Definition:** K-Means is an unsupervised machine learning algorithm that partitions a dataset into **K distinct, non-overlapping clusters** based on feature similarity. Each data point belongs to the cluster whose center (called a **centroid**) is closest to it.

**In Simple Words:** Imagine you have a room full of people. You want to split them into K groups based on how similar they are. K-Means does exactly that — it keeps rearranging people until each group makes the most sense.

**Real-Life Example:** Think of K-Means like a seating arrangement at a wedding. You have 100 guests. The event manager groups them — family members together, office colleagues together, college friends together. The guests in each group are most "similar" to each other compared to guests in other groups. K-Means does this for data automatically.

---

### What Is a Cluster and What Is a Centroid?

These are the two most important words in K-Means. Let us understand each one clearly.

- **Cluster:** A group of data points that are similar to each other. Points within a cluster are close to each other and far from points in other clusters.
- **Centroid:** The center point of a cluster. Think of it as the "average" or "representative" of the whole group. It may or may not be an actual data point — it is a calculated position.

**Real-Life Example:** Imagine 5 friends living in different parts of Mumbai. If they want to meet at a central location, they pick a place that is roughly equidistant for all — that meeting point is the **centroid**. The 5 friends and that central location together form a **cluster**.

![Each cluster is a group of similar points; the centroid (often marked with an X) is the mean position of that group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-clusters-centroids.png)

---

### Why K-Means? What Problem Does It Solve?

Before K-Means, if you had 10,000 customer records, you would have to manually go through them and group them — which is impossible at scale.

- K-Means automates the grouping process using math, making it possible to handle millions of records.
- It is **fast and scalable**, which is why it is the first choice for clustering tasks in real businesses.
- However, K-Means requires you to decide **K** (the number of clusters) in advance — this is its main limitation, and we will address how to handle that.

---

## K-Means Workflow — Step by Step

Understanding K-Means deeply requires walking through its algorithm step by step. Think of it as a process of iterative improvement.

**The core idea:** K-Means assigns each point to the nearest centroid, then recalculates centroids based on the current groupings, and repeats this until nothing changes.

![K-Means loop: pick K, initialize centroids, assign each point to the nearest center, recompute the mean, repeat until stable](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-kmeans-workflow-loop.png)

---

### Step 1 — Choose the Number of Clusters (K)

The very first step is deciding how many groups you want. This number is called **K**.

- If you are segmenting customers, maybe K = 3 (Budget buyers, Mid-range buyers, Premium buyers).
- If you are grouping cities by climate, maybe K = 5 (very hot, hot, moderate, cold, very cold).
- **Choosing the wrong K** is the most common mistake. If K is too small, very different things end up in the same group. If K is too large, you get too many tiny meaningless groups.

---

### Step 2 — Initialize Centroids Randomly

After choosing K, the algorithm places K centroids at **random positions** in the data space.

- Think of it like this: You throw K pins randomly on a map. These are your starting "group headquarters."
- These initial positions are random, so different runs of K-Means may give slightly different results — this is a known quirk of the algorithm.
- A smarter initialization method called **K-Means++** picks initial centroids that are spread far apart, reducing the chance of a bad random start.

---

### Step 3 — Assign Each Point to the Nearest Centroid

Now the algorithm goes through every single data point and asks: **"Which centroid am I closest to?"**

- Distance is usually measured using **Euclidean Distance** — the straight-line distance between two points in space.
- Each point gets a label: "I belong to Centroid 1," "I belong to Centroid 2," etc.
- **Doubt:** What if a point is equally close to two centroids? In practice, a tiebreak rule assigns it to one arbitrarily.

**Real-Life Analogy:** Imagine you are in a city with 3 hospitals. Every neighbourhood goes to whichever hospital is closest. Each hospital now serves a cluster of neighbourhoods.

---

### Step 4 — Recalculate the Centroid of Each Cluster

After all points are assigned to their nearest centroid, the centroid position is **recalculated** as the mean (average) of all points in that cluster.

- The centroid moves to the true center of its group.
- This is why the algorithm is called **K-Means** — it uses the **mean** of K groups.
- Think of it as: the hospital moves its location to the actual geographic center of all the neighbourhoods it serves, to minimize travel time for everyone.

---

### Step 5 — Repeat Until Convergence

Steps 3 and 4 are repeated again and again. Each time:

- Points may switch to a different centroid if a centroid has moved closer to them.
- Centroids keep moving to the true center of their updated groups.
- Eventually, the centroids stop moving and assignments stop changing. This is called **convergence**.

**When does K-Means stop?**

- When centroids do not move between iterations (full convergence).
- Or when a maximum number of iterations is reached (a safety limit).

---

### Visualizing K-Means in Action

Let us imagine a simple 2D example:

```
Before K-Means:
● ● ○ ○ △ △
(All mixed together, no groups)

After K-Means (K=3):
[Cluster A: ● ●]   [Cluster B: ○ ○]   [Cluster C: △ △]
(Each shape found its own group)
```

- The algorithm discovered the 3 natural groups without being told they existed.
- In real data, points are in many dimensions, not just 2D — but the logic is exactly the same.

---

### How to Choose the Right K — The Elbow Method

Since K must be chosen manually, we need a smart way to pick it. The most popular technique is the **Elbow Method**.

**Official Definition:** The Elbow Method plots the **Within-Cluster Sum of Squares (WCSS)** — the total distance of each point from its centroid — against different values of K. The "elbow" in the curve (the point where improvement slows down drastically) is the optimal K.

**In Simple Words:** As K increases, clusters get smaller and more precise, so the total distance drops. But after a point, adding more clusters gives almost no improvement — that sweet spot is your K.

- **WCSS** is also called **Inertia** in scikit-learn.
- If the elbow is at K = 3, it means 3 clusters explain the data structure well without being unnecessarily complex.
- **Common Mistake:** Picking K = the total number of data points. Then each point is its own cluster — WCSS = 0, but completely useless.

![Elbow method: plot WCSS (inertia) vs K; the bend (elbow) suggests a good trade-off before gains flatten out](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-elbow-method-wcss.png)

---

### Implementing K-Means in Python

Let us now build a K-Means model from scratch using Python and scikit-learn.

**About the Dataset We Are Using — `make_blobs`**

- `make_blobs` is a **synthetic data generator** built into scikit-learn. It creates artificial data points that are naturally grouped into clusters — perfect for learning and testing clustering algorithms.
- Think of it like a teacher drawing dots on a whiteboard in 3 separate groups and saying: "Now tell me — can your algorithm find these 3 groups?" We control how many points, how many groups, and how spread out each group is.
- Since this data is **generated by code**, no CSV file or download is needed. One line of code creates the entire dataset instantly.

```python
# Import necessary libraries
import numpy as np                          # For numerical operations
import pandas as pd                         # For data handling
import matplotlib.pyplot as plt             # For plotting graphs
from sklearn.cluster import KMeans          # K-Means algorithm from scikit-learn
from sklearn.datasets import make_blobs     # To generate sample clustered data
from sklearn.preprocessing import StandardScaler  # To scale the features

# -------------------------------------------------------
# Step 1: Generate sample data with 3 natural clusters
# -------------------------------------------------------
X, y_true = make_blobs(
    n_samples=300,      # Create 300 data points
    centers=3,          # Data will have 3 natural cluster centers
    cluster_std=0.60,   # How spread out each cluster is
    random_state=42     # Fixing seed for reproducibility
)

# -------------------------------------------------------
# Step 2: Scale the data (very important for K-Means)
# -------------------------------------------------------
scaler = StandardScaler()   # Initialize the scaler
X_scaled = scaler.fit_transform(X)  # Scale all features to mean=0, std=1

# -------------------------------------------------------
# Step 3: Apply the Elbow Method to find the best K
# -------------------------------------------------------
wcss = []                        # List to store WCSS values for each K

for k in range(1, 11):           # Try K from 1 to 10
    kmeans = KMeans(
        n_clusters=k,            # Number of clusters for this trial
        init='k-means++',        # Smart initialization to avoid bad random starts
        random_state=42          # Fixing seed for consistent results
    )
    kmeans.fit(X_scaled)         # Train K-Means on the scaled data
    wcss.append(kmeans.inertia_) # Save the WCSS (inertia) score

# Plot the Elbow curve
plt.figure(figsize=(8, 5))                   # Set figure size
plt.plot(range(1, 11), wcss, marker='o')     # Plot K vs WCSS
plt.title('Elbow Method — Finding Optimal K') # Chart title
plt.xlabel('Number of Clusters (K)')          # X-axis label
plt.ylabel('WCSS (Inertia)')                  # Y-axis label
plt.tight_layout()                            # Adjust layout
plt.show()                                    # Display the chart

# -------------------------------------------------------
# Step 4: Train K-Means with the optimal K = 3
# -------------------------------------------------------
kmeans_final = KMeans(
    n_clusters=3,        # We chose K=3 from the Elbow Method
    init='k-means++',    # Smart initialization
    n_init=10,           # Run 10 times with different random seeds, pick the best
    random_state=42      # Fixing seed for reproducibility
)
kmeans_final.fit(X_scaled)                    # Fit the model on scaled data

# -------------------------------------------------------
# Step 5: Get the cluster labels for each data point
# -------------------------------------------------------
labels = kmeans_final.labels_                 # Each point gets a cluster number: 0, 1, or 2
centroids = kmeans_final.cluster_centers_     # The final centroid coordinates

# -------------------------------------------------------
# Step 6: Visualize the clusters
# -------------------------------------------------------
plt.figure(figsize=(8, 6))                    # Set figure size
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 1],           # X and Y coordinates
    c=labels,                                  # Color each point by its cluster label
    cmap='viridis',                            # Color palette
    s=50,                                      # Size of each point
    alpha=0.7                                  # Slight transparency
)
plt.scatter(
    centroids[:, 0], centroids[:, 1],          # Plot centroids
    s=300,                                      # Make centroids larger
    c='red',                                    # Color centroids red
    marker='X',                                 # Use X marker for centroids
    label='Centroids'                           # Label for legend
)
plt.title('K-Means Clustering Result (K=3)')  # Chart title
plt.legend()                                   # Show legend
plt.tight_layout()                             # Adjust layout
plt.show()                                     # Display the chart
```

**How the code works:**

- We generate synthetic data with 3 natural clusters using `make_blobs`.
- We **scale the data** first — this is critical because K-Means uses distance, and features on different scales would distort distances.
- We loop through K values 1–10 and record the WCSS (inertia) to plot the Elbow curve.
- We train the final model with K = 3 and extract the **labels** (which cluster each point belongs to) and **centroids** (the center of each cluster).
- The scatter plot colors each point by its cluster and marks centroids with red X markers.

---

## PCA — Principal Component Analysis

So far, K-Means clusters data. But what happens when your data has **50 features, or 100 features**? You cannot visualize or even intuitively understand such data. That is where **PCA** comes in.

**Official Definition:** PCA (Principal Component Analysis) is a **dimensionality reduction** technique that transforms a dataset with many features into a smaller set of new features called **Principal Components**, while preserving as much of the original information (variance) as possible.

**In Simple Words:** Imagine you have a student's profile with 50 different test scores. PCA compresses those 50 scores into maybe 2 or 3 "summary scores" that still capture most of what makes that student unique. You lose a little detail but gain the ability to visualize and process the data easily.

**Real-Life Example:** Think of a photo from a 48-megapixel camera. It is huge and detailed. Now you save it in a compressed format — the image looks almost identical but takes much less space. PCA is the mathematical equivalent of this compression, applied to data features.

---

### Why Do We Need PCA?

The problem PCA solves is called the **Curse of Dimensionality**.

- When data has too many features (dimensions), models get confused because everything looks equally far from everything else.
- Visualizing data in more than 3 dimensions is **impossible** for humans.
- Many features are often **correlated** — for example, "height in cm" and "height in inches" carry the same information. PCA collapses such redundancies.
- Reducing dimensions speeds up model training and often **improves model performance** by removing noise.

---

### Key Concept: Variance and Why It Matters

Before understanding PCA, you need to understand **variance**.

**Official Definition:** Variance is a statistical measure of how spread out data points are from their mean (average). High variance means data is spread widely; low variance means data is clustered tightly.

**In Simple Words:** If 10 students scored 85, 86, 87, 88, and 89 — very low variance. If they scored 20, 45, 60, 80, 95 — high variance. High variance means more information is being captured.

- PCA finds the directions in your data where **variance is highest** — those are the most informative directions.
- These directions are called **Principal Components**.

---

### What Are Principal Components?

**Official Definition:** A Principal Component is a **new axis (direction)** in the data space that captures the maximum variance. The first principal component captures the most variance, the second captures the next most, and so on. Each component is **orthogonal** (perpendicular) to all others.

**In Simple Words:** Imagine your data points are scattered on a table. PCA finds the direction along which the points are spread out the most — that is PC1. Then it finds the next direction (at 90°) that captures the second-most spread — that is PC2. These new directions become your new axes.

- **PC1** always captures the most variance.
- **PC2** captures the next most, and so on.
- The original features no longer exist — they are replaced by these new summary components.

![PCA projects high-dimensional data onto new axes (PC1, PC2, …) that capture the most variance, enabling 2D plots](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-highd-to-2d.png)

---

### The PCA Process Step by Step

PCA follows a mathematical process. Let us understand it conceptually without getting lost in heavy math.

**Step 1 — Standardize the Data**
- PCA is sensitive to the scale of features. A feature measured in rupees (thousands) would dominate a feature measured in kilograms.
- We use **StandardScaler** to bring all features to the same scale (mean = 0, standard deviation = 1).

**Step 2 — Compute the Covariance Matrix**
- PCA looks at how features **relate to each other** (covariance).
- If "age" and "income" both increase together, they have high covariance.
- The covariance matrix captures all pairwise relationships between features.

**Step 3 — Find Eigenvectors and Eigenvalues**
- This is the mathematical core of PCA.
- **Eigenvectors** tell us the **directions** of maximum variance (these become the Principal Components).
- **Eigenvalues** tell us **how much variance** each direction captures.
- Directions with higher eigenvalues are more important.

**Step 4 — Select Top Components**
- Sort components by their eigenvalue (highest first).
- Choose the top N components that together explain enough variance (typically 90–95%).
- Discard the rest.

**Step 5 — Transform the Data**
- Project the original data onto the selected Principal Components.
- The output is a new dataset with fewer dimensions but most of the original information preserved.

---

### Explained Variance Ratio

This is the key metric in PCA that tells you how much information each component holds.

**Official Definition:** The **Explained Variance Ratio** of a principal component is the proportion of the total variance in the dataset that it accounts for.

**In Simple Words:** If PC1 has an explained variance ratio of 0.72, it means PC1 alone captures 72% of all the information in the original dataset.

- You want the cumulative explained variance of your selected components to be at least **90%**.
- If PC1 + PC2 together give you 92% explained variance, reducing to 2 dimensions is very safe.
- **Common Mistake:** Always reducing to 2 dimensions regardless of how much variance they capture. If PC1 + PC2 only give 40% variance, you have lost 60% of the information — that is bad.

---

### Implementing PCA in Python

**About the Dataset We Are Using — Breast Cancer Wisconsin Dataset**

- The **Breast Cancer Wisconsin dataset** is a real-world medical dataset built directly into scikit-learn — no file download needed.
- It contains **569 patient records**. For each patient, doctors measured **30 different characteristics** of a tumour — things like its radius, texture, smoothness, and symmetry.
- The goal is to predict whether a tumour is **Malignant (cancerous)** or **Benign (non-cancerous)** based on those 30 measurements.
- We are using this dataset specifically because **30 features is too many to visualize**. It is a perfect real-world example to show why PCA is needed — we will compress those 30 features into just 2 and still be able to see the two groups clearly on a chart.

```python
# Import necessary libraries
import numpy as np                              # For numerical operations
import pandas as pd                             # For data handling
import matplotlib.pyplot as plt                 # For plotting
from sklearn.decomposition import PCA           # PCA from scikit-learn
from sklearn.preprocessing import StandardScaler  # For feature scaling
from sklearn.datasets import load_breast_cancer   # Sample dataset with many features

# -------------------------------------------------------
# Step 1: Load a real dataset with many features
# -------------------------------------------------------
data = load_breast_cancer()          # Load the breast cancer dataset (30 features!)
X = data.data                        # Feature matrix (569 rows, 30 columns)
y = data.target                      # Target labels (0 = malignant, 1 = benign)

print(f"Original shape: {X.shape}")  # Will print: (569, 30) — 30 features!

# -------------------------------------------------------
# Step 2: Standardize the features
# -------------------------------------------------------
scaler = StandardScaler()            # Initialize the scaler
X_scaled = scaler.fit_transform(X)  # Bring all 30 features to the same scale

# -------------------------------------------------------
# Step 3: Apply PCA to check explained variance for all components
# -------------------------------------------------------
pca_full = PCA()                     # Initialize PCA without specifying components
pca_full.fit(X_scaled)               # Fit on the scaled data

# -------------------------------------------------------
# Step 4: Plot the Cumulative Explained Variance
# -------------------------------------------------------
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)  # Cumulative sum of variance

plt.figure(figsize=(10, 5))                                     # Set figure size
plt.plot(range(1, 31), cumulative_variance, marker='o')         # Plot components vs cumulative variance
plt.axhline(y=0.90, color='r', linestyle='--', label='90% Variance')  # Red line at 90%
plt.axhline(y=0.95, color='g', linestyle='--', label='95% Variance')  # Green line at 95%
plt.xlabel('Number of Principal Components')                    # X-axis label
plt.ylabel('Cumulative Explained Variance')                     # Y-axis label
plt.title('How Many Components to Keep?')                       # Chart title
plt.legend()                                                    # Show legend
plt.tight_layout()                                              # Adjust layout
plt.show()                                                      # Display chart

# -------------------------------------------------------
# Step 5: Reduce to 2 components for visualization
# -------------------------------------------------------
pca_2d = PCA(n_components=2)         # Keep only the top 2 principal components
X_pca = pca_2d.fit_transform(X_scaled)  # Project the 30-feature data to 2D

print(f"Reduced shape: {X_pca.shape}")   # Will print: (569, 2) — only 2 features now!
print(f"Variance explained by PC1: {pca_2d.explained_variance_ratio_[0]:.2%}")
print(f"Variance explained by PC2: {pca_2d.explained_variance_ratio_[1]:.2%}")
print(f"Total variance captured: {sum(pca_2d.explained_variance_ratio_):.2%}")

# -------------------------------------------------------
# Step 6: Visualize the 2D projection
# -------------------------------------------------------
plt.figure(figsize=(8, 6))                        # Set figure size
plt.scatter(
    X_pca[y == 0, 0], X_pca[y == 0, 1],          # Points for class 0 (malignant)
    color='red',                                   # Red for malignant
    alpha=0.6,                                     # Slight transparency
    label='Malignant'                              # Legend label
)
plt.scatter(
    X_pca[y == 1, 0], X_pca[y == 1, 1],          # Points for class 1 (benign)
    color='blue',                                  # Blue for benign
    alpha=0.6,                                     # Slight transparency
    label='Benign'                                 # Legend label
)
plt.xlabel('Principal Component 1 (PC1)')         # X-axis is PC1
plt.ylabel('Principal Component 2 (PC2)')         # Y-axis is PC2
plt.title('PCA: Breast Cancer Data Reduced to 2D') # Chart title
plt.legend()                                       # Show legend
plt.tight_layout()                                 # Adjust layout
plt.show()                                         # Display chart
```

**How the code works:**

- We load the **Breast Cancer dataset** which has 30 features — impossible to visualize directly.
- We scale the data with `StandardScaler` because PCA is distance-sensitive.
- We run PCA on all 30 components first and plot the **Cumulative Explained Variance** curve to decide how many components to keep.
- We then reduce to 2 components (`n_components=2`) and print how much variance they capture together.
- Finally, we create a scatter plot where each point (a patient) is represented in 2D. The colors show whether they are malignant or benign — and you can see they form distinct clusters even in 2D!

---

## PCA Visualization — Making Sense of High-Dimensional Data

We already saw how PCA reduces data to 2D. Now let us understand **why visualization matters** and how to interpret a PCA plot.

**The Core Value:** When you reduce a 30-feature dataset to 2 features using PCA, you can now **plot it on a standard X-Y graph** that any human can read. The patterns that were hiding in 30 dimensions become visible in 2D.

---

### Reading a PCA Plot

When you look at the 2D PCA scatter plot, here is how to interpret it:

- **Points that are close together** in the 2D plot were also similar in the original 30-dimensional space.
- **Points that are far apart** in the 2D plot are genuinely different from each other.
- If you color points by their class labels, you can visually check how well the two classes separate. Good separation = the model will likely perform well.
- **Overlap in the 2D plot** means those classes are genuinely hard to distinguish — even 30 features could not clearly separate them.

---

### Combining PCA with K-Means

PCA and K-Means are a **powerful combination** and are frequently used together in real projects.

- First, use PCA to **reduce dimensions** (e.g., from 50 features to 10).
- Then, apply **K-Means on the reduced data**.
- Benefits: K-Means runs faster on fewer features. Distance calculations are more meaningful without noisy or redundant features.
- Finally, reduce further to 2D using PCA to **visualize the resulting clusters**.

![Typical pipeline: scale high-dimensional data, use PCA to reduce dimensions, then run K-Means and visualize in 2D](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-kmeans-pipeline.png)

**About the Dataset We Are Using — `make_blobs` (5D version)**

- Again we use `make_blobs`, but this time we create data with **5 features** instead of 2 — making it impossible to visualize directly.
- This is intentional: it simulates a real situation where your data has many columns and you need PCA to see it.
- We know there are 4 natural groups in the data (we set `centers=4`), so after clustering we can verify whether K-Means found them correctly.

```python
# Full pipeline: PCA + K-Means + Visualization

# Import all required libraries
from sklearn.pipeline import Pipeline                # To chain steps together
from sklearn.cluster import KMeans                   # K-Means algorithm
from sklearn.decomposition import PCA                # PCA algorithm
from sklearn.preprocessing import StandardScaler     # Feature scaling
from sklearn.datasets import make_blobs              # Sample data
import matplotlib.pyplot as plt                      # For plotting

# Generate 5-dimensional sample data with 4 natural clusters
X, _ = make_blobs(
    n_samples=500,     # 500 data points
    centers=4,         # 4 natural groups
    n_features=5,      # 5 features (not easily visualizable directly)
    random_state=42    # For reproducibility
)

# Step 1: Scale the data
scaler = StandardScaler()           # Initialize scaler
X_scaled = scaler.fit_transform(X)  # Scale to mean=0, std=1

# Step 2: Reduce to 2 components using PCA for visualization
pca = PCA(n_components=2)           # Keep top 2 components
X_pca = pca.fit_transform(X_scaled) # Transform 5D data to 2D

# Step 3: Apply K-Means on the PCA-reduced data (K=4)
kmeans = KMeans(
    n_clusters=4,          # We know there are 4 groups
    init='k-means++',      # Smart initialization
    random_state=42        # Reproducibility
)
cluster_labels = kmeans.fit_predict(X_pca)  # Fit and get labels in one step

# Step 4: Visualize PCA + K-Means together
plt.figure(figsize=(9, 6))              # Set figure size
plt.scatter(
    X_pca[:, 0], X_pca[:, 1],          # 2D PCA coordinates
    c=cluster_labels,                   # Color by cluster
    cmap='tab10',                       # Distinct color palette
    s=50,                               # Point size
    alpha=0.8                           # Slight transparency
)
plt.title('K-Means Clusters Visualized on PCA-Reduced Data')  # Title
plt.xlabel('PC1')                       # X-axis
plt.ylabel('PC2')                       # Y-axis
plt.colorbar(label='Cluster Label')    # Color bar for cluster IDs
plt.tight_layout()                      # Adjust layout
plt.show()                              # Show the chart
```

**How the code works:**

- We start with 5-dimensional data (impossible to visualize directly).
- We scale it and then apply PCA to compress it to 2D.
- We run K-Means with K = 4 on the PCA-reduced data to find the 4 clusters.
- The final scatter plot shows the 4 clusters in 2D, each in a different color.

---

### Important Cautions When Using PCA

PCA is powerful but comes with some important warnings:

- **PCA components are not interpretable** like the original features. You can no longer say "PC1 = age" — it is a mathematical combination of all original features.
- **PCA is linear** — it only captures linear relationships. If your data has complex non-linear structure, PCA may miss important patterns.
- Always check the **explained variance ratio**. Never blindly use 2 components without checking how much variance they capture.
- **Do not use PCA as a substitute for feature selection.** If you want to keep features interpretable, use feature selection methods instead.

---

## Key Takeaways

- **Unsupervised Learning** finds hidden patterns in data without any labels. It is used when collecting labeled data is impractical or expensive.
- **K-Means Clustering** groups data into K clusters by iteratively assigning points to the nearest centroid and recalculating centroids — this repeats until convergence. Use the **Elbow Method** to find the optimal K.
- **PCA (Principal Component Analysis)** compresses high-dimensional data into fewer **Principal Components** while retaining maximum variance. The first component captures the most information, and subsequent components capture progressively less.
- **PCA + K-Means** is a powerful combo — PCA reduces noise and dimensions, K-Means finds structure, and a final 2D PCA plot makes the clusters human-readable.
- In the upcoming sessions, we will build on these concepts to explore more advanced machine learning workflows including model pipelines, feature engineering, and ensemble methods.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Means |
|---|---|
| `KMeans(n_clusters=K)` | Initialize K-Means with K clusters |
| `kmeans.fit(X)` | Train the K-Means model on data X |
| `kmeans.labels_` | Array of cluster assignments for each data point |
| `kmeans.cluster_centers_` | Coordinates of each centroid |
| `kmeans.inertia_` | WCSS (Within-Cluster Sum of Squares) — lower is better |
| `init='k-means++'` | Smart centroid initialization to avoid poor random starts |
| `PCA(n_components=n)` | Initialize PCA, keeping top n components |
| `pca.fit_transform(X)` | Fit PCA and transform the data in one step |
| `pca.explained_variance_ratio_` | How much variance each component explains |
| `np.cumsum(...)` | Calculates cumulative sum (used for cumulative variance plot) |
| `StandardScaler` | Scales features to mean=0, std=1 — required before PCA and K-Means |
| **Cluster** | A group of similar data points |
| **Centroid** | The calculated center (mean position) of a cluster |
| **WCSS / Inertia** | Total distance of points from their cluster center — used in Elbow Method |
| **Elbow Method** | Technique to pick optimal K by finding the "elbow" in WCSS vs K plot |
| **Dimensionality Reduction** | Reducing the number of features while preserving information |
| **Principal Component (PC)** | A new axis in PCA that captures maximum variance |
| **Explained Variance Ratio** | Fraction of total variance captured by one principal component |
| **Curse of Dimensionality** | Problem where too many features make distances meaningless |
| **Convergence** | State where K-Means centroids stop moving between iterations |
| **Unsupervised Learning** | Learning patterns from data without labels |
