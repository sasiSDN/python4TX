#max of 3 numbers
num1=int(input("Enter the num1:\t"))
num2=int(input("Enter the num2:\t"))
num3=int(input("Enter the num3:\t"))

if num1>num2 and num1>num3:
    print("Max number is ",num1)
elif num2>num1 and num2>num3:
    print("Max number is ", num2)
else:
    print("Max number is ", num3)

