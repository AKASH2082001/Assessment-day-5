import sqlite3

connection = sqlite3.connect("hospital.db")

# connection.execute('''  Create Table hospitaldata(
#                    patientId integer primary key autoincrement,
#                    patientname text,
#                    patientaddress text,
#                    phonenumber integer,
#                    emailid text,
#                    pincode integer
#
#  )''')
print("Table Created Sucessfully")

getname = input("enter the patient name")
getaddress = input("enter the patient address")
getphonenumber = input("enter the phonenumber")
getemailid = input("enter the emailid")
getpincode = input("enter the pincode")
connection.execute("Insert into hospitaldata(patientname,patientaddress,phonenumber,emailid,pincode) values('"+getname+"','"+getaddress+"','"+getphonenumber+"','"+getemailid+"','"+getpincode+"')")


connection.commit()
connection.close()

print("Inserted Sucessfully")