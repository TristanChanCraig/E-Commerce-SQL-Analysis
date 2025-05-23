import sqlite3
import pandas as pd
import database_connector as dc
from statistics import mode

conn = dc.main()
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for table in tables:
    print(table[0])

df = pd.read_sql_query('SELECT * FROM albums', conn)
# print(df)

# cur.execute('INSERT INTO albums (AlbumId, Title, ArtistId) VALUES (7777, "oof", 77777)', conn)
# print(df)

cur.execute('INSERT INTO artists (ArtistID, Name) VALUES (276, "Braeden")')
df = pd.read_sql_query('SELECT * FROM artists', conn)
# print(df)


# cur.execute('SELECT * FROM playlists', conn)
# print(df)
# cur.execute('SELECT * FROM playlist_track', conn)
# print(df)
# cur.execute('SELECT * FROM tracks', conn)
# print(df) 
cur.execute('''SELECT Title, Name
FROM albums  
INNER JOIN artists 
ON albums.ArtistId = artists.ArtistId''')
result = cur.fetchall() 
# print(mode(result[1](0)), "=========================================================================")
# print(type(result), "===================================================================")
# for row in result: 
#    print(row) 

df = pd.read_sql_query('SELECT * FROM invoices', conn)
# print(df)

modeCustomerId = mode(df['CustomerId'])
print("The most frequent customer is: ", modeCustomerId)

avgTotal = df['Total'].describe()
print("The description of total invoices: ${}".format(avgTotal))

modeBillingCountry = df['BillingCountry'].describe()
print("The description of countries billed: {}".format(modeBillingCountry))

df = pd.read_sql_query('SELECT * FROM invoice_items', conn)
# print(df)

modeTrackId = df['TrackId'].mode()
# df = pd.read_sql_query('SELECT * FROM customers', conn)
# print(df)


# df = pd.read_sql_query('SELECT * FROM tracks', conn)
# print(df)
# cur.execute('''SELECT Total, UnitPrice
# FROM invoices  
# LEFT JOIN invoice_items 
# USING ('InvoiceID')''')
# result = cur.fetchall() 
# for row in result: 
#     print(row) 
# albums
# sqlite_sequence
# artists
# customers
# employees
# genres
# invoices
# invoice_items
# media_types
# playlists
# playlist_track
# tracks
# sqlite_stat1