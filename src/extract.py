import pandas as pd

def extract_data():
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2023-01.csv.gz"
    df = pd.read_csv(url, nrows=10000)  # sample
    df.to_csv("/tmp/nyc_taxi_raw.csv", index=False)
    print("✅ Extracted data")
