from backend.portfolio_analysis.metrics import load_portfolio, fetch_live_prices, calculate_portfolio_metrics

portfolio = load_portfolio("data/sample_portfolio.csv")
tickers = portfolio["Ticker"].tolist()
live_prices = fetch_live_prices(tickers)
metrics = calculate_portfolio_metrics(portfolio, live_prices)

print("📊 Portfolio Metrics:")
for k, v in metrics.items():
    print(f"{k}: {v}")
