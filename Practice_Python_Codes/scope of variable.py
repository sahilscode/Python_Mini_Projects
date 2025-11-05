a=10
def func():
    a=20
    print (a)
    print(id(a))
func()
print(a)
print(id(a))

print("--------------------------------------------------------------")

a=30
def func1():
    global a
    a=40
    print(a)
    print(id(a))
func1()
print(a)
print(id(a))

print("--------------------------------------------------------------")

a=50
def func():
    a=60
    x=globals()['a']
    print (a)
    print(id(a))
    print('x is =',x)
    print('id of x is =',id(x))
func()
print(a)
print(id(a))