import pandas as pd
from src.ingestion.pipeline_runner import Pipeline

def test_pipeline_ingest_and_analyze(monkeypatch, tmp_path):
    # Patch DataIngestion.fetch_yahoo to return dummy data
    dummy_df = pd.DataFrame({'AAPL': [1, 2, 3]}, index=pd.date_range("2020-01-01", periods=3))
    class DummyIngestion:
        def __init__(self, data_path): pass
        def fetch_yahoo(self, tickers, start, end): return dummy_df
        def load(self): return dummy_df

    monkeypatch.setattr("src.ingestion.pipeline_runner.DataIngestion", DummyIngestion)
    pipeline = Pipeline(['AAPL'], data_path=str(tmp_path / "test.csv"))
    pipeline.run()
    assert pipeline.df is not None
    assert pipeline.features is not None
    assert pipeline.summaries is not None
