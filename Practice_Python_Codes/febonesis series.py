times=int(input("Enter how many values you want to print : "))
init=0
init1=1
res=0
while res < times:
    print(init, end=' , ')
    nth = init1 + init
    init= init1
    init1 = nth
    res += 1