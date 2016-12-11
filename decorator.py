#!/usr/bin
# -*- coding: utf-8 -*-


def decorator_for_return_value_method(method):
    def wrapper(x):
        if(x > 10):
            x = 0
        return method(x)
    return wrapper


def decorator_for_no_return_method(method):
    def wrapper(x):
        if(x > 10):
            x = 0
        method(x)
    return wrapper


@decorator_for_no_return_method
def no_return_method(x):
    print x + 1


@decorator_for_return_value_method
def return_value_method(x):
    return x + 1


if __name__ == '__main__':
    no_return_method(6)
    no_return_method(12)
    print return_value_method(6)
    print return_value_method(12)
