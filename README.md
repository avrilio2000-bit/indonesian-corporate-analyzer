Indonesian Corporate Financial Analyzer

A Python data analysis project that retrieves financial data for Indonesian companies using Yahoo Finance and visualizes revenue and net income over time.

What it does

* Retrieves income statements directly from Yahoo Finance using `yfinance`.
* Converts large Indonesian Rupiah (IDR) figures into trillions for better readability.
* Uses `pandas` to process financial data and `matplotlib` to visualize revenue and net income in a bar chart.
* Uses Alfamart (`AMRT.JK`) as an example to analyze corporate financial performance over time.

Tools Used

* Python 3.x
* `yfinance` (Financial Data Retrieval)
* `pandas` (Data Processing & Analysis)
* `matplotlib` (Data Visualization)
* Yahoo Finance (Financial Data Source)

How to run

1. Open your terminal or command prompt.
2. Install the required packages:
   ```bash
   pip install yfinance pandas matplotlib
   ```
3. Save the Python script to your local machine.
4. Run the script:
   ```bash
   python main.py
   ```
