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

## PCA Visualization — Making Sense of High-Dimensional Data

One of the most practical uses of PCA is **visualization**. When you have a dataset with many features, there is no way to plot it on a standard graph. PCA solves this by compressing those many features down to just 2, which you can then plot on a standard X-Y scatter chart that any human can read.

**The Core Value:** When you reduce a dataset with many features to 2 dimensions using PCA, the patterns that were hiding in high-dimensional space become visible in 2D.

- With 10, 20, or 30 features, you cannot draw any meaningful chart.
- Humans can only comfortably interpret up to 3 dimensions visually.
- PCA gives you a "best possible 2D view" of your high-dimensional data — like flattening a 3D object to see its most informative shadow.

![PCA projects high-dimensional data onto new axes (PC1, PC2, …) that capture the most variance, enabling 2D plots](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/Session32/lecture-notes-images/session32-pca-highd-to-2d.png)

- **Important:** The new features (Principal Components) produced by PCA are mathematical combinations of all original features — they are **not human-interpretable**.
- You cannot label PC1 as "age" or "income" — it is a mathematical summary blending all original columns.
- This is a key trade-off: you gain the ability to visualize high-dimensional data, but you lose direct feature meaning in the process.

---

## Key Takeaways

- **Unsupervised Learning** finds hidden patterns in data without any labels. It is used when collecting labeled data is impractical or expensive.
- **K-Means Clustering** groups data into K clusters by iteratively assigning points to the nearest centroid and recalculating centroids — this repeats until convergence. Use the **Elbow Method** to find the optimal K.
- **PCA (Principal Component Analysis)** compresses high-dimensional data into fewer dimensions while retaining as much information as possible — making it possible to visualize data that would otherwise be impossible to plot.
- PCA components are **not directly interpretable** like the original features — they are mathematical summaries of the original data.
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
| `StandardScaler` | Scales features to mean=0, std=1 — required before K-Means |
| **Cluster** | A group of similar data points |
| **Centroid** | The calculated center (mean position) of a cluster |
| **WCSS / Inertia** | Total distance of points from their cluster center — used in Elbow Method |
| **Elbow Method** | Technique to pick optimal K by finding the "elbow" in WCSS vs K plot |
| **Dimensionality Reduction** | Reducing the number of features while preserving information |
| **Principal Component (PC)** | A new summary feature created by PCA that captures maximum variance |
| **Curse of Dimensionality** | Problem where too many features make distances meaningless |
| **Convergence** | State where K-Means centroids stop moving between iterations |
| **Unsupervised Learning** | Learning patterns from data without labels |
