import pandas as pd
import yfinance as yf
import numpy as np

def load_portfolio(csv_path):
    return pd.read_csv(csv_path)

def fetch_live_prices(tickers):
    # Request data with auto_adjust=False to get 'Adj Close' column
    data = yf.download(tickers, period="1d", auto_adjust=False)["Adj Close"]
    return data.iloc[-1]  # Get the latest prices

def calculate_portfolio_metrics(df, live_prices):
    df["LivePrice"] = df["Ticker"].map(live_prices)
    df["Invested"] = df["Quantity"] * df["BuyPrice"]
    df["CurrentValue"] = df["Quantity"] * df["LivePrice"]
    total_invested = df["Invested"].sum()
    total_current = df["CurrentValue"].sum()
    returns = (total_current - total_invested) / total_invested

    # Ensure weights indexed by ticker!
    weights = df.set_index("Ticker")["CurrentValue"] / total_current

    tickers = df["Ticker"].tolist()
    hist_data = yf.download(tickers, period="6mo", auto_adjust=False)["Adj Close"].pct_change().dropna()

    weights = weights.reindex(hist_data.columns).fillna(0)

    portfolio_returns = hist_data.dot(weights)

    volatility = portfolio_returns.std() * np.sqrt(252)
    risk_free_rate = 0.06
    sharpe_ratio = (portfolio_returns.mean() * 252 - risk_free_rate) / volatility

    return {
        "Total Invested": round(total_invested, 2),
        "Current Value": round(total_current, 2),
        "Overall Return": f"{returns*100:.2f}%",
        "Volatility (Ann.)": f"{volatility*100:.2f}%" if not np.isnan(volatility) else "N/A",
        "Sharpe Ratio": round(sharpe_ratio, 2) if not np.isnan(sharpe_ratio) else "N/A"
    }
