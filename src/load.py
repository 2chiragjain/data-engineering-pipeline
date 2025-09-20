import pandas as pd
from sqlalchemy import create_engine

def load_data():
    engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/nyc_taxi")
    df = pd.read_csv("/tmp/nyc_taxi_clean.csv")
    df.to_sql("trips", con=engine, if_exists="replace", index=False)
    print("✅ Loaded data into Postgres")
