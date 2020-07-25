#Fibonnaci Series
a = int(input("Enter First Number:"))
b = int(input("Enter Second number"))
n = int(input("How many numbers you want in Series"))

print(a,b)

while(n>=0):
    c =a + b
    a=b
    b=c
    print(c)
    n=n-1

# 1 2 3 5 8 13 21 .....
