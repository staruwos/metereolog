import sys
import matplotlib.pyplot as PlotLib
import sqlite3

def search_day(cursor):
    day = raw_input("Date (MM-DD-YYY): ")
    cursor.execute("SELECT * FROM infos WHERE date LIKE ?", ('%'+day+'%',))

    rows = cursor.fetchall()

    for row in rows:
        print row

def hour_range(rows, cursor):
    print("Aopa") 

def search_month_range(x, y = -1):
    if y == -1:
        print(x)
    else:
        print (x, y)

#connection = sqlite3.connect("metereolog.db")
#cursor = connection.cursor()

#search_day(cursor)

def main():
    args = list(sys.argv)
    n_args = len(sys.argv)
    
    if n_args >= 2:
        if args[1] == "--range":
            print n_args
            if n_args >= 4:
                print (args[2] + ", " + args[3])

if __name__ == "__main__":
    main()

#cursor.execute("SELECT * FROM infos")

#rows = cursor.fetchall()

# 0-9: Date info
# 10, 11: comma and space
# 12-16: Time info

#for row in rows:
#    search_month_range(row[0])

