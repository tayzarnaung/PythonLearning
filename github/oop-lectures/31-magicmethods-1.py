#!/usr/bin/env python

# 30-magicmethods-1.py

# In the backend, python is mostly objects and method
# calls on objects.

# Here we see an example, where the `print()` function
# is just a call to the magic method `__repr__()`.


class Ls(object):

    def __init__(self, my_list):
        self.ls = my_list

    def __repr__(self):
        return "repr: " + str(self.ls)

    def __str__(self):
        return "str: " + str(self.ls)

    def __add__(self, other):
        return Ls(self.ls + other.ls)


obj = Ls(["a", "b", "c"])

print(obj.__str__())
print(obj.__repr__())

print(obj)
print([obj])

print(str(obj))
print(repr(obj))

print(obj + obj)
print(obj.__add__(obj))

obj += obj
print(obj)