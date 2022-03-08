# the main idea was taken from:
# https://predictivehacks.com/newton-raphson-method-in-python/


import numpy as np
from sympy import *


def tests():
    print(find_root(lambda x: x ** 2 - 4, 1, 3) == find_root(lambda x: x ** 2 - 4, 3, 1))
    print(find_root(lambda x: x ** 3 - 100 * x ** 2 - x + 100, 0, 200)
          == find_root(lambda x: x ** 3 - 100 * x ** 2 - x + 100, 200, 0))
    try:
        find_root(lambda x: x ** 3, 0, 200)
        print("not good!")
    except ZeroDivisionError:
        print("good, exception caught successfully ")

    try:
        find_root(lambda x: x ** 3, 200, 0)
        print("not good!")
    except ZeroDivisionError:
        print("good, exception caught successfully ")


def find_root(f, first_bound, second_bound):
    # set the char x as the symbol x
    x = symbols('x')
    # find f(x) derivative
    fx_tag = f(x).diff(x)
    # set first value of x
    xn = min(first_bound, second_bound)

    # do 10 iter, enough for our need
    for i in range(10):
        # update xn by newton raphson
        if float(fx_tag.evalf(subs={x: xn})) == 0:
            raise ZeroDivisionError
        xn = xn - float(f(x).evalf(subs={x: xn})) / float(fx_tag.evalf(subs={x: xn}))
        # if its close enough
        if float(f(x).evalf(subs={x: xn})) < 0.001:
            # if we in the area of out bounds
            if min(first_bound, second_bound) < xn < max(first_bound, second_bound):
                return xn


if __name__ == '__main__':
    print(find_root(lambda x: x ** 2 - 4, -1, -3))
    print(find_root(lambda x: x ** 2 - 4, 1, 3))
    print(find_root(lambda x: x ** 3 - 100 * x ** 2 - x + 100, 0, 200))
