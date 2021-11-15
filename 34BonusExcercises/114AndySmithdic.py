names = {"firstname" : "Andy", "lastname": "Smith"}
print(names)
for key in names:
    print(key)
    print(names[key])
print("Welcome {firstname} {lastname} to our shop!".format(firstname=names["firstname"], lastname=names["lastname"]))
