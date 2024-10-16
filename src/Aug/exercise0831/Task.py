class Employee:
    def __init__(self,name,age,phone,address,eid):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.eid=eid

    def walk(self):
        print("Employee "+self.name+" walking")
    def  talk(self):
        print("Employee "+self.name+" talking")


E1=Employee(name=input("Enter your name"),age=int(input("Enter your age")),
            phone=int(input("Enter your Mobile number:")),address=input("Enter your address:"),
            eid=int(input("Enter your eid:")))
print(E1.name)
print(E1.age)
print(E1.phone)
print(E1.address)
print(E1.eid)
E1.walk()
E1.talk()

E2=Employee(name=input("Enter your name"),age=int(input("Enter your age")),
            phone=int(input("Enter your Mobile number:")),address=input("Enter your address:"),
            eid=int(input("Enter your eid:")))
print(E2.name)
print(E2.age)
print(E2.phone)
print(E2.address)
print(E2.eid)

E2.walk()
E2.talk()