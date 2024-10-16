#- Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
import math
radius=float(input("Enter the radius of the circle:\n"))
area=3.14*math.pow(radius,2)
print(area)