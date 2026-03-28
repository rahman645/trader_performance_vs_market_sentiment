import streamlit as st
import pandas as pd

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("historical_data.csv")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Trader Performance vs Market Sentiment Dashboard")

# -----------------------------
# Basic Overview
# -----------------------------
st.subheader("Dataset Overview")
st.write(df.describe())

# -----------------------------
# PnL Distribution
# -----------------------------
st.subheader("PnL Distribution")
st.bar_chart(df['Closed PnL'])

# -----------------------------
# Trader Selection
# -----------------------------
st.subheader("Trader Analysis")

account = st.selectbox("Select Account", df['Account'].unique())

filtered_df = df[df['Account'] == account]

st.write("Selected Trader Data:")
st.write(filtered_df.head())

# -----------------------------
# PnL Trend
# -----------------------------
st.subheader("PnL Trend")
st.line_chart(filtered_df['Closed PnL'])