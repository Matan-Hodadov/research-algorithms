last_call = ""


def lastcall(func):
    def wrapper(*args, **kwargs):
        return_val = func(*args, *kwargs)
        global last_call
        if type(last_call) == type(return_val):
            if last_call != return_val:
                # last_call = return_val
                print(return_val)
                last_call = return_val
            else:
                print("I already told you that the answer is", str(return_val) + "!")
        else:
            last_call = return_val
            print(return_val)
        return return_val
    return wrapper


@lastcall
def int_example(num: int) -> int:
    return num ** 2


@lastcall
def int_example2(num1: int, num2: int) -> int:
    return num1 * num2


@lastcall
def float_example(num: float) -> float:
    return round(num - 7.53, 2)


@lastcall
def string_example(str: str) -> str:
    return str


if __name__ == '__main__':
    # test all function options on int
    number = 4
    int_example(number)
    int_example(number)
    int_example(number)
    number = 0
    int_example(number)
    int_example(number)
    number = -8
    int_example(number)
    int_example(number)

    # test function with several numbers of arguments
    var = 25
    int_example2(number, var)
    int_example2(var, number)
    var = -25
    int_example2(var, number)

    # test the function on different type on variables
    var = 33.86
    float_example(var)
    float_example(var)

    # note that the calc for string and int/float are 2 different things
    var = "26.33"
    string_example(var)
    string_example(var)



