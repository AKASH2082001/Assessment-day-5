import sqlite3

connection = sqlite3.connect("hospital.db")

result = connection.execute("select * from hospitaldata")

for i in result:
    print("patientid =>", i[0])
    print("patientname =>", i[1])
    print("patientaddress =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])
    print("pincode =>", i[5])

