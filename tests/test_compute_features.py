import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.features.compute_features import compute_features

def test_compute_features_basic():
    df = pd.DataFrame({'AAPL': [1, 2, 4, 8]})
    features = compute_features(df)
    assert "log_returns" in features
    assert "rolling_volatility" in features
    assert "rolling_correlation" in features
    assert isinstance(features["log_returns"], pd.DataFrame)
