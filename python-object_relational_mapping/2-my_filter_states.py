#!/usr/bin/python3
"""Write a script that takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()

    # create query
    # states with a name starting with N
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name = '{}' "
                "ORDER BY id ASC ".format(state_name))

    # fetch data and print
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
