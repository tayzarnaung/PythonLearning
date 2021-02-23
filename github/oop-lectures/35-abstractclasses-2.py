# NOTE: This code will error out. This is an example on what 
# happens when a child class doesn't implement the abstract methods
# defined in the Parent Class.

import abc


class My_ABC_Class(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        return

    @abc.abstractmethod
    def get_val(self):
        return

# Abstract Base Class defined above ^^^

# Custom class inheriting from the above Abstract Base Class, below


class MyClass(My_ABC_Class):

    def set_val(self, input):
        self.val = input

    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")

my_class = MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
