import matplotlib.pyplot as PlotLib
import sqlite3

def search_day(cursor):
    day = raw_input("Date (MM-DD-YYY): ")
    cursor.execute("SELECT * FROM infos WHERE date LIKE ?", ('%'+day+'%',))

    rows = cursor.fetchall()

    for row in rows:
        print row

def search_month_range(x, y = -1):
    if y == -1:
        print(x)
    else:
        print (x, y)

connection = sqlite3.connect("metereolog.db")
cursor = connection.cursor()

search_day(cursor)

#cursor.execute("SELECT * FROM infos")

#rows = cursor.fetchall()

# 0-9: Date info
# 10, 11: comma and space
# 12-16: Time info

#for row in rows:
#    search_month_range(row[0])

