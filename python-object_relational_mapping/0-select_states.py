#!/usr/bin/python3
"""Write a script that lists all states
from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # collecting data from input
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         password=password,
                         database=database)

    cur = db.cursor()

    # create query
    # Results must be sorted in ascending order by states.id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch data and prin
    rows = cur.fetchall()
    for row in rows:
        print(f"{row},", end=" ")

    cur.close()
    db.close()
