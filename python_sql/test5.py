import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)
mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
with open("aditya.csv" , "w", newline="" ) as output:
  data=csv.writer(output)
  data.writerow([i[0] for i in mycursor.description])
  data.writerow(myresult)

print(f"Data has been exported")

