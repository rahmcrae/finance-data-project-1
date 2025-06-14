from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.ingestion.fetch_yfinance import fetch_yahoo_data

def run_ingestion():
    df = fetch_yahoo_data(['AAPL', 'SPY'])
    df.to_csv("data/processed/aapl_spy.csv")

with DAG("airflow_ingestion_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    ingest_task = PythonOperator(
        task_id="fetch_yahoo_data",
        python_callable=run_ingestion
    )
