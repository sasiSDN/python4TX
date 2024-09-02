
#Decorators

#Decorators are two parts
#wrapper & call
def deco(fun):
    def wap2():
        print("Before the fuction")
        fun()
        print("Afeter the functionn")
        print("Safe Driving")
    return wap2()
@deco
def my_bike():
    print("Im driving")