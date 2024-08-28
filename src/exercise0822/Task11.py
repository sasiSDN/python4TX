# Task #11 -
# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0,1, 1, 2, 3, 5, 8, 13

num=int(input("Enter a number to print fibonaci series:\n"))
num=num-2
a=0
b=1
print(a)
print(b)
while num>0:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    num=num-1
