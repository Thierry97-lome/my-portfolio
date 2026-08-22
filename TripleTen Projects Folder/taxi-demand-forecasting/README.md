# 🚕 Sweet Lift Taxi — Hourly Demand Forecasting

## 📌 Project Summary
Sweet Lift Taxi company wants to predict the number of taxi orders for the next hour at airports, in order to attract more drivers during peak demand periods. This project builds a time-series forecasting model to predict hourly order volume.

**Goal:** Achieve an RMSE of **48 or lower** on the test set.

## 🗂 Dataset
`taxi.csv` — timestamped taxi order counts, resampled to hourly totals, covering **March 1 – August 31, 2018** (4,416 hourly observations).

## 🔧 Approach
- Loaded and resampled the raw data into hourly order counts
- Visualized the time series and a 24-hour rolling mean to spot trends
- Performed **seasonal decomposition** (additive, 24-hour period) to separate trend, daily seasonality, and residual noise
- Engineered time-series features: hour of day, day of week, 24 lag features, and rolling averages (3-hour, 24-hour)
- Split the data **chronologically** (not randomly) into training and test sets, respecting the time-series structure
- Trained and tuned two models:
  - **Random Forest Regressor** (hyperparameter search over depth/estimators)
  - **CatBoost Regressor**
- Attempted Auto-ARIMA (pmdarima) as a third approach, but excluded it after it caused repeated kernel crashes — a practical tradeoff documented in the analysis
- Evaluated both models on RMSE and visualized predicted vs. actual demand over the test period

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, Statsmodels (seasonal decomposition), Scikit-learn (Random Forest), CatBoost

## 📈 Key Findings
| Model | RMSE |
|---|---|
| Random Forest | 43.80 |
| **CatBoost** | **42.44** |

- **Both models beat the target RMSE of 48**, confirming strong predictive accuracy
- **CatBoost slightly outperformed Random Forest**, likely due to its gradient-boosting approach capturing subtler temporal dependencies
- Visual comparison of predicted vs. actual demand confirmed both models tracked the overall daily pattern well, with minor deviations during sharp demand spikes — typical and expected behavior in time-series forecasting

**Recommendation:** CatBoost is the preferred model for Sweet Lift's operational forecasting, offering the best accuracy of the models tested while meeting the project's performance target.

---
*This project was completed as part of the TripleTen Data Science bootcamp.*
