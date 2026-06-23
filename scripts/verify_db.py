import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM fund_master"
)

print("Fund Master Rows:", cursor.fetchone()[0])

cursor.execute(
    "SELECT COUNT(*) FROM nav_history"
)

print("NAV History Rows:", cursor.fetchone()[0])

conn.close()