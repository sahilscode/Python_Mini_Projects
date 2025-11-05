class area():
    def calc(self,a=None,b=None):
        if a!=None and b!=None:
            print ("area of rectangle is : ", a*b)
        if a!=None and b==None:
            print("area of square is : ", a*a)

a=area()
a.calc(20,30)
a.calc(20)