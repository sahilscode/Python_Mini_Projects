class sai:
    def __init__(self,name,price):
        self.n=name
        self.p=price
    def display(self):
        print(self.n)
        print(self.p)

def __main__():
    s=sai("rolex",'1,50,000')
    s.display()
if __name__ == '__main__':
    __main__()
