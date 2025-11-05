import mysql.connector


mydb1=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="sahil",
    database="sahil")

mycursur=mydb1.cursor()
#mycursur.execute("create database sahil")
#mycursur.execute("show databases")
#for i in mycursur:
    #print(i)
mycursur.execute("use sahil")
mycursur.execute("alter table data modify mob numeric(10)")
#mycursur.execute('insert into data values("sahil",9685743214)')
#print(mycursur.execute("desc data"))

#mycursur.execute("create table myinfo(name varchar(20),mob numeric(10))")
#mycursur.execute("insert into myinfo(name)values ('abc')")
#mycursur.execute("select * from myinfo")
#mycursur.execute("desc data")
mycursur.execute("insert into data values('asd',9567403010)")
mydb1.commit()
mycursur.execute("select * from data")
myc=mycursur.fetchall()
for i in myc:
    print(i)