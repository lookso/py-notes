import datetime
import time
import os
import mysql.connector

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.time())
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d"))

f = open("demofile2.txt", "a+")
f.write("Now the file has more content!\n")

print(f.read())
f.close()
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")

txt = "Hello World"[::-1]
print(txt)

# pip3 install mysql-connector-python
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="123456",
                               database="tools",
                               buffered=True)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor)
tag = 0
for x in mycursor:
    if "customers" in x:
        tag = 1
        break

if tag == 0:
    mycursor.execute(
        "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
