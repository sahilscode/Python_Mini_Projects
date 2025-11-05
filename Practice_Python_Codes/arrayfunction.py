from array import *
a=array('i',[21,23,34,45,56,67])

print(a.buffer_info())

a.reverse()
print(a)

a.append(96)
print(a)

print(a.typecode)
