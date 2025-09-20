import pandas as pd
import os

def extract_data():
    url = "https://data.cityofnewyork.us/api/views/4b4i-vvec/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(url, nrows=10000)
    os.makedirs("/tmp/data", exist_ok=True)
    raw_path = "/tmp/data/nyc_taxi_raw.csv"
    df.to_csv(raw_path, index=False)
    print(f"✅ Extracted data to {raw_path}")
    return raw_path
