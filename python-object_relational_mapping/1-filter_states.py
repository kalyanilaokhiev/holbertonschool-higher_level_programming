#!/usr/bin/python3
"""Write a script that lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()

    # create query
    # states with a name starting with N
    cur.execute("SELECT * FROM states "
                # binary makes it follow exactly N not n
                "WHERE BINARY name LIKE 'N%' "
                "ORDER BY id ASC")

    # fetch data and prin
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
