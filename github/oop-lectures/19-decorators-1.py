
# Decorators are functions that compliment other functions,
# or in other words, modify a function or method.


def my_decorator(my_function):    # <-- (4)
    def my_inner_decorator():        # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()             # <-- (7)
        print("This happens after ")    # <-- (10)
        print("This happened at the end!")    # <-- (11)
    return my_inner_decorator
    # return None


@my_decorator       # <-- (3)
def normal_fun():    # <-- (2) <-- (8)
    print("This happened!")   # <-- (9)

if __name__ == '__main__':
    normal_fun()    # <-- (1)

# This prints:
# # python 19-decorators-1.py
# This happened before!
# This happened!
# This happens after
# This happened at the end!
