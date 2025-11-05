class swap():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def swapping(self):
        self.temp=self.x
        self.x=self.y
        self.y=self.temp
        print("after swapping x is : ",self.x)
        print("after swappping y is : ", self.y )

    class areaC():
        def __init__(self,r):
            self.redius=r
        def calc(self):
            self.area=3.142*self.redius*self.redius
            print("area of circle is : ", self.area)

s=swap(10,20)
s.swapping()
ar=s.areaC(20)
ar.calc()

