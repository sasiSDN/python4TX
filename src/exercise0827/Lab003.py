#function Scope
global_Var=13
def my_fun():
    a=10
    print(a)
    print(global_Var)

def f1():
    print(global_Var)
# print(a)
my_fun()
print(global_Var)
f1()