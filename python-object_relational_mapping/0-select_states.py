#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all the results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

