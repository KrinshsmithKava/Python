try:
    file = open("cleaningup.py")
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age. ")
else:
    print("No exception were thrown. ")
finally:
    file.close()
