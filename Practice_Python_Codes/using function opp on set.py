from functools import *
l={1,2,3,4,5,6,7,8,9}
a=list(filter(lambda l:l%3==0,l))
print(a)
print("------------------------")
b=list(map(lambda a:a*a,a))
print(b)
print("------------------------")
c=reduce(lambda b,d:b+d,b)
print(c)