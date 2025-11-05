from  array import *
a=array('i',[12,23,34,45,65,67,78,89,99,100])
print(a)
p=int(input("Enter number u want to search : "))
for i in a:
    if p==i:
        print("Number found")
else:
    print("Number not found")
