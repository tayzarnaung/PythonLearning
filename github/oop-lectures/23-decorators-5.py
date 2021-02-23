# 2. Decorator function
def handle_exceptions(func_name):
    def inner(*args, **kwargs):
        try:
            return func_name(*args, **kwargs)
        except ZeroDivisionError:
            print("An exception raised : ", ZeroDivisionError)            
    return inner


# 1. Main function
@handle_exceptions
def divide(x, y):
    return x / y


# print(divide(8, 0))
print(divide(8, 2))
