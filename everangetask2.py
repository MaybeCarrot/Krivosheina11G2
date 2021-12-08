import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT name, sername, (SELECT name FROM goods WHERE id = streams.good_id) AS good_name, date  FROM client WHERE born >= "2003/01/01" ')

conn.close()