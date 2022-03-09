import sqlite3

connection = sqlite3.connect("hospital.db")

getphonenumber = input("enter the phonenumber: ")

connection.execute("delete from doctor where phonenumber="+getphonenumber)
connection.commit()

print("Doctor Data deleted successfully")

result = connection.execute("select * from doctor")

print("Doctor data updated")

for i in result:
    print("name =>", i[0])
    print("qualification =>", i[1])
    print("address =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
