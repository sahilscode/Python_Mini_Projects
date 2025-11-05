class abc():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        self.x=self.a
        if self.x<=10:
            self.a+=1
            return self.x
        else:
            raise StopIteration


a1=abc()
g=iter(a1)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print()

print("-----------------------------------------")
for a in g:
    print(a)
