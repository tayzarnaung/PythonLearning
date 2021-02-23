# A classmethod is an inbuilt decorator which is called on functions via
# @classmethod.

# The @classmethod decorator marks the function/method as bound to the
# class and not to an instance.

# Remember that we used 'self' in a function within a class, which denoted
# the instance. In class methods, we use `cls` which denotes the class
# rather than the instance.

# class_1() is a class method while class_2() is an instance method.

# Class methods can be accessed by the class as well as the instance.

# Instance methods can only be accessed by the Instance.

# NOTE : For the class MyClass:
# 	MyClass is the class itself
#	MyClass() is an instance


class MyClass(object):
    @classmethod
    def class_1(cls):
        print("Class method 1")

    def class_2(self):
        print("Self/Instance method 1")


MyClass.class_1()
# MyClass.class_2()


MyClass().class_1()
MyClass().class_2()

cls_obj = MyClass()
cls_obj.class_1()
cls_obj.class_2()
