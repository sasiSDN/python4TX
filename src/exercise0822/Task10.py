# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

num=int(input("Enter the factorial of a number:\n"))
b=1
for i in range(num,0,-1):
    a=b*i
    b=a
print(b)



