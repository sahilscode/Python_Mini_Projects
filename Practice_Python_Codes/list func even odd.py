l=[1,2,3,4,5,6,7,8,9,10]
def func(l):
    count_even=0
    count_odd=0
    for i in l:
        if(i%2==0):
            count_even=count_even+1
        else:
            count_odd=count_odd+1

    print("total even numbers are :",count_even)
    print("total odd numbers are :",count_odd)


func(l)
