letters = ["a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "-")
# print(letters)

# remove
letters.pop(0)
# print(letters)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
