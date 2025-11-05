l = int(input("enter the number :"))
n=l
rev = 0
while l > 0:
    d = l % 10
    rev = rev * 10 + d
    l = l // 10
if n==rev:
    print("Number is palindrom")
else:
    print("Number is not palindrom")
