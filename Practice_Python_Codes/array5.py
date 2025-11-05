from array import *
s=int(input("Enter size of array : "))
a=array('i',[])
for j in range (s):
    p=int(input("Enter the element to add : "))
    a.append(p)
for k in a:
    print(k)
