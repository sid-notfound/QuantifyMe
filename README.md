
# QuantifyMe

QuantifyMe is a Python-based portfolio analysis tool that fetches live stock prices, calculates key portfolio metrics, and helps users track their investments effectively.

## Features

- Load portfolio data from CSV files
- Fetch live stock prices using Yahoo Finance API (`yfinance`)
- Calculate portfolio metrics including:
  - Total Invested
  - Current Value
  - Overall Return (%)
  - Annualized Volatility (%)
  - Sharpe Ratio
- Easy to extend and customize

## Getting Started

### Prerequisites

- Python 3.7+
- `yfinance`
- `pandas`
- `numpy`

You can install the required packages using:

```bash
pip install -r requirements.txt


Organization: 

QuantifyMe/
├── backend/
│   └── portfolio_analysis/
│       └── metrics.py       # Core portfolio calculation logic
├── data/
│   └── sample_portfolio.csv # Sample portfolio data
├── main.py                  # Entry point of the project
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
