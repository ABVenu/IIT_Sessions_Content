# Assignment: Objective — Session 15: Leakage & Imbalance

**Total Questions: 10 | Format: 6 MCQs (Single Correct) + 4 MSQs (Multiple Correct)**  
**Order: Easy → Moderate → Hard**

**Instructions:** Choose the best answer for MCQs. For MSQs, **select all that apply**. Submit via the LMS objective assessment.

---

## MCQ 1 — Easy (Single Correct)

NovaBank is building a model to flag **fraudulent transactions before they settle**. A data engineer adds a column `refund_issued` that is filled in **only after** a disputed transaction is reviewed. At prediction time, that column does not exist yet. What problem does this feature create?

**A)** Class imbalance — one label appears far more often than the other  
**B)** Data leakage — training uses information that would not exist at real prediction time  
**C)** Cross-validation noise — one random split looks too good or too bad  
**D)** Low recall — the model misses too many real fraud cases  

**Correct Answer: B**

**Answer Explanation:**  
`refund_issued` is decided **after** the moment the bank must score risk, so it is a forbidden future clue. That is **data leakage**. **A** is about skewed label counts, not forbidden features. **C** is about evaluation strategy, not feature timing. **D** is a metric outcome, not the root cause of using post-outcome data.

---

## MCQ 2 — Easy (Single Correct)

A campus health app team prepares numeric vitals for a dropout-risk model. They want a **leakage-safe** order of operations. Which sequence is correct?

**A)** Scale all rows → split train/test → train the model  
**B)** Split train/test → fit the scaler on training rows only → transform test with training statistics → train the model  
**C)** Train the model → split train/test → scale test with test statistics  
**D)** Fit the scaler on the test set → fit_transform the training set → train the model  

**Correct Answer: B**

**Answer Explanation:**  
**Split first**, then **learn** scaling parameters from **training only**, then **`transform` test** without refitting — that keeps test statistics out of preprocessing. **A** leaks because test rows influence the scaler. **C** trains before a proper holdout workflow. **D** fits on test, which is backwards and leaks.

---

## MCQ 3 — Easy (Single Correct)

SecureLogin monitors **10,000** login attempts: **9,800** are labelled **safe** and **200** are **hacked**. A rookie model predicts **“safe”** for every row. What is its **accuracy**?

**A)** 2%  
**B)** 20%  
**C)** 98%  
**D)** 100%  

**Correct Answer: C**

**Answer Explanation:**  
The model is correct on all **9,800** safe rows and wrong on all **200** hacked rows: **9,800 ÷ 10,000 = 98%** accuracy. **A** is the minority rate (2%), not accuracy. **B** and **D** do not match the counts.

---

## MCQ 4 — Easy (Single Correct)

A rare-disease screen reports **99% accuracy**, but doctors complain that most sick patients are still sent home as “healthy.” Which statement best explains the gap?

**A)** Accuracy counts all correct answers equally, so a model can look strong while catching almost none of the rare sick cases  
**B)** Accuracy always equals recall on imbalanced data  
**C)** High accuracy proves the model has no false positives  
**D)** Imbalance only affects regression models, not classification  

**Correct Answer: A**

**Answer Explanation:**  
When the healthy class dominates, predicting “healthy” often yields **high accuracy** while **recall on the sick class** stays near zero. **B** is false — accuracy and recall measure different things. **C** is false — high accuracy does not rule out false positives. **D** is false — imbalance is a classification issue in this story.

---

## MCQ 5 — Moderate (Single Correct)

A quality team reviews flagged defects on a factory line. Out of **100** items the model marked **defective**, **85** truly were defective (**15** were false alarms). Out of **60** real defects on the line that day, the model found **51**. What are **precision** and **recall** (for the “defective” positive class)?

**A)** Precision = 0.85 ; Recall = 0.85  
**B)** Precision = 0.85 ; Recall = 0.51  
**C)** Precision = 0.51 ; Recall = 0.85  
**D)** Precision = 0.51 ; Recall = 0.51  

**Correct Answer: A**

**Answer Explanation:**  
**Precision** = TP ÷ (TP + FP) = **85 ÷ 100 = 0.85** (when we flag defective, how often we are right). **Recall** = TP ÷ (TP + FN). True positives = **51** caught; false negatives = 60 − 51 = **9**; recall = **51 ÷ 60 = 0.85**. **B–D** swap or miscompute one of the two rates.

---

## MCQ 6 — Moderate (Single Correct)

After fixing a leaky pipeline, test **accuracy drops** from 94% to 78%. The product owner asks whether this is bad news. What is the best reply?

**A)** Yes — always roll back; lower accuracy always means a worse model  
**B)** No — the earlier 94% was likely inflated by leakage; 78% is a more honest estimate  
**C)** No — accuracy on imbalanced data is always trustworthy, so 78% must be wrong  
**D)** Yes — you should apply SMOTE to the test set until accuracy rises again  

**Correct Answer: B**

**Answer Explanation:**  
Removing leakage often **lowers** reported scores because the model no longer “cheats” with test-set information. That drop can mean the evaluation is finally **honest**. **A** treats every drop as failure. **C** ignores imbalance pitfalls. **D** is wrong — never balance the **test** set to chase a prettier accuracy number.

---

## MSQ 7 — Moderate (Multiple Correct) — Select all that apply

Which actions belong on a **data-leakage guard checklist** before you trust a model score?

**A)** Call `train_test_split` immediately after loading data and lock away the test portion  
**B)** Fit imputers, encoders, and scalers on **training rows only**, then `transform` the test set  
**C)** Tune every hyperparameter by whichever setting maximises test accuracy  
**D)** Keep only features you would truly know **before** the outcome you are predicting  

**Correct Answers: A, B, D**

**Answer Explanation:**  
**A**, **B**, and **D** match the taught guards: split first, train-only fit, and real-time feature discipline. **C** is leakage-by-peeking — repeatedly optimising on the test set lets test information steer training choices.

---

## MSQ 8 — Moderate (Multiple Correct) — Select all that apply

A fraud analyst reads a **binary** confusion matrix for the “fraud” positive class. Which statements are correct?

**A)** A **false positive** means the model flagged fraud, but the transaction was legitimate  
**B)** A **false negative** means the model cleared the transaction, but it was actually fraud  
**C)** **True negatives** are legitimate transactions correctly labelled as not fraud  
**D)** **High recall** means that when the model says “fraud,” it is almost always right  

**Correct Answers: A, B, C**

**Answer Explanation:**  
**A**, **B**, and **C** are standard TP/TN/FP/FN readings. **D** describes **precision** (trust when we flag “yes”), not recall (how many real fraud cases we **catch**).

---

## MSQ 9 — Hard (Multiple Correct) — Select all that apply

PayGuard’s ML team balances **training** data with **SMOTE** after a proper train–test split. Which practices are **sound**?

**A)** Apply `SMOTE.fit_resample` only on **training** features and labels  
**B)** Leave the **test set** at the real-world class ratio for evaluation  
**C)** Compare baseline and SMOTE models using the same held-out test set and a **classification report**  
**D)** Run SMOTE on the combined train+test table so both sets have 50/50 labels  

**Correct Answers: A, B, C**

**Answer Explanation:**  
**A–C** follow honest imbalance handling: balance **train** for learning, keep **test** realistic, and compare fairly on the same test split. **D** leaks and destroys production-like evaluation by altering the test distribution.

---

## MSQ 10 — Hard (Multiple Correct) — Select all that apply

Two candidate models are compared on a **medium-sized** tabular dataset. Which statements about **cross-validation** are fair?

**A)** Repeating train–test evaluation on several folds and **averaging** scores can reduce reliance on one lucky split  
**B)** If five fold scores are `[0.76, 0.74, 0.78, 0.75, 0.77]`, performance looks relatively **stable** compared with a single score of `0.95` from one split  
**C)** Cross-validation replaces the need to ever hold out a final test set in every real project  
**D)** A wide spread across folds (for example `0.55` to `0.92`) suggests performance may depend heavily on which rows were held out  

**Correct Answers: A, B, D**

**Answer Explanation:**  
**A**, **B**, and **D** match the conceptual goals: averaged, stable estimates and reading spread. **C** overstates CV — teams often still keep a **locked** final test set for late validation; CV is not a universal substitute.

---

**End of objective assignment.**
