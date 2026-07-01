# 📊 Customer Segmentation & Discount Recommendation App

A data-driven customer intelligence project built on the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail). It segments customers into behavioral clusters using **K-Means**, recommends personalized discount tiers, and presents the analysis through multiple deliverables — an interactive Streamlit app, a Power BI dashboard, a Jupyter notebook, and a presentation deck.

## 🗂 Project Structure

| File | Description |
|---|---|
| `project.py` | Streamlit app — interactive customer clustering & discount lookup |
| `project.ipynb` | Jupyter notebook — exploratory analysis & model development |
| `project.pbix` | Power BI dashboard — visual reporting on customer segments |
| `Customer_Intelligence_Pipeline_final.pptx` | Presentation summarizing methodology & insights |
| `data/` | Source dataset (Online Retail) |

## ✨ Features
- **Data cleaning pipeline**: handles missing values, computes total purchase value, removes outliers via Z-score filtering.
- **Customer-level aggregation**: total quantity, total sales, average unit price, invoice count, unique products per customer.
- **K-Means clustering**: segments customers into 3 tiers — *Top Customers*, *Good Customers*, *New Customers* — based on scaled behavioral features.
- **Automated discount mapping**: assigns 20% / 15% / 10% discounts by cluster, ranked by average sales.
- **Interactive customer lookup**: search any CustomerID for cluster, stats, and suggested discount.
- **Cluster summary dashboard**: sortable table of top customers and per-cluster statistics.
- **Power BI dashboard**: visual, business-facing view of segmentation results.
- **Notebook**: full exploratory data analysis and model iteration.

## 🛠 Tech Stack
Python · Pandas · NumPy · SciPy · Scikit-learn · Streamlit · Matplotlib · Power BI

## 🚀 How to Run the Streamlit App
```bash
pip install -r requirements.txt
streamlit run project.py
```
> Update the dataset path in `load_data()` (inside `project.py`) to point to your local copy of `Online Retail.xlsx`, or use the `data/` folder included in this repo.

## 📓 Notebook & Dashboard
- Open `project.ipynb` in Jupyter
- Open (https://colab.research.google.com/drive/1-H4KWrlsGp7f3RzQ3clpRFbc-emQXiAl?usp=sharing) in Colab for the full exploratory analysis.
- Open `project.pbix` in Power BI Desktop to explore the interactive dashboard.
- See `Customer_Intelligence_Pipeline_final.pptx` for a summarized walkthrough of the pipeline and findings.

## 👤 Author
George Essam and Hesham Salah
