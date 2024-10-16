#Method overding
#method overding means with in one or more class
class Father:
    a = 10
    def home(self):
        print("3bhk house")
class Son(Father):
    def home(self):
        super().home()
        print(super().a)
        print("no house")
ob1=Son()
ob1.home()