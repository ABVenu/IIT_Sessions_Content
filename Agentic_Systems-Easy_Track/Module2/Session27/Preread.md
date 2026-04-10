# Data leakage, class imbalance, and evaluation — session notes

You train a model, compute **accuracy**, and get a high number—so the model looks ready. In many real pipelines that number is **misleading**: the model may have seen information it will not have at prediction time (**data leakage**), or the labels may be **skewed** so “always guess the majority class” still scores well (**class imbalance**).

Both issues are easy to miss because they rarely throw errors; they quietly inflate scores until **production**. Below follows the lecture thread: leakage and how it happens, the **split-first** workflow, imbalance and why **accuracy** fails, **precision** / **recall**, **resampling** and **synthetic** ideas, **cross-validation**, and how those pieces fit one honest evaluation story.

## 1. Why headline accuracy can lie (summary)

| Hidden issue | What the model does | What you see | What breaks later |
| --- | --- | --- | --- |
| **Leakage** | Uses future or “answer” features | Great train/test scores | No access to those features live |
| **Imbalance** | Predicts the majority class almost always | High accuracy | **Rare** class (fraud, disease) nearly never found |
| **One lucky split** | Fits one test draw | One score looks “final” | Number not representative |

**Core habit:** treat metrics as trustworthy only when **data handling**, **label balance**, and **how you evaluate** are all disciplined.

## 2. Data leakage — meaning

**Leakage** means training uses information that **would not exist** at the moment you must predict. The model learns a shortcut; evaluation looks strong until deployment.

**Thinking question** before any feature:

> Would this information genuinely exist at prediction time?

If no (or unclear), drop or redesign the feature.

## 3. How leakage usually enters (patterns)

**Preprocessing before split.** Filling missing values or fitting **scalers** on the **full** dataset lets test rows influence means, mins, maxs, or imputations. The test set is no longer unseen.

**Features built from the target.** A column derived from the outcome (e.g. “expensive” from actual price) restates the answer; the model “learns” without generalising.

**Duplicates across train and test.** The same (or near-duplicate) rows in both sets make evaluation look like memory, not generalisation.

**Payoff when fixed:** reported accuracy may **drop**—that is often progress toward an honest estimate, not failure.

## 4. Leakage guard — split-first workflow

**Principle.** Split **first**; learn every statistic and transform **only** on **training**; apply the **same** fitted objects to validation/test without refitting.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit on train
X_test_scaled = scaler.transform(X_test)         # only transform test
```

**Semantics.** `fit_transform` on train; `transform` on test—never `fit` on the full table before splitting.

## 5. Class imbalance — meaning

**Imbalance:** one label vastly outnumbers another (fraud vs normal, sick vs healthy, purchase vs bounce). That often reflects reality, not “bad CSVs.”

**Model effect.** Minimising plain error pushes the model toward the **majority** label; overall accuracy can stay high while the **minority**—often the reason you built the model—is ignored.

## 6. Accuracy under imbalance — toy case

**Setup.** 99 “normal”, 1 “fraud”; model predicts “normal” for **every** row.

**Result.** **99% accuracy**, **0%** fraud caught. The headline number hides total failure on the task you care about.

**Insight.** Not all errors cost the same; accuracy alone does not encode that.

## 7. Precision and recall — what accuracy hides

**Precision:** of positive predictions, how many were truly positive? (quality of “yes” calls; false alarms hurt here.)

**Recall:** of actual positives, how many did we find? (coverage; **misses** hurt here.)

**Trade-off.** Stricter thresholds usually raise precision and lower recall, and the reverse when you relax. Which side hurts more depends on the domain (spam vs missed fraud, etc.).

## 8. Handling imbalance — resampling (overview)

**Oversampling** adds weight to the minority (e.g. duplicates). **Risk:** memorising repeated rows instead of learning shape.

**Undersampling** drops majority rows to balance. **Risk:** throwing away useful majority signal.

**Goal:** give the minority a fair chance to influence learning—not token equality for its own sake. **Synthetic** methods (lecture) try to add **plausible new** minority points, not only copies; bad blends can add noise.

## 9. Cross-validation — trusting the number

**Single split.** Test set composition is one random draw; scores can be **lucky** or **harsh**.

**k-fold CV.** Each fold acts as test once; you average (and inspect spread across folds). **Lower variance** in fold scores suggests a stabler estimate than one split alone.

Lecture **§10** uses `make_classification` with ~92% / ~8% labels and `cross_val_score(..., cv=5)` as a concrete pattern.

## 10. Connecting leakage, imbalance, and CV

**Leakage** inflates scores; you ship a model that cannot reproduce them live.

**Imbalance** makes accuracy look fine while the rare class is missed.

**No CV** leaves you hostage to one split’s noise.

**Together:** guard the split and transforms, report **class-aware** metrics (and balancing if needed), and stabilise estimates with **cross-validation** where appropriate.

## 11. Pitfalls (quick checklist)

1. **Impute or scale before `train_test_split`**—classic leakage.
2. **Refit** preprocessing on train+test “so it’s consistent”—still leakage; fit on train only.
3. **Trust accuracy** on rare-event problems without precision/recall (or related) views.
4. **Oversample then leak**—if balancing uses test data, you have contaminated evaluation (keep balancing inside training folds when using CV).
5. **One split, one number, ship**—no sense of variance across data partitions.
6. **Synthetic data** built without domain sense—unreal blends hurt more than they help.

Full examples, domain stories, diagrams, and the **Quick Reference** table live in **Lecture Notes.md** in this folder (sections **1–11** and cheat sheet).
