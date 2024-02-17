#!/usr/bin/python3

import MySQLdb
import sys

def list_states():
    """List all the states in a MySQL database"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    info = cursor.fetchall()

    for data in info:
        print(data)

    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()
