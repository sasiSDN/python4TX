#Take input and create a class in python

class Person:
    def __init__(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.phone=int(input("Enter your phone:"))
        self.occupation=input("Enter your occupation:")
    def print_details(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"phone is: {self.phone}")
        print(f"occupation is: {self.occupation}")


obj1=Person()
obj1.print_details()
