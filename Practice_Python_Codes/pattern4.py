a=int(input("enter the range :" ))
for i in range(a):
    b = a
    for j in range(i):
        print(b,end=" ")
        b=b-1
    print()