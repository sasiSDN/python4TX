class Father:
    house="2bhk"
    def car(self):
        print("Father has car: ALTO")

class Son(Father):
    def car(self):
        print("son has: Lambo")
obj1=Son()
obj1.car()