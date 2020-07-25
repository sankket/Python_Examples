string1 = str(input("Enter a string to reverse :"))


def reverse_string(string):

    for i in string:
        string = i + string
    return string


print("The original string : ", string1)

print("The reverse of the string: ", reverse_string(string1))

string2 = "my name is sanket godbole"

print(string2[::-1])
