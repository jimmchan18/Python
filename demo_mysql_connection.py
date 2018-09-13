import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="test@13579"
)

print(mydb) 
