class emp:
    def __init__(self,id,name,salary):
        self.i=id
        self.n=name
        self.sal=salary
    def display(self):
        print("id is : ", self.i)
        print("name is : ",self.n )
        print("salary is : ", self.sal)

e=emp(1,"sai",10000)
e.display()


        