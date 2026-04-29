# Assignment: Unsupervised Learning — Clustering

## Subjective Assignment

**Total Questions: 1 | Type: Coding Implementation | Difficulty: Medium**

---

### Question 1 — Patient Risk Segmentation Using K-Means

**Background:**

HealthFirst Analytics, a healthcare data science company, has collected health metrics for **400 patients** across five clinical measurements. Their medical team wants to identify **natural patient risk segments** from this data — without relying on any pre-existing diagnosis labels — so they can proactively design targeted health intervention programs.

You have been told to work on this project. Your task is to build a complete, well-documented Python pipeline that clusters patients into risk groups and helps the team pick the right number of groups.

---

**Your pipeline must complete all of the following steps:**

**Step 1 — Generate the Patient Dataset**
Use the dataset generation code provided below. Do not change the random seed or the array structure.

**Step 2 — Scale the Features**
Apply `StandardScaler` from scikit-learn to normalize the data before clustering.

**Step 3 — Elbow Method**
Loop through K = 1 to 10, fit a K-Means model for each K using `init='k-means++'`, and record the WCSS (inertia). Plot a labeled line chart of WCSS vs K to identify the optimal K visually. Title the plot: `"Elbow Method — Optimal K for Patient Clustering"`.

**Step 4 — Train the Final K-Means Model**
Using the optimal K identified from your Elbow plot, train a final K-Means model with `n_init=10` and `random_state=42`.

**Step 5 — Print a Cluster Summary Table**
For each cluster, calculate and print the **mean value** of each health feature for patients in that cluster. Format it as a readable table using a pandas DataFrame. Round all values to 2 decimal places.

**Dataset Generation Code — Use exactly as given:**

```python
import numpy as np
import pandas as pd

np.random.seed(42)

data = {
    'systolic_bp':   np.concatenate([np.random.normal(118, 10, 150),
                                     np.random.normal(142, 12, 150),
                                     np.random.normal(168, 8,  100)]),
    'cholesterol':   np.concatenate([np.random.normal(178, 18, 150),
                                     np.random.normal(222, 22, 150),
                                     np.random.normal(262, 18, 100)]),
    'bmi':           np.concatenate([np.random.normal(21.5, 2, 150),
                                     np.random.normal(27.0, 3, 150),
                                     np.random.normal(33.5, 3, 100)]),
    'glucose_level': np.concatenate([np.random.normal(88,  10, 150),
                                     np.random.normal(112, 14, 150),
                                     np.random.normal(148, 18, 100)]),
    'age':           np.concatenate([np.random.normal(34, 7,  150),
                                     np.random.normal(51, 6,  150),
                                     np.random.normal(63, 5,  100)])
}

df = pd.DataFrame(data)
```

---

**Expected Output:**
1. An Elbow Method line plot saved or displayed (WCSS vs K, 1–10)
2. A printed Cluster Summary Table (mean feature values per cluster, rounded to 2 decimal places)

**Submission Instructions:**
- Code all the steps mentioned above in VS Code in a single `.py` file (e.g., `patient_clustering.py`)
- Run the code and verify it works correctly — both outputs (Elbow plot and Cluster Summary table) should be generated without errors
- Then submit the code in the code editor/answer box in the LMS

-------------------------------------------

**Answer Explanation (Ideal Solution Walkthrough):**

The dataset contains three naturally embedded patient groups — low-risk (younger, healthy metrics), moderate-risk (middle-aged, elevated metrics), and high-risk (older, significantly elevated metrics). The Elbow Method should reveal K=3 as the elbow point where WCSS flattening begins.

Key solution steps:
1. Scale all 5 features using `StandardScaler` — critical because features like `cholesterol` (150–300) and `bmi` (18–40) are on very different scales.
2. Loop K=1 to 10, storing `kmeans.inertia_` at each step, then plot.
3. Train final model with `KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)`.
4. Build cluster summary: group the original `df` by `kmeans.labels_`, call `.mean().round(2)`.

**Complete Reference Solution:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

np.random.seed(42)

data = {
    'systolic_bp':   np.concatenate([np.random.normal(118, 10, 150),
                                     np.random.normal(142, 12, 150),
                                     np.random.normal(168, 8,  100)]),
    'cholesterol':   np.concatenate([np.random.normal(178, 18, 150),
                                     np.random.normal(222, 22, 150),
                                     np.random.normal(262, 18, 100)]),
    'bmi':           np.concatenate([np.random.normal(21.5, 2, 150),
                                     np.random.normal(27.0, 3, 150),
                                     np.random.normal(33.5, 3, 100)]),
    'glucose_level': np.concatenate([np.random.normal(88,  10, 150),
                                     np.random.normal(112, 14, 150),
                                     np.random.normal(148, 18, 100)]),
    'age':           np.concatenate([np.random.normal(34, 7,  150),
                                     np.random.normal(51, 6,  150),
                                     np.random.normal(63, 5,  100)])
}
df = pd.DataFrame(data)

# Step 2: Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Step 3: Elbow Method
wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, init='k-means++', random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method — Optimal K for Patient Clustering')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Inertia)')
plt.tight_layout()
plt.show()

# Step 4: Final model
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# Step 5: Cluster Summary
df['Cluster'] = labels
print("\nCluster Summary (Mean Feature Values per Cluster):")
print(df.groupby('Cluster').mean().round(2).to_string())
```

---


