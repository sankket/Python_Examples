#Dictionary is mutable.
person=dict(Name="Harish",Age=23,Salary=90000)
print(person)
print(person["Name"])
print("update name")
person["Name"]="Hari marllapale"
print(person["Name"])
print("add Insurance key")
person["Insurance"]="Yes"
print(person)
print("delete age")
del person["Age"]
print(person)
#print Salary of Hari
print("The salary of Hari is:")
print(person["Salary"])
