#
# a=132
# class person:
#     b=11   #instance variable
#
#     def pro_in(self):
#         print(a)
#         print(self.b)
# object1=person()
# object1.pro_in()


a=132
class person:
    b=11   #instance variable

    def pro_in(self):
        global a
        a="sasi"
        print(a)
        print(self.b)
object1=person()
object1.pro_in()

