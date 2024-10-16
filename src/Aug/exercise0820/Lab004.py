#grade caluclator
gra=int(input("Enter your marks:\t"))
if gra>=90 and gra<=100:
    print("Your grade is:A")
elif gra>=80 and gra<=89:
    print("Your grade is:B")
elif gra>=70 and gra<=79:
    print("Your grade is:C")
elif gra>=60 and gra<=69:
    print("Your grade is:D")
elif gra>=35 and gra<=59:
    print("Your grade is:E")
elif gra<35:
    print("Your grade is:F")
else:
    print("Please Enter the valid marks")