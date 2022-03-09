import sqlite3

connection = sqlite3.connect("hospital.db")

# connection.execute('''  Create Table doctor(
#                    doctorname text,
#                    qualification text,
#                    address text,
#                    phonenumber integer,
#                    emailid text
#
#  )''')
print("Table Created Sucessfully")

getname = input("enter the doctor name")
getqualification = input("enter the doctor qualification")
getaddress = input("enter the address")
getphonenumber = input("enter the phonenumber")
getemailid = input("enter the emailid")
connection.execute("Insert into doctor(doctorname,qualification,address,phonenumber,emailid) values('"+getname+"','"+getqualification+"','"+getaddress+"',"+getphonenumber+",'"+getemailid+"')")

connection.commit()
connection.close()

print("Inserted Sucessfully")