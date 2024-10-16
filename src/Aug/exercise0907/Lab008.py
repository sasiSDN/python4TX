
#static method

class Maths():
    def div(self,a,b):
        return a/b
    @staticmethod
    def add(a,b):
        return a+b
ob1=Maths()
output=ob1.div(10,2)
print(output)
print(Maths.add(10,24))