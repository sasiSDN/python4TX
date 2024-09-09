class Parent:
    gold="2kg"
    def house(self):
        print("Father has 2bhk")
class Child(Parent):
    def son_house(self):
        print("Child has 3bhk")
obj1=Child()
print(obj1.gold)
obj1.son_house()
