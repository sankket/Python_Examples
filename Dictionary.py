#Dictionary is mutable.(The values can be chnaged)
person=dict(Name="Sanket",Age=23,Salary=52000)
print(person)
print(person["Name"])
print("update name")
person["Name"]="Sanket Godbole"
print(person["Name"])
print("add Insurance key")
person["Insurance"]="Yes"
print(person)
print("delete age")
del person["Age"]
print(person)
#print Salary of Sanket
print("The salary of Sanket is:")
print(person["Salary"])
