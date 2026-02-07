
# tempertature = 15
# if tempertature > 30:
#     print("It's warm")
#     print("Drink Water")
# elif tempertature > 20:
#     print("its nice")
# else:
#     print("its cold")
# print("done")


number1 = float(input("enter first number "))
operation = input("enter the operation ")
number2 = float(input("enter second  number "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number1)
else:
    print("Enter the valid operation")
