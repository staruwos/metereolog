import sys
import matplotlib.pyplot as PlotLib
import sqlite3
import extract_info

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

def main():
    connection = sqlite3.connect("metereolog.db")
    cursor = connection.cursor()
    
    search_day(cursor)

if __name__ == "__main__":
    main()

#cursor.execute("SELECT * FROM infos")

#rows = cursor.fetchall()

# 0-9: Date info
# 10, 11: comma and space
# 12-16: Time info

#for row in rows:
#    search_month_range(row[0])

