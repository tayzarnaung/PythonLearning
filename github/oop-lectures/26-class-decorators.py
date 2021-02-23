# NOTE: When creating a decorator for a class, return a Class.

# NOTE: When creating a decorator for a function, return a function.


def add_prefix_Dr(cls):
    class MyClass(cls):
        def full_name(self):
            return "Dr. " + super(MyClass, self).full_name()
    return MyClass


@add_prefix_Dr
class ParentClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return " ".join([self.first_name, self.last_name])
        # print(" ".join([self.first_name, self.last_name]))

result = ParentClass("Tay Zar", "Naung").full_name()
print("Full name: {0}, Welcome".format(result))


# This needs further check. Erroring out.
