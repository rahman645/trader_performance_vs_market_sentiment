# Trader Performance vs Market Sentiment

This project analyzes how trader behavior and performance vary under different market conditions (Fear vs Greed).

---

## Project Overview

The goal of this project is to:
- Analyze trader performance using historical trading data
- Understand behavioral patterns under different sentiment conditions
- Build a predictive model for next-day profitability
- Provide an interactive dashboard for exploration

---

## Dataset

Two datasets were used:
- `historical_data.csv` → Trader-level transaction data
- Sentiment (classification) was derived using PnL due to non-overlapping datasets

---

## Key Features

### Analysis
- Performance comparison (Fear vs Greed)
- Behavioral analysis (trade size, frequency, direction)
- Trader segmentation (risk, activity, performance)

### Predictive Model
- Predicts next-day profitability (Profit/Loss)
- Uses:
  - PnL
  - Trade size
  - Win rate
  - Sentiment (classification)
  - Trade count & volatility

### Dashboard
- Built using Streamlit
- Features:
  - Dataset overview
  - PnL distribution
  - Trader-level filtering
  - PnL trend visualization

---

## How to Run

### 1. Install dependencies
