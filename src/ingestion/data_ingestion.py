import os
from datetime import datetime

import pandas as pd
import yfinance as yf  # type: ignore


class DataIngestion:
    def __init__(self, data_path="data/processed/financial_data.csv"):
        self.data_path = data_path
        self.df = None

    def fetch_yahoo(self, tickers, start="2020-01-01", end=None):
        if end is None:
            end = datetime.today().strftime("%Y-%m-%d")
        # Accepts list or string
        if isinstance(tickers, (list, tuple)):
            tickers_str = " ".join(tickers)
        else:
            tickers_str = tickers
        df = yf.download(tickers_str, start=start, end=end, auto_adjust=False)
        # Handle both single and multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            if "Adj Close" in df.columns.get_level_values(0):
                df = df["Adj Close"]
            elif "Close" in df.columns.get_level_values(0):
                df = df["Close"]
            else:
                raise KeyError(
                    "Neither 'Adj Close' nor 'Close' found in downloaded data."
                )
        else:
            if "Adj Close" in df.columns:
                df = df["Adj Close"]
            elif "Close" in df.columns:
                df = df["Close"]
            else:
                raise KeyError(
                    "Neither 'Adj Close' nor 'Close' found in downloaded data."
                )
        df = df.dropna()
        self.df = df
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        df.to_csv(self.data_path)
        return df

    def load(self):
        if self.df is None:
            self.df = pd.read_csv(self.data_path, index_col=0, parse_dates=True)
        return self.df
