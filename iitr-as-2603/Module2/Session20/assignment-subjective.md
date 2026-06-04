# Subjective Assignment - Medium Difficulty

## Practical Task: QuickMart Customer Segmentation Pipeline

**QuickMart** is an online store with **no pre-defined shopper segments**. You receive behavioral data for **300 customers** and **8 numeric features** (e.g. pages viewed, cart adds, session length, spend indicators). Your job is to compress the data for visualization, find a sensible number of segments, cluster in 2D, and summarize what each group looks like.

### Requirements

1. **Create reproducible data** in code (`random_state=42`):
   - At least **300 rows** and **8 numeric feature columns** (you may use `numpy` / `pandas`; column names are your choice).
   - **No target/label column** for clustering.

2. **Preprocessing & reduction:**
   - Scale all features with `StandardScaler`.
   - Apply `PCA(n_components=2)` and store the result in a DataFrame with **two columns** for the 2D summary directions (column names are your choice).

3. **Choose K (elbow):**
   - For **K = 1 to 8**, fit `KMeans` on the **2D PCA data** and record **inertia** (WCSS).
   - Print a small table or list: `K` vs `inertia`.
   - Pick one **final K** (2–6) and print **one sentence** justifying your choice from the elbow pattern.

4. **Final clustering:**
   - Fit `KMeans` with your chosen **K** on the PCA data.
   - Print **cluster id** and **count of customers** per cluster.

5. **Visualization:**
   - One **scatter plot**: first summary direction vs second summary direction, points colored by cluster id, with axis labels and a title.

6. **Business interpretation (text output):**
   - For each cluster, print the **mean of the original 8 features** (use the rows belonging to that cluster from your original table, not scaled PCA space).
   - End with **2–3 lines** naming each segment in plain language (e.g. “budget browsers,” “high-engagement buyers”) based on those means.

### Expected Output (minimum)

- Printed K vs inertia values  
- Chosen K with one-line justification  
- Cluster counts  
- One PCA + cluster scatter plot (saved or shown when run)  
- Per-cluster mean feature table + short segment naming paragraph  

### Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

### Answer Explanation (Reference Approach)

#### Step-by-step solution walkthrough

1. Generate 300×8 synthetic customer features with a fixed seed (no `y`).
2. `StandardScaler` → `PCA(2)` → a 2-column reduced DataFrame for plotting and clustering.
3. Loop K = 1..8 on the reduced 2D data, append `inertia_`, print and pick K at the elbow (often 3 or 4 on random Gaussian-like data).
4. Final `KMeans(n_clusters=chosen_K)` → `fit_predict` → counts and scatter plot.
5. Map cluster labels back to original rows; `groupby` cluster and `.mean()` on raw features; write segment names from dominant patterns.

#### Complete exact code (single-file reference solution)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 1) Reproducible 300 x 8 customer features (no labels)
np.random.seed(42)
n_rows = 300
n_features = 8
feature_names = [f"metric_{i+1}" for i in range(n_features)]
X_raw = np.random.randn(n_rows, n_features) * 2 + np.linspace(0, 3, n_features)
df_raw = pd.DataFrame(X_raw, columns=feature_names)

# 2) Scale -> PCA (2 components)
X_scaled = StandardScaler().fit_transform(df_raw.values)
X_reduced = PCA(n_components=2).fit_transform(X_scaled)
df_reduced = pd.DataFrame(
    X_reduced,
    columns=["summary_direction_1", "summary_direction_2"],
)

# 3) Elbow: K = 1..8 on 2D reduced data
print("K vs inertia (WCSS):")
inertia_by_k = []
for k in range(1, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df_reduced.values)
    inertia_by_k.append((k, km.inertia_))
    print(f"  K={k}: inertia={km.inertia_:.2f}")

# Example elbow choice (adjust if your plot bends earlier/later)
chosen_k = 3
print(
    f"\nChosen K={chosen_k}: largest drop in inertia happens early; "
    "gains flatten after K=3 on this run."
)

# 4) Final K-Means
kmeans_final = KMeans(n_clusters=chosen_k, random_state=42, n_init=10)
labels = kmeans_final.fit_predict(df_reduced.values)
df_raw["cluster"] = labels

print("\nCustomers per cluster:")
print(df_raw["cluster"].value_counts().sort_index())

# 5) Scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(
    df_reduced["summary_direction_1"],
    df_reduced["summary_direction_2"],
    c=labels,
    cmap="tab10",
    s=45,
    alpha=0.85,
)
plt.xlabel("Summary direction 1")
plt.ylabel("Summary direction 2")
plt.title(f"QuickMart segments (K={chosen_k}) — 2D summary plot")
plt.tight_layout()
plt.show()

# 6) Business interpretation: mean of original features per cluster
print("\nMean of original features by cluster:")
cluster_means = df_raw.groupby("cluster")[feature_names].mean()
print(cluster_means.round(2))

print("\nSegment summary (example wording — align to your means):")
for cid in sorted(df_raw["cluster"].unique()):
    row = cluster_means.loc[cid]
    top = row.idxmax()
    print(
        f"  Cluster {cid}: relatively higher '{top}' and peers; "
        "name this segment from your printed means."
    )
print(
    "Overall: PCA+K-Means gives marketing-ready groups when original-feature "
    "means are interpreted, not only the 2D summary axes."
)
```

#### Alternative approaches

- Elbow K can be chosen visually from a plotted curve instead of a fixed `chosen_k = 3`, as long as inertia table and justification are printed.
- Feature names and synthetic generation formulas may differ; clustering must still use **scaled → PCA(2) → KMeans on PCA data**.

#### Notes for evaluation

- Accept solutions that follow the pipeline and include all six requirement blocks.
- `n_init` may vary; `random_state=42` should be set for reproducibility where used.
