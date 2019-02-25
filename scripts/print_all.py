import sqlite3

connection = sqlite3.connect("metereolog.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM infos")

rows = cursor.fetchall()

for row in rows:
    print(row)
