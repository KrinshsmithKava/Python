# point = 1, 2
# point = 1
# point = 1,
# point = ()
# print(type(point))

# point = (1, 2) + (3, 4)
# point = (1, 2) * 3
# print(point)

# point = tuple([1, 2])
# point = tuple("Hello World")
# print(point)
point = (1, 2, 3)
# print(point[0])
print(point[0:2])

x, y, z = point
if 10 in point:
    print("exists")
point[0] = 10
