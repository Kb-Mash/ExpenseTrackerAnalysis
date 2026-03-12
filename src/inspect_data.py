from raw_data_loader import load_raw_data
import pandas as pd


df = load_raw_data()

print(df.head())
print()
print(df.dtypes)
