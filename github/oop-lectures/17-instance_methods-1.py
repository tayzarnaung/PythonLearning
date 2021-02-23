# Instance methods are also known as Bound methods since the methods
# within a class are bound to the instance created from the class, via
# 'self'.


class A:
    def method(*argv):
        return argv

a = A()
print(a.method)
# <bound method A.method of <__main__.A object at 0x7fc91d83e790>>
