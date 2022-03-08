from collections.abc import Iterable


# only if we save the wanted output and not only print him
def tests():
    x = {}
    print_sorted(print_sorted(x) == "")
    x = ()
    print_sorted(print_sorted(x) == "")
    x = []
    print_sorted(print_sorted(x) == "")
    x = 1
    print_sorted(print_sorted(x) == 1)
    x = "hey"
    print_sorted(print_sorted(x) == "hey")
    x = [1, 7, "c", {"y", "b"}, 2, "a"]
    print_sorted(print_sorted(x) == print_sorted(x.reverse()))


def print_sorted(x):
    # check the type of x
    if type(x) in (list, tuple):
        # sort x as needed
        x = sorted(x, key=lambda x: str(x))
        # go through x items
        for i in x:
            # if i is complex (need to be sorted as well)
            if type(i) in (dict, set, list, tuple):
                print_sorted(i)
            else:
                print(i)
    # if the type of x is dict
    elif type(x) is dict:
        l = [i for i in x]
        # sort l
        l = sorted(l, key=lambda x: str(x))
        # go through the keys is l
        for key in l:
            # if its a complex type
            if type(x[key]) in (dict, set, list, tuple):
                print(key, ":")
                # sort the value (the item) that we want to sort (inside loop)
                print_sorted(x[key])
            else:
                print(key, ":", x[key])
    # if x's type is set just convert him to list and send him again to the function
    elif type(x) is set:
        print_sorted(list(x))
    # print(x)


if __name__ == "__main__":
    print("first example")
    x = {"a": 5, "c": 6, "b": (1, 3, 4, 2)}
    print_sorted(x)
    print("second example")
    x = [1, 7, "c", {"y", "b"}, 2, "a"]
    print_sorted(x)
    print("third example")
    x = ("hey", 7, "c", {"4", "b"}, 2, [-1, 0])
    print_sorted(x)
