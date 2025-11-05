accno='x011223561295'
class account():
    name=input("Enter your name : ")
    branch=input("Enter branch name : ")
    type=input("Enter account type you want : ")

class saving(account):
    def show(self):
        print()
        print("dear customer ", account.name ,"you have now saving account in our bank in branch ",account.branch)
        print("Your account number is : ",accno)
        print("Interest rate is 8.5%")
        print("minimum deposit is rs1000")
        print("Daily transaction limit is 20000")

class current(account):
    def show(self):
        print()
        print("dear customer ", account.name, "you have now current account in our bank in branch ", account.branch)
        print("Your account number is : ",accno)
        print("Interest rate is 6.8%")
        print("minimum deposit is rs5000")
        print("Daily transaction limit is 100000")

a=account()

if(a.type==saving):
    s=saving()
    s.show()
else:
    c=current()
    c.show()