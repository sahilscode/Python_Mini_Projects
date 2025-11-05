class even():
    def __iter__(self):
        self.a=2
        return self
    def  __next__(self):
        self.b=self.a
        if self.b<=20:
            self.a+=2
            return self.b
        else:
            raise StopIteration

e=even()
n=iter(e)
for i in n:
    print(i)