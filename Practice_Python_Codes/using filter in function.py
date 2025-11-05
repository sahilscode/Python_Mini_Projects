def even(l):
    if l%2==0:
        return 1
l=[1,2,3,4,5,6,7,8,9]
even1=list(filter(even,l))
print(even1)

print("------------------------------------------")

#using lambda fuction in

l=[1,2,3,4,5,6,7,8,9]
c=list(filter(lambda l:l%2==0,l))
print(c)

