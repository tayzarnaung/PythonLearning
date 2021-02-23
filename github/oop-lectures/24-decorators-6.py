#!/usr/bin/env python


def decorator(func):
    def inner_decorator(*args, **kwargs):
        print("This function takes " + str(len(args)) + " arguments")
        func(*args)
    return inner_decorator


@decorator
def func1(string_args):
    print("This happened: " + str(string_args))


@decorator
def func2(num1, num2):
    print(f"Sum of {num1} & {num2} is {num1 + num2}" )
    # print("Sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2))


if __name__ == "__main__":
    func1("Hello")
    func2(1, 2)
