import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT(SELECT name FROM types WHERE id = type_id ) AS type_name,(SELECT name FROM goods WHERE id = good_id) AS good_name,price FROM price')

conn.close()