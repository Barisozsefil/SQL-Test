#MySQL Connector İmport Etme
import mysql.connector


# Veritabanı bağlantısı kurma
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bebay19034",
  database="testmain"
)


# MySQL cursor oluşturma
mycursor = mydb.cursor()


# Yeni bir veritabanı oluşturma
#mycursor.execute("CREATE DATABASE testmain")

# Tablo oluşturma
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age VARCHAR(255))")

# Tablo Silme 
#mycursor.execute("DROP TABLE studentsss")

# Tabloya Sütun ekleme
#mycursor.execute ("ALTER TABLE students ADD city VARCHAR(255)")

# Tablo Sutün Silme
#mycursor.execute("ALTER TABLE students DROP COLUMN city")



"""
#Tablo İçeriği
sql = "INSERT INTO custumers (name, age, city) VALUES (%s,%s,%s)"

students1=[
           ("Baris",21,"mars"),
           ("Burak",21,"jupiter"),
           ("Büşra",21,"adana"),
           ("Bengi",21,"mersin"),
           ("Berkay",21,"hatay"),
]

mycursor.executemany(sql, students1)

mydb.commit()





sql = ("SELECT * FROM custumers WHERE name='Bengi' ")

mycursor.execute (sql)


myresult = mycursor.fetchall()

for row in myresult:
    print(row)




sql = "UPDATE custumers SET age = 13 WHERE name = 'Bengi' "

mycursor.execute(sql)


mydb.commit()





sql = "DELETE FROM custumers WHERE name = 'Baris'"


mycursor.execute(sql)

mydb.commit()

for x in sql:
    print(x)
    
"""