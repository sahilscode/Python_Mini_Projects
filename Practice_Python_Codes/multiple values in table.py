import mysql.connector


mydb1=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="sahil",
    database="emp")

mycursor=mydb1.cursor()
#query="insert into employee(name,salary)values(%s,%s)"
#a=[('asd1',122),('dfg1',566),('ghj1',987),('jhi',653),('kij',869)]
#mycursor.executemany(query,a)
#mydb1.commit()
#mycursor.execute("select * from employee")
#d=mycursor.fetchall()
#for i in d:
    #print(i)
#mycursor.execute("select id from employee")
#e=mycursor.fetchone()
#print(e)
#mycursor.execute("select name,salary from employee where id=63")
#h=mycursor.fetchall()
#for i in h:
    #print(i)

#mycursor.execute("select name from employee")
#h1=mycursor.fetchall()
#for j in h1:
    #print(j)

#mycursor.execute("select * from employee where salary<=500")
#g1=mycursor.fetchall()
#for k in g1:
    #print(k)

#mycursor.execute("select * from employee where id<=30 and id>=20")
#f=mycursor.fetchall()
#for l in f:
    #print(l)

#mycursor.execute("select * from employee order by name desc")
#v=mycursor.fetchall()
#for y in v:
    #print(y)


#mycursor.execute("delete from employee  where id =3 or salary<500")
#mydb1.commit()
#mycursor.execute("select * from employee")
#m=mycursor.fetchall()
#for s in m:
   #print(s)


#mycursor.execute("update employee set salary=900 where id=2")
#mydb1.commit()
#mycursor.execute("select * from employee")
#m=mycursor.fetchall()
#for s in m:
    #print(s)