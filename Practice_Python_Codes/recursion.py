import sys
print('before setting limit ')
print(sys.getrecursionlimit())
print("after setting limit")
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

print('--------------------------------------------------')

def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
b=int(input("Enter value : "))
f=fact(b)
print("factorial is : ",f )