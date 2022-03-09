import sqlite3

connection = sqlite3.connect("hospital.db")

getpatientid = input("enter the patientid")
getname = input("enter the patient name")
getaddress = input("enter the address")
getphonenumber = input("enter the phonenumber")
getemailid = input("enter the emailid")
getpincode = input("enter the pincode")


result = connection.execute("update hospitaldata set patientname='"+getname+"',patientaddress='"+getaddress+"',phonenumber="+getphonenumber+",emailid='"+getemailid+"',pincode="+getpincode+" where patientid="+getpatientid+"")
connection.commit()

print("data updated successfully")
result = connection.execute("select * from hospitaldata where patientid="+getpatientid+"")

print("patient data updated")

for i in result:
    print("patientid =>", i[0])
    print("patientname =>", i[1])
    print("patientaddress =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
    print("pincode =>", i[5])

