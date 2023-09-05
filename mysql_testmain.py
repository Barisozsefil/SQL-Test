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
mycursor.execute("CREATE DATABASE testmain")


# Örnek bir Students tablo oluşturma
mycursor.execute("CREATE TABLE students (name VARCHAR(255) , age INTEGER(10)) ")


# SQL sorgusu
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
students1=("Baris",21)

mycursor.execute(sql, students1)

mydb.commit()



for x in mycursor:
    print(x)












"""



"""

