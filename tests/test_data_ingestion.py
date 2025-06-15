import os
import pandas as pd
from src.ingestion.data_ingestion import DataIngestion

def test_fetch_yahoo(monkeypatch, tmp_path):
    # Mock yfinance download
    class DummyDF(pd.DataFrame):
        @property
        def columns(self):
            return pd.Index(['Adj Close', 'Close'])
        def dropna(self):
            return self

    def dummy_download(*args, **kwargs):
        return pd.DataFrame({'Adj Close': [1, 2, 3], 'Close': [1, 2, 3]})

    import yfinance
    monkeypatch.setattr(yfinance, "download", dummy_download)

    data_path = tmp_path / "test.csv"
    ingestion = DataIngestion(str(data_path))
    df = ingestion.fetch_yahoo(['AAPL'], start="2020-01-01", end="2020-01-03")
    assert not df.empty
    assert os.path.exists(data_path)

def test_load(tmp_path):
    data_path = tmp_path / "test.csv"
    df = pd.DataFrame({'AAPL': [1, 2, 3]}, index=pd.date_range("2020-01-01", periods=3))
    df.to_csv(data_path)
    ingestion = DataIngestion(str(data_path))
    loaded = ingestion.load()
    assert not loaded.empty
