import sqlite3
import pandas as pd

conn = sqlite3.connect("my_db.db")
cur = conn.cursor()
df = pd.read_csv("data.csv")
df.to_sql("bodyPerformance", conn, if_exists='append', index=False)
