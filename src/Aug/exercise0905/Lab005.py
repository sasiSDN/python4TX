class Grand_father:
    gold="2kg"
    def house(self):
        print("Grand_father has 1bhk")
class Father(Grand_father):
    diamond="3kg"
    def house2(self):
        print("Father has 2bhk")
class Son(Father):
    bitcoi="1btc"
    def house3(self):
        print("Son has 3bhk")
obj1=Son()
obj1.house2()