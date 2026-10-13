import yfinance as yf
import pandas as pd
import streamlit as st

st.set_page_config(page_title="IDX Financials", layout="wide")

st.title("Indonesian Stock Analyzer")
st.write("Track multi-year financial trends for equities on the Indonesia Stock Exchange.")

user_input = st.text_input("Ticker symbol (e.g., AMRT, BBCA, TLKM, UNVR):", "AMRT")

if user_input:
    ticker = user_input.strip().upper()
    if not ticker.endswith(".JK"):
        ticker += ".JK"

    try:
        stock = yf.Ticker(ticker)
        raw_data = stock.financials.T

        # get official company name
        company_name = stock.info.get("longName", ticker)
        st.subheader(company_name)

        # detect currency &  scale
        currency = stock.fast_info.get("currency", "IDR")
        if currency == "IDR":
            scale = 1e12
            unit = "Trillions IDR"
        else:
            scale = 1e9
            unit = "Billions USD"

        # clean and sort years chronologically
        df = raw_data[["Total Revenue", "Net Income"]].dropna() / scale
        df.index = pd.to_datetime(df.index).year
        df = df.sort_index()

        # calculate profit margin %
        df["Profit Margin (%)"] = (df["Net Income"] / df["Total Revenue"]) * 100

        # latest year metrics
        latest_year = df.index[-1]
        latest_rev = df["Total Revenue"].iloc[-1]
        latest_inc = df["Net Income"].iloc[-1]
        latest_margin = df["Profit Margin (%)"].iloc[-1]

        # display metric cards
        col1, col2, col3 = st.columns(3)
        col1.metric(label=f"{latest_year} Revenue ({unit})", value=f"{latest_rev:.2f}")
        col2.metric(label=f"{latest_year} Net Income ({unit})", value=f"{latest_inc:.2f}")
        col3.metric(label=f"{latest_year} Profit Margin", value=f"{latest_margin:.1f}%")

        # line chart
        st.subheader("Revenue vs Net Income Trend")
        st.line_chart(df[["Total Revenue", "Net Income"]], color=["#1f77b4", "#2ca02c"])

        # collapsible raw data table wowzie
        with st.expander("View Raw Data Table"):
            st.dataframe(df.style.format("{:.2f}"))

    except Exception:
        st.error(f"Couldn't pull data for '{ticker}'. Make sure it's a valid symbol.")
