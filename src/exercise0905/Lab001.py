class My_class:
    public_var="134"
    __private_var="Secrete"  #private we cant print
    _protected="I am protected"

obj1=My_class()
print(obj1._protected)