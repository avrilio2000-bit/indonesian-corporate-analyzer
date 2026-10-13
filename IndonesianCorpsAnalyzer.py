import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "AMRT.JK"
raw_data = yf.Ticker(ticker).financials.T

# grab revenue and net income, scale to trillions
df = raw_data[["Total Revenue", "Net Income"]].dropna() / 1e12
df.index = pd.to_datetime(df.index).year

# plot
df.plot(kind="bar", color=["#1f77b4", "#ff7f0e"], edgecolor="black")
plt.title(f"{ticker} Revenue vs Net Income")
plt.ylabel("IDR (Trillions)")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.5)
plt.tight_layout()
plt.show()
