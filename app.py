import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide", page_title="Telecom Dashboard")

# Use raw string (r"") to handle backslashes in Windows paths
df1 = pd.read_csv(r"C:\New folder\telcom_data2.csv")

# Optional preview
st.write(df1.head())


st.sidebar.header("Filter Options")
if 'region' in df1.columns:
    selected_regions = st.sidebar.multiselect("Select Region", df1['region'].dropna().unique())
    if selected_regions:
        df1 = df1[df1['region'].isin(selected_regions)]

# Show some basic metrics
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", f"{len(df1):,}")

if 'Monthly Charges' in df1.columns:
    col2.metric("Average Monthly Charges", f"${df1['Monthly Charges'].mean():.2f}")
else:
    col2.write("Monthly Charges column not found")

if 'Churn Label' in df1.columns:
    churn_rate = df1['Churn Label'].value_counts(normalize=True).get('Yes', 0) * 100
    col3.metric("Churn Rate", f"{churn_rate:.2f}%")
else:
    col3.write("Churn Label column not found")

# Visualization examples
if 'region' in df1.columns:
    st.subheader("🗺️ Customers by Region")
    fig1 = px.histogram(df1, x='region')
    st.plotly_chart(fig1, use_container_width=True)

if 'Churn Label' in df1.columns:
    st.subheader("🔁 Churn Distribution")
    fig2 = px.pie(df1, names='Churn Label', title='Churn Rate Breakdown')
    st.plotly_chart(fig2, use_container_width=True)

# Show raw data
st.subheader("📄 Raw Data Preview")
st.dataframe(df1)
