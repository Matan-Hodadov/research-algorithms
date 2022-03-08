import sys


class FuncRecord:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.doc = func.__doc__
        if self.doc is not None:
            self.doc = self.doc.replace("\n", "<br>")
        else:
            self.doc = ""
        self.annotations = func.__annotations__
        if "return" in self.annotations:
            del self.annotations["return"]
        self.annotations = str([i + "<br>" for i in self.annotations]).replace("'", "").replace(",", "")[1:-1]

    def build(self):
        block = \
f'''
        <p>
            <h1> Function {self.name}: </h1>
            {self.doc} <br>
            {self.annotations}  
        </p>
'''
        return block


def filter_func(obj_name):
    obj = eval("imp." + obj_name)
    if type(obj).__name__ == "function":
        if len(obj_name) <= 4:
            return True
        elif obj_name[:2] != '__' and obj_name[-2:] != '__':
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    imp = __import__(sys.argv[1][:-3])
    functions = list(filter(filter_func, dir(imp)))
    text = "<html>\n\t<body>"
    for func in functions:
        func_record = FuncRecord(eval("imp." + func))
        text += func_record.build()
    text += "\n\t</body>\n</html>"
    # print(text)

    new_file_name = sys.argv[2]
    file = open(new_file_name, "w")
    file.write(text)
    file.close()


