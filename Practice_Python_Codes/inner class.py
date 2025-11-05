class sample:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def show(self):
        self.c=self.x+self.y
        print(self.c)
    class pra:
        def __init__(self):
            self.z=10
        def show(self):
            print("this is inner class")

s=sample(20,10)
s.show()
s1=s.pra()
s1.show()

