import mysql.connector


mydb1=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="sahil",
    database="emp")

mycursor=mydb1.cursor()
#mycursor.execute("create database emp")
#mycursor.execute("show databases")
#for i in mycursor:
    #print(i)

#mycursor.execute("create table employee(id int primary key auto_increment ,name varchar(20),salary numeric(6))")
#mycursor.execute("insert into employee values(12,'sahil',10000)")
#mydb1.commit()
#mycursor.execute("insert into employee (name,salary)values('rohit',10000)")
#mycursor.execute("insert into employee (name,salary)values('patu',10000)")
#mycursor.execute("insert into employee (name,salary)values('piyu',10000)")
#mycursor.execute("insert into employee (name,salary)values('anees',10000)")
#mydb1.commit()

mycursor.execute("select * from employee")
d=mycursor.fetchall()
for i in d:
    print(i)
