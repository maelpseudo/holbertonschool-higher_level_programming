#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: error")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        user=username,
        host="localhost",
        port=3306,
        password=password,
        database=db_name,
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL statement to get cities of the specified state
    statement = """SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id"""
    cursor.execute(statement, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Extract city names and print the result
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()
