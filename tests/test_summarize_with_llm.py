import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ai.summarize_with_llm import summarize_timeseries

def test_summarize_timeseries_increasing():
    df = pd.Series([1, 2, 3, 4])
    summary = summarize_timeseries(df, "AAPL")
    assert "increasing" in summary

def test_summarize_timeseries_decreasing():
    df = pd.Series([4, 3, 2, 1])
    summary = summarize_timeseries(df, "AAPL")
    assert "decreasing" in summary
