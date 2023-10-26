import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='username ',
    password='password',
    database='database name'
)
mycursor = mydb.cursor()

sql = "INSERT INTO  users(name, email) VALUES (%s, %s)"
val =("Omer ", "omer@gmail.com" ) 


mycursor.execute( sql, val )


mydb.commit()

print("kayıt eklendi,ID: ", mycursor.lastrowid) 
