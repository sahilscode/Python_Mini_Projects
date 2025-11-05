import mysql.connector

mydb1=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="sahil",
    database="info")

mycursor=mydb1.cursor()
mycursor.execute("insert into myinfo values ('abc',7620622891)")
mydb1.commit()
mycursor.execute("select * from myinfo")
d=mycursor.fetchall()
for i in d:
    print(i)