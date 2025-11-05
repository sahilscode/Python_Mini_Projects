l=[1,2,3,4,5,6,7,8,9]
c=list(filter(lambda l:l%2==0,l))
print(c)
d=list(map(lambda c:c*c,c))
print("----------------------")
print(d)
