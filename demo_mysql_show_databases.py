import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="test@13579"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
