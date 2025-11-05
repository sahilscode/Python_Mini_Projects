class stud:
    def __init__(self,r,name):
        self.r1=r
        self.n1=name

    def show(self):
        print(self.r1)
        print(self.n1)

s1=stud(1,"abc")
s1.r1=4
s1.show()