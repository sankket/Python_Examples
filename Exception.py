def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")


try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")

finally:
    print("Finally Block will always executes")
    
#In The Exception Handling if you think that this block of the code will throw an error, so keep it in the try block and try to handle it catch.
#The finally block will always executes.
