#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC ")

    # fetch data and print
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
