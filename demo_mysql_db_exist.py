import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="test@13579",
  database="wordpress"
)


#If this page is executed with no error, the database "mydatabase" exists in your system
