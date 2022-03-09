import sqlite3

connection = sqlite3.connect("hospital.db")

result = connection.execute("select * from doctor")

for i in result:
    print("Name =>", i[0])
    print("qualification =>", i[1])
    print("address =>", i[2])
    print("phonenumber =>", i[3])
    print("emailid =>", i[4])

