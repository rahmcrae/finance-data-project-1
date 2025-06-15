from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os
import json

# Add the project root to sys.path so 'src' is importable by Airflow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.ingestion.data_ingestion import DataIngestion

TICKERS_CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config/tickers.json"))

def load_tickers(config_path=TICKERS_CONFIG_PATH):
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return [
        'AAPL', 'SPY', 'GOOG', 'MSFT', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'V',
        'UNH', 'HD', 'PG', 'MA', 'DIS', 'BAC', 'ADBE', 'CMCSA', 'NFLX', 'KO',
        'PFE', 'PEP', 'T', 'CSCO', 'XOM', 'VZ', 'ABT', 'CVX', 'WMT', 'MCD',
        'INTC', 'CRM', 'MRK', 'NKE', 'TMO', 'LLY', 'ORCL', 'COST', 'DHR', 'MDT'
    ]

def run_ingestion():
    ingestion = DataIngestion("data/processed/financial_data.csv")
    ingestion.fetch_yahoo(load_tickers())

with DAG(
    "airflow_ingestion_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    ingest_task = PythonOperator(
        task_id="fetch_yahoo_data",
        python_callable=run_ingestion,
    )
