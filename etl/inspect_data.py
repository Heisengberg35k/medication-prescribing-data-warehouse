import pandas as pd


file_path = "data/raw/T201901PDPI BNFT.csv"

# Read only first 5 rows 
df = pd.read_csv(file_path, nrows=5)

print("Columns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())
print(df.columns.tolist())