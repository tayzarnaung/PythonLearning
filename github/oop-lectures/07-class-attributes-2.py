# a) A class attribute can be overridden in an instance, even
# though it is bad due to breaking Encapsulation.

# b) There is a lookup path for attributes in Python. The first being
# the method defined within the class, and then the class above it.

# When classy' class attribute in the instance 'dd' is overridden, the python interpreter reads the overridden value.
# But once the new value is deleted with 'del', the overridden value is no longer present in the instance, and hence the lookup goes a level above and gets it from the class.


class YourClass(object):
    classy = "class value"

    def f(self):
        print(YourClass.classy, ", ", self.classy)

dd = YourClass()
# print(dd.classy)  # "class value"
dd.f()

dd.classy = "Instance value"
# print(dd.classy)    # "Instance value"
dd.f()

# This will delete the value set for 'dd.classy' in the instance.
del dd.classy
# Since the overriding attribute was deleted, this will print 'class value'.
print(dd.classy)  # "class value"
