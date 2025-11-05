sal1=int(input("enter the salary : "))
i1=int(input("Enter the id : "))
n1=input("enter the name : ")
print()
class emp:
    def display(self,i,n,sal):
        print("id is : ", i)
        print("name is : ",n )
        print("salary is : ", sal)

e=emp()
e.display(i1,n1,sal1)