class cal():
    def __init__(self,m1,m2):
        self.x=m1
        self.y=m2

    def __add__(self, other):
        self.x1=self.x + other.x
        self.y1=self.y + other.y
        z=cal(self.x1,self.y1)
        return z

m=cal(5,10)
n=cal(10,16)
z=m+n
print(z.x)
print(z.y)