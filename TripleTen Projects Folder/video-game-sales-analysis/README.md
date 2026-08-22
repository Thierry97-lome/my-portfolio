# 🎮 Video Game Sales Analysis

## 📌 Project Summary
Working as an analyst for the online video game store **Ice**, this project analyzes historical video game sales data (platform, genre, regional sales, critic/user reviews, ESRB rating) to identify the patterns that determine whether a game succeeds — with the goal of informing future advertising and inventory decisions.

## 🗂 Dataset
`games.csv` — sales and review data for thousands of video games, including:
- Platform, genre, year of release
- Regional sales (NA, EU, JP, other)
- Critic score, user score, ESRB rating

## 🔧 Approach
- Cleaned and standardized column names and data types (numeric conversion, handling `'tbd'` values, missing data)
- Engineered a `total_sales` column aggregating sales across all regions
- Analyzed release trends over time and platform lifecycle (rise and decline of consoles)
- Identified the most relevant recent time period (2012–2016) for forecasting future sales, filtering out stale/declining platforms
- Examined the relationship between critic/user scores and total sales
- Compared sales performance across genres and ESRB ratings, by region
- Ran hypothesis tests (t-tests) comparing:
  - Average user ratings: Xbox One vs. PC
  - Average user ratings: Action vs. Sports genres

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy (hypothesis testing)

## 📈 Key Findings
- **PS4, Xbox One, and PC** were the dominant and fastest-growing platforms heading into 2017
- **Action, Sports, Shooter, and Role-Playing** genres led in both volume and revenue, though sales were concentrated in a small number of top titles
- ESRB rating correlates with regional performance — broad-appeal ratings like **E (Everyone)** and **T (Teen)** consistently sold well
- User ratings vary meaningfully by genre, and hypothesis testing found statistically significant differences in average user ratings between some platform and genre pairs
- Focusing on recent sales trends (2012–2016) rather than the full historical dataset avoids bias from outdated platforms and produces more reliable forecasting signals

---
*This project was completed as part of the TripleTen Data Analytics bootcamp.*
