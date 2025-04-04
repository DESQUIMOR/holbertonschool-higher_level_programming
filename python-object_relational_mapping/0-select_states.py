#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

It connects to a MySQL database using MySQLdb and retrieves all
rows from the 'states' table, displaying them in ascending order
by states.id.
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Connects to the MySQL database and prints all states in ascending order by ID.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): Name of the database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
