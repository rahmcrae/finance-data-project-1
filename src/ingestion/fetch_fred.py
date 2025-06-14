from fredapi import Fred
import pandas as pd

def fetch_fred_data(series_dict, api_key):
    fred = Fred(api_key=api_key)
    df = pd.DataFrame({name: fred.get_series(code) for name, code in series_dict.items()})
    df.index = pd.to_datetime(df.index)
    return df.dropna()
