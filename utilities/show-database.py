import sqlite3
from tabulate import tabulate

# Connect to the database
db = sqlite3.connect("../databases/user_database.db")
db_cursor = db.cursor()

# Execute a query to fetch all data from the table
db_cursor.execute("SELECT * FROM user_data")

# Fetch all rows from the executed query
rows = db_cursor.fetchall()

# Define the column headers
headers = ["Username", "Password Hash", "Balance"]

# Print the data in a tabular format using tabulate
print(tabulate(rows, headers, tablefmt="grid"))

# Close the database connection
db_cursor.close()
db.close()