import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")

csv_files = list(raw_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())