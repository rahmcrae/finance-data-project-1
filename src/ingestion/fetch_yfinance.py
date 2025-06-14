import yfinance as yf
import pandas as pd

def fetch_yahoo_data(tickers, start='2020-01-01', end='2025-01-01'):
    # Explicitly set auto_adjust to False to preserve old behavior if needed
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
