#Finding the Factorial of Number.
n  = int(input('Enter a number For Factorial:'))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)
