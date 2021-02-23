#!/usr/bin/env python
from __future__ import print_function

# 30-staticmethod-2.py

# Refer
# https://arvimal.wordpress.com/2016/06/12/instance-class-static-methods-object-oriented-programming/

# Static methods are functions/methods which doesn’t need a binding to a class or an instance.
# Static methods, as well as Class methods, don’t require an instance to be called.
# Static methods doesn’t need  self or cls as the first argument since it’s not bound to an instance or class.
# Static methods are normal functions, but within a class.
# Static methods are defined with the keyword @staticmethod above the function/method.
# Static methods are usually used to work on Class Attributes.


class MyClass:
    # A class attribute
    count = 0

    def __init__(self, name, value):
        # print("An instance is created!")
        self.name = name
        self.age = self.filterint(value)
        MyClass.count += 1

    # Our class method
    @staticmethod
    def status():
        print("The total number of instances are ", MyClass.count)

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            # print("Entered value is not an int, value set to 0")
            return 0
        else:
            return value

print(MyClass.count)

my_func_1 = MyClass("P1", 12)
my_func_2 = MyClass("P2", 21)
my_func_3 = MyClass("P3", '40')

# print(my_func_1)

MyClass.status()
my_func_1.status()
print(MyClass.count)
