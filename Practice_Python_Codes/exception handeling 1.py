try:
    a=10
    b=a/0
except Exception as e:
    print("Exception occured is : ", e)
else:
    print("no exception is occured ")
finally:
    print("all excetions are handeled")

print("----------------------------------------")

try:
    a=10
    b='abc'
    c=a+b
except Exception as e:
    print("Exception is : ", e)
finally:
    print("done")