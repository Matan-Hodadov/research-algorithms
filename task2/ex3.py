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
    l = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
    ])
    l[0, 0, 0] = [1, 1, 1, 1, 1]
    print(l)
