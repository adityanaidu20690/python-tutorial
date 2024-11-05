# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# quer = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# value = [("Aditya", "Hyd"),
#          ("arun", "bang"),
#          ("vijay", "Rajasthan")]
# mycursor.execute(quer, value)

# mydb.commit()
# print(mycursor.rowcount, "data inserted")

################################
# to fetch the data
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
#################################
# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM movies.moviesdb")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# mycursor = mydb.cursor()



# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
import mysql.connector

# Connect to MySQL server (without specifying a database initially)
mydb = mysql.connector.connect(
  host="localhost",  # Host where the MySQL server is running
  user="root",       # MySQL username (root in this case)
  password="root"    # MySQL password (replace with actual password)
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Create the 'mydatabase' if it does not already exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# Switch to the 'mydatabase' to work on it
mycursor.execute("USE mydatabase")

# Create the 'customers' table if it does not already exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        name VARCHAR(255),   # Column for storing names of customers
        address VARCHAR(255) # Column for storing address of customers
    )
""")

# Insert multiple records into the 'customers' table
quer = "INSERT INTO customers (name, address) VALUES (%s, %s)"
value = [
    ("Aditya", "Hyd"),
    ("arun", "bang"),
    ("vijay", "Rajasthan"),
    ("srikar", "Hyd")
]

# Execute multiple insert operations in one go using executemany()
mycursor.executemany(quer, value)

# Commit the transaction to the database
mydb.commit()

# Print the number of records inserted
print(mycursor.rowcount, "data inserted")

# Close the cursor and database connection
mycursor.close()
mydb.close()
