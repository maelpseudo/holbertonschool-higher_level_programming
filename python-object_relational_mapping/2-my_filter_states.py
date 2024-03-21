#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the expected number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./1-filter_states.py <username> <password> <database>")
        sys.exit(1)

    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    s_n: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306
    s: str = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(s_n)

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()
    cursor.execute(s)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
