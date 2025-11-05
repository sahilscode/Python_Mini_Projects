try:
    print(x)
except Exception as e:
    print("exception occured",e)
finally:
    print("all exceptions are handeled")