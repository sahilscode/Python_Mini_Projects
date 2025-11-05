class addition():
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            self.addi=a+b+c+d
            print("addition is : ", self.addi)
        elif a!=None and b!=None and c!=None and d==None:
            self.addi = a + b + c
            print("addition is : ", self.addi)
        elif a!=None and b!=None and c==None and d==None:
            self.addi = a + b
            print("addition is : ", self.addi)
        elif a != None and b == None and c == None and d == None:
            self.addi = a
            print("addition is : ", self.addi)
        else:
            print("addition is 0")


a1=addition()
a1.add()
a1.add(30)
a1.add(30,20)
a1.add(30,20,40)
a1.add(30,20,40,60)
