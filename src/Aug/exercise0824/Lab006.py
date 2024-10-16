#no return type no argument
def greet():
    print("Hello there")
result=greet()
print(result)

#no return type with argument
def greet(name):
    print("Hello ",name)
result=greet("sasi")
print(result)

#3. no return type with default argument

def say_hello_default_arg(name="sasi"):
    print("Hello",name)
say_hello_default_arg()
say_hello_default_arg("Naidu")
say_hello_default_arg(name="Dhara")


def multiple_arg(name1="sasi",name2="dhara",name3="naidu"):
    print("mutlple arguments",name1,name2,name3)
# multiple_arg(name1="raina",name2="dhoni",name3="Kholi")
multiple_arg(name1="raina",name2="dhoni")




#4.argument +return Type

def sum_of_two_numbers(num1,num2):
    return num1+num2

def sum_of_two_numbers(num1=200,num2=100):
    return num1+num2



#result=sum_of_two_numbers(10,20)
#result=sum_of_two_numbers(num1=30,num2=30)
result=sum_of_two_numbers()
print(result)