a=int(input("Enter marks of first subject :"))
b=int(input("Enter marks of second subject :"))
c=int(input("Enter marks of third subject :"))
d=a+b+c
avg=d/3
print("Your average is",avg)
if avg>=75:
    print("you got 'A' grade")
elif avg>=60:
    print("You got 'B' grade")
elif avg>=50:
    print("You for 'C' grade")
elif avg>=35:
    print("You got 'D' grade")
else:
    print("You are fail")