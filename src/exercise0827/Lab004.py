
def outer_fun():   #declaration
    var1=200
    def inner_fun(): #declaration
        print(var1)
    def inner_fun2(): #declaration
        print(var1)
    inner_fun()  #CALLING
    inner_fun2() #CALLING

outer_fun() # CALLING