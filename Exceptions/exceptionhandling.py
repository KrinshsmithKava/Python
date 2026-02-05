try:
    age = int(input("age: "))
except ValueError as ex:
    print("You didn't enter a valid age. ")
    print(ex)
    print(type(ex))
else:
    print("No exception were thrown. ")
print("Exceution continues.")
