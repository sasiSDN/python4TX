#OVERLOADING
# method overloading means with in the class
class Math(object):
    def add(self,a,b):
        return  a+b
    def add(self,a,b,c=0):
        return  a+b+c

ob1=Math()
print(ob1.add(2,3))