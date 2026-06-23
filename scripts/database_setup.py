import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock.db"
)

print("Database Created Successfully")

conn.close()