import sqlite3

connection = sqlite3.connect("hospital.db")

getname = input("enter the name to be searched :")

result = connection.execute("select * from doctor where doctorname='"+getname+"'")

for i in result:
    print("name =>", i[0])
    print("qualification =>", i[1])
    print("address =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
