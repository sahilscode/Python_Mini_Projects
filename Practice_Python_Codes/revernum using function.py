def revnum():
    l = int(input("enter the number :"))
    rev = 0
    while l > 0:
        d = l % 10
        rev = rev * 10 + d
        l = l // 10
    print("reversed number is :", rev)
revnum()