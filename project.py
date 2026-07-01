import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


@st.cache_data
def load_data():
    df = pd.read_excel("D:\VS_code\VS_code_WorkSpace\python_projects\learn\data\Online+Retail.xlsx")
    df = df.dropna(subset=['CustomerID', 'Quantity', 'UnitPrice', 'Description', 'Country'])
    df['CustomerID'] = df['CustomerID'].astype(int)
    df['TotalSum'] = df['Quantity'] * df['UnitPrice']

    cols_to_clean = ['Quantity', 'UnitPrice', 'TotalSum']
    z_scores = np.abs(stats.zscore(df[cols_to_clean]))
    df = df[(z_scores < 3).all(axis=1)]

    return df


@st.cache_data
def prepare_customer_summary(df):
    customer_summary = (
        df.groupby('CustomerID', as_index=False)
        .agg(
            total_quantity=('Quantity', 'sum'),
            total_sales=('TotalSum', 'sum'),
            average_price=('UnitPrice', 'mean'),
            invoice_count=('InvoiceNo', 'nunique'),
            unique_products=('StockCode', 'nunique'),
        )
    )

    scaler = StandardScaler()
    features = customer_summary[['total_quantity', 'total_sales', 'average_price', 'invoice_count', 'unique_products']]
    features_scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(features_scaled)
    customer_summary['cluster'] = labels

    cluster_order = (
        customer_summary.groupby('cluster')['total_sales'].mean()
        .sort_values(ascending=False)
        .index.tolist()
    )

    discount_by_cluster = {
        cluster_order[0]: 20,
        cluster_order[1]: 15,
        cluster_order[2]: 10,
    }
    customer_summary['discount_pct'] = customer_summary['cluster'].map(discount_by_cluster)

    customer_summary['cluster_name'] = customer_summary['cluster'].map(
        lambda c: 'Top Customers' if c == cluster_order[0] else 'Good Customers' if c == cluster_order[1] else 'New Customers'
    )

    return customer_summary, discount_by_cluster


def main():
    st.set_page_config(page_title='Customer Discount Report', layout='wide')

    st.title('Online Retail Customer Analysis Streamlit App')
    st.write(
        'This app loads Online Retail data, clusters customers into three groups using K-Means, '
        'and suggests a discount for each customer based on their sales behavior.'
    )

    df = load_data()
    customer_summary, discount_by_cluster = prepare_customer_summary(df)

    st.sidebar.header('Customer Search')
    customer_id = st.sidebar.number_input('Enter CustomerID', value=0, step=1)

    st.sidebar.header('Discount Rates by Cluster')
    st.sidebar.write('Top Customers: 20% discount')
    st.sidebar.write('Good Customers: 15% discount')
    st.sidebar.write('New Customers: 10% discount')

    if customer_id:
        if customer_id in customer_summary['CustomerID'].values:
            row = customer_summary[customer_summary['CustomerID'] == customer_id].iloc[0]
            st.subheader('Customer Search Result')
            st.markdown(f'- **CustomerID:** {row.CustomerID}')
            st.markdown(f'- **Cluster:** {row.cluster + 1} ({row.cluster_name})')
            st.markdown(f'- **Total Quantity:** {int(row.total_quantity)}')
            st.markdown(f'- **Total Sales:** {row.total_sales:.2f}')
            st.markdown(f'- **Average Unit Price:** {row.average_price:.2f}')
            st.markdown(f'- **Invoice Count:** {int(row.invoice_count)}')
            st.markdown(f'- **Unique Products:** {int(row.unique_products)}')
            st.markdown(f'### Suggested Discount: {row.discount_pct}%')
        else:
            st.warning('CustomerID not found. Please enter a valid value.')

    st.markdown('---')
    st.subheader('Customer Cluster Summary')
    st.dataframe(customer_summary.sort_values(by='total_sales', ascending=False).head(20))

    st.markdown('---')
    st.subheader('Cluster Details')
    cluster_stats = (
        customer_summary.groupby('cluster')
        .agg(
            customers=('CustomerID', 'count'),
            avg_sales=('total_sales', 'mean'),
            avg_quantity=('total_quantity', 'mean'),
            avg_discount=('discount_pct', 'mean'),
        )
        .reset_index()
        .sort_values(by='cluster')
    )
    st.table(cluster_stats)


if __name__ == '__main__':
    main()
