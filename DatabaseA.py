import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gh5@@hfE',
    database='pythontask'
)
mycursor = mydb.cursor()

sql = "INSERT INTO  users(name, email) VALUES (%s, %s)"
val =("Omer Tascan", "omertascan10@gmail.com" ) 


mycursor.execute( sql, val )


mydb.commit()

print("kayıt eklendi,ID: ", mycursor.lastrowid) 
