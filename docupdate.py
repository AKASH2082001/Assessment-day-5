import sqlite3

connection = sqlite3.connect("hospital.db")

getname = input("enter the doctor name")
getqualification = input("enter the doctor qualification")
getaddress = input("enter the address")
getphonenumber = input("enter the phonenumber")
getemailid = input("enter the emailid")

result = connection.execute("update doctor set doctorname='"+getname+"',qualification='"+getqualification+"',address='"+getaddress+"',emailid='"+getemailid+"' where phonenumber="+getphonenumber+"")
connection.commit()

print("data updated successfully")
result = connection.execute("select * from doctor where phonenumber="+getphonenumber+"")

print("Doctor data updated")

for i in result:
    print("name =>", i[0])
    print("qualification =>", i[1])
    print("address =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
