#constructor

class Dog:
    name=None
    breed=None
    def __init__(self,name):
        self.name=name
        print("Dog is barking",name)

    def sleeping(self):
        print("Dog is sleeping"+self.name)

dog1=Dog("Chow")

dog=Dog("mow")