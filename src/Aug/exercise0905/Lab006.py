#multiple inheritance
class Father:
    def house1(self):
        print("Father's house")
class Mother:
    def house2(self):
        print("Mother's house")
class Son(Mother,Father):
    pass
obj1=Son()
# obj1.house1()
obj1.house2()