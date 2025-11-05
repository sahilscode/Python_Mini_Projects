class test1():
    def __init__(self):
        self.mathe=20
        self.his=20
        self.geo=15

class test2():
    def __init__(self):
        self.math1 = 15
        self.his1 = 18
        self.geo1 = 15

class result(test1):
    def __init__(self):
        test1.__init__(self)
        test2.__init__(self)
        self.total=self.mathe+self.his+self.geo+self.math1+self.geo1+self.geo1
        self.avg=self.total/6

    def calc(self):
            print("total is : ", self.total)
            print("average is : ", self.avg)
res=result()
res.calc()
