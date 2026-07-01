# Customer Segmentation & Discount Recommendation App

A Streamlit web app that analyzes the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail), segments customers into behavioral clusters using **K-Means**, and recommends a personalized discount tier for each customer based on their purchasing patterns.

## Features
- **Data cleaning pipeline**: handles missing values, computes total purchase value, and removes outliers using Z-score filtering.
- **Customer-level aggregation**: total quantity purchased, total sales, average unit price, invoice count, and unique products per customer.
- **K-Means clustering**: segments customers into 3 tiers — *Top Customers*, *Good Customers*, and *New Customers* — based on scaled behavioral features.
- **Automated discount mapping**: assigns discount percentages (20%, 15%, 10%) per cluster, ranked by average sales.
- **Interactive customer lookup**: search any CustomerID to view their cluster, stats, and suggested discount.
- **Cluster summary dashboard**: sortable table of top customers and per-cluster statistics.

## Tech Stack
- Python, Pandas, NumPy, SciPy
- Scikit-learn (StandardScaler, KMeans)
- Streamlit (UI)
- Matplotlib

## How to Run
```bash
pip install -r requirements.txt
streamlit run project.py
```

> Note: update the dataset path in `load_data()` to point to your local copy of `Online Retail.xlsx`.

## Project Structure
```
├── project.py          # Main Streamlit app
└── data/
└── Online+Retail.xlsx
```

## Author
George Essam and Hesham Salah
