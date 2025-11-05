a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a>b:
    if a>c:
        print("a is largest")
if b>a:
    if b>c:
        print("b is largest")
if c>a:
    if c>b:
        print("c is greater")
    else:
        print(" all are equal")