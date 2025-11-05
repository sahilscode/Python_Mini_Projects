def fact():
    a=int(input("Enter the number : "))
    c=1
    while a > 0:
        c = c * a
        a = a - 1
    print(c)
fact()