import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock.db"
)

fund_master = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

nav_history = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

print("Tables Loaded Successfully")

conn.close()