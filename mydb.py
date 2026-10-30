import mysql.connector

dateBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9818"
)

cursorObject = dateBase.cursor()
cursorObject.execute("CREATE DATABASE BDCRM")

print("All done!")
