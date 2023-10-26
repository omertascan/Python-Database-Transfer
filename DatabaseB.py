import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database=' Target database name'  
)

mycursor = mydb.cursor()

#Create Table
#mycursor.execute("CREATE TABLE newtable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL)")
#INSERT işlemi 
sql = "INSERT INTO newtable (name, email) VALUES (%s, %s)"
val = ("Omer", "omer@example.com") 

mycursor.execute(sql, val)
mydb.commit()

#print("Tablo oluşturuldu")

print("1 kayıt eklendi, ID:", mycursor.lastrowid)

