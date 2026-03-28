import streamlit as st
import pandas as pd

# -----------------------------
# Title
# -----------------------------
st.title("Trader Performance vs Market Sentiment Dashboard")

# -----------------------------
# Load data safely
# -----------------------------
try:
    df = pd.read_csv("https://drive.google.com/file/d/1wlp-kLAc8UiCir-XvlHNeiabICOzF3WC/view?usp=drive_link")
except:
    st.error("Dataset not found. Please upload 'historical_data.csv'")
    st.stop()

# -----------------------------
# Basic Info
# -----------------------------
st.subheader("Dataset Overview")

st.write("Total Records:", len(df))
st.write(df.describe())

# -----------------------------
# PnL Distribution
# -----------------------------
st.subheader("PnL Distribution")

# limit rows for better visualization
st.bar_chart(df['Closed PnL'].head(100))

# -----------------------------
# Trader Selection
# -----------------------------
st.subheader("Trader Analysis")

accounts = df['Account'].unique()
account = st.selectbox("Select Account", accounts)

filtered_df = df[df['Account'] == account]

# sort if timestamp exists
if 'Timestamp' in filtered_df.columns:
    filtered_df = filtered_df.sort_values('Timestamp')

st.write("Selected Trader Data:")
st.write(filtered_df.head())

# -----------------------------
# PnL Trend
# -----------------------------
st.subheader("PnL Trend")

st.line_chart(filtered_df['Closed PnL'])
