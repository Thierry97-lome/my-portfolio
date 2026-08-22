# 🚗 Rusty Bargain — Used Car Price Prediction

## 📌 Project Summary
Rusty Bargain, a used car sales service, is building an app that lets customers quickly find out the market value of their car. This project develops and compares machine learning models to predict used car prices from historical listing data, balancing three business priorities: **prediction quality, training speed, and prediction speed**.

## 🗂 Dataset
`car_data.csv` — over 350,000 used car listings, including:
- Vehicle details: type, brand, model, registration year/month, gearbox, power, mileage, fuel type
- Condition: whether the car has unrepaired damage
- Listing metadata: date crawled, date created, postal code

## 🔧 Approach
- Cleaned the data: filled missing categorical values (vehicle type, gearbox, model, fuel type, brand, repair status) with `"unknown"`, corrected invalid registration years, and dropped columns irrelevant to price prediction (dates, postal codes, picture counts)
- Encoded categorical features and split the data into training and test sets
- Trained and compared five regression models:
  - Linear Regression (baseline)
  - Decision Tree (with hyperparameter tuning)
  - Random Forest (with hyperparameter tuning)
  - LightGBM
  - CatBoost
- Measured **RMSE** (prediction quality), **training time**, and **prediction time** for every model to evaluate the full quality/speed tradeoff Rusty Bargain cares about

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Scikit-learn (Linear Regression, Decision Tree, Random Forest, GridSearchCV), LightGBM, CatBoost

## 📈 Key Findings
- **Random Forest** (tuned) achieved the lowest RMSE (≈ 1,800), the most accurate model overall — but with the longest training time
- **LightGBM** came in a close second on accuracy (RMSE ≈ 1,881) while training and predicting significantly faster, offering the best balance of speed and accuracy
- **CatBoost** performed well but its longer training time makes it less practical for rapid iteration or deployment
- **Linear Regression**, used as the baseline, had the highest error by far — confirming that car pricing relationships are strongly nonlinear
- **Recommendation:** LightGBM is the most practical choice for Rusty Bargain's production app — it delivers near-best accuracy with minimal latency, supporting fast, real-time price estimates at scale

---
*This project was completed as part of the TripleTen Data Science bootcamp.*
