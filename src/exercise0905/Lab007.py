
#heirachy
class Father:
    def house1(self):
        print("father's house")
class Son1(Father):
    def house2(self):
        print("Son1 house")
class Son2(Father):
    def house3(self):
        print("son2 house")
obj1=Son2()
obj1.house3()