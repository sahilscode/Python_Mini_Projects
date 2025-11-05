def add(a,*b):
    c=a
    for i in b:
        c=c+i
    return c
d=add(1,2,3,4,5,6)
print(d)