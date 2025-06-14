import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_yahoo_data(tickers, start='2020-01-01', end=None):
    if end is None:
        # yfinance's 'end' is exclusive, so to get data up to yesterday, set end to today
        end = datetime.today().strftime('%Y-%m-%d')
    df = yf.download(tickers, start=start, end=end, auto_adjust=False)
    # Handle both single and multi-index columns
    if isinstance(df.columns, pd.MultiIndex):
        # Try to get 'Adj Close' if present, else fallback to 'Close'
        if 'Adj Close' in df.columns.get_level_values(0):
            df = df['Adj Close']
        elif 'Close' in df.columns.get_level_values(0):
            df = df['Close']
        else:
            raise KeyError("Neither 'Adj Close' nor 'Close' found in downloaded data.")
    else:
        # Single index columns
        if 'Adj Close' in df.columns:
            df = df['Adj Close']
        elif 'Close' in df.columns:
            df = df['Close']
        else:
            raise KeyError("Neither 'Adj Close' nor 'Close' found in downloaded data.")
    df = df.dropna()
    return df
