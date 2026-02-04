def greet(name):
    print(f"Hi{name}")

# 1- perform a task
# 2- return a value

# round(1.9)


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("context.txt", "w")
# file.write(message)

print(greet("Mosh"))
