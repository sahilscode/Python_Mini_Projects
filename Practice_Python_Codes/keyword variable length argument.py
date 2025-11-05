def stud(name,**b):
    print (name)
    print(b)
stud('sai',roll=1,city='isl',marks=75)

print("--------------------------------------------------------------")

def stud1(name,**b):
    print(name)
    for i,j in b:
        print(i , j)
stud('sai',roll=2,city='kol',marks=78)

print("--------------------------------------------------------------")
def stud1(name,**b):
    print(name)
    for i,j in b.items():
        print(i , j)
stud('sai',roll=2,city='kol',marks=78)