import mysql.connector 

mydb_source=mysql.connector.connect(
    
    host="localhost",
    user="username",
    password="password",
    database=" Source database name"
    
)
mycursor_source=mydb_source.cursor()

#Hedef Dataabase 

mydb_target=mysql.connector.connect(
    
     host="localhost",
    user="username",
    password="password",
    database="Target database name"
)
mycursor_target=mydb_target.cursor()

mycursor_target.execute("CREATE TABLE otomobil_fiyatlari AS SELECT * FROM source_database_name.otomobil_fiyatlari")
#mycursor_source.execute("CREATE TABLE otomobil_fiyatlari_backup AS SELECT * FROM otomobil_fiyatlari")

#mycursor_target.execute("INSERT INTO otomobil_fiyatlari SELECT * FROM otomobil_fiyatlari_backup")

#mycursor_source.execute("DROP TABLE otomobil_fiyatlari_backup")

mydb_target.commit()

print("tablo taşaındı")

mydb_source.close()
mydb_target.close()
