class MyClass:
    def my_set_val(self, v):
        self.value = v

    def my_get_val(self):
        return self.value


class MyChildClass(MyClass):
    def my_set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(MyChildClass, self).my_set_val(value)


my_instance = MyChildClass()
my_instance.my_set_val(100)
print(my_instance.my_get_val())

my_instance.my_set_val(None)
print(my_instance.my_get_val())
