import os


f=open("a.txt","w")
f.write("hello friend what is going on what are u about to do ")
f.close()
f=open("a.txt","r")
#print(f.read())
#print(f.read(5))
#print(f.readline())
for z in f:
    print(z)
f.close()

try:
    os.remove("a.txt")
    f=open("a.txt","r")
except Exception as e:
    print("Exception is : ", e)
