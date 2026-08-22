# ⛏️ Gold Recovery Prediction — Industrial Process Optimization

## 📌 Project Summary
This project uses real industrial data from a gold recovery plant to predict how efficiently gold is extracted from ore at two stages of the processing pipeline: the **rougher** (initial flotation) stage and the **final** purification stage. The production line includes flotation and two purification stages, each with its own technological parameters (feed size, reagent amounts, air flow, metal concentrations) that affect how much gold is recovered.

**Goal:** Build a model that accurately predicts recovery efficiency at both stages, using **sMAPE (symmetric Mean Absolute Percentage Error)** as the evaluation metric — the standard metric for this type of industrial recovery prediction.

## 🗂 Dataset
Three files describing the same industrial process at different stages:
- `gold_recovery_train.csv` — training data with target recovery values
- `gold_recovery_test.csv` — test data (no target values, used for final predictions)
- `gold_recovery_full.csv` — the complete unsplit dataset

Each dataset includes dozens of process parameters covering feed composition, reagent levels, air flow, and metal concentrations (Au, Ag, Pb) at each processing stage.

## 🔧 Approach
- Validated the provided `recovery` values by recalculating them from raw concentration data using the official recovery formula, confirming data integrity (MAE ≈ 0 after correcting a missing ×100 factor)
- Identified and handled the structural difference between train and test sets (test set lacks post-process output features by design)
- Cleaned the data: dropped rows with missing target values, aligned feature sets between train and test
- Performed exploratory analysis on metal concentration behavior across processing stages and compared feed particle size distributions between train and test sets to check for distribution shift
- Analyzed total metal concentration to detect and remove anomalous/invalid records
- Implemented a custom **sMAPE** evaluation function (the official project metric, weighted between rougher and final recovery)
- Performed model selection via cross-validation using sMAPE, comparing model families and tuning hyperparameters
- Retrained the best model on the full training set and generated final predictions on the test set

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn (Random Forest Regressor, cross-validation, custom metric implementation)

## 📈 Key Findings
- A **Random Forest Regressor (max depth 5)** achieved the lowest weighted sMAPE during cross-validation, indicating the strongest and most stable generalization among the models tested
- Consistent use of sMAPE across model selection, tuning, and evaluation ensured the metric driving decisions matched the project's real evaluation criteria
- Careful preprocessing — particularly aligning train/test feature sets and validating the recovery formula — was essential to producing a reliable model, since industrial sensor data of this kind is prone to structural inconsistencies

**Recommendations:** Integrate the model into the production pipeline for real-time recovery estimates, retrain periodically as new process data becomes available, and analyze feature importance to identify which parameters most influence recovery — turning the model into an operational tool rather than a one-off analysis.

---
*This project was completed as part of the TripleTen Data Science bootcamp.*
