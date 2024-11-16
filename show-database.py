import sqlite3

# Connect to the database
db = sqlite3.connect("database.db")
db_cursor = db.cursor()

# Execute a query to fetch all data from the table
db_cursor.execute("SELECT * FROM user_data")

# Fetch all rows from the executed query
rows = db_cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
db.close()
