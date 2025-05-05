import sqlite3
import pandas as pd
import database_connector as dc

conn = dc.main()
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for table in tables:
    print(table[0])

df = pd.read_sql_query('SELECT * FROM albums', conn)
print(df)

cur.execute('DELETE', conn)