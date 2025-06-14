import numpy as np

def compute_features(price_df):
    returns = np.log(price_df / price_df.shift(1))
    vol_21d = returns.rolling(21).std()
    corr_matrix = returns.rolling(60).corr()
    return {
        "log_returns": returns,
        "rolling_volatility": vol_21d,
        "rolling_correlation": corr_matrix
    }
