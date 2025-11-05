i=int(input("Enter the number : "))
for a in range(2,i) :
    if i%a==0:
        print("Number is not prime")
        break
else:
    print("number is prime")