import sys
import sqlite3
import database

def main():
    connection = sqlite3.connect("metereolog.db")
    cursor = connection.cursor()

    print("""
---Options---
1-Plot Day
2-Plot Month
3-Plot Year
4-Plot Days in range
5-Plot Months in range
6-Plot Years in range
            """)

if __name__ == "__main__":
    main()

#cursor.execute("SELECT * FROM infos")

#rows = cursor.fetchall()

# 0-9: Date info
# 10, 11: comma and space
# 12-16: Time info

#for row in rows:
#    search_month_range(row[0])

