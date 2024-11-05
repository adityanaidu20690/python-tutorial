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

# Connect to MySQL server (not specifying the database initially)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

# Create the database if it does not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# Switch to the created database
mycursor.execute("USE mydatabase")

# Create the 'customers' table if it doesn't already exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        name VARCHAR(255),
        address VARCHAR(255)
    )
""")

# Insert multiple rows into the 'customers' table
quer = "INSERT INTO customers (name, address) VALUES (%s, %s)"
value = [
    ("Aditya", "Hyd"),
    ("arun", "bang"),
    ("vijay", "Rajasthan"),
    ("srikar", "Hyd")
]

# Execute multiple inserts using executemany()
mycursor.executemany(quer, value)

# Commit the transaction
mydb.commit()

# Print the number of records inserted
print(mycursor.rowcount, "data inserted")

# Close the cursor and database connection
mycursor.close()
mydb.close()