from src.ingestion.data_ingestion import DataIngestion, load_tickers
from src.features.compute_features import compute_features
from src.ai.summarize_with_llm import summarize_timeseries
from prometheus_client import start_http_server, Summary
import os
import json

RAW_DATA_PATH = "data/processed/financial_data.csv"
TICKERS_CONFIG_PATH = "config/tickers.json"

class Pipeline:
    def __init__(self, tickers=None, start='2020-01-01', end=None, data_path=RAW_DATA_PATH):
        if tickers is None:
            tickers = load_tickers()
        self.tickers = tickers
        self.start = start
        self.end = end
        self.data_path = data_path
        self.ingestion = DataIngestion(data_path)
        self.df = None
        self.features = None
        self.summaries = None

    def ingest(self):
        self.df = self.ingestion.fetch_yahoo(self.tickers, start=self.start, end=self.end)
        return self.df

    def analyze(self):
        if self.df is None:
            self.df = self.ingestion.load()
        self.features = compute_features(self.df)
        self.summaries = {col: summarize_timeseries(self.df[col], col) for col in self.df.columns}
        return self.features, self.summaries

    def run(self):
        self.ingest()
        features, summaries = self.analyze()
        for asset, summary in summaries.items():
            print(f"{asset}: {summary}")
        print("Last date in data:", self.df.index[-1])

def main():
    start_http_server(8000)
    REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

    tickers = load_tickers()

    @REQUEST_TIME.time()
    def run_pipeline():
        pipeline = Pipeline(tickers)
        pipeline.run()

    run_pipeline()

if __name__ == "__main__":
    main()
