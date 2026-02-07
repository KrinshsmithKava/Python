try:
    age = int(input("age: "))
except ValueError as ex:
    print("You didn't enter a valid age. ")
    print(ex)
    print(type(ex))
else:
    print("No exception were thrown. ")
print("Exceution continues.")


# a = 10
# b = 0

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divided bt Zero. ")
