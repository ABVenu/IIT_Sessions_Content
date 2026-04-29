# Assignment Question QC Report — Session 32

**Session:** Unsupervised Learning: Clustering and Dimensionality Reduction
**Module:** Module 2
**Course:** iitr-as-2601

---

## Objective Assignment QC

| Q# | Type | Correct Option(s) | Correct Option Relevancy | Remarks |
|---|---|---|---|---|
| Q1 | MCQ — Easy | C | Yes | Tests core definition of unsupervised learning. Scenario-based (Riya, food delivery). All distractors plausible. Correct option directly maps to the unlabeled-data scenario. |
| Q2 | MCQ — Easy | C | Yes | Tests Step 4 of K-Means workflow (centroid recalculation = mean). Correct option "Mean (average)" is explicitly from session notes. Distractors are valid mathematical operations that are factually wrong for K-Means. |
| Q3 | MCQ — Easy | C | Yes | Tests the concept of convergence. Correct option "The model has converged" maps precisely to session definition: "centroids stop moving and assignments stop changing." |
| Q4 | MCQ — Easy | C | Yes | Tests K-Means++ initialization. Correct option is directly covered in session notes. Distractor A ("init='random'") is the root cause of the problem described, making it a well-crafted trap. |
| Q5 | MCQ — Moderate | C | Yes | Tests Elbow Method interpretation with a numerical scenario. WCSS table provided. Correct answer (K=3) is verifiable from the drop-off pattern. Scenario-based and requires application, not just recall. |
| Q6 | MCQ — Moderate | C | Yes | Tests the consequence of skipping StandardScaler before K-Means. Correct option explains the distance-distortion mechanism, which is explicitly covered in the session. |
| Q7 | MSQ — Moderate | A, B, C | Yes | Tests multiple K-Means properties simultaneously. Trap: Option D ("globally optimal") is a deliberate misconception — K-Means gives local optima only. A, B, C are all directly stated in session notes. |
| Q8 | MSQ — Moderate | A, B, D | Yes | Tests the ability to distinguish unsupervised from supervised use cases. Option C is a supervised problem (has labels). A, B, D all match unsupervised definitions from the session. |
| Q9 | MSQ — Hard | A, B, D | Yes | Tests deeper understanding of WCSS behavior and the Elbow Method. Trap: Option C ("optimal K = WCSS of 0") is a deliberate and common misconception explicitly addressed in session notes. All correct options are verifiable from lecture material. |
| Q10 | MSQ — Hard | A, C, D | Yes | Tests PCA understanding including the non-interpretability of Principal Components. Trap: Option B ("PCs can be labeled with original feature names") is explicitly called out as incorrect in session notes ("PCA components are not directly interpretable"). All correct options align with session content. |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear | Dataset Dependency | Remarks |
|---|---|---|---|---|---|
| Q1 | Coding Implementation | Medium | Yes — Single `.py` file, run and verify, submit via code editor in LMS | No external file needed — dataset is generated fully in-code using `numpy` | Creative applied scenario (healthcare domain, patient risk segmentation). Not a direct replication of lecture code — uses a different domain, 5 features instead of 2, and combines K-Means + Elbow Method + Cluster Summary Table + PCA visualization in a single integrated pipeline. |

---

## Overall QC Ratings

| Metric | Objective Assignment | Subjective Assignment |
|---|---|---|
| Content Coverage | 5 / 5 | 5 / 5 |
| Creativity | 5 / 5 | 5 / 5 |
| Structural Adherence | 5 / 5 | 5 / 5 |
| No Logical Mistakes | True | True |
| No Presentation Mistakes | True | True |

---

## QC Verification Notes

**Structural Adherence:**
- Objective: 10 questions total — 6 MCQs (4 Easy + 2 Moderate) + 4 MSQs (2 Moderate + 2 Hard). Order is progressive: Easy (Q1–Q4) → Moderate (Q5–Q8) → Hard (Q9–Q10). Matches spec exactly.
- Subjective: 1 practical coding task. Medium difficulty. Submission instructions follow Case C (single `.py` file, submit in code editor).

**Content Coverage:**
- All 10 objective questions draw exclusively from Session 32 topics: unsupervised learning concepts, K-Means workflow (Steps 1–5), Elbow Method / WCSS, feature scaling, K-Means++, convergence, PCA, Curse of Dimensionality, and Principal Components.
- Subjective question tests the full K-Means implementation pipeline from the session, extended into a novel applied domain.

**Creativity:**
- All questions use scenario-based framing (Riya, Arjun, Priya, e-commerce companies, hospitals) rather than dry textbook prompts.
- Subjective question uses a healthcare context not present in the session's lecture example, requiring genuine transfer of knowledge.

**Logical Accuracy:**
- WCSS values in Q5 are internally consistent and correctly identify K=3 as the elbow.
- All correct MSQ answer sets have been cross-verified against the lecture notes.
- Reference solution in subjective assignment produces correct output with the given dataset generation code.

**No content outside session scope has been included.**
