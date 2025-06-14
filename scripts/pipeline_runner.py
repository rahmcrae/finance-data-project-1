from src.ingestion.fetch_yfinance import fetch_yahoo_data
from src.features.compute_features import compute_features
from src.ai.summarize_with_llm import summarize_timeseries
import pandas as pd
import os

RAW_DATA_PATH = "data/processed/aapl_spy.csv"

def ingester_agent(tickers, start='2020-01-01', end='2025-01-01'):
    df = fetch_yahoo_data(tickers, start=start, end=end)
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    df.to_csv(RAW_DATA_PATH)
    return RAW_DATA_PATH

def analyzer_agent(data_path):
    df = pd.read_csv(data_path, index_col=0, parse_dates=True)
    features = compute_features(df)
    # Placeholder for LLM-based analysis (could use OpenAI, etc.)
    summaries = {col: summarize_timeseries(df[col], col) for col in df.columns}
    return features, summaries

def main():
    tickers = ['AAPL', 'SPY']
    data_path = ingester_agent(tickers)
    features, summaries = analyzer_agent(data_path)
    for asset, summary in summaries.items():
        print(f"{asset}: {summary}")

if __name__ == "__main__":
    main()
