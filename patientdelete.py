import sqlite3

connection = sqlite3.connect("hospital.db")

getpatientid = input("enter the patient id: ")

connection.execute("delete from hospitaldata where patientid="+getpatientid)
connection.commit()

print("patient Data deleted successfully")

result = connection.execute("select * from hospitaldata")

print("patient data updated")

for i in result:
    print("patientid =>", i[0])
    print("patientname =>", i[1])
    print("patientaddress =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
    print("pincode =>", i[5])

