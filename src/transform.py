import pandas as pd

def transform_data():
    df = pd.read_csv("/tmp/nyc_taxi_raw.csv")
    df = df[["tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance", "fare_amount"]]
    df = df.dropna()
    df.to_csv("/tmp/nyc_taxi_clean.csv", index=False)
    print("✅ Transformed data")
