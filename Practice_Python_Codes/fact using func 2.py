def fact(a):
    c=1
    while a > 0:
        c = c * a
        a = a - 1
    print(c)
a=int(input("Enter the number : "))
fact(a)
