class List(list):
    def __getitem__(self, args):
        if type(args) is int:
            return super().__getitem__(args)
        if len(args) >= 1:
            ret = super().__getitem__(args[0])
            for i in range(1, len(args)):
                ret = ret[args[i]]
            return ret

    def __setitem__(self, args, value):
        if type(args) is int:
            super().__setitem__(args, value)
        elif len(args) >= 1:
            ret = super().__getitem__(args[0])
            for i in range(1, len(args)-1):
                ret = ret[args[i]]
            ret[args[-1]] = value


if __name__ == '__main__':

    l = List()
    print(l)
    l2 = []
    l = List(l2)
    print(l)

    l = List([
        [],
        [[], []],
        [[], [], []]
    ])

    # # show prints
    # print(l)
    # print(l[0])
    # print(l[1])
    # print(l[2])
    
    # # building our own self List
    # # add values and print them
    # # int value
    # l[0] = 5
    # print(l[0])
    # print(l)
    # l[0] = [-5]
    # print(l[0])
    # print(l)
    # l[0] = [5, 0, 3]
    # print(l[0])
    # print(l)
    #
    # # adding float value and insert list of lists (multi dimensions
    # l[1] = 5.2
    # print(l[1])
    # print(l)
    # l[1] = [9.4]
    # print(l[1])
    # print(l)
    # l[1] = [7.7, 0.2, -4.5]
    # print(l[1])
    # print(l)
    # l[1] = [l[1], l[0]]
    # print(l[1])
    # print(l)
    #
    # # add string values
    # l[2] = "matan"
    # print(l[2])
    # print(l)
    # l[2] = ["matan", "guy"]
    # print(l[2])
    # print(l)
    # l[2] = [["matan", -1.5], [], ["1", ["inside list"], 999]]

    l = List([
        [5, 0, 3],
        [[7.7, 0.2, -4.5], [5, 0, 3]],
        [["matan", -1.5], [], ["1", ["inside list", "second place"], 999]]
    ])
    print(l)

    # prints
    print(l[0, 2])
    print(l[1, 1])
    print(l[2, 1])
    print(l[1, 0, 0])
    print(l[2, 0, 1])
    print(l[2, 2])
    print(l[2, 2, 1])
    print(l[2, 2, 1, 1])
    print(l)

    # changing values inside the multi list (List)
    l[0, 2] = [3, 3]
    l[1, 1] = "503"
    l[2, 1] = -0.5
    l[1, 0, 0] = ["nir"]
    l[2, 0, 1] = [[[]]]
    l[2, 2] = [1.5, [-1.5]]
    l[2, 2, 1] = [[1, -.9, "multi type list"], []]
    l[2, 2, 1, 1] = 7
    print(l)
