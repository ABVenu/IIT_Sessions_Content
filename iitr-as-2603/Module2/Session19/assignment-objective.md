# Objective Assignment - Classification Models and Evaluation Metrics

## Instructions
- Total questions: 10
- Question types: 6 MCQs (single correct), 4 MSQs (multiple correct)
- Difficulty progression: Easy -> Moderate -> Hard

---

## MCQs (Single Correct)

### Q1 (Easy)
In a Decision Tree, which part stores the final class prediction (Pass/Fail)?

A. Root node  
B. Leaf node  
C. Branch  
D. Depth

**Correct Answer:** B  
**Explanation:** Leaf nodes are terminal nodes where the model outputs the final class label.

### Q2 (Easy)
Why is `max_depth` used in a Decision Tree?

A. To increase the number of features automatically  
B. To limit tree complexity and reduce overfitting  
C. To convert the tree into logistic regression  
D. To remove the need for train-test split

**Correct Answer:** B  
**Explanation:** Limiting depth prevents the tree from becoming too specific to training data.

### Q3 (Easy)
What is the main idea behind Random Forest for classification?

A. One very deep tree predicts all labels  
B. Multiple trees vote, and majority vote decides the class  
C. Data is sorted and nearest point is chosen  
D. It predicts only probabilities, not labels

**Correct Answer:** B  
**Explanation:** Random Forest combines predictions from many trees and uses majority voting.

### Q4 (Easy)
Precision is defined as:

A. TP / (TP + FN)  
B. TP / (TP + FP)  
C. TN / (TN + FP)  
D. (TP + TN) / Total

**Correct Answer:** B  
**Explanation:** Precision measures correctness among predicted positives.

### Q5 (Moderate)
A model predicts 50 students as Pass. Out of these, 35 actually pass. What is precision?

A. 0.35  
B. 0.50  
C. 0.70  
D. 0.85

**Correct Answer:** C  
**Explanation:** Precision = TP / (TP + FP) = 35 / 50 = 0.70.

### Q6 (Moderate)
Which metric is most suitable when you want threshold-independent ranking quality of classifiers?

A. Accuracy  
B. Recall  
C. F1 Score  
D. ROC-AUC

**Correct Answer:** D  
**Explanation:** ROC-AUC evaluates ranking quality across all thresholds, not a single cut-off.

---

## MSQs (Multiple Correct)

### Q7 (Moderate)
Which statements about Random Forest are correct?

A. It uses bootstrap samples of training data for different trees.  
B. Every tree is trained on exactly the same feature subset at each split.  
C. Majority voting is used for final class prediction.  
D. It usually provides more stable performance than a single tree.

**Correct Answers:** A, C, D  
**Explanation:** Random Forest uses bagging and voting; random feature subsets vary by split, so B is incorrect.

### Q8 (Moderate)
For a binary classifier, which statements are correct?

A. Recall = TP / (TP + FN)  
B. Precision increases when FP increases while TP is fixed  
C. F1 score combines precision and recall  
D. Confusion matrix helps inspect TP, TN, FP, FN

**Correct Answers:** A, C, D  
**Explanation:** Increasing FP lowers precision, so B is incorrect.

### Q9 (Hard)
A model gives probability outputs for "Pass". Which actions are valid for ROC analysis?

A. Use `roc_auc_score(y_true, y_prob)` with probabilities  
B. Use hard labels from `predict()` as the best mandatory input for ROC-AUC  
C. Generate TPR/FPR pairs over multiple thresholds  
D. Compare classifier ranking ability before fixing a decision threshold

**Correct Answers:** A, C, D  
**Explanation:** ROC-AUC is designed for probability scores and threshold sweeps. Hard labels lose ranking information.

### Q10 (Hard)
You are comparing two classifiers on an imbalanced dataset where "Pass" is rare. Which conclusions are valid?

A. High accuracy alone can still hide poor minority-class detection  
B. Precision and recall are both useful to evaluate positive-class behavior  
C. AUC near 0.5 suggests no meaningful class separation  
D. F1 can be high even if either precision or recall is extremely low

**Correct Answers:** A, B, C  
**Explanation:** F1 drops when either precision or recall is very low; therefore D is incorrect.

