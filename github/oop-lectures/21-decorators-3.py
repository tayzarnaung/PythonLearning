# When the decorator `@my_decorator` is called, it
# takes the func `normal_func()` as its argument, and
# the argument of `normal_func()` as the argument of `inner_fun()`.
# Hence the arg `number` is passed to `num_copy`.

import datetime


def my_decorator(func):
    def inner_fun(num_copy):
        print(datetime.datetime.utcnow())
        func(int(num_copy) + 1)
        print(datetime.datetime.utcnow())
    return inner_fun


@my_decorator
def normal_func(number):
    print("This happened : " + str(number))

if __name__ == "__main__":
    normal_func(5)

# This prints:
# python 21-decorators-3.py
# 2016-05-29 12:11:57.212125
# This happened : 6
# 2016-05-29 12:11:57.212168
