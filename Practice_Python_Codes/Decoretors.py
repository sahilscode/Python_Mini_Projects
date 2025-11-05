def div(a,b):
    if a<b:
        a,b=b,a
    return a/b
c=div(2,4)
print(c)

print("---------------------------------------")
# To change the code of function externally without changing its defination

def div1(w,e):
    print(w/e)
def mdiv1(func):
    def inner(w,e):
        if w < e:
            w, e = e, w
            return func(w,e)
    return inner
divi=mdiv1(div1)
divi(3,6)


