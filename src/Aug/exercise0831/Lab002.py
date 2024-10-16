class Dog:
    #attributes
    color=None
    name=None

    #behaviour
    def sleeping(self,name):
        self.name=name
        print("Dog is sleeping",name)
    def bark(self,don):
        print("Dog is barking",don)
dog1=Dog()
dog1.name="chow"
print(dog1.name)
dog1.sleeping("chow")