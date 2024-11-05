import mysql.connector
import csv

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",        # Host where the MySQL server is running
  user="root",             # MySQL username
  password="root",         # MySQL password
  database="mydatabase"    # Database to connect to
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Execute the SQL query to fetch all data from the 'customers' table
mycursor.execute("SELECT * FROM customers")

# Fetch all rows of data from the query result
myresult = mycursor.fetchall()

# Open the output CSV file in write mode
with open("aditya.csv", "w", newline="") as output:
    # Create a CSV writer object to write data to the file
    data = csv.writer(output)

    # Write the column headers (the names of the columns)
    # These headers are manually specified in this case
    data.writerow(["Name", "Address"])

    # Write each row of data (from the query result) into the CSV file
    for row in myresult:
        data.writerow(row)

# Print a message confirming that the data has been exported
print("Data has been exported to aditya.csv")
