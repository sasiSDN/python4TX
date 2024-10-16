try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a/b
except ValueError as ve:
    print("valueerror, you have entered string insted number")
except ZeroDivisionError as ze:
    print("don't enter 0 for b")
else:
    print(c)
finally:
    print("program completded successfully")