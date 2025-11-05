class student():
    def disp(self):
        self.name=input("Enter name of student : ")
        self.roll=int(input("Enter the roll number : "))
class marks(student):
    def getm(self):
        self.eng=int(input("Enter marks of English : "))
        self.hin=int(input("Enter marks of Hindi : "))
        self.mat=int(input("Enter marks of Maths : "))
        self.his=int(input("Enter marks of History : "))
        self.geo=int(input("Enter marks of Geography : "))
class result(marks):
    def total(self):
        self.tot=self.eng+self.hin+self.mat+self.his+self.geo
        self.per=self.tot/5
    def show(self):
        print()
        print("Total of marks is : ", self.tot)
        print("Percentage is : ", self.per)

res=result()
res.disp()
res.getm()
res.total()
res.show()