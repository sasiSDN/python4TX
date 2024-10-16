

try:
    a = int(input("Enter your first number"))
    b = int(input("Enter your second number"))

    c = a + b
    print(c)
except Exception as e:
    print("Invalid input")
