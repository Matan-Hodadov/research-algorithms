
def tests():
    try:
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d="car", e=3)
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d=-1, e=3)
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d={}, e=3)
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d=(1, 2, "hey"), e=3)
    except TypeError:
        print("don't need to raise exceptions")

    try:
        safe_call(stam, a='5', b={'a': 3}, c=(1, 2, "hey"), d=(1, 2, "hey"), e=3)
        print("not good!")
    except TypeError:
        print("good, need to raise TypeError exception")
    try:
        safe_call(stam, a=5, b={'a': 3}, c=9, d=(1, 2, "hey"), e=3)
        print("not good!")
    except TypeError:
        print("good, need to raise TypeError exception")
    try:
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d=(1, 2, "hey"))
        print("not good!")
    except TypeError:
        print("good, need to raise TypeError exception")
    try:
        safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d=(1, 2, "hey"), e=(5))
        print("not good!")
    except TypeError:
        print("good, need to raise TypeError exception")


# safe call function
def safe_call(f, **kwargs):
    # gets a function f and other arguments
    for var_name, var_value in kwargs.items():  # for each variable that we get in kwargs
        anno_type = f.__annotations__.get(var_name, -1)  # use the annotation attribute to see
                                                         # if annotation is exists in the given function
        if anno_type == -1:  # if annotation doesnt exist, continue
            continue
        if type(var_value) != anno_type:  # if exists, check the type with the given type
            raise TypeError  # if the types are not match, raise typeError
    f(**kwargs)  # if everything is ok, call the function with the given args


def stam(a: int, b: dict, c: tuple, d, e: int):
    print("a*e =", a*e)


if __name__ == "__main__":
    # test()
    safe_call(stam, a=5, b={'a': 3}, c=(1, 2, "hey"), d="car", e=3)
    safe_call(stam, a=5, b={'a': 2}, c=(1, 2, ""), d=5, e=10)
    safe_call(stam, a=5, b={'a': 3}, c=(), d=(1, 2, ""), e=0)
