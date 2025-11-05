class prac():
    def __init__(self,a):
        self.b=a
    def __cmp__(self, other):
        if self.b > other.b:
            #print("hiii")
            p2 = prac(self.b)
            return p2

        else:
            p2 = prac(other.b)
            return p2

p=prac(50)
p1=prac(30)
if(p.b > p1.b):
    print("hi")
    print(p.b)

