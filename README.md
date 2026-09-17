# 🎮 Steam Games Data Analysis

## 📌 Project Overview
This project analyzes Steam game data to explore pricing patterns, player engagement, and genre performance.

The goal is to understand:
- How game prices are distributed
- Whether price relates to popularity or reviews
- Which genres perform best in terms of player base

---

## 📊 Dataset
- Source: Kaggle (Steam Games Dataset)
- This repository includes `games_sample.csv`, a sample of approximately 5,000 games used for this analysis
- Features used:
  - Price
  - Estimated Owners
  - Positive / Negative Reviews
  - Genres

---

## ⚙️ Data Processing
- Cleaned missing values
- Converted ownership estimates and review fields to numeric values
- Created:
  - `Owners_clean`
  - `Review_score`
- Removed invalid entries (e.g. zero reviews)

---

## 📈 Visualizations

### 1. Price Distribution
Shows how most Steam games are priced.
- Majority cluster around $10–$50
- Few extreme high-price outliers

### 2. Correlation Heatmap
Examines relationships between:
- Price
- Player ownership
- Review score

👉 Result: Weak correlations → pricing does not strongly determine success

### 3. Genre vs Player Base
(Boxplot, log scale)
- Action and RPG tend to have higher player counts
- Indie and Casual games show high variance

---

## 🛠️ Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📂 Files
- `steam_project.py` → main analysis script  
- `games_sample.csv` → cleaned dataset sample  
- `*.png` → visualization outputs  

---

## ▶️ How to Run

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the analysis: `python steam_project.py`

---

## 🚀 Key Insights
- Steam pricing is heavily clustered in mid-range ($10–$50)
- Popularity (owners) is not strongly correlated with price
- Genre plays a larger role in player engagement than pricing

---

## 👤 Author
Yushuo Wang  
Applied Mathematics @ UCSD  
MS in Applied Analytics @ Columbia University
