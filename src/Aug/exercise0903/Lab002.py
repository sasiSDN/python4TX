class Cal:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

cal=Cal()
a=int(input("Enter  the a value:"))
b=int(input("Enter  the b value:"))
print(cal.add(a,b))
print(cal.sub(a,b))
print(cal.mul(a,b))
print(cal.div(a,b))

