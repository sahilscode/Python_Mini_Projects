a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a>c:
    print("a Is largest")
elif b > a and b>c:
    print("b Is largest")
elif c>a and c>b:
    print("c is largest")
else:
    print("all are equal")