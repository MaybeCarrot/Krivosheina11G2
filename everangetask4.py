import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT (SELECT name FROM goods WHERE id = streams.good_id) AS good_name, price FROM price WHERE date >= "?"')

conn.close()