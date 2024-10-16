#- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1=int(input("Enter the first number:\t"))
num2=int(input("Enter the second number:\t"))
if num1>num2:
    print(num1,"is greater than",num2)
elif num1<num2:
    print(num1,"is Lesser than",num2)
else:
    print(num1,"is equals",num2)