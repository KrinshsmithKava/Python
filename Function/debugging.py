def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))

# step by step debugging
# f5 for start debugging
# f10 for continue debugging to the next line and close debuging
# f11 for one by one line debugging
