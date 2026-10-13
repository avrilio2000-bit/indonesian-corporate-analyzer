# Indonesian Stock Analyzer

A web app built with Python and Streamlit to visualize financial performance for equities listed on the Indonesia Stock Exchange (IDX). It pulls live income statement data from Yahoo Finance to track Revenue, Net Income, and Profit Margins over time.

### Features
* **Live IDX Integration**: Automatically formats Indonesian tickers (e.g., `AMRT`, `BBCA`, `TLKM`) to fetch live data.
* **Financial Metrics**: Displays latest fiscal year Total Revenue, Net Income, and Profit Margin percentages.
* **Trend Visualization**: Plots multi-year financial trends with interactive line charts.
* **Raw Data Inspector**: Includes an expandable table to view raw figures.

### Requirements
```bash
pip install -r requirements.txt
```

### How to Run Locally
1. Clone or download this repo, then open your terminal inside the project folder (or use `cd`):
```bash
cd indonesian-corporate-analyzer
```
2. Run the app
```bash
streamlit run app.py
```
