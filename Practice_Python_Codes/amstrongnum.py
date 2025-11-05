num = int(input("Enter a number: "))

sum = 0

ams = num
while ams > 0:
   digit = ams% 10
   sum += digit ** 3
   ams //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")