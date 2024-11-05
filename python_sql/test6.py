import mysql.connector
import csv

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Execute the query to fetch all data from the 'customers' table
mycursor.execute("SELECT * FROM customers")

# Fetch all rows of data
myresult = mycursor.fetchall()

# Open the CSV file for writing
with open("aditya.csv", "w", newline="") as output:
    # Create a CSV writer object
    data = csv.writer(output)

    # Write the column headers (column names from the query)
    data.writerow(["Name", "Address"])  # Column headers are manually specified

    # Write each row of data from the result set to the CSV file
    for row in myresult:
        data.writerow(row)

print("Data has been exported to aditya.csv")
