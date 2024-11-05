import mysql.connector
import csv

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",      # Host where the MySQL server is running
  user="root",           # MySQL username
  password="root",       # MySQL password
  database="mydatabase"  # Name of the database to connect to
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Execute the query to fetch all data from the 'customers' table
mycursor.execute("SELECT * FROM customers")

# Fetch all rows of data
myresult = mycursor.fetchall()

# Open the output CSV file in write mode
with open("aditya.csv", "w", newline="") as output:
    # Create a CSV writer object
    data = csv.writer(output)

    # Write the column headers (column names from the query result)
    data.writerow([i[0] for i in mycursor.description])

    # Write all rows of data (the result of the SELECT query)
    data.writerows(myresult)

# Print confirmation message
print(f"Data has been exported to aditya.csv")
