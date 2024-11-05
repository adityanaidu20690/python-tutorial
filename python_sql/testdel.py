import mysql.connector

# Connect to MySQL server (without specifying a database)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()

# Delete the database if it exists
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")

# Commit the transaction (although DROP DATABASE doesn't require commit)
mydb.commit()

# Confirm the database deletion
print("Database 'mydatabase' has been deleted.")

# Close the cursor and connection
mycursor.close()
mydb.close()
