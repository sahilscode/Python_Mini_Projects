sal1=int(input("enter the salary : "))
i1=int(input("Enter the id : "))
n1=input("enter the name : ")
class emp:
    def __init__(self,id,name,salary):
        self.i=id
        self.n=name
        self.sal=salary
    def display(self):
        print("id is : ", self.i)
        print("name is : ",self.n )
        print("salary is : ", self.sal)

e=emp(i1,n1,sal1)
e.display()
del e.i
print(e.i)