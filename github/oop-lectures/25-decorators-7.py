def double(my_func):
    def inner_func(a, b):
        return 2 * my_func(a, b)
    return inner_func


@double
def adder(a, b):
    return a + b


@double
def subtractor(a, b):
    return a - b


print(adder(10, 20))
print(subtractor(6, 1))
