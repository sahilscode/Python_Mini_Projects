def sub(a,b):
    if a<b:
        a,b=b,a
    return a-b
c=sub(2,4)
print(c)

print("---------------------------------------")
# To change the code of function externally without changing its defination

def sub1(w,e):
    print(w-e)
def nsub1(func):
    def inner(w,e):
        if w < e:
            w, e = e, w
            return func(w,e)
    return inner
subt=nsub1(sub1)
subt(3,6)
