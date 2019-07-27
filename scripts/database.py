import sys
import sqlite3
import extract_info
import matplotlib.pyplot as PlotLib

#search_day
#search_month
#search_range_day
#search_range_month
#search_range_hour

def search_day(cursor):
    day = raw_input("Date (MM-DD-YYY): ")
    cursor.execute("SELECT * FROM infos WHERE date LIKE ?", ('%'+day+'%',))

    rows = cursor.fetchall()

    temps = []

    for row in rows:
        temps.append(extract_info.break_info(row))

    PlotLib.plot(temps)
    PlotLib.ylabel('Temperature')
    PlotLib.show()

def hour_range(rows, cursor):
    print("Aopa")

def search_month_range(x, y = -1):
    if y == -1:
        print(x)
    else:
        print (x, y)
