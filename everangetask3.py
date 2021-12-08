import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT name, kol FROM goods WHERE type_id = (SELECT id FROM types WHERE name = "?") ')

conn.close()