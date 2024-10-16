# #Task 08
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

a=int(input("Enter a value of side 1:\t"))
b=int(input("Enter a value of side 2:\t"))
c=int(input("Enter a value of side 3:\t"))
if a==b==c:
    print("It is a Equilateral triangle")
elif a==b or b==c or c==a:
    print("It is a isosceles triangle")
else:
    print("It is a scalene triangle")