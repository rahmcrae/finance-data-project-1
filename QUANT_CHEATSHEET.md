# 🧠 Quantitative Finance Cheat Sheet

---

## 📈 Correlation & Time Series Analysis

| Concept | Description | Why It Matters |
|--------|-------------|----------------|
| **Log Returns** | `log(P_t / P_{t-1})` | Returns are additive; stabilizes variance |
| **Rolling Correlation** | `corr(windowed_returns_a, b)` | Shows changing relationships over time |
| **Pearson Correlation** | Measures linear relationship | Helps with asset clustering and diversification |
| **Spearman Correlation** | Measures monotonic rank-order relationship | Useful when returns are non-linear |
| **Granger Causality** | Does A help predict B? | Great for macro forecasting and lead-lag detection |

---

## 📉 Risk Modeling

| Metric | Formula (simplified) | Purpose |
|--------|----------------------|---------|
| **Volatility (σ)** | `std(log_returns)` | Measures spread of returns |
| **Beta (β)** | `cov(R_asset, R_market) / var(R_market)` | Systematic risk: sensitivity to market moves |
| **VaR (Value at Risk)** | `quantile(returns, α)` | Max expected loss at confidence level |
| **CVaR (Expected Shortfall)** | `mean(returns < VaR)` | Average loss when VaR is breached |
| **Drawdown** | `peak - trough` | Max observed loss from a high point |
| **Sharpe Ratio** | `(mean_return - r_f) / std_dev` | Risk-adjusted return |

---

## 💼 Portfolio Construction

| Concept | Description | Why It Matters |
|--------|-------------|----------------|
| **Mean-Variance Optimization** | Minimize risk for a target return | Foundation of modern portfolio theory |
| **Efficient Frontier** | Curve showing optimal portfolios | Helps visualize trade-offs |
| **Risk Parity** | Allocate capital to equalize risk per asset | Often more robust than equal-weighting |
| **Monte Carlo Simulation** | Simulate random future paths | Stress-test strategies under uncertainty |
| **Backtesting** | Apply strategy to historical data | Validates hypotheses and performance |

---

## 🛠️ Data Engineering & AI Layer

| Layer | Tool | Purpose |
|-------|------|---------|
| **Ingestion** | `yfinance`, `fredapi` | Market & macroeconomic data |
| **Storage** | `Parquet`, `Snowflake` | Scalable time-series storage |
| **Feature Engineering** | `pandas`, `numpy` | Compute returns, vol, beta, etc. |
| **LLM Summaries** | OpenAI, Anthropic | Auto-generate insight & anomaly reports |
| **Visualization** | `seaborn`, `matplotlib` | Communicate patterns and risk clearly |

---

## 📌 Common Pitfalls

| Mistake | Consequence |
|--------|-------------|
| Assuming normal distribution | Underestimates tail risk (black swans) |
| Using static correlation | Misses risk regime shifts |
| Ignoring fees/slippage in backtests | Overstates profitability |
| Overfitting to historical data | Fails to generalize to future |

---

## 🧭 Suggested Next Steps

1. Pull asset & macro data (e.g. AAPL, SPY, CPI, 10Y rates)
2. Compute: log returns, volatility, beta, VaR
3. Visualize: rolling correlations, drawdowns, efficient frontier
4. Summarize: AI-generated markdown/HTML reports
5. Simulate: Monte Carlo paths, backtest rules
6. Deploy: Streamlit dashboard or CI notebook renderer
