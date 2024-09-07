class person:
    #attributes
    name=None
    gender=None
    #behaviour

    def talk(self,name):
        print("i can talk", name)

#create an object
p1=person()
p1.name="sasi"
print(p1.name)
p1.talk("sasi")