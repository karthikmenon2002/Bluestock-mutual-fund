import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=== Missing Values ===")
print(fund_master.isnull().sum())
print(nav_history.isnull().sum())

print("\n=== Duplicate Check ===")
print("Before:", len(nav_history))

nav_history = nav_history.drop_duplicates()

print("After:", len(nav_history))

print("\n=== Data Types Before ===")
print(nav_history.dtypes)

nav_history["date"] = pd.to_datetime(
    nav_history["date"],
    errors="coerce"
)

nav_history["nav"] = pd.to_numeric(
    nav_history["nav"],
    errors="coerce"
)

print("\n=== Data Types After ===")
print(nav_history.dtypes)

fund_master.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("\nCleaned files saved successfully.")