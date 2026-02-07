class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)

# text = Text("Python")
# print(text.duplicate())


list = TrackableList()
list.append("1")


# Example Extend Built in Types

# class MyList(list):
#     def sum(self):
#         return sum(self)


# nums = MyList([1, 2, 3])
# print(nums.sum())
