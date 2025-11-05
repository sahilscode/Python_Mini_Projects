cost=int(input("Enter the cost of product :"))
selling=int(input("Enter the selling prize of product :"))
if selling>cost:
    count = selling - cost
    print("Product is in profit of ",count,"rs")
else:
    count = cost-selling
    print("Product is in loss of ", count, "rs")