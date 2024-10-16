#create a program to sum of three numbers from user input
num1=int(input("Enter the num 1"))
num2=int(input("Enter the num 2"))
num3=int(input("Enter the num 3"))

def sum_of_three_number(n1,n2,n3):
    return n1+n2+n3
# result=sum_of_three_number(num1,num2,num3)
result=sum_of_three_number(n1=num1,n2=num2,n3=num3)
print(result)