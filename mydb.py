import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shahid@786"
)

#create a cursor object
cursorObj = mydb.cursor()

cursorObj.execute("CREATE DATABASE CRMDB")

print("Database created successfully..")